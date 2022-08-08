# stock-management-api

**Although you can view this project on the site, it's no longer active or maintained. Still, you can open an issue or a PR if you find a critical bug, I'll fix it ASAP.**

***

A simple Stock Management API that was my very first project and built with Django Rest Framework. It has CRUD, schema, documents, API authentication and authorization features.

# Live showcase

## Registration & Authentication

- [API Registration](https://stockmanagementksenofanex.herokuapp.com/api/v1/rest-auth/registration/) 

- [API Login](https://stockmanagementksenofanex.herokuapp.com/api-auth/login/?next=/api/) 


## Pages


- [API Root](https://stockmanagementksenofanex.herokuapp.com/api/)

- [Materials](https://stockmanagementksenofanex.herokuapp.com/api/materials/)

- [Suppliers](https://stockmanagementksenofanex.herokuapp.com/api/suppliers/)

- [Currencies](https://stockmanagementksenofanex.herokuapp.com/api/currencies/)

- [Measurement Types](https://stockmanagementksenofanex.herokuapp.com/api/measurement-types/) 

## Documentation

- [Swagger Documents](https://stockmanagementksenofanex.herokuapp.com/swagger-docs/)

# Installation

## Clone the project

Depending on the choice of yours, you can clone the project in various ways. Either via IDE, Git Desktop or Git commands.

Whatever the case, make sure Git is installed and after cloning the project, you are at the same working directory with the project.

- Look below for cloning the project via bash:

```bash
$ git clone https://github.com/Ksenofanex/stock-management-api.git

$ cd stock-management-api

$ pwd
/stock-management-api
```

## Environment Variables

Before installing the project, you need a proper `.env` file. The project's [settings.py](stockmanagement_project/settings.py) module is depending on these variables.

The project has a fictional [env file](.env.example) for educational purposes. You can either manually create a `.env` file or enter the command below to the bash/terminal to clone a proper `.env` file:

```bash
$ cp .env.example .env
```

An example configuration for the `.env` file:

```
DEBUG=True
SECRET_KEY=itdb4-_wc!=*hgl3)h@v$#jy7bxingn(n+qklsdso%9yq&c5)!
```

- You can generate the `SECRET_KEY` via sites like [Djecrety](https://djecrety.ir/) and add it to the `.env` file.

> Set DEBUG to True while developing and testing in local/testing environments. Otherwise, set DEBUG to False.

After properly configuring the environment variables, you can proceed to the [Docker](https://github.com/Ksenofanex/stock-management-api#docker) or [Venv](https://github.com/Ksenofanex/stock-management-api#venv) section to initialize the project.

## Docker

Thanks to the magical technology of Docker, you can build and initialize the project with single command. Like hokus pokus!

- Make sure your OS contains Docker[^1] and Docker Compose[^2], Docker Desktop is open and your working directory is the same with the project.

```bash
$ pwd
/stock-management-api

$ docker-compose up
```

With that single line of command, Docker will take care of everything.

![Docker Compose GIF](https://i.imgur.com/91tbxPS.gif)

- After the building and initialization process, you must see this output:

![Docker successfully initialized project output](https://i.imgur.com/K7FIMMK.png)

Then you can start exploring the project from either http://localhost:8000/api/ or http://127.0.0.1:8000/api/. Happy coding!

> Remember, you must approve the created objects from the admin panel in order them to be visible in the API.

> You can access to the documentation of the project from this URLs (http://localhost:8000/swagger-docs/ or http://127.0.0.1:8000/swagger-docs/) to see all available endpoints.

## Venv

You prefer the traditional way, ha? Oki doki, no judgements.

- Make sure your working directory is the same with the project and virtualenv package is installed in your OS.

<details>
<summary>Windows</summary>

```bash
> pwd
/stock-management-api

> pip install virtualenv

> virtualenv env

> .\env\Scripts\activate

> pip install -r requirements.txt

> python manage.py makemigrations

> python manage.py migrate

> python manage.py runserver
```

![Virtualenv GIF](https://i.imgur.com/0IbCroR.gif)

</details>

<details>
<summary>Linux</summary>

```bash
$ pwd
/stock-management-api

$ pip3 install virtualenv

$ python3 -m venv env

$ source env/bin/activate

$ pip3 install requirements.txt

$ python3 manage.py makemigrations

$ python3 manage.py migrate

$ python3 manage.py runserver
```

</details>

- After the initialization process, you must see this output:

![Virtualenv success output](https://i.imgur.com/k3zGPJ3.png)

Then you can start exploring the project from either http://localhost:8000/api/ or http://127.0.0.1:8000/api/. Happy coding!

> Remember, you must approve the created objects from the admin panel in order them to be visible in the API.

> You can access to the documentation of the project from this URLs (http://localhost:8000/swagger-docs/ or http://127.0.0.1:8000/swagger-docs/) to see all available endpoints.

[^1]: https://www.docker.com/products/docker-desktop
[^2]: https://docs.docker.com/compose/install/
