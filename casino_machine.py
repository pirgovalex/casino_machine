import random
import time

class Symbol:
    """Represents a single symbol on the slot machine board."""

    def __init__(self, name, point_value):
        self.name = name
        self.point_value = point_value

    def __str__(self):
        return self.name

class SlotMachine:
    """Simulates a slot machine with a visual board, point values, and subtle time-based influence."""

    def __init__(self):
        self.symbols = ["A", "B", "C", "D", "E", "F"]#Winning char
        self.point_values = {"A": 100, "B": 200, "C": 300, "D": 400, "E": 500, "F": 600}#key,value relationship of winning chars
        self.board = []

    def generate_board(self):
        """Generates a 3x3 board with random symbols."""
        for _ in range(3):
            row = random.choices(self.symbols, k=3)
            self.board.append(row)
    def print_board(self):
        print("-" * 41)
        """Prints the slot machine board."""
        for row in self.board:
            print("\t|\t".join(str(symbol) for symbol in row) + "\t|\t")
            print("-" * 41)
    

    def calculate_score(self):
        """Calculates the total score based on the winning combination."""
        total_score = 0
        for row in self.board:
            if all(symbol == row[0] for symbol in row):
                total_score = sum(self.point_values[symbol] for symbol in row) * 3  # Triple points for horizontal win
                return total_score

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            total_score = sum(self.point_values[symbol] for symbol in self.board[0]) * 4 #Vertical win
            return total_score
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            total_score = sum(self.point_values[symbol] for symbol in self.board[0]) * 5  # points for diagonal win
            return total_score
        
        current_time = time.time_ns()
        
        subtle_boost = 0.02  # Increase chance by 2% between 22ms and 34ms
        if random.random() < 0.5+subtle_boost and 22000 <= current_time <= 34000:
    # Perform the reshuffle operation
            self.board[0][2] = random.choice(self.symbols)
        """     :
            if random.random() < 0.5 + subtle_boost:  # Adjust base chance (originally 0.5) alternative idea!
                self.board[0][2] = self.board[1][1]  # assign the same char for better chance of higher points via diagonal win"""
        return total_score  # No win

    def check_win(self):
        """Checks for horizontal and diagonal wins and returns the total score if applicable."""
        total_score = self.calculate_score()
        if total_score > 0:
            print(f"You win! Total score: {total_score}")
            return True
        else:
            print("Sorry, no win this time.")
            return False

        

    def play(self):
        """Simulates a single spin of the slot machine."""
        self.generate_board()
        self.print_board()

        current_time = time.time_ns() % 1000000  # Get milliseconds



        self.check_win()

    # Inform user about subtle time influence
        subtle_influence_text = "(There might be a very slight influence on the outcome based on the time you played.)"
        print(subtle_influence_text)
        
        print(f"Total execution time: {(current_time - start_time) / 1000000:.2f} milliseconds")


# Run

start_time = time.time_ns()
slot_machine = SlotMachine()
slot_machine.play()
