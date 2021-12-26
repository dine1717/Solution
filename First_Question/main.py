import uvicorn
from ImageSimilarity import feat_img,calculate_similarity,feat_img_download
from typing import List

from fastapi import FastAPI, File, UploadFile,Form
from fastapi.responses import HTMLResponse

application=FastAPI()

@application.get('/')
def index():
    return {'message': 'Hello World'}


@application.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}

@application.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    
    files_upload=[file.filename for file in files]
    files_upload_1 = files_upload[0]
    files_upload_2 = files_upload[1]
    f1 = feat_img(files_upload_1)
    f2 = feat_img(files_upload_2)
    cosine_score = calculate_similarity(f1, f2)
    return {"Similarty Score", cosine_score }

@application.post("/uploadurls/")
async def create_upload_files(url1: str =Form(...), url2: str =Form(...)):
    
    
    urls_upload_1 = url1
    urls_upload_2 = url2
    
    f4_image =feat_img_download(urls_upload_1,"image1")
    f5_image =feat_img_download(urls_upload_2,"image2")
    
    f6 = feat_img(f4_image)
    f7 = feat_img(f5_image)
    cosine_score = calculate_similarity(f6, f7)
    return {"Similarty Score", cosine_score }




@application.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadurls/" enctype="multipart/form-data" method="post">
<input name="urls" type="url" multiple>
<input type="submit">
</form>

</body>
    """
    return HTMLResponse(content=content)


if __name__=='__main__':
    uvicorn.run(application,host='127.0.0.1',port=8000)
    