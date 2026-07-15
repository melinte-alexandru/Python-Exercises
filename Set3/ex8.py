# 8. Unice vs Duplicate
def count_unique_duplicate(s):
    unique = {x for x in s if list(s).count(x) == 1}
    duplicate = {x for x in s if list(s).count(x) > 1}
    return (len(unique), len(duplicate))