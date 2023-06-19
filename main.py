from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel
from customer import customer
from factor import factor

app=FastAPI()

@app.get('/customer/{customer_id}')
def get_customer(customer_id:int):
    try:
        mydb=mysql.connector.connect(host='localhost',
                             database='resturan',
                             user='root',
                             password='Bs5295025s'

)
        cursor=mydb.cursor()
        result=cursor.callproc('select_customer',[customer_id])
        mydb.commit()

        for result in cursor.stored_results():
            detail=result.fetchall()
            if len(detail) > 0:
                 for det in detail:
                      return(det)
            else:
                 raise HTTPException(status_code=404,detail="customer not found!!!")
        
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
            if mydb.is_connected():
                    cursor.close()
                    mydb.close()
                    print("MySQL connection is closed")       

@app.post('/create_customer')
def get_customer(customer:customer):
    try:
        mydb=mysql.connector.connect(host='localhost',
                             database='resturan',
                             user='root',
                             password='Bs5295025s'

)
        customer0=[customer.id,customer.name,customer.number,customer.address]
        cursor=mydb.cursor()
        result=cursor.callproc(procname='insert_customer',args=customer0)
        mydb.commit()
        
        for result in cursor.stored_results():
            print(result.fetchall())
        # for det in detail:
        #     return(det)

        return {f"insert successfully!!"}
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
            if mydb.is_connected():
                    cursor.close()
                    mydb.close()
                    print("MySQL connection is closed") 

@app.delete('/customer/{customer_id}')
def delete_customer(customer_id:int):
    try:
        mydb=mysql.connector.connect(host='localhost',
                             database='resturan',
                             user='root',
                             password='Bs5295025s'

)
        cursor=mydb.cursor()
        result=cursor.callproc('delete_customer',[customer_id])
        mydb.commit()

        for result in cursor.stored_results():
            print(result.fetchall())
        


        return {f"Delete Successfully!!"}
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
            if mydb.is_connected():
                    cursor.close()
                    mydb.close()
                    print("MySQL connection is closed")  

@app.post('/customer/update_customer')
def update_customer(customer:customer):
    try:
        mydb=mysql.connector.connect(host='localhost',
                             database='resturan',
                             user='root',
                             password='Bs5295025s'

)
        customer0=[customer.id,customer.name,customer.number,customer.address]
        cursor=mydb.cursor()
        result=cursor.callproc(procname='update_customer',args=customer0)
        mydb.commit()
        
        for result in cursor.stored_results():
            print(result.fetchall())
        # for det in detail:
        #     return(det)

        return {f"update successfully!!"}
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
            if mydb.is_connected():
                    cursor.close()
                    mydb.close()
                    print("MySQL connection is closed") 