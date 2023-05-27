import random
import time

username = input("Enter your username: ")

uc = 100
gold = 100
level = 1
tier = "Bronze"
gaming_xp = 0
ranked_up = False
battles_fought = 0

def start_battle(map_choice):
    print(f"Entering {map_choice} map lobby...")
    print("Finding players...")
    for i in range(5, 0, -1):
        print(f"Starting in {i}")
        time.sleep(1)
    print("Battling...")
    time.sleep(5)
    kills = random.randint(1, 30)
    winning_ratio = random.uniform(0, 100)
    level_up = random.randint(1, 5)
    tier_up = random.randint(1, 3)
    print("\n---- GAME RESULT ----")
    print(f"Kills: {kills}")
    print(f"Winning Ratio: {winning_ratio:.2f}%")
    print(f"Level Up: {level_up}")
    print(f"Tier Up: {tier_up}")

    global level, tier, gaming_xp, ranked_up, battles_fought
    level += level_up
    gaming_xp += kills * 10

    if winning_ratio > 50:
        ranked_up = True

    battles_fought += 1
    if battles_fought % 5 == 0:
        if tier == "Conqueror":
            print("Congratulations! You have reached the highest rank!")
        else:
            tier_up += 1
            ranked_up = True
            tier = rank_up_tier(tier)

def rank_up_tier(current_tier):
    ranks = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Crown", "Ace", "Conqueror"]
    current_index = ranks.index(current_tier)
    if current_index < len(ranks) - 1:
        return ranks[current_index + 1]
    else:
        return current_tier

def see_profile():
    print("\n---- PROFILE ----")
    print(f"Username: {username}")
    print(f"Level: {level}")
    print(f"Gaming XP: {gaming_xp}")
    print(f"Rank: {tier}")
    print(f"UC: {uc}")
    print(f"Gold: {gold}")

def visit_shop():
    global uc  # Declare uc as global
    print("\n---- SHOP ----")
    items = {
        1: {"name": "Legendary Outfit", "price": 100},
        2: {"name": "Gun Skins", "price": 50},
        3: {"name": "Pet", "price": 20}
    }
    for key, item in items.items():
        print(f"{key}. {item['name']} - {item['price']} UC")

    item_choice = input("Enter the item choice: ")
    if item_choice.isdigit() and int(item_choice) in items:
        item = items[int(item_choice)]
        if uc >= item["price"]:
            uc -= item["price"]
            print(f"You have purchased {item['name']} for {item['price']} UC.")
        else:
            print("Insufficient UC to purchase the item.")
    else:
        print("Invalid item choice!")

def quit_game():
    print("Goodbye!")
while True:
    print("\n---- PUBG MOBILE CLI ----")
    print("1. Battle")
    print("2. See Profile")
    print("3. Shop")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n---- MAP SELECTION ----")
        maps = {
            1: "Erangle",
            2: "Shanhok",
            3: "Livik"
        }
        for key, map_name in maps.items():
            print(f"{key}. {map_name}")

        map_choice = input("Enter the map choice: ")

        if map_choice.isdigit() and int(map_choice) in maps:
            start_battle(maps[int(map_choice)])
        else:
            print("Invalid map choice!")

    elif choice == "2":
        see_profile()

    elif choice == "3":
        visit_shop()

    elif choice == "4":
        quit_game()
        break

    else:
        print("Invalid choice!")
