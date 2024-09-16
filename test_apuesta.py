import pytest
from Apuesta import Apuesta

def test_prueba():
    assert(True)

def test_constructor():
    a = Apuesta()
    assert(a.fichas == 0)

def test_repr():
    a = Apuesta()
    msj = a.__repr__()
    assert ("Apuesta: " in msj)

def test_ponerFicha():
    a = Apuesta()
    a.ponerFicha(8)
    assert(a.fichas == 8)

    a = Apuesta()
    a.ponerFicha(2)
    assert(a.fichas == 2)

    a = Apuesta()
    a.ponerFicha(2)
    a.ponerFicha(2)
    assert(a.fichas == 4)

def test_tomarFicha_sin_argumentps():
    a = Apuesta()
    a.fichas = 5
    a.tomarFicha()
    assert(a.fichas == 4)

def test_ponerFicha_sin_argumentos():
    a = Apuesta()
    a.fichas = 5
    a.ponerFicha()
    assert(a.fichas == 6)


    