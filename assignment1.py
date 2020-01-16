import json

with open('AssignmentPart1/SouthAfrica1990.json', encoding='utf-16') as file:
    data= json.load(file)
print(data)



# with open('json_sample_read', 'w', encoding='utf8') as file:
#     json.dump(data, file, indent = 4)
