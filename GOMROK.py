import mysql.connector
import os
from colorama import Fore, Back, Style

def menu():
    
    print(Fore.LIGHTBLUE_EX+"[1.Insert]",end='\t\t')
    print(Fore.LIGHTBLUE_EX+"[2.Select]",end='\t\t')
    print(Fore.LIGHTBLUE_EX+"[3.Update]",end='\t\t')
    print(Fore.LIGHTBLUE_EX+"[4.Delete]",end='\t\t')
    print(Fore.LIGHTBLUE_EX+"[5.Exit]",end='\n\n')
    choose=int(input("Select 1 to 5 :  "))
    return choose

def insert_information():
    os.system('cls')
    print(Fore.RED+"1.Insert Data For product",end="\n")
    print(Fore.RED+"2.Insert Data For Transport",end="\n")
    print(Fore.RED+"3.Insert Data For store",end="\n")
    print(Fore.RED+"4.Insert Data For customer",end="\n")


    choose=int(input("Enter Number : "))

    def insert_data_product():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gomrok',
                                                user='root',
                                                password='Bs5295025s')
            pid=int(input("Enter ProductID : "))
            pname=input("Enter ProductName : ")
            ptype=input("Enter ProductType : ")
            pyear=int(input("Enter ProductYear : "))
            insertion=(pid,pname,ptype,pyear)                                    
            cursor = connection.cursor()
            result=cursor.callproc( procname='insert_product', args=insertion)
            connection.commit()
            
            print("insert successfully!!")

            for result in cursor.stored_results():
                print(result.fetchall())
           

        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: "+error)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def insert_data_transport():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gomrok',
                                                user='root',
                                                password='Bs5295025s')
            vid=int(input("Enter VehicleID : "))
            vtype=input("Enter VehicleType : ")

            insertion=(vid,vtype)                                    
            cursor = connection.cursor()
            result=cursor.callproc( procname='insert_transport', args=insertion)
            connection.commit()
            
            print("insert successfully!!")

            for result in cursor.stored_results():
                print(result.fetchall())
           

        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: "+error)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def insert_data_store():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gomrok',
                                                user='root',
                                                password='Bs5295025s')
            sid=int(input("Enter StoreID : "))
            stype=input("Enter StoreType : ")
            scapacity=int(input("Enter Store Of Capacity : "))
            insertion=(sid,stype,scapacity)                                    
            cursor = connection.cursor()
            result=cursor.callproc( procname='insert_store', args=insertion)
            connection.commit()
            
            print("insert successfully!!")

            for result in cursor.stored_results():
                print(result.fetchall())
           

        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: "+error)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def insert_data_customer():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gomrok',
                                                user='root',
                                                password='Bs5295025s')
            cid=int(input("Enter CustomerID : "))
            cname=input("Enter Customer Name : ")
            clastname=input("Enter CustomerLastName : ")
            cage=int(input("Enter Customer Age : "))
            insertion=(cid,cname,clastname,cage)                                    
            cursor = connection.cursor()
            result=cursor.callproc( procname='insert_customer', args=insertion)
            connection.commit()
            
            print("insert successfully!!")

            for result in cursor.stored_results():
                print(result.fetchall())
           

        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: "+error)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


    
    if choose==1:
        os.system('cls')
        insert_data_product()

    elif choose==2:
        insert_data_transport()
        
    elif choose ==3:
        os.system('cls')
        insert_data_store()
        
    elif choose==4:
        os.system('cls')
        insert_data_customer()
    else:
        print("Choose is Wrong!!! TRY AGAIN..")
        insert_information()

