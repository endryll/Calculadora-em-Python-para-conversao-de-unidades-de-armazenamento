from Calculadoradeconversão import converterStringParaFloat,bitParaByte, byteParaBit, byteparakilobyte, kilobyteparabyte, kilobyteparamegabyte, megabeteparakilobyte, megabyteparagigabyte, gigabyteparamegabyte, terabyteParagigabyte, gigabyteParaTerabyte, terabyteParaPetabyte, petabyteParaTerabyte

print(' -Escrever 1 Byte para Bit \n -Escrever 2 Bit para Byte \n -Escrever 3 Byte para Kilobyte \n -Escrever 4 Kilobyte para Byte \n -Escrever 5 Kilobyte para Megabyte \n -Escrever 6 Megabyte para Kilobyte \n -Escrever 7 Megabyte para Gigabyte \n Escrever 8 Gigabyte para Megabyte')
funcEscolha = input()
if(funcEscolha == '1'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha == '3'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteparakilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha == '4'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = kilobyteparabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha == '5'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = kilobyteparamegabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

if(funcEscolha == '6'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = megabeteparakilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)