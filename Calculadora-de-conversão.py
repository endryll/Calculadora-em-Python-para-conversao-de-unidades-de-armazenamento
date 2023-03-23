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
    megabytescalculado = valorASerConvertido / 1024
    return megabytescalculado

def megabeteparakilobyte(valorASerConvertido):
    print('Valor convertido de megabyte para kilobyte')
    kilobytescalculado = valorASerConvertido * 1024
    return kilobytescalculado

def megabyteparagigabyte(valorASerConvertido):
    print('Valor convertido de megabyte para gigabyte')
    gigabytecalculado = valorASerConvertido / 1024
    return gigabytecalculado

def gigabyteparamegabyte(valorASerConvertido):
    print('Valor convertido de gigabyte para megabyte')
    megabytescalculado = valorASerConvertido * 1024
    return megabytescalculado

def gigabyteParaTerabyte(valorASerConvertido):
    print('Valor convertido de gigabyte para terabyte')
    terabytesCalculado = valorASerConvertido / 1024
    return terabytesCalculado

def terabyteParagigabyte(valorASerConvertido):
    print('Valor convertido de terabyte para gigabyte')
    gigabytesCalculado = valorASerConvertido * 1024
    return gigabytesCalculado

def terabyteParaPetabyte(valorASerConvertido):
    print('Valor convertido de terabyte para petabyte')
    petabytesCalculado = valorASerConvertido / 1024
    return petabytesCalculado

def petabyteParaTerabyte(valorASerConvertido):
    print('Valor convertido de petabyte para terabyte')
    terabytesCalculado = valorASerConvertido * 1024
    return terabytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = terabyteParagigabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)