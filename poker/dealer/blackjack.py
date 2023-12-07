from ..base import DealerBase


class BlackjackDealer(DealerBase):
    def __init__(self, deck, game_name) -> None:
        super().__init__(deck, game_name)
        self.__game_name = game_name
        self.__deck = {
            "gamer": [],
            "dealer": [],
        }

    def poker_game(self):
        self.__deck["gamer"].append(self.deal_card())
        self.__deck["gamer"].append(self.deal_card())
        self.__deck["dealer"].append(self.deal_card())
        self.__deck["dealer"].append(self.deal_card())

        print(f"Dealer's card: [{self.__deck['dealer'][0]}, X]")
        print(
            f"Your card: {self.__deck['gamer']}, Total points: {self.__calculate(self.__deck['gamer'])}"
        )
        while True:
            if self.__is_blackjack(self.__deck["gamer"]):
                print("Blackjack!")
                break
            else:
                i = input("Do you want to hit (Y/n): ").lower()
                if i == "y":
                    print("Hit!")
                    self.__round("gamer")
                    if self.__bust("gamer") == True:
                        return print("Bust!")
                elif i == "n":
                    print("Stand!")
                    self.__round("dealer")
                    __gp = self.__calculate(self.__deck["gamer"])
                    __dp = self.__calculate(self.__deck["dealer"])
                    if self.__bust("dealer") == True:
                        return print("Bust! You win")
                    elif self.__is_blackjack(self.__deck["dealer"]):
                        return print("Blackjack! You lose!")
                    else:
                        if __gp > __dp:
                            return print("You win!")
                        elif __gp < __dp:
                            return print("You lose!")
                        else:
                            return print("Draw")
                else:
                    print("please enter Y/n.")

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

    def __round(self, gamer: str):
        self.__deck[gamer].append(self.deal_card())
        print(
            f"{gamer}'s card: {self.__deck[gamer]}, Total points: {self.__calculate(self.__deck[gamer])}"
        )
        if gamer == "dealer" and self.__calculate(self.__deck["dealer"]) < 17:
            return self.__round("dealer")

    def __bust(self, gamer: str):
        return True if self.__calculate(self.__deck[gamer]) > 21 else False

    def __is_blackjack(self, deck):
        if len(deck) == 2:
            has_a = any(v == "A" for v in deck)
            has_ten = any(v in ["10", "J", "Q", "K"] for v in deck)
            return has_a and has_ten
