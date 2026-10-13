def aua():
    cadrasto = []

    nome = input('ola qual e seu nome: ')
    cadrasto.append(nome)
    print(f'ola {nome}, seja bem vindo')
    print('temos os seguintes servicos disponiveis 1 cachorro 2 gato e 3 coelho ')
    escolhar_de_servico = input('qual servico voce deseja: ')
    while escolhar_de_servico == '1' or escolhar_de_servico == '2' or escolhar_de_servico == '3':
        
        if escolhar_de_servico == '1':
            print(f'sua {escolhar_de_servico} voce escolheu o servico de cachorro')
            cadrasto.append('cachorro')
            print('obrigado por utilizar nossos servicos 1 continuar 2 parar')
            nao = input('')
            if nao == '2':
                print('para')
                break
            elif nao == '1':
                print('continuar')
                escolhar_de_servico = input('qual servico voce deseja: ')
            aua()
            
        elif escolhar_de_servico == '2':
            print(f'sua {escolhar_de_servico} voce escolheu o servico de gato')
            cadrasto.append('gato')
            print('obrigado por utilizar nossos servicos 1 continuar 2 parar')
            nao = input('')
            if nao == '2':
                print('para')
                print(cadrasto)
                break
            elif nao == '1':
                print('continuar')
                escolhar_de_servico = input('qual servico voce deseja: ')
                print(cadrasto) 
                continue 
            aua()
        elif escolhar_de_servico == '3' :
            print(f'sua {escolhar_de_servico} voce escolheu o servico de coelho')
            cadrasto.append('coelho')
            print('obrigado por utilizar nossos servicos 1 continuar 2 parar')
            nao = input('')
            if nao == '2':
                print('para')
                print(cadrasto)
                break
            elif nao == '1':
                print('continuar')
                escolhar_de_servico = input('qual servico voce deseja: ')
                print(cadrasto)
                continue
            aua()

        else:
            print('servico invalido')
        print('obrigado por utilizar nossos servicos')
        escolhar_de_servico = input('qual servico voce deseja: ')
    print('obrigado por utilizar nossos servicos')
    continue_ = input('deseja continuar 1 sim 2 nao: ')
    if continue_ == '1' == escolhar_de_servico :
        print('continuar')
    elif continue_ == '2':
        print('obrigado por utilizar nossos servicos')
        print(cadrasto)
    print('obrigado por utilizar nossos servicos')
    print(cadrasto)
aua()



