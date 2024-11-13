import os
import requests
import time

api_key = input("Enter API key: ")

folder_path = "FilesToScan"
upload_url = "https://www.virustotal.com/api/v3/files"
report_url = "https://www.virustotal.com/api/v3/analyses/"

headers = {
    "accept": "application/json",
    "x-apikey": api_key
}

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if not os.path.isfile(file_path):
        continue

    with open(file_path, "rb") as file:
        files = {'file': (filename, file)}

        response = requests.post(upload_url, headers=headers, files=files)
        
        if response.status_code == 200:
            data = response.json()
            analysis_id = data['data']['id']
            print(f"Checking {filename} results...")

            while True:
                report_response = requests.get(report_url + analysis_id, headers=headers)
                report_data = report_response.json()

                if report_response.status_code == 200 and 'data' in report_data:
                    status = report_data['data']['attributes']['status']
                    if status == 'completed':
                        stats = report_data['data']['attributes']['stats']
                        print(f"File: {filename}")
                        print(f"Results: {stats}")
                        break
                    else:
                        print("Analysis in progress")
                        time.sleep(10)
                else:
                    print(f"Failed to report for {filename}. {report_response.status_code}")
                    break
        else:
            print(f"Failed to upload {filename}. {response.status_code}")
