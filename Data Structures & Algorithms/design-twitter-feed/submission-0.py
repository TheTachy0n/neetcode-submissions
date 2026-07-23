from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)      # user -> [(time, tweetId)]
        self.followMap = defaultdict(set)      # user -> {followees}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        # User always follows themselves
        self.followMap[userId].add(userId)

        # Put the newest tweet of each followed user into the heap
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(heap, (-time, tweetId, followee, index))

        while heap and len(res) < 10:
            negTime, tweetId, followee, index = heapq.heappop(heap)
            res.append(tweetId)

            # Push the next older tweet from the same followee
            if index > 0:
                index -= 1
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(heap, (-time, tweetId, followee, index))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Can't unfollow yourself
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)