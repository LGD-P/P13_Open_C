# Use Python as base image
FROM python:3.11.6

# Set working directory of the container
WORKDIR /app/

# Prevents Python from generating pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures that Python output is logged to the terminal.
ENV PYTHONUNBUFFERED 1


RUN pip install poetry 

ENV PATH="$PATH:$HOME/.poetry/bin"

# Copy pyproject.toml in working directory
COPY pyproject.toml poetry.lock /app/ 


# Install dependecies with Poetry --only main | poetry shell
RUN poetry install --no-ansi --only main

# Copy the entire project in working directory
COPY . /app/

EXPOSE 8000

# Run Django app 
CMD ["poetry", "run", "python3", "manage.py", "migrate", "&&", "python3", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]