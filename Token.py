""" Token - an object that has a value and type
    Eg: for 3, the value type will be INTEGER and the value will be 3
    The process of breaking the input string into tokens  is called lexical analyzer
    
"""
class Token(object):
    def __init__(self, type, value):
        # We have three types of tokens: 
        # INTEGER, PLUS or EOF
        self.type = type
        # the values are 0 to 9, + or none
        self.value = value

    def __str__(self):
        """Method for the string representation of the class instance.
            Like: Token(INTEGER, 5)
        """
        return 'Token({type}, {value})'.format(
            type = self.type, 
            value = repr(self.value)
        )
    
    # changing the repr to the str function output 
    def __repr__(self):
        return self.__str__()
