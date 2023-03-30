from pinatapy import PinataPy
import requests
import json

pinata_api_key = '381dcf71a3f37534f152'
pinata_secret_api_key = '2936a7d5251793cf27245515ed15fd97fb7853d5e2c9b7ae5297cc2a9beecb1e'

def photo_ipfs():
    file = "0.png"
    pinata = PinataPy(pinata_api_key, pinata_secret_api_key)

    p = pinata.pin_file_to_ipfs(file, '/test07')
    photo_CID = p["IpfsHash"]
    
    myDict = {
        "name": "kai test00",
        "external_url": "https://ipfs.io/ipfs/"+photo_CID+"/0.png",
        "description": "testing by kai",
        "image": "https://ipfs.io/ipfs/"+photo_CID+"/0.png"
    }

    # 將 Python 資料轉為 JSON 格式，儲存至 output.json 檔案
    with open("0.json", "w") as f:
        json.dump(myDict, f)


# def json_ipfs():
#     pinata = PinataPy(pinata_api_key, pinata_secret_api_key)
#     json_file = "output.json"
#     j = pinata.pin_file_to_ipfs(json_file, '/test01')
#     json_CID = j["IpfsHash"]
#     return json_CID