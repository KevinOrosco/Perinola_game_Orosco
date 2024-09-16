import pytest
from Perinola import Perinola

def test_prueba():
    assert(True)

def test_constructor_con_caras():
    a = Perinola()
    assert(a.cara_visible == "Pon 1")

def test_constructor_sin_caras():
    a = Perinola()
    assert(len(a.caras) == 6)

def test_repr():
    a = Perinola()
    msj = a.__repr__()
    assert ("Salio: " in msj)

def test_tirar_aleatorio1():
    a = Perinola()
    a.tirar()
    original = a.cara_visible
    salioOtro = False
    for _ in range(1000):
        a.tirar()
        if (a.cara_visible != original):
            salioOtro = True

    assert(salioOtro)

def test_tirar_aleatorio_todos_los_valores():
    d = Perinola()
    caras = []
    for _ in range(1000):
        d.tirar()
        if (d.cara_visible not in caras):
            caras.append(d.cara_visible)

    assert(len(caras) == 6)