.. _strating_guide:

======================================
Démarrage rapide fonctionnement local:
======================================

Lancement classique de Django:
------------------------------

*Une fois la phase d'installation réalisée, le projet est exécutable en local*

.. code-block:: bash

    poetry run python3 manage.py runserver

Cette commande exécutera un serveur gunicorn accessible depuis les localhosts du settings.py: 
    - http://0.0.0.0.:8000
    - http://localhost:8000
    - http://127.0.0.1:8000


Lancer l'application depuis le container Docker en local:
---------------------------------------------------------

*Dans un premier temps il faut contruire l'image grace au Dockerfile et son .dockerignore*


- On créer l'image

.. code-block:: bash

    docker build -t nom-de-l`image-souhaité
  
- On lance l'image en définissant un Django Secret avec -e et en mappant les ports du container et les ports de notre machine en local avec -p

.. code-block:: bash
    
    docker run -e SECRET_KEY=VotreSecret -p 8000:8000 votre-image

- L'application sera accessible depuis : 

    - http://0.0.0.0:8000