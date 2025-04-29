# Joan
import csv

def check_wonky(row):
    if len(row) == 3:
        if len(row[1].split()) == 1: # english name on 2nd item
            row[0] = row[0] + ',' + row[1]
            del row[1]
        elif len(row[2].split()) == 1: # sst singapore name on 3rd item 
            row[1] = row[1] + ',' + row[2]
            del row[2]
            

def count_win(row, current_medal):
    if current_medal == 'Gold':
        medal_counter[row[1]][0] += 1
    elif current_medal == 'Silver':
        medal_counter[row[1]][1] += 1
    elif current_medal == 'Bronze':
        medal_counter[row[1]][2] += 1
        

with open('./resources/NOI_24_RESULT.csv', 'r') as f:
    x = list(row for row in csv.reader(f))
    schools = []
    for row in x: #to build list of schools
        check_wonky(row)
        if len(row) == 2 and row[1] not in schools:
            schools.append(row[1])
    medal_counter = {school:[0,0,0] for school in schools}
    current_medal = None
    for row in x: # to check medals 
        if len(row) == 1:
            if row[0] in ['Gold', 'Silver', 'Bronze']:
                current_medal = row[0]
        elif len(row) == 2:
            count_win(row, current_medal)
    medal_count = {school: (medal_counter[school][0], medal_counter[school][1], medal_counter[school][2]) for school in schools}
    medal_sum = [[school,sum(medal_counter[school])] for school in schools]
    medal_sum.sort(key=lambda x: x[1], reverse=True)
top_5 = [school[0] for school in medal_sum[:5]]

print(','.join(top_5))
