import time

tempo = time.localtime()
hora = tempo.tm_hour

ms = 'Olá! Aqui é o bot de teste do Samuel. Ele não está disponível no momento. Aguarde um pouco.'

if hora <= 11:
    print('Bom dia!!')
elif hora <= 16:
    print('Boa tarde!!')
else:
    print('Boa noite!!')

print(ms)

meu_id = '-Samuel-'

tempo_inicial = time.time()

while time.time() - tempo_inicial < 60:

    remetente = ''

    if remetente == meu_id:
        break

    time.sleep(1)