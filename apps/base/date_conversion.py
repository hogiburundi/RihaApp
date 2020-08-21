ordinal = ["", "premier", "deuxième", "troisième", "quatrième", "cinquième",
	"sixième", "septième", "huitième", "neuvième", "dixième", "onzième",
	"douzième", "treizième", "quatorzième", "quinzième", "seizième", 
	"dix septième", "dix huitième", "dix neuvième", "vingtième", 
	"vingt-et-unième", "vingt deuxième", "vingt troisième", "vingt quatrième",
	"vingt cinquième", "vingt sixième", "vingt septième", "vingt huitième",
	"vingt neuvième", "trentième", "trente-et-unième"]

cardinal = ["", "un", "deux", "trois", "quatre", "cinq", "six", "sept",
	"huit", "neuf", "dix", "onze", "douze", "treize", "quatorze",
	"quinze", "seize", "dix sept", "dix huit", "dix neuf"]

dizaines = ["", "", "vingt", "trente", "quarante", "cinquante", "soixante",
	"septante", "quatre-vingt", "nonante"]

mois = ["","janvier", "février", "mars", "avril", "mai", "juin", "juillet",
	"août", "septembre", "octobre", "novembre", "décembre"]

def lireMilles(x):
	mil  = (x//1000)%10
	if mil == 0 : return ""
	if mil == 1 : return "mil "
	return cardinal[mil]+" mille "

def lireCentaines(x):
	cent  = (x//100)%10
	if cent == 0 : return ""
	if cent == 1 : return "cent "
	return cardinal[cent]+" cent "

def lireDizaines(x):
	valeur = x%100
	if valeur < 20 : return cardinal[valeur]

	unite = valeur%10
	dizaine = valeur//10

	if unite == 0 : return dizaines[dizaine]
	if unite == 1 : return dizaines[dizaine]+"-et-un"

	return dizaines[dizaine]+" "+cardinal[unite]

def lireTout(x):
	return lireMilles(x)+lireCentaines(x)+lireDizaines(x)

def lireDate(x):
	return f"l'an {lireTout(x.year)}, le {ordinal[x.day]} jour du mois de {mois[x.month]}"

def lireAge(x):
	return f'{cardinal[x.year]}'
if __name__ == '__main__':
	from datetime import date
	today = date.today()
	print(lireDate(today))
