import MyPlotFunction
import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


dataFilename = "data/All_three_exp_conditions_3.csv"
figFilename = "figures/absSpeedVsSpikesV1.png"
data = pd.read_csv(dataFilename, index_col=0)

print(data.columns.values)
# 'Expt #', 'Cell #', 'Speed', 'Bin(i)', 'Bin(i+1)', 'Bin(i+2)', 'Bin(i+3)',
# 'Bin(i+4)', 'Bin(i+5)', 'Trial Condition', 'Region', 'Layer', 'Cell Type'

trialConditions = data.loc[:, "Trial Condition"].unique()
print(trialConditions)
# ['Vestibular' 'VisVes' 'Visual']

regions = data.loc[:, "Region"].unique()
print(regions)
# ['SUB' nan 'V1' 'SC' 'RSPg' 'RSPd' 'Hip']

# We will make a figure with len(trialConditions)==3 panels
f, axes = plt.subplots(1, len(trialConditions), sharey=True)
MyPlotFunction.plot_panel(data, axes, 0, "Vestibular","Vestibular")
MyPlotFunction.plot_panel(data,axes, 1, "VisVes","Visual and Vestibular")
MyPlotFunction.plot_panel(data, axes, 2, "Visual","Visual")

MyPlotFunction.mySavefig(figFilename)

f.show()