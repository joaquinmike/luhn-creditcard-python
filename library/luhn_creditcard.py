'''
Validates popular debit and credit cards numbers against regular expressions and Luhn algorithm.
Also validates the CVC and the expiration date.
https://github.com/joaquinmike/luhn-creditcard-python

Converted code of Php (http://inacho.es)
'''
import re

class libraryLuhnCreditCard(object):

    cards = {
        'visaelectron':{
            'type': 'visaelectron',
            'pattern': r'^4(026|17500|405|508|844|91[37])',
            'length':{16},
            'cvcLength':{3},
            'luhn': True,
        },
        'maestro':{
            'type': 'maestro',
            'pattern': r'^(5(018|0[23]|[68])|6(39|7))',
            'length':{12, 13, 14, 15, 16, 17, 18, 19},
            'cvcLength':{3},
            'luhn': True,
        },
        'forbrugsforeningen':{
            'type': 'forbrugsforeningen',
            'pattern': r'^600',
            'length':{16},
            'cvcLength':{3},
            'luhn': True,
        },
        'dankort':{
            'type': 'dankort',
            'pattern': r'^5019',
            'length':{16},
            'cvcLength':{3},
            'luhn': True,
        },
        #Credit cards
        'visa':{
            'type': 'visa',
            'pattern': r'^4',
            'length':{13, 16},
            'cvcLength':{3},
            'luhn': True,
        },
        'mastercard':{
            'type': 'mastercard',
            'pattern': r'^(5[0-5]|2[2-7])',
            'length':{16},
            'cvcLength':{3},
            'luhn': True,
        },
        'amex':{
            'type': 'amex',
            'pattern': r'^3[47]',
            'format': r'(\d{1,4})(\d{1,6})?(\d{1,5})?',
            'length':{15},
            'cvcLength':{3, 4},
            'luhn': True,
        },
        'dinersclub':{
            'type': 'dinersclub',
            'pattern': r'^3[0689]',
            'length':{14},
            'cvcLength':{3},
            'luhn': True,
        },
        'discover':{
            'type': 'discover',
            'pattern': r'^6([045]|22)',
            'length':{16},
            'cvcLength':{3},
            'luhn': True,
        },
        'unionpay':{
            'type': 'unionpay',
            'pattern': r'^(62|88)',
            'length':{16, 17, 18, 19},
            'cvcLength':{3},
            'luhn': False,
        },
        'jcb':{
            'type': 'jcb',
            'pattern': r'^35',
            'length':{16},
            'cvcLength':{3},
            'luhn': True,
        },

    }

    @staticmethod
    def validCreditCard(number, type = None):
        try:
            ret = {'valid': False,'number': '','type': ''}
            #Strip non-numeric characters
            number = str(re.sub('/[^0-9]/', '', number))

            if not type:
                type = libraryLuhnCreditCard.creditCardType(number);


            if type in libraryLuhnCreditCard.cards and libraryLuhnCreditCard.validCard(number,type):
                return {
                    'valid': True,
                    'number': number,
                    'type': type
                }
            return ret

        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    @staticmethod
    def validCard(number, type):
        return (libraryLuhnCreditCard.validPattern(number, type) and libraryLuhnCreditCard.validLength(number, type) and libraryLuhnCreditCard.validLuhn(number, type));

    @staticmethod
    def validPattern(number, type):
        matches = re.search(libraryLuhnCreditCard.cards[type]['pattern'], number)
        return matches

    @staticmethod
    def creditCardType(number):
        for (card,data) in libraryLuhnCreditCard.cards.items():
            match = re.search(data['pattern'], number)
            if(match):
                return type

        return ''

    @staticmethod
    def validLength(number,type):
        data = libraryLuhnCreditCard.cards[type]['length']
        for length in data:
            if(len(number) == length):
                return True
        return False

    @staticmethod
    def validCvcLength(cvc, type):
        cvcLengths = libraryLuhnCreditCard.cards[type]['cvcLength']
        for cvcLength in cvcLengths:
            if(len(cvc) == cvcLength):
                return True
        return False

    @staticmethod
    def validLuhn(number, type):
        dluhn = libraryLuhnCreditCard.cards[type]['luhn']
        if dluhn:
            return libraryLuhnCreditCard.luhnCheck(number)
        else:
            return True

    @staticmethod
    def luhnCheck(number):
        try:
            checksum = 0
            dlen = int(len(number))
            ini = 2 - (dlen % 2) - 1
            for i in range(ini,dlen,2):
                checksum += int(number[i])

            #Analyze odd digits in even length strings or even digits in odd length strings.
            ini = (dlen % 2) + 1
            for i in range(ini,dlen,2):
                digit = int(number[i - 1]) * 2
                if digit < 10:
                    checksum += digit
                else:
                    checksum += (digit - 9)

            if checksum % 10 == 0:
                return True
            else:
                return False

        except ValueError:
            print("Oops!.  Try again...")
            return False
