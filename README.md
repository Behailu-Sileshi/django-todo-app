<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Taskly</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/behailu-sileshi/django-todo-app.svg)](https://github.com/behailu-sileshi/django-todo-app/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/behailu-sileshi/django-todo-app.svg)](https://github.com/behailu-sileshi/django-todo-app/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A simple yet functional to-do app built with Django, designed for learning purposes and showcasing skills.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Taskly is a simple yet powerful to-do application built with Django to manage tasks efficiently. It allows users to create tasks, categorize them, and manage deadlines. The app is intended for learning purposes and to showcase Django development skills.

The project is structured to highlight Django’s key features like custom models, migrations, and working with MySQL databases.

## 🏁 Getting Started <a name = "getting_started"></a>

Follow the steps below to set up this project locally for development and testing.

### Prerequisites

You will need the following installed on your system:

- Python 3.8+
- Pipenv for dependency management
- MySQL database server

### Installing

1. Clone the repository to your local machine:
   ```bash
        git clone https://github.com/behailu-sileshi/django-todo-app.git
        cd django-todo-app
   ```

2. Install dependencies:
   ```bash
        pipenv install --dev
   ```

3. Activate the virtual environment:
   ```bash
         pipenv shell
   ```

4. Create a `.env` file in the root directory with the following content:
   ```plaintext
        SECRET_KEY=your-secret-key
        DEBUG=True
        NAME='taskly'         # MySQL Database Name
        HOST='localhost'      # Database Host
        USER='root'           # MySQL Username
        PASSWORD='your-password'  # MySQL Password
   ```

5. Run migrations to set up the database schema:
   ```bash
        python manage.py migrate
   ```

6. Create a superuser to access the Django admin panel:
   ```bash
        python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
        python manage.py runserver
   ```

## 🔧 Running the tests <a name = "tests"></a>

To run the tests, use the following command:

```bash
    pytest
```



## 🎈 Usage <a name="usage"></a>
Once the server is running, navigate to http://127.0.0.1:8000/ to use the application.
Log in with your superuser credentials to access the admin panel and manage tasks.

- Create categories and tasks, and assign deadlines for efficient task management.


## 📚 API Documentation <a name="api-documentation"></a>

For detailed API documentation, visit the [API Documentation](http://127.0.0.1:8000/api-docs/), which provides an interactive interface to test all available endpoints.

Some example endpoints you can interact with are:
- `/todo/tasks/` - View all tasks.
- `/todo/categories/` - View all categories.
- `/todo/tasks/<id>/` - View a specific task by ID.
- `/todo/categories/<id>/` - View a specific category by ID.


## 🚀 Deployment <a name = "deployment"></a>

*This project is intended for local development and is being showcased on GitHub.*


## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com/) - Web Framework
- [MySQL](https://www.mysql.com/) - Database
- [Pipenv](https://pipenv.pypa.io/en/latest/) - Dependency Management

## ✍️ Authors <a name = "authors"></a>

- [@Behailu-Sileshi](https://github.com/behailu-sileshi) - Developer & Maintainer

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Django documentation for being an excellent resource.
- Open-source libraries and tools used in the project.
- Inspiration from various task management apps.


