"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0
        self.inventory = []

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        if self.coins >= item.cost:
            self.coins -= item.cost
            #Store itself in the inventory instead of apply to hero
            #item.store_item(hero.inventory)
            self.inventory.append(item)
        else:
            print "Not enough coins"

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        crit_attack = random.randint(1,10) > 8
        #crit_attack = 10
        if crit_attack:
            print "Critical attack!"
            self.power = self.power*2
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        #Each evade point deceases chance of being hit by 5%
        percent_chance = 100 - (self.evade * 5)
        #print "%s percent chance to be hit" % percent_chance
        if percent_chance > 90:
            percent_chance = 90

        if random.randrange(0,100) < percent_chance:
            points = points - self.armor
            self.health -= points
            print "%s received %d damage." % (self.name, points)

        if self.health <= 0:
            print "%s is dead." % self.name

    def collect_bounty(self, enemy):
        print "%s collected %d coins" % (self.name, enemy.bounty)
        self.coins = self.coins + enemy.bounty

    # def store_item(self, item):
    #     inventory.append(item)

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 6
        self.power = 2
        self.bounty = 5

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        recuperate = random.randint(1,10) > 8
        #recuperate = 10
        if recuperate:
            print "%s recuperates 2 points of health!" % self.name
            self.health += 2
        if self.health <= 0:
            print "%s is dead." % self.name

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 2
        self.bounty = 10

    def receive_damage(self, points):
        dodge = random.randint(1,10) > 1
        #dodge = 10
        if dodge:
            print "%s evades attack" % self.name
        else:
            print "%s received %d damage." % (self.name, points)
            self.health -= points
        if self.health <= 0:
            print "%s is dead." % self.name

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 2
        self.power = 2
        self.bounty = 5

    def alive(self):
        return True

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s cannot die." % self.name

class Rat(Character):
    def __init__(self):
        self.name = "rat"
        self.health = 1
        self.power = 1
        self.bounty = 1

class Ghost(Character):
    def __init__(self):
        self.name = "ghost"
        self.health = 2
        self.power = 2
        self.bounty = 2

    def receive_damage(self, points):
        scary = random.randint(1,10) > 5
        if scary:
            print "Boo!"
            points = 0

        print "%s received %d damage." % (self.name, points)
        self.health -= points
        if self.health <= 0:
            print "%s is dead." % self.name

class Goblin_Chief(Character):
    def __init__(self):
        self.name = 'goblin chief'
        self.health = 10
        self.power = 4
        self.bounty = 8


class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.bounty = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.bounty = 6

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. check inventory"
            print "4. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                for item in hero.inventory:
                    print item
            elif input == 4:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            hero.collect_bounty(enemy)
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

    def __repr__(self):
        return "Tonic"

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

    def __repr__(self):
        return "Sword"

class Axe(object):
    cost = 15
    name = 'axe'
    def apply(self, hero):
        hero.power += 4
        print "%s's power increased to %d." % (hero.name, hero.power)

    def __repr__(self):
        return "Axe"

class SuperTonic(object):
    cost = 10
    name = 'super tonic'
    def apply(self, character):
        character.health = 10
        print "%s's health is restored." % character.name

    def __repr__(self):
        return "Super Tonic"

class Poison(object):
    cost = 10
    name = 'poison'
    def apply(self, character):
        character.health -= 10
        print "%s's health decreased to %d." % (character.name, character.health)

    def __repr__(self):
        return "Poison"

class Armor(object):
    cost = 10
    name = 'armor'
    def apply(self, character):
        character.armor += 2
        print "%s's armor is increased by %d" % (hero.name, hero.armor)

    def __repr__(self):
        return "Armor"

class Evade(object):
    cost = 10
    name = 'evade'
    def apply(self, character):
        character.evade += 2
        print "%s's evade is increased by %d" % (hero.name, hero.evade)

    def __repr__(self):
        return "Evade"

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, Axe, SuperTonic, Armor, Evade, Poison]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
#enemies = [Goblin(), Wizard()]
enemies = [Goblin(), Goblin_Chief(), Goblin()]

#Inventory Checking
#free_tonic = Tonic()
#hero.inventory.append(free_tonic)

battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
