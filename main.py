from blackjack_classes import Deck, Player

def play_blackjack():
    print("Welcome to Blackjack!\n")

    deck = Deck()

    player = Player("Player")
    dealer = Player("Dealer")

    for _ in range(2):
        player.hit(deck)
        dealer.hit(deck)

    player.show_hand()
    print(f"Dealer shows: {dealer.hand.cards[0]}\n")

    while True:
        action = input("Do you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            player.hit(deck)
            player.show_hand()
            if player.hand.value > 21:
                print("You bust! Dealer wins.")
                return
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    print("\n Dealer's turn...")
    dealer.show_hand()
    while dealer.hand.value < 17:
        dealer.hit(deck)
        print("Dealer hits...")
        dealer.show_hand()

    player_score = player.hand.value
    dealer_score = dealer.hand.value

    if dealer_score > 21:
        print("Dealer busts! You win!")
    elif dealer_score > player_score:
        print("Dealer wins.")
    elif dealer_score < player_score:
        print("You win!")
    else:
        print("It's a draw (Push).")

if __name__ == '__main__':
    play_blackjack()