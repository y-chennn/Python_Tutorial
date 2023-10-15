def luhn_check(card_number):
    def digit_of(n):
        return [int(d) for d in str(n)][::-1]

    digit = digit_of(card_number)
    odd = digit[0::2]
    even = digit[1::2]

    checksum = sum(odd) + sum([sum(divmod(i * 2, 10)) for i in even])
    return checksum


def is_valid(card_number):
    return luhn_check(card_number) % 10 == 0


if __name__ == "__main__":
    card = 5301955844479782
    print(card, is_valid(card))
