from typing import List, Dict

DATA_FILE = "Elenco-comuni-italiani.csv"
DATA = []

LABELS: Dict[str, int] = {}
REGIONS: Dict[str, List[str]] = {}

STOP_SEQUENCE = "***"

def main():
    global DATA

    try:
        with open(DATA_FILE) as f:
            data = f.readlines()[1:]
            for line in data:
                DATA.append([x.strip('"').strip() for x in line.split(';')])
    
    except IOError:
        print(f"[!] Non è stato possibile leggere il file `{DATA_FILE}`!")
        exit(1)

    finally:
        f.close()

    # Prendi i dati
    for data in DATA:
        region_name = data[10]
        
        if region_name not in REGIONS:
            REGIONS[region_name] = []
        
        city_name = data[6]
        REGIONS[region_name].append(city_name)
    
    # Liberiamo la memoria
    DATA.clear()
    
    # Ordina le regioni
    for cities in REGIONS.values():
        cities.sort() # Ordina per alfabetico
        cities.sort(key=lambda x: len(x)) # Ordina per lunghezza
    
    while True:
        query = input("\nInserisci il nome di una regione: ").strip().lower()

        if query == STOP_SEQUENCE:
            print("\n[!] Arrivederci!")
            exit(0)
        
        results = [(k, v) for (k, v) in REGIONS.items() if query in k.strip().lower()]
        
        if len(results) > 1:
            print(f"[!] Sono stati trovati più risultati (`{'`, `'.join([k for (k, _) in results])}`). Per favore, immetti un valore più specifico!")
            continue

        if len(results) == 0:
            print(f"[!] Non sono stati trovati risultati. Per favore, riprova!")
            continue

        found_region = results[0]
        
        region_name = found_region[0]
        region_cities = found_region[1]

        print(f"Numero comuni in \"{region_name}\": {len(region_cities)}")

        print(f"Comune con il nome più corto: {region_cities[0]}")
        print(f"Comune con il nome più lungo: {region_cities[-1]}")

if __name__ == "__main__":
    main()