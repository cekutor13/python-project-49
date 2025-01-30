import random
import prompt

def is_even(number):
    """Проверяет, является ли число четным."""
    return number % 2 == 0

def main():
    """Основная логика игры Brain Even."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    for _ in range(3):  # Три раунда
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ").strip().lower()
        correct_answer = "yes" if is_even(number) else "no"

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при первой ошибке

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
