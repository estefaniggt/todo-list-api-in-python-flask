from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
        { "label": "My first task", "done": False }
        ]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_tras = jsonify(todos)

    return json_tras

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    json_todos = jsonify(todos)
    return json_todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_newtodos = jsonify(todos)
    return json_newtodos

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)