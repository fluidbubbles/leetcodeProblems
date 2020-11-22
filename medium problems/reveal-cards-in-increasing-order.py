import collections


def deckRevealedIncreasing(deck):
    deck.sort()
    index = collections.deque(range(len(deck)))
    ordered = [0] * len(deck)
    for card in deck:
        ordered[index.popleft()] = card
        if index:
            index.append(index.popleft())
    return ordered
