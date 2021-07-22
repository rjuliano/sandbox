import json
import os
import locale
import boto3
from github import Github, GithubIntegration

GHAPP_ID = "125186";

ssm_client = boto3.client('ssm')

def handler(event, context):
    # print('Raw event:')
    # print(event)
    
    if 'X-GitHub-Event' not in event['headers']:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({'reason': "Invalid event received."})
        }

    body = json.loads(event['body']);
    print(json.dumps(body))

    hash_from_gh = event['headers']['X-Hub-Signature-256']
    if not validate_request(hash_from_gh, event['body']):
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({'reason': "Unable to validate event payload."})
        }

    
    event_type = event['headers']["X-GitHub-Event"];
    action = body['action'];
    installation_id = body['installation']['id'];
    
    github_client = login_as_app_installation(installation_id=installation_id)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps({
            'eventType': event_type,
            'action': action
        })
    }


def validate_request(hash_from_gh, body):
    return True

def login_as_app_installation(installation_id):
    gh_app_auth = GithubIntegration(GHAPP_ID, private_key=get_private_key())
    installation_authorization = gh_app_auth.get_access_token(installation_id=installation_id)
    return Github(installation_authorization.token)
    # private_key_as_bytes = bytearray(get_private_key(), locale.getpreferredencoding())
    # Github.login_as_app_installation(private_key_as_bytes, GHAPP_ID, installation_id)

def login_as_app(app_id:str):
    # TODO
    return

def get_private_key():
    ssm_param_name = os.environ.get('GITHUB_GHAPP_KEY') # next(filter(lambda key: key.endswith('GITHUB_GHAPP_KEY'), os.environ.keys()))
    if ssm_param_name is None:
        raise "Unable to lookup parameter name for private key lookup."
    # print(f"parameter: {ssm_param_name}")
    ssm_param_response = ssm_client.get_parameter(
        Name=ssm_param_name.replace("/env/","/dev/"),
        WithDecryption=True
    )
    return ssm_param_response['Parameter']['Value']
    



