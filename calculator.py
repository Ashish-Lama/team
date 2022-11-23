@app.route('/multiply/<a>/<b>', methods=['GET'])
def multiply(a, b):
    try:
        a, b = float(a), float(b)
    except ValueError:
        return jsonify({'Value Error': "Only numbers Please"})
    return jsonify({'result': a * b})
