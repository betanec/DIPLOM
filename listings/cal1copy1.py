url = self.base_url
data = {"content": message}
header = {"authorization": token}
r = requests.post(url, data=data, headers=header)