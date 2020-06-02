""""
*/ 

##########################################################################################
USED MODULES : pyproj - pandas
Please refer to README in case of any interrogations.

This file contain all the geographical fonctions definitions used inside the main code.

PROJ license : MIT.
PANDA license : BSD 3-Clause License

##########################################################################################
##########################################################################################

MODULES UTILISÉS : pyproj - pandas
Merci de se diriger vers le README en cas d'intérrogations.

Ce fichier contient toutes les définhitions des fonctions géographiques utilisées dans le
code principal.

License PROJ : MIT.
License Panda : BSD 3-Clause License
##########################################################################################

NOM / Prénom : HAMDOUN Walid.
*/
"""

#python -m pip install pyproj --upgrade
#python -m pip install pandas --upgrade

from pyproj import *
import pandas

# ---------- NON-FILE COMPATIBLE / Coordonnées uniquement à partir de l'entrée directe utilisateur ----------

def convertCRScoords_Unic(inProj: str, outProj: str, x: float, y: float, alwaysxy: bool, direction_pos: str):
	"""
	Converti des coordonnées géographiques x et y entre deux systèmes
	de référentiels différents indiqués par l'utilisateur du GUI.
	Convert coordinates entered (input) by GUI user
	between two different CRS listed in the proj library.

	Retourne un Tuple sous conditions normales.
	Returns un Tuple under normal conditions.

	>>> convertCRScoords_Unic("EPSG:4326", "EPSG:26917", -80, 50, True, "FORWARD")
	(571666.4475041276, 5539109.815175673)
	"""

	transformer = Transformer.from_crs(inProj, outProj, always_xy=alwaysxy)
	x_out, y_out = transformer.transform(x, y, direction=direction_pos)

	return x_out, y_out

def convertCRScoords_Quato(inProj, outProj, x: float, y: float, z: float, time_zone: float, direction_pos: str):
	"""
	Converti des coordonnées géographiques entre deux systèmes
	de référentiels avec plus de précision que la première formule.
	Dénommée "conversion 14 param". Prends en compte la composante z
	ainsi que le fuseau horaire.
	Convert coordinates entered (input) by GUI user
	between two different CRS listed in the proj library.
	Takes into account more factors for a more precise
	conversion.

	Retourne une liste à 4 éléments.
	Returns a 4-elements list.

	>>> convertCRScoords_Quato(7789, 8401, 4213551.1590, 162494.2700, 4769661.5530, 2019, "FORWARD")
	(4213551.545562921, 162493.73915001773, 4769661.229592867, 2019.0)
	"""

	transformer = Transformer.from_crs(inProj, outProj)
	coords_out = transformer.transform(xx=x, yy=y, zz=z, tt=time_zone, direction=direction_pos)

	return coords_out

def convertGeoCRScoords(proj_ecef, ellps_ecef, datum_ecef, proj_lla, ellps_lla, datum_lla, x: float, y: float, z: float):
	"""
	Converti des coordonnées géographiques entre deux systèmes
	de référentiels en format lon/lat/h. (ECEF --> LLA).
	Convert coordinates between 2 systems CRS in lon/lat/h format.

	Retourne une liste à 3 élements.
	Returns a 3-elements list. 

	>>> convertGeoCRScoords("cart", "GRS80", "WGS84", "latlon", "GRS80", "WGS84", 4213551.1590, 162494.2700, 4769661.5530)
	(2.208499227055863, 48.712164749881154, 217.42466429807246)
	"""

	ecef = Proj(proj=proj_ecef, ellps=ellps_ecef, datum=datum_ecef)
	lla = Proj(proj=proj_lla, ellps=ellps_lla, datum=datum_lla)
	lon, lat, hau = transform(ecef, lla, x, y, z)

	return lon, lat, hau

# ---------- FUNCTION USAGE WITH FILE / Utilisation des fonctions à partir d'un fichier traité ----------
"""
Files dispositions / Dispositions des fichiers. (Examples).
Les fichiers doivent être de format CSV.
#POSSIBILITÉ D'UTILISER "," au lieu de ";" en CSV.

- CRScoords_Unic : TYPE 1

ID;inProj;outProj;x;y;alwaysxy;direction_pos
1;EPSG:4326;EPSG:26917;-80;70;True;FORWARD
2;EPSG:4326;EPSG:26917;-40;70;True;FORWARD
...

- CRScoords_Quato : TYPE 2

ID;inProj;outProj;x;y;z;time_zone;direction_pos
1;7789;8401;4213551.1590;162494.2700;4769661.5530;2019;FORWARD
2;7789;8401;4213551.1590;162494.2700;4769661.5530;2019;FORWARD
...

- GeoCRScoords : TYPE 3

ID;proj_ecef;ellps_ecef;datum_ecef;proj_lla;ellps_lla;datum_lla;x;y;z
1;cart;GRS80;WGS84;latlong;GRS80;WGS84;4213551.1590;162494.2700;4769661.5530
2;cart;GRS80;WGS84;latlong;GRS80;WGS84;4213551.1590;162494.2700;4769661.55307
...
"""
"""
utilisation_fichier = input("Voulez-vous convertir des coordonnées à partir du fichier ? Rep : oui ou non : ")

if utilisation_fichier == "non":
	pass
elif utilisation_fichier == "oui":
	fichier = str(input("Entrez le nom du fichier (ex : athlete_events.csv) : "))
	sep_valeurs = str(input("Entrez le séparateur des valeurs du fichier (, ou ;) : "))
	if sep_valeurs == ";":
		coords = pd.read_csv(fichier, sep = ";") #Charge le fichier.
	elif sep_valeurs == ",":
		coords = pd.read_csv(fichier, sep = ",") #Charge le fichier.

	conv_type = int(input("Entrez le type de conversion. Celles-ci sont affichées dans le GUI : "))

	for index, row in coords.iterrows():
		if conv_type == 1:
			coords_conv = convertCRScoords_Unic(row["inProj"], row["outProj"], row["x"], row["y"], row["alwaysxy"], row["direction_pos"])
			print(coords_conv)
		if conv_type == 2:
			coords_conv = convertCRScoords_Quato(row["inProj"], row["outProj"], row["x"], row["y"], row["z"], row["time_zone"], row["direction_pos"])
			print(coords_conv)
		if conv_type == 3:
			coords_conv = convertGeoCRScoords(row["proj_ecef"], row["ellps_ecef"], row["datum_ecef"], row["proj_lla"], row["ellps_lla"], row["datum_lla"], row["x"], row["y"], row["z"])
			print(coords_conv)
"""