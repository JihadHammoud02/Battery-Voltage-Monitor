import requests

# set up the request parameters
url = 'https://numerique-60ae4-default-rtdb.europe-west1.firebasedatabase.app'
data = {'bat': 40}  # example data to be sent

# send the POST request
response = requests.post(url, json=data)

# check the response status code
if response.status_code == 200:
    print('Data sent successfully!')
else:
    print('Error sending data. Status code:', response.status_code)
