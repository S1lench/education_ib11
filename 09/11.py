num_whitelist = int(input())
whitelist = set(input() for _ in range(num_whitelist))

num_queries = int(input())
queries = [input() for _ in range(num_queries)]

valid_queries = [query for query in queries if query in whitelist]

for valid_query in valid_queries:
    print(valid_query)
