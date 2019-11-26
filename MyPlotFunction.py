
# import ipdb
import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

    ### Start first panel
def plot_panel(data, axes, axis_index, trialCondition, title):
    # Extract the subset of the data corresponding to vestibular-only stimulation
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"]==trialCondition) & (data["Region"]=="V1"),:]

    # Plot the spikes counts in Bin(i) as a function of the absolute value of
    # the stimulation speed
    axes[axis_index].scatter(x=abs(dataSubset["Speed"]), y=dataSubset["Bin(i)"], c="lightgray")
    axes[axis_index].set_title(title)

    # Estimate the regression line
    regressors = sm.add_constant(abs(dataSubset["Speed"]))
       # fit.params contains the regression coefficients
       # fit.pvalues contains the regression coefficients pvalues
    fit = sm.OLS(endog=dataSubset["Bin(i)"], exog=regressors).fit()

    # Plot the regression line
    legend = "p={:.4f}".format(fit.pvalues[1])
    axes[axis_index].plot(abs(dataSubset["Speed"]), fit.params[0] + abs(dataSubset["Speed"]) * fit.params[1], color="red", label=legend)
    axes[axis_index].legend(loc="upper left")

    axes[axis_index].set_title(title)
    axes[axis_index].set_xlabel("Abs(Speed)")
    axes[axis_index].set_ylabel("Spike Count")

def mySavefig(filename):
    try:
        plt.savefig(filename)
    except FileNotFoundError:
        directoryName = os.pathname(filename)
        os.mkdir(directoryName)
        plt.savefig(filename)
