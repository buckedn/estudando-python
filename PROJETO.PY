import os
import json 
import tkinter as t
os.system('cls')


items = []

with open('arquivos.json', 'r') as j:
    items =  json.load(j)

def menu():
    def cadrato():
        while True:
            
            pd = input('adicionar produto: ')
            vlr = float(input('valor do produto: '))
            qtd = int(input('quantidade de produtos: '))
            tt = vlr*qtd
            lts = {
                'PRODUTOS': pd,
                'VALOR': vlr,
                'QUANTIDADE': qtd,
                'total': tt,
                'numero': len(items)+1,
                }
            items.append(lts)
            
            des = input('deseja continuar: s ou n ').lower()
            
            if des == 's':
                continue
            elif des  == 'n':
                break

        with open('arquivos.json', 'w') as arquivos:
            json.dump(items, arquivos, indent= 4,)


    #########cadastro fim
    def edit():
        with open('arquivos.json', 'r') as i :
            json.load(i)
        print(f'items {items}')

    edit()
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
            ir = int(input( ' para ir cadastar produtos digite 1, para editar digite 2 : '))
            if ir == 1:
                print('cadastra produtos')
                print('aguade...')
                print('=================================================')
                cadrato()
                
            elif ir == 2:
                print (' editar produtos')
                print('==================')
                edit()
                
            else:
                print('opçao invalida tente novamente')
menu()