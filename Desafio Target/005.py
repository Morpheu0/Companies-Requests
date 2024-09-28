#Exemplo no código

idas = 0

Lampadas = {"Lâmpada.E":"Desligada","Lâmpada.M":"Desligada","Lâmpada.D":"Desligada"}

def ligar(l):
    match l:
        case 1:
            if Lampadas["Lâmpada.M"] == "Desligada":
                Lampadas["Lâmpada.M"] = "Ligada"
            else:
                print("A lâmpada já está ligada!")
        case 2:
            if Lampadas["Lâmpada.E"] == "Desligada":
                Lampadas["Lâmpada.E"] = "Ligada"
            else:
                print("A lâmpada já está ligada!")
        case 3:
            if Lampadas["Lâmpada.D"] == "Desligada":
                Lampadas["Lâmpada.D"] = "Ligada"
            else:
                print("A lâmpada já está ligada!")

def desligar(d):
        match d:
            case 1:
                if Lampadas["Lâmpada.M"] == "Ligada":
                    Lampadas["Lâmpada.M"] = "Desligada"
                else:
                    print("A lâmpada já está delisgada!")
            case 2:
                if Lampadas["Lâmpada.E"] == "Ligada":
                    Lampadas["Lâmpada.E"] = "Desligada"
                else:
                    print("A lâmpada já está delisgada!")
            case 3:
                if Lampadas["Lâmpada.D"] == "Ligada":
                    Lampadas["Lâmpada.D"] = "Desligada"
                else:
                    print("A lâmpada já está delisgada!")

while idas <=2:
    while True:
        user = int(input("Escolha um dos 3 interrruptores para ligar: 1[*] 2[*] 3[*]\n"))
        if user < 4:
            match user:
                case 1:
                    ligar(1)
                case 2:
                    ligar(2)
                case 3:
                    ligar(3)
        else:
            print("Escolha um interruptor!")
            continue
        user = int(input("Deseja verificar a sala de lâmpadas??: 1[Sim] 2[Não]\n"))
        if user == 1:
            idas += 1
            print(Lampadas.items())
        elif user == 2:
            while True:
                user = int(input("Deseja desligar algum interruptor? 1[Sim] 2[Não]\n"))
                if user == 1:
                        user = int(input("Qual interruptor deseja desligar??: 1[*] 2[*] 3[*]\n"))
                        match user:
                            case 1:
                                desligar(1)
                            case 2:
                                desligar(2)
                            case 3:
                                desligar(3)
                elif user == 2:
                    break
                else:
                    print("Escolha uma opção certa")
        if idas > 2:
            break
print("Game Over!")