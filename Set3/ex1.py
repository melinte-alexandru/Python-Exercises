# 1. Operații seturi
def set_operations(a, b):
    s1, s2 = set(a), set(b)
    return (s1 & s2, s1 | s2, s1 - s2, s2 - s1)