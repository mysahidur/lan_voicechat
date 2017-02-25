# Echo server program
import socket
import pyaudio
import wave
import time

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 20000
RECORD_SECONDS = 4000


#HOST = '127.0.0.1'
HOST = '192.168.1.196'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr


#connection setup done and client connected.



p = pyaudio.PyAudio()

# for receiving data
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

# for sending data
stream2 = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


data='a'
i=0
while data != '':
    try:			# receiving data
        data = conn.recv(1024)
        stream.write(data)
        print i
        i=i+1
    except KeyboardInterrupt:
     	break
    except:
        pass

    try:		# sending data
        data2  = stream2.read(CHUNK)
        conn.sendall(data2)
    except KeyboardInterrupt:
     	break
    except:
        pass




stream.stop_stream()
stream.close()
p.terminate()
conn.close()
