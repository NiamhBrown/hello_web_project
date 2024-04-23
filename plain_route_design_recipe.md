
# hello_web_project Route Design Recipe


## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Request:
GET /names?add=Eddie
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE
# GET /names?add=Eddie
#  Parameters:
#    name: Eddie
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""
# GET /names?add=
#  Parameters:
#    name: 
#  Expected response (400):
"""
'Please enter the name you'd like to add.'
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

# EXAMPLE
# GET /names?add=Eddie
#  Parameters:
#    name: Eddie
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""
def test_add_name(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

# EXAMPLE
# GET /names?add=
#  Parameters:
#    name: 
#  Expected response (400):
"""
Julia, Alice, Karim, Eddie
"""
def test_add_name_with_no_name(web_client):
    response = web_client.get('/names?add=')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Please enter the name you'd like to add."
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == Thanks Leo, you sent this message: "Hello world"'
```

