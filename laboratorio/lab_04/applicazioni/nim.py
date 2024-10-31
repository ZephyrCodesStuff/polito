from enum import Enum
from math import floor
import random

RNG_LOW = 10
RNG_HIGH = 100

POWERS = [pow(2, x) for x in range(1, 7)]

class Player(Enum):
    HUMAN = 0,
    CPU = 1

    @staticmethod
    def from_int(i: int) -> 'Player':
        return Player.HUMAN if i == 0 else Player.CPU
    
    @classmethod
    def switched(self) -> 'Player':
        if self == Player.CPU:
            return Player.HUMAN
        else:
            return Player.CPU
    
    @staticmethod
    def random() -> 'Player':
        return Player.from_int(random.randint(0, 1))

class Intelligence(Enum):
    LOW = 0
    HIGH = 1

    @staticmethod
    def from_int(i: int) -> 'Intelligence':
        return Intelligence.LOW if i == 0 else Intelligence.HIGH
    
    @staticmethod
    def random()  -> 'Intelligence':
        return Intelligence.from_int(random.randint(0, 1))

def game_loop(orbs: int, start: Player, intelligence: Intelligence):
    remaining_orbs = orbs
    current_player = start

    while True:
        max_pickable = int(floor(remaining_orbs / 2))

        if current_player == Player.HUMAN:
            picked = None

            while picked == None:
                try:
                    picked = int(input("Quante biglie vuoi prendere?: "))

                    if picked > max_pickable:
                        raise ValueError
                except ValueError:
                    print("Il valore non è un numero valido (tra 1 e n/2). Riprova...")
                except KeyboardInterrupt:
                    print()
                    print("CTRL+C rilevato: termino...")
                    exit(0)
            
        else: # CPU
            if intelligence == Intelligence.LOW:
                if max_pickable == 0:
                    current_player = current_player.switched()

                    print()
                    print(f"Il giocatore {current_player.name} ha vinto!.")
                    break

                picked = random.randint(1, max_pickable)
            else:
                max_power = list(reversed([x for x in POWERS if x <= remaining_orbs]))

                if len(max_power) == 0:
                    current_player = current_player.switched()

                    print()
                    print(f"Il giocatore {current_player.name} ha vinto!.")
                    break

                picked = max_power[0] - 1
            
            print(f"{current_player.name} prende {picked} biglie.")

        remaining_orbs -= picked

        if remaining_orbs <= 0:
            current_player = current_player.switched()

            print()
            print(f"Il giocatore {current_player.name} ha vinto!.")

            break

        else:
            print()
            print(f"Rimangono {remaining_orbs} biglie.")
        
        current_player = current_player.switched()
    
def main():
    orbs = random.randint(RNG_LOW, RNG_HIGH)

    starting_player = Player.random()
    cpu_intel = Intelligence.random()

    print(f"Giocando con modalità di intelligenza: {cpu_intel.name}")
    print(f"Inizia: {starting_player.name}")

    game_loop(orbs, starting_player, cpu_intel)

if __name__ == "__main__":
    main()