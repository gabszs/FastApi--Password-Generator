# FastAPI Password Generator

This is a project for generating passwords, pins, and complex passwords (with character or string injection). The project uses FastAPI to handle HTTP requests and responses.

## 🚀 Starting

This is a project developed using the FastAPI web framework, with the goal of providing a simple API for generating complex passwords. The API allows users to specify various parameters, including the length of the additional random characters, the number of passwords to generate, and whether or not to include punctuation characters. Additionally, users can inject custom characters and strings into the generated passwords to create more unique and memorable passwords.

The project is designed with clean, scalable architecture and leverages modern Python features such as asynchronous programming to ensure efficient and responsive performance. The API documentation is automatically generated using Swagger UI and can be easily accessed by navigating to the API endpoint.

### 📋 Pre-requisites

For the project, only PYPOETRY and PYENV and docker need to be installed on your machine, whether it is Linux or Windows. The packages and dependencies will be automatically added via POETRY.

### 🔧 Installation

A series of step-by-step examples that tell you what you need to do to get a development environment up and running.

To set up and download the project locally, follow these steps:

1º Make sure you have Git installed locally.

2º Open the terminal or command prompt and navigate to the directory where you want to clone the repository.

3º Get the URL of the repository you want to clone. You can usually find it on the repository's main page on GitHub or another code hosting platform.

4º Use the git clone command followed by the repository's URL to clone it to your local directory. For example, if the repository's URL is https://github.com/username/repository, the command will be:

```
git clone https://github.com/gabszs/FastApi--Conversor-de-Cambio.git
```

5º Wait for Git to finish cloning the repository. This will create a folder with the repository's name in your current directory.

6º Type the following command in your local console to initialize PYPOETRY:

```
poetry shell
```

And repeat the following code to install the dependencies:

```
poetry install
```

After that, if configured correctly, try starting uvicorn to access the endpoints (--reload if you want the hot reload function enabled):

```
uvicorn main:app --reload
```

These previous steps are the basic for the project, but you will need to build the docker image, and run the docker compose in a series of step-by-step examples bellow:

To build the docker image:

```
docker build -t passgenerator .
```

to build the docker-compose:

```
docker-compose build
```

and

```
docker-compose run app
```

also, you can run the project by this command:

```
docker-compose up app
```

---

to run commands inside the container you can use:

```
docker-compose run app sh -c "command"
```

## ⚙️ Running the tests

The API was developed using the TDD methodology, so the project already has automated tests for all elements of the project.

To run them:

```
docker-compose run app sh -c "pytest"
```

Endpoints

The API has the following endpoints:

1. `/password/pin/{password_lenght}`
   Endpoint to generate random pin codes.

Parameters
password_lenght (required, int): The length of the pin code to be generated.
quantity (optional, int): The number of pin codes to be generated. Defaults to 1.
Returns
An object containing a message and a list of dictionaries, each containing a number and its respective pin code.

2. `/password/pass/{password_lenght}`
   Endpoint to generate random passwords.

Parameters
password_lenght (required, int): The length of the password to be generated.
quantity (optional, int): The number of passwords to be generated. Defaults to 1.
ponctuation (optional, bool): A boolean value indicating whether the password should contain punctuation characters. Defaults to False.
Returns
An object containing a message and a list of dictionaries, each containing a number and its respective password.

3. `/password/complex_password/`{adicional_lenght}
   Endpoint to generate a list of complex passwords.

Parameters
adicional_lenght (required, int): The additional length to be added to each generated password.
quantity (optional, int): The number of passwords to be generated. Defaults to 1.
ponctuation (optional, bool): A boolean value indicating whether the password should contain punctuation characters. Defaults to False.
Request Body
suffle_string_inject (optional, bool): If set to true, the order of the string injections will be randomized in each generated password. Defaults to False.
char_inject (optional, list): A list of ASCII characters that will be injected into each generated password. Each item in the list must be a string of length 1.
string_inject (optional, list): A list of strings that will be injected into each generated password. Each item in the list must be a string of length 2 or greater.
Returns
An object containing a message and a list of dictionaries, each containing the generated password as a value and its position in the list as a key. Each generated password will contain at least one numeric and one alphabetic character. If punctuation is set to true, each generated password will also contain at least one punctuation character.

Json Models:

Input Json:

```
{
  "suffle_string_inject": false,
  "char_inject": [
    "string"
  ],
  "string_inject": [
    "string"
  ]
}
```

Output Json:

```
{
  "message": "string",
  "data": [
    {}
  ]
}
```

## 🛠️ Build with

Tools used to create the project:

- [FastApi](http://www.dropwizard.io/1.0.2/docs/) - The Rest framework used to build the API.
- [Poetry](https://python-poetry.org/docs/) - Dependency and virtual environment manager
- [Pyenv](https://github.com/pyenv/pyenv) - Used to implement the Python environment in the development environment

## 📌 Versioning

[Git](https://git-scm.com/doc)

## ✒️ Autores

Authors:

- **Gabriel Carvalho** - API implementation - [GabrielCarvalho](https://github.com/gabszs)

- **linkedin** - [Gabriel Carvalho](https://www.linkedin.com/in/gabzsz/)
