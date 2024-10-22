import requests
import time
from concurrent.futures import ThreadPoolExecutor

# 网站 URL
URL = "https://sixu.org/"
# 线程数量
NUM_THREADS = 100
# 请求间隔（秒）
REQUEST_INTERVAL = 0.1

def visit_website():
    while True:
        try:
            response = requests.get(URL)
            if response.status_code == 200:
                print(f"访问成功: {response.status_code}")
            else:
                print(f"访问失败，状态码: {response.status_code}")
        except requests.RequestException as e:
            print(f"请求异常: {e}")
        # 等待指定时间后重新访问
        time.sleep(REQUEST_INTERVAL)

def main():
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        for _ in range(NUM_THREADS):
            executor.submit(visit_website)

if __name__ == "__main__":
    main()
