import os
from flask import Blueprint


data = Blueprint('date',__name__)



@data.route('/upload/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(current_app.config['UPLOADED_PATH'], f.filename))
        return render_template('index.html')

@data.route('/completed/')
def completed():
    return '<h1>The Redirected Page</h1><p>Upload completed.</p>'

