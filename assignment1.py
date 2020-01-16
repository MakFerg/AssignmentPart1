#open json file
import json

with open('AssignmentPart1/SouthAfrica1990.json', encoding='utf-16') as file:
    data= json.load(file)


#open json file as csv with keys wanted :

sample = data[0]

with open("SouthAfrica1990.csv", "w", encoding= 'utf8') as file:
    headers = file.write('type_of_violence, best_estimate\n')
    for entry in data:
        file.write(f"{entry['type_of_violence']},{entry['best']}\n")

    
        






# with open('json_sample_read', 'w', encoding='utf8') as file:
#     json.dump(data, file, indent = 4)
