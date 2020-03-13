# Backend configuration

## Packages

```bash
pipenv shell

pipenv install pip-tools==4.3.0

pip-compile --output-file requirements.txt requirements.in
pipenv install -r requirements.txt

pipenv install --dev black==19.10b0 autopep8==1.5
```

## Docker

* Build image: `docker build .`
  * Use `--no-cache` to force rebuilding the image.

### Docker Compose

* Run docker-compose detached (in background): `docker-compose up -d`
* Run docker-compose and force build: `docker-compose up -d --build`
* Close docker-compose container: `docker-compose down`

* When installing new packages, rebuild the image to avoid `Pipfile` and `Pipfile.lock` errors:

```bash
docker-compose down
docker-compose up -d --build
```

* To run with another `docker-compose` file: `docker-compose -f docker-compose-prod.yml up -d --build`

### Django commands

* Run commands *inside* the docker image: `docker-compose exec [service]`

* Make migrations: `docker-compose exec web python manage.py makemigrations`
* Migrate database: `docker-compose exec web python manage.py migrate --noinput`
* Create superuser: `docker-compose exec web python manage.py createsuperuser`
  * `admin@admin.com`
  * `admin`
  * `admin123`
* Create test user:
  * `test`
  * `test@test.com`
  * `test123456`
* Check predeploy: `docker-compose exec web python manage.py check --deploy`

#### Optional

* Install `psycopg`: `docker-compose exec web pipenv install psycopg2-binary==2.8.4`
* Install additional packages: `docker-compose exec web pipenv install dj-database-url==0.5.0 gunicorn==20.0.4`

## Deploy to Heroku

* `heroku create`.
* `heroku stack:set container -a [damp-dawn-44130]`
* `heroku addons:create heroku-postgresql:hobby-dev -a [damp-dawn-44130]`
* `heroku git:remote -a [damp-dawn-44130]`
* `git push heroku master`
* `heroku run python manage.py migrate`
* `heroku run python manage.py createsuperuser`
* `heroku open -a [damp-dawn-44130]`
* `heroku logs --tail`

## Resources

* [How to use Django, PostgreSQL, and Docker - William Vincent](https://wsvincent.com/django-docker-postgresql/)
* [Deploying Django to Heroku With Docker | TestDriven.io](https://testdriven.io/blog/deploying-django-to-heroku-with-docker/)
