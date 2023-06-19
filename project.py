import mysql.connector
import os
def menu():
    
    print("1.Insert Information  ",end='\n')
    print("2.Select Information  ",end='\n')
    print("3.Update Information  ",end='\n')
    print("4.Delete Information  ",end='\n')
    print("5.Exit  ",end='\n')
    choose=int(input("Select 1 to 5 :  "))
    return choose

def insert_information():
    os.system('cls')
    print("1.Insert Data For Customer",end="\n")
    print("2.Insert Data For Factor ",end="\n")
    print("3.Insert Data For Food",end="\n")
    print("4.Insert Data For Senf ",end="\n")

    choose=int(input("Enter Number : "))

    def insert_data_customer():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='resturan',
                                                user='root',
                                                password='Bs5295025s')
            cid=int(input("Enter customer_id : "))
            cname=input("Enter Name : ")
            cnumber=int(input("Enter number : "))
            caddress=input("Enter address : ")
            insertion=(cid,cname,cnumber,caddress)
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

    def insert_data_factor():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='resturan',
                                                user='root',
                                                password='Bs5295025s')
            fid=int(input("Enter factor_id  : "))
    
            ffood_quantity = int(input("Enter foodquantity : "))
            funitprice = int(input("Enter UnitPrice : "))
            ftakhfif = int(input("Enter takhfif : "))
            insertion=[fid,ffood_quantity,funitprice,ftakhfif]
            cursor = connection.cursor()
            result=cursor.callproc( procname='insert_factor', args=insertion)
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

    def insert_data_food():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='resturan',
                                                user='root',
                                                password='Bs5295025s')
            fid=int(input("Enter food_id : "))
            fname=input("Enter FoodName : ")
            ffood_description=input("Enter fooddescription : ")
    
            insertion=(fid,fname,ffood_description)
            cursor = connection.cursor()
            result=cursor.callproc( procname='insert_food', args=insertion)
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

    def insert_data_senf():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='resturan',
                                                user='root',
                                                password='Bs5295025s')
            id=int(input("Enter Food_id : "))
            type=input("Enter Type of food : ")
            report=input("Report For Food : ")
            insertion=(id,type,report)
            cursor = connection.cursor()
            result=cursor.callproc( procname='insert_senf', args=insertion)
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
        insert_data_customer()

    if choose==2:
        insert_data_factor()
        
    if choose ==3:
        os.system('cls')
        insert_data_food()
        
    if choose==4:
        os.system('cls')
        insert_data_senf()
    else:

        print("Choose is Wrong!!")
        insert_information()

def select_information():
    os.system('cls')
    print("1.Select Data in customer Table",end="\n")
    print("2.Select Data in factor Table",end="\n")
    print("3.Select Data in food Table",end="\n")
    print("4.Select Data in senf Table",end="\n")
    choose=int(input("Enter For Select Data : "))
    def select_data_in_customer():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='resturan',
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

    def select_data_in_factor():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='resturan',
                                                    user='root',
                                                    password='Bs5295025s')
                insertion=int(input("Enter Id For Finding : "))
                cursor = connection.cursor()
                result=cursor.callproc('select_factor',[insertion])
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


    def select_data_in_food():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='resturan',
                                                    user='root',
                                                    password='Bs5295025s')
                insertion=int(input("Enter Id For Finding : "))
                cursor = connection.cursor()
                result=cursor.callproc('select_food',[insertion])
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

    
    def select_data_in_senf():
            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='resturan',
                                                    user='root',
                                                    password='Bs5295025s')
                insertion=int(input("Enter FoodId For Finding : "))
                cursor = connection.cursor()
                result=cursor.callproc('select_senf',[insertion])
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
        print("You Selected cstomerTable")
        select_data_in_customer()

    elif choose==2:
        print("You Selected factorTable")
        select_data_in_factor()


    elif choose==3:
        os.system('cls')
        print("You Selected foodTable")
        select_data_in_food()


    elif choose==4:
        os.system('cls')
        print("You Selected SenfTable")
        select_data_in_senf()
    else:
    
        print("choose is wrong!!!!")
        select_information()
