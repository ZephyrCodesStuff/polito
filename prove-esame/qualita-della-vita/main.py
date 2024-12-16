from typing import List, Dict, Union

DATA_SOURCE: str = "20201214_QDV2020_001.csv"

# Caching per i contenuti dei file
header: List[Union[str, int, float]] = []
data: List[Union[str, int, float]] = []

labels: List[str] = []
locations: Dict[str, Dict[str, str]] = {}

def main():
    # Prova a raccogliere i dati
    global header
    global data

    try:
        with open(DATA_SOURCE, "r") as file:
            header = file.readline().split(",")
            data = [line.split(",") for line in file.readlines()]
    except IOError:
        print(f"\n[!] Il file \"{DATA_SOURCE}\" non è stato trovato, o non è leggibile!")
        exit(1)
    
    # Troviamo tutti gli indicatori
    global labels
    
    labels = list(set([str(i[5]).strip('"').replace('""', '') for i in data]))
    labels.sort()
    
    # Organizziamo i dati
    global locations

    for i in data:
        name = i[0].strip('"')
        label = str(i[5]).strip('"').replace('""', '')
        value = float(i[4])
        
        if name not in locations:
            locations[name] = {}

        locations[name][label] = value
    
    # Iniziamo il loop principale per poter eseguire query
    while True:
        print("\n\nIndicatori della qualità della vita:")

        label_idx = 1
        for i in labels:
            print(f"{label_idx}. {i}")
            label_idx += 1
        
        chosen_idx = input("\n> Scegli l'indicatore desiderato: ")
        chosen_label = ""

        try:
            chosen_idx = int(chosen_idx) - 1
            chosen_label = labels[chosen_idx]
                
        except ValueError:
            print(f"[!] Non è stato immesso un numero valido.")
            input("\n(Immetti qualsiasi cosa per continuare...)")
            continue

        except IndexError:
            print(f"[!] Il valore immesso è fuori dai confini: [0,{len(labels)}]")
            input("\n(Immetti qualsiasi cosa per continuare...)")
            continue
        
        # Troviamo i dati per ogni località
        query = [(k, v[chosen_label]) for (k, v) in locations.items()]

        # Ordiniamo in ordine discendente
        query.sort(key=lambda x: x[1], reverse=True)

        # Stampiamo i risultati
        print(f"\nClassifica secondo l'indicatore \"{chosen_label}\": \n")

        for (location, value) in query:
            print(f"{location}: {value}")
        
        input("\n(Immetti qualsiasi cosa per continuare...)")

if __name__ == "__main__":
    main()