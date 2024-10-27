import requests
import json

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
        response = requests.get(f'http://ipapi.com/ip_api.php?ip={str(proxy).split(':')[0]}', proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            if "country_name" in response.text:
                data = response.json()
                country_name = data["country_name"]
                return country_name
            else:
                return False
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False

if __name__ == "__main__":
    for proxy in scrape():
        if check_proxy(proxy) == False:
            print(f"[DEAD] {proxy}")
        else:
            print(f"[LIVE] {proxy} - {check_proxy(proxy)}")