# quiz_game.py

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Silver", "D. Hydrogen"],
        "answer": "B"
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. William Shakespeare", "B. George Orwell", "C. Charles Dickens", "D. Jane Austen"],
        "answer": "A"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Quartz"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["A. 1905", "B. 1912", "C. 1918", "D. 1925"],
        "answer": "B"
    }
]

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
    print(f"\nYour final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz(questions)
