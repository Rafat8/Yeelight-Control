import telnetlib

HOST = "192.168.1.4"  # your bulb ip here.
PORT = 55443

# connection to yeelight.
tn = telnetlib.Telnet(HOST, PORT)

# get command from user.
command = input("Which command? ")

# commands.
if command == "toggle":
    tn.write("{\"id\":1,\"method\":\"toggle\",\"params\":[]}\r\n".encode('ascii'))
elif command == "power on" or command == "on":
    tn.write("{\"id\":1,\"method\":\"set_power\",\"params\":[\"on\"]}\r\n".encode('ascii'))
elif command == "power off" or command == "off":
    tn.write("{\"id\":1,\"method\":\"set_power\",\"params\":[\"off\"]}\r\n".encode('ascii'))
elif command == "set bright" or command == "set_bright" or command == "set brightness" or command == "brightness" or command == "bright":
    bright = input("percentage? ")
    tn.write("{\"id\":1,\"method\":\"set_bright\",\"params\":[".encode('ascii') + bright.encode('ascii') + "]}\r\n".encode('ascii'))
else:
    print("bad_input")

# end session.
tn.close()
