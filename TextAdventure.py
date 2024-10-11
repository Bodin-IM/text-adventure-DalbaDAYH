import time
import random
from pystyle import Colors, Box, Write, Center, Colorate, Anime
import sys
import json
import os

startgame = input('!START THIS CODE ON TERMINAL OR IT WILL NOT WORK! - 1 = i alredy done it. 2 = i will do it right now.')
if startgame == '1':
    print('ok')
elif startgame == '2':
    print("Exiting...")
    time.sleep(0.5)
    exit()

intro = """
  ██████ ▄▄▄█████▓ ▒█████   ██▀███ ▓██   ██▓     ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒    ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░   ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░   ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░   ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒     ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░      ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░     ░ ░   ░   ░   ▒   ░      ░      ░   
      ░               ░ ░     ░     ░ ░              ░       ░  ░       ░      ░  ░
                                    ░ ░                                            
                                    PRESS TO ENTER
"""
Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.045, enter=True)

menu = """
  ██████ ▄▄▄█████▓ ▒█████   ██▀███ ▓██   ██▓     ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒    ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░   ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░   ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░   ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒     ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░      ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░     ░ ░   ░   ░   ▒   ░      ░      ░   
      ░               ░ ░     ░     ░ ░              ░       ░  ░       ░      ░  ░
                                    ░ ░    
                                                                            
                                /=-=-=-=-=-=-=-=--=\
                                |  1. New Game     |
                                |  2. Continue     |
                                |  3. Saves        |
                                |  4. Settings     |
                                |  5. About        |
                                |  6. Exit         |
                                \=-=-=-=-=-=-=-=--=/ 
"""
Write.Print(Center.XCenter(menu), Colors.black_to_red, interval=0.001)

def settings():
    text = """
                                    /=-=-=-=-=-=-=-=--=\
                                    |  4. Settings     |
                                    |  5. About        |
                                    |  6. Inventory    |
                                    |  7. Exit         |
                                    \=-=-=-=-=-=-=-=--=/ 
    """
    Write.Print(Center.XCenter(text), Colors.black_to_red, interval=0.001)
    


def save_game():
    
    game_data = {
        'main_character': main_character,
        'HP': HP,
        'inventory': inventory,
        'visited_rooms': visited_rooms
    }
    with open('save_file.json', 'w') as file:
        json.dump(game_data, file)
    slow_print("\nThe game is saved.")

def load_game():
    global main_character, HP, inventory, visited_rooms
    try:
        with open('save_file.json', 'r') as file:
            game_data = json.load(file)
        main_character = game_data['main_character']
        HP = game_data['HP']
        inventory = game_data['inventory']
        visited_rooms = game_data['visited_rooms']
        slow_print("\nThe game is loaded.")
    except FileNotFoundError:
        slow_print("\nNo save file found!")


main_character = "Hero"
HP = 100
inventory = {
    "money": 100,
    "phone": "Working Phone"
}

visited_rooms = ["Room1", "Room2"]



def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()



red = "\033[0;32m"

i = 3

for _ in range(i):
    animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
    for j in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + red + animation[j])
        sys.stdout.flush()

