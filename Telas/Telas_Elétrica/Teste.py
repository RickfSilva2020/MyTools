
while True:
    
        p = str(input('INFORME A POTÊNCIA DO MOTOR: '))
        if p.isalpha() == False:
            break
            
        else:
            print('Informe um valor válido')
            p = str(input('INFORME A POTÊNCIA DO MOTOR: '))
            if p.isalpha() == False:
                break
       