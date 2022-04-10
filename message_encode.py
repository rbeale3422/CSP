"""Class module that defines a cipher message class called Message"""
class Message():
    def __init__(self, original_message, offset):
        self.original = original_message
        self.off = offset
        self.encrypted_message = self.__encode()
    
    def __encode(self):
        letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
        new_message = ''
        for c in self.original:
            if c == ' ' or c == '.' or c == '?' or c == '!':
                new_message += c
            else:
                letter_pos = letters.index(c) + self.off
                if letter_pos > len(letters) - 1: # index is past the last letter, wrap around
                    letter_pos -= len(letters)
                new_message += letters[letter_pos]
        return new_message
