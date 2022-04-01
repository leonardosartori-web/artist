from flask import Flask, render_template, request, redirect
from myLib import *
import pprint

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
    print("Ciao")
    print(artist)
    platforms = getPlatformObject(artist)
    pprint.pp(platforms)
    data = getData(platforms[0]["url"])
    image = data["image"]
    name = data["name"]
    return render_template("page.html", platforms=platforms, image=image, name=name)


@app.route('/search/<string:artist>/<string:track>', methods=('GET', 'POST'))
def track(artist, track):
    platforms = getPlatformObject(artist + '/' + track)
    data = getData(platforms[0]["url"])
    social = getSocial(data)
    image = data["image"]
    name = data["name"]
    return render_template("page.html", platforms=platforms, social=social, image=image, name=name)


@app.route('/api/<string:artist>', methods=('GET', 'POST'))
def artistApi(artist):
    platforms = getPlatformObject(artist)
    data = getData(platforms[0]["url"])
    image = data["image"]
    name = data["name"]
    obj = {"name": name, "image": image, "platforms": platforms}
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

