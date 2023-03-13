# Tutorials API

Django REST API to share links to tutorials

## Screenshots

### Docs page

![Home](./docs/screenshots/docs.png)

## Goals

App developed in order to put into practice my studies on Django REST.  
Some of the concepts I was able to put into practice:

- Serializers
- Model viewset
- API documentation
- Basic token auth
- Integration with third party lib

## Tools

[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)

## Run locally

The first thing to do is to clone the repository:

```sh
git clone https://github.com/ogaaabriel/tutorials.git
cd tutorials
```

Create a virtual environment to install dependencies in and activate it:

```sh
python -m venv venv
source venv/Scripts/activate
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:

```sh
python manage.py migrate
python manage.py runserver
```

And navigate to `http://localhost:8000/api/docs`.
