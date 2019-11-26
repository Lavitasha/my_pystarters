
# import ipdb
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

    ### Start first panel
def plot_panel(data,axis,trialCondition,title):
    # Extract the subset of the data corresponding to vestibular-only stimulation
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"]==trialCondition) & (data["Region"]=="V1"),:]

    # Plot the spikes counts in Bin(i) as a function of the absolute value of
    # the stimulation speed
    axes[axis].scatter(x=abs(dataSubset["Speed"]), y=dataSubset["Bin(i)"], c="lightgray")
    axes[axis].set_title(title)

    # Estimate the regression line
    regressors = sm.add_constant(abs(dataSubset["Speed"]))
       # fit.params contains the regression coefficients
       # fit.pvalues contains the regression coefficients pvalues
    fit = sm.OLS(endog=dataSubset["Bin(i)"], exog=regressors).fit()

    # Plot the regression line
    legend = "p={:.4f}".format(fit.pvalues[1])
    axes[axis].plot(abs(dataSubset["Speed"]), fit.params[0]+abs(dataSubset["Speed"])*fit.params[1], color="red", label=legend)
    axes[axis].legend(loc="upper left")

    axes[axis].set_title(title)
    axes[axis].set_xlabel("Abs(Speed)")
    axes[axis].set_ylabel("Spike Count")


plot_panel(data, 0, "Vestibular","Vestibular")
plot_panel(data, 1, "VisVes","Visual and Vestibular")
plot_panel(data, 2, "Visual","Visual")

plt.savefig(figFilename)

f.show()

