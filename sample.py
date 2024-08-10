import matplotlib.pyplot as plt
import pandas as pd
import regex as re

class Timestamp:
    def __init__(self,name: str,mapDf: pd.DataFrame):
        self.name = name
        self.heatmap = mapDf
        self.average = mapDf.mean()
        self.sDev = mapDf.std()
        self.timepoint = re.match(r'^\d+_',name)

    # Getter Functions
    def get_average(self):
        return self.average 
    def get_timepoint(self):
        return self.timepoint
    def get_standard_deviation(self):
        return self.sDev


class Sample:
    def __init__(self,timestamps: list[Timestamp]):
        self.timestamps = timestamps
        self.days = len(timestamps)
        self.averages = []
        self.sDevs = []
        for n in range(self.days):
            self.averages.append(timestamps[n].get_average())
        for n in range(self.days):
            self.sDevs.append(timestamps[n].get_standard_deviation)

    # Plotting Functions
    def growth_plot(self):
        plt.plot(self.averages)
        plt.show()


    



    
