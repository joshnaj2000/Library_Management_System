
# from handler.mongo_handler import Mongo_Library

# from schemas.model import User,Book
# from db.Mongo_db import m_db
# from handler import mongo_handler
# m_handler = mongo_handler.Mongo_Library
# # User = User
# Book =Book
# mongo = m_db.mongo_db

from fastapi import FastAPI , Depends , APIRouter
# from handler import mongo_handler
from ..handler.mongo_handler import Mongo_Library
from ...schemas.model import User,Book
from ...dependencies.mongo_dependencies import MongoDbDependency


app = FastAPI()
router = APIRouter()


# class MongoDbDependency:
#     def __init__(self):
#         self.mongo_handler = Mongo_Library()

#     def __call__(self):
#         return self.mongo_handler


# mongo = MongoDbDependency()  

@router.post("/insert-user/{user_id}")
def insert_document_user(user_id: int, user: User, db: MongoDbDependency = Depends()):
    db.mongo_handler.insert_user(user_id, user.dict())

@router.post("/insert-book/{book_id}")
def insert_document_book(book_id: int, book: Book, db:MongoDbDependency = Depends()):
    db.mongo_handler.insert_book(book_id, book.dict())
    return {"Book inserted successfully"}

@router.get("/get-user/{user_id}")
def get_user(user_id:int , db :MongoDbDependency = Depends()):
    user = db.mongo_handler.get_user(user_id)
    return user

@router.get("/get-book/{book_id}")
def get_book(book_id:int , db :MongoDbDependency = Depends()):
    book = db.mongo_handler.get_book(book_id)
    return book

@router.put("/update-user/{user_id}")
def update_user(user_id:int ,user :User, db:MongoDbDependency = Depends()):
    user = db.mongo_handler.update_user(user_id,user)
    return user

@router.put("/update-book/{book-id}")
def update_book(book_id:int ,book :Book, db:MongoDbDependency= Depends()):
    book = db.mongo_handler.update_book(book_id,book)
    return book

@router.delete("/delete-user/{user-id}")
def delete_user(user_id:int , db:MongoDbDependency = Depends()):
    user = db.mongo_handler.delete_user(user_id)
    return user


@router.delete("/delete-book/{book-id}")
def delete_book(book_id:int , db:MongoDbDependency= Depends()):
    book = db.mongo_handler.delete_book(book_id)
    return book

@router.put("/borrow_book/{user_id}")
def borrow_book(user_id:int , book_id :int , db:MongoDbDependency= Depends()):
    borrow = db.mongo_handler.borrow_book(user_id , book_id)
    return borrow

@router.put("/return_book/{user_id}")
def return_book(user_id:int , book_id :int , db:MongoDbDependency = Depends()):
    returnn = db.mongo_handler.return_book(user_id , book_id)
    return returnn

    

mongo_service_router = router




# @app.post("/insert-user/{user_id}")
# def insert_document_user(user_id: int, user: User, db: mongo = Depends()):
#     m_handler.insert_user(user_id, user.dict())
#     return {"User inserted successfully"}

# @app.post("/insert-book/{book_id}")
# def insert_document_book(book_id: int, book: Book, db:mongo = Depends()):
#     m_handler.insert_book(book_id, book.dict())
#     return {"Book inserted successfully"}

# @app.get("/get-user/{user_id}")
# def get_user(user_id:int , db :mongo = Depends()):
#     user = m_handler.get_user(user_id)
#     return user

# @app.get("/get-book/{book_id}")
# def get_book(book_id:int , db :mongo = Depends()):
#     book = m_handler.get_book(book_id)
#     return book

# @app.put("/update-user/{user_id}")
# def update_user(user_id:int ,user :User, db:mongo = Depends()):
#     user = m_handler.update_user(user_id,user)
#     return user

# @app.put("/update-book/{book-id}")
# def update_book(book_id:int ,book :Book, db:mongo= Depends()):
#     book = m_handler.update_book(book_id,book)
#     return book

# @app.delete("/delete-user/{user-id}")
# def delete_user(user_id:int , db:mongo = Depends()):
#     user = m_handler.delete_user(user_id)
#     return user


# @app.delete("/delete-book/{book-id}")
# def delete_book(book_id:int , db:mongo= Depends()):
#     book = m_handler.delete_book(book_id)
#     return book

# @app.put("/borrow_book/{user_id}")
# def borrow_book(user_id:int , book_id :int , db:mongo= Depends()):
#     borrow = m_handler.borrow_book(user_id , book_id)
#     return borrow

# @app.put("/return_book/{user_id}")
# def return_book(user_id:int , book_id :int , db:mongo = Depends()):
#     returnn = m_handler.return_book(user_id , book_id)
#     return returnn







































































# # class Mongo_Library:
    
# #     def insert_user(self, user_id, user_data):
# #         try:
# #             existing_user = self.db.user.find_one({"id": user_id})
# #             if existing_user:
# #                 print("User already exists")
# #             else:
# #                 user_data["id"] = user_id
# #                 self.db.user.insert_one(user_data)
# #                 print("User inserted successfully")
# #         except Exception as e:
#             print(f"Error inserting user: {e}")

