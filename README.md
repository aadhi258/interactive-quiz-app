# Interactive Quiz Application

A full-stack web application built with Flask and PostgreSQL that enables users to create, manage, and take interactive quizzes with real-time scoring and detailed analytics.

## 🚀 Live Demo

[View Live Application](https://your-deployment-url.replit.app) <!-- Replace with actual deployment URL -->

## 📋 Features

### Quiz Management
- ✅ Create and edit quizzes with custom titles and descriptions
- ✅ Add multiple-choice questions with 2-4 answer options
- ✅ Organize questions with custom ordering
- ✅ Delete and modify existing content

### Interactive Quiz Taking
- ✅ Single-page quiz interface with smooth navigation
- ✅ Real-time progress tracking with visual progress bar
- ✅ Keyboard navigation support (arrow keys)
- ✅ Answer persistence using local storage
- ✅ Form validation ensuring all questions are answered

### Scoring & Results
- ✅ Automatic scoring with immediate results
- ✅ Detailed question-by-question breakdown
- ✅ Performance analytics with percentage scores
- ✅ Session tracking with timestamps
- ✅ Performance badges based on score ranges

### User Experience
- ✅ Responsive design for mobile and desktop
- ✅ Dark theme with Bootstrap styling
- ✅ Intuitive navigation with breadcrumbs
- ✅ Error handling with user-friendly messages

## 🛠️ Technical Stack

### Backend
- **Flask** - Python web framework
- **SQLAlchemy** - ORM for database operations
- **PostgreSQL** - Relational database
- **Gunicorn** - WSGI HTTP server

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with custom properties
- **JavaScript (ES6+)** - Interactive functionality
- **Bootstrap 5** - Responsive UI framework
- **Font Awesome** - Icon library

### Database Schema
- **Quiz** - Stores quiz metadata
- **Question** - Contains quiz questions
- **Choice** - Stores answer options
- **QuizSession** - Tracks user attempts
- **UserAnswer** - Records individual responses

## 🏗️ Architecture

```
├── app.py                 # Flask application setup and configuration
├── models.py              # Database models and relationships
├── routes.py              # API endpoints and view functions
├── templates/             # HTML templates with Jinja2
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage with quiz listing
│   ├── create_quiz.html  # Quiz creation form
│   ├── take_quiz.html    # Interactive quiz interface
│   └── quiz_result.html  # Results display
├── static/               # Static assets
│   ├── css/style.css     # Custom styling
│   └── js/quiz.js        # Interactive functionality
└── requirements.txt      # Python dependencies
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11+
- PostgreSQL
- Git

### Local Development
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/quiz-app.git
   cd quiz-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**
   ```bash
   export DATABASE_URL="postgresql://username:password@localhost/quiz_db"
   export SESSION_SECRET="your-secret-key-here"
   ```

4. **Initialize database**
   ```bash
   python -c "from app import app, db; app.app_context().push(); db.create_all()"
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open http://localhost:5000 in your browser

## 📊 Database Schema

### Entity Relationship Diagram
```
Quiz (1) ─────────── (Many) Question (1) ─────────── (Many) Choice
 │                                                        │
 │                                                        │
 └─── (1) QuizSession (Many) ─────────── (Many) UserAnswer ─┘
```

### Key Relationships
- One Quiz can have many Questions
- One Question can have many Choices
- One Quiz can have many QuizSessions
- One QuizSession can have many UserAnswers

## 🎯 Usage Examples

### Creating a Quiz
1. Navigate to "Create Quiz" in the navigation
2. Enter quiz title and description
3. Add questions with multiple choice answers
4. Mark the correct answer for each question
5. Save and preview your quiz

### Taking a Quiz
1. Select a quiz from the homepage
2. Navigate through questions using Next/Previous buttons
3. Use arrow keys for quick navigation
4. Submit when all questions are answered
5. View detailed results with correct answers

## 🔧 Configuration

### Environment Variables
- `DATABASE_URL` - PostgreSQL connection string
- `SESSION_SECRET` - Flask session encryption key
- `FLASK_ENV` - Development/production environment

### Database Configuration
- Connection pooling with health checks
- Automatic table creation on startup
- Cascading deletes for data integrity

## 🚀 Deployment

### Production Deployment
1. **Set production environment variables**
2. **Configure PostgreSQL database**
3. **Deploy using Gunicorn**
   ```bash
   gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
   ```

### Replit Deployment
1. Fork this repository on Replit
2. Configure environment variables in Secrets
3. Run the application using the configured workflow

## 📈 Performance Features

- **Optimized Queries** - Efficient database queries with proper indexing
- **Session Management** - Secure session handling with cookies
- **Error Handling** - Comprehensive error handling with user feedback
- **Responsive Design** - Mobile-first approach with Bootstrap

## 🔒 Security Features

- **Input Validation** - Server-side validation for all user inputs
- **SQL Injection Prevention** - Parameterized queries using SQLAlchemy
- **Session Security** - Encrypted session cookies
- **Error Handling** - Secure error messages without information leakage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Bootstrap for the responsive UI framework
- Font Awesome for the icon library
- Flask community for excellent documentation
- PostgreSQL for robust database functionality

---

⭐ **Star this repository if you found it helpful!**