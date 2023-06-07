from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []

for one_question in question_data:
    q_t = (one_question["question"])
    q_a = (one_question["correct_answer"])
    new_q = Question(q_t, q_a)
    question_list.append(new_q)

quiz = QuizBrain(question_list)
while quiz.has_qs() == True: #,,Kóder,, gentleman
    quiz.next_q()
else:
    print("Koneeeeeec")
    print(f"_______________\nYour final score: {quiz.score}/{len(quiz.q_list)}\n_______________")
