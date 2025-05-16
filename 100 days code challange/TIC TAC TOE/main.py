import random

tic_tac = {
    7:"___|",8:"___",9:"|___",
    4:"___|",5:"___",6:"|___",
    1:"   |",2:"   ",3:"|   "
}
def alredy_in(number):
    place = tic_tac[number]
    if "X" in place or "O" in place:
        return True
    return False

def choice(who, number):

    if who == "user":
        symbol = "X"
    else:
        symbol = "O"

    if number == 1:
        tic_tac[number] = f' {symbol} |'
    elif number == 2:
        tic_tac[number] = f' {symbol} '
    elif number == 3:
        tic_tac[number] = f'| {symbol} '
    elif number == 4:
        tic_tac[number] = f'_{symbol}_|'
    elif number == 5:
        tic_tac[number] = f'_{symbol}_'
    elif number == 6:
        tic_tac[number] = f'|_{symbol}_'
    elif number == 7:
        tic_tac[number] = f'_{symbol}_|'
    elif number == 8:
        tic_tac[number] = f'_{symbol}_'
    elif number == 9:
        tic_tac[number] = f'|_{symbol}_'

    return tic_tac

def victory(symbol):

    if symbol in tic_tac[7] and symbol in tic_tac[8] and symbol in tic_tac[9]:
        return True
    elif symbol in tic_tac[4] and symbol in tic_tac[5] and symbol in tic_tac[6]:
        return True
    elif symbol in tic_tac[1] and symbol in tic_tac[2] and symbol in tic_tac[3]:
        return True
    elif symbol in tic_tac[1] and symbol in tic_tac[4] and symbol in tic_tac[7]:
        return True
    elif symbol in tic_tac[2] and symbol in tic_tac[5] and symbol in tic_tac[8]:
        return True
    elif symbol in tic_tac[3] and symbol in tic_tac[6] and symbol in tic_tac[9]:
        return True
    elif symbol in tic_tac[2] and symbol in tic_tac[5] and symbol in tic_tac[8]:
        return True
    elif symbol in tic_tac[1] and symbol in tic_tac[5] and symbol in tic_tac[9]:
        return True
    elif symbol in tic_tac[7] and symbol in tic_tac[5] and symbol in tic_tac[3]:
        return True
    else:
        return False
        
def victory2(symbol):
    winning_combinations = [
        [7, 8, 9], [4, 5, 6], [1, 2, 3],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]
    
    for combo in winning_combinations:
        if all(symbol in tic_tac[num] for num in combo):
            return True
    return False
    
while True:
    print(f'{tic_tac[7]}{tic_tac[8]}{tic_tac[9]}')
    print(f'{tic_tac[4]}{tic_tac[5]}{tic_tac[6]}')
    print(f'{tic_tac[1]}{tic_tac[2]}{tic_tac[3]}')
    user_choice = int(input('Chose a number betwen 1 and 9: '))
    check = alredy_in(user_choice)

    if check:
        print('Not valid Position')
        continue

    while True:
        pc_choice = random.randint(1,9)
        if pc_choice != user_choice:
            check = alredy_in(pc_choice)
            if check:
                continue
            else:
                break
    
    tic_tac = choice(who="user", number=user_choice)
    check2= victory("X")
    if check2:
        print(f'{tic_tac[7]}{tic_tac[8]}{tic_tac[9]}')
        print(f'{tic_tac[4]}{tic_tac[5]}{tic_tac[6]}')
        print(f'{tic_tac[1]}{tic_tac[2]}{tic_tac[3]}')
        print("User WON!!!")
        break

    tic_tac = choice(who="pc", number=pc_choice)
    check2= victory("O")
    if check2:
        print(f'{tic_tac[7]}{tic_tac[8]}{tic_tac[9]}')
        print(f'{tic_tac[4]}{tic_tac[5]}{tic_tac[6]}')
        print(f'{tic_tac[1]}{tic_tac[2]}{tic_tac[3]}')
        print("PC WON!!!")
        break
