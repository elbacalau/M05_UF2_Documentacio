class ProgramaOperacions:
    '''
    Aquesta clase te uns metodes que realitzen algunes operacions 
    basiques.
    '''


    def multiplicacio(n):
        '''
        Aquest mètode calcula la taula de multiplicar d'un número 'n'
        des de 1 fins a 10

        Retorna el resultat de la multiplicació
        '''
        for i in range(1, 11):
            resultado = n * i
            print(f"{n} * {i} = {resultado}")

    multiplicacio(5)
    help(multiplicacio)

    def divisio_residu(a, b):
        '''
        Aquest metode realitza una divisió de 2 parametres 'a' i 'b'
        També calcula el residu dels paràmetres

        El programa retorna la divisió dels 2 enters y el residu en una tupla
        '''
        div = a // b
        residu = a % b
        return div, residu

    result = divisio_residu(20, 3)
    print(f"El resultat de la divisió es: {result[0]}, i el residu es {result[1]}.")
    help(divisio_residu)


help(ProgramaOperacions)