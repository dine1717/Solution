import uvicorn,json
from typing import List

from fastapi import FastAPI,Form
from fastapi.responses import HTMLResponse
from main  import search
import pandas as pd



application=FastAPI()


@application.post("/enterquery/")
async def create_query(searchquery: str =Form(...)):
    
    
    urls_upload_1 = searchquery
    
    f4_data =search(urls_upload_1)
    #f4_data = pd.Data_Frame(f4_data)
    result = f4_data.to_json(orient="split")
    parsed = json.loads(result)
    parsed=json.dumps(parsed, indent=4) 
    
    return {"Similar Query", parsed }



@application.get("/")
async def main():
    content = """
<body>
</form>
<form action="/enterquery/" enctype="multipart/form-data" method="post">
<input name="search query" type="file" >
<input type="submit">
</form>

</body>
    """
    return HTMLResponse(content=content)