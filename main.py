from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question["question"]  # Gets a hold of the key for the value (actual question in text form)
    question_answer = question["correct_answer"]  # Gets a hold of the key for the value (actual answer in text form)
    new_question = Question(question_text, question_answer)  # creates a Question object from each entry in
    # question_data
    question_bank.append(new_question)  # This appends each question into question bank.


quiz = QuizBrain(question_bank)
quiz.next_question()
still_has_questions = True

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")




