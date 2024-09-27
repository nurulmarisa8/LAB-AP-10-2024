import random

def takecard():
    return random.randint(1, 11)

def player_turn():
    card_player = takecard()
    print(f"Kartu anda sekarang adalah: {card_player}")
    
    while True:
        pilihan = input("Apakah masih akan mengambil kartu? (y/n): ")
    
        if pilihan == "y" or pilihan == "Y":
            new_card = takecard()
            card_player += new_card
            print(f"Kartu baru anda adalah: {new_card}.")

            if card_player > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return card_player, False  
        elif pilihan == "n" or pilihan == "N":
            return card_player, True 
        else:
            print("Pilihan tidak valid. Masukkan 'y' atau 'n'.")

def dealer_turn():
    card_dealer = takecard()
    print(f"Kartu dealer adalah: {card_dealer}")
    
    while card_dealer < 17:
        new_card = takecard()
        card_dealer += new_card
        print(f"Kartu dealer sekarang adalah: {card_dealer}")
    
    return card_dealer

def main():
    print("Welcome to Blackjack!")
    card_player, player_in_game = player_turn()

    if not player_in_game:
        return 
    card_dealer = dealer_turn()
    if card_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif card_player > card_dealer:
        print("Anda menang!")
    elif card_player == card_dealer:
        print("Seri!")
    else:
        print("Dealer menang!")
main()
