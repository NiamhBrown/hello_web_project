
def test_add_names(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Leo'

def test_add_name_with_none_given(web_client):
    response = web_client.get('/names?add=')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Please enter a name to add.'

# def test_add_name_with_no_name(web_client):
#     response = web_client.get('/names?add=')
#     assert response.status_code == 400
#     assert response.data.decode('utf-8') == "Please enter the name you'd like to add."

# """
# EXAMPLE 
# When: I make a POST request to /count_vowels
# And: I send "eee" as the body parameter text
# Then: I should get a 200 response with 3 in the message
# # """
# def test_post_count_vowels_eee(web_client):
#     response = web_client.post('/count_vowels', data={'text': 'eee'})
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

