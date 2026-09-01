import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps('Hello from out CICD Github actions workflow vscode')
    }