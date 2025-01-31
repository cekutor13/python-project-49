import random
from brain_games.engine import run_game

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Определяет, является ли число простым."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    """Генерирует число и его правильный ответ."""
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    question = str(number)
    return question, correct_answer


def main():
    """Запуск игры."""
    run_game(RULE, generate_round)


if __name__ == "__main__":
    main()