#     def insert_book(self, book_id, book_data):
#         try:
#             existing_book = self.db.book.find_one({"book_id": book_id})
#             if existing_book:
#                 print("Book already exists")
#             else:
#                 book_data["book_id"] = book_id
#                 self.db.book.insert_one(book_data)
#                 print("Book inserted successfully")
#         except Exception as e:
#             print(f"Error inserting book: {e}")


#     def get_user(self , user_id):
#         try:
#             user_details = self.db.user.find_one({"id":user_id})
#             if not user_details :
#                 return {"user_details not found"}
#             else:
#                 user_details['id']=str(user_details['id'])
#                 del user_details["_id"]
#                 return user_details
#         except Exception as e:
#             print(e)


#     def get_book(self , book_id):
#         try:
#             book_details = self.db.book.find_one({"book_id":book_id})
#             if not book_details :
#                 return {"book_details not found"}
#             else:
#                 book_details['book_id']=str(book_details['book_id'])
#                 del book_details["_id"]
#                 return book_details
#         except Exception as e:
#             print(e)


#     def update_user(self , user_id , user):
#         try:
#             user_details = self.db.user.find_one({"id": user_id})
#             if not user_details:
#                 return {"User not exists"}
#             update_data = {}
#             if user.fname is not None:
#                 update_data["fname"] = user.fname
#             if user.lname is not None:
#                 update_data["lname"] = user.lname
#             if user.age is not None:
#                 update_data["age"] = user.age
#             if user.email is not None:
#                 update_data["email"] = user.email
#             self.db.user.update_one({"id": user_id}, {"$set": update_data})
#             updated_user = self.db.user.find_one({"id": user_id})
#             updated_user['_id'] = str(updated_user['_id'])  # Convert ObjectId to string

#             return updated_user
#         except Exception as e:
#             print(e)

    
        
#     def update_book(self , book_id  , book ):
#         try:
#             book_details = self.db.book.find_one({"book_id": book_id})
#             if not book_details:
#                 return {"Book not exists"}
#             update_data = {}
#             if book.isbn is not None:
#                 update_data["isbn"] = book.isbn
#             if book.title is not None:
#                 update_data["title"] = book.title
#             if book.author is not None:
#                 update_data["author"] = book.author
#             if book.year is not None:
#                 update_data["year"] = book.year
#             if book.availability is not None:
#                 update_data["availability"] = book.availability
#             self.db.book.update_one({"book_id": book_id}, {"$set": update_data})
#             self.db.book.find_one({"id": book_id})
#             return {"Book Updated "}
#         except Exception as e:
#             print(e)


#     def delete_user(self , user_id):
#         try:
#             user_details = self.db.user.find_one({"id": user_id})
#             if user_details:
#                 # if 'borrowed_books' in user_details:
#                 #     return_book(self, user_id, user_details['borrowed_books'])               
#                 self.db.user.delete_one(user_details)
#                 return {"User deleted successfully"}
#             else:
#                 return {"User not exists"}
#         except Exception as e:
#             print(e)
#             return {"error": str(e)}
        
#     def delete_book(self , book_id):
#         try:
#             book_details = self.db.book.find_one({"book_id": book_id})
#             if book_details:
#                 # if 'borrowed_books' in user_details:
#                 #     return_book(self, user_id, user_details['borrowed_books'])               
#                 self.db.book.delete_one(book_details)
#                 return {"Book deleted successfully"}
#             else:
#                 return {"Book not exists"}
#         except Exception as e:
#             print(e)
#             return {"error": str(e)}
        

#     def borrow_book(self , user_id, book_id):
#         try:
#             existing_user = self.db.user.find_one({"id": user_id})

#             if existing_user:
#                 existing_book = self.db.book.find_one({"book_id": book_id, "availability": {"$gt": 0}})

#                 if existing_book and existing_book['book_id'] not in existing_user["borrowed_books"]:
#                     self.db.book.update_one({"book_id": existing_book['book_id'], "availability": {"$gt": 0}}, {"$inc": {"availability": -1}})
#                     self.db.user.update_one({"id": user_id}, {"$addToSet": {"borrowed_books": existing_book['book_id']}})
#                     return {"Book borrowed successfully."}
#                 else:
#                     return {"Book not found or not available."}
#             else:
#                 return {"User not found."}
#         except Exception as e:
#              return {"Error updating book"}
        

#     def return_book(self , user_id, book_id):
#         try:
#             existing_user = self.db.user.find_one({"id": user_id})

#             if existing_user:
#                 existing_book = self.db.book.find_one({"book_id": book_id})

#                 if existing_book and existing_book['book_id']  in existing_user['borrowed_books']:
#                     self.db.book.update_one({"book_id": existing_book['book_id']}, {"$inc": {"availability": 1}})
#                     self.db.user.update_one({"id": user_id}, {"$unset": {"borrowed_books": existing_book['book_id']}})
#                     return {"Book returned successfully."}
#                 else:
#                     return {"Book not found or not available."}
#             else:
#                 return {"User not found."}
#         except Exception as e:
#             return {"Error updating book"}