from socket import *



# mail server ip is default for local machines
def smtp_client(port=1025, mailserver='127.0.0.1'):
        # a placeholder msg not used in the code
        msg = "\r\n My message"

        # a special string message that marks the end of an email
        endmsg = "\r\n.\r\n"

        # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

        # Create socket called clientSocket and establish a TCP connection with mailserver and port

        # Fill in start

        # AF_INET is for ipv4 addresses
        # SOCK_STREAM is a streaming socket for TCP
        clientSocket = socket(AF_INET, SOCK_STREAM)

        # connecting the cocket to the mailserver and port
        #the connect methodstarts a 3-way handshake for tcp connection with remote server
        #
        clientSocket.connect((mailserver, port))

        # Fill in end

        # recieve data from the SMTP server on the socket and decode it from bytes to a string
        # uses upto a maximum of 1024 bytes
        # the data recieved is for debugging like 220 for server reaady to start convo and 550 that the request is not successful
        #the recv function blocks until it recieves data from the server and the recieved data is return in bytes
        recv = clientSocket.recv(1024).decode()

        #print(recv) #You can use these print statement to validate return codes from the server.
        # onlt the first 3 letters
        #if recv[:3] != '220':
        #    print('220 reply not received from server.')

        # create the Send HELO command, after a few steps we print server response.
        # this message contains the Helo command that will be sent into SMTP server - initiate and identify client to server
        heloCommand = 'HELO Alice\r\n'

        # send message to the server
        # encode string to bytes
        clientSocket.send(heloCommand.encode())

        # recieve a response from the the same network socket
        #max is 1024 bytes
        #the recv method blocks until it recieves data from the server

        #the recv function blocks until it recieves data from the server and the recieved data is return in bytes
        #decode converts bytes to string
        # the 250 response means that the server is ready to proceed with convo
        recv1 = clientSocket.recv(1024).decode()
        #print(recv1)
        #if recv1[:3] != '250':
        #    print('250 reply not received from server.')



        # Send MAIL FROM command and handle server response.
        # Fill in start

        # create a string containing the MAIL FROM command that is sent to SMTP server
        mailFrom = 'MAIL FROM: <al8211@nyu.edu>\r\n'

        #send MAIL FROM command to SMtp server over network socket
        #encode converts into byte sequences
        clientSocket.send(mailFrom.encode())

        # this recieves a response from SMTP server on the same network socket, max 1024 bytes and decode to string
        recv2 = clientSocket.recv(1024).decode()

        # check if 250 is back, if not display message
        # print(recv2)
        # if recv2[:3] != '250':
        #    print('250 reply not received from server.')

        # Fill in end


        # Send RCPT TO command and handle server response.
        # Fill in start

        sendRcpt = 'RCPT TO: <aishalallics@gmail.com>\r\n'
        clientSocket.send(sendRcpt.encode())
        recv3 = clientSocket.recv(1024).decode()

        # check if 250 is back, if not display message
        # print(recv3)
        # if recv3[:3] != '250':
        #    print('250 reply not received from server.')

        # Fill in end

        # Send DATA command and handle server response.

        # Fill in start

        #inform server that the the following lines will be the message
        sendData = 'DATA\r\n'
        clientSocket.send(sendData.encode())
        recv4 = clientSocket.recv(1024).decode()

        # 354 indicates that server is ready to recieve message data
        # check if 354 is back, if not display message
        # print(recv4)
        # if recv4[:3] != '354':
        #    print('354 reply not received from server.')

        # Fill in end

        # Send message data.
        # Fill in start

        clientSocket.send('Subject: SMTP Client\r\n'.encode())
        clientSocket.send('From: al8211@nyu.edu\r\n'.encode())
        clientSocket.send('To: aishalallics@gmail.com\r\n'.encode())
        clientSocket.send('Life is good! \r\n'.encode())
        clientSocket.send('Please check your spam/junk folder for this email here.\r\n'.encode())
        # Fill in end

        # Message ends with a single period, send message end and handle server response.
        # Fill in start

        #send end of message indicator to SMTP server and recieve a response
        # endmsg was declared in top as "r\n.\r\n"
        clientSocket.send(endmsg.encode())
        recv5 = clientSocket.recv(1024).decode()

        #response code is 250 again
        # check if 250 is back, if not display message
        # print(recv5)
        # if recv5[:3] != '250':
        #    print('250 reply not received from server.')

        # Fill in end

        # Send QUIT command and handle server response.
        # Fill in start

        #the QUIT command is used to terminate the SMTP session and close the connection with the server
        sendQuit = 'QUIT\r\n'
        clientSocket.send(sendQuit.encode())
        recv6 = clientSocket.recv(1024).decode()

        # for quiting code 221 indicates that session is closed
        # print(recv6)
        # if recv6[:3] != '221':
        #    print('221 reply not received from server.')
        # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')