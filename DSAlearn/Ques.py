from collections import deque

queue = deque(["George", "Trump", "Dane", "Jane"])
queue.popleft()
queue.pop()
print(queue)

queue.append("George")
queue.appendleft("Jane")
print(queue)

queue.rotate()  # can add anything in the parameter for *n amount of the rotates
print(queue)
