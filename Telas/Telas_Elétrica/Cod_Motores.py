

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
           
while True:
    
        p = str(input('INFORME A POTÊNCIA DO MOTOR: '))
        if p.isalpha() == False:
            break
            
        else:
            print('Informe um valor válido')
            p = str(input('INFORME A POTÊNCIA DO MOTOR: '))
            if p.isalpha() == False:
                break
while True:
         
    v = str(input('INFORME A TENSÃO DO MOTOR:  '))
    if v.isalpha() == False:
        break
            
    else:
        print('Informe um valor válido')
        v = str(input('INFORME A TENSÃO DO MOTOR:  '))
        if v.isalpha() == False:
            break
        
while True:
    
    i = str(input('INFORME A CORRENTE DO MOTOR: '))
    if i.isalpha() == False:
        break
        
    else:
        print('Informe um valor válido')
        i = str(input('INFORME A CORRENTE DO MOTOR: '))
        if i.isalpha() == False:
            break
        
    
if mot == 'T':
    if p == '':
        i = float(i)   
        v = int(v)
        pw = i * v * 1.732050808 * 0.85 * 0.85
        pcv = pw / 736
        if uni == 'CV':
            
            print(f'A potência do MIT é de {pcv:.2f} CV')
            
        if uni == 'KW' or uni == 'W':
            
            print(f'A potência do MIT é de {pw / 1000:.2f} Kw')
    elif v == '':
        i = float(i)
        p = float(p)
        if uni == 'CV':
            pw = p * 736
            vc = pw / (i * 1.732050808 * 0.85 * 0.85)
            print(f'A tensão do MIT é {vc:.0f} Volts')
        elif uni == 'KW':
            pw = p * 1000
            vc = pw / (i * 1.732050808 * 0.85 * 0.85)
            print(f'A tensão do MIT é {vc:.0f} Volts')
        elif  uni == 'W':
            pw = p
            vc = pw / (i * 1.732050808 * 0.85 * 0.85)
            print(f'A tensão do MIT é {vc:.0f} Volts')
    elif i == '':
        v = int(v)
        p = float(p)
        if uni == 'CV':
            pw = p * 736
            i = pw / (v * 1.732050808 * 0.85 * 0.85 )
            print(f'A corrente do MIT é {i:.2f} Amperes')
        elif uni == 'KW':
            pw = p * 1000
            i = pw / (v * 1.732050808 * 0.85 * 0.85 )
            print(f'A corrente do MIT é {i:.2f} Amperes')
        elif uni == 'W':
            pw = p 
            i = pw / (v * 1.732050808 * 0.85 * 0.85 )
            print(f'A corrente do MIT é {i:.2f} Amperes')
                
if mot == 'M':
    if p == '':
        i = float(i)   
        v = int(v)
        pw = i * v * 0.85 * 0.85
        pcv = pw / 736
        if uni == 'CV':
            
            print(f'A potência do MIM é de {pcv:.2f} CV')
            
        if uni == 'KW' or uni == 'W':
            
            print(f'A potência do MIM é de {pw / 1000:.2f} Kw')
    elif v == '':
        i = float(i)
        p = float(p)
        if uni == 'CV':
            pw = p * 736
            vc = pw / (i * 0.85 * 0.85)
            print(f'A tensão do MIM é {vc:.0f} Volts')
        elif uni == 'KW':
            pw = p * 1000
            vc = pw / (i * 0.85 * 0.85)
            print(f'A tensão do MIM é {vc:.0f} Volts')
        elif  uni == 'W':
            pw = p
            vc = pw / (i * 0.85 * 0.85)
            print(f'A tensão do MIM é {vc:.0f} Volts')
    elif i == '':
        v = int(v)
        p = float(p)
        if uni == 'CV':
            pw = p * 736
            i = pw / (v * 0.85 * 0.85 )
            print(f'A corrente do MIM é {i:.2f} Amperes')
        elif uni == 'KW':
            pw = p * 1000
            i = pw / (v * 0.85 * 0.85 )
            print(f'A corrente do MIM é {i:.2f} Amperes')
        elif uni == 'W':
            pw = p 
            i = pw / (v * 0.85 * 0.85 )
            print(f'A corrente do MIM é {i:.2f} Amperes')




