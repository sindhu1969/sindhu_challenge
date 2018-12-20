import re

class CreditCard:

	def __init__(self):
		self.PATTERN = r'^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

	def validate_creditcard(self, card):
		match_result = re.match(self.PATTERN, card)
		if not match_result:
			return False
		if not self.check_card_has_repeated_sequence(card):
			return False
		if card.count('-') not in (0, 3):
			return False
		return True
		
	def check_card_has_repeated_sequence(self, card):
		card = card.replace("-", "")
		numbers = set(list(card))
		flag = True
		card_list = list(card)
		for i in numbers:
			seq = str(i) * 4
			if seq in card:
				flag = False
				break
		return flag


if __name__ == '__main__':
    N = int(input())
    
    credit_cards = []
    for i in range(N):
        credit_cards.append(input())
	cardService = CreditCard()
    for credit_card in credit_cards:
        if cardService.validate_creditcard(credit_card):
            print('Valid')
        else:
            print('Invalid')