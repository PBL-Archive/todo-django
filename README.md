# Todo Django
Todo App website to demonstrate Django CRUD operations.

## Screenshots
![Demonstration](https://github.com/baijudodhia/todo-django/blob/master/readme-assets/0.png)

## Setup

1. Clone this repository.
2. Open settings.py -> empty the ALLOWED_HOSTS list and set DEBUG=True
3. Open command line inside the project folder.
4. Run the commands below in cmd - 
```bash
venv/Scripts/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```
5. Open http://localhost:8000/ in your browser

## Deploy to Heroku

You can deploy this app yourself to Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://devcenter.heroku.com/articles/deploying-python)
