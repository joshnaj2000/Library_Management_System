
# from schemas.model import User , Book
from ...config.mdb_cofig import my_mongo_db
import logging


logging.basicConfig(level=logging.DEBUG , format=' %(asctime)s - %(levelname)s - %(message)s' , filename="main.log")

class Mongo_Library:
    def __init__(self):
        self.db = my_mongo_db.db

        
    
    def insert_user(self, user_id, user_data):
        try:
            existing_user = self.db.user.find_one({"id": user_id})
            if existing_user:
                logging.warning("User already exists")
            else:
                user_data["id"] = user_id
                self.db.user.insert_one(user_data)
                logging.info("User inserted successfully")
        except Exception as e:
            logging.error(f"Error inserting user: {e}")

    def insert_book(self, book_id, book_data):
        try:
            existing_book = self.db.book.find_one({"book_id": book_id})
            if existing_book:
                logging.warning("Book already exists")
            else:
                book_data["book_id"] = book_id
                self.db.book.insert_one(book_data)
                logging.info("Book inserted successfully")
        except Exception as e:
            logging.error(f"Error inserting book: {e}")


    def get_user(self , user_id):
        try:
            user_details = self.db.user.find_one({"id":user_id})
            if not user_details :
                logging.warning("User not found")
                return {"user_details not found"}
            else:
                user_details['id']=str(user_details['id'])
                del user_details["_id"]
                logging.info("User found with user id :{}".format(user_details))
                return user_details
        except Exception as e:
            logging.exception(e)


    def get_book(self , book_id):
        try:
            book_details = self.db.book.find_one({"book_id":book_id})
            if not book_details :
                logging.warning("Book Not found")
                return {"book_details not found"}
            else:
                book_details['book_id']=str(book_details['book_id'])
                del book_details["_id"]
                logging.info("Book found with Book id :{}".format(book_details))
                return book_details
        except Exception as e:
            logging.exception(e)


    def update_user(self , user_id , user):
        try:
            user_details = self.db.user.find_one({"id": user_id})
            if not user_details:
                logging.warning("User not found")
                return {"User not exists"}
            update_data = {}
            if user.fname is not None:
                update_data["fname"] = user.fname
            if user.lname is not None:
                update_data["lname"] = user.lname
            if user.age is not None:
                update_data["age"] = user.age
            if user.email is not None:
                update_data["email"] = user.email
            self.db.user.update_one({"id": user_id}, {"$set": update_data})
            updated_user = self.db.user.find_one({"id": user_id})
            updated_user['_id'] = str(updated_user['_id'])  
            logging.info("User updated : {}" .format(updated_user))
            return updated_user
        except Exception as e:
            logging.exception(e)

    
        
    def update_book(self , book_id  , book ):
        try:
            book_details = self.db.book.find_one({"book_id": book_id})
            if not book_details:
                logging.warning("Book not found")
                return {"Book not exists"}
            update_data = {}
            if book.isbn is not None:
                update_data["isbn"] = book.isbn
            if book.title is not None:
                update_data["title"] = book.title
            if book.author is not None:
                update_data["author"] = book.author
            if book.year is not None:
                update_data["year"] = book.year
            if book.availability is not None:
                update_data["availability"] = book.availability
            self.db.book.update_one({"book_id": book_id}, {"$set": update_data})
            self.db.book.find_one({"id": book_id})
            logging.info("Book Updated:{}".format(update_data))
            return {"Book Updated "}
        except Exception as e:
            logging.exception(e)


    def delete_user(self , user_id):
        try:
            user_details = self.db.user.find_one({"id": user_id})
            if user_details:
                # if 'borrowed_books' in user_details:
                #     return_book(self, user_id, user_details['borrowed_books'])               
                self.db.user.delete_one(user_details)
                logging.info("User deleted successfully")
                return {"User deleted successfully"}
            else:
                logging.warning("User not exists")
                return {"User not exists"}
        except Exception as e:
            logging.exception(e)
            return {"error": str(e)}
        
    def delete_book(self , book_id):
        try:
            book_details = self.db.book.find_one({"book_id": book_id})
            if book_details:
                # if 'borrowed_books' in user_details:
                #     return_book(self, user_id, user_details['borrowed_books'])               
                self.db.book.delete_one(book_details)
                logging.info("Book Deleted Successfully:{}".format(book_id))
                return {"Book deleted successfully"}
            else:
                return {"Book not exists"}
        except Exception as e:
            logging.exception(e)
            return {"error": str(e)}
        

    def borrow_book(self , user_id, book_id):
        try:
            existing_user = self.db.user.find_one({"id": user_id})

            if existing_user:
                existing_book = self.db.book.find_one({"book_id": book_id, "availability": {"$gt": 0}})

                if existing_book and existing_book['book_id'] not in existing_user["borrowed_books"]:
                    self.db.book.update_one({"book_id": existing_book['book_id'], "availability": {"$gt": 0}}, {"$inc": {"availability": -1}})
                    self.db.user.update_one({"id": user_id}, {"$addToSet": {"borrowed_books": existing_book['book_id']}})
                    logging.info("Book Borrowed Successfully")
                    return {"Book borrowed successfully."}
                else:
                    logging.warning("Book not found or not available")
                    return {"Book not found or not available."}
            else:
                logging.warning("User not found")
                return {"User not found."}
        except Exception as e:
            logging.error(e)
            return {"Error updating book"}
        

    def return_book(self , user_id, book_id):
        try:
            existing_user = self.db.user.find_one({"id": user_id})

            if existing_user:
                existing_book = self.db.book.find_one({"book_id": book_id})

                if existing_book and existing_book['book_id']  in existing_user['borrowed_books']:
                    self.db.book.update_one({"book_id": existing_book['book_id']}, {"$inc": {"availability": 1}})
                    self.db.user.update_one({"id": user_id}, {"$unset": {"borrowed_books": existing_book['book_id']}})
                    logging.info("Book Returened Successfully")
                    return {"Book returned successfully."}
                else:
                    logging.warning("Book not found")
                    return {"Book not found or not available."}
            else:
                logging.warning("User not found")
                return {"User not found."}
        except Exception as e:
            logging.exception(e)
            return {"Error updating book"}







































