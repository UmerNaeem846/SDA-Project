from typing import List
import matplotlib.pyplot as plt #type:ignore


from typing import List


class ConsoleWriter:

    def write(self, records: List[dict]) -> None:
        try:
            print("\n" + "=" * 70)
            print("🌍 GDP ANALYSIS REPORT".center(70))
            print("=" * 70)

            for section in records:
                for title, data in section.items():

                    print("\n" + "-" * 70)
                    print(f"📊 {title}".upper())
                    print("-" * 70)

                    if isinstance(data, list):

                        if not data:
                            print("No data available.")
                            continue

                        # If list of dictionaries (countries)
                        if isinstance(data[0], dict):
                            for item in data:
                                country = item.get("country", "N/A")
                                gdp = item.get("gdp", "N/A")
                                year = item.get("year", "")

                                if year:
                                    print(f"{country:<25} | Year: {year:<6} | GDP: {gdp:,.2f}")
                                else:
                                    print(f"{country:<25} | GDP: {gdp:,.2f}")

                        else:
                            # Simple list (like decline countries)
                            for item in data:
                                print(f"- {item}")

                    elif isinstance(data, dict):
                        for key, value in data.items():
                            print(f"{key:<20} : {value:,.2f}")

                    else:
                        print(data)

            print("\n" + "=" * 70)
            print("END OF REPORT".center(70))
            print("=" * 70 + "\n")

        except Exception as e:
            print(f"[ERROR] Failed while printing to console: {e}")
            raise




class GraphicsChartWriter:

    def write(self, records: List[dict]) -> None:
        try:

            for record in records:
                for title, dataset in record.items():

                    if isinstance(dataset, list) and dataset and isinstance(dataset[0], dict):

                        names = list(map(lambda x: x["country"], dataset))
                        values = list(map(lambda x: float(x["gdp"]), dataset))

                        plt.figure(figsize=(10, 6))
                        plt.bar(names, values, color="steelblue")
                        plt.title(title, fontsize=14)
                        plt.xticks(rotation=45)
                        plt.xlabel("Country")
                        plt.ylabel("GDP")
                        plt.tight_layout()
                        plt.show()

                    elif isinstance(dataset, dict) and all(isinstance(k, int) for k in dataset.keys()):

                        years = list(dataset.keys())
                        values = list(dataset.values())

                        plt.figure(figsize=(10, 6))
                        plt.plot(years, values, marker="o", color="green")
                        plt.title(title, fontsize=14)
                        plt.xlabel("Year")
                        plt.ylabel("Total GDP")
                        plt.grid(True)
                        plt.tight_layout()
                        plt.show()

                    elif "Contribution" in title and isinstance(dataset, dict):

                        labels = list(dataset.keys())
                        values = list(dataset.values())

                        plt.figure(figsize=(8, 8))
                        plt.pie(values, labels=labels, autopct='%1.1f%%')
                        plt.title(title, fontsize=14)
                        plt.tight_layout()
                        plt.show()

                    elif "Growth Rate" in title and isinstance(dataset, dict):

                        countries = list(dataset.keys())
                        growths = list(dataset.values())

                        plt.figure(figsize=(12, 6))
                        plt.bar(countries, growths, color="orange")
                        plt.title(title, fontsize=14)
                        plt.xticks(rotation=45)
                        plt.xlabel("Country")
                        plt.ylabel("Growth Rate (%)")
                        plt.axhline(0, color='black', linewidth=0.8)
                        plt.tight_layout()
                        plt.show()

                    elif "Fastest Growing Continent" in title:

                        plt.figure(figsize=(6, 4))
                        plt.text(0.5, 0.5, dataset,
                                 fontsize=18,
                                 ha='center')
                        plt.title(title, fontsize=14)
                        plt.xticks([])
                        plt.yticks([])
                        plt.tight_layout()
                        plt.show()

                    elif "Average GDP" in title and isinstance(dataset, dict):

                        labels = list(dataset.keys())
                        values = list(dataset.values())

                        plt.figure(figsize=(8, 6))
                        plt.bar(labels, values, color="purple")
                        plt.title(title, fontsize=14)
                        plt.xlabel("Continent")
                        plt.ylabel("Average GDP")
                        plt.tight_layout()
                        plt.show()

                    elif "Decline" in title and isinstance(dataset, list):

                        plt.figure(figsize=(6, 4))

                        text_data = "\n".join(dataset) if dataset else "None"

                        plt.text(0.5, 0.5, text_data,
                                 ha='center',
                                 fontsize=12)

                        plt.title(title, fontsize=14)
                        plt.xticks([])
                        plt.yticks([])
                        plt.tight_layout()
                        plt.show()

        except Exception as e:
            print(f"[ERROR] Failed while generating charts: {e}")
            raise