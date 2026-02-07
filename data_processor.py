def data_conversion(data):
    
    year_col=list(filter(lambda y: y.isdigit(), data[0].keys()))
    
    return[
        {
            "Country":row["Country Name"],
            "Region":row["Continent"],
            "Year":int(year),
            "Values": float(row[year])
            if row[year]
            else None
        }
        
        for row in data
        for year in year_col
        if row[year]!=""
    ]

def clean_data(data):
    return list(filter(lambda col: col["Value"] is not None, data))

def region_filter(data, regions):
    return list(filter(lambda col:col["Region"] in regions,data ))

def year_filter(data, year):
    return list(filter(lambda col:col["Year"]==year,data ))

def country_filter(data, countries):
    return list(filter(lambda col:col["Country"] in countries,data ))
