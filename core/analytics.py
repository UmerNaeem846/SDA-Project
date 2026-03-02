from typing import List, Dict
from itertools import groupby
from operator import itemgetter
from functools import reduce


# VALIDATION

def validate_record(record: Dict) -> bool:
    required = {"country", "continent", "year", "gdp"}
    return required.issubset(record.keys())


# FILTERING

def filter_by_continent(data: List[Dict], continent: str) -> List[Dict]:
    return list(filter(lambda d: d["continent"] == continent, data))


def filter_by_year_range(data: List[Dict], start: int, end: int) -> List[Dict]:
    return list(filter(lambda d: start <= d["year"] <= end, data))


# TOP GDP

def top_n_by_gdp(data: List[Dict], n: int = 10) -> List[Dict]:
    return list(sorted(data, key=itemgetter("gdp"), reverse=True))[:n]


# BOTTOM GDP

def bottom_n_by_gdp(data: List[Dict], n: int = 10) -> List[Dict]:
    return list(sorted(data, key=itemgetter("gdp")))[:n]


# GDP GROWTH RATE PER COUNTRY

def growth_rate_by_country(data: List[Dict]) -> Dict[str, float]:

    sorted_data = sorted(data, key=itemgetter("country", "year"))
    grouped = groupby(sorted_data, key=itemgetter("country"))

    def compute_growth(records):
        records = list(records)
        if len(records) < 2:
            return 0.0

        start = records[0]["gdp"]
        end = records[-1]["gdp"]

        return 0.0 if start == 0 else ((end - start) / start) * 100

    return dict(
        map(
            lambda item: (item[0], compute_growth(item[1])),
            grouped
        )
    )


# AVERAGE GDP BY CONTINENT (FOR GIVEN RANGE)

def average_gdp_by_continent_range(data: List[Dict]) -> Dict[str, float]:

    sorted_data = sorted(data, key=itemgetter("continent"))
    grouped = groupby(sorted_data, key=itemgetter("continent"))

    def compute_average(records):
        records = list(records)
        total = reduce(lambda acc, d: acc + d["gdp"], records, 0)
        return total / len(records) if records else 0

    return dict(
        map(
            lambda item: (item[0], compute_average(item[1])),
            grouped
        )
    )


# TOTAL GLOBAL GDP TREND (YEARLY)

def total_global_trend(data: List[Dict]) -> Dict[int, float]:

    sorted_data = sorted(data, key=itemgetter("year"))
    grouped = groupby(sorted_data, key=itemgetter("year"))

    return dict(
        map(
            lambda item: (
                item[0],
                reduce(lambda acc, d: acc + d["gdp"], item[1], 0)
            ),
            grouped
        )
    )


# FASTEST GROWING CONTINENT

def fastest_growing_continent(data: List[Dict]) -> str:

    sorted_data = sorted(data, key=itemgetter("continent", "year"))
    grouped = groupby(sorted_data, key=itemgetter("continent"))

    def compute_growth(records):
        records = list(records)
        if len(records) < 2:
            return 0.0

        start = records[0]["gdp"]
        end = records[-1]["gdp"]

        return 0.0 if start == 0 else ((end - start) / start) * 100

    growth_map = dict(
        map(
            lambda item: (item[0], compute_growth(item[1])),
            grouped
        )
    )

    if not growth_map:
        return "No Data"

    return max(growth_map.items(), key=itemgetter(1))[0]


# COUNTRIES WITH CONSISTENT GDP DECLINE

def countries_with_decline(data: List[Dict], years: int) -> List[str]:

    sorted_data = sorted(data, key=itemgetter("country", "year"))
    grouped = groupby(sorted_data, key=itemgetter("country"))

    def is_declining(records):
        records = list(records)

        if len(records) < years:
            return False

        last_years = records[-years:]
        gdps = list(map(itemgetter("gdp"), last_years))

        return all(map(lambda p: p[0] > p[1], zip(gdps, gdps[1:])))

    return list(
        map(
            lambda item: item[0],
            filter(
                lambda item: is_declining(item[1]),
                grouped
            )
        )
    )


# CONTRIBUTION OF EACH CONTINENT TO GLOBAL GDP

def continent_contribution(data: List[Dict]) -> Dict[str, float]:

    total_global = reduce(lambda acc, d: acc + d["gdp"], data, 0)

    if total_global == 0:
        return {}

    sorted_data = sorted(data, key=itemgetter("continent"))
    grouped = groupby(sorted_data, key=itemgetter("continent"))

    return dict(
        map(
            lambda item: (
                item[0],
                (reduce(lambda acc, d: acc + d["gdp"], item[1], 0) / total_global) * 100
            ),
            grouped
        )
    )