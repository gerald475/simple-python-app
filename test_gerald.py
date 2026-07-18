from gerald import app

def test_home_route():
    # 1. Create a virtual test client for your Flask app
    client = app.test_client()
    
    # 2. Simulate a GET request to the homepage
    response = client.get('/')
    
    # 3. Assert (verify) that the server responds with a 200 OK status code
    assert response.status_code == 200
    
    # 4. Assert that the page returns the exact string you expect
    assert b"Hello, my name is Gerald. What is your name?" in response.data

def test_greet_route_with_name():
    client = app.test_client()
    
    # Simulate a POST request with form data just like your curl command did
    response = client.post('/greet', data={'name': 'TechGangsta'})
    
    assert response.status_code == 200
    assert b"Hello TechGangsta!" in response.data

def test_greet_route_default_guest():
    client = app.test_client()
    
    # Simulate a POST request with no name provided to test the 'Guest' fallback
    response = client.post('/greet')
    
    assert response.status_code == 200
    assert b"Hello Guest!" in response.data
