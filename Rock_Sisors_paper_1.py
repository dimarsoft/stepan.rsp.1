from enum import Enum
import random
colvo_raunds = 5
raunds_win = 3
# print("jglkdjgldkf", b, c)
# print(f"hello {name}")

class GameResult(Enum):

    Win = 0
    Lost = 1
    Drew = 2 

    
ROCK = "r"
SCISSORS = "s"
PAPER = "p"

R_S_P = [ROCK, SCISSORS, PAPER]
R_S_P_dict = {    
    ROCK : "камень", 
    SCISSORS: "ножницы", 
    PAPER:"бумага"
    }

def test_win_men_str(men_choice, PS_choice) -> str:
    '''
    Проверяет выиграл ли игрок.

    '''
    if men_choice == ROCK and PS_choice == SCISSORS:
        return "Ты выиграл"
    if men_choice == SCISSORS and PS_choice == PAPER:
       return "Ты выиграл"
    if men_choice == PAPER and PS_choice == ROCK:
        return "Ты выиграл"
    if men_choice == ROCK and PS_choice == PAPER:
        return "Ты проиграл"
    if men_choice == SCISSORS and PS_choice == ROCK:
        return "Ты проиграл"
    if men_choice == PAPER and PS_choice == SCISSORS:
        return "Ты проиграл"

    if men_choice == PS_choice:
        return "Ничья"

def print_result(res: GameResult):
    if res == GameResult.Drew:
       print("Ничья")
    elif res == GameResult.Win:
        print("Ты выиграл")
    else:
        print("Ты проиграл")     

def test_win_men(men_choice, PS_choice) -> GameResult:
    '''
    Проверяет выиграл ли игрок.

    '''
    if men_choice == ROCK and PS_choice == SCISSORS:
        return GameResult.Win
    if men_choice == SCISSORS and PS_choice == PAPER:
       return GameResult.Win
    if men_choice == PAPER and PS_choice == ROCK:
        return GameResult.Win

    if men_choice == ROCK and PS_choice == PAPER:
        return GameResult.Lost

    if men_choice == SCISSORS and PS_choice == ROCK:
        return GameResult.Lost
    if men_choice == PAPER and PS_choice == SCISSORS:
        return GameResult.Lost

    if men_choice == PS_choice:
        return GameResult.Drew


def get_men_choice():
    m_choice = input(f"Напишите {ROCK} чтобы выбрать камень, {SCISSORS} чтобы ножницы, {PAPER} чтобы бумагу ")

    while m_choice not in R_S_P:
        m_choice = input(f"Ошибка. Напишите {ROCK} чтобы выбрать камень, {SCISSORS} чтобы ножницы, {PAPER} чтобы бумагу ")
    return m_choice

def get_pc_choice(prev_men_state: GameResult, prev_choice: str) -> str:

    if prev_men_state == GameResult.Drew:
        return random.choice(R_S_P)

    # человек проиграл == компьютер выиграл
    if prev_men_state == GameResult.Lost:
        if prev_choice == ROCK:
            return SCISSORS
        elif prev_choice == SCISSORS:
            return PAPER
        return ROCK

    if prev_choice == ROCK:
        return PAPER
    elif prev_choice == SCISSORS:
        return ROCK
    return SCISSORS



print(f"Привет это игра камень ножницы бумага каждая игра состоит из {colvo_raunds}  раундов выйграв в {raunds_win} вы или копьютер автамотически выйгрываете")

men_choice = get_men_choice()

PS_choice = random.choice(R_S_P)
print("Компьютер выбирает", R_S_P_dict[PS_choice])

result = test_win_men(men_choice, PS_choice)
print_result(result)

while True:
    answer = input("Продолжим? yes(y)/no(n): ")
    if answer == 'n':
        break
    men_choice = get_men_choice()
    PS_choice = get_pc_choice(result, PS_choice)
    print("Компьютер выбирает", R_S_P_dict[PS_choice])

    result = test_win_men(men_choice, PS_choice)

    print_result(result)
