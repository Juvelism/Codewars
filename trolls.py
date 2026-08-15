def disemvowel(string_):

    vowels = "aeiou"

    for i in vowels:
        if i in string_.lower():
            print(f'Vowel/s is: {i}')

    #return string_

disemvowel('Yes')
