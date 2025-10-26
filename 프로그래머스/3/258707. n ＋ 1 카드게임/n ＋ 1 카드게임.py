from collections import deque

def next_round(card_deck1, card_deck2, N):
    for card in card_deck1:
        if N + 1 - card in card_deck2:
            card_deck1.remove(card)
            card_deck2.remove(N+1-card)
            return True
    return False
def solution(coin, cards):
    N = len(cards)
    card_deck = cards[:int(N/3)]
    remainder = deque(cards[int(N/3):])
    pending = []
    answer = 1
    
    while coin >= 0 and remainder:
        pending.append(remainder.popleft())
        pending.append(remainder.popleft())
        
        if next_round(card_deck, card_deck, N):
            pass
        elif coin >= 1 and next_round(card_deck, pending, N):
            coin -= 1
        elif coin >= 2 and next_round(pending, pending, N):
            coin -= 2
        else:
            break
        answer += 1
    return answer