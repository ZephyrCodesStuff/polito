def translate(s):
    match s:
        case "I":
            return 1
        case "V":
            return 5
        case "X":
            return 10
        case "L":
            return 50
        case "C":
            return 100
        case "D":
            return 500
        case "M":
            return 1000

def roman_to_arabic(s: str) -> int:
    total = 0
    
    while len(s) > 0:
        if len(s) == 1 or translate(s[0]) >= translate(s[1]):
            total += translate(s[0])
            s = s[1:]
        else:
            total -= translate(s[1]) - translate(s[0])
            s = s[2:]
    
    return total

def main():
    s = input("Inserisci un numero romano: ")
    print(f"Il numero arabo corrispondente è {roman_to_arabic(s)}.")

if __name__ == "__main__":
    main()