from flask import Flask, request
from flask_api import status
import json
from socket import *

app = Flask(__name__)

def fib(number):
    '''
    Recursive fibonacci calculation.
    '''
    number = int(number)
    if number <= 1:
        return number
    return fib(number-1) + fib(number-2)

@app.route('/fibonacci', methods = ['GET'])
def fibonacci():
    '''
    Fibonacci server.
    '''
    number = request.args['number']
    result = fib(number)
    return str(result)

@app.route('/register', methods = ['PUT'])
def register():
    '''
    Registration.
    '''
    # print('In FS')
    content = request.get_json()
    hostname = content.get('hostname')
    ip = content.get('ip')
    as_ip = content.get('as_ip')
    as_port = int(content.get('as_port'))
    # print('In FS registration')
    # TTL - 15
    data = {'TYPE': 'A', 'NAME': hostname, 'VALUE': ip, 'TTL': 15}
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.sendto(json.dumps(data).encode(), (as_ip, int(as_port)))
    _, _ = client_socket.recvfrom(2048)
    return 'Registration complete', status.HTTP_201_CREATED

# Port 9090
app.run(host='0.0.0.0', port=9090, debug=True)
