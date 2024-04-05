import requests


url = 'https://newsdata.io/api/1/news?apikey=pub_3926120e9bf71e357caffd16d5e3c9126b6d3&q=ukraine'

data = requests.get(url)

news = data.json()

print('results')


# print(news["articles"])
      
# for latest in news["articles"]:
    #latest['author']
    #latest['title']
    #latest['url']
    #latest['content']


    # print(latest['url'])

