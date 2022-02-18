from bs4 import BeautifulSoup
from requests import get

query = 'topstories'

country = get("http://ip-api.com/json").json()
CountryCode = country['countryCode']

origin = 'https://news.google.com'
path = f'/{query}?hl=en-{CountryCode}&gl={CountryCode}&ceid={CountryCode}:en'

html_text = get(origin + path).text
soup = BeautifulSoup(html_text, 'lxml')

newsBlock = soup.find_all('div', jscontroller='MRcHif')
print(len(newsBlock))

def getTopStories():
    allNews = []
    for block in newsBlock:
        headingText = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").h3.a.text
        image = block.find('div', 'DBQmFf NclIid BL5WZb Oc0wGc xP6mwf j7vNaf').div.a.figure.img['src']
        linkToSource = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").a['href'].replace(".", origin)
        source = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").div.div.a.text
        time = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").div.div.time['datetime']
        similarNewsBlocks = block.find_all('article', jscontroller='HyhIue')
        similarNews = []
        for Block in similarNewsBlocks:
            smallNewsBlock = Block.find("a", class_='DY5T1d RZIKme')
            smallNewsBlockDetails = Block.find("div", class_='QmrVtf RD0gLb kybdz')
            similarNews.append(
                {"Heading": smallNewsBlock.text, "Link": smallNewsBlock['href'], "Source": smallNewsBlockDetails.div.a.text, "Time": smallNewsBlockDetails.div.time['datetime']}
            )
        allNews.append({
            "Heading": headingText,
            "Image": image,
            "LinkToSource": linkToSource,
            "Source": source,
            "Time": time,
            "SimilarNews": similarNews
        })

    for news in allNews:
        print(f'''
            Heading: {news["Heading"]}
            Image: {news["Image"]}
            link: {news["LinkToSource"]}
            source: {news["Source"]}
            time: {news["Time"]}
            SimilarNews: {news["SimilarNews"]}
        ''')

def getTopicsNews():
    allNews = []
    for block in newsBlock:
        headingText = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").h3.a.text
        image = block.find("div", class_="DBQmFf NclIid BL5WZb Oc0wGc xP6mwf j7vNaf").figure.img['src']
        linkToSource = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").a['href'].replace(".", origin)
        source = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").div.div.a.text
        time = block.find('article', class_="MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne").div.div.time['datetime']

        allNews.append({
            "Heading": headingText,
            "Image": image,
            "LinkToSource": linkToSource,
            "Source": source,
            "Time": time,
        })

    for news in allNews:
        print(f'''
            Heading: {news["Heading"]}
            link: {news["LinkToSource"]}
            source: {news["Source"]}
            time: {news["Time"]}
            image: {news["Image"]}
        ''')



def main():
    if("topics" in query):
        getTopicsNews()
    elif("topstories" in query):
        getTopStories()


main()