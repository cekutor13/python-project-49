import random
import math
from brain_games.engine import run_game

RULE = "Find the greatest common divisor of given numbers."


def generate_round():
    """Генерирует два случайных числа и их НОД."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))  # Используем встроенную функцию НОД

    return question, correct_answer


def main():
    """Запуск игры."""
    run_game(RULE, generate_round)


if __name__ == "__main__":
    main()
