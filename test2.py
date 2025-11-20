import json

with open('testdata.json', 'r') as file:
    data = json.load(file)
#print(data['game1']['tags'][0])

top_level = []
for x in data:
    top_level.append(x)

mid_level = []
for x in top_level:
    mid_level.append(data[x])
#print(data[top_level[0]]['rating'])

jsonob = json.dumps(data, indent=4) # this code results in the testdata.json file (not saved to disk)
print(jsonob)