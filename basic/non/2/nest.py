def guest_fruit(fruit:str):
    if fruit == 'apple' or fruit == 'strawberry':
        print(fruit)        

    # red = ['apple', 'strawberry', 'cherry']
    # if fruit in red:
    #     print(fruit)
    # else:
    #     print('it''s not red')    

def guest_fruit_q(fruit:str, quantity:int):
    if fruit is not None:
        if quantity < 10:
            print("need more!")
        else:
            if fruit == 'apple' or fruit == 'strawberry':
                print(fruit)
            else:
                print('it''not red')
    else:
        print("it''s None")

# def guest_fruit(fruit:str, quantity:int):
#     red = ['apple', 'strawberry', 'cherry']
#     if fruit is None:
#         return print('It''s None')

#     if quantity < 10:
#         return print('need more')

#     if fruit in red:
#         print(fruit)
#     else:
#         print('it''s not red')  


if __name__ == '__main__':
    # fruit = input('please enter a fruit: ')
    fruit = 'apple'
    # guest_fruit(fruit)
    guest_fruit_q(fruit, 1)