from clinic_app import create_app

def test_app_loads():
    app = create_app()
    client = app.test_client()
    res = client.get("/auth/login")
    assert res.status_code == 200
