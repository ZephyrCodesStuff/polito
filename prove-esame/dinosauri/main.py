# Il file da cui leggere il mazzo di carte dei giocatori.
DATA_FILE: str = "mazzo.txt"

# Il numero di giocatori.
PLAYER_COUNT = 2

# Lo stato iniziale di ognuno dei giocatori.
PLAYER_INIT = { "cards": [], "points": 0 }
PLAYERS = [dict.copy(PLAYER_INIT) for _ in range(PLAYER_COUNT)]

# Il numero di turni del gioco.
# 
# Il mazzo deve contenere almeno ``ROUNDS * 2`` carte.
ROUNDS = 15

# Le carte sul tavolo al momento.
#
# Viene resettato ogni volta che un giocatore vince un turno,
# e viene mantenuto se accade un pareggio.
TABLE = []

def points(color: str) -> int:
    match color:
        case "Rosso":
            return 5
        case "Verde":
            return 3
        case "Giallo":
            return 1

    return 0

def print_player_points():
    for (i, x) in enumerate(PLAYERS):
        print(f"Punteggio giocatore {i+1}: {x["points"]}")

def main():
    lines = []

    try:
        with open(DATA_FILE, "r") as f:
            lines = [x.strip() for x in f.readlines() if x.strip() in ["Rosso", "Verde", "Giallo"]]

            # Distribuisci le carte ai giocatori, in ordine alterno
            for i in range(PLAYER_COUNT):
                PLAYERS[i]["cards"] = lines[i::PLAYER_COUNT]

    except IOError:
        print(f"[!] Non è stato possibile leggere il file `{DATA_FILE}`!")
        exit(1)
    
    finally:
        f.close()
    
    # Assicuriamoci che i giocatori abbiano ricevuto abbastanza carte per ``ROUNDS`` turni
    for i in range(PLAYER_COUNT):
        if len(PLAYERS[i]["cards"]) < ROUNDS:
            print(f"[!] Il giocatore {i} non ha abbastanza carte nel mazzo per {ROUNDS} turni.\nIl minimo è {ROUNDS * 2}, ma il giocatore ne ha soltanto {len(PLAYERS[i]["cards"])}.")
            exit(1)
    
    # Se ne hanno ricevute di più, prendiamo solo quelle necessarie
    for round in range(ROUNDS):
        print(f"\nMano n. {round+1}")

        for i in range(PLAYER_COUNT):
            print(f"Carta giocatore {i+1}: {PLAYERS[i]["cards"][round]}")

        # Mettiamo le carte sul tavolo
        TABLE.extend([x["cards"][round] for x in PLAYERS])

        # Prendiamo le ultime carte messe sul tavolo
        current_round_cards = TABLE[::-1][:PLAYER_COUNT][::-1]

        max_value = max([points(x) for x in current_round_cards])
        max_cards = [i for i, x in enumerate(current_round_cards) if points(x) == max_value]

        # Controlliamo se ci sono giocatori che hanno pareggiato
        if len(max_cards) > 1:
            print(f"Pareggio tra i giocatori: {', '.join([str(x+1) for x in max_cards])}")
            print_player_points()

            continue

        # Trova il giocatore che ha vinto
        max_card_idx = max_cards[0]

        print(f"Vince la mano il giocatore {max_card_idx+1}")
        PLAYERS[max_card_idx]["points"] += sum([points(x) for x in TABLE])
        TABLE.clear()

        print_player_points()
        
    
    # Annuncia il vincitore
    max_player_points = max([x["points"] for x in PLAYERS])
    max_players = [(i, x) for i, x in enumerate(PLAYERS) if x["points"] == max_player_points]

    if len(max_players) > 1:
        print(f"Vincono in pareggio i giocatori: {', '.join([str(i+1) for i, _ in max_players])}")
    
    else:
        winner_idx, winner = max_players[0]
        
        print(f"\nVince il giocatore {winner_idx+1}, con {winner["points"]} punti!")

if __name__ == "__main__":
    main()