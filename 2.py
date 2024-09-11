import urllib.request
try:
    urllib.request.urlopen('http://www.google.com', timeout=2)
    print("Connected to the internet")
except urllib.error.URLError as e:
    print("No internet connection:", e) 