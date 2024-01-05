# Use Python as base image
FROM python:3.11.6

# Set working directory of the container
WORKDIR /app/

# Prevents Python from generating pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures that Python output is logged to the terminal.
ENV PYTHONUNBUFFERED 1

# to avoid problem with bjoern dependences need
RUN apt-get update && apt-get install -y libev-dev

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
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
