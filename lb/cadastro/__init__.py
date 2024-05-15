



def leiaInt(msg):
    while True:
        try:
            n= int(input(msg))
        except (ValueError,TypeError):
            print('Erro!Digite um numero inteiro')
            continue #joga direto para o while
        except(KeyboardInterrupt):
            print('Erro! Programa parado pelo usuario')
            return 0
        else:
            return n
       
  
def linha(tam = 42):
  return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt .center(42))
    print(linha())

def menu(lista):
    cabecalho('\033[32m MENU PRINCEIPAL\33[m')
    c=1
    for item in lista:
        print(f' {c} - {item}')
        c+= 1
    print(linha())
    opc = leiaInt('  Sua opção:  ')
    return opc

    

        
