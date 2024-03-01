import argparse

parser = argparse.ArgumentParser()
parser.add_argument('string', type=str, help='String for decryption')
args = parser.parse_args()

args.string = args.string.strip()

ls = args.string.split()
answer = ''
for word in ls:
    answer = ''.join([answer, word[0]])
  
print(answer)