import random

def game_functions():
    game_skills = ["Rock", "Paper", "Scissors"]
    computer = random.choice(game_skills)
    return computer

def logic(computer, a):
    if computer == "Rock" and a == "Paper":
        print(f'You selected {a} and the computer selected {computer} \n You Won!!!!!')
        
    elif computer == "Rock" and a == "Rock":
        print(f'You selected {a} and the computer selected {computer} \n Match Draw.')
    
    elif computer == "Paper" and a == "Paper":
        print(f'You selected {a} and the computer selected {computer} \n Match Draw.')
        
    elif computer == "Scissors" and a == "Scissors":
        print(f'You selected {a} and the computer selected {computer} \n Match Draw.')
    
    elif computer == "Rock" and a == "Scissors":
        print(f'You selected {a} and the computer selected {computer} \n You Lost.')
        
    elif computer == "Paper" and a == "Rock":
        print(f'You selected {a} and the computer selected {computer} \n You Lost.')
        
    elif computer == "Scissors" and a == "Paper":
        print(f'You selected {a} and the computer selected {computer} \n You Lost.')
        
    elif computer == "Paper" and a == "Scissors":
        print(f'You selected {a} and the computer selected {computer} \n You Won.')
        
    elif computer == "Scissors" and a == "Rock":
        print(f'You selected {a} and the computer selected {computer} \n You Won.')
        
    elif computer == "Rock" and a == "Paper":
        print(f'You selected {a} and the computer selected {computer} \n You Won.')


print(" WELCOME TO THE ROCK, PAPER AND SCISSORS GAME ")

while True:
    a = input("Choose 1 from the following: \n \t Rock   \t   Paper   \t   Scissors \n Type Here: \t").strip()
    if a in ["Rock", "Paper", "Scissors"]:
        break
    print("Invalid input. Please try again!")

computer = game_functions()

logic(computer,a)