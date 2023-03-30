import json

# Python 的 dict 類型資料
myDict = {
    "name": "kai test00",
    "description": "testing by kai",
    "image": "ipfs://QmYHiLbYTK9hMpGwLdG9JZvStRGfBaFwv6XEW2JaENuBox",
}

# 將 Python 資料轉為 JSON 格式，儲存至 output.json 檔案
with open("output.json", "w") as f:
    json.dump(myDict, f, indent = 3)