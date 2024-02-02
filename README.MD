# Setup

- Create a virtual environment

```
python3 -m venv venv
```

- then activate it

```
source venv/bin/activate
```
- install all required packages by entering the command
```
pip install -r requirements.txt
```

- Create a ".env" file in order to make your settings.py more secure from anyone else, otherwise the code won't work properly. In case if you're not using ".env" file you need to change your settings.py database credintials and secret key. Afterwards, you need to apply migrations to your database.

```
python3 manage.py makemigrations
python3 manage.py migrate
```

- Finally, if you followed to every step correctly, your application must work. Launch it by typing the command

```
python3 manage.py runserver
```

- You can also check the application for functionality by launching the unit tests

```
python3 manage.py test
```

# End points

- api/v1/post [METHODS GET, POST]
- api/v1/post/id [METHODS GET, POST, PATCH, DELETE, PUT]
- api/v1/comment [METHODS GET, POST]
- api/v1/comment/id [METHODS GET, POST, DELETE, PATCH, PUT]
- dj-rest-auth/login [METHODS POST]
- dj-rest-auth/logout [METHODS GET, POST]
- dj-rest-auth/password/change [METHODS POST]
- dj-rest-auth/password/reset [METHODS POST]
- dj-rest-auth/password/reset/confirm [METHODS POST]
- dj-rest-auth/registration [METHODS POST]
- dj-rest-auth/registration/verify-email [METHODS POST]
- dj-rest-auth/registration/resend-email [METHODS POST]
- dj-rest-auth/user [METHODS GET, PUT, PATCH]
- api-auth/login [METHODS GET, POST]
- api-auth/logout [METHODS GET]

or you could just use a swagger to see all endpoints and methods that available, just visit the following route

- http://127.0.0.1:8000/swagger/

# Docker

To create an image 
```
docker build . -t drf
```
Run the image, so it creates a container
```
docker run -p 8000:8000 drf
```

# Documentations

to enhance your understanding of the specific package, you can read the documentations that I listed below

- [Documentation Django Rest](https://www.django-rest-framework.org/)
- [Documentation drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)
- [Documentation dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/)
- [Documentation django](https://docs.djangoproject.com/en/5.0/)