nric = input('Enter an NRIC number: ')

# Type your code below
prefix = nric[0]
valid_prefix = 'stgfSTGF'
digits = nric[1:8]
suffix = nric[-1]
if str(digits).isdecimal() and prefix in valid_prefix:
    num1 = int(nric[1])*2
    num2 = int(nric[2])*7
    num3 = int(nric[3])*6
    num4 = int(nric[4])*5
    num5 = int(nric[5])*4
    num6 = int(nric[6])*3
    num7 = int(nric[7])*2
    totalnum = num1 + num2 + num3 + num4 + num5     + num6 + num7
    if prefix == 'T' or prefix == 'G':
        totalnum += 4
    remainder = totalnum%11
    if remainder == 0:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'J'
        else:
            checkdigit = 'X'
    if remainder == 1:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'Z'
        else:
            checkdigit = 'W'
    if remainder == 2:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'I'
        else:
            checkdigit = 'U'
    if remainder == 3:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'H'
        else:
            checkdigit = 'T'
    if remainder == 4:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'G'
        else:
            checkdigit = 'R'
    if remainder == 5:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'F'
        else:
            checkdigit = 'Q'
    if remainder == 6:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'E'
        else:
            checkdigit = 'P'
    if remainder == 7:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'D'
        else:
            checkdigit = 'N'
    if remainder == 8:
        if prefix ==  'S' or prefix == 'T':
            checkdigit = 'C'
        else:
            checkdigit = 'M'
    if remainder == 9:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'B'
        else:
            checkdigit = 'L'
    if remainder == 10:
        if prefix == 'S' or prefix == 'T':
            checkdigit = 'A'
        else:
            checkdigit = 'K'
    if checkdigit == suffix:
        print('NRIC is valid.')
else:
        print('NRIC is invalid.')