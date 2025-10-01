# **llm-multimodel-response-aggregator**

<p align="center"> 🚀 This script is designed to call a given prompt in N different models and providers, and use a specific template to aggregate all returns and generate a new answer.</p>

<h3>🏁 Table of Contents</h3>

<br>

===================

<!--ts-->

💻 [Dependencies and Environment](#dependenciesandenvironment)

☕ [Using](#using)

👷 [Author](#author)

<!--te-->

===================

<div id="dependenciesandenvironment"></div>

## 💻 **Dependencies and Environment**

**Gemini**: This project uses the paid Google Gemini API, it's necessary to [configure a valid Gemini API Key](https://aistudio.google.com/apikey). Ensure you have a `.env` file with the environment variable **API_KEY_GEMINI** and linked billing account.

**OpenAI**: This project uses the paid OpenAI API, it's necessary to [configure a valid OpenAI API Key](https://platform.openai.com/settings/organization/api-keys). Ensure you have a `.env` file with the environment variable **API_KEY_OPENAI** and linked billing account.

To setup environment use (you will need [venv](https://docs.python.org/pt-br/3.13/library/venv.html)):

```
$ make setup
```

And enable the virtual ambient using:

```
$ source .venv/bin/activate
```

You can clean the environment using

```
$ make clean
```

<div id="using"></div>

## ☕ **Using**

First, check the [dependencies](#dependenciesandenvironment) process

You can run using the script

```
$ python main.py
```

Check the required and optional parameters in the [`src/args.py`](src/args.py) file.

<div id="author"></div>

#### **👷 Author**

Made by Glener Pizzolato! 🙋

[![Linkedin Badge](https://img.shields.io/badge/-Glener-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/glener-pizzolato/)](https://www.linkedin.com/in/glener-pizzolato-6319821b0/)
[![Gmail Badge](https://img.shields.io/badge/-glenerpizzolato@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:glenerpizzolato@gmail.com)](mailto:glenerpizzolato@gmail.com)
