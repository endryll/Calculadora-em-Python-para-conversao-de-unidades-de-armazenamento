def menu():
    print('''
        MENU:

        [a] - Cadastrar novo voto
        [b] - Ver Resultado
        [c] - Sair
    ''')
    str(input('Escolha uma opção: '))

bitParaByte = "a"

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def byteparakilobyte(valorASerConvertido):
    print('Valor convertido de byte para kilobyte')
    kilobytecalculado = valorASerConvertido / 1024
    return kilobytecalculado

def kilobyteparabyte(valorASerConvertido):
    print('Valor convertido de kilobyte para byte')
    bytescalculado = valorASerConvertido * 1024
    return bytescalculado

def kilobyteparamegabyte(valorASerConvertido):
    print('Valor convertido de kilobyte para megabyte')
    kilobytecalculado = valorASerConvertido / 1024
    return kilobytecalculado

def megabeteparakilobyte(valorASerConvertido):
    print('Valor convertido de megabyte para kilobyte')
    bytescalculado = valorASerConvertido * 1024
    return bytescalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = megabeteparakilobyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)