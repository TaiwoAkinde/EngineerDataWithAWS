from bs4 import BeautifulSoup
import requests
import csv
import boto3
import json
#from auth import ACCESS_KEY, SECRET_KEY

"""
    GET DATA FROM NEWS SITE
"""
def get_news_items():
        
    soup = BeautifulSoup(requests.get('https://www.newsnow.co.uk/h/World+News').text, 'lxml')
    csv_file = open('data.csv', 'w', newline='', encoding="utf-8")
    writer = csv.writer(csv_file)
    writer.writerow(['News Link', 'News Headline'])

    articles_2 = soup.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['hll'])
    news_object = {}
    news_list = []

    for article in articles_2:
        if article['href'][:6] == 'https:':

            """Jsonify Data for Dynamo DB"""
            news_object['_link'] = article['href']
            news_object['_headline'] = article.text

            news_list.append(news_object.copy())

            """Write Data to CSV for S3 Bucket"""
            writer.writerow([article['href'], article.text])   

    csv_file.close()
    return json.dumps(news_list)

def put_data_in_s3_bucket():
    pass


def put_data_in_dynamo_db():
    pass

get_news_items()
