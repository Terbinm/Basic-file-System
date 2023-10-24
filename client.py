import os
import requests
from concurrent.futures import ThreadPoolExecutor

class FileUploader:
    def __init__(self, client_id, folder):
        self.client_id = client_id
        self.folder = folder
        self.server_url = "http://127.0.0.1:9999/input/" + client_id + "/A/"
        self.directory = os.path.join(os.getcwd(), "out", folder)

    def upload_file(self, filename):
        """
        上傳單一檔案到伺服器。
        """
        file_path = os.path.join(self.directory, filename)
        with open(file_path, 'rb') as file:
            try:
                response = requests.post(self.server_url, files={'file': file})
                if response.status_code == 200:
                    print(f"成功上傳 {filename}!")
                else:
                    print(f"上傳 {filename} 失敗. 錯誤碼: {response.status_code}")
            except Exception as e:
                print(f"上傳 {filename} 時發生錯誤: {str(e)}")

    def upload_files(self):
        """
        上傳所有檔案到伺服器。使用多線程上傳。
        """
        filenames = os.listdir(self.directory)
        with ThreadPoolExecutor() as executor:
            executor.map(self.upload_file, filenames)

# 使用方法：
print("wait")
uploader = FileUploader("223", "A")  # 建立一個FileUploader實例
uploader.upload_files()  # 上傳 out/A/ 中的所有檔案
