import pandas as pd
import matplotlib.pyplot as plt
import csv
from itertools import islice


#seting starting parameters
start_date = '02.12.2021' #input("Input date of start ")
start_hour = '10:15:00' #input("Input hour of start ")
end_hour = '10:16:00' #input("Input hour of end ")
start_date = start_date[:6]+start_date[8:] # converting 02.12.2021 to 02.21.21 format
path = r"C:\Users\Lenovo\Kolo naukowe\Dane.csv" #csv file path


#converting 00:00:00 hour int seconds
def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

#drawing graph
def grap_drawer(graph_end_row, graph_start_row, path):
    df = pd.read_csv(path)
    df.drop(df.index[graph_end_row:], inplace=True)
    df.drop(df.index[:graph_start_row], inplace=True)
    df['ETCO2'] = df['ETCO2'].astype(str).astype(int)
    plt.plot(df['ETCO2'], color='r')
    plt.ylabel('ETCO2')
    #plt.xticks(np.arange(0, 177220, step=100))
    plt.show()

#returning intervals when CO2 concentration is below/under certain value
def sample_intervals(max_value, operator, path, graph_start_row, graph_end_row, frequency):
    sample = 0
    samples_list = []
    with open(path) as df:
        f = csv.reader(df)
        for row in islice(f, graph_start_row, graph_end_row):
            if eval('int(row[3]) {} max_value'.format(operator)):
                sample += 1
            else:
                if sample != 0:
                    samples_list.append(sample*frequency)
                    sample = 0
    return samples_list


if __name__ == "__main__":
    max_value = 0
    line_number = 0

    #opening file, and finding heading nearest given date and hour
    with open(path) as df:
        f = csv.reader(df)
        for row in f:
            line_number += 1
            if start_date in row and get_sec(row[6]) < get_sec(start_hour):
                accurate_row = row
                i = line_number

    frequency = int(accurate_row[4]) #finding frequency(5th parameter in heading line)
    #first row of interval
    graph_start_row = i + (get_sec(start_hour) - get_sec(accurate_row[6])) * frequency
    # last row of interval
    graph_end_row = graph_start_row + (get_sec(end_hour) - get_sec(start_hour)) * frequency

    #finding the max value of CO2 concentration in above interval
    with open(path) as df:
        f = csv.reader(df)
        for row in islice(f, graph_start_row, graph_end_row):
            if int(row[3]) > max_value:
                max_value = int(row[3])
    max_value = 0.2*max_value

    print('Time intervals (in seconds) when the CO2 concentration is below', max_value)
    print(sample_intervals(max_value, ">", path, graph_start_row, graph_end_row, frequency))
    print('Time intervals (in seconds) when the CO2 concentration is under', max_value)
    print(sample_intervals(max_value, "<", path, graph_start_row, graph_end_row, frequency))
    grap_drawer(graph_end_row, graph_start_row, path)



