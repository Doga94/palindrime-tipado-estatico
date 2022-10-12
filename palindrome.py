#Función con el nombre de palindrome
    #Se creo una función que debe recibir un string y devuelve si es true o false
def is_palindrome(string: str) -> bool:
    #Para saber si es palindromo se debe eliminar los espacios que se ingresen y pasarlo a minusculas para no tener problemas 
    #Con la verificación
    string = string.replace(" ", "").lower()
    #Vamos a retornar la letra o frase ingresada al reves para validar si es palindromo
    return string == string[::-1]

def run():
    print(is_palindrome("AnA"))


if __name__ == '__main__':
    run()