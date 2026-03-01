import json
import os
from core.engine import TransformationEngine
from plugins.inputs import CsvReader, JsonReader
from plugins.outputs import ConsoleWriter, GraphicsChartWriter


INPUT_DRIVERS = {
    "csv": CsvReader,
    "json": JsonReader
}

OUTPUT_DRIVERS = {
    "console": ConsoleWriter,
    "chart": GraphicsChartWriter
}


def load_config(config_path: str) -> dict:
    if not os.path.exists(config_path):
        raise FileNotFoundError("config.json not found")

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        required_keys = [
            "input_type",
            "output_type",
            "file_path",
            "continent",
            "start_year",
            "end_year",
            "decline_years"
        ]

        for key in required_keys:
            if key not in config:
                raise KeyError(f"Missing required config key: {key}")

        return config

    except json.JSONDecodeError:
        raise ValueError("Invalid JSON in config file")


def bootstrap():
    try:
        config = load_config("config.json")

        # Validate drivers
        if config["input_type"] not in INPUT_DRIVERS:
            raise ValueError("Unsupported input type")

        if config["output_type"] not in OUTPUT_DRIVERS:
            raise ValueError("Unsupported output type")

        # 1️⃣ Instantiate Output
        sink_class = OUTPUT_DRIVERS[config["output_type"]]
        sink = sink_class()

        # 2️⃣ Instantiate Core Engine (Dependency Injection)
        engine = TransformationEngine(
            sink=sink,
            continent=config["continent"],
            start_year=int(config["start_year"]),
            end_year=int(config["end_year"]),
            decline_years=int(config["decline_years"])
        )

        # 3️⃣ Instantiate Input (Inject Core)
        input_class = INPUT_DRIVERS[config["input_type"]]
        reader = input_class(config["file_path"], engine)

        # 4️⃣ Run system
        reader.run()

    except Exception as e:
        print(f"\n[FATAL ERROR] {e}\n")


if __name__ == "__main__":
    bootstrap()