from flask import Flask, escape, request, render_template, jsonify, send_file
from flask_cors import CORS
import random
import numpy as np
import io
from PIL import Image
from datetime import timedelta
import pandas as pd


app = Flask(
    __name__,
    static_folder="../dist/static",
    template_folder="../dist"
)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

batch_data = (np.random.rand(10,256,256,3)*255).astype(np.uint8)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': random.randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/test_img')
def test_img():
    return send_file(
        open("./backend/test.png", 'rb'),
        mimetype="image/png",
        cache_timeout=0
    )

@app.route('/api/random_img')
def random_img():
    rand_img = (np.random.rand(256,256,3) * 255).astype(np.uint8)
    rand_img = Image.fromarray(rand_img)
    img_io = io.BytesIO()
    rand_img.save(img_io, "png")
    img_io.seek(0)
    return send_file(
        img_io,
        mimetype='image/png',
        as_attachment=False,
        attachment_filename='mkp.png',
        cache_timeout=0
    )

@app.route('/api/random_imgs/<idx>')
def show_one_from_batch(idx):
    img = Image.fromarray(batch_data[int(idx)])
    img_io = io.BytesIO()
    img.save(img_io, "png")
    img_io.seek(0)
    return send_file(
        img_io,
        mimetype='image/png',
        as_attachment=False,
        # attachment_filename='mkp.png',
        cache_timeout=0
    )


@app.route('/api/random_imgs')
def refresh_data():
    global batch_data
    batch_data = (np.random.rand(16,256,256,3)*255).astype(np.uint8)
    res = []
    for idx in range(batch_data.shape[0]//4):
        res.append({
            'A': 'random_imgs/' + str(4 * idx),
            'B': 'random_imgs/' + str(4 * idx + 1),
            'C': 'random_imgs/' + str(4 * idx + 2),
            'D': 'random_imgs/' + str(4 * idx + 3),
        })
    res = jsonify(res)
    return res

@app.route('/api/test_csv')
def open_csv():
    # test_df = pd.read_csv('./backend/test.csv')
    return send_file(
        'test.csv',
        mimetype='text/csv',
        cache_timeout=0
    )

@app.route('/api/save_csv', methods=['POST'])
def save_csv():
    post_data = request.get_data()
    # str_data = str(post_data, encoding='utf-8')
    f = open('save.csv', 'wb')
    f.write(post_data)
    f.close()
    # print(str_data)
    return 'received'


if __name__ == "__main__":
    app.run(debug=True)