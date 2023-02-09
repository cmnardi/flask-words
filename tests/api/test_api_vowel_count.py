import json

def test_count_vowels_incorrect_method(app, client):
    res = client.get('/vowel_count')
    assert res.status_code == 405

def test_count_vowels_incorrect_field(app, client):
    data = {
        "word": ["a", "b", "c"]
    }
    res = client.post(
        '/vowel_count',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )
    response = json.loads(res.data)
    assert response["message"] == "Words field is required"
    assert res.status_code == 400

def test_count_vowels_ok(app, client):
    data = {
        "words": ["a", "b", "c"]
    }
    res = client.post(
        '/vowel_count',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )
    print(res)
    assert res.status_code == 200