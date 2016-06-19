square_of_sum = lambda n: sum(xrange(n + 1)) ** 2
sum_of_squares = lambda n: sum(x * x for x in xrange(n + 1))
difference = lambda n: square_of_sum(n) - sum_of_squares(n)
