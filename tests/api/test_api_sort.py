import json

def test_sort_incorrect_method(app, client):
    res = client.get('/sort')
    assert res.status_code == 405

def test_sort_incorrect_field_words(app, client):
    data = {
        "word": ["a", "b", "c"]
    }
    res = client.post(
        '/sort',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )
    response = json.loads(res.data)
    assert "Words field is required" in response["errors"]
    assert res.status_code == 400

def test_sort_incorrect_field_order(app, client):
    data = {
        "words": ["a", "b", "c"], 
        "sort":"desc"
    }
    res = client.post(
        '/sort',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )
    response = json.loads(res.data)
    assert "Order field is required" in response["errors"]
    assert res.status_code == 400

def test_sort_incorrect_value_field_order(app, client):
    data = {
        "words": ["a", "b", "c"],
        "order": "ababab"
    }
    res = client.post(
        '/sort',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )
    response = json.loads(res.data)
    assert "Order field must be asc or desc" in response["errors"]
    assert res.status_code == 400

def test_sort_ok(app, client):
    data = {
        "words": ["a", "b", "c"],
        "order": "asc"
    }
    res = client.post(
        '/sort',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )
    print(res)
    assert res.status_code == 200