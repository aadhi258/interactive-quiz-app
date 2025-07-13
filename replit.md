# Quiz App

## Overview

This is a Flask-based quiz application that allows users to create interactive quizzes with multiple-choice questions and take them with immediate scoring. The application provides a web interface for quiz creation, management, and taking quizzes with real-time progress tracking.

## User Preferences

Preferred communication style: Simple, everyday language.
Project purpose: Resume/placement preparation - focus on technical skills demonstration.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database**: SQLAlchemy ORM with PostgreSQL (configured via DATABASE_URL environment variable)
- **Session Management**: Flask sessions with SECRET_KEY for security
- **Middleware**: ProxyFix for handling HTTPS redirects in production environments

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default templating system)
- **CSS Framework**: Bootstrap (dark theme variant)
- **Icons**: Font Awesome for consistent iconography
- **JavaScript**: Vanilla JavaScript for interactive quiz functionality

### Application Structure
```
├── app.py              # Main Flask application setup
├── main.py             # Entry point for deployment
├── models.py           # Database models
├── routes.py           # API endpoints and view functions
├── templates/          # HTML templates
├── static/            # CSS and JavaScript files
```

## Key Components

### Database Models
- **Quiz**: Stores quiz metadata (title, description, timestamps)
- **Question**: Contains question text and ordering within quizzes
- **Choice**: Multiple choice answers with correct/incorrect flags
- **QuizSession**: Tracks user attempts and scores
- **UserAnswer**: Records individual question responses (referenced but not fully implemented)

### Core Features
1. **Quiz Creation**: Create quizzes with titles and descriptions
2. **Question Management**: Add multiple-choice questions to quizzes
3. **Quiz Taking**: Interactive quiz interface with progress tracking
4. **Results Display**: Score calculation and performance feedback
5. **Quiz Management**: Edit and manage existing quizzes

### Route Structure
- `/` - Home page listing available quizzes
- `/create_quiz` - Quiz creation interface
- `/quiz/<id>/manage_questions` - Question management for specific quiz
- `/quiz/<id>/add_question` - Add questions to quiz
- Additional routes for quiz taking and results (referenced in templates)

## Data Flow

1. **Quiz Creation Flow**:
   - User creates quiz with title/description
   - System generates Quiz record
   - User adds questions with multiple choices
   - Questions and choices stored with relationships

2. **Quiz Taking Flow**:
   - User selects quiz from homepage
   - System loads questions with choices
   - User answers questions with real-time progress tracking
   - JavaScript handles local answer storage
   - Form submission creates QuizSession and UserAnswer records

3. **Results Flow**:
   - System calculates score based on correct answers
   - Performance metrics displayed (percentage, badges)
   - Session data stored for future reference

## External Dependencies

### Python Packages
- Flask: Web framework
- Flask-SQLAlchemy: Database ORM
- Werkzeug: WSGI utilities (ProxyFix middleware)

### Frontend Dependencies
- Bootstrap CSS: UI framework (via CDN)
- Font Awesome: Icon library (via CDN)
- Custom CSS: Application-specific styling

### Environment Variables
- `DATABASE_URL`: PostgreSQL connection string
- `SESSION_SECRET`: Flask session encryption key

## Deployment Strategy

### Configuration
- Uses environment variables for sensitive configuration
- Database connection pooling configured for production
- ProxyFix middleware for reverse proxy deployment
- Debug mode configurable via Flask settings

### Database Setup
- Models automatically create tables on app startup
- SQLAlchemy handles migrations and schema management
- Connection pooling with health checks (pool_pre_ping)

### Static Assets
- CSS and JavaScript served from `/static/` directory
- External CDN dependencies for Bootstrap and Font Awesome
- Custom styling in `static/css/style.css`

### Entry Points
- `main.py`: Primary entry point for deployment platforms
- `app.py`: Direct Flask application runner for development
- Configured for host `0.0.0.0:5000` for container deployment

## Notable Implementation Details

### Database Relationships
- Cascading deletes ensure data integrity when removing quizzes
- Proper foreign key relationships between Quiz → Question → Choice
- Session tracking for user attempts and scoring

### Frontend Interactivity
- JavaScript quiz functionality with progress tracking
- Local storage for answer persistence
- Keyboard navigation support
- Form validation and user feedback

### Incomplete Features
- UserAnswer model referenced but not fully implemented in routes
- Some template routes reference non-existent view functions
- Quiz editing functionality partially implemented