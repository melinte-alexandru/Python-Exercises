# 6. Elemente care apar de exact x ori
def elements_appearing_x_times(x, *lists):
    from collections import Counter
    all_elements = [item for sublist in lists for item in sublist]
    counts = Counter(all_elements)
    return [item for item, count in counts.items() if count == x]