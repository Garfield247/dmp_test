import os
from flask import Blueprint,request,current_app


data = Blueprint('date',__name__)



#@data.route('/upload/', methods=['POST', 'GET'])
#def upload():
#    if request.method == 'POST':
#        f = request.files.get('file')
#        f.save(os.path.join(current_app.config['UPLOADED_PATH'], f.filename))
#        return render_template('index.html')

#@data.route('/completed/')
#def completed():
#    return '<h1>The Redirected Page</h1><p>Upload completed.</p>'
@data.route('/upload/', methods=['GET', 'POST'])
def index():                                        # 一个分片上传后被调用
    if request.method == 'POST':
        upload_file = request.files['file']
        task = request.form.get('task_id')          # 获取文件唯一标识符
        chunk = request.form.get('chunk', 0)        # 获取该分片在所有分片中的序号
        filename = '%s%s' % (task, chunk)           # 构成该分片唯一标识符
        upload_file.save(os.path.join(current_app.config.get("UPLOADED_PATH"),filename))  # 保存分片到本地
    return "OK"


@data.route('/success', methods=['GET'])
def upload_success():                               # 所有分片均上传完后被调用
    target_filename = request.args.get('filename')
    task = request.args.get('task_id')
    chunk = 0
    with open(os.path.join(current_app.config.get("UPLOADED_PATH"),target_filename), 'wb') as target_file:
        while True:
            try:
                filename = os.path.join(current_app.config.get("UPLOADED_PATH"),'%s%d' % (
      task, chunk))
                source_file = open(filename, 'rb')                    # 按序打开每个分片
                target_file.write(source_file.read())                 # 读取分片内容写入新文件
                source_file.close()
            except IOError:
                break
            chunk += 1
            os.remove(filename)                     # 删除该分片，节约空间
    return 'OK'
