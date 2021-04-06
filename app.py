from bs4 import BeautifulSoup
import requests
import csv
import boto3
import json 
from auth import ACCESS_KEY_ID, SECRET_ACCESS_KEY, REGION

"""
    GET DATA FROM NEWS SITE
"""
def get_news_items():

    try:
                
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
    except Exception as e:
        return e

    return json.dumps(news_list)

"""PUT DATA IN S3 BUCKET"""
def put_data_in_s3_bucket():
    client = boto3.client(
        's3',
        aws_access_key_id = ACCESS_KEY_ID,
        aws_secret_access_key = SECRET_ACCESS_KEY,
        region_name = REGION,
    )
    try:
        client.create_bucket(Bucket = 'python-aws-data-engineering')

        with open("data.csv", "rb") as file:
            client.upload_fileobj(file, 'python-aws-data-engineering', "data.csv")

    except Exception as e:
        return e

    return {'status_code': 200, 'Message': f'{file.name} Uploaded Successfully'}

"""PUT DATA IN DYNAMO DB"""
def put_data_in_dynamo_db():
    pass

print(put_data_in_s3_bucket())
