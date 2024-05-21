numbers = list(map(int, input().split()))
M, K = map(int, input().split())
subset_sum_of_squares = sum(number**2 for number in numbers[M:K+1])
print(subset_sum_of_squares)
