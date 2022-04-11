import json
import pandas as pd


def lambda_handler(event, context):
    print("Sample lambda function with Docker!")
    print("Request json msg:", json.dumps(event))
    series = pd.Series([2, 4, 6, 8])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda and pandas.. ' + str(series.max()))

    }
