import urllib
import httplib2

http = httplib2.Http()

url = 'http://127.0.0.1:8080'   
body1 = {'requestType': 'print_all'}
body2 = {'requestType': 'new_repo', 'params': ["012","Zsigmond"]}

headers = {'Content-type': 'application/x-www-form-urlencoded'}
response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body1))
print content

response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body2))
print content

#Configuring the new topology
#setConfiguration(content)
