import random


class PokerDeck:
    def __init__(self, num=1) -> None:
        self.cards = self.create_deck(num)
        self.shuffle_deck()

    def create_deck(self, num):
        cards = []
        for _ in range(0, num):
            cards += self.init_deck()
        return cards

    def init_deck(self):
        # suits = ["Heart", "Diamond", "Club", "Spade"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return ranks * 4

    def shuffle_deck(self):
        random.shuffle(self.cards)
