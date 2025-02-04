import requests

url = "https://api-gw1-prod1.fisglobal.com/token"

payload = 'grant_type=client_credentials'
headers = {
  'Authorization': 'Basic RWFRV2Z3UGxSTFFDOExQRWNYaUlSTkMwb1ZJYTpiOHhUNUIxT25NTmJZRU5UZWhzaVByVkFwdU1h',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
