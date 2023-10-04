import board
import busio
from adafruit_pn532.i2c import PN532_I2C


class Lector_NFC():
    # Configura la interfaz I2C : protocol pel qual s'enven dades el lector NFC i la RPi
    i2c = busio.I2C(board.SCL, board.SDA) #metode donat per la llibreria adafruit_pn534.i2c. Definim els pins GPIO SLC (pin 5) i SDA (pin 3) 
# Crea una instancia del objeto PN532 : li anomenem on està connectat el lector i que es comunica amb i2c
    pn532 = PN532_I2C(i2c, address=0x24)  #aqui hem d'escriure l'adreça del lector. Per trobarlo hem de fer: sudo i2cdetect -y 1
# Inicializa el PN532
    pn532.SAM_configuration() #metode de configuració del lector
    uid_str = ""  #la sortida comença buida

    def llegir(self):
        print("Esperant una tarjeta NFC...")
        while(True):
            uid = PN532_I2C.read_passive_target(timeout=20)
            for i in uid:
                print(i)
        

if __name__ == "__main__":
    l1 = Lector_NFC()
    l1.llegir()