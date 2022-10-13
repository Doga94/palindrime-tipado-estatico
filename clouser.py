#Se va a crear un prgrama para que repita n veces un estring que indiquemos
from timeit import repeat


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo se puede utilizar cadenas"
        return string * n
    return repeater

def run():
    #Acá aignamos el numero que va a repetirse y el string que va a repetir
    repeat_5 = make_repeater_of(5)
    print(repeat_5("David"))
    repeat_user = make_repeater_of(int(input("Ingrese un numero: ")))
    print(repeat_user(input("Ingrese la frase a repetir: ")))


if __name__ == "__main__":
    run()
