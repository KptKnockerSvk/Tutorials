class QuizBrain:

    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def next_q(self):
        current_q = self.q_list[self.q_num]
        self.q_num += 1
        user_answer = input(f"Question number {self.q_num}: {current_q.text} (True/False): ")
        self.check_answer(user_answer, current_q.answer)

    def has_qs(self):
        if self.q_num <len(self.q_list):
            return True
        else:
            return False

    def check_answer(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            print("Ding Dong")
            self.score += 1
        else:
            print("Bad bong :(((")
        print(f"Your score is: {self.score}/{len(self.q_list)}")
