from enum import Enum
import random
#import math
#import enum

count_rounds = 5
rounds_win = 3

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

def print_result(res: GameResult):
    if res == GameResult.Drew:
       print("Ничья")
    elif res == GameResult.Win:
        print("Ты выиграл")
    else:
        print("Ты проиграл")     

def test_win_men(m_choice, pc_choice) -> GameResult:
    """
    Проверяет выиграл ли игрок.

    """
    if m_choice == PS_choice:
        return GameResult.Drew

    if m_choice == ROCK and pc_choice == SCISSORS:
        return GameResult.Win
    if m_choice == SCISSORS and pc_choice == PAPER:
       return GameResult.Win
    if m_choice == PAPER and pc_choice == ROCK:
        return GameResult.Win

    return GameResult.Lost

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



print(f"Привет это игра камень ножницы бумага каждая игра состоит из {count_rounds}  раундов выйграв в {rounds_win} вы или копьютер автамотически выйгрываете")

PS_choice = None
result = GameResult.Drew

pc_win_games = 0
men_win_games = 0
for round_number in range(count_rounds):
    print(f"Раунд {round_number+1}")

    men_choice = get_men_choice()
    PS_choice = get_pc_choice(result, PS_choice)
    print("Компьютер выбирает", R_S_P_dict[PS_choice])

    result = test_win_men(men_choice, PS_choice)

    print_result(result)

    if result == GameResult.Win:
        men_win_games += 1
    elif result == GameResult.Lost:
        pc_win_games += 1

    print(f"men wins = {men_win_games}, pc wins = {pc_win_games}")

    if men_win_games == rounds_win or pc_win_games == rounds_win:
        break

    answer = input("Продолжим? yes(y)/no(n): ")
    if answer == 'n':
        break

print("Игра закончена. Итог:")

if pc_win_games == men_win_games:
    print("Ничья")
elif pc_win_games > men_win_games:
    print("Выиграл ПК")
else:
    print("Выиграл игрок")

