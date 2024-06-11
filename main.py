import requests
    def fetch_data(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except  requests.RequestException as e:
            print(f"获取代码错误：{e}")
            return None

    if __name__ =="__main__":
        url = "https://api.github.com/repos/AwangGit/GLM4Learn"
        data = fetch_data(url)
        if data:
            print("仓库数据拉取成功")
            print(data)
        else:
            print("仓库数据获取失败")