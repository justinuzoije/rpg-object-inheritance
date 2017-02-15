"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Hero(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power

class Goblin(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power

def main():
    # Hero.health = 10
    # Hero.power = 5
    # Goblin.health = 6
    # Goblin.power = 2

    goblin = Goblin(6,2)
    hero = Hero(10,5)

    while goblin.health > 0 and hero.health > 0:
        print "You have %d health and %d power." % (hero.health, hero.power)
        print "The goblin has %d health and %d power." % (goblin.health, goblin.power)
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            goblin.health -= hero.power
            print "You do %d damage to the goblin." % hero.power
            if goblin.health <= 0:
                print "The goblin is dead."
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print "The goblin does %d damage to you." % goblin.power
            if hero.health <= 0:
                print "You are dead."

main()
