# Flask Project

A Flask web application with user management system featuring CRUD operations and SQLAlchemy database integration.

## Description

This Flask project demonstrates full-stack web development with Python, including database management, user authentication forms, and CRUD (Create, Read, Update, Delete) operations. The application features a complete user management system with a SQLite database.

## Features

- **User Management System** - Complete CRUD functionality
- **Database Integration** - SQLAlchemy ORM with SQLite
- **User Registration** - Add new users via login form
- **User Display** - View all registered users on homepage
- **Update Users** - Modify existing user credentials
- **Delete Users** - Remove users from database
- **Template Inheritance** - Using Jinja2
- **Responsive Design** - Bootstrap 5 integration
- **Clean Navigation** - Easy navigation between pages

## Technologies Used

- **Python** - Programming language
- **Flask** - Web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Database
- **Jinja2** - Template engine
- **Bootstrap 5** - CSS framework
- **HTML** - Frontend markup

## Project Structure

```
First Flask Project/
│
├── app.py              # Main Flask application with routes
├── instance/
│   └── user.db         # SQLite database
├── Templates/          # HTML templates directory
│   ├── base.html       # Base template with Bootstrap
│   ├── nav.html        # Navigation component
│   ├── index.html      # Home page - displays all users
│   ├── about.html      # About page
│   ├── login.html      # User registration form
│   └── update.html     # Update user form
├── static/             # Static files (CSS, JS, images)
└── README.md           # Project documentation
```

## Database Schema

### User Model
- `sno` - Primary key (Integer)
- `username` - User email (String, max 80 characters)
- `password` - User password (String, max 200 characters)
- `datetime` - Registration timestamp (DateTime)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/PiyushJimiwal/Flask-project.git
cd Flask-project
```

2. Create a virtual environment:
```bash
python -m venv .env
```

3. Activate the virtual environment:
   - **Windows:**
     ```bash
     .\.env\Scripts\Activate.ps1
     ```
   - **macOS/Linux:**
     ```bash
     source .env/bin/activate
     ```

4. Install required packages:
```bash
pip install flask flask-sqlalchemy
```

## Usage

1. Run the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

3. Available routes:
   - `/` - Home page (displays all users)
   - `/about` - About page
   - `/login` - Add new user
   - `/update/<sno>` - Update user by serial number
   - `/delete/<sno>` - Delete user by serial number

## Features in Detail

### Create User
Navigate to `/login` and fill in the form with username (email) and password. The user will be added to the database.

### View Users
The home page (`/`) displays all registered users in a table format.

### Update User
Click the update button next to any user to modify their credentials. The form will be pre-filled with current data.

### Delete User
Click the delete button next to any user to remove them from the database.

## Author

**Piyush Jimiwal**

## License

This project is open source and available for educational purposes.