def select_information():
    os.system('cls')
    print(Fore.LIGHTMAGENTA_EX+"1.Select Data in product Table",end="\n")
    print(Fore.LIGHTMAGENTA_EX+"2.Select Data in Transport Table",end="\n")
    print(Fore.LIGHTMAGENTA_EX+"3.Select Data in store Table",end="\n")
    print(Fore.LIGHTMAGENTA_EX+"4.Select Data in customer Table",end="\n")
    choose=int(input("Enter For Select Data : "))
    def select_data_in_product():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='gomrok',
                                                    user='root',
                                                    password='Bs5295025s')
                insertion=int(input("Enter Id For Finding : "))
                cursor = connection.cursor()
                result=cursor.callproc('select_product',[insertion])
                connection.commit()
                # fetch result
                for result in cursor.stored_results():
                    detail=result.fetchall()
                for det in detail:
                    print(det)
                    print("Finding Successfully")
            except mysql.connector.Error as error:
                print("Failed to get record from MySQL table: {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

    def select_data_in_transport():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='gomrok',
                                                    user='root',
                                                    password='Bs5295025s')
                insertion=int(input("Enter Id For Finding : "))
                cursor = connection.cursor()
                result=cursor.callproc('select_transport',[insertion])
                connection.commit()
                # fetch result
                for result in cursor.stored_results():
                    detail=result.fetchall()
                for det in detail:
                    print(det)


                    print("Finding Successfully")
            except mysql.connector.Error as error:
                print("Failed to get record from MySQL table: {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")


    def select_data_in_store():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='gomrok',
                                                    user='root',
                                                    password='Bs5295025s')
                insertion=int(input("Enter Id For Finding : "))
                cursor = connection.cursor()
                result=cursor.callproc('select_store',[insertion])
                connection.commit()
                # fetch result
                for result in cursor.stored_results():
                    detail=result.fetchall()
                for det in detail:
                    print(det)


                    print("Finding Successfully")
            except mysql.connector.Error as error:
                print("Failed to get record from MySQL table: {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

    
    def select_data_in_customer():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='gomrok',
                                                    user='root',
                                                    password='Bs5295025s')
                insertion=int(input("Enter Id For Finding : "))
                cursor = connection.cursor()
                result=cursor.callproc('select_customer',[insertion])
                connection.commit()
                # fetch result
                for result in cursor.stored_results():
                    detail=result.fetchall()
                for det in detail:
                    print(det)


                    print("Finding Successfully")
            except mysql.connector.Error as error:
                print("Failed to get record from MySQL table: {}".format(error))

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")


    if choose==1: 
        os.system('cls')
        print("You Selected ProductTable")
        select_data_in_product()

    elif choose==2:
        print("You Selected TransportTable")
        select_data_in_transport()


    elif choose==3:
        os.system('cls')
        print("You Selected storeTable")
        select_data_in_store()


    elif choose==4:
        os.system('cls')
        print("You Selected CustomerTable")
        select_data_in_customer()
    else:
        print("choose is wrong!!!")
        exit

