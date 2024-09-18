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


@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/v1/data/duns/{dunsNumber}")
async def companyDetails(dunsNumber:str, blockIDs:str = Query(None)):
    if (blockIDs==None):
        return {"msg":"BlockIds missing"}
    elif(blockIDs.find("esg")!=-1):
        f = open('esginsight_L3_v1.json')
        return json.load(f)
    else:
        f = open('dataBlocks-sample (4).json')
        return json.load(f)

@app.get("/mappings")
async def mappings():
    return {
        "mappings":[
        {
            "Provider": "DnB",
            "API_URL": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L1_V1",
            "Attribute_path": "organization.primaryName",
            "provider_Attribute": "Company",
            "Data_type": "String"
        },
        {
            "Provider": "DnB",
            "API_URL": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L1_V1",
            "Attribute_path": "organization.registeredName",
            "provider_Attribute": "RegisteredName",
            "Data_type": "String"
        },
        {
            "Provider": "DnB",
            "API_URL": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L4_V1",
            "Attribute_path": "organization.websiteAddress[0].url",
            "provider_Attribute": "CorporateWebsite",
            "Data_type": "url"
        },
        {
            "Provider": "DnB",
            "API_URL": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_advgeoposition_V1",
            "Attribute_path": "oraganization.telephone[0].telephoneNumber",
            "provider_Attribute": "address.PhoneNumber",
            "Data_type": "Number"
        },
        {
            "Provider": "DnB",
            "API_URL": "v1/data/duns/{dunsNumber}?blockIDs=companyfinancials_L4_V2",
            "Attribute_path": "organization.otherFinancials[0].currency",
            "provider_Attribute": "Currency",
            "Data_type": "String"
        },
        {
            "Provider": "DnB",
            "API_URL": "v1/data/duns/{dunsNumber}?blockIDs=companyesgInsights_L4_V3",
            "Attribute_path": "organization.esgRanking.score",
            "provider_Attribute": "Score",
            "Data_type": "Number"
        }
    ]}


# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
