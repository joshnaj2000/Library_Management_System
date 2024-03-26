
from ...db.sql_db import s_db 
import json
import logging
from ...schemas.model import User , Book

logging.basicConfig(level=logging.DEBUG , format='%(asctime)s - %(levelname)s - %(message)s' , filename="main.log")

class Service:
    def __init__(self):
        self.db = s_db.Library()


    def insert_users(self,user_id :int , user:User):
        try:
            existing_usr = "SELECT * FROM Users WHERE user_id = %s"
            self.db.mycursor.execute(existing_usr,(user_id,))
            usr = self.db.mycursor.fetchone()
            if usr is None:
                user_insert = "INSERT INTO Users (user_id , fname , lname , age , email , password) VALUES (%s , %s , %s , %s , %s , %s)"
                user_data = (user_id, user.fname , user.lname , user.age , user.email,user.password )
                self.db.mycursor.execute(user_insert , user_data)
                self.db.db.commit()
                logging.info("User Inserted with user id : {}".format(user_data))
                return {user_data}
            else:
                logging.warning("User already exist")
        except Exception as e:
            logging.exception("Exception Occured :{}".format(e))

    def insert_book(self,book_id:int ,book :Book):
        try:
            book_query = "SELECT * FROM Book WHERE Book_id = %s"
            self.db.mycursor.execute(book_query,(book_id,))
            existing_book = self.db.mycursor.fetchone()
            if existing_book is None:
                book_insert = "INSERT INTO Book (book_id , isbn , Title , Author, Publisher, Availability) VALUES (%s , %s , %s , %s , %s , %s)"
                book_data = (book_id , book.isbn , book.Title , book.Author, book.Publisher, book.Availability)
                self.db.mycursor.execute(book_insert , book_data)
                self.db.db.commit()
                logging.info("Book Inserted :{}".format(book_data))
                return {book_data}              
            else :
                logging.warning("Book Already Exists")
                return ("Book ALready Exists")
        except Exception as e:
            logging.exception("Exception Occured :{}".format(e))



    def update_user(self, user_id: int, user: User):
        try:
            user_query = "SELECT * FROM Users WHERE user_id = %s"
            self.db.mycursor.execute(user_query, (user_id,))
            existing_user = self.db.mycursor.fetchone()
            if existing_user is None:
                logging.warning("User not exists")
                return {"User not exists"}
            
            update_data = []
            values = []
            
            if user.fname is not None:
                update_data.append("fname = %s")
                values.append(user.fname)
            if user.lname is not None:
                update_data.append("lname = %s")
                values.append(user.lname)
            if user.age is not None:
                update_data.append("age = %s")
                values.append(user.age)
            if user.email is not None:
                update_data.append("email = %s")
                values.append(user.email)
            if user.password is not None:
                update_data.append("password = %s")
                values.append(user.password)         
            set_clause = ', '.join(update_data)
            values.append(user_id)
            query = f"UPDATE Users SET {set_clause} WHERE user_id = %s"
            self.db.mycursor.execute(query, tuple(values))
            self.db.db.commit()
            logging.info("Updated Sucessfully")
            return {"Successfully Updated"}
        except Exception as e:
            logging.exception("Exception Occured :{}".format(e))


    def update_book(self , book_id :int , book:Book ):
        try:
            book_query = "SELECT * FROM Book WHERE Book_id = %s"
            self.db.mycursor.execute(book_query , (book_id,))
            existing_book = self.db.mycursor.fetchone()
            if existing_book is None:
                logging.warning("Book not exits")
                return {"Book Not exists"}
            update_data = []
            values = []
                
            if book.isbn is not None:
                update_data.append("isbn = %s")
                values.append(book.isbn)
            if book.Title is not None:
                update_data.append("Title = %s")
                values.append(book.Title )
            if book.Author is not None:
                update_data.append("Author = %s")
                values.append(book.Author)
            if book.Publisher is not None:
                update_data.append("Publisher = %s")
                values.append(book.Publisher)
            if book.Availability is not None:
                update_data.append("Availability = %s")
                values.append(book.Availability)
            
            set_clause = ', '.join(update_data)
            values.append(book_id)
            query = f"UPDATE Book SET {set_clause} WHERE Book_id = %s"
            
            self.db.mycursor.execute(query, tuple(values))
            self.db.db.commit()  
            logging.info("Successfully updated")
            return {"Updated"}
        except Exception as e:
            logging.exception("Exception Occured :{}".format(e))


    def get_user(self , fname:str):
        try:
            user = "SELECT * FROM Users WHERE fname = %s"
            if user is None:
                print("User Not exists")
            self.db.mycursor.execute(user, (fname,))
            result = self.db.mycursor.fetchall()
            logging.info("User :{}".format(result))
            return (result)

        except Exception as e:
            logging.exception("Exception Occured :{}".format(e))

    

    def get_book(self , book_id:int):
        try:
            book = "SELECT * FROM Book WHERE Book_id = %s"
            if book is None:
                print("Book Not Exists")
            self.db.mycursor.execute(book, (book_id,))
            result = self.db.mycursor.fetchall()
            logging.info("Book :{}".format(result))

            return (result)
        except Exception as e:
            logging.exception("Exception Occured :{}".format(e))
    
    
    def delete_user(self , user_id :int):
        try:
            user = "SELECT * FROM Users WHERE User_id = %s"
            self.db.mycursor.execute(user,(user_id,))
            existing_user = self.db.mycursor.fetchone()
            if existing_user is None:
                logging.warning("USer not exist")
            query = "DELETE FROM Users WHERE User_id = %s"
            self.db.mycursor.execute(query,(user_id,))
            self.db.db.commit()
            logging.info("User Deleted with user id :{}".format(user_id))
            return ("User Deleted")
        except Exception as e:
            logging.exception("Exception Occured :{}".format(e))

    def delete_book(self , book_id:int):
        try:
            book = "SELECT * FROM Book WHERE Book_id = %s"
            self.db.mycursor.execute(book , (book_id,))
            existing_book = self.db.mycursor.fetchone()
            if existing_book is None:
                logging.warning("book not exists")
            query = "DELETE FROM Book WHERE Book_id = %s"
            self.db.mycursor.execute(query,(book_id,))
            self.db.db.commit()
            logging.info("Book deleted with book id:{}".format(book_id))
            return ("Book DEleted")
        except Exception as e:
            logging.exception("Exception Occured :{}".format(e))


    def borrow_book(self,user_id:int , book_id :int):
        try:
            user_query = "SELECT * FROM Users WHERE user_id = %s"
            self.db.mycursor.execute(user_query , (user_id,))
            user_one = self.db.mycursor.fetchone()
            if user_one is None:
                logging.warning("User not found")
            else:
                book_query = "SELECT * FROM Book WHERE Book_id = %s"
                self.db.mycursor.execute(book_query , (book_id,))
                book_one = self.db.mycursor.fetchone()
                if book_one is None:
                    logging.warning("Book Not found")
                else:
                    current_list = "SELECT borrowed_books FROM Users WHERE user_id = %s"
                    self.db.mycursor.execute(current_list,(user_id,))  
                    current_borrowed_books = self.db.mycursor.fetchone()[0]

                    if current_borrowed_books is None:
                        book_borrowed_list = []
                    else:
                        book_borrowed_list = json.loads(current_borrowed_books) 
                        if not isinstance(book_borrowed_list, list):
                            book_borrowed_list = []
                    book_borrowed_list.append(book_id)
                    updated = json.dumps(book_borrowed_list) 
                    b_book = "UPDATE Users SET borrowed_books = %s WHERE user_id = %s"
                    self.db.mycursor.execute(b_book , (updated,user_id))
                    count = "UPDATE Book SET availability = availability -1  WHERE Book_id = %s"
                    self.db.mycursor.execute(count , (book_id,))
                    self.db.db.commit()
                    logging.info("Book Borrowed")
                    return {"Book Borrowed"}
        except Exception as e:
            logging.exception("Exception Occured :{}".format(e))



    def return_book(self ,user_id:int , book_id:int):
        try:
            user_query = "SELECT * FROM Users WHERE user_id = %s"
            self.db.mycursor.execute(user_query , (user_id,))
            user_one = self.db.mycursor.fetchone()
            if user_one is None:
                logging.warning("User not found")
            else:
                book_query = "SELECT * FROM Book WHERE Book_id = %s"
                self.db.mycursor.execute(book_query , (book_id,))
                book_one = self.db.mycursor.fetchone()
                if book_one is None:
                    logging.warning("Book Not found")
                else:

                    current_list = "SELECT borrowed_books FROM Users WHERE user_id = %s"
                    self.db.mycursor.execute(current_list,(user_id,))  
                    current_borrowed_books = self.db.mycursor.fetchone()[0]

                    if current_borrowed_books is None:
                        logging.warning("User didnt have the book")
                    else:
                        book_borrowed_list = json.loads(current_borrowed_books) 
                        if book_id in  book_borrowed_list:
                            book_borrowed_list.remove(book_id)
                            updated = json.dumps(book_borrowed_list) 
                            b_book = "UPDATE Users SET borrowed_books = %s WHERE user_id = %s"
                            self.db.mycursor.execute(b_book , (updated,user_id))
                            count = "UPDATE Book SET availability = availability +1  WHERE Book_id = %s"
                            self.db.mycursor.execute(count , (book_id,))
                            self.db.db.commit()
                            logging.info("book retured")
                            return {"Book returned"}
        except Exception as e:
            logging.exception("Exception Occured :{}".format(e))


    def get_borrowed_books(self , user_id :int ):
        try:
            user_query = "SELECT * FROM Users WHERE user_id = %s"
            self.db.mycursor.execute(user_query, (user_id,))
            user_one = self.db.mycursor.fetchone()
            if user_one is None:
                logging.warning("User not found.")
            else:
                book_query="select bl.user_id ,b.book_id ,  b.isbn , b.Title , b.Author , b.Author , b.Publisher , b.Availability  from Book b inner join BorrowedList bl on b.Book_id = bl.book_id where user_id = %s"
                self.db.mycursor.execute(book_query, (user_id,))
                borrowed_books_details = self.db.mycursor.fetchall()
                logging.info(f"Borrowed Books:{borrowed_books_details}")
                return (borrowed_books_details)
        except Exception as e:
            logging.critical("Exception Occured :{}".format(e))



    def find_user_first_letter(self , letter:str):
        try:
            query = " select * from users where fname LIKE %s "
            self.db.mycursor.execute(query , (f"{letter}%",))
            user = self.db.mycursor.fetchall()
            if user is None:
                logging.warning("User not found ")
            else:
                logging.info("User found:{}".format(user))
                return user
        except Exception as e:
            logging.exception(e)

    def users(self):
        try:
            query = "select * from users order by fname asc "
            self.db.mycursor.execute(query)
            users = self.db.mycursor.fetchall()
            if users is None:
                logging.info("There are no users")
            else:
                logging.info("User found :{}".format(users))
                return users
        except Exception as e:
            logging.exception(e)
    
