
.. _install:

=======================
Installation du projet:
=======================

Cloner le projet:
--------------------

.. code-block:: bash

    git clone https://github.com/LGD-P/P13_Open_C.git

Installer le gestionnaire de dépendances poetry:
------------------------------------------------    

.. code-block:: bash

    pip3 install poetry 

Activer l'environnement virtuel depuis P13_Open_C/:
---------------------------------------------------

.. code-block:: bash

    poetry shell 


Installer les dépendances:
--------------------------
.. code-block:: bash

    poetry install 
    poetry update


Créer et pousser l'image sur son Docker Hub:
---------------------------------------------

.. code-block:: bash

    docker login -u votre-identifiant
    docker build -t oc-lettings-docker-build .
    docker tag oc-lettings-docker-build:latest votre-identifiant/oc-lettings-build:last-build
    docker push votre-identifiant/oc-lettings-build:latest

Les variables d'environnement :
-------------------------------

*Ce projet utilise dotenv et il vous faut adapter un certain nombre de variables d'environnement sur les différentes plateformes utilisées.*


- Directement pour le projet Django dans .env

.. code-block:: bash

    SENTRY_DNS ="à récupérer sur Sentry"
    SECRET_KEY="à générer pour le fonctionnement de Django"


