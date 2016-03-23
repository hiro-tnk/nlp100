import sys

with open('hightemp.txt', 'r') as f:
    hightemp=f.readlines()
N=int(sys.argv[1])
L=len(hightemp) // N + 1

for i in range(N):
    with open('sp_hightemp_{0}.txt'.format(i), 'w') as f:
        f.writelines(hightemp[i*L:min(i*L+L, len(hightemp))])
