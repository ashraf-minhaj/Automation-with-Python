import requests
import io
endpoint = "https://api.virusscannerapi.com/virusscan"
headers = {
    'X-ApplicationID': 'Get your key from https://app.docconversionapi.com/#/applications',
    'X-SecretKey': 'Get your key from https://app.docconversionapi.com/#/applications'
}
file = open("example.html", "rb")
data = {
    'async': 'false',
}
files = {
    'inputFile': ('example.docx', file.read())
}
r = requests.post(url=endpoint, data=data, headers=headers, files = files)
response = r.text
print(response)