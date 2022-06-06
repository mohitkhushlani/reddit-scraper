import praw
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)
print("Enter subreddits,type exit to exit")
subreddits = []
while(1==1):
    subreddit = input()
    if(subreddit == "exit"):
        break
    else:
        subreddits.append(subreddit)
print("Enter keywords , type stop to stop")
keywords = []
while(1==1):
    keyword = input()
    if(keyword == "stop"):
        break
    else:
        keywords.append(keyword)


print(subreddits)
print(keywords)

post_depth = int(input("enter post depth"))
comment_depth = int(input("enter comment depth"))
for keyword in keywords:
    for subreddit in subreddits:
        sr = reddit.subreddit(subreddit)
        results = 0
        for post in sr.top(limit=post_depth):
            pt = post.title.lower()
            if keyword in pt:

                print("********")
                print(post.title)

                print(">>>>")
                print(post.url)
            for comment in post.comments:
                    if hasattr(comment, "body"):
                        comment_lower = comment.body.lower()
                        if keyword in comment_lower:
                            print("----------")
                            print(comment.body)
