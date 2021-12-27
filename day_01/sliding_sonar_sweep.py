from pathlib import Path
input_path = Path.cwd() / 'day_01'/'input_2.txt'
with open(input_path, 'r') as file:
    lines = file.readlines()
measurements = [int(element.split('\\')[0]) for element in lines]

cnt = 0
for a1,a2,a3,b1,b2,b3 in zip(measurements[:-3],measurements[1:-2],measurements[2:-1],measurements[1:-2],measurements[2:-1], measurements[3:]):
    if a1+a2+a3 < b1+b2+b3:
        cnt +=1
print(cnt)
