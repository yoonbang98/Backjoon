import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []
N = len(st1)
M = int(sys.stdin.readline())
for _ in range(M):
    command = sys.stdin.readline().strip()
    if command[0] == 'P':
        st1.append(command.split()[1])
    else:
        if command == 'L':
            if st1:
                st2.append(st1.pop())
        elif command == 'D':
            if st2:
                st1.append(st2.pop())
        else:
            if st1:
                st1.pop()
st1.extend(reversed(st2))
print(''.join(st1))