from subprocess import check_output
import re
from platform import system
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# find system private ip automatically run the server with your private ip address.
# Most connect wifi network or local network
# Example 192.168.0.23

if(system()=="Linux"):
    cmd="ifconfig"
else:
    cmd="ipconfig"
text=check_output(cmd,shell=True)
    

pattern = re.compile("\\d{1,3}(?:\\.\\d{1,3}){3}(?::\\d{1,5})?")
matcher=re.findall(pattern,text.decode('utf-8'))
for x in matcher:
    if x[0:7]=="192.168" and x[-3:]!="255":
        host=x

# end of the ip finder


server.bind((host,9999))

server.listen(3)
def main():
    con,addr=server.accept()
    con.send(b'welcome dear client...\n')

    while True:
        try:
            con.send(b'>')
            con.send(check_output( con.recv(1204).decode("utf-8") , shell=True )) # Process the client request command and send the returened data
        except(BrokenPipeError):
            print("Connection closed by user\nwaiting for new connection...")
            main()
        except(Exception):
            print("unexcepted error occured...\nre start....")
            con.send(b'Command is not found\n')

if __name__=="__main__":
    main()
    
# Access the server via netcat or telnet.
