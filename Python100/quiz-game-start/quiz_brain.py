class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def ask_question(self):
        curr = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {curr.text} (True/False)?: ")
        self.check_answer(ans, curr.answer)

    def check_answer(self, user, answer):
        if user.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")


