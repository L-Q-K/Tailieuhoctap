from models.girl_type import GirlType, dump_data
from flask import Flask, render_template, request, redirect
import mlab
from mongoengine import *

mlab.connect()

dump_data()

girl_type = GirlType(name= "Gái hư",
                    image= "https://via.placeholder.com/400x200",
                    description= "Hay đua đòi, ăn chơi, đi chơi qua đêm, bia, rượu,...")

#girl_type.save()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', girl_types=GirlType.objects())

@app.route ('/girl/<girl_id>')
def girldetail(girl_id):
    girl_type = GirlType.objects().with_id(girl_id)

    if girl_type is not None:
        return render_template("girl_type_detail.html", girl_type=girl_type)
    else:
        return "<h4>Không tìm thấy gái này</h4>"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin')
def adminn():
    return render_template('admin.html',girl_types=GirlType.objects())

@app.route('/delete_girl/<girl_id>')
def delete_girl(girl_id):
    #1. Delete girl from database:
    girl_type = GirlType.objects().with_id(girl_id)
    if girl_type is not None:
        #Found it:
        girl_type.delete()
    #2. Come back to admin:
    return redirect('/admin')

@app.route('/edit_girl/<girl_id>')
def edit_girl(girl_id):
    #1. Delete girl from database:
    girl_type = GirlType.objects().with_id(girl_id)
    if girl_type is not None:
        return render_template("girl_edit.html", girl_type= girl_type)
    else:
        return "<h4> Không có "+ gái + " này</h4>"

@app.route('/search')
def search_girl():
    args = request.args
    girl_type = args["girl"]
    girl_types =GirlType.objects()
    i = 0
    search_results = []
    for gt in girl_types:
        if (girl_type.lower() in gt["name"].lower()):
            search_results.insert(i, gt)
            i += 1
    if (i>0):
        return render_template("search_page.html", search_results=search_results)
    else:
        return "<h2> Sorry!We don't support for this girl type </h2>"


if __name__ == '__main__':
  app.run(debug=True)
