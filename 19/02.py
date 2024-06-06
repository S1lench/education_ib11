def simple_map(transformation, values):
    result = []
    for element in values:
        result.append(transformation(element))
    return result


values = [1, 3, 1, 5, 7]
print(*simple_map(lambda x: x + 5, values))