def slow_print(text, delay=0.05):
    """Function to simulate typing text gradually."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def game1():
    
    settings()
    global gender_pronouns, subject_pronoun, possessive_pronoun, object_pronoun, main_character, HP, story_end, inventory, visited_rooms
    slow_print('Hi, now we are going to make a story')
    HP = 100
    inventory = []
    visited_rooms = []
    main_character = input("What's your main character's name? ")

    genders = {
        'male': ('he', 'his', 'him'),
        'female': ('she', 'her', 'her'),
        'non-binary': ('they', 'their', 'them')
    }
    slow_print("≺Available genders≻: male, female, non-binary")
    gender_choice = input("What's your main character's gender? ").lower()

    while gender_choice not in genders:
        slow_print("Invalid choice. Please choose again.")
        gender_choice = input("What's your main character's gender? ").lower()

    gender_pronouns = genders[gender_choice]
    subject_pronoun = gender_pronouns[0]
    possessive_pronoun = gender_pronouns[1]
    object_pronoun = gender_pronouns[2]

    genres = ['adventure', 'fantasy', 'horror', 'romance', 'science fiction', 'comedy']
    slow_print('!CURRENTLY THERE IS NO OTHERS GENRES EXCEPT HORROR!')
    slow_print(f"≺Available genres≻: {', '.join(genres)}")
    genre = input("⇒ What type of genre should the story be? ⇐ ").lower()

    while genre != 'horror':
        print("Invalid choice. Only 'horror' is available at the moment.")
        genre = input("⇒ What type of genre should the story be? ⇐ ").lower()

    end = ['sad', 'bad', 'good']
    slow_print(f"≺Available endings≻: {', '.join(end)}")
    story_end = input("⇒ How should the story end? ⇐ ").lower()

    while story_end not in end:
        slow_print("Invalid choice. Please choose again.")
        story_end = input("⇒ How should the story end? ⇐ ").lower()
def achievements():
    if story_end == 'good':
        slow_print(f"\n{main_character} finally escaped the house, with only minor injuries.")
    elif story_end == 'bad':
        slow_print(f"\n{main_character} found {possessive_pronoun} way out but suffered severe injuries in the process.")
    else:
        slow_print(f"\n{main_character} didn't survive the horrors of the house...")
def random_event(room):
    events = ['trap', 'find_item', 'monster_encounter', 'nothing']
    event = random.choice(events)
    if event == 'trap':
        HP_loss = random.randint(5, 20)
        slow_print(f"\n{main_character} fell into a trap! Loss {HP_loss} HP.")
        HP -= HP_loss
    elif event == 'find_item':
        item = random.choice(['Health Potion', 'Magic Scroll'])
        slow_print(f"\n{main_character} found {item}!")
        inventory.append(item)
    elif event == 'monster_encounter':
        slow_print(f"\nMonster attacking {main_character}!")
        HP -= random.randint(10, 30)
    elif event == 'nothing':
        slow_print(f"\nSomething happened in {room}.")

def use_inventory():
    slow_print(f"\nCurrent Inventory: {', '.join(inventory)}")
    item = input("What item do you want to use? > ").title()
    if item == 'Health Potion' and 'Health Potion' in inventory:
        HP_heal = random.randint(15, 30)
        slow_print(f"\n{main_character} used a health potion and restored {HP_heal} HP.")
        HP += HP_heal
        inventory.remove('Health Potion')
    else:
        slow_print(f"\n{item} Cannot be used.")

def npc_interaction():
    slow_print(f"\n{main_character} met a strange old man.")
    slow_print("Old man: 'You can ask me about two things: how to leave this place or the mystery of this house.'")
    choice = input("1. Ask about the exit 2. Ask about the mystery > ")
    if choice == '1':
        slow_print("Old man: 'To get out of here, you need to find the key in the basement.'")
    elif choice == '2':
        slow_print("Old man: 'This house was built on cursed land, and no one could leave it alive.'")


def check_room_or_leave():
    slow_print("You entered the room. What do you want to do?")
    choice = input("1. Inspect the room\n2. Leave the room\n> ")
    
    if choice == '1':
        explore_room()
    elif choice == '2':
        slow_print("\nYou decide to leave the room.")
    else:
        slow_print("\nnot correct choice.")

def choose_room():
    global visited_rooms
    rooms = ['Bathroom', 'Bedroom', 'Corridors', 'Kitchen', 'Storage Room', 'Basement', 'Attic']
    
    available_rooms = [room for room in rooms if room not in visited_rooms]
    slow_print(f"\nAvailable rooms: {', '.join(available_rooms)}")
    slow_print("⇒ Choose a room to explore ⇐")

    choice = input('> ').title()

    while choice not in available_rooms:
        slow_print("Invalid choice or room already explored. Please choose again.")
        choice = input('> ').title()

    visited_rooms.append(choice)
    return choice

def explore_room():
    slow_print("\nYou inspecting a room for some items.")
    random_event(choose_room())

def panic(room):
    global HP
    slow_print(f"\n≺Panic Attack!≻ {main_character} feels something strange in the {room}. Anxiety rises.")
    
    panic_effects = random.choice(['lose_hp', 'hallucination', 'nothing'])

    if panic_effects == 'lose_hp':
        HP_loss = random.randint(5, 15)
        slow_print(f"The panic causes {main_character} to feel faint, losing {HP_loss} HP.")
        HP -= HP_loss
    elif panic_effects == 'hallucination':
        slow_print(f"{main_character} experiences hallucinations, seeing strange figures in the room.")
    elif panic_effects == 'nothing':
        slow_print(f"{main_character} feels anxious, but nothing happens.")

def room_logic(choice):
    global HP, inventory, visited_rooms

    if visited_rooms.count(choice) > 1:  
        panic(choice) 

    if choice == 'Bathroom':
        slow_print(f"\nThe bathroom was eerily quiet, but {main_character} found some Bandages.")
        inventory.append('Bandages')
    elif choice == 'Bedroom':
        slow_print("\nThe bedroom looked terrifying, like someone or something had been there.")
        HP -= 10
    elif choice == 'Corridors':
        slow_print("\nThe corridors were consumed by darkness. There was a faint sound in the distance.")
        HP -= 5
    elif choice == 'Kitchen':
        slow_print(f"\nThe kitchen was as {main_character} left it before falling asleep. {main_character} found a Knife.")
        inventory.append('Knife')
    elif choice == 'Storage Room':
        slow_print(f"\nThe storage room was filled with unused, old items. {main_character} found a Flashlight.")
        inventory.append('Flashlight')
    elif choice == 'Attic':
        slow_print(f"\nThe attic was filled with dust and cobwebs. {main_character} found an old mirror that radiates an eerie glow.")
        HP -= 25
    elif choice == 'Basement':
        basement_scene()

def basement_scene():
    global HP, inventory
    slow_print(f"\nAs {main_character} descended into the basement, the air grew cold.")
    
    if 'Flashlight' in inventory:
        slow_print(f"\nUsing the flashlight, {subject_pronoun} illuminated the dark corners of the basement.")
    else:
        slow_print("\nWithout a flashlight, the darkness was overwhelming.")
        HP -= 20

    slow_print(f"\nIn the far corner of the basement, {subject_pronoun} discovered a door leading to hidden catacombs. "
        f"The air grew even colder, and {main_character} could hear strange, guttural sounds in the distance.")

    if 'Knife' in inventory:
        slow_print(f"\nArmed with a Knife, {main_character} felt a bit safer, but fear lingered.")

    slow_print("Suddenly, a massive creature appeared from the shadows. What should you do?")
    slow_print("1. Run back upstairs 2. Fight the creature 3. Hide")

    choice = input('> ')
    while choice not in ['1', '2', '3']:
        slow_print("Invalid choice. Please choose again.")
        choice = input('> ')

    if choice == '1':
        slow_print(f"\n{main_character} turned and ran as fast as possible back up the stairs, narrowly escaping the creature.")
        HP -= 15
    elif choice == '2':
        if 'Knife' in inventory:
            slow_print(f"\n{main_character} fought the creature bravely with the Knife and barely survived. {subject_pronoun} was wounded, but the creature was defeated.")
            HP -= 40
        else:
            slow_print(f"\nWithout a weapon, {main_character} stood no chance. The creature attacked, and {subject_pronoun} barely escaped.")
            HP -= 60
    elif choice == '3':
        slow_print(f"\n{main_character} quickly ducked behind a pillar and held {possessive_pronoun} breath. The creature roamed the catacombs for what felt like hours but eventually moved on.")
        HP -= 10

def beginning():
    global HP
    slow_print(f"\nIt was a dark and creepy night. {main_character} was on {possessive_pronoun} way to the store, "
        f"because {subject_pronoun} had forgotten to buy snacks for {possessive_pronoun} party."
        f"As {subject_pronoun} entered the store, {subject_pronoun} heard strange noises behind {object_pronoun}, "
        f"but {subject_pronoun} decided to ignore them. After buying the snacks, {main_character} headed back to {possessive_pronoun} house.")

    slow_print(f"\nWhen {main_character} reached the front door, {subject_pronoun} hesitated. What should {subject_pronoun} do?")
    print("1. Open the door and go in 2. Go for a walk")

    answer = input('> ')

    if answer == '1':
        slow_print(f"\n{main_character} went in.")
        
    elif answer == '2':
        slow_print(f"\n{main_character} went for a walk and got tired.")
        HP -= 15
    else:
        slow_print(f"\n{main_character} stood frozen at the door, unsure of what to do. Eventually, {subject_pronoun} decided to stay outside for a while, "
            f"gathering {possessive_pronoun} thoughts.")

    slow_print(f"\n{main_character} entered the house, but the atmosphere felt wrong. {subject_pronoun} heard strange noises coming from the rooms. "
        f"What should {subject_pronoun} do next?")

    while HP > 0:
        room = choose_room()
        room_logic(room)
        
        if room == 'Basement':
            break

    if HP <= 0:
        slow_print(f"\n{main_character}'s health dropped to zero. {subject_pronoun} did not survive the night.")
    else:
        ending()
    check_room_or_leave()
def ending():
    global HP
    slow_print("\n==> The End <==")
    if story_end == 'good' and HP > 50:
        slow_print(f"\nIn the end, {main_character} survived the horrors of the night, emerging stronger and wiser.")
    elif story_end == 'bad' or HP <= 0:
        slow_print(f"\nIn the end, {main_character} couldn't escape the dread that haunted the night, and the horrors left a permanent scar on {object_pronoun}.")
    elif story_end == 'sad':
        slow_print(f"\nIn the end, {main_character}'s fate was sealed with tragedy. {subject_pronoun} never fully recovered from the terror of the night.")
    slow_print(f"\nFinal HP: {HP}")

game1()
beginning()
