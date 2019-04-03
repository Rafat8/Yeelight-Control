import telnetlib

HOST = "192.168.1.4"  # your bulb ip here.
PORT = 55443

# connection to yeelight.
tn = telnetlib.Telnet(HOST, PORT)

# toggle command.
tn.write("{\"id\":1,\"method\":\"toggle\",\"params\":[]}\r\n".encode('ascii'))

# end session.
tn.close()
