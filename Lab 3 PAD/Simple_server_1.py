from Server import *

host_name = HOST_NAME
message = host_name
file = FILE

if __name__ == '__main__':
	run_server(host_name, PORT_NUMBER, file, message)
