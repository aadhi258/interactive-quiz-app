from flask import render_template, request, redirect, url_for, flash, jsonify, session
from app import app, db
from models import Quiz, Question, Choice, QuizSession, UserAnswer
from sqlalchemy import func
from datetime import datetime
import logging

@app.route('/')
def index():
    """Home page showing available quizzes"""
    quizzes = Quiz.query.order_by(Quiz.created_at.desc()).all()
    return render_template('index.html', quizzes=quizzes)

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    """Create a new quiz"""
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        
        if not title:
            flash('Quiz title is required!', 'danger')
            return render_template('create_quiz.html')
        
        quiz = Quiz(title=title, description=description)
        db.session.add(quiz)
        db.session.commit()
        
        flash('Quiz created successfully!', 'success')
        return redirect(url_for('manage_questions', quiz_id=quiz.id))
    
    return render_template('create_quiz.html')

@app.route('/quiz/<int:quiz_id>/manage_questions')
def manage_questions(quiz_id):
    """Manage questions for a specific quiz"""
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).order_by(Question.question_order).all()
    return render_template('manage_questions.html', quiz=quiz, questions=questions)

@app.route('/quiz/<int:quiz_id>/add_question', methods=['POST'])
def add_question(quiz_id):
    """Add a new question to a quiz"""
    quiz = Quiz.query.get_or_404(quiz_id)
    question_text = request.form.get('question_text')
    
    if not question_text:
        flash('Question text is required!', 'danger')
        return redirect(url_for('manage_questions', quiz_id=quiz_id))
    
    # Get the next question order
    max_order = db.session.query(func.max(Question.question_order)).filter_by(quiz_id=quiz_id).scalar() or 0
    
    question = Question(
        quiz_id=quiz_id,
        question_text=question_text,
        question_order=max_order + 1
    )
    db.session.add(question)
    db.session.commit()
    
    # Add choices
    choices_data = [
        (request.form.get('choice1'), request.form.get('correct') == '1'),
        (request.form.get('choice2'), request.form.get('correct') == '2'),
        (request.form.get('choice3'), request.form.get('correct') == '3'),
        (request.form.get('choice4'), request.form.get('correct') == '4')
    ]
    
    for i, (choice_text, is_correct) in enumerate(choices_data, 1):
        if choice_text:
            choice = Choice(
                question_id=question.id,
                choice_text=choice_text,
                is_correct=is_correct,
                choice_order=i
            )
            db.session.add(choice)
    
    db.session.commit()
    flash('Question added successfully!', 'success')
    return redirect(url_for('manage_questions', quiz_id=quiz_id))

@app.route('/quiz/<int:quiz_id>/delete_question/<int:question_id>')
def delete_question(quiz_id, question_id):
    """Delete a question from a quiz"""
    question = Question.query.get_or_404(question_id)
    
    if question.quiz_id != quiz_id:
        flash('Invalid question!', 'danger')
        return redirect(url_for('manage_questions', quiz_id=quiz_id))
    
    db.session.delete(question)
    db.session.commit()
    flash('Question deleted successfully!', 'success')
    return redirect(url_for('manage_questions', quiz_id=quiz_id))

@app.route('/quiz/<int:quiz_id>/take')
def take_quiz(quiz_id):
    """Start taking a quiz"""
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).order_by(Question.question_order).all()
    
    if not questions:
        flash('This quiz has no questions yet!', 'warning')
        return redirect(url_for('index'))
    
    # Store quiz session in Flask session
    session['quiz_session'] = {
        'quiz_id': quiz_id,
        'current_question': 0,
        'answers': {},
        'start_time': str(datetime.utcnow())
    }
    
    return render_template('take_quiz.html', quiz=quiz, questions=questions)

@app.route('/quiz/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    """Submit quiz answers and calculate score"""
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).order_by(Question.question_order).all()
    
    if not questions:
        flash('This quiz has no questions!', 'danger')
        return redirect(url_for('index'))
    
    # Get user name if provided
    user_name = request.form.get('user_name', 'Anonymous')
    
    # Create quiz session
    quiz_session = QuizSession(
        quiz_id=quiz_id,
        user_name=user_name,
        total_questions=len(questions)
    )
    db.session.add(quiz_session)
    db.session.flush()  # Get the session ID
    
    score = 0
    
    # Process each question's answer
    for question in questions:
        choice_id = request.form.get(f'question_{question.id}')
        
        if choice_id:
            choice = Choice.query.get(int(choice_id))
            if choice and choice.question_id == question.id:
                # Record the user's answer
                user_answer = UserAnswer(
                    session_id=quiz_session.id,
                    question_id=question.id,
                    choice_id=choice.id,
                    is_correct=choice.is_correct
                )
                db.session.add(user_answer)
                
                # Update score if correct
                if choice.is_correct:
                    score += 1
    
    # Update session score
    quiz_session.score = score
    db.session.commit()
    
    # Clear session data
    session.pop('quiz_session', None)
    
    return redirect(url_for('quiz_result', session_id=quiz_session.id))

@app.route('/result/<int:session_id>')
def quiz_result(session_id):
    """Display quiz results"""
    quiz_session = QuizSession.query.get_or_404(session_id)
    
    # Get detailed answers
    answers = UserAnswer.query.filter_by(session_id=session_id).all()
    
    return render_template('quiz_result.html', 
                         quiz_session=quiz_session, 
                         answers=answers)

@app.route('/quiz_list')
def quiz_list():
    """Display all quizzes for management"""
    quizzes = Quiz.query.order_by(Quiz.created_at.desc()).all()
    return render_template('quiz_list.html', quizzes=quizzes)

@app.route('/quiz/<int:quiz_id>/delete')
def delete_quiz(quiz_id):
    """Delete a quiz"""
    quiz = Quiz.query.get_or_404(quiz_id)
    db.session.delete(quiz)
    db.session.commit()
    flash('Quiz deleted successfully!', 'success')
    return redirect(url_for('quiz_list'))

@app.route('/quiz/<int:quiz_id>/edit', methods=['GET', 'POST'])
def edit_quiz(quiz_id):
    """Edit quiz details"""
    quiz = Quiz.query.get_or_404(quiz_id)
    
    if request.method == 'POST':
        quiz.title = request.form.get('title')
        quiz.description = request.form.get('description')
        
        if not quiz.title:
            flash('Quiz title is required!', 'danger')
            return render_template('create_quiz.html', quiz=quiz)
        
        db.session.commit()
        flash('Quiz updated successfully!', 'success')
        return redirect(url_for('manage_questions', quiz_id=quiz_id))
    
    return render_template('create_quiz.html', quiz=quiz)

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    flash('The requested page was not found.', 'danger')
    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    flash('An internal error occurred. Please try again.', 'danger')
    return redirect(url_for('index'))
