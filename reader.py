import pandas as pd

df = pd.read_csv("csv/vg.csv", encoding='ISO-8859-1')
print(df.values)