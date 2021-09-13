
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reservation', methods=['POST'])
def write_reservation():
    checkIn_receive = request.form['checkIn_give']
    checkOut_receive = request.form['checkOut_give']
    room_receive = request.form['room_give']
    id_receive = request.form['id_give']

    doc = {
        'checkIn': checkIn_receive,
        'checkOut': checkOut_receive,
        'room': room_receive,
        'id': id_receive
    }

    db.reservation.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route('/reservation', methods=['GET'])
def reservation():
    reservations = list(db.reservation.find({}, {'_id': False}))
    return jsonify({'all_reservation': reservations})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
