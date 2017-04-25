import random


class Dice(object):
    def __init__(self, dice_type):
        self.dice_type = dice_type

    def roll(self):
        return random.randint(1, self.dice_type)

    def generator(self):
        for i in range(0, 10):
            yield self.roll()


dice = Dice(3)
for r in dice.generator():
    print(r)

d = Dice(3)
print(d.roll())
print(d.dice_type)

