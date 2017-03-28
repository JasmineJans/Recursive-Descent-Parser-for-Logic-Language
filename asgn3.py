'''
Class: CPSC 427 - 01
Assignment: asgn3.py, a recursive descent parser for our propositional logic language
Developer 1: Jasmine Jans (jjans) submitter
Developer 2: Myanna Harris (mharris)
Developer 3: Carol Joplin (cjoplin)

Date: 2/6/2017
Run as: python asgn2.py
During program: type sentence, with spaces between tokens, and hit enter
To end: type "q" and hit enter

Propositional Symbols = A ... Z
Truth Symbols = true, false
Connective Symbols = not, and, or, =, ->
'''

import sys

'''
checks if l==t, checks if the sentence is finished
and if not, moves to the next token
'''
def match(l, t, sentence):
    if l == t:
        if len(sentence) < 1:
            return "done"
        return sentence[0]
    else:
        return "No"

'''
checks if l is A...Z
'''
def propositionalSymbol(l, sentence):
    if l.isalpha() and l.isupper():
        l = match(l, l, sentence)
        if l == "done":
            return "Yes"
        elif l == "No":
            return l
        return connectiveSymbol(l, sentence[1:])
    else:
        return "No"

'''
checks if l is true or false
'''
def truthSymbol(l, sentence):
    if l == "true":
        l = match(l, "true", sentence)
        if l == "done":
            return "Yes"
        elif l == "No":
            return l
        return connectiveSymbol(l, sentence[1:])
    elif l == "false":
        l = match(l, "false", sentence)
        if l == "done":
            return "Yes"
        elif l == "No":
            return l
        return connectiveSymbol(l, sentence[1:])
    else:
        return "No"

'''
checks if l is a connective symbol
'''
def connectiveSymbol(l, sentence):
    if l == "and" or l == "or" or l == "=" or l == "->":
        l = match(l, l, sentence)
        if l == "done":
            return "No"
        elif l == "No":
            return l
        sentence = sentence[1:]

        return typeMethod(sentence, l)
    else:
        return "No"

'''
checks if l is a not symbol
'''
def notSymbol(l, sentence):
    l = match(l, "not", sentence)
    if l == "done":
        return "No"
    elif l == "No":
        return l
    sentence = sentence[1:]
    if l == "not":
        return notSymbol(l,sentence)
    elif l.isalpha() and l.isupper():
        l = match(l, l, sentence)
        if l == "done":
            return "Yes"
        elif l == "No":
            return l
        return connectiveSymbol(l, sentence[1:])
    else:
        return "No"
    
'''
checks if l is a prop, truth or not symbol
'''
def typeMethod(sentence, l):
    if l.isalpha() and l.isupper():
        return propositionalSymbol(l, sentence)
    elif l == "true" or l == "false":
        return truthSymbol(l, sentence)
    elif l == "not":
        return notSymbol(l, sentence)
    else:
        return "No"

'''
loops to ask for a sentence to check syntac of until
the user types "q"
'''
def main():
    sentence = raw_input("Please enter a sentence: \n")
    while not(sentence == "q"):
        sentence = sentence.split()
        if len(sentence) < 1:
            print "Yes"
        else:
            l = sentence[0]
            print typeMethod(sentence[1:], l)
        sentence = raw_input("Please enter a sentence: \n")

    return 0

if __name__ == '__main__':
    main()
