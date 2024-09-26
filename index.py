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
        "search_api_url":"search",
        "company_name_provider_attr":"organization.primaryName",
        "provider_attribute1":"organization.duns",
        "provider_attribute2":"organization.websiteAddress[0].url",
        "provider_attribute3":"organization.telephone[0].telephoneNumber",
        "provider_attribute4":None,
        "provider_attribute5":None
    }

@app.get("/autoSuggest")
async def autoSuggest():
    return [
    {
        "id": "5130efc38989846a360001f6",
        "object_type": "company",
        "name": "NetSuite",
        "slug": "netsuite",
        "url": "netsuite.com",
        "location": "Redwood City, CA",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/5130efc38989846a360001f6.ico"
    },
    {
        "id": "5130efec8989846a36007762",
        "object_type": "company",
        "name": "Dyn",
        "slug": "dyn",
        "url": "www.dyn.com",
        "location": "Manchester, NH",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/5130efec8989846a36007762.ico"
    },
    {
        "id": "541abb8356a990ca1c000508",
        "object_type": "company",
        "name": "Sedgwick",
        "slug": "sedgwick-1",
        "url": "www.sedgwick.com",
        "location": "Memphis, TN",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/541abb8356a990ca1c000508.ico"
    },
    {
        "id": "5254d1049f309cd30400013a",
        "object_type": "company",
        "name": "Oracle Lighting",
        "slug": "oracle-lighting",
        "url": "oraclelights.com",
        "location": "Metairie, LA",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/5254d1049f309cd30400013a.ico"
    },
    {
        "id": "5130f0248989846a3601359e",
        "object_type": "company",
        "name": "CrowdTwist",
        "slug": "crowdtwist",
        "url": "www.crowdtwist.com",
        "location": "New York, NY",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/5130f0248989846a3601359e.ico"
    },
    {
        "id": "5130f0598989846a3601e7a0",
        "object_type": "company",
        "name": "Moat",
        "slug": "moat",
        "url": "moat.com",
        "location": "New York, NY",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/5130f0598989846a3601e7a0.ico"
    },
    {
        "id": "58e22e3545930d2649ebd647",
        "object_type": "company",
        "name": "Oracle Corporation UK Limited",
        "slug": "oracle-corporation-uk-limited",
        "url": "www.oracle.com/uk",
        "location": "Reading, United Kingdom",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/58e22e3545930d2649ebd647.ico"
    }
]


@app.get("/v1/data/duns/{dunsNumber}")
async def companyDetails(dunsNumber:str, blockIDs:str = Query(None)):
    if (blockIDs==None):
        return {"msg":"BlockIds missing"}
    else:
        f = open('dataBlocks-sample (4).json')
        return json.load(f)

@app.get("/search")
async def mappings():
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
            "Attribute_path": "organization.duns",
            "provider_Attribute": "DUNSNumber",
            "Data_type": "Number"
        },
        {
            "Provider": "DnB",
            "API_URL": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L1_V1",
            "Attribute_path": "organization.primaryAddress.addressCountry.isoAlpha2Code",
            "provider_Attribute": "TaxpayerCountryCode",
            "Data_type": "Number"
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
            "Attribute_path": "organization.telephone[0].telephoneNumber",
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