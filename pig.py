import random

class Die: # using a class and assigning to die
    def __init__(self):
        random.seed(0) # using random and placing a seed to make sure the numbers are generated
    
    def roll(self): 
        return random.randint(1, 6) # return an int number 1-6


class Player: # defining a class player
    def __init__(self, name):
        self.name = name 
        self.score = 0 # self.score to ensure that players will begin with score of 0
    
    def add_score(self, points): 
        self.score += points # adds point to the score
    
    def __str__(self):
        return f"{self.name} - Score: {self.score}" # return player name and player score 


class Game: # defining class name 
    def __init__(self):
        self.die = Die()
        self.players = [Player("Player 1"), Player("Player 2")] # 2 players in game, record the records of players 1 and 2
        self.current_player_index = 0 # initizating player will start at 0
    
    def switch_player(self): # defining switch player 
        self.current_player_index = (self.current_player_index + 1) % 2 # monitor player turn and ensures to change players turn
    
    def get_current_player(self): 
        return self.players[self.current_player_index] # get player turn and return on who indication on players turn
    
    def play_turn(self):
        player = self.get_current_player() # keeping track on whose player turn 
        turn_total = 0
        print(f"\n{player.name}'s turn!") # printing a message of the player's.name turn
        
        while True:
            action = input(f"ROLL: [ r ] or HOLD [ h ] ").strip().lower() # player inputs r or h to roll
            if action == 'r':
                roll_result = self.die.roll()
                print(f"Rolled: {roll_result}")
                if roll_result == 1: 
                    print("Rolled a 1! No points this turn.")
                    turn_total = 0 # resetting the turn back to 0
                    break
                else:
                    turn_total += roll_result
                    print(f"Turn Total: {turn_total}")
            elif action == 'h': # if player hold they would still retain their points until next turn decision
                player.add_score(turn_total)
                break
            else:
                print("Invalid input. Please enter 'r' or 'h'.")
        
        print(f"{player.name}'s total score: {player.score}")
    
    def determine_winner(self):
        for player in self.players:
            if player.score >= 100: # ensures if player has met the requirement if equal or greater than 100
                return player
        return None
    
    def play(self):
        print("Welcome to the Pig Game!") # starts the game with "welcome to the pig game"
        while True:
            self.play_turn()
            winner = self.determine_winner() # determines the player winner of the game
            if winner:
                print(f"\n{winner.name} wins with a score of {winner.score}!")
                break
            self.switch_player()


if __name__ == "__main__":
    game = Game()
    game.play()
