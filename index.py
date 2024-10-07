from fastapi import FastAPI, Request,Query
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/token")
async def main(req:Request):
    headers = req.headers
    print("Headers:", headers)

    body = await req.body()
    print("Body:", body.decode('utf-8'))  # Decoding from bytes to string

    return {"message": "Hello World"}

@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/dataProviders")
async def dataProviders():
    return {
        "ext_data_provider_id":101,
        "ext_data_provider_code":"DNB",
        "ext_data_provider_name":"Dun and Bradstreet",
        "primary_flag":"Y",
        "enabled_flag":"Y",
        "search_api_url":"autoSuggest",
        "company_name_provider_attr":"name",
        "provider_attribute1":"icon_url",
        "provider_attribute2":"url",
        "provider_attribute3":"location",
        "provider_attribute4":None,
        "provider_attribute5":None,
        "provider_identifier":"DUNSNumber",
        "search_candidates":"res.results"
    }


@app.get("/autoSuggest")
async def autoSuggest(searchText: str = Query(None)):
    f = open('companies.json')
    companies=json.load(f)["comp"]
    if searchText:
        searchText = searchText.lower() 
        res = [val for val in companies if searchText in val['name'].lower()]
        return {"res": {"results": res}}
    else:
        return {"res": {"results": []}}

@app.get("/v1/data/duns/{dunsNumber}")
async def companyDetails(dunsNumber:str, blockIDs:str = Query(None)):
    if (blockIDs==None):
        return {"msg":"BlockIds missing"}
    else:
        f = open('dataBlocks-sample (4).json')
        return json.load(f)[dunsNumber]


@app.get("/mappings")
async def mappings():
    f = open('mappings.json')
    return json.load(f)

# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

