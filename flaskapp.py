#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


#get all tasks method
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

#get individual task - abort if task ID not found
from flask import abort
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

#what happens if error code 404 encountered
#the (error) in the function seems to be meaningless
from flask import make_response
@app.errorhandler(404)
def not_found(error):
    #this makes a response with some json content saying the error type is not found
    #the ,404 just feeds in the status code passed with the response (good practice to
    #match the @errorhandler but not required)
    return make_response(jsonify({'error': 'Not found'}), 404)


#this is where i'm going to put the first POST request job



if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
