RNG_A = 32310901
RNG_B = 1729
RNG_MOD = pow(2, 24)

class RNG:
    seed: int

    @classmethod
    def __init__(self, seed) -> int:
        self.seed = seed

    @classmethod
    def generate(self) -> int:
        new_val = (RNG_A * self.seed + RNG_B) % RNG_MOD
        self.seed = new_val

        return new_val

def main():
    seed = input("Inserisci un valore iniziale casuale: ")

    try:
        seed: int = int(seed)
    except ValueError:
        seed = hash(seed) # Fallback ad una hash del contenuto immesso

    rng = RNG(seed=seed)

    for i in range(0, 100):
        print(f"Iterazione {i}: {rng.generate()}")

    pass

if __name__ == "__main__":
    main()