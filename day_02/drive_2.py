class Submarine:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def move(self,comand):
        direction, step = tuple(comand.split(' '))
        step = int(step)
        if direction == 'forward':
            self.x += step
            self.y += self.aim * step
        elif direction == 'down':
            # self.y += step
            self.aim += step
        elif direction == 'up':
            # self.y -= step
            self.aim -= step
        else:
            print(f'Directon unrecognized: {direction=}')


# print(*tuple('sdf df'.split(' ')) )

from pathlib import Path
input_path = Path.cwd() / 'day_02'/'input_1.txt'
with open(input_path, 'r') as file:
    lines = file.readlines()

sub = Submarine()
for line in lines:
    sub.move(line.split('\n')[0])

print(sub.x * sub.y)
