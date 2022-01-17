import csv
import pandas as pd
import plotly.figure_factory as ff

reader = pd.read_csv("HeightWeight.csv")

fig = ff.create_distplot([reader["Weight(Pounds)"].tolist()], ["Weight"], show_hist=False)
fig.show()