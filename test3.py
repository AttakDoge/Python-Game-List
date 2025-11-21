import json
import pandas as pd

with open('ex_format.json', 'r') as file:
    data = json.load(file)

print(data[0]['name'])

print(pd.DataFrame(data))

print(pd.DataFrame(data).iloc[0]['developer']) # can get specific rows and columns, iloc selects row