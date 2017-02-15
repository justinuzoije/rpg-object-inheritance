"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Hero(object):
    def __init__(self):
        health = 10
        power = 5

class Goblin(object):
    def __init__(self):
        health = 6
        power = 2

def main():
    # Hero.health = 10
    # Hero.power = 5
    # Goblin.health = 6
    # Goblin.power = 2

    while Goblin.health > 0 and Hero.health > 0:
        print "You have %d health and %d power." % (Hero.health, Hero.power)
        print "The goblin has %d health and %d power." % (Goblin.health, Goblin.power)
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            Goblin.health -= Hero.power
            print "You do %d damage to the goblin." % Hero.power
            if Goblin.health <= 0:
                print "The goblin is dead."
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if Goblin.health > 0:
            # Goblin attacks hero
            Hero.health -= Goblin.power
            print "The goblin does %d damage to you." % Goblin.power
            if Hero.health <= 0:
                print "You are dead."

main()
