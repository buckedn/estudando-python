def sos():
    
    print('================================                                                             ')
    print(' -----------BEM VINDO-----------')
    print('================================                                                              ')
    def cadastra_prod():
          arquivos = open('infos.txt', 'r+')
          print('==============================================================')
          produtos = []
          valor = []
          quantidade = []
           
          while True:
                for i in range(3):
                    print('deve ser adicionado no minimo 3 items')
                    arm = input('qual produto voce quer adicionar: ')
                    vlr = int(input('qual o valor do produto: '))
                    qtd = int(input('qual a quantidade de produtos: '))
                    print('==============================================')

                    produtos.append(arm)
                    valor.append(vlr)
                    quantidade.append(qtd)
                    print(produtos)
                    arquivos.write(f'{arm} - R${vlr} - quantidade: {qtd}\n')
                    tudo = [
                         produtos,

                         valor,

                         quantidade,
                    ]
                    print('=============================')
                    print('items', tudo)
                    print('-----------------------------')
                    dsj = input('deseja continuar s/n: ')
                    if dsj == 's':
                         print('===============================')
                         print('continuar a adicionar produtos')
                         print(tudo)
                         continue
                    elif dsj == 'n':
                         print('=====================')
                         print('retornado')
                         print(tudo)
                         break
                    else:
                         print('incorreto')
          arquivos.close()
    def lis():
         print('------------')
         print('------------')
         arquivos = open('infos.txt', 'r+')
         print(arquivos.read())
         arquivos.close()
        
    def login():
        print('para da continuidade acesse qual sua conta')

        while True:

            login = input('login: ')
            senha = input('senha: ')
            casd = (login == '12' and senha == '12')
            liss = (login == '1' and senha == '1' )

            if casd:
                print('======================================')
                print('acesso liberado para cadastra produtos')
                print('aguarde...')
                print('======================================')
                cadastra_prod()
                break

            elif liss:
                 print('======================================')
                 print('acesso liberado para cadastra produtos')
                 print('aguarde...')
                 print('=====================================')
                 lis()
                 break
            else:
                print('senha ou login incorreto tente novamente')
    login()

 
sos()