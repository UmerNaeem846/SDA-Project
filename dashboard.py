import matplotlib.pyplot as plt
from collections import defaultdict

def show_dashboard(config, data, result):
    
    print("\n===== GDP ANALYTICS DASHBOARD =====")
    print(f"Region      : {config['region']}")
    print(f"Year        : {config['year']}")
    print(f"Operation   : {config['operation'].upper()}")
    print(f"Result GDP  : {result:.2f}")
    print("=================================\n")

    #Generate charts
    region_wise_plot(data)
    year_wise_plot(data)


def region_wise_plot(data):
    
    #Sum GDP per region
    region_totals = defaultdict(float)
    for row in data:
        region_totals[row["Region"]] += row["Value"]

    regions = list(region_totals.keys())
    values = list(region_totals.values())

    #Bar Chart
    plt.figure()
    plt.bar(regions, values, color='skyblue')
    plt.title("Region-wise GDP (Bar Chart)")
    plt.xlabel("Region")
    plt.ylabel("GDP Value")
    plt.show()

    #Pie Chart
    plt.figure()
    plt.pie(values, labels=regions, autopct="%1.1f%%", startangle=140)
    plt.title("Region-wise GDP Distribution (Pie Chart)")
    plt.show()


def year_wise_plot(data):
    
    years = list(map(lambda x: x["Year"], data))
    values = list(map(lambda x: x["Value"], data))

    #Line Graph
    plt.figure()
    plt.plot(years, values, marker="o", linestyle='-', color='green')
    plt.title("Year-wise GDP Trend (Line Graph)")
    plt.xlabel("Year")
    plt.ylabel("GDP Value")
    plt.show()

    #Histogram
    plt.figure()
    plt.hist(values, bins=10, color='orange', edgecolor='black')
    plt.title("GDP Distribution (Histogram)")
    plt.xlabel("GDP Value")
    plt.ylabel("Frequency")
    plt.show()
