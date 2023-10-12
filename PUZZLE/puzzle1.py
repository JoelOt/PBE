import board
import busio
from adafruit_pn532.i2c import PN532_I2C

class Lector_NFC():
    def __init__(self): #constructor de la classe
        # Configura la interfaz I2C : protocol pel qual s'enven dades el lector NFC i la RPi
        self.i2c = busio.I2C(board.SCL, board.SDA) #metode donat per la llibreria adafruit_pn534.i2c. Definim els pins GPIO SLC (pin 5) i SDA (pin 3) 
        
        # Crea una instancia del objeto PN532 : li anomenem on està connectat el lector i que es comunica amb i2c
        self.pn532 = PN532_I2C(self.i2c, address=0x24)  #aqui hem d'escriure l'adreça del lector. Per trobarlo hem de fer: sudo i2cdetect -y 1
        
        # Inicializa el PN532
        self.pn532.SAM_configuration() #metode de configuració del lector
        self.uid_str = ""  #la sortida comença buida
        self.rebut = 0
        
    def llegir(self):
        print("Esperant una tarjeta NFC...")
        while True:
            try:
                # Intenta detectar una tarjeta NFC
                uid = self.pn532.read_passive_target() #es un array de 4 HEX. Mètode amb el qual se li dona la ordre al sensor de llegir una targeta
        
                if uid:  #en cas que la llegeixi
                    for i in uid:  #hem de transformar el array de HEX a numeros en decimal. per això ho fem un a un
                        self.uid_str = self.uid_str + str(i)
                    #print(self.uid_str)
                    return self.uid_str
                    
            except KeyboardInterrupt:  #una excepció per si hi ha algun problema, indicar-ho
                print("\nPrograma interrumpido.")
                break

if __name__ == '__main__': 
    l1 = Lector_NFC()
    l1.llegir()
    
