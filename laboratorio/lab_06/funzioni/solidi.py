from math import pi, pow

def sphere_volume(r):
    """
    Returns the volume of a sphere with radius r.

    @param r: The radius of the sphere
    @return: The volume of the sphere
    """
    return 4/3 * pi * pow(r, 3)

def sphere_surface(r):
    """
    Returns the surface of a sphere with radius r.

    @param r: The radius of the sphere
    @return: The surface of the sphere
    """
    return 4 * pi * pow(r, 2)

def cylinder_volume(r, h):
    """
    Returns the volume of a cylinder with radius r and height h.
    
    @param r: The radius of the cylinder
    @param h: The height of the cylinder

    @return: The volume of the cylinder
    """
    return pi * pow(r, 2) * h

def cylinder_surface(r, h):
    """
    Returns the surface of a cylinder with radius r and height h.
    
    @param r: The radius of the cylinder
    @param h: The height of the cylinder

    @return: The surface of the cylinder
    """
    return 2 * pi * r * (r + h)

def cone_volume(r, h):
    """
    Returns the volume of a cone with radius r and height h.
    
    @param r: The radius of the cone
    @param h: The height of the cone
    
    @return: The volume of the cone
    """
    return 1/3 * pi * pow(r, 2) * h

def cone_surface(r, h):
    """
    Returns the surface of a cone with radius r and height h.
    
    @param r: The radius of the cone
    @param h: The height of the cone
    
    @return: The surface of the cone
    """
    return pi * r * (r + (r**2 + h**2)**0.5)

def main():
    r = input("Inserisci il raggio: ")
    h = input("Inserisci l'altezza: ")

    try:
        r = float(r)
        h = float(h)
    except ValueError:
        print("Errore: i valori inseriti non sono numeri.")
        exit(1)

    print(f"\nVolume della sfera: {sphere_volume(r)}")
    print(f"Superficie della sfera: {sphere_surface(r)}\n")

    print(f"Volume del cilindro: {cylinder_volume(r, h)}")
    print(f"Superficie del cilindro: {cylinder_surface(r, h)}\n")

    print(f"Volume del cono: {cone_volume(r, h)}")
    print(f"Superficie del cono: {cone_surface(r, h)}\n")

if __name__ == "__main__":
    main()