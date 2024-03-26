


import logging
from fastapi import FastAPI
from scripts.core.services.mongo_services import mongo_service_router
from scripts.core.services.sql_services import sql_service_router
# import uvicorn
# import webbrowser
app = FastAPI()

logger = logging.getLogger(__name__)

app.include_router(mongo_service_router, prefix="/mongo", tags=["mongo"])

app.include_router(sql_service_router,prefix="/sql" , tags=["sql"])


# if __name__=="__main__":
#     uvicorn.run("main:app" , port=8000,log_level="debug" , reload=True)
#     webbrowser.open("http://localhost:8000") 

