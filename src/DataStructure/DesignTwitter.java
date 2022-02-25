package DataStructure;

import java.util.*;

// https://leetcode.com/problems/design-twitter/
public class DesignTwitter {
    private HashMap<Integer, HashSet<Integer>> follows; // userId as key
    private HashMap<Integer, LinkedList<Tweet>> tweets; // userId as key
    private int timestamp;

    private class Tweet implements Comparable<Tweet> {
        private int tweetId;
        private int ts;
        private int userId;

        public Tweet(int tweetId, int userId, int timestamp) {
            this.tweetId = tweetId;
            this.ts = timestamp;
            this.userId = userId;
        }

        @Override
        public int compareTo(Tweet t2) {
            return t2.ts - this.ts; // maxHeap
        }
    }

    /**
     * Initialize your data structure here.
     */
    public DesignTwitter() {
        follows = new HashMap<>();
        tweets = new HashMap<>();
        timestamp = 0;
    }

    /**
     * Compose a new tweet.
     */
    public void postTweet(int userId, int tweetId) {
        if (!tweets.containsKey(userId)) {
            tweets.put(userId, new LinkedList<>());
        }
        tweets.get(userId).add(0, new Tweet(tweetId, userId, timestamp++)); // put to index=0, most recent

        if (!follows.containsKey(userId)) { // follow self
            follows.put(userId, new HashSet<>());
            follows.get(userId).add(userId);
        }
    }

    /**
     * Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
     * users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
     */
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> feed = new LinkedList<>();
        PriorityQueue<Tweet> q = new PriorityQueue<>();
        if (!follows.containsKey(userId)) {
            return feed;
        }
        HashSet<Integer> followed = follows.get(userId);
        HashMap<Integer, Integer> count = new HashMap<>(); // track the current userId's position - where to fetch the next
        for (Integer followedUserId : followed) {
            if (tweets.containsKey(followedUserId)) {
                Tweet t = tweets.get(followedUserId).get(0);
                q.add(t);
                count.put(t.userId, 1);
            }
        }
        while (q.size() > 0 && feed.size() < 10) {
            Tweet t = q.poll();
            feed.add(t.tweetId);
            int next = count.get(t.userId); // refill the heap - greedy
            count.put(t.userId, next + 1);
            if (next < tweets.get(t.userId).size()) { // if there is still more tweets from this userId
                q.add(tweets.get(t.userId).get(next));
            }
        }
        return feed;
    }

    /**
     * Follower follows a followee. If the operation is invalid, it should be a no-op.
     */
    public void follow(int followerId, int followeeId) {
        if (!follows.containsKey(followerId)) {
            follows.put(followerId, new HashSet<>());
            follows.get(followerId).add(followerId);
        }
        follows.get(followerId).add(followeeId);
    }

    /**
     * Follower unfollows a followee. If the operation is invalid, it should be a no-op.
     */
    public void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) {
            return;
        }
        if (follows.containsKey(followerId)) {
            follows.get(followerId).remove(followeeId);
        }
    }
}

