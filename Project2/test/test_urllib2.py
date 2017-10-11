import http.cookiejar
import urllib.request

url = "http://www.baidu.com"

print("method1")

response1 = urllib.request.urlopen(url)

print (response1.getcode())
print(len(response1.read()))

print("method2")
request = urllib.request.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print (response2.getcode())
print(len(response2.read()))

print("method3")
#cookie container
cj=http.cookiejar.CookieJar()

#creat an opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

#opener for urllib
urllib.request.install_opener(opener)

response3=urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())
