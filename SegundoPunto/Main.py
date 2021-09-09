import hashlib
import winsound
import threading
from Stop import StoppableThread

password = "a911c42c9b290bfe6a28f153165d7a82641486a5"
alp = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"


def detenerHilos(hilos):
    for hilo in hilos:
        stop = StoppableThread(hilo)
        stop.stop()


def decifrar(linm1, hilos):
    print("Corriendo hilo:" , linm1)
    for w1 in range(linm1, len(alp)):
        for w2 in range(linm1, len(alp)):
            for w3 in range(linm1, len(alp)):
                cadena = alp[w1] + alp[w2] + alp[w3]
                if cadena.isupper():
                    del cadena
                    break
                for w4 in range(linm1, len(alp)):
                    cadena = alp[w1] + alp[w2] + alp[w3] + alp[w4]
                    if cadena.isupper():
                        del cadena
                        break
                    for w5 in range(linm1, len(alp)):
                        cadena = alp[w1] + alp[w2] + alp[w3] + alp[w4] + alp[w5]
                        if cadena.isupper():
                            del cadena
                            break
                        for w6 in range(linm1, len(alp)):
                            cadena = alp[w1] + alp[w2] + alp[w3] + alp[w4] + alp[w5] + alp[w6]
                            if cadena.isupper():
                                del cadena
                                break

                            for w7 in range(linm1, len(alp)):

                                cadena = alp[w1] + alp[w2] + alp[w3] + alp[w4] + alp[w5] + alp[w6] + alp[w7]

                                if cadena.isupper():
                                    del cadena
                                    break
                                temp = cadena.encode("utf-8")
                                res = hashlib.sha1(temp).hexdigest()

                                if res == password:
                                    print("SE HA ENCONTRADO LA CADENA Y ES: ", cadena)
                                    frequency = 1000
                                    duration = 100
                                    winsound.Beep(frequency, duration)
                                    detenerHilos(hilos)


hilos = []

for i in range(len(alp)):

    hilo = threading.Thread(target=decifrar, args=(i, hilos,))
    hilos.append(hilo)

for hilo in hilos:
    hilo.start()
