import random
colvo_raunds = 5
raunds_win = 3
# print("jglkdjgldkf", b, c)
# print(f"hello {name}")

ROCK = "r"
SCISSORS = "s"
PAPER = "p"

R_S_P = [ROCK, SCISSORS, PAPER]
R_S_P_dict = {    
    ROCK : "камень", 
    SCISSORS: "ножницы", 
    PAPER:"бумага"
    }

def test_win_men(men_choice, PS_choice) -> str:
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
    if men_choice == PAPER and PS_choice == PAPER:
        return "Ничья"
    if men_choice == SCISSORS and PS_choice == SCISSORS:
        return "Ничья"
    if men_choice == ROCK and PS_choice == ROCK:
        return "Ничья"
        
print(f"Привет это игра камень ножницы бумага каждая игра состоит из {colvo_raunds}  раундов выйграв в {raunds_win} вы или копьютер автамотически выйгрываете")

men_choice = input(f"Напишите {ROCK} чтобы выбрать камень, {SCISSORS} чтобы ножницы, {PAPER} чтобы бумагу ")

while men_choice not in R_S_P:
    men_choice = input(f"Напишите {ROCK} чтобы выбрать камень, {SCISSORS} чтобы ножницы, {PAPER} чтобы бумагу ")

#while men_choice != "r" or "s" or "p":
#    men_choice = input("Введите r, s или p")

# R_S_P = ["Rock - камень", "Scissors - ножницы", "Paper - бумага"]
PS_choice = random.choice(R_S_P)
print("Компьютер выбирает", R_S_P_dict[PS_choice])

result = test_win_men(men_choice, PS_choice)

print(result)

men_choice = input(f"Напишите {ROCK} чтобы выбрать камень, {SCISSORS} чтобы ножницы, {PAPER} чтобы бумагу ")