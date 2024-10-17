INT_ONE: int = 10
INT_TWO: int = 25

def main():
    print(f"Somma:           { INT_ONE + INT_TWO }")
    print(f"Differenza:      { INT_ONE - INT_TWO }")
    print(f"Prodotto:        { INT_ONE * INT_TWO }")
    
    print(f"Valore medio:    { (INT_ONE * INT_TWO) / 2 }")
    print(f"Distanza:        { abs(INT_ONE - INT_TWO) }")

    print(f"Valore massimo:  { max(INT_ONE, INT_TWO) }")
    print(f"Valore minimo:   { min(INT_ONE, INT_TWO) }")
    
if __name__ == "__main__":
    main()