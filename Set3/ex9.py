# 9. Operatii între seturi
def set_matrix_ops(*sets):
    results = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            results[f"{sets[i]} | {sets[j]}"] = len(sets[i] | sets[j])
            # Adăugați restul operatorilor...
    return results