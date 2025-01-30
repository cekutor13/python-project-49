import random
import prompt
from brain_games.engine import run_game

RULE = "What is the result of the expression?"


def generate_round():
    """Генерирует один раунд игры: операнды и оператор."""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])
    question = f"{num1} {operator} {num2}"

    if operator == "+":
        correct_answer = str(num1 + num2)
    elif operator == "-":
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)

    return question, correct_answer


def main():
    """Запуск игры."""
    run_game(RULE, generate_round)


if __name__ == "__main__":
    main()
