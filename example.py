from binomial import distribution


print('\n------------Binomial Probability Distribution----------------\n')

n = int(input('Enter total amount of tests >>> '))
p = float(input('Enter the determined probability >>> '))

bdist = distribution(n, p)
bdist.Binomial()

