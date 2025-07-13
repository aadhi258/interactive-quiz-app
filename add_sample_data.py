#!/usr/bin/env python3
"""
Script to add sample quizzes and questions to the database
"""

from app import app, db
from models import Quiz, Question, Choice
from datetime import datetime

def add_sample_data():
    with app.app_context():
        # Check if we already have sample data
        if Quiz.query.count() > 0:
            print("Sample data already exists. Skipping...")
            return
        
        # Sample Quiz 1: General Knowledge
        quiz1 = Quiz(
            title="General Knowledge Quiz",
            description="Test your general knowledge with these fun questions!"
        )
        db.session.add(quiz1)
        db.session.flush()
        
        # Questions for General Knowledge Quiz
        questions_data = [
            {
                "question": "What is the capital of France?",
                "choices": [
                    ("Paris", True),
                    ("London", False),
                    ("Berlin", False),
                    ("Madrid", False)
                ]
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "choices": [
                    ("Venus", False),
                    ("Mars", True),
                    ("Jupiter", False),
                    ("Saturn", False)
                ]
            },
            {
                "question": "What is the largest mammal in the world?",
                "choices": [
                    ("African Elephant", False),
                    ("Blue Whale", True),
                    ("Giraffe", False),
                    ("Polar Bear", False)
                ]
            },
            {
                "question": "In which year did World War II end?",
                "choices": [
                    ("1944", False),
                    ("1945", True),
                    ("1946", False),
                    ("1947", False)
                ]
            },
            {
                "question": "What is the chemical symbol for gold?",
                "choices": [
                    ("Go", False),
                    ("Gd", False),
                    ("Au", True),
                    ("Ag", False)
                ]
            }
        ]
        
        for i, q_data in enumerate(questions_data, 1):
            question = Question(
                quiz_id=quiz1.id,
                question_text=q_data["question"],
                question_order=i
            )
            db.session.add(question)
            db.session.flush()
            
            for j, (choice_text, is_correct) in enumerate(q_data["choices"], 1):
                choice = Choice(
                    question_id=question.id,
                    choice_text=choice_text,
                    is_correct=is_correct,
                    choice_order=j
                )
                db.session.add(choice)
        
        # Sample Quiz 2: Science Quiz
        quiz2 = Quiz(
            title="Science Quiz",
            description="Challenge yourself with these science questions!"
        )
        db.session.add(quiz2)
        db.session.flush()
        
        science_questions = [
            {
                "question": "What is the smallest unit of matter?",
                "choices": [
                    ("Molecule", False),
                    ("Atom", True),
                    ("Cell", False),
                    ("Electron", False)
                ]
            },
            {
                "question": "What gas do plants absorb from the atmosphere during photosynthesis?",
                "choices": [
                    ("Oxygen", False),
                    ("Nitrogen", False),
                    ("Carbon Dioxide", True),
                    ("Hydrogen", False)
                ]
            },
            {
                "question": "What is the speed of light in vacuum?",
                "choices": [
                    ("300,000 km/s", False),
                    ("299,792,458 m/s", True),
                    ("150,000 km/s", False),
                    ("500,000 km/s", False)
                ]
            },
            {
                "question": "Which organ in the human body produces insulin?",
                "choices": [
                    ("Liver", False),
                    ("Kidney", False),
                    ("Pancreas", True),
                    ("Heart", False)
                ]
            }
        ]
        
        for i, q_data in enumerate(science_questions, 1):
            question = Question(
                quiz_id=quiz2.id,
                question_text=q_data["question"],
                question_order=i
            )
            db.session.add(question)
            db.session.flush()
            
            for j, (choice_text, is_correct) in enumerate(q_data["choices"], 1):
                choice = Choice(
                    question_id=question.id,
                    choice_text=choice_text,
                    is_correct=is_correct,
                    choice_order=j
                )
                db.session.add(choice)
        
        # Sample Quiz 3: Programming Quiz
        quiz3 = Quiz(
            title="Programming Basics",
            description="Test your programming knowledge with these questions!"
        )
        db.session.add(quiz3)
        db.session.flush()
        
        programming_questions = [
            {
                "question": "What does HTML stand for?",
                "choices": [
                    ("Hypertext Markup Language", True),
                    ("High Tech Modern Language", False),
                    ("Home Tool Markup Language", False),
                    ("Hyperlink and Text Markup Language", False)
                ]
            },
            {
                "question": "Which of these is a Python web framework?",
                "choices": [
                    ("React", False),
                    ("Angular", False),
                    ("Flask", True),
                    ("jQuery", False)
                ]
            },
            {
                "question": "What does SQL stand for?",
                "choices": [
                    ("Structured Query Language", True),
                    ("Simple Query Language", False),
                    ("Standard Query Language", False),
                    ("System Query Language", False)
                ]
            }
        ]
        
        for i, q_data in enumerate(programming_questions, 1):
            question = Question(
                quiz_id=quiz3.id,
                question_text=q_data["question"],
                question_order=i
            )
            db.session.add(question)
            db.session.flush()
            
            for j, (choice_text, is_correct) in enumerate(q_data["choices"], 1):
                choice = Choice(
                    question_id=question.id,
                    choice_text=choice_text,
                    is_correct=is_correct,
                    choice_order=j
                )
                db.session.add(choice)
        
        # Commit all changes
        db.session.commit()
        print("Sample data added successfully!")
        print(f"Created {Quiz.query.count()} quizzes")
        print(f"Created {Question.query.count()} questions")
        print(f"Created {Choice.query.count()} choices")

if __name__ == '__main__':
    add_sample_data()