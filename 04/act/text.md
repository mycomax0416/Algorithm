화학문제2



재귀 함수 - 자기 자신을 호출하는 함수

재귀 호출의 목적 --> 재귀적 정의(점화식) 구현하기 위해



for, while 사용하지 않고 반복적인 작업을 할 수 있다.



(그래프의 깊이 우선 탐색, 백트래킹)



```python
cnt = 0
def printHello(i, n):
    global cnt
    if i == n:
        cnt += 1
        return
   printHello(i + 1, n)
	printHello(i + 1, n)

printHello(0, 3)
print(cnt)
```

