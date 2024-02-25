import os
import json
import requests
import time

def handler(req, res):
    username = os.environ['username']
    password = os.environ['password']

    while True:
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

        token = json.loads(response.content)['token']
        payload = '"{}"'

        response = requests.post(
            "https://dev-nakama.winterpixel.io/v2/rpc/collect_timed_bonus",
            headers={"authorization": f"Bearer {token}"},
            data=payload.encode('utf-8'))

        print(json.loads(response.content))

        time.sleep(1801)

    return 'Success'
