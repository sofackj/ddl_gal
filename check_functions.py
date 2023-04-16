import requests

def test_requests(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
    try:
        response = requests.get(url, headers=headers)
        return True if response.status_code == 200 else False
    except:
        print(f"Couldn't process the following url with the request module :\n{url}")

