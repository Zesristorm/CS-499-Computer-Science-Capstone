import random


def display_instructions():
    print("Welcome to the Villainess Text Adventure Game!")
    print("Collect all items to win the game and avoid the Saintess heroine.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'item name'")


def show_status(current_room, inventory, rooms):
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")


def process_move(current_room, direction, rooms):
    direction = direction.lower()  # Ensure direction is in lowercase
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print("You can't go that way!")
        return current_room


def get_item(current_room, inventory, rooms):
    if 'item' in rooms[current_room]:
        item = rooms[current_room]['item']
        inventory.append(item)
        del rooms[current_room]['item']
        print(f"{item} retrieved!")
    else:
        print("No item in this room!")


def check_win_lose(inventory, villain_room, current_room):
    if len(inventory) == 6:  # Assuming there are 6 items to collect
        print("You have collected all the items! Now head to the Throne Room to confront the Saintess heroine!")
        return 'throne room'
    if current_room == villain_room:
        if 'poisoned dagger' in inventory:
            if battle_start():
                return 'win'
        print("You encountered the Saintess heroine! GAME OVER!")
        return 'lose'
    return None


class Saintess:
    max_health = 200.0
    health = max_health
    Abilities = {
        1: {'name': 'Slash', 'type': 'physical', 'damage': 10},
        2: {'name': 'Screech', 'type': 'special', 'damage': 5},
        3: {'name': 'Rampage', 'type': 'physical', 'damage': 15},
        4: {'name': 'Heal', 'type': 'special', 'damage': 10},
        5: {'name': 'Purify', 'type': 'special', 'damage': 0},
        6: {'name': 'Light Attack', 'type': 'special', 'damage': 20},
    }
    status_effect = []
    alive = True


class Player:
    max_health = 100.0
    health = max_health
    Abilities = {
        1: {'name': 'Poison Slash', 'type': 'physical', 'damage': 5},
        2: {'name': 'Thrust', 'type': 'physical', 'damage': 10},
        3: {'name': 'Last Will', 'type': 'physical', 'damage': 50},
        4: {'name': 'Full Counter', 'type': 'physical', 'damage': 3},
    }
    status_effect = []
    alive = True


def get_s_move():
    return random.randint(1, 6)


def poison_chance():
    poison = random.randint(1, 100)
    print("Poisoned Chance:", poison, "%")
    return poison <= 70


def do_battle(saintess_move, p_move, s, p):
    print("The Saintess used ability", s.Abilities[saintess_move]['name'])
    print("You used ability", p.Abilities[p_move]['name'])

    # Player's move
    if p_move == 1:
        if poison_chance():
            s.status_effect.append('poisoned')
        s.health -= p.Abilities[p_move]['damage']
        print("The Saintess suffered", p.Abilities[p_move]['damage'], "damage")
    elif p_move == 2:
        s.health -= p.Abilities[p_move]['damage']
        print("The Saintess suffered", p.Abilities[p_move]['damage'], "damage")
    elif p_move == 3:
        s.health -= p.Abilities[p_move]['damage']
        p.health -= 10
        print("The Saintess suffered", p.Abilities[p_move]['damage'], "damage")
        print("You were hurt due to the effects of Last Will and suffered 10 additional damage.")
    elif p_move == 4:
        if s.Abilities[saintess_move]['type'] == 'physical':
            reflect_damage = s.Abilities[saintess_move]['damage'] * p.Abilities[p_move]['damage']
            s.health -= reflect_damage
            print("You reflected the Saintess's ability and she suffered greatly", reflect_damage, "damage")

    if s.health <= 0:
        s.alive = False
        return

    # Saintess's move
    if saintess_move == 1 or saintess_move == 2 or saintess_move == 3:
        p.health -= s.Abilities[saintess_move]['damage']
        print("You suffered", s.Abilities[saintess_move]['damage'], "damage")
    elif saintess_move == 4:
        s.health += s.Abilities[saintess_move]['damage']
        print("The Saintess healed herself for", s.Abilities[saintess_move]['damage'], "health")
    elif saintess_move == 5:
        if s.status_effect:
            s.status_effect.pop()
            print("The Saintess cast Purify and cleared a status effect")
        else:
            print("The Saintess had no status effect so Purify had no effect")
    elif saintess_move == 6:
        p.health -= s.Abilities[saintess_move]['damage']
        print("You suffered", s.Abilities[saintess_move]['damage'], "damage")


def apply_poison(s):
    poison_damage = s.max_health * 0.1  # 10% of max health
    print("The Saintess suffered", poison_damage, "points of damage due to poison")
    s.health -= poison_damage
    if s.health <= 0:
        s.alive = False
    return


def battle_start():
    print('The Saintess heroine approaches you PREPARE FOR BATTLE!!!!')
    s = Saintess()
    p = Player()
    while True:
        print('The Saintess stares at you ready to attack, What will you do? Choose a move 1-4.')
        print('Move 1:', p.Abilities[1]['name'], 'Move 2:', p.Abilities[2]['name'], 'Move 3:', p.Abilities[3]['name'],
              'Move 4:', p.Abilities[4]['name'])
        p_move = int(input())
        saintess_move = get_s_move()

        do_battle(saintess_move, p_move, s, p)

        if s.health <= 0:
            s.alive = False
        if p.health <= 0:
            p.alive = False

        if not s.alive:
            print("You have slain the Saintess heroine, Congratulations")
            return True
        if not p.alive:
            print("The Saintess heroine was too strong. SLEEP WELL!")
            return False

        if s.alive and 'poisoned' in s.status_effect:
            apply_poison(s)

        if s.alive:
            print("Saintess health is at:", s.health)
        if p.alive:
            print("Your health is at:", p.health)


def main():
    inventory = []
    rooms = {
        'start room': {'north': 'ballroom', 'west': 'throne room', 'south': 'secret passage', 'east': 'armory'},
        'dungeon': {'west': 'secret passage', 'item': 'key to dungeon'},
        'secret passage': {'north': 'start room', 'east': 'dungeon', 'item': 'disguise cloak'},
        'ballroom': {'south': 'start room', 'east': 'garden', 'item': 'invitation to ball'},
        'garden': {'west': 'ballroom', 'item': 'enchanted amulet'},
        'royal library': {'south': 'armory', 'item': 'ancient grimoire'},
        'armory': {'north': 'royal library', 'west': 'start room', 'item': 'poisoned dagger'},
        'throne room': {'east': 'start room'}  # Villain Room
    }
    current_room = 'start room'
    villain_room = 'throne room'

    display_instructions()

    while True:
        show_status(current_room, inventory, rooms)
        try:
            move = input('Enter your move: ').strip().lower()
        except EOFError:
            print("EOFError: Input was not provided. Exiting the game.")
            break

        if move.startswith('go '):
            direction = move.split()[1]
            current_room = process_move(current_room, direction, rooms)
        elif move.startswith('get '):
            item = move.split(maxsplit=1)[1] if len(move.split(maxsplit=1)) > 1 else ''
            if item:
                get_item(current_room, inventory, rooms)
            else:
                print("Invalid item!")
        else:
            print('Invalid input!')

        win_lose_status = check_win_lose(inventory, villain_room, current_room)
        if win_lose_status == 'throne room':
            current_room = 'throne room'
            if battle_start():
                print("You collected all items and defeated the Saintess heroine! YOU WIN!")
                break
            else:
                print("You encountered the Saintess heroine! GAME OVER!")
                break
        elif win_lose_status:
            break


if __name__ == "__main__":
    main()