# from services import mongo_services
# from fastapi import FastAPI , Depends
# from schemas import model
# from db.Mongo_db import m_db

# m_service = mongo_services.Mongo_Library()
# User = model.User
# Book = model.Book
# mongo = m_db.mongo_db

# app = FastAPI()

# @app.post("/insert-user/{user_id}")
# def insert_document_user(user_id: int, user: User, db: mongo = Depends()):
#     m_service.insert_user(user_id, user.dict())
#     return {"message": "User inserted successfully"}

# @app.post("/insert-book/{book_id}")
# def insert_document_book(book_id: int, book: Book, db:mongo = Depends()):
#     m_service.insert_book(book_id, book.dict())
#     return {"message": "Book inserted successfully"}

# @app.get("/get-user/{user_id}")
# def get_user(user_id:int , db :mongo = Depends()):
#     user = m_service.get_user(user_id)
#     return user

# @app.get("/get-book/{book_id}")
# def get_book(book_id:int , db :mongo = Depends()):
#     book = m_service.get_book(book_id)
#     return book

# @app.put("/update-user/{user_id}")
# def update_user(user_id:int ,user :User, db:mongo = Depends()):
#     user = m_service.update_user(user_id,user)
#     return user

# @app.put("/update-book/{book-id}")
# def update_book(book_id:int ,book :Book, db:mongo = Depends()):
#     book = m_service.update_book(book_id,book)
#     return book

# @app.delete("/delete-user/{user-id}")
# def delete_user(user_id:int , db:mongo = Depends()):
#     user = m_service.delete_user(user_id)
#     return user


# @app.delete("/delete-book/{book-id}")
# def delete_book(book_id:int , db:mongo = Depends()):
#     book = m_service.delete_book(book_id)
#     return book

# @app.put("/borrow_book/{user_id}")
# def borrow_book(user_id:int , book_id :int , db:mongo = Depends()):
#     borrow = m_service.borrow_book(user_id , book_id)
#     return borrow

# @app.put("/return_book/{user_id}")
# def return_book(user_id:int , book_id :int , db:mongo = Depends()):
#     returnn = m_service.return_book(user_id , book_id)
#     return returnn
