class Twitter(object):

    def __init__(self):
        
        self.follows=defaultdict(set)
        self.posts=defaultdict(list)
        self.count=0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.posts[userId].append([self.count, tweetId])
        self.count-=1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res=[]
        minHeap=[]
        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            if followeeId in self.posts:
                index=len(self.posts[followeeId])-1
                count,tweetId= self.posts[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        while minHeap and len(res)<10:
            count,tweetId,followeeId,index=heapq.heappop(minHeap)
            res.append(tweetId)
            if index>=0:
                count,tweetId=self.posts[followeeId][index]
                heapq.heappush(minHeap,[count,tweetId,followeeId,index-1])
        return res


    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)