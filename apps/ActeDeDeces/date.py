
# cardinal = ["", "un", "deux", "trois", "quatre", "cinq", "six", "sept",
# 	"huit", "neuf", "dix", "onze", "douze", "treize", "quatorze",
# 	"quinze", "seize", "dix sept", "dix huit", "dix neuf"]

# dizaines = ["", "", "vingt", "trente", "quarante", "cinquante", "soixante",
# 	"septante", "quatre-vingt", "nonante"]


# def lireMilles(x):
# 	mil  = (x//1000)%10
# 	if mil == 0 : return ""
# 	if mil == 1 : return "mil "
# 	return cardinal[mil]+" mille "

# def lireCentaines(x):
# 	cent  = (x//100)%10
# 	if cent == 0 : return ""
# 	if cent == 1 : return "cent "
# 	return cardinal[cent]+" cent "

# def lireDizaines(x):
# 	valeur = x%100
# 	if valeur < 20 : return cardinal[valeur]

# 	unite = valeur%10
# 	dizaine = valeur//10

# 	if unite == 0 : return dizaines[dizaine]
# 	if unite == 1 : return dizaines[dizaine]+"-et-un"

# 	return dizaines[dizaine]+" "+cardinal[unite]

# def lireTout(x):
# 	return lireMilles(x)+lireCentaines(x)+lireDizaines(x)


# def lireAge(x):
# 	return f'{lireTout(x.year)}'

# if __name__ == '__main__':
# 	from datetime import date
# 	today = date.today()
# 	print(lireAge(today))



# ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "] 
 
# twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "] 
 
# thousands = ["","thousand ","million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ", "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", "octodecillion ", "novemdecillion ", "vigintillion "] 
 
 
# def num999(n): 
#     c = n % 10 # singles digit 
#     b = ((n % 100) - c) / 10 # tens digit 
#     a = ((n % 1000) - (b * 10) - c) / 100 # hundreds digit 
#     t = "" 
#     h = "" 
#     if a != 0 and b == 0 and c == 0: 
#         t = ones[a] + "hundred " 
#     elif a != 0: 
#         t = ones[a] + "hundred and " 
#     if b <= 1: 
#         h = ones[n%100] 
#     elif b > 1: 
#         h = twenties[b] + ones[c] 
#     st = t + h 
#     return st 
 
# def num2word(num): 
# 	if num == 0: return 'zero' 
#     i = 3 
#     n = str(num) 
#     word = "" 
#     k = 0 
#     while(i == 3): 
#         nw = n[-i:] 
#         n = n[:-i] 
#         if int(nw) == 0: 
#             word = num999(int(nw)) + thousands[int(nw)] + word 
#         else: 
#             word = num999(int(nw)) + thousands[k] + word 
#         if n == '': 
#             i = i+1 
#         k += 1 
#     return word[:-1] 
# And the output is:

# num2word(20156) 
# Out[1]: 'twenty thousand one hundred and fifty six' 
 
# num2word(1515126844962) 
# Out[2]: 'one trillion five hundred and fifteen billion one hundred and twenty six million eight hundred and forty four thousand nine hundred and sixty two' 
 
# num2word(0) 
# Out[3]: 'zero' 