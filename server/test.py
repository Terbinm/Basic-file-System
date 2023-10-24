import os
import requests

def upload_files(client_id, folder):
    server_url = "http://127.0.0.1:80/input/" + client_id + "/A/"
    current_path = os.getcwd()
    directory = os.path.join(current_path, "out", folder)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'rb') as file:
            response = requests.post(server_url, files={'file': file})

            if response.status_code == 200:
                print(f"成功上傳 {filename}!")
            else:
                print(f"上傳 {filename} 失敗. 錯誤碼: {response.status_code}")

# 使用方法：
print(f"wait")
upload_files("223", "A")  # 上傳 out/A/ 中的所有檔案
# upload_files("your-client-id", "B")  # 上傳 out/B/ 中的所有檔案
