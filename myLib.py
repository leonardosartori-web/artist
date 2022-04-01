import requests
from bs4 import *
from requests.structures import CaseInsensitiveDict
import pprint
import validators
import tldextract

def getData(link):
    url = "https://songwhip.com/"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = "{\"url\":\"" + link + "\"}"
    resp = requests.post(url, headers=headers, data=str(data))
    return resp.json()


def getLinksTrack(url):
    xhtml = requests.get(url)
    soup = BeautifulSoup(str(xhtml.text), "html.parser")
    links = []
    for link in soup.findAll('a'):
        tmp = link.get('href')
        if validators.url(tmp):
            links.append(tmp)
    links = links[:-4]
    return links

def refData(data):
    for x in data:
        pprint.pp(x)

def getDomain(url):
    res = tldextract.extract(url)
    return res.domain.capitalize()

def getPlatformObject(query):
    links = getLinksTrack("https://songwhip.com/" + query)
    platforms = []
    for x in links:
        platforms.append({"name": getDomain(x), "url": x})
    return platforms


def getSocial(data):
    res = data["artists"][0]["links"]
    keys = dict(res).keys()
    platforms = ['facebook', 'instagram']
    links = []
    for x in platforms:
        if x in keys:
            tmp = {"url": res[x][0]["link"], "name": x}
            links.append(tmp)
    return links


# pprint.pp(getSocial("https://open.spotify.com/album/5XpHo23Du4H9scYqGxLUIJ"))
# pprint.pp(getData("https://open.spotify.com/artist/4NVhhX3tA4m84EqNNSOJV2"))