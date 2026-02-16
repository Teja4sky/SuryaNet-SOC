import requests

cache={}

def locate(ip):

    if ip in cache:
        return cache[ip]

    try:

        r=requests.get(f"http://ip-api.com/json/{ip}")
        j=r.json()

        loc=f"{j['country']} {j['city']}"

        cache[ip]=loc

        return loc

    except:

        return "Unknown"
