# Overlay Marker
Un outil de marquage visuel pour écran qui permet d'annoter n'importe quelle application en surimpression.

## Description
Ce programme crée une couche transparente en plein écran sur laquelle vous pouvez placer des marqueurs numérotés. Il est utile pour :
- Marquer des points d'intérêt sur des captures d'écran
- Annoter des présentations en direct
Identifier des zones spécifiques dans des applications
- Créer des repères temporaires sur l'écran


## Prérequis
- Python 3.12
- Système Linux (testé sur Ubuntu/Debian)
- Droits sudo (nécessaire pour capturer les événements clavier système)

## Installation
Créez un environnement virtuel et installez les dépendances :

```py
python3 -m venv venv
source venv/bin/activate
pip install PyQt5 pynput keyboard evdev
```

## Utilisation
Lancez le programme avec les droits sudo :

```py
sudo ./venv/bin/python3 main.py
```

## Raccourcis clavier
- **Clic droit** : Ajouter un marqueur numéroté à la position du curseur
- **F9** : Basculer entre premier plan (marquage actif) et arrière-plan (interaction avec les applications)
- **Espace** : Effacer tous les marqueurs (uniquement en mode premier plan)
- **Échap** : Quitter l'application

## Modes de fonctionnement

### Mode premier plan (par défaut)

- La couche est visible avec une teinte bleue légère
- Vous pouvez placer des marqueurs
- Les clics sont interceptés par l'overlay

### Mode arrière-plan

- La couche passe derrière avec une teinte rouge légère
- Les marqueurs restent visibles
- Vous pouvez interagir normalement avec vos applications

## Dépendances

Les packages Python suivants sont requis (voir requirements.txt si vous en créez un) :

- **PyQt5** : Interface graphique et rendu
- **pynput** : Capture des événements souris
- **keyboard** : Capture des événements clavier système
- **evdev** : Support des périphériques d'entrée sous Linux

## Notes techniques

- Le programme utilise Qt pour créer une fenêtre transparente en plein écran
- Les événements souris et clavier sont capturés au niveau système
- Les marqueurs sont dessinés avec des cercles jaunes numérotés séquentiellement
- L'application doit être lancée avec sudo pour capturer les événements clavier système
