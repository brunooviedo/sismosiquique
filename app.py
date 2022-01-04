from flask import *
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/areas')
def areas():
   return render_template('areas.html')

@app.route('/head')
def head():
   return render_template('head.html')

@app.route('/mapa')
def mapa():
   return render_template('mapa.html')

@app.route('/graf3d')
def graf3d():
   return render_template('graf3d.html')

@app.route('/magnitud')
def magnitud():
   return render_template('magnitud.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)