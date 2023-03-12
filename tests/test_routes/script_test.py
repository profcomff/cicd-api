import json


def test_script_execute(client):
    action = "test_script"
    url=f"/{action}"
    body = {
        "repo_url": 'https://...',
        "git_ref": '123123123'
    }
    res = client.post(url, data=json.dumps(body))
    print(str(res.json()))
    assert res.json()['code'] == 0
