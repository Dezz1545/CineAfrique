CineAfrique
Introduction
CineAfrique est une plateforme cinématographique dédiée à la communauté africaine. Ce projet inclut un Dashboard pour l'administration et une plateforme pour les producteurs de films. Le Dashboard permet de gérer les films déposés par les producteurs, les paiements et les supports. La plateforme Producteur permet aux utilisateurs de déposer des vidéos, de suivre les visualisations et de gérer les paiements.

Prérequis
Assurez-vous d'avoir les éléments suivants installés sur votre machine :

Python 3.11.4
Git
Installation du projet
Cloner le projet
Ouvrez un terminal ou une console.
Clonez le dépôt GitHub en utilisant la commande suivante :

git clone https://github.com/Dezz1545/CineAfrique.git
cd CineAfrique

Configurer l'environnement virtuel
Créez un environnement virtuel Python :
python -m venv venv

Activez l'environnement virtuel :
Sur Windows :
venv\Scripts\activate

Sur macOS/Linux :
source venv/bin/activate

Installer les dépendances
Installez les dépendances nécessaires à partir du fichier requirements.txt :
pip install -r requirements.txt

Appliquer les migrations
Appliquez les migrations pour créer les tables nécessaires dans la base de données :
python manage.py migrate

Créer un superutilisateur
Créez un superutilisateur pour accéder au panneau d'administration Django :
python manage.py createsuperuser

Lancer le serveur de développement
Démarrez le serveur de développement Django :
python manage.py runserver


Installez les dépendances nécessaires à partir du fichier requirements.txt :
