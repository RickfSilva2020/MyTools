import string
#Código para cálculos relacionados á motores

#Cálculo de corrente
'''
 Para calcular a corrente do motor será nacassário a coleta das seguintes 
 informações:
 
 Fórmula = Motor trifásico
 I = P (watts)/(V * 1.732050808 * cosFI * rend.)
 1Cv = 736 watts
rendimento médio dos motores 85
Coseno FI médio = 0.85 

Fórmula de motor monofásico

I = P (watts) / (V * cosFI * rend)

 
 Tensão em Volts
 Potência em CV ou Kw
 
'''
# INFORMAR O TIPO DE MOTOR. TRIFÁSICO OU MONOFÁSICO

#from curses.ascii import isalnum


while True:    
    
    mot = str(input('INFORME SE O MOTOR É TRIFÁSICO(T) OU MONO(M): ')).strip().upper()
    
    if mot == 'T' or mot == 'M':
        break
    else:
        print('ESCOLHA UMA OPÇÃO VÁLIDA')
        mot = str(input('INFORME SE O MOTOR É TRIFÁSICO(T) OU MONO(M): ')).strip().upper()
        if mot == 'T' or mot == 'M':
            break
while True:       
    uni = str(input('O MOTOR É EM CV, KW OU watts(W): ')).strip().upper()
    
    if uni == 'CV' or uni == 'KW' or uni == 'W':
        break
    else: 
        print('ESCOLHA UMA UNIDADE PARA O MOTOR')
        uni = str(input('O MOTOR É EM CV, KW OU watts: ')).strip().upper()
        if uni == 'CV' or uni == 'KW' or uni == 'W':
            break
  

a = list(string.ascii_letters)
           
while True:
    
    p = str(input('INFORME A POTÊNCIA DO MOTOR: '))
    
    if p in str(a):
        print('possui letras')
        #print('Informe apenas números')
        #p = str(input('INFORME A POTÊNCIA DO MOTOR: '))
    else:
        break
        
    
        
       
v = str(input('INFORME A TENSÃO DO MOTOR:  '))
i = str(input('INFORME A CORRENTE DO MOTOR: '))

if mot == 'T' and p == '':
    i = float(i)   
    v = int(v)
    pw = i * v * 1.732050808 * 0.85 * 0.85
    pcv = pw / 736
if uni == 'CV':
    
    print(f'A potência do motor é de {pcv:.2f} CV')
    
if uni == 'KW' or uni == 'W':
    
    print(f'A potência do motor é de {pw / 1000:.2f} Kw')


if mot == 'M' and p == '':
    i = float(i)   
    v = int(v)
    pw = i * v  * 0.85 * 0.85
    pcv = pw / 736


    
if mot == 'M' and p == '':
    i = float(i)   
    v = int(v)
    pw = i * v  * 0.85 * 0.85
    pcv = pw / 736

if uni == 'KW':
    
    print(f'A potência do motor é de {pw / 1000:.2f} Kw')




