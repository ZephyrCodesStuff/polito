# Laboratorio 2

## Domande
1. I dati hanno diversi tipi. Le variabili le contengono. Ogni variabile ha un tipo di dati assegnato (alcuni esempi sono `str`, `int`, ecc.).\
\
In alcuni linguaggi (come, ad esempio, Python) il tipo di una variabile può cambiare durante il corso del programma. In altri linguaggi (come il C++), il tipo della variabile deve rimanere uguale per tutta la vita di quella variabile.

2. (vedi sotto)
```py
var_float: float = 0.5
var_int: int = 1

# La variabile `var_int` viene automaticamente trasformata in un `float` (dunque `1.0`) in modo da poterla sommare all'altra.
var_sum: float = var_float + var_int
assert var_sum == 1.5
```

3. Nei seguenti casi...
    1. Vengono sommati i valori dei due numeri interi
    2. L'`int` viene trasformato in un `float` per poterli sommare. Il risultato sarà un `float`.
    3. Le stringhe vengono concatenate nell'ordine in cui vengono sommate. Ad esempio, `"abc" + "def"` darà `"abcdef"`.
    4. Viene creata un'eccezione `TypeError`, in quanto non è possibile sommare direttamente un numero ad una stringa.\
    \
    È però possibile concatenare un numero ad una stringa se viene chiamato il metodo `.__str__()` o il costruttore di `str` con il valore desiderato. In questo modo verranno concatenate.

## Programmi
1. Parte 1: `./aritmetica/*`
    1. Due numeri: `due_numeri.py`
    2. Resistenze: `resistenze.py`
    3. Cifre: `cifre.py`
    4. Auto ibrida: `auto_ibrida.py`
    5. Forza elettrica: `forza_elettrica.py`

2. Parte 2: `./stringhe/*`
    1. Caratteri: `caratteri.py`
    2. Numero telefonico: `num_telefonico.py`
    3. Allineamento: (vedi `due_numeri.py`)