# -----------
# User Instructions
# 
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.
import sys

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.
    temp = ranks.pop(0)
    for number in ranks:
        if number != temp - 1:
            return False
        temp = number
    return True
# return (max(ranks)-min(ranks)) == 4) and len(set(ranks))==5

def flush(hand):
    "Return True if all the cards have the same suit."
    suit = hand.pop(0)[1]
    for card in hand:
        if card[1] != suit:
            return False
    return True
#suits =[s for r,s in hand]
#return len(set(suits))==1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
        Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r)==n : return r
    return None
# Your code here.

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
        tuple: (highest, lowest); otherwise return None."""
# Your code here.
    first = kind(2, ranks)
    if first != None:
        modified = list(ranks)
        modified.remove(first)
        modified.remove(first)
        second = kind(2, modified)
        if second != None:
            return (first, second)
    return None
# lowpair = kind(2, list(reversed(ranks))

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks
        

def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split()
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9,5)
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'

#print test()

if __name__ == "__main__":
    test()
