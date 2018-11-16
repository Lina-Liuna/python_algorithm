#write a class RecentCounter to count recent requests.
#It has only one method: ping(int t), where t represents some time in milliseconds.
#Return the number of ping s that have been made from 3000 milliseconds ago until now.
#Any ping with time in [t - 3000, t] will count, including the current ping.
#It is guaranteed that every call to ping uses a strictly larger value of t than before.

#Example:
import collections

#inputs = ["RecentCounter", "ping", "ping", "ping", "ping"],
Inputs = [1,100, 3001,3002]
#Output: [1, 2, 3, 3]

class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)

obj = RecentCounter()

for i in Inputs:
    param_1 = obj.ping(i)
    print(param_1)