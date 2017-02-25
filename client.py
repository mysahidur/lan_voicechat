import socket
import pyaudio
import wave

#record
CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 20000
#RECORD_SECONDS = 4000

#HOST = '127.0.0.1'
HOST = '192.168.1.198'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


#connection setup done and connected to server


p = pyaudio.PyAudio()


# for sending data
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


# for receiving data
stream2 = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)



print("*recording")

data2='a'

i=0
while data2 != '':

 try:		# sending data
     data  = stream.read(CHUNK)
     s.sendall(data)
 except KeyboardInterrupt:
     break
 except:
     pass

 try:       	# receiving data
     data2 = s.recv(1024)
     stream2.write(data2)
     print i
     i=i+1
 except KeyboardInterrupt:
     break
 except:
     pass

print("*done recording")





stream.stop_stream()
stream.close()
p.terminate()
s.close()

print("*closed")
