#!/usr/bin/python3
#Classes are defined for to convert Roman numerals to Arabic and vice versa.

class Checkforclass(object):
    """Creates objects with functions that check whether a word entered contains certain letters"""
    def __init__(self, checkfor = "aeiou"):
        super(Checkforclass, self).__init__()
        self.checkfor = checkfor.lower()

    def check_for(self, word = "Default"):
        """Returns Boolean true or false depending on whether the word entered contains at least one letter from the object string"""
        self.word = word
        for v in self.checkfor:
            if v in word.lower():
                return True
        return False

    def check_all(self, word = "Default"):
        """Returns Boolean true or false depending on whether the word entered is only made up of letter from the object string"""
        self.word = word
        for v in word.lower():
            if not v in self.checkfor:
                print(f"Error: Not all letters are contained in \"{self.checkfor}\": e.g. \"{v}\"")
                return False
        else: return True
