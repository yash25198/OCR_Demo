from flask import Flask,render_template,request
import os
from ocr import ocr

app = Flask(__name__)

ALLOWED_FORMATS = {'png', 'jpg', 'jpeg', 'gif'}
DEFAULT_FOLDER = "/static/uploads/"


def allowed_formats(file):
    return '.' in file and file.rsplit('.',1)[1].lower() in ALLOWED_FORMATS


@app.route('/',methods = ['GET','POST'])
def homepage():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', msg = 'File not found in uploads')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', msg = 'No File Selected')
        if file and allowed_formats(file.filename):
            file.save(os.path.join(os.getcwd() + DEFAULT_FOLDER, file.filename))
            text = ocr(file)
            return render_template('index.html',msg = 'Success',obtained_text = text,img_src = DEFAULT_FOLDER + file.filename)

    else:
        return render_template('index.html');


#
if __name__ == '__main__':


    app.run(debug = True)


