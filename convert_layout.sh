#!/bin/bash

# Funcao que converte o arquivo uic para .py para que os type hints funcionem
venv/bin/pyside6-uic ./calc/assets/layout/layout.ui -o ./calc/view/layout.py