import requests

def scrape():
    try:
        response = requests.get('https://api.proxyscrape.com/v2/', params={
            'request': 'displayproxies',
            'protocol': 'all',
            'timeout': '10000',
            'country': 'all',
            'ssl': 'all',
            'anonymity': 'all',
        })

        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        return e

def check_proxy(proxy):
    try:
        # Use a simple GET request to check the proxy
        response = requests.get('https://api.ipify.org/', proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False

if __name__ == "__main__":
    # Read the list of proxies from a file
    # with open("list.txt", "r") as f:
    #     proxies = f.read().splitlines()
    
    # for proxy in proxies:
    #     if check_proxy(proxy):
    #         print(f"[LIVE] {proxy}")
    #     else:
    #         print(f"[DEAD] {proxy}")
    print(scrape())