import sys
sys.stdin = open('5521_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    best_friends = []
    invite = []

    for friend in G[1]:
        best_friends.append(friend)
        invite.append(friend)

    for friend in best_friends:
        for friend_friend in G[friend]:
            if friend_friend not in invite and friend_friend != 1:
                invite.append(friend_friend)

    print('#{} {}'.format(t+1, len(invite)))