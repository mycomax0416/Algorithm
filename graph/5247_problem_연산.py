import sys
sys.stdin = open('5247_sample_input.txt', 'r')
from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    
    queue = deque()
    queue.append((N, 0))
    visit = set()

    while queue:
        test_s, test_count = queue.popleft()

        if test_s == M:
            min_count = test_count
            break

        if test_s <= 1000000:
            if test_s+1 not in visit: 
                queue.append((test_s+1, test_count+1))
                visit.add(test_s+1)
            
            if test_s-1 not in visit:
                queue.append((test_s-1, test_count+1))
                visit.add(test_s-1)
            
            if test_s*2 not in visit:
                queue.append((test_s*2, test_count+1))
                visit.add(test_s*2)

            if test_s-10 not in visit:
                queue.append((test_s-10, test_count+1))
                visit.add(test_s-10)

    print('#{} {}'.format(t+1, min_count))