def is_a_exist(voc: str) -> bool:
    if 'a' in voc:
        return True
    return False

def find_a(voc: str):
    voc = str(voc).lower()
    if is_a_exist(voc):
        for i in range(len(voc)):
            if voc[i] == 'a':
                print(f'a is in the {i+1}')
    else:
        return print('a is not in vocabulary')


voc = input('plz input a string: ')
find_a(voc)

# for i, a in enumerate(str(voc).lower()):
#     if a == 'a':
#         print(f'a is on the {i+1}')
