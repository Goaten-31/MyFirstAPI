# My First API

Prototypal API for a personal portfolio website.

## Overview

This project is a prototype API for my personal portfolio website (see "firstWebPage").

## Tech stack

- Python 3.13
- FastAPI
- SQLAlchemy
- JWT with PyJWT

## Goals

This project's goal is to help me learn backend and full-stack development. I chose FastAPI because:

- It works well for deploying ML models via HTTP APIs.
- It's modular, letting me pick libraries for authentication, authorization, and database access.
- It's lightweight and a good fit for small-scale web apps compared to frameworks such as Django.

I'm new to software engineering and focusing on learning broadly applicable backend skills.

## Getting started

Prerequisites: Python 3.13 and Git.

1. Create and activate a virtual environment

- Windows (PowerShell):
    - `python -m venv venv`
    - `.\\venv\\Scripts\\Activate.ps1`

- macOS / Linux:
	- `python3 -m venv venv`
	- `source venv/bin/activate`

2. Install dependencies

- `pip install -r requirements.txt`

3. Run the development server

- `uvicorn main:app --reload`