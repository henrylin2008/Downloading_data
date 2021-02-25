import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)   # next line from the file (file header)
    # print(header_row)   # ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header) # 0 STATION /n 1 NAME /n...

    # Get high temperatures from this file.
    highs = []
    for row in reader:
        high = int(row[5])  # convert data from string to integer
        highs.append(high)
    print(highs)    # [62, 58, 70, 70, 67,...]



