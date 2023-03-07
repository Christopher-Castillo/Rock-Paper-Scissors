import random
class Rock_Paper_Scissors():
    
    CHOICES = ['rock', 'paper', 'scissors']

    def player_input(self):
        while True:
            rps = input('Type your choice: rock, paper, or scissors (type "I quit" to exit): ')
            if rps.lower() == "i quit":
                return None
            elif rps in self.CHOICES:
                return rps.lower()
            else:
                print("Invalid input, please try again.")
class Computer():

    def computer_choice(self):
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        return computer_choice
    
game = Rock_Paper_Scissors()
computer = Computer()

while True:
    player_choice = game.player_input()
    if player_choice is None: 
        print("Player ended game, Thank you for playing ")
        break
    computer_choice = computer.computer_choice()

    if player_choice == computer_choice:
        print(f"Game Tied, Both selected {player_choice}")
    elif player_choice == "rock" and computer_choice == "paper" or player_choice == "paper" and computer_choice == "scissors" or player_choice == "scissors" and computer_choice == "rock":
        print(f'Player Chose: {player_choice}\nComputer Chose: {computer_choice}')
        print("You lose")   
    else:
        print(f'Player Chose: {player_choice}\nComputer Chose: {computer_choice}')
        print("You Win!")