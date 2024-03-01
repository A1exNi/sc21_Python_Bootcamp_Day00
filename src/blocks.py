import argparse

def check_str(str):
    answer = True
    if len(str) == 32:
        for i in range(5):
            if str[i] != '0':
                answer = False
                break
        if answer and str[5] == '0':
            answer = False
    else:
        answer = False
    return answer

parser = argparse.ArgumentParser()
parser.add_argument('number_string', type=int, help='Number string for input')
args = parser.parse_args()

for i in range(args.number_string):
    str = input()
    str = str.strip()
    if check_str(str):
        print(str)

