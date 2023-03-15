import os
import time


class QuizBrain:
    def timer(self):
        for sec in range(5, -1, -1):
            time.sleep(1)
            os.system('cls')
            print(sec)

        os.system('cls')

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q.{self.question_number} : {current_question.text} (TRUE / FALSE) ? :\n")
        self.check_answer(user_choice, current_question.answer)

    def check_answer(self, user_choice, correct_answer):
        os.system('cls')
        if user_choice.lower() == correct_answer.lower():
            print("YOU GOT IT RIGHT")
            self.score += 1
        else:
            print("THAT'S WRONG")
        print(f"The correct answer : {correct_answer}")
        print(f"Your current score : {self.score} / {self.question_number}")
