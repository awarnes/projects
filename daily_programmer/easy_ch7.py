"""
Write a program that can translate Morse code in the format of ...---...
A space and a slash will be placed between words. ..- / --.-
For bonus, add the capability of going from a string to Morse code.
Super-bonus if your program can flash or beep the Morse.
This is your Morse to translate:

.... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--

"""


import string


#  A list of punctuation to append to the english and morse code lists for better translation.
punct = [' ', ',', '\'', '"', '!', '?', '$', '%', '*', '(', ')', '[', ']', '/', '\\', '{', '}']

#  Create a string of letters and numbers for use in the dictionaries.
english = list(string.ascii_lowercase)
numbers = [str(i) for i in range(0, 10)]
english.extend(numbers)
english.extend(punct)

#  Morse code taken from http://morsecode.scphillips.com/translator.html after typing in full string a-z and 0-9
morse_txt = '.- | -... | -.-. | -.. | . | ..-. | --. | .... | .. | .--- | -.- | .-.. | -- | -. | --- | .--. | --.- | .-. | ... | - | ..- | ...- | .-- | -..- | -.-- | --.. | ----- | .---- | ..--- | ...-- | ....- | ..... | -.... | --... | ---.. | ----.'
morse = morse_txt.split(' | ')
morse.extend(punct)

#  Create an english to morse code dictionary.
eng_to_morse = dict()

for indeng, eng in enumerate(english):
    for indmor, mor in enumerate(morse):
        if indeng == indmor:
            eng_to_morse.update({eng: mor})

#  Create a morse code to english dictionary.
morse_to_eng = dict()

for indmor, mor in enumerate(morse):
    for indeng, eng in enumerate(english):
        if indmor == indeng:
            morse_to_eng.update({mor: eng})

def decode(msg=''):
    """
    Choose whether to decode from morse code to english or english to morse code.
    Can put a message in the call or paste a message into the input.
    Will return a normal English sentence or a string of morse code with letters
    separated by spaces and words separated by ' / '.
    """


    char_list = list()
    result = list()

    trans = input("Are you translating from [m]orse code to english or [e]nglish to morse code? ")

    choice = input("Did you already enter a message? [y/n] ")

    if 'y' in choice:
        pass
    elif 'n' in choice:
        msg = input("What is your message? ")
    else:
        print("I don't understand...")

    if 'm' in trans:
        msg = msg.split()

        for word in msg:
            char_list.extend(msg[msg.index(word)].split())

        for letter in char_list:
            try:
                result.append(morse_to_eng[letter])
            except KeyError:
                print("I'm sorry, there's something that's not morse code in that message!")

        for index, letter in enumerate(result):
            if index == 0:
                result[0] = letter.upper()

            if result[index - 2] in punct[1:] and not result[index - 1].isalpha():
                result[index] = letter.upper()

            if result[index] == '/':
                result[index] = ' '

        result = ''.join(result)

        return result

    elif 'e' in trans:
        msg = msg.lower()

        for word in msg:
            char_list.extend(msg[msg.index(word)])

        for letter in char_list:
            if letter == ' ':
                result.append('/')
            try:
                result.append(eng_to_morse[letter])
            except KeyError:
                print("I'm sorry, there's something that I cannot translate to morse code in that message!")

        result = ' '.join(result)

        return result

    else:
        print("I'm sorry, I don't understand...")

print(decode())
