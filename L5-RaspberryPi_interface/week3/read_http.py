import http.client

conn = http.client.HTTPSConnection("www.uci.com")
conn.request("GET", "/index.html", ' ', {})
resu = conn.getresponse(1000)
print(resu.status, resu.reason, resu.info())
