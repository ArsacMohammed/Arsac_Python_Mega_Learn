import requests
from send_email import send_email
api_key="154fcf9923d746c2b37b604d298efc00"   # get this from news.api.org

url="https://newsapi.org/v2/everything?q=tesla&from=2023-09-03&sortBy=publishedAt&apiKey=154fcf9923d746c2b37b604d298efc00"

request=requests.get(url)
# context=request.text   this provide the output in the string format but dict is more accessible therefore
content = request.json()
message=""" """
for index,article in enumerate(content["articles"]):
    message +=(str(index+1)+" "+article["title"]+("\n")+(4*" ")+article["description"]+(2*"\n"))

message=message.encode("utf-8")
send_email(message)


