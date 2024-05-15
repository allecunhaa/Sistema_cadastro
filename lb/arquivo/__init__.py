from lb.cadastro import *

#para verificar se o arquivo existe, usamos o tratamento de erro

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # abrir o arquivo em formato de texto (r,t - read text)
        a.close()
    except FileNotFoundError:
       return False
    else:
      return True
  
#criar um novo 
def criarArquivo(nome): 
    try:
        a= open(nome, 'wt+') # aqui criamos o arquivo. o wt9write text + signifuca que se o arquivo nao existir ele vai criar um novo
        a.close() #para fechar
    except:
        print('Houve um Erro na criação do arquivo')  
    else:
        print(f' Arquio {nome} criado com sucesso!')      

def lerArquivo(nome):
    try:
        a= open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho(' \033[32mPESSOAS CADASTRADAS \033[m')
        for linha in a:
            dado = linha.split(';')
            for item in dado:
                print(item, end=' ')
    finally:
        a.close()    
        
def cadastrar(arq, nome, idade,email):
    try:
        a = open(arq,'at') # aqui vamos add o arquivo - at(append text)
    except:
        print('Erro na abertura do arquivo')    
    else:
        a.write(f'{nome}; {idade};{email} \n') # para cadastrar os dados 
        print('Cadastro Realizado com Sucesso!')
        a.close()
        

      
        
     
           
        
                
                