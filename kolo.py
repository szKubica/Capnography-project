import pandas as pd
import matplotlib.pyplot as plt
import csv


start_date = '02.12.2021' #input("Input date of start ")
start_hour = '10:15:00' #input("Input hour of start ")
end_hour = '10:16:00' #input("Input hour of end ")
start_date = start_date[:6]+start_date[8:] # coonverting 02.12.2021 to 02.21.21 format
path = r"C:\Users\Lenovo\Kolo naukowe\Dane1.csv"

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def grap_drawer(graph_end_row, graph_start_row, path):
    df = pd.read_csv(path)
    df.drop(df.index[graph_end_row:], inplace=True)
    df.drop(df.index[:graph_start_row], inplace=True)
    df['ETCO2'] = df['ETCO2'].astype(str).astype(int)
    plt.plot(df['ETCO2'], color='r')
    plt.ylabel('ETCO2')
    plt.xticks([])
    plt.show()


line_number=0
with open(path) as df:
    f = csv.reader(df)
    for row in f:
        line_number += 1
        if start_date in row and get_sec(row[6]) < get_sec(start_hour):
            accurate_row = row
            print(row, line_number)
            i = line_number

    survey_start = get_sec(accurate_row[6])
    frequency = int(accurate_row[4])

    print(survey_start, frequency, 'Line number', i)

    graph_start_row = i+(get_sec(start_hour)-get_sec(accurate_row[6]))*frequency
    graph_end_row = graph_start_row + (get_sec(end_hour)-get_sec(start_hour))*frequency
    print(graph_start_row)
    print(graph_end_row)
    grap_drawer(graph_end_row, graph_start_row, path)
