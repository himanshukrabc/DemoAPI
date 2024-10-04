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
        "provider_identifier":"dunsNumber",
        "search_candidates":"res.results"
    }


const companies=[
    {
        "id": "5130efc38989846a360001f6",
        "object_type": "company",
        "name": "NetSuite",
        "slug": "netsuite",
        "dunsNumber": "754235132",
        "url": "netsuite.com",
        "location": "Redwood City, CA",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/5130efc38989846a360001f6.ico"
    },
    {
        "id": "5130efc38989846a360001f6",
        "object_type": "company",
        "name": "Gorman",
        "slug": "Gorman",
        "dunsNumber": "804735132",
        "url": "gorman.com",
        "location": "Redwood City, CA",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/5130efc38989846a360001f6.ico"
    },
    {
        "id": "5130efec8989846a36007762",
        "object_type": "company",
        "name": "Dyn",
        "slug": "dyn",
        "dunsNumber": "213489712",
        "url": "www.dyn.com",
        "location": "Manchester, NH",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/5130efec8989846a36007762.ico"
    },
    {
        "id": "541abb8356a990ca1c000508",
        "object_type": "company",
        "name": "Sedgwick",
        "slug": "sedgwick-1",
        "dunsNumber": "239047824",
        "url": "www.sedgwick.com",
        "location": "Memphis, TN",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/541abb8356a990ca1c000508.ico"
    },
    {
        "id": "5254d1049f309cd30400013a",
        "object_type": "company",
        "name": "Oracle Lighting",
        "slug": "oracle-lighting",
        "dunsNumber": "345987533",
        "url": "oraclelights.com",
        "location": "Metairie, LA",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/5254d1049f309cd30400013a.ico"
    },
    {
        "id": "5130f0248989846a3601359e",
        "object_type": "company",
        "name": "CrowdTwist",
        "slug": "crowdtwist",
        "dunsNumber": "354198734",
        "url": "www.crowdtwist.com",
        "location": "New York, NY",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/5130f0248989846a3601359e.ico"
    },
    {
        "id": "5130f0598989846a3601e7a0",
        "object_type": "company",
        "name": "Moat",
        "slug": "moat",
        "dunsNumber": "135412344",
        "url": "moat.com",
        "location": "New York, NY",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/5130f0598989846a3601e7a0.ico"
    },
    {
        "id": "58e22e3545930d2649ebd647",
        "object_type": "company",
        "name": "Oracle Corporation UK Limited",
        "slug": "oracle-corporation-uk-limited",
        "dunsNumber": "234512342",
        "url": "www.oracle.com/uk",
        "location": "Reading, United Kingdom",
        "icon_url": "//axdprrulpfmh.compat.objectstorage.us-phoenix-1.oraclecloud.com/datafox-public-prod/favicons/58e22e3545930d2649ebd647.ico"
    }
]
@app.get("/autoSuggest")
async def autoSuggest(searchString:str = Query(None)):
    return {"res":{"results":
                   [val for val in companies if searchString in val['name']]}}


@app.get("/v1/data/duns/{dunsNumber}")
async def companyDetails(dunsNumber:str, blockIDs:str = Query(None)):
    if (blockIDs==None):
        return {"msg":"BlockIds missing"}
    else:
        f = open('dataBlocks-sample (4).json')
        return json.load(f)[dunsNumber]

@app.get("/search")
async def mappings():
    f = open('dataBlocks-sample (4).json')
    return json.load(f)

@app.get("/mappings")
async def mappings():
    return {
        "mappings":[
        {
            "mapping_id":1,
            "ext_data_provider_code": "DnB",
            "api_url": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L1_V1",
            "api_field_name": "organization.primaryName",
            "internal_reg_attribute": "Company",
            "supp_profile_attribute":"Y",
            "data_type": "String"
        },
        {
            "mapping_id":1,
            "ext_data_provider_code": "DnB",
            "api_url": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L1_V1",
            "api_field_name": "organization.duns",
            "internal_reg_attribute": "DUNSNumber",
            "supp_profile_attribute":"Y",
            "data_type": "Number"
        },
        {
            "mapping_id":1,
            "ext_data_provider_code": "DnB",
            "api_url": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L1_V1",
            "api_field_name": "organization.primaryAddress.addressCountry.isoAlpha2Code",
            "internal_reg_attribute": "TaxpayerCountryCode",
            "supp_profile_attribute":"Y",
            "data_type": "Number"
        },
        {
            "mapping_id":1,
            "ext_data_provider_code": "DnB",
            "api_url": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L1_V1",
            "api_field_name": "organization.registeredName",
            "internal_reg_attribute": "RegisteredName",
            "supp_profile_attribute":"Y",
            "data_type": "String"
        },
        {
            "mapping_id":1,
            "ext_data_provider_code": "DnB",
            "api_url": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_L4_V1",
            "api_field_name": "organization.websiteAddress[0].url",
            "internal_reg_attribute": "CorporateWebsite",
            "supp_profile_attribute":"Y",
            "data_type": "url"
        },
        {
            "mapping_id":1,
            "ext_data_provider_code": "DnB",
            "api_url": "v1/data/duns/{dunsNumber}?blockIDs=companyInfo_advgeoposition_V1",
            "api_field_name": "organization.telephone[0].telephoneNumber",
            "internal_reg_attribute": "address.PhoneNumber",
            "supp_profile_attribute":"Y",
            "data_type": "Number"
        },
        {
            "mapping_id":1,
            "ext_data_provider_code": "DnB",
            "api_url": "v1/data/duns/{dunsNumber}?blockIDs=companyfinancials_L4_V2",
            "api_field_name": "organization.otherFinancials[0].currency",
            "internal_reg_attribute": "Currency",
            "supp_profile_attribute":"Y",
            "data_type": "String"
        },
        {
            "mapping_id":1,
            "ext_data_provider_code": "DnB",
            "api_url": "v1/data/duns/{dunsNumber}?blockIDs=companyesgInsights_L4_V3",
            "api_field_name": "organization.esgRanking.score",
            "internal_reg_attribute": "Score",
            "supp_profile_attribute":"Y",
            "data_type": "Number",
        }
    ]}


# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

