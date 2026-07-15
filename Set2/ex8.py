# 8. Implementare zip
def custom_zip(*lists):
    max_len = max([len(l) for l in lists])
    result = []
    for i in range(max_len):
        row = tuple(lists[j][i] if i < len(lists[j]) else None for j in range(len(lists)))
        result.append(row)
    return result