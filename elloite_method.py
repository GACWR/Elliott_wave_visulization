#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------#
"""
File name: elloite_method.py
Author: MAX KUAN
Date created: 19/8/2021
Date last modified: 19/8/2021
Version: 0.1.0
Python Version: 3.8.8
Status: Developing
"""
#--------------------------------#

import math
import mplfinance as mpf
import pandas as pd
import matplotlib
import pandas_datareader as pdr
import numpy as np
import datetime


def turnover(data, tick=3):
    """This method calculate the turnover point of a wave"""
    
    data.columns = [i.lower() for i in data.columns]

    for index, row in data.iterrows():

        try:
            if (data.high[index -tick : index] < row["high"]).any() and (row["high"] >= data.high[index:index + tick]).all() and (row["low"] > data.close[index:index + tick]).any() :
                data.at[index, "turnover"] = "+"

            elif (data.low[index-tick:index] > row["low"]).any() and (row["low"] <= data.low[index:index + tick]).all() and (row["high"] < data.close[index:index + tick]).any() :
                data.at[index, "turnover"] = "*"

            else:
                data.at[index, "turnover"] = "-"

        except:
            pass

    return data

def make_plot(df, title, tick):
    """This function generate the plot for a specific stock"""

    sample = []
    line = []
    switch = 0

    for index, row in df.iterrows():
        if row["turnover"] == "+" and switch == 0:
            sample.append(row["high"] * 1.001)
            line.append((index, row["high"]))
            switch = 1

        elif row["turnover"] == "*" and switch == 1:
            sample.append(row["low"] * 0.999)
            line.append((index, row["low"]))
            switch = 0
        else:
            sample.append(np.nan)
    
    turnover_point = line

    style = mpf.make_marketcolors(
        up='tab:red', down='tab:green'
    )

    build_style = mpf.make_mpf_style(marketcolors=style)

    apd = mpf.make_addplot(sample,type='scatter')
    mpf.plot(
        df,
        addplot=apd, 
        type='candle', 
        style=build_style,
        alines=line,
        title=f"Stock ID:{title}, Tick:{tick}",
        figsize=(60,30))
    
    return turnover_point


def Elloite_plot(stock_code, start_date, tick=4):
    """This is the main function for create a Elloite plot"""
    
    data = pdr.DataReader(stock_code, "yahoo", start=start_date).reset_index()

    df = turnover(data, tick=tick)

    df.index = pd.to_datetime(df.date)
    
    df = df.drop(columns=["date"])

    turnover_point = make_plot(df, stock_code, tick)

if __name__ == "__main__":
    pass


    


