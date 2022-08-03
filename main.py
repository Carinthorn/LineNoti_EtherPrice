import requests
import datetime

def ether_price():
    url = 'https://notify-api.line.me/api/notify'
    token = "Ivp6PbZiQ0RMp81b7Tqz0PDDkJmYxjwevhpNU9D9bAw"
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    
    msg = "Hello line notify"
    resp = requests.post(url, headers=headers, data={"message":msg})
    print(resp.text)
    
ether_price()