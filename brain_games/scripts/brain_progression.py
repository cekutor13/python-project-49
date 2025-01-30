import random
from brain_games.engine import run_game

RULE = "What number is missing in the progression?"


def generate_progression(start, step, length):
    """Генерирует арифметическую прогрессию заданной длины."""
    return [start + step * i for i in range(length)]


def generate_round():
    """Создаёт раунд игры: скрытая позиция в прогрессии и правильный ответ."""
    start = random.randint(1, 20)  # Начало прогрессии
    step = random.randint(2, 5)    # Шаг прогрессии
    length = 10                    # Длина прогрессии

    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)  # Выбираем случайный индекс

    correct_answer = str(progression[hidden_index])  # Запоминаем правильный ответ
    progression[hidden_index] = ".."  # Заменяем число на ".."

    question = " ".join(map(str, progression))  # Формируем строку для вывода
    return question, correct_answer


def main():
    """Запуск игры."""
    run_game(RULE, generate_round)


if __name__ == "__main__":
    main()
