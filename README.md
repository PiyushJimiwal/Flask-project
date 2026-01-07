# Flask Project

A simple Flask web application with multiple routes and template rendering.

## Description

This is a beginner-friendly Flask project that demonstrates the basics of building a web application with Python. The application includes a home page and an about page, showcasing Flask's routing and template rendering capabilities.

## Features

- Home page with personalized greeting
- About page
- Template inheritance using Jinja2
- Clean navigation between pages
- Responsive HTML templates

## Technologies Used

- **Python** - Programming language
- **Flask** - Web framework
- **Jinja2** - Template engine
- **HTML** - Frontend markup

## Project Structure

```
First Flask Project/
│
├── app.py              # Main Flask application
├── Templates/          # HTML templates directory
│   ├── base.html       # Base template
│   ├── nav.html        # Navigation component
│   ├── index.html      # Home page template
│   └── about.html      # About page template
└── README.md           # Project documentation
```

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

4. Install Flask:
```bash
pip install flask
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
   - `/` - Home page
   - `/about` - About page

## Author

**Piyush Jimiwal**

## License

This project is open source and available for educational purposes.
