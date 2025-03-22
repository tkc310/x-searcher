import statistics
import asyncio
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from twikit import Client

# import pdb

load_dotenv()
EMAIL = os.getenv("EMAIL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

client = Client('ja-JP')

async def main(target_user_id):
    print("\nツイート取得中...🏃‍♂️")

    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

    tweets = []
    try:
      # 最新300件のツイートを取得
      tweets = await client.search_tweet(
        query=f"from:{target_user_id}",
        product='Latest',
        count=300
      )
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return

    # pdb.set_trace()

    # インプレッション数のリスト作成
    impressions = [int(tweet.view_count or 0) for tweet in tweets]

    # 平均インプレッション数を計算
    avg_impressions = statistics.mean(impressions)
    print(f"\n平均インプレッション数: {avg_impressions:.1f}")

    avg_gq_tweets = []

    for tweet in tweets:
      view_count = int(tweet.view_count or 0)
      if view_count >= avg_impressions:
        avg_gq_tweets.append(tweet)

    # 平均以上のインプレッションを持つツイートを表示
    print(f"\n=== 平均インプレッション以上のツイート (合計{len(avg_gq_tweets)}件) ===")

    for index, tweet in enumerate(avg_gq_tweets):
      print("-" * 50)
      print(f"{index + 1}件目")
      print(f"ID: {tweet.id}")
      print(f"内容: {tweet.text}")
      print(f"インプレッション数: {view_count}")
      print(f"投稿日時: {tweet.created_at_datetime.strftime('%Y/%m/%d %H:%M:%S')}")

    print("-" * 50)

if __name__ == "__main__":
    target_user_id = input("分析したいXアカウントのユーザーIDを入力してください: ")
    asyncio.run(main(target_user_id))
