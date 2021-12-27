from pathlib import Path
input_path = Path.cwd() / 'day_01'/'input_1.txt'
with open(input_path, 'r') as file:
    lines = file.readlines()
measurements = [int(element.split('\\')[0]) for element in lines]

cnt = 0
for m1,m2 in zip(measurements[:-1],measurements[1:]):
    if m1 < m2:
        cnt +=1
print(cnt)
print(input_path )