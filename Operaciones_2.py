memoria=[]

def suma(n):
    total=0
    for i in range(n):
        nro=int(input("Ingrese nro.,i+1"))
        total+=nro
        
    return total

def resta(n1,n2):
    return

while True:
    print("----- Menu_Calculadora -----")
    print("1. Sumar")
    print("2. Resta")
    print("5. Sumar")
    
    op=input("Digite la opcion del menu:")
    
    match op:
        case '1': 
            suma(int(input("Ingrese cantidad de nros. a sumar:")))
            memoria.append(res)
            kj
        case'2':
            print()
        case '5':
            print("Usted ha salido del sistema!!!!")   
            break
        case _:
            print("Opcion no valida")