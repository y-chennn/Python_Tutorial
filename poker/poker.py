from .base import PokerDeck
from .dealer import BlackjackDealer

from enum import Enum


class Poker_game(Enum):
    BLACKJACK = 1


class Poker:
    @staticmethod
    def start_game(game_name: str):
        if game_name.upper() not in [game.name for game in Poker_game]:
            print("please enter correct game name. \n")
        else:
            if game_name.upper() == Poker_game.BLACKJACK.name:
                print(f"Welcome! Let's play {game_name}! \n")
                deck = PokerDeck(2)
                return BlackjackDealer(deck, game_name)
