from itertools import combinations
from collections import deque

def play_game(card_deck, card_deck2, N):
    card_deck2 = set(card_deck2)
    for card in card_deck:
        if N + 1 - card in card_deck2:
            card_deck2.remove(N+1-card)
            card_deck.remove(card)
            return True
    return False
    
def solution(coin, cards):
    answer = 0
    N = len(cards)
    card_deck = set(cards[:int(N/3)])
    card_remainder = deque(cards[int(N/3):])
    pending = []
    turn = 1
    while coin >= 0 and card_remainder:
        pending.append(card_remainder.popleft())
        pending.append(card_remainder.popleft())
    
        if play_game(card_deck, card_deck, N):
            pass
        elif coin >= 1 and play_game(card_deck, pending, N):
            coin -= 1
        elif coin >= 2 and play_game(pending, pending, N):
            coin -= 2
        else:
            break
        turn += 1
    return turn