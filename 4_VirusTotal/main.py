import requests

api_key = input("Enter API key: ")

url = "https://www.virustotal.com/api/v3/files"

headers = {
    "accept": "application/json",
    "content-type": "multipart/form-data",
    "x-apikey": api_key
}
file_path = "FilesToScan/skeebi.txt"

with open(file_path, "rb") as file:
    files = {'file': (file_path, file)}

    response = requests.post(url, headers=headers, files=files)

print(response.text)
