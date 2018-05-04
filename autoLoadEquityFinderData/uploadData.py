from __future__ import print_function
import boto3
import os
import sys
from botocore.vendored import requests


s3_client = boto3.client('s3')

# custom generated authorization token that never expires

authorization = "eyJpYXQiOjE1MjUzOTI4NTIsImV4cCI6MTUyNTM5NjQ1MiwiYWxnIjoiSFMyNTYifQ.eyJlbWFpbCI6ImF1dG9sb2FkQHRydWVwcm9kaWd5LnRlY2giLCJtb2R1bGVzIjpbIlByb2RpZ3kgRXF1aWZpbmRlciJdLCJ1c2VycmlnaHRzIjpbXSwiaWQiOjAsIm9mZmljZSI6IlRydWUgUHJvZGlneSJ9.sdPx8-KgAMtdhnYofUJfxfT2nCmnohnDgmDasfqPPTA"

alertUrl = "https://dev.trueprodigyapi.com/equityfinder/dataload/alert"

def handler(event, context):

    print(event, file=sys.stderr)

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        if key == "equityfinderdata.zip":

            response = requests.post(alertUrl, headers={'Authorization':authorization}, json={'bucket':bucket, 'key':key})

            if (response.ok):

                print(bucket)
                print(key)
                print("request was successful")

                    #regressionStats = response.json()
            else:

                print (response)
                response.raise_for_status()
