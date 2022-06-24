from pprint import pprint
import requests
import os

class YaUploader:
    
    
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, path):
        url = f'{host}/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        resp = requests.get(url, params = params, headers = headers)
        return resp.json().get('href')
        


    def upload(self, path, path_to_file):
        upload_link = self.get_upload_link(path)
        headers = self.get_headers()
        os.chdir(path_str)

        resp = requests.put(upload_link, data = open(path_to_file, 'rb'), headers=headers)
        resp.raise_for_status() # ???
        if resp.status_code == 201: 
            print('Success')
      
host = 'https://cloud-api.yandex.net:443'
path_to_file = 
# file_name = 'огонь.jpeg'
token = 
if __name__ == '__main__':
    uploader = YaUploader(token)
    path_list = path_to_file.split('/')
    file_name = str(path_list[-1])
    path_str = '/'.join(path_list[0:-1])
    uploader.upload(file_name, path_to_file) 