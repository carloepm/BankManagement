import pickle
import os
import pathlib

class Account:
    accNo = 0
    name = ''
    deposit= 0
    type = ''
    
 #CREACION DE CUENTA   
    
    def createAccount(self):
        self.accNo = int(input("Ingresa numero de cuenta: "))
        self.name = input("Ingresa nombre de la cuenta: ")
        self.type = input("Ingresa tipo de cuenta C/S: ")
        self.deposit = int(input("Ingresa el monto inicial: "))
        print("\n\n\nCuenta creada")

#MOSTRAR LOS DATOS DE LA CUENTA

    def showAccount(self):
        print("Numero de cuenta: ", self.accNo)
        print("Nombre de la cuenta: ", self.name)
        print("Tipo de cuenta: ", self.type)
        print("Balance: ", self.deposit)
    
#MODIFICAR DATOS DE LA CUENTA
    
    def modifyAccount(self):
        print("Numero de cuenta: ", self.accNo)
        self.name = input("Modificar nombre de la cuenta: ")
        self.type = input("Modificar tipo de cuenta: ")
        self.deposit = int(input("Modificar balance: "))

#SUMA DEPOSITO

    def depositAmount(self,amount):
        self.deposit += amount

#RESTA EXTRACCION

    def withdrawAmount(self, amount):
        self.deposit -= amount
 
#REPORTE DE LA CUENTA
    
    def report(self):
        print(self.accNo, " ", self.name, " ",self.type," ",self.deposit)

#DATOS DE LA CUENTA ATRAVEZ DEL NUMERO DE CUENTA
    
    def getAccountNo(self):
        return self.AccNo
        def getAccountHolderName(self):
            return self.name
        def getAccountType(self):
            return self.type
        def getAccountBalance(self):
            return self.deposit

#PRIMERA VISUAL

def intro():
        print("\t\t\t\t**********************")
        print("\t\t\t\tSISTEMA DE GESTION BANCARIA")
        print("\t\t\t\t**********************")
    
        input("Presiona ENTER para continuar.")

#CREACION DE CUENTA PART2
    
def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

#DATOS DE LA CUENTA

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist : 
            print(item.accNo," ",item.name," ",item.type," ",item.deposit)
        infile.close()
    else: 
        print("Sin registro que ejecutar")

#FUNCION DEPOSITO

def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.accNo == num:
                print("El balance de tu cuenta es: ", item.deposit)
                found = True
    else:
        print("No hay registros")
    if not found:
        print("No hay registros con este numero de cuenta")
  
#FUNCION EXTRACCION
  
def depositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.accNo == num1 :
                if num2 == 1:
                    amount = int(input("Ingresar el monto del deposito: "))
                    item.deposit += amount
                    print("Tu cuenta se ha actualizado")
                elif num2 == 2:
                    amount = int(input("Ingresa el monto de extraccion: "))
                    if amount <= item.deposit:
                        item.deposit -=amount
                    else:
                        print("No puedes realizar esta extraccion")
                

    else:
        print("No hay registros")
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
#FUNCION BORRAR/MODIFICAR CUENTA

def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')
        

def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist= pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.accNo == num:
                item.name = input("Ingresa el nombre de la cuenta: ")
                item.type = input("Ingresa el tipo de cuenta: ") 
                item.deposit = int(input("Ingresa el monto: "))
        
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')

#LISTA DE CUENTAS
        
def writeAccountsFile(account):
    file = pathlib.Path('accounts.data')
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


""""ARRANCA EL PROGRAMA"""""

ch=''
num=0
intro()

#LOOP DE OPCIONES 

while ch != 8:
    print("\tMENU PRINCIPAL")
    print("\t1. NUEVA CUENTA")
    print("\t2. DEPOSITAR")
    print("\t3. EXTRAER") 
    print("\t4. SALDO DISPONIBLE")
    print("\t5. LISTA DE CUENTAS")
    print("\t6. CERRAR CUENTA")
    print("\t7. MODIFICAR CUENTA")
    print("\t8. SALIR")
    print("\tSelecciona una opcion (1-8)")
    ch = input()                        
    
    
    if ch == '1':
        writeAccount()
    elif ch == '2':
        num = int(input("\tIngresa el numero de cuenta: "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tIngresa el numero de cuenta: "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tIngresa numero de cuenta: "))
        displaySp(num)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num = int(input("\Ingresa el numero de cuenta: "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tIngresa el numero de cuenta: "))
        modifyAccount(num)
    elif ch == '8':
        print("\t Gracias por usar el sistema de gestion bancaria")
    else: 
        print("Opcion invalida")
        
    ch = input("Ingresa tu opcion: ")