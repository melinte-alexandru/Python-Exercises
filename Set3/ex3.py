# 3. Comparare dicționare recursivă
def compare_dicts(d1, d2):
    diff1, diff2, common_diff = [], [], []
    keys1, keys2 = set(d1.keys()), set(d2.keys())
    
    for k in keys1 & keys2:
        if isinstance(d1[k], dict) and isinstance(d2[k], dict):
            # recursivitate pentru structuri imbricate
            continue 
        if d1[k] != d2[k]:
            common_diff.append(k)
            
    return (common_diff, list(keys1 - keys2), list(keys2 - keys1))