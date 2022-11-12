from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for index in question_data:
    question_text = index["question"]
    question_answer = index["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    if not quiz.still_has_questions():
        print("You've completed the quiz.")
        print(f"Your final score was {quiz.current_score} / {quiz.question_number}")