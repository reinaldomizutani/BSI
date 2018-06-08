def getMean(x):
	soma = 0
	i = 0
	for item in x:
		soma = soma + item
		i += 1
	return soma/i

if __name__ == '__main__':
	with open('set.txt', 'r') as file:

		col1 = []
		col2 = []
		col3 = []
		col4 = []
		col5 = []
		col6 = []

		conj = file.readlines()

		for item in conj:
			x,y = item.split()
			x = float(x)
			y = float(y)

			col1.append(x)
			col2.append(y)

		meanx = getMean(col1)
		meany = getMean(col2)

		for item in col1:
			col3.append(item-meanx)

		for item in col2:
			col4.append(item-meany)

		for item in col1:
			col5.append((item-meanx)*(item-meanx))

		i=0
		for item in col1:
			col6.append(col3[i]*col4[i])
			i = i +1

		somacol5=0
		somacol6=0

		for item in col5:
			somacol5 = somacol5 + item

		for item in col6:
			somacol6 = somacol6 + item


		a = somacol6/somacol5

		b = (meany * somacol5) / (somacol6 * meanx)

		a = str(a)
		b = str(b)

		print('a equação da linha é:')
		print( 'y = ' + a + 'x' + ' + ' + b)

