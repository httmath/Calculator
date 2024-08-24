# Test perdi as contas depois de 1 mes AAAAH
n1 = float(input('Digite o primeiro valor: '))
operador = input('Digite o operador: ')
n2 = float(input('Digite o segundo valor: '))


def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Erro: Divisão por zero não é permitida!"

def porcentagem(n1, n2):
    return n1 * n2 / 100

def Quadrada(n1, n2):
    return n1 ** n2
    
def calculadora(n1, n2, operador):
    match operador:
        case '+': return somar(n1, n2)
        case '-': return subtrair(n1, n2)
        case '*': return multiplicar(n1, n2)
        case '/': return dividir(n1, n2)
        case '%': return porcentagem(n1, n2)
        case 'Raiz Quadrada': return Quadrada(n1)
        case _: return 'Operador inválido!'  #POde usar um _ no lugar de others

resultado = calculadora(n1, n2, operador)
print(f'O resultado é: {resultado}')