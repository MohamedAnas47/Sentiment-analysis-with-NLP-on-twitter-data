from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2020, 1, 10)
end_date = dt.date(2020, 4, 29)

limit = 500
lang = 'english'


class scratch:
    def scr(self, keyword):


        tweets = query_tweets("delhi riots", limit=limit, begindate=begin_date, enddate=end_date, lang=lang)
        # tweets = query_tweets(keyword, limit=limit, begindate=begin_date, enddate=end_date, lang=lang)
        print(tweets)
        df = pd.DataFrame(t.__dict__ for t in tweets)
        print(df)

        k = 1

        for i in df.values:
            screen_name = (i[0])
            if screen_name is None:
                screen_name = ""
            print("1", screen_name)

            username = (i[1])
            if username is None:
                username = ""
            print("2", username)

            user_id = (i[2])
            if user_id is None:
                user_id = ""
            print("3", user_id)

            tweet_id = (i[3])
            if tweet_id is None:
                tweet_id = ""
            print("4", tweet_id)

            tweet_url = (i[4])
            if tweet_url is None:
                tweet_url = ""
            print("5", tweet_url)

            timestamp = (i[5])
            if timestamp is None:
                timestamp = ""
            print("6", timestamp)

            imestamp_epoch = (i[6])
            if imestamp_epoch is None:
                imestamp_epoch = ""
            print("7", imestamp_epoch)

            text = (i[7])
            if text is None:
                text = ""
            print("8", text)

            text_html = (i[8])
            if text_html is None:
                text_html = ""
            print("9", text_html)

            links = (i[9])
            if links is None:
                links = ""
            links = ""
            print("10", links)

            hashtags = i[10]
            if hashtags is None:
                hashtags = ""
            hashtags = ""
            print("11", hashtags)

            has_media = (i[11])
            if has_media is None:
                has_media = ""
            # print("12", has_media)

            img_urls = (i[12])
            if img_urls is None:
                img_urls = ""
            img_url = ""
            print("13", img_urls)

            vedio_url = (i[13])
            if vedio_url is None:
                vedio_url = ""
            vedio_url = ""

            print("14", vedio_url)

            likes = (i[14])
            if likes is None:
                likes = ""
            print("15", likes)

            retweets = (i[15])
            if retweets is None:
                retweets = ""
            print("16", retweets)

            replies = (i[16])
            if replies is None:
                replies = ""
            print("17", replies)

            is_replied = (i[17])
            if is_replied is None:
                is_replied = ""
            print("18", is_replied)

            is_reply_to = (i[18])
            if is_reply_to is None:
                is_reply_to = ""
            print("19", is_reply_to)

            parent_tweet_id = (i[19])
            if parent_tweet_id is None:
                parent_tweet_id = ""
            print("20", parent_tweet_id)

            reply_to_users = (i[20])
            if reply_to_users is None:
                reply_to_users = ""
            reply_to_users = ""
            print("21", reply_to_users)

            print(type(screen_name))

            text_html = text_html.replace(
                '<p class="TweetTextSize js-tweet-text tweet-text" data-aria-label-part="0" lang="en">', "")
            text_html = text_html.replace('</p>', "")
            text_html = text_html.replace("'", "")
            text = text.replace("'", "")
            text = text.replace("/", "")
            username = username.replace("'", "")

            # qry ="insert into  tweets  values(null,'"+screen_name+"','"+username+"','"+str(user_id)+"','"+str(tweet_id)+"','"+str(tweet_url)+"','"+str(timestamp)+"','"+str(imestamp_epoch)+"','"+str(text)+"','"+str(text_html)+"','"+str(links)+"','"+str(hashtags)+"','"+str(has_media)+"','"+""+"','"+""+"','"+str(likes)+"','"+str(retweets)+"','"+str(replies)+"','"+str(is_replied)+"','"+""+"','"+str(parent_tweet_id)+"','00','00','00')"

            qry = "insert into  tweets  values(null,'" + screen_name + "','" + username + "','" + str(
                user_id) + "','" + str(tweet_id) + "','','','','" + str(text) + "','','','" + str(
                hashtags) + "','" + str(has_media) + "','" + "" + "','" + "" + "','" + str(likes) + "','" + str(
                retweets) + "','','" + str(is_replied) + "','" + "" + "','" + str(parent_tweet_id) + "','00','00','00')"
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            print(qry)

            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


obj = scratch()
obj.scr("delhi")
