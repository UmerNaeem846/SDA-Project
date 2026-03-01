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

        def transform(row):
            try:
                return {
                    "country": row["Country Name"],
                    "continent": row["Continent"],
                    "year": int(row["Year"]),
                    "gdp": float(row["Value"])
                }
            except (KeyError, ValueError):
                return None

        return list(
            filter(
                lambda r: r is not None and analytics.validate_record(r),
                map(transform, raw_data)
            )
        )

    
    # Execute Pipeline
    def execute(self, raw_data: List[Any]) -> None:

        data = self.normalize_data(raw_data)

        continent_data = analytics.filter_by_continent(
            data, self.continent
        )

        ranged_data = analytics.filter_by_year_range(
            continent_data,
            self.start_year,
            self.end_year
        )

        results = list(filter(None, [
            {
                "Top 10 Countries":
                analytics.top_n_by_gdp(ranged_data)
            },
            {
                "Bottom 10 Countries":
                analytics.bottom_n_by_gdp(ranged_data)
            },
            {
                "Average GDP by Continent":
                analytics.average_gdp_by_continent(data)
            },
            {
                "Global GDP Trend":
                analytics.total_global_trend(data)
            },
            {
                "Countries with Consistent Decline":
                analytics.countries_with_decline(
                    continent_data,
                    self.decline_years
                )
            }
        ]))

        self.sink.write(results)