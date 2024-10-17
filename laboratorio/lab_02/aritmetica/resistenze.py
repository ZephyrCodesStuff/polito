def reciprocal(n: float):
    return 1 / float(n)

def main():
    res_single = input("Inserisci il valore della resistenza in serie (in Ohm): ")

    res_par_1 = input("Inserisci il valore della prima resistenza in parallelo (in Ohm): ")
    res_par_2 = input("Inserisci il valore della seconda resistenza in parallelo (in Ohm): ")

    total_res = reciprocal(reciprocal(res_par_1) + reciprocal(res_par_2))
    print(f"Il valore della resistenza totale del circuito è di {total_res} Ohm")
    
if __name__ == "__main__":
    main()