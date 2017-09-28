import boto3, json

def invoke_lambda():
    client = boto3.client('lambda')

    payload = {
        'key1': 'KEY1_CONTENT',
        'key2': 'KEY2_CONTENT',
        'key3': 'KEY3_CONTENT',
    }

    payload = json.dumps(payload)

    response = client.invoke(
        FunctionName='my_lambda_function',
        #InvocationType='RequestResponse',
        InvocationType='Event',
        LogType='Tail',
        Payload=payload,
    )
    print(response)

if __name__ == '__main__':
    invoke_lambda()
