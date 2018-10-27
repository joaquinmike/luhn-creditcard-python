from library.luhn_creditcard import *

#Card Visa Valid
validateCard = libraryLuhnCreditCard.validCreditCard('4257418986233381','visa')
print(validateCard)

#Card MC Not Valid
validateCard = libraryLuhnCreditCard.validCreditCard('4257418986233381','mastercard')
print(validateCard)

#Card MC Not Valid
validateCard = libraryLuhnCreditCard.validCreditCard('5514757572511015','mastercard')
print(validateCard)
