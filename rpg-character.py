full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        print('The character name should be a string')
    
    if len(name) > 10:
        print('The character name is too long')
    
    #check for spaces in name
    if name.find(' ') > 0:
        print('The character name should not contain spaces')
    
    #This is a generator expression that loops through the tuple. It checks each variable to see if it is an integer; all() returns: True if every value inside is True ; False if any value is False

    if not all(isinstance(x, int) for x in (strength, intelligence, charisma)): 
        print('All stats should be integers')

    #rewritten from: if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int): return 'All stats should be integers'

    if not all(x >= 1 for x in (strength, intelligence, charisma)):
        print('All stats should be no less than 1')

    if any(x > 4 for x in (strength, intelligence, charisma)):
        print('All stats should be no more than 4')

    if not sum((strength, intelligence, charisma)) == 7:
        print('The character should start with 7 points')

    print(name + '\nSTR ' + full_dot * strength + empty_dot * (10 - strength) + '\nINT ' + full_dot * intelligence + empty_dot * (10 - intelligence) + '\nCHA ' + full_dot * charisma + empty_dot * (10 - charisma))


create_character("bina", 3, 2, 1)