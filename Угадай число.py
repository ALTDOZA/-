from random import randint
from sys import exit

MAXIMUM_NUMBER = 100
GAME_NAME = "Угадай число"
ANON_NAME = "Анонимус"

if len(GAME_NAME) > 37:
    print(f"Ошибка! {GAME_NAME}: слишком длинное название игры!")
    exit()

wants_to_play = True
games = 0
total_attempts = 0

x = (39 - len(GAME_NAME)) // 2
y = 1 if len(GAME_NAME) % 2 == 0 else 0

print("* " * 20 + "*")
print("*" + " " * 39 + "*")
print("*" + " " * x + GAME_NAME.upper() + " " * (x + y) + "*")
print("*" + " " * 39 + "*")
print("* " * 20 + "*")
print()

print(f"Добро пожаловать в \"{GAME_NAME}\"!\n")

name = input("Как тебя зовут? ")
if not name:
    name = ANON_NAME

print(f"\n{name}, правила этой игры просты.")
print(f"Я загадаю число от 1 до {MAXIMUM_NUMBER}, а тебе надо его отгадать.\n")

while wants_to_play:

    print(f"Итак, {name}, я загадал число от 1 до {MAXIMUM_NUMBER}.\n")
    secret_number = randint(1, MAXIMUM_NUMBER)
    guess = 0
    attempts = 0
    games += 1

    while guess != secret_number:

        guess = input("Какое я загадал число? ")

        while not guess.isdigit() or not (1 <= int(guess) <= MAXIMUM_NUMBER):
            guess = input(f"Введи целое число от 1 до {MAXIMUM_NUMBER}: ")

        guess = int(guess)
        attempts += 1
        if guess > secret_number:
            print(f"Число {guess} больше загаданного числа.\n")
        elif guess < secret_number:
            print(f"Число {guess} меньше загаданного числа.\n")

    if 11 <= attempts % 100 <= 14:
        end = "ок"
    elif attempts % 10 == 1:
        end = "ку"
    elif 2 <= attempts % 10 <= 4:
        end = "ки"
    else:
        end = "ок"

    total_attempts += attempts

    print(f"{name}, поздравляю! Ты угадал, правильное число {guess}!")
    print(f"Ты потратил {attempts} попыт{end}.\n")

    again = input("Хочешь сыграть еще раз? (да/нет): ")

    while again != "да" and again != "нет":
        again = input("Просто напиши \"да\" или \"нет\": ")

    if again == "нет":
        wants_to_play = False

if 11 <= games % 100 <= 14:
    end = ""
elif games % 10 == 1:
    end = "у"
elif 2 <= games % 10 <= 4:
    end = "ы"
else:
    end = ""

average_attempts = round(total_attempts / games, 2)

if int(average_attempts) != average_attempts:
    end2 = "ки"
else:
    average_attempts = int(average_attempts)
    if 11 <= average_attempts % 100 <= 14:
        end2 = "ок"
    elif average_attempts % 10 == 1:
        end2 = "ку"
    elif 2 <= average_attempts % 10 <= 4:
        end2 = "ки"
    else:
        end2 = "ок"

print(f"\n{name}, спасибо за участие!")
print(f"Ты сыграл {games} игр{end}.")
print(f"В среднем ты сделал {average_attempts} попыт{end2} за игру.")
input()
