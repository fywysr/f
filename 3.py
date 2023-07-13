# This is a sample Python script.
def compare_entities(entity1, entity2, entity3):
    different_parameters = {}

    for param in ['A', 'B', 'C', 'D']:
        if entity1.get(param) != entity2.get(param) or entity1.get(param) != entity3.get(param):
            different_parameters[param] = [entity1.get(param), entity2.get(param), entity3.get(param)]

    return different_parameters

# 示例数据
entity1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
entity2 = {'A': 1, 'B': 2, 'C': 5, 'D': 4}
entity3 = {'A': 1, 'B': 6, 'C': 5, 'D': 7}

result = compare_entities(entity1, entity2, entity3)
print(result)

