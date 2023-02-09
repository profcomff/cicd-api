import json


def test_script_execute(client):
    action = "test_script"
    url=f"/{action}"
    body = {
        "repo_url": 'surname',
        "commit_hash": 'union_number'
    }
    res = client.post(url, data=json.dumps(body))
    print(str(res.json()))
    assert res.json()['code'] == 0
