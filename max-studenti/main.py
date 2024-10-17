import argparse

import csv
from matplotlib import pyplot

parser = argparse.ArgumentParser(description='Analisi di un elenco di studenti')
parser.add_argument('filename', type=str, help="Nome del file CSV da analizzare"),

args = parser.parse_args()

FILENAME = args.filename

# Leggi l'elenco degli studenti e salvalo in un'array
def leggi(nome_file):
    # Apri il file in lettura e carica ogni riga dalla seconda in poi
    with open(nome_file, newline='') as file:
        reader = list(csv.reader(file))

        return [x for x in reader[1:] if len(x) > 0]


# estrai i nomi di battesimo da un elenco di studenti
def estrai_nomi(elenco):
    return [riga[2] for riga in elenco]

# Calcola le frequenze dei vari nomi presenti in un array
def frequenze(tokens):
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] = freq[token] + 1
        else:
            freq[token] = 1
    return freq


# calcola il massimo valore presente nelle frequenze
def max_frequenza(freq):
    return max(freq.values())


def nomi_piu_frequenti(freq, max):
    return [nome for (nome, frequenza) in freq.items() if frequenza == max]


def main():
    stud = leggi(FILENAME)
    nomi = estrai_nomi(stud)
    print(f"Nella classe ci sono {len(stud)} studenti")

    freq = frequenze(nomi)
    max_freq = max_frequenza(freq)
    print(f"Il nome più frequente compare {max_freq} volte")

    nomi_max = nomi_piu_frequenti(freq, max_freq)
    print(f"Si tratta di: {nomi_max}")

    # estrai solo i nomi che compaiono almeno 2 volte
    freq2 = {k: v for (k, v) in freq.items() if v >= 2}
    print(
        f"I nomi che compaiono più di una volta sono {', '.join(sorted(list(freq2.keys())))}."
    )

    pyplot.barh(list(freq2.keys()), freq2.values())
    pyplot.show()

main()
