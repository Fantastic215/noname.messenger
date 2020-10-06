from flask import Flask, jsonify, make_response,request
import os
app = Flask(__name__)
users={}#{name:{pwd,messege:{id:text}}
@app.route('/send_api',methods=['GET'])
def api():
    return jsonify({'name':'NoName.MessengeR','api_version':'0.1'})

@app.route('/send_api',methods=['POST'])
def api1():
    content = request.json
    if content['login'] in users.keys():
        if content['password'] == users.get(content['login']).get('password'):
            if content['to'] in users.keys():
                try:
                    users.get(content['login']).get('message')[content['to']]= users.get(content['login']).get('message').get(content['to'])+content['to']+'>> '+content['text']+'\n'
                    users.get(content['to']).get('message')[content['login']] = users.get(content['to']).get(
                    'message').get(content['login']) + content['login'] + '<< ' + content['text'] + '\n'

                except:
                    try:
                        users.get(content['login']).get('message')[content['to']] =  content['to'] + '>> ' + content['text'] + '\n'
                        users.get(content['to']).get('message')[content['login']] = content['login'] + '<< ' + content['text'] + '\n'
                    except Exception as e:
                        print(e)
                return jsonify({'name':'NoName.MessengeR','api_version':'0.1','state':'OK'})
@app.route('/login',methods=['POST'])
def api2():
    content = request.json
    if content['login'] in users.keys():
        if content['password'] == users.get(content['login']).get('password'):
            return jsonify({'name':'NoName.MessengeR','api_version':'0.1','state':'OK'})
    else:
        return jsonify({'name': 'NoName.MessengeR', 'api_version': '0.1', 'state': 'error'})

@app.route('/reg',methods=['POST'])
def api3():
    content = request.json
    if content['login'] not in users.keys():
        users[content['login']]={'password':str(content['password']),'message':{}}
        return jsonify({'name':'NoName.MessengeR','api_version':'0.1','state':'OK'})
    else:
        return jsonify({'name': 'NoName.MessengeR', 'api_version': '0.1', 'state': 'error'})

@app.route('/update',methods=['POST'])
def api4():
    content = request.json
    if content['login'] in users.keys():
        if content['password'] == users.get(content['login']).get('password'):
            if content['to'] in users.keys():
                return jsonify({'message':users.get(content['login']).get('message').get(content['to'])})
    else:
        return jsonify({'name': 'NoName.MessengeR', 'api_version': '0.1', 'state': 'error'})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'state': 'Not found'}),404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
