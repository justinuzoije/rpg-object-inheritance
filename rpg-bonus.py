"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print "%s does %d damage to the %s." % (self.name, self.power, enemy.name)

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print "%s Health: %d and Power: %d" % (self.name,self.health, self.power)

class Hero(Character):
    pass

#You must have pass to have an empty class
class Goblin(Character):
    pass

class Zombie(Character):
    def alive(self):
        return True

def main():
    hero = Hero("Hero",10,5)
    zombie = Zombie("Zombie",20,2)

    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print
        print "What do you want to do?"
        print "1. fight zombie"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            hero.attack(zombie)
            # print "You do %d damage to the goblin." % hero.power
            if zombie.health <= 0:
                print "The zombie cannot die!"
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if zombie.health > 0:
            zombie.attack(hero)
            #print "The goblin does %d damage to you." % goblin.power
            if hero.health <= 0:
                print "You are dead."

main()
