from flask import Flask, render_template, request, redirect
from myLib import *
import pprint

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():  # put application's code here
    if request.method == "POST":
        url = request.form['url']
        print(url)
        data = getData(url)
        pprint.pprint(data)
        return redirect('/' + data['path'])
    return render_template("index.html")


@app.route('/<string:artist>', methods=["GET", "POST"])
def artist(artist):
    platforms = getPlatformObject(artist)
    data = getData(platforms[0]["url"])
    pprint.pp(data)
    image = data["image"]
    name = data["name"]
    return render_template("page.html", platforms=platforms, image=image, name=name)


@app.route('/<string:artist>/<string:track>', methods=["GET", "POST"])
def track(artist, track):
    platforms = getPlatformObject(artist + '/' + track)
    data = getData(platforms[0]["url"])
    pprint.pp(data)
    social = getSocial(data)
    image = data["image"]
    name = data["name"]
    return render_template("page.html", platforms=platforms, social=social, image=image, name=name)


@app.route('/api/<string:artist>', methods=["GET", "POST"])
def artistApi(artist):
    platforms = getPlatformObject(artist)
    data = getData(platforms[0]["url"])
    pprint.pp(data)
    image = data["image"]
    name = data["name"]
    obj = {"name": name, "image": image, "platforms": platforms}
    return obj


@app.route('/api/<string:artist>/<string:track>', methods=["GET", "POST"])
def trackApi(artist, track):
    platforms = getPlatformObject(artist + '/' + track)
    data = getData(platforms[0]["url"])
    pprint.pp(data)
    social = getSocial(data)
    image = data["image"]
    name = data["name"]
    obj = {"name": name, "image": image, "platforms": platforms, "social": social}
    return obj

if __name__ == '__main__':
    app.run()
