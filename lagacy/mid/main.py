from poker import Poker

if __name__ == "__main__":
    player = Poker.create_player("P1")
    dealer = Poker.start_game("blackjack")

    player.deposit(1000)
    # dealer.poker_game()
