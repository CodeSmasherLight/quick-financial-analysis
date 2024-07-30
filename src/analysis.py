import pandas as pd

def calculate_returns(data):
    return data.pct_change()

def calculate_correlations(data):
    return data.corr()

def calculate_average_returns(returns):
    return returns.mean()