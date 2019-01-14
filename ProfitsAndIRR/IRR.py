from scipy.optimize import newton
import pandas as pd

df = pd.read_excel('../../personal-finance-with-python/data/xirr.xlsx', sheet_name="irregular")
df['total'] = df.income + df.expenses

print(df)


def xnpv(rate, values, dates):
    '''Runs XNPV function'''
    min_date = min(dates) 
    return sum([
        value / (1 + rate)**((date - min_date).days / 365) # Convert each value to present
        for (value, date) # iterate through each value, date set
        in zip(values, dates) # Makes an iterator taking the passed iterators in to consideration
    ])


# internal rate of return is the rate at which the discounted value becomes  zero
print(xnpv(0.12, df.total, df.date))
print(xnpv(0.13, df.total, df.date))
print(xnpv(0.1257, df.total, df.date)) 


# Use newton rampson method and define the XIIR method

def XIIR(values, dates):
    return newton(lambda r: xnpv(r, values, dates), 0)
    
print('Value using Newton Rampson method')
print(XIIR(df.total, df.date))
