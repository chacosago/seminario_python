import pandas as pd

auto = 'http://www.stata-press.com/data/r15/auto2.dta'

df = pd.read_stata(auto)
print(df.head())