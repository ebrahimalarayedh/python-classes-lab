class Game():
    def __init__(self):
        self.turn= "X"
        self.tie= False
        self.winner= None
        self.board= {'a1': None, 'b1': None, 'c1': None,
                    'a2': None, 'b2': None, 'c2': None,
                    'a3': None, 'b3': None, 'c3': None,}
        self.stats = {"X": 0, "O": 0, "Ties": 0}
        self.play_is_on= True
    def start(self):
        print('Welcome to CLI-based Tic-Tac-Toe using Python Classes!')
        while self.play_is_on:
            self.play_game()

    def play_game(self):
        print('welcome to CLI-based tic-tac-toe utlizing Class Concept in python')
        while not self.winner and not self.tie:
            self.print_board()
            self.render()
            self.get_move()
            self.check_winner()
            self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()
        self.render()
        # Ask if they want to play again
        self.ask_replay()


    def print_board(self):
        b={}
        for k,v in self.board.items():
            if v:
                b[k]= f"  {v} "
            else:
                b[k]= f"    "
        
        print(f'''
                A    B    C
            1) {b["a1"]}|{b["b1"]}|{b["c1"]}
            -------|----|-------
            2) {b["a2"]}|{b["b2"]}|{b["c2"]}
            -------|----|-------
            3) {b["a3"]}|{b["b3"]}|{b["c3"]}
              
              ''')
    def print_message(self):
        if(self.tie):   
            print("Tie game!")
        elif(self.winner):
            print(f"{self.winner} wins the game!")
        else: 
            print(f"It's player {self.turn}'s turn!")
    def render(self):
        self.print_board()
        self.print_message()
    def get_move(self):
        move= input("enter the key of an empty space on the board: ").lower()
        while 1:
            if (move in self.board and self.board[move]==None):
                self.board[move]= self.turn
                break
            elif(move in self.board and self.board[move]):
                self.print_board()
                move=input("choose empty space!!")
            else:
                self.print_board()
                move=input("Choose valid space key!!")
    def check_winner(self):
        b= self.board
        winning_combinations= [
            ["a1","b1","c1"],["a2","b2","c2"],["a3","b3","c3"],
            ["a1","a2","a3"],["b1","b2","b3"],["c1","c2","c3"],
            ["a1","b2","c3"],["a3","b2","c1"]
        ]
        for winning_combination in winning_combinations:
            if(b[winning_combination[0]]==b[winning_combination[1]]==b[winning_combination[2]] == self.turn):
                self.winner= self.turn
                print(self.winner)
                return True
        return False
    def check_for_tie(self):
        b= self.board
        if(not self.winner):
            for space in b.values():
                if(not space):
                    return False
            self.tie= True
            return
        else:
            return False
    def switch_turn(self):
        self.turn= {"X": "O","O": "X"}[self.turn]
    def reset_game(self):
        self.turn = "X"
        self.tie = False
        self.winner = None
        self.board = {key: None for key in self.board}
    def ask_replay(self):
        if self.winner:
            self.stats[self.winner] += 1
        elif self.tie:
            self.stats["Ties"] += 1

        print(f"\nScoreboard: X - {self.stats['X']} | O - {self.stats['O']} | Ties - {self.stats['Ties']}")
        choice = input("Play again? (y/n): ").strip().lower()
        self.play_is_on = (choice == "y")
        if self.play_is_on:
            self.reset_game()
        else:
            print("Thanks for playing! ✌️")

game_instance = Game()
# game_instance.play_game()
game_instance.start()
