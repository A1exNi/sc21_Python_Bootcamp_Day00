try:
    file_name = input()
    file = open(file_name, 'r')
    answer = 'True'
    count_line = 0
    for line in file:
        line = line.strip()
        if count_line > 2 or len(line) != 5:
            answer = 'Error'
            break
        if count_line == 0:
            if (line.count('*') != 2 or line[0] != '*' or line[4] != '*'):
                answer = 'False'
                break
        elif count_line == 1:
            if (line.count('*') != 4 or not line.startswith('**') or not
                line.endswith('**')):
                answer = 'False'
                break
        else:
            if (line.count('*') != 3 or line[0] != '*' or
                line[2] != '*' or line[4] != '*'):
                answer = 'False'
                break
        count_line += 1
    file.close()
    if count_line != 3 and answer == 'True':
        answer = 'Error'
    print(answer)
except FileNotFoundError:
    print(f'File {file_name} not found')
