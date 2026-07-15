# 7 Funcții globale (Extensibilitate)
def apply_function(op_name, *args, **kwargs):
    # Dictionar global de functii
    return globals()[op_name](*args, **kwar