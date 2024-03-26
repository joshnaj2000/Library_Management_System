import mysql.connector
import logging



class Library():
    def __init__(self ):
        try:

            logging.basicConfig(level=logging.DEBUG , format='%(asctime)s - %(levelname)s - %(message)s' , filename="main.log" , filemode="w")

            self.db = mysql.connector.connect(
            host = "localhost",
            user="root",
            password = "Joshna@2000",
            database = "library"
        )
            self.mycursor = self.db.cursor()
            logging.info("Connection Successfull")
        except Exception as e:
            logging.exception("Exception Occured:{}".format(e))

    def close_connection(self):
        self.mycursor.close()
        self.db.close()
        logging.info("Connection Closed")