# @app.get("/left-join") #Get details of all users and borrowed books even if a user didnt take any book
    def left_join(self):
        try:
            query = "select * from users u left join borrowedlist  bb on u.user_id = bb.user_id"
            # qquery = "select * from users u left join borrowedlist  bb on u.user_id = bb.user_id where book_id is null"
            self.db.mycursor.execute(query)
            details = self.db.mycursor.fetchall()
            logging.info("fetched")
            return details
        except Exception as e:
            logging.error("Exception Occur")


    #Get details of all book with corresponding user details , if a book is borrowed by nobody the user will not be there
    def right_join(self):
        try:
            query = "select * from borrowedlist bb right join users u on u.user_id = bb.user_id"
            self.db.mycursor.execute(query)
            details = self.db.mycursor.fetchall()
            logging.info("fetched")
            return details
        except Exception as e:
            logging.error("Exception Occur")


     #Get cartesian product of datas , each user is connected with each book
    def cross_join(self):
        try :
            query = "select * from borrowedlist bb cross join users u"
            self.db.mycursor.execute(query)
            details = self.db.mycursor.fetchall()
            logging.info("fetched")
            return details
        except Exception as e:
            logging.error("Exception Occur")





























































    # from fastapi import FastAPI
    # from services import sql_services 
# from schemas import model

