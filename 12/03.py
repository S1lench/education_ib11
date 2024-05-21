numbers = list(map(int, input().split()))
M, K = map(int, input().split())
subset_sum = sum(numbers[M:K+1])
print(subset_sum)
