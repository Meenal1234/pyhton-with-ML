from urllib2 import Request,urlopen
values = """
 {
   "image": "https://en.wikipedia.org/wiki/Ranbir_Kapoor#/media/File:Ranbir_Kapoor_promoting_Bombay_Velvet.jpg",
   "gallery_name": "My Gallery"
 }
"""
headers = {
 'Content-Type':'application/json',
 'app_id':'d5a618e9',
 'app_key':'c92e5f1a3bbf8a38acbd1ff671a1e457'
}
request=Request('https://api.kairos.com/recognize', data=values, headers=headers)
response_body=urlopen(request).read()
print (response_body)
