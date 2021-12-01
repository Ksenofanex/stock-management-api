# stock-management-api

A simple Stock Management API that was built with Django Rest Framework. It has CRUD, schema, documents, API authentication and authorization features.

# Live showcase

### Authentication
***

- [API Registration Page](https://stockmanagementksenofanex.herokuapp.com/api/v1/rest-auth/registration/) 

- [API Login Page](https://stockmanagementksenofanex.herokuapp.com/api-auth/login/?next=/api/v1/materials) 

***
### Pages
***

- [Main Page](https://stockmanagementksenofanex.herokuapp.com/api/v1/materials/)

- [Material Detail Page](https://stockmanagementksenofanex.herokuapp.com/api/v1/materials/1/) 

- [Suppliers Page](https://stockmanagementksenofanex.herokuapp.com/api/v1/suppliers/)

- [Currencies Page](https://stockmanagementksenofanex.herokuapp.com/api/v1/currencies/)

- [Measurements Page](https://stockmanagementksenofanex.herokuapp.com/api/v1/measurements/) 

***
### Docs
***

- [Swagger-Documents Page](https://stockmanagementksenofanex.herokuapp.com/swagger-docs/)

- [Documents Page](https://stockmanagementksenofanex.herokuapp.com/docs/)
***

# Installation

**Clone the project**

Depending on the choice of yours, you can clone the project in various ways. Either via IDE, Git Desktop or Git commands.

Whatever the case, make sure Git is installed and after cloning the project, you are at the same working directory with the project.

Look below for cloning the project via Git:

```bash
git clone https://github.com/Ksenofanex/stock-management-api.git

cd stock-management-api

pwd
/stock-management-api
```

**Environment Variables**

* Before installing the project, you first need to configure environment variables in the [.env](stockmanagement_project/.env) file. The project's [settings.py](stockmanagement_project/settings.py) module is depending on these variables.
* You can generate the `SECRET_KEY` via sites like [this](https://djecrety.ir/) and add it to the [.env](https://github.com/Ksenofanex/stock-management-api/blob/35955cdabcb12e3cdb0d9bcff4efa23bee921682/stockmanagement_project/.env#L2) file.

* The layout of the [.env](stockmanagement_project/.env) file:

```
DEBUG=
SECRET_KEY=
```

* An example configuration for the [.env](stockmanagement_project/.env) file:

> Set DEBUG to True while developing and testing in local/testing environments. Otherwise, set DEBUG to False.

```
DEBUG=True
SECRET_KEY=itdb4-_wc!=*hgl3)h@v$#jy7bxingn(n+qklsdso%9yq&c5)!
```

* After properly configuring the environment variables, you can proceed to the [Docker](https://github.com/Ksenofanex/stock-management-api#docker) or [Venv](https://github.com/Ksenofanex/stock-management-api#venv) section to initialize the project.

## Docker

Thanks to the magical technology of Docker, you can build and initialize the project with single command. Like hokus pokus!

Make sure your OS contains Docker[^1] and Docker Compose[^2] and your working directory is the same with the project.

```bash
pwd
/stock-management-api

docker-compose up
```

With that single line of command, Docker will take care of everything. After building and initializing process, you must see this output:

![Docker successfully initialized project output](https://i.imgur.com/PiTp1cL.png)

Then you can start exploring the project from either http://localhost:8000/ or http://127.0.0.1:8000/. Happy coding!

## Venv

You prefer the traditional way, ha? Oki doki, no judgements.

Make sure your working directory is the same with the project and virtualenv package is installed in your OS.

For Windows:

```bash
pwd
/stock-management-api

virtualenv env

.\env\Scripts\activate

pip install -r requirements.txt
```

For Linux:

```bash
python3 -m venv env

source env/bin/activate

pip3 install requirements.txt
```

After activating the env, run the following commands:

```bash
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

![Venv success output](https://i.imgur.com/k3zGPJ3.png)

Then you can start exploring the project from either http://localhost:8000/ or http://127.0.0.1:8000/. Happy coding!

[^1]: https://www.docker.com/products/docker-desktop
[^2]: https://docs.docker.com/compose/install/
