import random
from enum import Enum
from abc import ABC, abstractmethod


class Poker_game(Enum):
    BLACKJACK = 1


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
        return ranks

    def shuffle_deck(self):
        random.shuffle(self.cards)


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


class BlackjackDealer(DealerBase):
    def __init__(self, deck, game_name) -> None:
        super().__init__(deck, game_name)
        self.__game_name = game_name
        self.__d_deck = []
        self.__g_deck = []

    def poker_game(self):
        self.__d_deck.append(self.deal_card())
        self.__d_deck.append(self.deal_card())
        self.__g_deck.append(self.deal_card())
        self.__g_deck.append(self.deal_card())
        print(f"banker's card: [{self.__d_deck[0]}, X]")
        print(
            f"Your card: {self.__g_deck}, Total points: {self.__calculate(self.__g_deck)}"
        )
        while True:
            if self.__is_blackjact(self.__g_deck):
                print("Blackjack, you win.")
            elif self.__is_blackjact(self.__d_deck):
                print("Dealer blackjack, you win.")

            i = input("Do you want to hit (Y/n): ").lower()
            if i == "y":
                print("hit!")
                self.__hit(self.__g_deck)
                print(
                    f"Your card: {self.__g_deck}, Total points: {self.__calculate(self.__g_deck)}"
                )
                if self.__bust(self.__g_deck) == True:
                    print("Bust!")
                    break
            if i == "n":
                print("stand")
                self.__dealer_round()
                gamer_p = self.__calculate(self.__g_deck)
                dealer_p = self.__calculate(self.__d_deck)
                if self.__bust(self.__d_deck) == True:
                    print("Bust!")
                    print("You win!")
                    break
                else:
                    if gamer_p > dealer_p:
                        print("You win!")
                    elif gamer_p < dealer_p:
                        print("You lose!")
                    else:
                        print("Draw")
                    break
            else:
                print("please enter Y/n.")

    def __hit(self, deck: list):
        deck.append(self.deal_card())
        self.__bust(deck)

    def __calculate(self, deck: list):
        s = ["A", "J", "Q", "K"]
        m_deck = [int(v) for v in deck if v not in s]
        total = sum(m_deck)
        ace_num = deck.count("A")
        for v in deck:
            if v in ["J", "Q", "K"]:
                total += 10
            elif v == "A":
                total += 11

            while ace_num > 0 and total > 21:
                total -= 10
                ace_num -= 1
        return total

    def __bust(self, deck: list):
        sum = self.__calculate(deck)
        if sum > 21:
            return True

    def __dealer_round(self):
        print(
            f"Dealer's card: {self.__d_deck}, Total points: {self.__calculate(self.__d_deck)}"
        )
        while self.__calculate(self.__d_deck) < 17:
            self.__hit(self.__d_deck)
            print(
                f"Dealer's card: {self.__d_deck}, Total points: {self.__calculate(self.__d_deck)}"
            )

    def __is_blackjact(self, deck):
        has_a = any(v == "A" for v in deck)
        has_ten = any(v in ["10", "J", "Q", "K"] for v in deck)
        return has_a and has_ten


class Poker:
    @staticmethod
    def start_game(game_name):
        if game_name.upper() in [game.name for game in Poker_game]:
            print(f"Welcome! Let's play {game_name}! \n")
            deck = PokerDeck(2)
            return BlackjackDealer(deck, game_name)
        else:
            print("please enter correct game name. \n")


if __name__ == "__main__":
    dealer = Poker.start_game("blackjack")
    dealer.poker_game()
