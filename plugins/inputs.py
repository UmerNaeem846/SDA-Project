import csv
import json
import os
from core.contracts import PipelineService


class CsvReader:
    def __init__(self, file_path: str, service: PipelineService):
        self.file_path = file_path
        self.service = service

    def run(self) -> None:
        # Check if file exists
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"CSV file not found: {self.file_path}")

        try:
            with open(self.file_path, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                data = list(reader)

            if not data:
                raise ValueError("CSV file is empty")

            self.service.execute(data)

        except Exception as e:
            print(f"[ERROR] Failed to process CSV file: {e}")
            raise


class JsonReader:
    def __init__(self, file_path: str, service: PipelineService):
        self.file_path = file_path
        self.service = service

    def run(self) -> None:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"JSON file not found: {self.file_path}")

        try:
            with open(self.file_path, encoding="utf-8") as f:
                data = json.load(f)

            if not data:
                raise ValueError("JSON file is empty")

            self.service.execute(data)

        except json.JSONDecodeError:
            print("[ERROR] Invalid JSON format")
            raise
        except Exception as e:
            print(f"[ERROR] Failed to process JSON file: {e}")
            raise