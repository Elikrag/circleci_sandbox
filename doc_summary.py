import pandas as pd

data = pd.read_excel("data/subpartkb-processed.xlsx")
summary = data['Classification'].describe()
print(summary)