# app = FastAPI()

# ser = sql_services.Service()

# User = model.User
# Book = model.Book

# @app.post("/insert-user/{user_id}")
# def insert_user(user_id:int  , user:User):
#     return ser.insert_users(user_id , user)
    

# @app.post("/insert-book/{book_id}")
# def insert_book(book_id:int , book:Book):
#     return ser.insert_book(book_id , book)

# @app.put("/update-user/{user_id}")
# def update_user(user_id:int , user:User):
#     return ser.update_user(user_id , user)

# @app.put("/update-book/{book_id}")
# def update_book(book_id:int , book:Book):
#     return ser.update_book(book_id , book)

# @app.get("/get-user/{user_id}")
# def get_user(fname:str):
#     return ser.get_user(fname)

# @app.get("/get-book/{book_id}")
# def get_book(book_id:int):
#     return ser.get_book(book_id)

# @app.delete("/delete-user/{user_id}")
# def delete_user(user_id:int):
#     return ser.delete_user(user_id)

# @app.delete("/delete-book/{book_id}")
# def delete_book(book_id:int):
#     return ser.delete_book(book_id)

# @app.put("/borrow-book/{user_id}")
# def borrow_book(user_id:int , book_id:int):
#     return ser.borrow_book(user_id , book_id)

# @app.put("/return_book/{book_id}")
# def return_book(user_id:int , book_id:int):
#     return ser.return_book(user_id , book_id)