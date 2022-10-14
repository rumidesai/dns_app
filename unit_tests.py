import requests

# Register FS
data = {"hostname": "fibonacci.com", "ip": "0.0.0.0", "as_ip": "0.0.0.0", "as_port": "53533"}
fs_ip = 'http://0.0.0.0'
fs_port = '9090'
fs_add = fs_ip + ':' + fs_port + '/register'
result = requests.put(fs_add, json=data)
print(result.text)

# print('Working till here')

# Test with a number
data = {'hostname': 'fibonacci.com', 'fs_port': '9090', 'as_ip': '0.0.0.0', 'as_port': '53533', 'number': 4}
us_ip = 'http://0.0.0.0'
us_port = '8080'
us_add = us_ip + ':' + us_port + '/fibonacci'
result = requests.get(us_add, params=data)
print(result.text)

# Test with a string - parmeter_checks() will throw an error
data = {'hostname': 'fibonacci.com', 'fs_port': '9090', 'as_ip': '0.0.0.0', 'as_port': '53533', 'number': 'strr'}
us_ip = 'http://0.0.0.0'
us_port = '8080'
us_add = us_ip + ':' + us_port + '/fibonacci'
result = requests.get(us_add, params=data)
print(result.text)