def update_information():
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX+"1.Update Data in product Table",end="\n")
    print(Fore.LIGHTYELLOW_EX+"2.Update Data in Transport Table",end="\n")
    print(Fore.LIGHTYELLOW_EX+"3.Update Data in store Table",end="\n")
    print(Fore.LIGHTYELLOW_EX+"4.Update Data in customer Table",end="\n")
    choose=int(input("Enter For UPDATE Data : "))

    def update_data_in_product():
    
    
            print("You Are Change ProductTable")

            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='gomrok',
                                                    user='root',
                                                    password='Bs5295025s')

                # before updating
                print("Before UPDATE ")
                pid=int(input("Enter ID For UPDATE :"))
                cursor = connection.cursor()
                result=cursor.callproc('select_product',[pid])
                connection.commit()
                # fetch result
                for result in cursor.stored_results():
                    detail=result.fetchall()
                for det in detail:
                    print(det)
            
                print("1.Change ProductName ")
                print("2.Change ProductType ")
                print("3.Change ProductYear ")
                choose=int(input("Enter 1 to 3 for Change : "))
                if choose == 1:
                    pname = input("New Name : ")

                    cursor.callproc('update_product', [pid,pname,'ptype',2050,choose])
                    connection.commit()
                    # print results
                    print("Change Successfully ")
                    for result in cursor.stored_results():
                        print(result.fetchall())
                elif choose == 2 :
                    ptype = input("NewType For Product : ")
                    cursor.callproc('update_product', [pid,'pname',ptype,'pyear',choose])
                    connection.commit()
                    # print results
                    print("Change Successfully ")
                    for result in cursor.stored_results():
                        print(result.fetchall())

                elif choose == 3 :
                    pyear = int(input("New Year Product : "))
                    cursor.callproc('update_product', [pid,'pname','ptype',pyear,choose])
                    connection.commit()
                    # print results
                    print("Change Successfully ")
                    for result in cursor.stored_results():
                        print(result.fetchall())
                else:
                    print("Choose is Wrong!!!")
                    update_data_in_product()
                
            except mysql.connector.Error as error:
                print("Failed to execute stored procedure: {}".format(error))
            finally:
                if (connection.is_connected()):
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")
    
    def update_date_in_transport():
            print("You Are Change ProductTable")

            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='gomrok',
                                                    user='root',
                                                    password='Bs5295025s')

                # before updating
                print("Before UPDATE ")
                tid=int(input("Enter ID For Show [AND] Update :"))
                cursor = connection.cursor()
                result=cursor.callproc('select_transport',[tid])
                connection.commit()
                # fetch result
                for result in cursor.stored_results():
                    detail=result.fetchall()
                for det in detail:
                    print(det)
            



                ptype = input("New Type Vehicle : ")

                cursor.callproc('update_transport', [tid,ptype])
                connection.commit()
                # print results
                print("Change Successfully ")
                for result in cursor.stored_results():
                    print(result.fetchall())

            except mysql.connector.Error as error:
                print("Failed to execute stored procedure: {}".format(error))
            finally:
                if (connection.is_connected()):
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")
    def update_date_in_store():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='gomrok',
                                                    user='root',
                                                    password='Bs5295025s')

                # before updating
                print("Before UPDATE ")
                sid=int(input("Enter ID For Show [AND] UPDATE :"))
                cursor = connection.cursor()
                result=cursor.callproc('select_store',[sid])
                connection.commit()
                # fetch result
                for result in cursor.stored_results():
                    detail=result.fetchall()
                for det in detail:
                    print(det)
            
                print("1.Change StoreType ")
                print("2.Change StoreCapacity ")
                choose=int(input("Enter 1 to 2 for Change : "))
                if choose == 1:
                    stype = input("New Type : ")

                    cursor.callproc('update_store', [sid,stype,2050,choose])
                    connection.commit()
                    # print results
                    print("Change Successfully ")
                    for result in cursor.stored_results():
                        print(result.fetchall())
                elif choose == 2 :
                    scapacity = input("New Capacity : ")
                    cursor.callproc('update_store', [sid,'pname',scapacity,choose])
                    connection.commit()
                    # print results
                    print("Change Successfully ")
                    for result in cursor.stored_results():
                        print(result.fetchall())
                else:
                    print("InputNumber is Wrong!!! Please Try Again :)")
                    update_date_in_store()
                
            except mysql.connector.Error as error:
                print("Failed to execute stored procedure: {}".format(error))
            finally:
                if (connection.is_connected()):
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")
    def update_data_in_customer():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='gomrok',
                                                    user='root',
                                                    password='Bs5295025s')

                # before updating
                print("Before UPDATE ")
                cid=int(input("Enter ID For Show [AND] UPDATE :"))
                cursor = connection.cursor()
                result=cursor.callproc('select_customer',[cid])
                connection.commit()
                # fetch result
                for result in cursor.stored_results():
                    detail=result.fetchall()
                for det in detail:
                    print(det)
            
                print("1.Change CustomerName ","\t\t")
                print("2.Change CustomerLastName ","\t\t")
                print("3.Change CustomerAge ","\t\t")
                print("4.Change All row Table Customer","\n")
                choose=int(input("Enter 1 to 3 for Change : "))
                if choose == 1:
                    cname = input("New Name : ")

                    cursor.callproc('update_customer', [cid,cname,'lastname',22,choose])
                    connection.commit()
                    # print results
                    print("Change Successfully ")
                    for result in cursor.stored_results():
                        print(result.fetchall())
                elif choose == 2 :
                    lcustomer = input("NewLastName For Customer : ")
                    cursor.callproc('update_customer', [cid,'pname',lcustomer,'cAGE',choose])
                    connection.commit()
                    # print results
                    print("Change Successfully ")
                    for result in cursor.stored_results():
                        print(result.fetchall())

                elif choose == 3 :
                    age = int(input("New Year Product : "))
                    cursor.callproc('update_customer', [cid,'firstName','LastName',age,choose])
                    connection.commit()
                    # print results
                    print("Change Successfully ")
                    for result in cursor.stored_results():
                        print(result.fetchall())
                elif choose == 4:
                    cname = input("New Name : ")
                    lcustomer = input("NewLastName For Customer : ")
                    age = int(input("New Year Product : "))
    
                    cursor.callproc('update_customer', [cid,cname,lcustomer,age,choose])
                    connection.commit()
                    # print results
                    print("Change Successfully ")
                    for result in cursor.stored_results():
                        print(result.fetchall())
                else:
                    print("Choose is Wrong!!! TRY AGAIN... ")
                    update_data_in_customer()
                
            except mysql.connector.Error as error:
                print("Failed to execute stored procedure: {}".format(error))
            finally:
                if (connection.is_connected()):
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")

    if choose == 1:
        update_data_in_product()
    elif choose == 2:
        update_date_in_transport()
    elif choose == 3:
        update_date_in_store()
    elif choose == 4:
        update_data_in_customer()
    else:
        print("Choose is Wrong!!! TRY AGAIN...")
        update_information()
    
