from socket import *
import json

def get_request(msg):
    '''
    Get request.
    '''
    message = json.loads(msg.decode())
    if 'VALUE' not in message:
        # DNS Query
        content = list_of_ips[message['TYPE'] + ' ' + message['NAME']]
        fs_ip = content['VALUE']
        return str(fs_ip).encode()
    else:
        # Registration
        hostname = message['NAME']
        ip = message['VALUE']
        request_type = message['TYPE']
        ttl = message['TTL']
        content = {'TYPE': request_type, 'NAME': hostname, 'VALUE': ip, 'TTL': ttl}
        key = request_type + ' ' + hostname
        list_of_ips[key] = content
        return json.dumps('').encode()


# Port 53533
server_port = 53533
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))

# Persistent store as per hints
list_of_ips = {}

while True:
    # print('Waiting to recv')
    msg, address = server_socket.recvfrom(2048)
    # print('In AS')
    response_message = get_request(msg)
    server_socket.sendto(response_message, address)
