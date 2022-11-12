def check_answer(correct_answer, user_answer):
    if correct_answer.answer.lower() == user_answer.lower():
        return True
    return False


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):

        current_item = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_item.text}. (True/False)")
        if check_answer(current_item, user_answer):
            self.current_score += 1
            print("You got it right")

        else:
            print("You failed.")
        print(f"Correct answer was: {current_item.answer}")
        print(f"Your current score is {self.current_score}/{self.question_number}")
        print("\n")
