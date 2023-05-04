# test n°2 Datalumni Python
import csv
import json

filename = 'students.csv'


# récupère les enregistrements
def getLines():
	with open(filename, 'r') as file:
		lines = csv.reader(file)
		return list(lines)


# sort les diférents diplomes
def getDegrees(rows):
	return list(set(row[4] for row in rows))


# récupère le nombre d'utilisateurs par diplome
def degreesAmount(rows, degrees):
	users_per_degrees = {}
	for degree in degrees:
		users_per_degrees[degree] = 0
		for row in rows:
			if row[4] == degree:
				users_per_degrees[degree] += 1
	return users_per_degrees


# export dans un fichier json le compte d'utilisateur par diplomes
def exportDegrees(users_per_degrees):
	with open('degree_count.json', 'w') as outfile:
		json.dump(users_per_degrees, outfile)
	print(f'\nFichier `degree_count.json` enregistré !')


def main():
	rows = getLines()
	degrees = getDegrees(rows)
	users_per_degree = degreesAmount(rows, degrees)

	print(f'\nLe fichier brut contient {len(rows)} lignes')
	print(f'\nLe fichier contient {len(degrees)} diplômes uniques')

	exportDegrees(users_per_degree)


main()
