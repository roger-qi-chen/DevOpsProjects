import csv
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame


def csv_reader_read_file(filename: str):
    with open(filename) as f:
        csv_file = csv.reader(f, delimiter=',')
        for row in csv_file:
            print(row)


def pandas_read_file(filename: str):
    df = pd.read_csv(filename)
    df = df.set_index("Date")
    print(df)
    return df


def compare_trend(stocks: dict):
    df = DataFrame()
    for code, stock_df in stocks.items():
        df[code] = stock_df["Adj Close"]
    df.plot()
    plt.show()


if __name__ == '__main__':
    csv_reader_read_file("AAPL.csv")
    appl = pandas_read_file("AAPL.csv")
    team = pandas_read_file("TEAM.csv")
    compare_trend(stocks={"APPL": appl, "TEAM": team})

