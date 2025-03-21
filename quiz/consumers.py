import json
from channels.generic.websocket import AsyncWebsocketConsumer

class QuizConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        student_id = data.get("student_id", "Unknown")
        quiz_id = data.get("quiz_id", "Unknown")
        answers = data.get("answers", {})

        # Correct answer key (add topics for each question)
        correct_answers = {
            "q1": {"answer": "A", "topic": "Mathematics - Algebra"},
            "q2": {"answer": "C", "topic": "Science - Newton's Laws"},
            "q3": {"answer": "B", "topic": "History - World War II"},
            "q4": {"answer": "D", "topic": "Geography - Continents"},
            "q5": {"answer": "A", "topic": "English - Grammar"},
        }

        # Evaluate the quiz
        total_questions = len(correct_answers)
        correct_count = 0
        incorrect_feedback = []

        for q, ans in answers.items():
            if correct_answers.get(q) and correct_answers[q]["answer"] == ans:
                correct_count += 1
            else:
                topic = correct_answers[q]["topic"]
                correct_ans = correct_answers[q]["answer"]
                incorrect_feedback.append(f"Q{q[-1]}: Revise {topic}. Correct answer: {correct_ans}")

        # Calculate Score
        score_percentage = (correct_count / total_questions) * 100

        # Generate AI feedback based on performance
        if score_percentage >= 90:
            general_feedback = "Excellent performance! Keep it up!"
        elif score_percentage >= 60:
            general_feedback = "Good job! Revise the missed topics."
        else:
            general_feedback = "Needs improvement. Consider reviewing key concepts."

        # Response
        response = {
            "total_correct": correct_count,
            "total_incorrect": total_questions - correct_count,
            "score_percentage": score_percentage,
            "general_feedback": general_feedback,
            "personalized_feedback": incorrect_feedback,
            "chart_data": [correct_count, total_questions - correct_count],
        }

        await self.send(text_data=json.dumps(response))
