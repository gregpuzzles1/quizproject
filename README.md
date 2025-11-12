# Danjo Project

Welcome to the Danjo project! This repository is part of my "quizproject" and is my first implementation of a Danjo (Django) application.

## Overview

Danjo is a project developed for learning and experimenting with Django. It’s intended as a simple demo and a foundation for future projects, showcasing core ideas and project structure.

## Features

- Simple, beginner-friendly Django setup
- Modular organization for growth
- Uses SQLite out of the box for easy database management

## Getting Started

### Prerequisites

- Python (version 3.6 or newer recommended)
- Django (install via pip)
- SQLite (included by default with Python and Django)

### Installation

Clone the repository:
```sh
git clone https://github.com/gregpuzzles1/quizproject.git
```

Navigate to the project directory:
```sh
cd quizproject
```

Install Django using pip:
```sh
pip install django
```

### Running the Project

To start the development server, run:
```sh
python manage.py runserver
```
Then open your browser and go to `http://127.0.0.1:8000/`.

### Database

This project uses SQLite by default. The `db.sqlite3` file is included for immediate use with example data.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

## License

This repository is released under the MIT License.

---

*This is my first Danjo project—feedback and suggestions are appreciated!*
Project Tree:
```.
├── .gitignore
├── README.md
├── db.sqlite3
├── manage.py
├── quiz/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20250414_1644.py
│   │   ├── 0003_choice_is_correct.py
│   │   ├── __init__.py
│   │   └── __pycache__/
│   ├── models.py
│   ├── templates/
│   │   └── quiz/
│   │       ├── quiz.html
│   │       └── result.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── quizproject/
    ├── __init__.py
    ├── __pycache__/
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
