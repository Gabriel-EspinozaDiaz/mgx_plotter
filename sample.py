import matplotlib.pyplot as plt
import pandas as pd
import regex as re
import statsmodels.api as sm
from statsmodels.formula.api import ols
import scipy.stats as stats

class Timestamp:
    def __init__(self,name: str,mapDf: pd.DataFrame):
        self.name = name
        self.cellnumber = len(mapDf)
        self.heatmap = mapDf
        self.average = mapDf['Value'].mean()
        self.area = 0
        self.sDev = mapDf.std()
        self.timepoint = re.match(r'^\d+_',name)
        for area in mapDf['Value']:
            self.area += area
            
    # Getter Functions
    def get_average(self):
        return self.average 
    def get_timepoint(self):
        return self.timepoint
    def get_standard_deviation(self):
        return self.sDev
    def get_cell_number(self):
        return self.cellnumber
    def get_area(self):
        return self.area

class Sample:
    def __init__(self,timestamps: list[Timestamp]):
        self.timestamps = timestamps
        self.days = len(timestamps)
        self.daylist = []
        self.cellnumbers = []
        self.averages = []
        self.areas = []
        self.sDevs = []
        for n in range(self.days):
            self.daylist.append(n+1)
            self.cellnumbers.append(timestamps[n].get_cell_number())
            self.averages.append(timestamps[n].get_average())
            self.areas.append(timestamps[n].get_area())
            self.sDevs.append(timestamps[n].get_standard_deviation)

    def one_way_anova(self):
        print(stats.f_oneway(self.daylist))

    def two_way_anova(self):
        adjusted_areas = self.areas
        print(sm.stats.anova_lm(ols('day ~ size',data=self.areas).fit(), typ=1))

    # Plotting Functions
    def growth_chart(self,title='Number of Cells Present in Tissue Sample Over Time'):
        fig, ax = plt.subplots()
        xticks = range(min(self.daylist), max(self.daylist) + 1)
        ax.set_xticks(xticks)
        plt.bar(self.daylist,self.cellnumbers)
        plt.title(title)
        plt.xlabel('Time (days)')
        plt.ylabel('Number of Cells')
        plt.show()

    def cell_size_chart(self,title='Average Cell Size Over Time'):
        fig, ax = plt.subplots()
        xticks = range(min(self.daylist), max(self.daylist) + 1)
        ax.set_xticks(xticks)
        plt.bar(self.daylist,self.averages)
        plt.title(title)
        plt.xlabel('Time (days)')
        plt.ylabel(r'Average Cell Size ($\mu$m$^2$)')
        plt.show()

    def total_area_chart(self,title='Total Surface Area of Sample Over Time'):
        fig, ax = plt.subplots()
        xticks = range(min(self.daylist), max(self.daylist) + 1)
        ax.set_xticks(xticks)
        plt.bar(self.daylist,self.areas)
        plt.title(title)
        plt.xlabel('Time (days)')
        plt.ylabel(r'Total Area ($\mu$m$^2$)')
        plt.show()

    def total_area_plot(self,title='Total Surface Area of Sample Over Time'):
        fig, ax = plt.subplots()
        xticks = range(min(self.daylist), max(self.daylist) + 1)
        ax.set_xticks(xticks)
        plt.plot(self.daylist,self.areas)
        plt.title(title)
        plt.xlabel('Time (days)')
        plt.ylabel(r'Total Area ($\mu$m$^2$)')
        plt.show()
