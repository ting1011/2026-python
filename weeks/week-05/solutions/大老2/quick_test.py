"""Quick functionality test"""

from game import Card, Deck, Hand, Player, HandClassifier, CardType

# Test Card creation
print("🧪 Testing Card...")
card1 = Card(14, 3)
card2 = Card(3, 0)
print(f"  Ace of Spades: {card1}")
print(f"  3 of Clubs: {card2}")
print(f"  Comparison: {card1} > {card2}? {card1 > card2}")

# Test Deck
print("\n🧪 Testing Deck...")
deck = Deck()
print(f"  Deck has {len(deck.cards)} cards")
dealt = deck.deal(5)
print(f"  Dealt 5 cards, {len(deck.cards)} remaining")

# Test Hand
print("\n🧪 Testing Hand...")
hand = Hand([Card(3, 0), Card(5, 1), Card(14, 3)])
print(f"  Hand size: {len(hand)}")
three_clubs = hand.find_3_clubs()
print(f"  Found 3♣? {three_clubs is not None}")

# Test Classifier
print("\n🧪 Testing HandClassifier...")
single = [Card(14, 3)]
pair = [Card(14, 3), Card(14, 2)]
triple = [Card(14, 3), Card(14, 2), Card(14, 1)]

result = HandClassifier.classify(single)
print(f"  Single card: {result[0].name if result else 'None'}")

result = HandClassifier.classify(pair)
print(f"  Pair: {result[0].name if result else 'None'}")

result = HandClassifier.classify(triple)
print(f"  Triple: {result[0].name if result else 'None'}")

# Test Player
print("\n🧪 Testing Player...")
player = Player("Alice", is_ai=False)
player.take_cards([Card(3, 0), Card(5, 1)])
print(f"  Player '{player.name}' has {len(player.hand)} cards")

print("\n✅ All basic tests passed!")
