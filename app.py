from flask import Flask, request, render_template, jsonify
import numpy as np
import cv2

app = Flask(__name__)

# 指定拡張子
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# 拡張子チェック関数
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload', methods=["POST"])
def upload():
  if 'file' not in request.files:
      return jsonify({'result': False, 'message': 'ファイルが選択されていません。'})
  img_file = request.files['file']
  fileName = request.form['fileName']
  if fileName == "":
    return jsonify({
      'result': False, 'message': '保存するファイルの名前を指定してください。'
    })
  if img_file.filename == '':
    return jsonify({
        'result': False, 'message': '選択したファイルの名前がありません。'
    })
  if not allowed_file(img_file.filename):
    return jsonify({
        'result': False, 'message': 'このファイル形式は読み込めません。'
    })
  if not allowed_file(fileName):
    return jsonify({
        'result': False, 'message': 'このファイル形式で保存することはできません。'
    })

  img_array = np.asarray(bytearray(img_file.stream.read()), dtype=np.uint8)
  img = cv2.imdecode(img_array, 1)
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  img_path = './images/' + fileName
  cv2.imwrite(img_path, img_gray)
  
  return jsonify({ 'result': True })


if __name__ == '__main__':
    app.run()
