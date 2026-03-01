from typing import List, Any, Dict
from .contracts import DataSink
from . import analytics
from operator import itemgetter


class TransformationEngine:

    def __init__(
        self,
        sink: DataSink,
        continent: str,
        start_year: int,
        end_year: int,
        decline_years: int
    ):
        self.sink = sink
        self.continent = continent
        self.start_year = start_year
        self.end_year = end_year
        self.decline_years = decline_years


    # Pure Normalization (No loops)
    def normalize_data(self, raw_data: List[Any]) -> List[Dict]:

        def extract_year_records(row):

            # Get only year columns (numbers)
            year_columns = list(
                filter(lambda key: key.isdigit(), row.keys())
            )

            return list(
                map(
                    lambda year: {
                        "country": row["Country Name"],
                        "continent": row["Continent"],
                        "year": int(year),
                        "gdp": float(row[year]) if row[year] else 0.0
                    },
                    year_columns
                )
            )

        # Map each row → list of year records
        mapped = list(map(extract_year_records, raw_data))

        # Flatten list of lists
        return [record for sublist in mapped for record in sublist]      

    
    # Execute Pipeline
    def execute(self, raw_data: List[Any]) -> None:
        try:

            data = self.normalize_data(raw_data)

            if not data:
                raise ValueError("No valid data after normalization.")

            continent_data = analytics.filter_by_continent(
                data, self.continent
            )

            ranged_data = analytics.filter_by_year_range(
                continent_data,
                self.start_year,
                self.end_year
            )

            if not ranged_data:
                raise ValueError("No data found for given continent and year range.")


            results = [

                {
                    "Top 10 Countries by GDP":
                    analytics.top_n_by_gdp(ranged_data)
                },

                {
                    "Bottom 10 Countries by GDP":
                    analytics.bottom_n_by_gdp(ranged_data)
                },

                {
                    "GDP Growth Rate of Each Country":
                    analytics.growth_rate_by_country(ranged_data)
                },

                {
                    "Average GDP by Continent (Range)":
                    analytics.average_gdp_by_continent_range(ranged_data)
                },

                {
                    "Total Global GDP Trend":
                    analytics.total_global_trend(ranged_data)
                },

                {
                    "Fastest Growing Continent":
                    analytics.fastest_growing_continent(
                        analytics.filter_by_year_range(
                            data,
                            self.start_year,
                            self.end_year
                        )
                    )
                },

                {
                    "Countries with Consistent GDP Decline":
                    analytics.countries_with_decline(
                        continent_data,
                        self.decline_years
                    )
                },

                {
                    "Contribution of Each Continent to Global GDP":
                    analytics.continent_contribution(
                        analytics.filter_by_year_range(
                            data,
                            self.start_year,
                            self.end_year
                        )
                    )
                }

            ]

            # Step 5: Send to Sink
            self.sink.write(results)

        except Exception as e:
            print(f"[FATAL ERROR] {e}")
            raise