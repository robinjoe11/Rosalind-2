from itertools import product


def main(alpha, num):
	orderedalpha = alpha.replace(" ", "")
	permlist = ([x for x in product(orderedalpha, repeat=num)])
	for i in permlist:
		print (''.join(map(str, i)))


main("A B C D E F G H I J", 2)

