import requests
import json
import time

def get_datadome_id():
    url = "https://dd.garena.com/js/"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://shop.garena.sg",
        "Referer": "https://shop.garena.sg/",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Ch-Ua-Mobile": "?0"
    }
    data = {
        "ddk": "AE3F04AD3F0D3A462481A337485081",
        "request": "/app",
        "responsePage": "origin",
        "jsData": "{}",
        "Sec-Fetch-Site": "cross-site",
        "Referer": "https://shop.garena.sg/app"
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["cookie"]
    else:
        return None

def player_id_login(datadome_id):
    url = "https://shop.garena.sg/api/auth/player_id_login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://shop.garena.sg/app",
        "Content-Type": "application/json",
        "x-datadome-clientid": "SEmnNVoPrGKOReqQARqWnoNSOBaLXWDUmuA0Covkv45Qok11VK9tCu_pPGNd5A5Yeo5DalB418E6M7iumSyDoUzdA8J3CPMh~mlhSMEBW26Dv1ab4~igm4eKogKQWkGz",
        "Origin": "https://shop.garena.sg",
        "Connection": "keep-alive",
        "Cookie": f"datadome={datadome_id}; source=pc; mspid2=4483346109c2ef0021c5b85c57580fe3; _ga_R04L19G92K=GS1.1.1725882045.2.0.1725882102.0.0.0; _ga=GA1.2.760287480.1725878800; _gid=GA1.2.303626532.1725878801; session_key=y3e3bhe7oty9rr8p2zx88l1d1a0sjm0b",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=0"
    }
    data = {
        "app_id": 100067,
        "login_id": "18923821",
        "app_server_id": 0
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 403:
        captcha_url = response.json()["url"]
        print(f"Captcha encountered. Please solve the captcha at: {captcha_url}")
        input("Press Enter after solving the captcha...")
        return player_id_login(get_datadome_id())
    else:
        return None

def main():
    datadome_id = get_datadome_id()
    if datadome_id:
        response = player_id_login(datadome_id)
        if response:
            print(response)
        else:
            print("Failed to login")
    else:
        print("Failed to get DataDome ID")

if __name__ == "__main__":
    main()