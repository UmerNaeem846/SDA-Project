def average_gdp_region(data):
    values = list(map(lambda col: col["Value"], data))
    return sum(values) / len(values) if values else 0

def sum_gdp_region(data):
    return sum(map(lambda col: col["Value"], data))
