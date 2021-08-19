# Elliott Wave Principle Visulization

This tool provide a quick way to identify the wave pattern of stock or indices.

## Description
The Elliott wave principle was introduced by Ralph Nelson Elliott in 1938, including impulse wave and corrective wave.
However, it is not easy to identify the pattern at first sight. Hence, this project focus on automatically applies the principle on stock and indices.

## Requirement
- mplfinance==0.12.7a17
- pandas-datareader==0.10.0

## Usage
```python
from elloite_method import *

# Select the stock ID or indices you are interesting in from yahoo finance
stock_id = "^DJI"

# Choose the time period (year) you want to observe
time_period_year = 1

# Output the plot
Elloite_plot(stock_id, start_date=datetime.date.today().replace(datetime.date.today().year - time_period_year), tick=3)
```
