# 4. Operații liste fără set
def list_operations(a, b):
    intersect = [x for x in a if x in b]
    reunion = a + [x for x in b if x not in a]
    diff_ab = [x for x in a if x not in b]
    diff_ba = [x for x in b if x not in a]
    return intersect, reunion, diff_ab, diff_ba