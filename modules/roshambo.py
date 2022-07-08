class Game:
    def __init__ (self, _player1, _player2):
        self.player1 = _player1
        self.player2 = _player2
    
    def rock_vs_scissors(_player1_choice, _player2_choice):
        if _player1_choice == "rock" and _player2_choice == "scissors":
            return f"Player 1 wins by playing {_player1_choice}"

    def rock_vs_paper(_player1_choice, _player2_choice):
        if _player1_choice == "rock" and _player2_choice == "paper":
            return f"Player 2 wins by playing {_player2_choice}"
    
    def paper_vs_rock(_player1_choice, _player2_choice):
        if _player1_choice == "paper" and _player2_choice == "rock":
            return f"Player 1 wins by playing {_player1_choice}"

    def paper_vs_scissors(_player1_choice, _player2_choice):
        if _player1_choice == "paper" and _player2_choice == "scissors":
            return f"Player 2 wins by playing {_player2_choice}"

    def scissors_vs_paper(_player1_choice, _player2_choice):
        if _player1_choice == "scissors" and _player2_choice == "paper":
            return f"Player 1 wins by playing {_player1_choice}"

    def scissors_vs_rock(_player1_choice, _player2_choice):
        if _player1_choice == "scissors" and _player2_choice == "rock":
            return f"Player 2 wins by playing {_player2_choice}"
    
    # def rock_vs_rock(_player1_choice, _player2_choice):
    #     if _player1_choice == "rock" and _player2_choice == "rock":
    #         return
    
    # def paper_vs_paper(_player1_choice, _player2_choice):
    #     if _player1_choice == "paper" and _player2_choice == "paper":
    #         return
    
    # def scissors_vs_scissors(_player1_choice, _player2_choice):
    #     if _player1_choice == "scissors" and _player2_choice == "scissors":
    #         return
    
