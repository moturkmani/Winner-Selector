import random

# Define the ASCII art banner using a raw string
ascii_art = r"""
.------..------..------..------..------..------..------.        
|P.--. ||O.--. ||K.--. ||E.--. ||M.--. ||O.--. ||N.--. |        
| :/\: || :/\: || :/\: || (\/) || (\/) || :/\: || :(): |        
| (__) || :\/: || :\/: || :\/: || :\/: || :\/: || ()() |        
| '--'P|| '--'O|| '--'K|| '--'E|| '--'M|| '--'O|| '--'N|        
`------'`------'`------'`------'`------'`------'`------'        
.------..------..------..------.                                
|C.--. ||A.--. ||R.--. ||D.--. |                                
| :/\: || (\/) || :(): || :/\: |                                
| :\/: || :\/: || ()() || (__) |                                
| '--'C|| '--'A|| '--'R|| '--'D|                                
`------'`------'`------'`------'                                
.------..------..------..------..------..------..------..------.
|G.--. ||I.--. ||V.--. ||E.--. ||A.--. ||W.--. ||A.--. ||Y.--. |
| :/\: || (\/) || :(): || (\/) || (\/) || :/\: || (\/) || (\/) |
| :\/: || :\/: || ()() || :\/: || :\/: || :\/: || :\/: || :\/: |
| '--'G|| '--'I|| '--'V|| '--'E|| '--'A|| '--'W|| '--'A|| '--'Y|
`------'`------'`------'`------'`------'`------'`------'`------'  
"""

def dramatic_reveal(winner):
    # Dramatic reveal sequence
    print("and", end=" ")
    input()
    print("the", end=" ")
    input()
    print("WINNER is...", end=" ")
    input()
    print(f">>> {winner} <<<")

def print_goodbye_ascii():
    # Print the custom goodbye ASCII art
    goodbye_ascii = r"""
   _____   ____    ____   _____   ____ __     __ ______  _  _  _ 
  / ____| / __ \  / __ \ |  __ \ |  _ \\ \   / /|  ____|| || || |
 | |  __ | |  | || |  | || |  | || |_) |\ \_/ / | |__   | || || |
 | | |_ || |  | || |  | || |  | ||  _ <  \   /  |  __|  | || || |
 | |__| || |__| || |__| || |__| || |_) |  | |   | |____ |_||_||_|
  \_____| \____/  \____/ |_____/ |____/   |_|   |______|(_)(_)(_)

    """
    print(goodbye_ascii)

def main():
    # Display ASCII art banner
    print(ascii_art)

    while True:
        print("Let's select a winner for the Pokémon Card Giveaway!")
        
        # Collect 10 TikTok display names
        names = []
        for i in range(1, 11):
            name = input(f"Please enter name {i}: ")
            names.append(name)

        # Display the collected names
        print("\nThere will be 1 lucky winner amongst these names:")
        for idx, name in enumerate(names, 1):
            print(f"{idx}. {name}")

        # Randomly pick a winner
        winner = random.choice(names)

        # Dramatic reveal
        dramatic_reveal(winner)

        # Ask if the user wants to restart
        restart = input("\nDo you want to start over? (yes/no): ").strip().lower()
        if restart not in ["yes", "y"]:
            print_goodbye_ascii()
            break

# Run the script
if __name__ == "__main__":
    main()
