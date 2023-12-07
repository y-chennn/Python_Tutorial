SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def check_sub_sequences(list_one, list_two):
    n1 = len(list_one)
    n2 = len(list_two)
    return any(list_two[i:i+n1] == list_one for i in range(n2 - n1 + 1))
    
def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if check_sub_sequences(list_one, list_two):
        return SUBLIST
    if check_sub_sequences(list_two, list_one):
        return SUPERLIST
    return UNEQUAL

if __name__ == '__main__':
    a = [1, 2, 3]
    b = [1]

    print(sublist(a, b))