import pandas as pd
import sample
# Imports for when this process can be automated
# import os 
# import regex as re

d1s6 = pd.read_csv('heatmaps/1_6_heatmap.csv',)


sample6 = []
for n in range (1,5):
    readin = pd.read_csv('heatmaps/' + str(n)+'_6_heatmap.csv')
    timestamp = sample.Timestamp('day' + str(n),readin)
    sample6.append(timestamp)

test_sample = sample.Sample(sample6)

test_sample.total_area_plot()


