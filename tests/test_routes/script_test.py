import pytest
import json
from starlette import status


def test_script_execute(client):
    url="/script/run"
    body = {
        "repo_url": 'surname',
        "commit_hash": 'union_number'
    }
    res = client.post(url, data=json.dumps(body))
    print(str(res.json()))
    assert res.json()['code'] == 0
