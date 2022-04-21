from flask import Flask, render_template, request, redirect
from myLib import *
import pprint
from spotify import *

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        url = request.form['url']
        print(url)
        data = getData(url)
        pprint.pprint(data)
        return redirect('/search/' + data['path'])
    else:
        return render_template("index.html")


@app.route('/search/<string:artist>', methods=('GET', 'POST'))
def showArtist(artist):
    platforms = getPlatformObject(artist)
    about = getAbout(artist)
    pprint.pp(platforms)
    albums = getArtistAlbums(getArtistIdByUrl(platforms[0]["url"]))
    albumData = getData(albums[0]["url"])
    social = getSocial(albumData)
    data = getData(platforms[0]["url"])
    image = data["image"]
    name = data["name"]
    return render_template("page.html", platforms=platforms, image=image, name=name, about=about, social=social)


@app.route('/search/<string:artist>/<string:track>', methods=('GET', 'POST'))
def showTrack(artist, track):
    platforms = getPlatformObject(artist + '/' + track)
    data = getData(platforms[0]["url"])
    pprint.pp(data)
    social = getSocial(data)
    image = data["image"]
    name = data["name"]
    return render_template("page.html", platforms=platforms, social=social, image=image, name=name)


@app.route('/api/<string:artist>', methods=('GET', 'POST'))
def artistApi(artist):
    platforms = getPlatformObject(artist)
    about = getAbout(artist)
    data = getData(platforms[0]["url"])
    image = data["image"]
    name = data["name"]
    albums = getArtistAlbums(getArtistIdByUrl(platforms[0]["url"]))
    albumData = getData(albums[0]["url"])
    social = getSocial(albumData)
    obj = {"name": name, "image": image, "platforms": platforms, "about": about, "social": social}
    pprint.pp(obj)
    return obj


@app.route('/api/<string:artist>/<string:track>', methods=('GET', 'POST'))
def trackApi(artist, track):
    platforms = getPlatformObject(artist + '/' + track)
    data = getData(platforms[0]["url"])
    social = getSocial(data)
    image = data["image"]
    name = data["name"]
    obj = {"name": name, "image": image, "platforms": platforms, "social": social}
    return obj


@app.route('/apiurl', methods=('GET',))
def urlApi():
    args = request.args
    url = args.get("url")
    data = getData(url)
    return redirect('/api/' + data['path'])


@app.route('/apiSearch/<string:types>', methods=('GET',))
def search(types):
    args = request.args
    query = args.get("query")
    data = searchQuery(query, types)
    return redirect('/apiurl?url=' + data)


@app.route('/apiPath', methods=('GET',))
def getPath():
    args = request.args
    url = args.get("url")
    data = getData(url)
    return data['path']