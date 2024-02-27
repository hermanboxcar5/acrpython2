import os
import requests
import json
# Credentials
username = os.environ.get('username')
password = os.environ.get('password')

def authenticate_user():
    response = requests.post(
        "https://dev-nakama.winterpixel.io/v2/account/authenticate/email?create=false",
        data=json.dumps({
            "email": username,
            "password": password,
            "vars": {
                "client_version": "99999"
            }
        }),
        headers={
            "authorization":
            "Basic OTAyaXViZGFmOWgyZTlocXBldzBmYjlhZWIzOTo="
        })
    return response

def collect_timed_bonus(token):
    payload = '"{}"'
    response = requests.post(
        "https://dev-nakama.winterpixel.io/v2/rpc/collect_timed_bonus",
        headers={"authorization": f"Bearer {token}"},
        data=payload.encode('utf-8'))
    return response

response = authenticate_user()
token = json.loads(response.content)['token']
response = collect_timed_bonus(token)
