from app import db
from datetime import datetime
from sqlalchemy import func

class Quiz(db.Model):
    """Model for storing quiz information"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship with questions
    questions = db.relationship('Question', backref='quiz', lazy=True, cascade='all, delete-orphan')
    # Relationship with quiz sessions
    sessions = db.relationship('QuizSession', backref='quiz', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Quiz {self.title}>'

class Question(db.Model):
    """Model for storing quiz questions"""
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_order = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with choices
    choices = db.relationship('Choice', backref='question', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Question {self.question_text[:50]}...>'

class Choice(db.Model):
    """Model for storing answer choices for questions"""
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    choice_text = db.Column(db.String(500), nullable=False)
    is_correct = db.Column(db.Boolean, default=False, nullable=False)
    choice_order = db.Column(db.Integer, nullable=False, default=1)
    
    def __repr__(self):
        return f'<Choice {self.choice_text[:30]}...>'

class QuizSession(db.Model):
    """Model for storing quiz session results"""
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_name = db.Column(db.String(100))  # Optional user name
    score = db.Column(db.Integer, default=0)
    total_questions = db.Column(db.Integer, default=0)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Store user answers as JSON or create separate model
    answers = db.relationship('UserAnswer', backref='session', lazy=True, cascade='all, delete-orphan')
    
    @property
    def percentage_score(self):
        if self.total_questions == 0:
            return 0
        return round((self.score / self.total_questions) * 100, 2)
    
    def __repr__(self):
        return f'<QuizSession {self.id} - Score: {self.score}/{self.total_questions}>'

class UserAnswer(db.Model):
    """Model for storing individual user answers"""
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('quiz_session.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    choice_id = db.Column(db.Integer, db.ForeignKey('choice.id'), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
    
    # Relationships
    question = db.relationship('Question', backref='user_answers')
    choice = db.relationship('Choice', backref='user_answers')
    
    def __repr__(self):
        return f'<UserAnswer {self.id} - Question: {self.question_id}, Choice: {self.choice_id}>'
