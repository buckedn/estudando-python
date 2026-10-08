def ppdt():
   print('--')
   login = 1234
   senha = 1234
   id = (senha == 1234) and (login == 1234)
   login = int(input('login'))
   senha = int(input('senha'))
   while login and senha:
      id =  (senha == 1234) and (login == 1234)
      
      if id == False:
         print('senha ou login errado')
         
      elif id == True:
         print('acesso autorizado')
         break
ppdt()

def lista_pr():
   print('bem vindo a loja de produtos')
   produtos = []
   print(produtos)
   usr = []
   usuario = usr.append(input('qual seu nome: '))
   print(usuario)
   for i in range(5):
      usr.append(input('ola usuario: '))
      produtos.append(input('qual produto voce deseja: '))
      #produtos.list.sort(produtos)
      #lista = produtos.count
      fd = len(produtos)
      if fd == 5:
         print('voce atingiu o limite de produtos')
         break
      if fd < 5:
         print('voce ainda pode adicionar produtos')
      ola = input('deseja apaga lista 0 para continuar 1 sim 2 que remove 1 produto 3 nao : ')
      print(ola)
      if ola == '1':
         produtos.clear()
         print('lista apagada')
         return lista_pr()
      elif ola == '0':
         return lista_pr()
      elif ola == '3':
         print('lista mantida')
      elif ola == '2':
         jj = input('qual produto voce deseja remover: ')
         produtos.remove (jj)
         print('produto removido', jj)
      else:
         print('lista mantida')
      produtos.sort()
      print(produtos)


   print (usr, produtos, fd)
   

lista_pr()