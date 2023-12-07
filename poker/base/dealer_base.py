from abc import ABC, abstractmethod
from .deck import PokerDeck


class DealerBase(ABC):
    def __init__(self, deck: PokerDeck, game_name: str) -> None:
        self.__deck = deck
        self.__game_name = game_name

    def deal_card(self):
        if not self.__deck:
            print("Card Deck is empty")
            return None
        return self.__deck.cards.pop()

    @property
    def game(self):
        return self.__game_name

    @abstractmethod
    def poker_game():
        pass
