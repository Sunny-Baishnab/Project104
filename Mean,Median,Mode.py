import csv
from collections import Counter

with open('SOCR-HeightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

n = len(new_data)

#Mean for the Weight
total = 0

for i in new_data:
    total = total+i

mean = total/n
print('Mean (Average) is ->',mean)

#Median for the Weight
new_data.sort()

if n%2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1+median2)/2

else:
    median = new_data[n//2]

print('Median is ->'+str(median))

#Mode for the Weight

data = Counter(new_data)

mode_data_for_range = {
    '90-100':0,
    '100-110':0,
    '110-120':0,
    '120-130':0,
    '130-140':0,
    '140-150':0,
    '150-160':0,
    '160-170':0
}

for weight,occurrence in data.items():
    if 90<float(weight)<100:
        mode_data_for_range['90-100']+=occurrence
    elif 100<float(weight)<110:
        mode_data_for_range['100-110']+=occurrence
    elif 110<float(weight)<120:
        mode_data_for_range['110-120']+=occurrence
    elif 120<float(weight)<130:
        mode_data_for_range['120-130']+=occurrence
    elif 130<float(weight)<140:
        mode_data_for_range['130-140']+=occurrence
    elif 140<float(weight)<150:
        mode_data_for_range['140-150']+=occurrence
    elif 150<float(weight)<160:
        mode_data_for_range['150-160']+=occurrence
    elif 160<float(weight)<170:
        mode_data_for_range['160-170']+=occurrence
    
mode_range,mode_occurrence = 0,0

for range,occurrence in mode_data_for_range.items():
    if occurrence>mode_occurrence:
        mode_range,mode_occurrence = [int(range.split('-')[0]),int(range.split('-')[1])],occurrence

mode = float((mode_range[0]+mode_range[1])/2)
print('Mode is ->',mode)
