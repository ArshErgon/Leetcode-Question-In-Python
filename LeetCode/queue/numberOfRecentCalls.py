


class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while t - self.queue[0] > 3000:
            self.queue.pop(0)

        return self.queue.__len__()



sol = RecentCounter()
print(sol.ping(1))
print(sol.ping(100))
print(sol.ping(3001))
print(sol.ping(3002))
