import csv

def gdb_data(file_path):
    try:
        with open(file_path,newline='',encoding='utf-8') as file:
            loader=csv.DictReader(file) # Make the Dictionary like Key value pair(colunm and their value pair)
            return list(loader) #List of Dictinaries
    except FileNotFoundError:
        raise Exception("GDP CSV File not found")
    
