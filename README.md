# CheapyTrips - Agence de Voyage

Bienvenue dans **CheapyTrips**, une application web de type "agence de voyage" développée avec Django. Cette application permet aux utilisateurs de consulter des offres de voyage et de se connecter via une authentification intégrée ou Google.
Réalisé par un jeune passionné de développement, développeur non-professionel.

## Table des Matières
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Technologies Utilisées](#technologies-utilisées)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## Fonctionnalités

- **Consulter les offres de voyage** : Affiche une liste d'offres avec des informations détaillées telles que le titre, le prix, la destination et une description.
- **Authentification utilisateur** : Permet la connexion et l'inscription d'utilisateurs via une authentification Django classique.
- **Connexion avec Google** : Intégration de l'authentification sociale avec Google pour une connexion rapide.

## Installation

### Prérequis

- Python 3.8+
- Django 5.1.3+
- Un compte Google Cloud pour l'authentification via Google

### Étapes d'installation

1. **Cloner le projet** :
   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-projet.git
   cd nom-du-projet
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données** :
   ```bash
   python manage.py migrate
   ```

5. **Créer un superutilisateur** pour accéder à l'interface d'administration :
   ```bash
   python manage.py createsuperuser
   ```

## Configuration

### Variables d'environnement

Créez un fichier `.env` à la racine du projet pour stocker les clés sensibles :

```plaintext
SECRET_KEY=votre_cle_secrete_django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Configuration de l'authentification Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=votre_client_id_google
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=votre_client_secret_google
```

### Configuration Google OAuth2

1. Allez sur la [console Google Cloud](https://console.cloud.google.com/).
2. Créez un projet, puis activez l'API Google+.
3. Configurez l'écran de consentement OAuth.
4. Ajoutez un nouvel identifiant OAuth pour application web :
   - URL de redirection autorisée : `http://127.0.0.1:8000/accounts/google/login/callback/`

## Utilisation

1. **Démarrer le serveur de développement** :
   ```bash
   python manage.py runserver
   ```

2. **Accéder à l'application** :
   Ouvrez [http://127.0.0.1:8000](http://127.0.0.1:8000) dans votre navigateur.

3. **Naviguer dans l'application** :
   - Connectez-vous ou inscrivez-vous.
   - Consultez les offres de voyage.
   - Connectez-vous avec Google pour tester l'authentification sociale. 

## Technologies Utilisées

- **Django** - Framework web principal
- **django-allauth** - Gestion de l'authentification sociale (Google)
- **HTML/CSS** - Interface utilisateur

## Contribuer

Les contributions sont les bienvenues !

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalite`).
3. Effectuez les modifications nécessaires et commitez-les (`git commit -m 'Ajouter ma fonctionnalité'`).
4. Poussez votre branche (`git push origin feature/ma-fonctionnalite`).
5. Ouvrez une *pull request*.

## Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

---
En suivant ce guide, vous devriez être en mesure de configurer, de personnaliser et d'exécuter l'application CheapyTrips en local.
