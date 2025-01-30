import prompt

ROUNDS_COUNT = 3  # Количество раундов для победы


def run_game(rule, generate_round):
    """Запускает игру."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(rule)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").strip().lower()

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при первой ошибке

    print(f"Congratulations, {name}!")
