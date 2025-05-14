# https://leetcode.com/problems/design-twitter/description/?envType=problem-list-v2&envId=plakya4j
# Neet

import collections
from typing import List


class Twitter:
    def __init__(self):
        self.usersPosts=collections.defaultdict(list)
        self.time=1
        self.followersToFollowees=collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.usersPosts[userId].append((self.time, tweetId))
        self.time+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        allTweets=self.usersPosts[userId].copy()
        for followeeId in self.followersToFollowees[userId]:
            if followeeId in self.usersPosts:
                allTweets+=self.usersPosts[followeeId]
        allTweets.sort(reverse=True, key=lambda x:x[0])
        return [tweetId for _, tweetId in allTweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.followersToFollowees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followersToFollowees[followerId]:
            self.followersToFollowees[followerId].remove(followeeId)

s=Twitter()
s.postTweet(1, 5)
s.postTweet(1, 6)
s.postTweet(1, 7)
s.postTweet(1, 8)
s.follow(1, 2)
s.postTweet(2, 10)
s.postTweet(2, 11)
print(s.getNewsFeed(1))
print(s.getNewsFeed(2))
