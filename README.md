

<p align = center>
<img  src="img/logo.png" />
</p>

# OC Lettings

<p align = center>Mettre à l'échelle une application Django, en utilisant une architecture modulaire.

Basé sur un projet à forker : 
- https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR

Il s'appuie sur Python3.11 et :</p>

<p align = center>
    <a href="https://docs.djangoproject.com/fr/3.2/">    
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" 
        width="65"/>
    </a>
    <a href="https://www.docker.com/">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original-wordmark.svg" width="65"/>
    </a>
    <a href="https://circleci.com/">     
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/circleci/circleci-plain-wordmark.svg"  width="65"/>
    </a>
    <a href="https://sentry.io/welcome/">
        <img src="https://cdn.freebiesupply.com/logos/large/2x/sentry-3-logo-svg-vector.svg" width="60" />
    </a>
    <a href="https://www.sphinx-doc.org/en/master/#">
        <img src="https://blog.expertrec.com/wp-content/uploads/2019/07/sphinxdoc.png" width="60"/>
    </a>
    <a href="https://docs.readthedocs.io/en/stable/#">
        <img src="https://docs.readthedocs.io/en/stable/_static/logo.svg" width="150" />
    </a>
</p>

## But du project : 
*Aborder au travers des bonnes pratiques DevOps, la phase de mise en production d'un project:*
- Réduire une dette technique grace à :  
    - la refonte de l'architecture du projet.
    - la résolution de bug.
    - la mise en place d'une politique de tests.
    - le monitoring de certaines données avec Sentry.
- Containerisation du projet avec Docker.
- Automatisation des phases de tests, de contrôle qualité et de déployement, avec Circle Ci et Render.
- Automatisation et déploiement de documentation avec Sphinx et Read the Docs.


# Pré-requis : 

- Un compte DockerHub
- Un compte Sentry
- Un compte Circle Ci
- Un compte Render
- Un compte Read The Doc


# Installation du project:

## Cloner le projet:
```bash
    git clone https://github.com/LGD-P/P13_Open_C.git
```
## Installer le gestionnaire de dépendances poetry:<img src="https://python-poetry.org/images/logo-origami.svg" width=30>
    
    pip3 install poetry 

## Activer l'environnement virtuel depuis P13_Open_C/:

    poetry shell 

## Installer les dépendances:

    poetry install 
    poetry update

## Créer et pousser l'image sur son Docker Hub    :

```bash
docker login -u votre-identifiant
docker build -t oc-lettings-docker-build .
docker tag oc-lettings-docker-build:latest votre-identifiant/oc-lettings-build:last-build
docker push votre-identifiant/oc-lettings-build:latest
```

Le site est désormais accéssible sur  : ==> https://oc-lettings-url.onrender.com

Et la documentation sur  : ==> https://p13-open-c.readthedocs.io/fr/latest/