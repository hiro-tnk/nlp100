import sys

with open('hightemp.txt', 'r') as f:
    hightemp=f.readlines()
N=int(sys.argv[1])
print(''.join(hightemp[:N])[:-1]) #最後の改行は print しない
