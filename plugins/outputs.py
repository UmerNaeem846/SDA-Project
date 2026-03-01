class ConsoleWriter:
    def write(self, records: list[dict]) -> None:
        for record in records:
            print(f"DEBUG: {record}")
