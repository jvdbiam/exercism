"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck

Card value rules used throughout this module:
1. 'J', 'Q', 'K' (face cards) = 10
2. 'A' (ace) = 1 (unless otherwise noted locally, e.g. when calculating blackjack/ace value)
3. '2' - '10' = numeric value
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    (Card value rules are defined at the top of the file.)
    """

    if card in ['J','Q','K']:
        return 10
    if card == 'A':
        return 1
    else:
        return int(card)



def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    (Card value rules are defined at the top of the file.)
    """

    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if v1 > v2:
        return card_one
    
    if v2 > v1:
        return card_two
    
    return (card_one, card_two)



def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    (Card value rules are defined at the top of the file.)
    """

    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if v1 + v2 + 11 > 21:
        return 1
    
    if 'A' in (card_one, card_two):
        return 1
    
    return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    (Card value rules are defined at the top of the file.)
    """

    if card_one in ('10','J','Q','K') and card_two == 'A':
        return True
    if card_two in ('10','J','Q','K') and card_one == 'A':
        return True
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if value_of_card(card_one) is value_of_card(card_two):
        return True
    return False

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if value_of_card(card_one) + value_of_card(card_two) in (9,10,11):
        return True
    return False
