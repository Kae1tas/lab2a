# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

def guess_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать его.")

    number_to_guess = random.randint(1, 10)

    attempts = 0
    while True:
        try:
            user_guess = int(input("Введите ваше предположение: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Слишком мало! Попробуйте снова.")
            elif user_guess > number_to_guess:
                print("Слишком много! Попробуйте снова.")
            else:
                print(f"Поздравляем! Вы угадали число {number_to_guess} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    guess_number()

#this words should be in develop