from typing import List


DRAWABLE_CHAR = '*'
SPACE_CHAR = ' '

def square(side_len: int) -> List[str]:
    lines = []

    for _ in range(side_len):
        lines.append(''.join([DRAWABLE_CHAR for _ in range(side_len)]))
    
    return lines

def triangle(side_len: int) -> List[str]:
    lines = []

    width = 1 + (2 * side_len) # Massima estensione

    for i in range(side_len):
        stars = 1 + (2 * i)
        space = (width - stars)

        line = ''.join([SPACE_CHAR for _ in range(int(space/2))] + [DRAWABLE_CHAR for _ in range(stars)] + [SPACE_CHAR for _ in range(int(space/2))])
        lines.append(line)
    
    return lines
        
def rhombus(side_len: int) -> List[str]:
    return triangle(side_len) + list(reversed(triangle(side_len)[:-1]))

def main():
    side_len = input("Inserisci un numero intero: ")

    try:
        side_len = int(side_len)
    except ValueError:
        print("Il valore immesso non è un numero!")
        exit(1)
    
    for shape in square, triangle, rhombus:
        for line in shape(side_len):
            print(line)

        print() # Empty separator

if __name__ == "__main__":
    main()