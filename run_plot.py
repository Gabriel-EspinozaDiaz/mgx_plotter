import matplotlib.pyplot as plt
import pandas as pd
import regex as re
import sample
# import os # For when I can automate this

d1s6 = pd.read_csv('heatmaps/1_6_heatmap.csv',)

d1s6.plot.scatter(x='Label',y='Value')

sample6 = []
for n in range (1,5):
    filename = 'heatmaps/' + str(n)+'_6_heatmap.csv'
    readin = pd.read_csv(filename)
    timestamp = sample.Timestamp('day' + str(n),readin)
    sample6.append(timestamp)

test_sample = sample.Sample(sample6)

test_sample.growth_plot()


