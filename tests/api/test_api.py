def test_health_get(app, client):
    res = client.get('/')
    assert res.status_code == 200

