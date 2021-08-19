from elloite_method import *

# This method is easy to use the only thing is to input the stock ID from yahoo finance and select the time period you need

# example ID for Dow Jones Industrial Average Index
stock_id = "^DJI"
time_period_year = 1

Elloite_plot(stock_id, start_date=datetime.date.today().replace(datetime.date.today().year - time_period_year), tick=3)