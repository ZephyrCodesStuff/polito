from math import floor
from typing import List

NUM_POSTI = 10
POSTI: List[bool] = [False for _ in range(NUM_POSTI)]

def sub_chunks():
    """
    Suddividi la lista di posti in tuple di sotto-liste
    con indici e posti, ogni qualvolta che un posto è occupato.
    """
    chunks: List[(int, list)] = []

    chunk_idx = 0
    chunk = []
    for p in POSTI:
        if not p:
            chunk.append(p)
        else:
            chunks.append((chunk_idx, chunk))
            chunk = []
            chunk_idx += 1
    
    chunks.append((chunk_idx, chunk))
    return chunks


def main():
    global POSTI

    while True:
        sub = sub_chunks()

        # Prendi la porzione più grande
        chunk_max = max(sub, key=lambda p: len(p[1]))

        # Occupa un posto a metà della porzione
        sub_posto_idx = floor(len(chunk_max[1]) / 2)
        chunk_max[1][sub_posto_idx] = True

        # Sostituisci il chunk modificato dentro `sub`
        for (i, chunk) in sub:
            if i == chunk_max[0]:
                sub[i] = (i, chunk_max[1])
        
        # Appiattisci i chunk e ricostituisci la lista
        sub.sort(key=lambda x: x[0])

        POSTI = []
        for (i, chunk) in sub:
            for c in chunk:
                POSTI.append(c)
            if i != (len(sub) - 1):
                POSTI.append(True)

        # Stampa i posti
        posti_str = ''.join([('X' if posto else '_') for posto in POSTI])
        print(posti_str)

        # Se tutti i posti sono stati occupati (tutti `True`), termina l'esecuzione.
        if all(POSTI):
            print("Tutti i posti sono stati occupati.")
            exit(0)

        input("Premi invio per occupare un posto.")

if __name__ == "__main__":
    main()