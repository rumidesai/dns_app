from flask import Flask, request
from flask_api import status
import json
from socket import *
import requests

app = Flask(__name__)

@app.route('/fibonacci', methods = ['GET'])
def parmeter_checks(hostname, fs_port, as_ip, as_port, number):
    '''
    Check if all parameters exist.
    '''
    if hostname == '' or fs_port == '' or as_ip == '' or as_port == '' \
    or number == '' or not number.isdigit():
        return status.HTTP_400_BAD_REQUEST

def accept_request():
    '''
    Accept request.
    '''
    hostname = request.args['hostname'] 
    fs_port = request.args['fs_port']
    as_ip = request.args['as_ip']
    as_port = int(request.args['as_port'])
    number = request.args['number']

    if parmeter_checks(hostname, fs_port, as_ip, as_port, number) == status.HTTP_400_BAD_REQUEST:
        # print('Wrong request')
        return 'bad request', status.HTTP_400_BAD_REQUEST

    client_socket = socket(AF_INET, SOCK_DGRAM)
    query = {'TYPE': 'A', 'NAME': hostname}
    client_socket.sendto(json.dumps(query).encode(), (as_ip, int(as_port)))
    ip_address, _ = client_socket.recvfrom(2048)
    fs_ip = ip_address.decode()
    address = 'http://' + fs_ip + ':' + fs_port
    result = requests.get(address + '/fibonacci', params={'number': number})
    return result.text, status.HTTP_200_OK

# Port 8080
app.run(host='0.0.0.0', port=8080, debug=True)
