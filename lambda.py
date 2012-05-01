# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.
import re

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [ ('%s*%s' % (10**i, d)) for (i,d) in enumerate(word[::-1])]
        print(terms)
        return '('+ '+'.join( terms ) +')'
    else:
        return word

def test():
    assert compile_word('YOU') == '(1*U+10*O+100*Y)'
    assert compile_word('+') == '+'

test()
