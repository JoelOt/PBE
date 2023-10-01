import board
import busio
from adafruit_pn532.i2c import PN532_I2C

# Configura la interfaz I2C : protocol pel qual s'enven dades el lector NFC i la RPi
i2c = busio.I2C(board.SCL, board.SDA) #metode donat per la llibreria adafruit_pn534.i2c. Definim els pins GPIO SLC (pin 5) i SDA (pin 3) 


# Crea una instancia del objeto PN532 : li anomenem on està connectat el lector i que es comunica amb i2c
pn532 = PN532_I2C(i2c, address=0x24)  #aqui hem d'escriure l'adreça del lector. Per trobarlo hem de fer: sudo i2cdetect -y 1

# Inicializa el PN532
pn532.SAM_configuration() #metode de configuració del lector
uid_str = ""  #la sortida comença buida
rebut = 0  #creem aquesta variable per tal de finalitzar el programa un cop llegida una targeta 
print("Esperando una tarjeta NFC...")

while rebut == 0: 
    try:
        # Intenta detectar una tarjeta NFC
        uid = pn532.read_passive_target() #es un array de 4 HEX. Mètode amb el qual se li dona la ordre al sensor de llegir una targeta
        
        if uid:  #en cas que la llegeixi
            for i in uid:  #hem de transformar el array de HEX a numeros en decimal. per això ho fem un a un
                num = int(hex(i), base=16)
                uid_str = uid_str + str(num)
                
            print(uid_str)
            rebut = 1  #indiquem que hem rebut una targeta per finalitzar el programa

    except KeyboardInterrupt:  #una excepció per si hi ha algun problema, indicar-ho
        print("\nPrograma interrumpido.")
        break
