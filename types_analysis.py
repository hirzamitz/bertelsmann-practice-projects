import csv

count = 0

'''
  Load the csv file into a nested list and remove the first column (cell_id)
  so we only have the columns for Dr. 123 Kid, Dr. Do Little, and Dr. Scrubs
'''
with open("dataset.csv", 'r') as f:
  reader = csv.reader(f)
  data = list(reader)
  data = [[col[1],col[2],col[3]] for col in data]

'''
  Count the number of rows where the col1 != col2 != col3
'''
for i in range(1, len(data)):
    if data[i].count(data[i][0]) != 3:
        count += 1

'''
  Create a dictionary of all the different combination of types 
  and set the initial count to zero for all combinations
  For example:
       combo ['Type1', 'Type2'] 
       combo ['Type1', 'Type3'] 
'''
combo = {}

for i in range(1,15):
    for j in range(2,15):
        if i != j:
            combo["Type" + str(i), "Type" + str(j)]  = 0

# Loop over data and increment combo
for i in range(1, len(data)):

    # Sort the row values so that the order matches the order in the combo keys
    temp = sorted(data[i])

    # Remove null values
    temp = list(filter(None,temp))

    if len(temp) == 2:
        if temp[0] != temp[1]:
            combo[temp[0],temp[1]] += 1
    elif len(temp) == 3:
        if temp[0] != temp[1]:
            combo[temp[0],temp[1]] += 1
        if temp[1] != temp[2]:
            combo[temp[1],temp[2]] += 1
        if temp[0] != temp[2]:
            combo[temp[0],temp[2]] += 1

print("Common disagreement patterns")
print("===========================================")

total = 0

for key, value in combo.items():
    total += value
    if value > 0:
        print(key, ": ", value)

print("===========================================")

print("Total rows: ", len(data))
print("Total rows with disagreements: ", count)
