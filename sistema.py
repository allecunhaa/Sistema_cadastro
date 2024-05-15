
from lb.cadastro import * # para importar uma biblioteca inteira
from lb.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq) 

  
while True:
    resposta = menu(['ACESSAR CADASTRO', 'CADASTRAR ' , 'SAIR DO SISTEMA'])
    if resposta == 1:
    #opcao de listar o conteudo do arquivo
        lerArquivo(arq)
     
    elif resposta == 2:
    # cadastrar pessoas
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')  # Não é necessário converter para string com str()
        idade = leiaInt('Idade: ') # Utilize a função int() para garantir que a entrada seja interpretada como um número
        email = input('Email: ')
        cadastrar(arq, nome, idade,email)  # Passando os parâmetros do arquivo que desejo cadastrar

    elif resposta == 3:
        cabecalho('Saindo do sistema....Até logo') 
        break
    else:
        print(' Erro!Digite uma opção inválida')         
        
