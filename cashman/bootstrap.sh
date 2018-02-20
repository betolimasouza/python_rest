#!/bin/bash

#env variable que o flask usa para iniciar
export FLASK_APP="C:\Users\beto\Documents\Beto\Programming\python_api\cashman\cashman\index.py"

#Ativar o pipenv (Dependecy Manager)
source $(pipenv --venv)"\Scripts\activate"

#Roda o Flask
flask run -h 0.0.0.0
