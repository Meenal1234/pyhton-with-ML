from urllib2 import Request,urlopen
values = """
 {
   "image": "https://upload.wikimedia.org/wikipedia/commons/4/41/Ranbir_Kapoor_at_the_launch_of_%27Barfi%21%27_promo_10.jpg",
   "subject_id":"ranbir kapoor",
   "gallery_name": "My Gallery"
 }
"""
headers = {
 'Content-Type':'application/json',
 'app_id':'d5a618e9',
 'app_key':'c92e5f1a3bbf8a38acbd1ff671a1e457'
}
request=Request('https://api.kairos.com/enroll', data=values, headers=headers)
response_body=urlopen(request).read()
print (response_body)
