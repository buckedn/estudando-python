
def menu():

    def cadastro():
        import json
        import os
        arquivar = open ('aquivos1.json', 'a')

        print('==============area para cadastro de info produtos================== ')

        produtos = []
    
        while True:
            pdt = input('descriçao do produto: ')
            pc = float(input('preço do produto:  '))
            qtd = int(input('quantidade do produto: '))
            tt = pc * qtd
        
            produto = {
            'produto': pdt,
            'preco': pc,
            'quantidade': qtd,
            'total': tt
            }
            
            produtos.append(produto)


            proceguir = input('deseja CADASTRAS OUTRO PRODUTO S OU N para editar digite 1 : ')
            if proceguir == 'S':
                continue

            elif proceguir == 'n':
                print('=============list=========')
                print(f'inte na lista {produtos}')
                pdt_qtd = len(produtos)
                print('quantidade de produtos cadastrados> ', pdt_qtd)
                break
            elif proceguir == '1':
                print('===========================')

       
        produto = json.load(arquivar)
        
        
     
        json.dump(produtos, arquivar)
        arquivar.close()
#fim do cadastro

    def editar():
        print('----------editar produtos------------')
                    

    
    #fim do editar
    def lista():
        print ('===========listas de produtos===========')
    #fim da lista 

    def login():
           print('===========login=========')
           tentativas = []
   
   
           while True:
               login = input('digite seu login: ')
               senha = input('digite sua senha: ')
               
               if  login == '1' and senha =='1':
                   print('acesso autorizado')
                   break
               elif login == '' and senha == '':
                   print('acesso negado')
   
               tentativas.append(senha == login)
           ff = len(tentativas)
           print(f'tentavivas {ff}')
           while True:
               print ('======opçoe========= ')
               ir = int(input( ' para ir cadastar produtos digite 1, para editar digite 2 e para ir para as listas 3: '))
               if ir == 1:
                   print('cadastra produtos')
                   print('aguade...')
                   print('=================================================')
                   cadastro()
                   
               elif ir == 2:
                   print (' editar produtos')
                   print('==================')
                   editar()
                   
               elif ir == 3:
                   print ('listas de produtos')
                   print('===================')
                   lista()
                   
               else:
                   print('opçao invalida tente novamente')
    login()

menu()
