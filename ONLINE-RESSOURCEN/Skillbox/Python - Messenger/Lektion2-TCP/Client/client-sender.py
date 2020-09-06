import requests

# "/send"
# {"username": "", "text": ""}

response = requests.get("http://localhost:5000/")
print(response.text)

'''
in Lektion statt localhost/send nur /send benutzt
'''
#requests.post("localhost/send", json={"username": "Jack", "text": "Hi, Mary"})

print("Enter you name")
username = input()
print("Enter your password")
password = input()
response = requests.post("http://localhost:5000/auth", json={"username": username, "password": password})
#print(response.text)


if not response.json()['ok']:
    print("Wrong Password")
    exit()



while True:
    print("Message eingeben")
    text = input()
    response = requests.post("http://localhost:5000/send", json={"username": username, "password": password, "text": text})
    print(response.text)


response = requests.get("http://localhost:5000/messages")
print(response.text)