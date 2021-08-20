class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        question_number = self.question_number
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {self.question_list[question_number].text} (True/False): ")
        if answer.lower() == self.question_list[question_number].answer.lower():
            return True
        else:
            return False

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

