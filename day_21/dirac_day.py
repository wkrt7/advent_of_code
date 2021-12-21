class Player:
    def __init__(self, starting_position):
        self.score = 0
        self.position = starting_position
    def move(self, nb_of_steps):
        self.position = (self.position + nb_of_steps ) % 10
        if self.position == 0:
            self.position = 1
        self.score += self.position

def roll_a_dice(last_roll):
    if last_roll == 100 :
        return sum([1,2,3]), 3
    elif last_roll == 99:
        return sum([100,1,2]), 2
    elif last_roll == 98:
        return sum([99,100,1]), 1
    else:
        return sum([last_roll + 1, last_roll + 2, last_roll + 3]), last_roll+3

roll_no = 0
finished = False
p1 = Player(2)
p2 = Player(8)

rolls_sum, last_roll = roll_a_dice(0)
p1.move(rolls_sum)
roll_no += 3
rolls_sum, last_roll = roll_a_dice(last_roll)
p2.move(rolls_sum)
roll_no += 3
while not finished:
    

    
    
    
    rolls_sum, last_roll = roll_a_dice(last_roll)
    roll_no += 3
    p1.move(rolls_sum)

    if p1.score >= 1000:
        break
    rolls_sum, last_roll = roll_a_dice(last_roll)
    roll_no += 3
    p2.move(rolls_sum)
    
    if p2.score >= 1000:
        break

print(roll_no, p1.score, p2.score)
print(roll_no * p1.score)