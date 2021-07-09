from flask import Flask, jsonify, request
from flask_cors import CORS
import trainer
app = Flask(__name__)
CORS(app)

@app.route('/chat',methods=['POST'])
def index():
    user_input = request.json['user_input']
    return jsonify({'msg':str(trainer.chatbot_response(user_input))})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=4200, debug=True)
 