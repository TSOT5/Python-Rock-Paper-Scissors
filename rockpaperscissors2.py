import random
import re

x = True
pattern = re.compile(r"^(1|2|3)$")
while x == True:
        choice = {1: "Rock", 2:"Paper", 3:"Scissors"}

        playchoicec = input("What do you pick? 1 for Rock 2 for Paper 3 for Sissors. Type 'I Quit' to quit: ").lower()
        if pattern.match(playchoicec):
            playchoice = int(playchoicec)
        
        
            comchice = random.randint(1, 3)

            pick = choice[playchoice]
            compick = choice[comchice]

            results = {
                ("Rock", "Paper"): "You Lose",
                ("Rock", "Rock"): "Tie",
                ("Rock", "Scissors"): "You Win",
                ("Paper", "Rock"): "You Win",
                ("Paper", "Paper"): "Tie",
                ("Paper", "Scissors"): "You Lose",
                ("Scissors", "Rock"): "You Lose",
                ("Scissors", "Scissors"): "Tie",
                ("Scissors", "Paper"): "You Win"
            }

            res = results[(pick, compick)]
            print(f"Your choice: {pick}, Computers choice: {compick}")
            print(res)
        
        elif playchoicec == "i quit":
             print("Thank you for playing")
             break

        else:
            print("Please type one of the options")
            pass 