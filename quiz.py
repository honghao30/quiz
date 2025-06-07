import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Rome", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    }
]

random.shuffle(questions)
score = 0

for idx, q in enumerate(questions, 1):
    print(f"Question {idx}: {q['question']}")
    for i, option in enumerate(q['options'], 1):
        print(f"  {i}. {option}")
    try:
        choice = int(input("Your answer (1-4): "))
        if q['options'][choice - 1].lower() == q['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")
    except (ValueError, IndexError):
        print(f"Invalid input. The correct answer is {q['answer']}\n")

print(f"You scored {score} out of {len(questions)}.")
