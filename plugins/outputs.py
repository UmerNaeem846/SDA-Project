from typing import List
import matplotlib.pyplot as plt #type:ignore


class ConsoleWriter:
    def write(self, records: List[dict]) -> None:
        try:
            print("\n========== GDP ANALYSIS RESULTS ==========\n")

            for record in records:
                print(record)

            print("\n==========================================\n")

        except Exception as e:
            print(f"[ERROR] Failed while printing to console: {e}")
            raise


class GraphicsChartWriter:
    def write(self, records: List[dict]) -> None:
        try:
            for record in records:
                for title, dataset in record.items():

                    if not isinstance(dataset, list):
                        continue

                    names = []
                    values = []

                    for item in dataset:
                        if "country" in item and "gdp" in item:
                            names.append(item["country"])
                            values.append(float(item["gdp"]))

                    if not names:
                        continue

                    plt.figure()
                    plt.bar(names, values)
                    plt.title(title)
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()

        except Exception as e:
            print(f"[ERROR] Failed while generating charts: {e}")
            raise