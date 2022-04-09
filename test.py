import requests

artistTest = "leonardosartori"
trackTest = "notturno"
urlTest = "https://open.spotify.com/artist/4NVhhX3tA4m84EqNNSOJV2"
queryTest = "Leonardo Sartori"

def concat(path):
    domain = "https://myartistpage.herokuapp.com"
    return domain + path


def returner(data):
    return data.ok


def testShowArtist():
    resp = requests.get(concat("/search/" + artistTest))
    return returner(resp)


def testShowTrack():
    resp = requests.get(concat("/search/" + artistTest + "/" + trackTest))
    return returner(resp)


def testApiArtist():
    resp = requests.get(concat("/api/" + artistTest))
    return returner(resp)


def testApiTrack():
    resp = requests.get(concat("/api/" + artistTest + "/" + trackTest))
    return returner(resp)


def testUrlApi():
    resp = requests.get(concat("/apiurl?url=" + urlTest))
    return returner(resp)


def testSearch():
    resp = requests.get(concat("/apiSearch/artist?query=" + queryTest))
    return returner(resp)


def testPath():
    resp = requests.get(concat("/apiPath?url=" + urlTest))
    return returner(resp)


if __name__ == '__main__':
    print(testShowArtist())
    print(testShowTrack())
    print(testApiArtist())
    print(testApiTrack())
    print(testUrlApi())
    print(testSearch())
    print(testPath())