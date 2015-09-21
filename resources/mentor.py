
parse = []
lines_to_write = []
year = ''
file = open('C:\\Users\\rahul\\Desktop\\NSight\\NSight\\resources\\mentors.txt', 'r')
f = open('C:\\Users\\rahul\\Desktop\\mentor_parse.txt', 'w')
for line in file:
    if(line[0] in '0123456789'):
        year = line.strip()
    else:
        parse = line.split(',')
        f.write(',\n{\n')
        f.write('\tname: \'' + parse[0].strip() + '\'')
        
        if (len(parse) > 2) :
            f.write(',\n\tyear: \'' + year + ' + ' + parse[2].strip() + '\'')
            f.write(',\n\toption: \'' + parse[1].strip() + '\'')
        elif (len(parse) > 1) :
            f.write(',\n\tyear: \'' + year + '\'')
            f.write(',\n\toption: \'' + parse[1].strip() + '\'')
        else :
            f.write(',\n\tyear: \'' + year + '\'')
            f.write(',\n\toption: \'undeclared\'')
            
        f.write('\n}')

f.close()
file.close()
