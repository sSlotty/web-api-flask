import boto3
import csv

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = "C:/Users/thanathip/Desktop/web-api/src/001.jpeg"

client = boto3.client('rekognition',
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key,
                      region_name='us-west-2')

with open(photo,'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_labels(
    Image={
        'Bytes':source_bytes
    },
    MaxLabels=10
)

print(response)