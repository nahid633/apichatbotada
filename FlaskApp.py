#!flask/bin/python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
quest_ans = [
    {
        "question": "hi",
        "answer": "hello"
    },
    {
        "question": "how are you?",
        "answer": "i am fine.How about you?"
    },
]
@app.route('/')
def index():
    return 'Hello World'

# @app.route('/api/v1.0/answer/', methods=['POST'])
# def get_answer():
#     if not request.json or not 'question' in request.json:
#         abort(400)
#     answer = [conversation['answer'] for conversation in quest_ans if conversation['question'] == request.json['question']]
#     return jsonify({'answer': answer})

#
# if __name__ == '__main__':
#     app.run()
