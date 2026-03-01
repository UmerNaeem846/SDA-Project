from typing import List, Dict
from functools import reduce
from itertools import groupby
from operator import itemgetter



# Validation
def validate_record(record: Dict) -> bool:
    required = {"country", "continent", "year", "gdp"}
    return required.issubset(record.keys())



# Filtering
def filter_by_continent(data: List[Dict], continent: str) -> List[Dict]:
    return list(filter(lambda d: d["continent"] == continent, data))


def filter_by_year_range(data: List[Dict], start: int, end: int) -> List[Dict]:
    return list(
        filter(lambda d: start <= d["year"] <= end, data)
    )



# Sorting
def top_n_by_gdp(data: List[Dict], n: int = 10) -> List[Dict]:
    return sorted(data, key=itemgetter("gdp"), reverse=True)[:n]


def bottom_n_by_gdp(data: List[Dict], n: int = 10) -> List[Dict]:
    return sorted(data, key=itemgetter("gdp"))[:n]



# Aggregations
def average_gdp_by_continent(data: List[Dict]) -> Dict[str, float]:

    sorted_data = sorted(data, key=itemgetter("continent"))

    grouped = groupby(sorted_data, key=itemgetter("continent"))

    return {
        continent: (
            lambda values: sum(values) / len(values)
        )(
            list(map(lambda d: d["gdp"], group))
        )
        for continent, group in grouped
    }


def total_global_trend(data: List[Dict]) -> Dict[int, float]:

    sorted_data = sorted(data, key=itemgetter("year"))

    grouped = groupby(sorted_data, key=itemgetter("year"))

    return {
        year: sum(map(lambda d: d["gdp"], group))
        for year, group in grouped
    }



# Growth
def growth_rate(records: List[Dict]) -> float:

    sorted_records = sorted(records, key=itemgetter("year"))

    if len(sorted_records) < 2:
        return 0.0

    start, end = sorted_records[0]["gdp"], sorted_records[-1]["gdp"]

    return 0.0 if start == 0 else ((end - start) / start) * 100


def countries_with_decline(data: List[Dict], years: int) -> List[str]:

    sorted_data = sorted(data, key=itemgetter("country", "year"))

    grouped = groupby(sorted_data, key=itemgetter("country"))

    def is_declining(records):
        last_years = list(records)[-years:]
        gdps = list(map(itemgetter("gdp"), last_years))
        return all(
            map(lambda pair: pair[0] > pair[1], zip(gdps, gdps[1:]))
        )

    return list(
        map(
            lambda item: item[0],
            filter(
                lambda item: is_declining(list(item[1])),
                grouped
            )
        )
    )