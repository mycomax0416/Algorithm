# import queue

# q = queue.Queue()
# q.put('A')
# q.put('B')
# q.put('C')

# while not q.empty():
#     print(q.get())
#-------------------------------
# def isEmpty():
#     return front == rear


# def isFull():
#     return (rear + 1) % len(cQ) == front


# def enQueue(item):
#     global rear
#     if isFull():
#         print("Queue_Full")
#     else:
#         rear = (rear + 1) % len(cQ)
#         cQ[rear] = item


# def deQueue():
#     global front
#     if isEmpty():
#         print("Queue_Empty")
#     else:
#         front = (front + 1) % len(cQ)
#         return cQ[front]

# cQ_SIZE = 4
# cQ = [0] * cQ_SIZE

# front = rear = 0

# enQueue('A')
# enQueue('B')
# enQueue('C')
# print(deQueue())
# print(deQueue())
# print(deQueue())
#----------------------------------
# arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# V, U = 7, 8

# G = [[] for _ in range(V+1)]
# visit = [False for _ in range(V+1)]

# for t in range(U):
#     G[arr.pop(0)] += [arr.pop(0)]

# print(G)

# Q = []
# Q += [1]

# while len(Q) > 0:
#     v = Q.pop(0)
#     print(v, end=' ')
#     if not visit[v]:
#         visit[v] = True
        
#         for w in G[v]:
#             if not visit[w] and not w in Q:
#                 Q += [w]
#---------------------------------------------------
arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
V, U = 7, 8

G = [[] for _ in range(V+1)]
visit = [False for _ in range(V+1)]

for t in range(U):
    first = arr.pop(0)
    second = arr.pop(0)
    G[first] += [second]
    G[second] += [first]

print(G)

Q = []
Q += [1]

while len(Q) > 0:
    v = Q.pop(0)
    print(v, end=' ')
    if not visit[v]:
        visit[v] = True
        
        for w in G[v]:
            if not visit[w] and not w in Q:
                Q += [w]

    
