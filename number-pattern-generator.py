def number_pattern(n):
    if not isinstance(n, int):
        return('Argument must be an integer value.')
    elif n <= 0:
        return('Argument must be an integer greater than 0.')
    else:
        for number in range(1, n + 1):
            if number == n:
                print(number, end='')
            else:
                print(number, end=' ')
    

print(number_pattern(2.0))
print(number_pattern(0))
print(number_pattern(4))


def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    
    else:
        number = ''
        for i in range(1,n+1):
            number += str(i) + ' '
        return number.strip()

print(number_pattern(4))