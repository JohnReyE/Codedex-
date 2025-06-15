import random

def main():
    print("""
================================
Rock Paper Scissors Lizard Spock
================================
1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖
    """)

    player = int(input("Pick a number: "))
    computer = random.randint(1, 5)
    choices = {
        1: "✊", 
        2: "✋", 
        3: "✌️",
        4: "🦎",
        5: "🖖"
        }
    winning_combinations = [ 
        (3, 2),
        (2, 1),
        (1, 4),
        (4, 5),
        (5, 3),
        (3, 4),
        (4, 2),
        (2, 5),
        (5, 1),
        (1, 3)
    ]

    if player in choices and computer in choices:
        print(f"You chose: {choices[player]}")
        print(f"CPU Chose: {choices[computer]}")
    else:
        print("Invalid choice")
        return
    
    if player == computer:
        print ("It's a tie!")
    elif (player, computer) in winning_combinations:
        print("The player wins!")
    else:
        print("The computer wins!")    
main()