def update_information():
    os.system('cls')
    print("1.Update Data in customer Table",end="\n")
    print("2.Update Data in factor Table",end="\n")
    print("3.Update Data in food Table",end="\n")
    print("4.Update Data in Senf Table",end="\n")
    choose=int(input("Enter For UPDATE Data : "))
    def update_customer_table():
    
            print("Your Are Change customerTable")

            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='resturan',
                                                    user='root',
                                                    password='Bs5295025s')
                
                pid=int(input("Enter customerID for change : "))
                print("before updating!!!!!")
                cursor = connection.cursor()
                result=cursor.callproc('select_customer',[pid])
                connection.commit()
                    # fetch result
                for result in cursor.stored_results():
                    detail=result.fetchall()
                for det in detail:
                    print(det)
                
                pname=input("Enter New Name : ")
                pnumber=int(input("Enter New number : "))
                paddress=input("Enter New Address : ")
                insertion=[pid,pname,pnumber,paddress]
                cursor = connection.cursor()
                cursor.callproc('update_customer', insertion)
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
    def update_factor_table():
            print("Your Are Change customerTable")

            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='resturan',
                                                    user='root',
                                                    password='Bs5295025s')

                id = int(input("Enter factorID for change : "))
                fquantity =int( input("Enter New food_quantity : "))
                funitprice=int(input("Enter New UnitPrice : "))
                ftakhfif=int(input("Enter New Takhfif : "))
                insertion = [id, fquantity,funitprice,ftakhfif]
                cursor = connection.cursor()
                cursor.callproc('update_factor', insertion)
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

    def update_food_table():
            print("Your Are Change foodTable")

            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='resturan',
                                                    user='root',
                                                    password='Bs5295025s')

                pid = int(input("Enter foodID for change : "))
                pname = input("Enter New food : ")
                food_description=input("Enter New Description For food : ")
                insertion = [pid, pname,food_description]
                cursor = connection.cursor()
                cursor.callproc('update_food', insertion)
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
    def update_senf_table():
            print("Your Are Change SenfTable")

            try:
                connection = mysql.connector.connect(host='localhost',
                                                    database='resturan',
                                                    user='root',
                                                    password='Bs5295025s')

                id = int(input("Enter FoodId : "))
                type = input("Enter New Type of Food : ")
                report=input("Enter Report : ")
                insertion = [id,type,report]
                cursor = connection.cursor()
                cursor.callproc('update_senf', insertion)
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
    if choose==1: 
        os.system('cls')
        print("update customer table")
        update_customer_table()

    elif choose==2:
        print("Update factor table")
        update_factor_table()


    elif choose==3:
        os.system('cls')
        print("update factor table")
        update_food_table()


    elif choose==4:
        os.system('cls')
        print("update senf table")
        update_senf_table()
    else:
        print("Choose is wrong!!!")
        update_information()
    
def delete_information():
    os.system('cls')
    print("1.Delete Data in customer Table",end="\n")
    print("2.Delete Data in factor Table",end="\n")
    print("3.Delete Data in food Table",end="\n")
    print("4.Delete Data in senf Table",end="\n")
    choose=int(input("Choose Between 1 to 4 For delete Data : "))

    def delete_data_in_customer():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='resturan',
                                                user='root',
                                                password='Bs5295025s')
            
            pid=int(input("Enter customer_id for Delete : "))

            cursor = connection.cursor()
            cursor.callproc('delete_customer',[pid])
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

    def delete_data_in_factor():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='resturan',
                                                user='root',
                                                password='Bs5295025s')
            
            tid=int(input("Enter factor_id for Delete : "))

            cursor = connection.cursor()
            cursor.callproc('delete_factor',[tid])
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
    
    def delete_data_in_food():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='resturan',
                                                user='root',
                                                password='Bs5295025s')
            
            tid=int(input("Enter food_id for Delete : "))

            cursor = connection.cursor()
            cursor.callproc('delete_food',[tid])
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
        
    def delete_data_in_senf():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='resturan',
                                                user='root',
                                                password='Bs5295025s')
            
            cid=int(input("Enter Food_id for Delete : "))

            cursor = connection.cursor()
            cursor.callproc('delete_senf',[cid])
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
        delete_data_in_customer()
    
    elif choose == 2:
        os.system('cls')
        delete_data_in_factor()

    elif choose == 3:
        os.system('cls')

        delete_data_in_food()
        
    elif choose == 4:
        os.system('cls')
        delete_data_in_senf()
    else:
        print("Choose is wrong!!!")
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