def delete_information():
    os.system('cls')
    print(Fore.LIGHTGREEN_EX+"1.Delete Data in product Table",end="\n")
    print(Fore.LIGHTGREEN_EX+"2.Delete Data in Transport Table",end="\n")
    print(Fore.LIGHTGREEN_EX+"3.Delete Data in store Table",end="\n")
    print(Fore.LIGHTGREEN_EX+"4.Delete Data in customer Table",end="\n")
    choose=int(input("Choose Between 1 to 4 For DELETE Data : "))

    def delete_data_in_product():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gomrok',
                                                user='root',
                                                password='Bs5295025s')
            
            pid=int(input("Enter ProductID for Delete : "))

            cursor = connection.cursor()
            cursor.callproc('delete_product',[pid])
            # print results
            connection.commit()
            print("Delete Successfully ")
            for result in cursor.stored_results():
                print(result.fetchall())
            
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def delete_data_in_transport():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gomrok',
                                                user='root',
                                                password='Bs5295025s')
            
            tid=int(input("Enter VehicleID for Delete : "))

            cursor = connection.cursor()
            cursor.callproc('delete_transport',[tid])
            # print results
            connection.commit()
            print("Delete Successfully ")
            for result in cursor.stored_results():
                print(result.fetchall())
            
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    
    def delete_data_in_store():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gomrok',
                                                user='root',
                                                password='Bs5295025s')
            
            tid=int(input("Enter StoreID for Delete : "))

            cursor = connection.cursor()
            cursor.callproc('delete_store',[tid])
            # print results
            connection.commit()
            print("Delete Successfully ")
            for result in cursor.stored_results():
                print(result.fetchall())
            
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        
    def delete_data_in_customer():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gomrok',
                                                user='root',
                                                password='Bs5295025s')
            
            cid=int(input("Enter CustomerID for Delete : "))

            cursor = connection.cursor()
            cursor.callproc('delete_customer',[cid])
            # print results
            connection.commit()
            print("Delete Successfully ")
            for result in cursor.stored_results():
                print(result.fetchall())
            
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    
    if choose == 1:
        os.system('cls')
        delete_data_in_product()
    
    elif choose == 2:
        os.system('cls')
        delete_data_in_transport()

    elif choose == 3:
        os.system('cls')

        delete_data_in_store()
        
    elif choose == 4:
        os.system('cls')
        delete_data_in_customer()
    else:
        print("choose is wrong!!! TRY AGAIN...")
        delete_information()
        
while True:
    choose=menu()
    
    if choose==5:
        break
    elif choose == 1:
        insert_information()
    elif choose == 2:
        select_information()
    elif choose == 3:
        update_information()
    elif choose == 4:
        delete_information()
    else:
        continue
