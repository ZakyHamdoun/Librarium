# Librarium

Librarium est un logiciel conçu par ____ pour convertir des données géographiques entre plusieurs systèmes de coordonnées. (GRS).

## Installation

Télécharger le fichier. Il faut au préalable avoir les modules :
pandas, pyqt5, pyproj.


```bash
pip install pandas --upgrade
pip install pyqt5 --upgrade
pip install pyproj --upgrade
```

## Usage

* Exécuter et lancer le fichier "main.py". Toutes les valeurs en sortie sont affichées à l'intérieur de la console Python.
* Pour la conversion 14 param, il faut obligatoirement mettre les GRS en format int / float. En gros, il faut écrire un nombre. Si vous souhaitez écrire une chaîne de caractères. Alors il faut changer enlever le "float" à la ligne correspondante.
* Si vous souhaitez convertir des fichiers entiers. Il faut qu'ils soient en format .csv. Comma Separated Values.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

PySide2 under a LGPL license

BSD 3-Clause License
