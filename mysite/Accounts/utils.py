from enum import Enum

class Rol(Enum):
    Administrador = 1
    Productor = 2
    Comercializador_Nacional = 3
    Comercializador_Provincial = 4
    Promotor = 5
    Controlador = 6

def get_min(groups):
    if len(groups) == 0:
        return -1
    mini = Rol[groups[0].name].value
    for i in groups:
        if Rol[i.name].value < mini:
            mini = Rol[i.name].value
    return mini

def can_operate(operator_groups, target_groups):
    min_operator = get_min(operator_groups)
    min_target = get_min(target_groups)

    if min_target == -1:
        return True
    if min_operator == -1:
        return False
    if min_operator < min_target:
        return True
    
    return False