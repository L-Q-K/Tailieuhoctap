from flask import *
import mlab
from mongoengine import *

mlab.connect()

class GirlType(Document):
    name = StringField()
    image = StringField()
    description = StringField()

girl_type = GirlType(name= "Gái hư",
                    image= "https://via.placeholder.com/400x200",
                    description= "Hay đua đòi, ăn chơi, đi chơi qua đêm, bia, rượu,...")

#girl_type.save()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', girl_types=GirlType.objects())


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/school')
def school():
    return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run(debug=True)
