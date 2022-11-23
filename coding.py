@app.route('/add/<a>/<b>', methods=['GET'])
def add(a, b):
    try:
        a, b = float(a), float(b)
    except ValueError:
        return jsonify({'Value Error': "Only numbers Please"})
    return jsonify({'result': a + b})
