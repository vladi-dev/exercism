sum_of_multiples = lambda lim, nums: sum(set(i for n in nums for i in range(1, lim) if n > 0 and i % n == 0))
