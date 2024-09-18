from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.get("/companyDetails")
async def companyDetails(request: Request):
    f = open('dataBlocks-sample (4).json')
    return json.load(f)

@app.get("/esgDetails")
async def esg(request: Request):
    f = open('esginsight_L3_v1.json')
    return json.load(f)

@app.get("/mappings")
async def mappings():
    return {
        "mappings":[
        {
            "Provider": "DnB",
            "API_URL": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L1_V1",
            "Attribute_path": "organization.primaryName",
            "provider_Attribute": "DnB Primary Name",
            "Data_type": "String"
        },
        {
            "Provider": "DnB",
            "API_URL": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L1_V1",
            "Attribute_path": "organization.registeredName",
            "provider_Attribute": "DnB Registered Name",
            "Data_type": "String"
        },
        {
            "Provider": "DnB",
            "API_URL": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L4_V1",
            "Attribute_path": "organization.websiteAddress[0].url",
            "provider_Attribute": "DnB Website",
            "Data_type": "url"
        },
        {
            "Provider": "DnB",
            "API_URL": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_advgeoposition_V1",
            "Attribute_path": "oraganization.telephone[type=\"phone\"]",
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
            "Attribute_path": "sum(organization.esgRanking.score)",
            "provider_Attribute": "Score",
            "Data_type": "Number"
        }
    ]}


# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
