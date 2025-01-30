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

@app.get("/EVData")
async def main(integration_id: str = Query(..., description="Integration ID")):
    if(integration_id=="\"Avian\""):
        return [
            {
                "integration_ids": [
                    "Avian"
                ],
                "extreme_string":"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula",
                "extreme_number":"12345678912345678900",
                "ev_supplier_name": "Avian",
                "client_supplier_name": "Avian",
                "parent_company": None,
                "vat_number": None,
                "tax_number": None,
                "siret_number": None,
                "active": True,
                "evid": "TJ374493",
                "city": None,
                "state": None,
                "country": "United States of America",
                "address_1": None,
                "address_2": None,
                "website": None,
                "isic_category": "Data processing, hosting and related activities; web portals",
                "employee_range": "100-499",
                "size": "M",
                "turnover": None,
                "risk_country": False,
                "supplier_contact_first_name": "@FirstName1",
                "supplier_contact_last_name": "@SupLast1",
                "supplier_contact_email": "email1@email.com",
                "supplier_contact_phone": "@Phone1",
                "campaign_name": "Ecovadis Demo Client Self-Registered BM1 2023",
                "campaign_type": "Standard",
                "rfp_campaign_icon": "",
                "current_stage": "Not under assessment",
                "progress_status": "Not under assessment",
                "sharing_status": "Accepted",
                "request_outcome": "Scorecard published",
                "current_stage_code": 6,
                "progress_status_code": 16,
                "sharing_status_code": 2,
                "request_outcome_code": 1,
                "source": "Invited",
                "launch_date": None,
                "deadline": "2024-01-10",
                "declined": False,
                "declined_date": None,
                "last_comment": "Scorecard published. Email notification sent to invited company.",
                "comment_date": "2023-12-05",
                "buyer_action": "No",
                "specific_comment": None,
                "buyer_last_contacted": None,
                "published_date": "2023-12-06",
                "status_last_update": "2022-10-04",
                "global_score": 60,
                "env_score": 60,
                "lab_score": 60,
                "fbp_score": 70,
                "sup_score": 40,
                "global_trend": "https://resources.ecovadis-survey.com/integrationapi/images/jn.gif",
                "env_trend": "https://resources.ecovadis-survey.com/integrationapi/images/C-C.gif",
                "lab_trend": "https://resources.ecovadis-survey.com/integrationapi/images/C-C.gif",
                "fbp_trend": "https://resources.ecovadis-survey.com/integrationapi/images/B-B.gif",
                "sup_trend": "https://resources.ecovadis-survey.com/integrationapi/images/D-D.gif",
                "scorecard_link": "https://integration.ecovadis-survey.com/?key=hgYFm5IwXFGKLk8k/P/ADOILbpw1P8FQMRUS6ExLknTINb8g7rkhAiWu1MobJwEqfXcbZ83M0s8SrQ1NXhqVYQ==",
                "expired": True,
                "documents_number": 6,
                "scope_change": False,
                "initial_requested_scope": None,
                "buyer_contact_first_name": "@BuyFirstName1",
                "buyer_contact_last_name": "@BuyLastName1",
                "buyer_contact_email": "buyer1@mail.com",
                "nb_flags": 1,
                "nb_client_filters": 4,
                "nb_integration_ids": 10,
                "nb_client_ca": 13,
                "nb_all_ca": 15,
                "nb_draft_ca": 0,
                "nb_requested_ca": 6,
                "nb_in_progress_ca": 0,
                "nb_rejected_ca": 0,
                "nb_completed_ca": 0,
                "nb_overdue_ca": 9,
                "nb_no_validation_ca": 15,
                "nb_not_validated_ca": 0,
                "nb_validated_ca": 0,
                "nb_closed_ca": 0,
                "next_deadline": "2025-02-02",
                "last_modification": "2024-07-18",
                "nb_documents": 0,
                "target_company_name": None,
                "target_company_country": None,
                "target_company_EVID": None,
                "target_progress_status": None,
                "target_progress_status_ID": None,
                "target_current_stage": None,
                "target_current_stage_ID": None,
                "target_request_outcome": None,
                "target_request_outcome_ID": None,
                "target_sharing_status": None,
                "target_sharing_status_ID": None,
                "target_global_score": None,
                "target_env_score": None,
                "target_lab_score": None,
                "target_fbp_score": None,
                "target_sup_score": None,
                "target_published_date": None,
                "target_scorecard_link": None
            }
        ]
    elif(integration_id =="\"Dell\""):
        return [
            {
                "integration_ids": [
                    "Dell"
                ],
                "extreme_string":"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula",
                "extreme_number":"12345678912345678900",
                "ev_supplier_name": "Dell",
                "client_supplier_name": "Dell",
                "parent_company": None,
                "vat_number": None,
                "tax_number": None,
                "siret_number": None,
                "active": True,
                "evid": "TJ374493",
                "city": None,
                "state": None,
                "country": "United States of America",
                "address_1": None,
                "address_2": None,
                "website": None,
                "isic_category": "Data processing, hosting and related activities; web portals",
                "employee_range": "100-499",
                "size": "M",
                "turnover": None,
                "risk_country": False,
                "supplier_contact_first_name": "@FirstName",
                "supplier_contact_last_name": "@SupLast",
                "supplier_contact_email": "email@email.com",
                "supplier_contact_phone": "@Phone",
                "campaign_name": "Ecovadis Demo Client Self-Registered BM1 2023",
                "campaign_type": "Standard",
                "rfp_campaign_icon": "",
                "current_stage": "Not under assessment",
                "progress_status": "Not under assessment",
                "sharing_status": "Accepted",
                "request_outcome": "Scorecard published",
                "current_stage_code": 6,
                "progress_status_code": 16,
                "sharing_status_code": 2,
                "request_outcome_code": 1,
                "source": "Invited",
                "launch_date": None,
                "deadline": "2024-01-10",
                "declined": False,
                "declined_date": None,
                "last_comment": "Scorecard published. Email notification sent to invited company.",
                "comment_date": "2023-12-05",
                "buyer_action": "No",
                "specific_comment": None,
                "buyer_last_contacted": None,
                "published_date": "2023-12-06",
                "status_last_update": "2022-10-04",
                "global_score": 60,
                "env_score": 60,
                "lab_score": 60,
                "fbp_score": 70,
                "sup_score": 40,
                "global_trend": "https://resources.ecovadis-survey.com/integrationapi/images/jn.gif",
                "env_trend": "https://resources.ecovadis-survey.com/integrationapi/images/C-C.gif",
                "lab_trend": "https://resources.ecovadis-survey.com/integrationapi/images/C-C.gif",
                "fbp_trend": "https://resources.ecovadis-survey.com/integrationapi/images/B-B.gif",
                "sup_trend": "https://resources.ecovadis-survey.com/integrationapi/images/D-D.gif",
                "scorecard_link": "https://integration.ecovadis-survey.com/?key=hgYFm5IwXFGKLk8k/P/ADOILbpw1P8FQMRUS6ExLknTINb8g7rkhAiWu1MobJwEqfXcbZ83M0s8SrQ1NXhqVYQ==",
                "expired": True,
                "documents_number": 6,
                "scope_change": False,
                "initial_requested_scope": None,
                "buyer_contact_first_name": "@BuyFirstName",
                "buyer_contact_last_name": "@BuyLastName",
                "buyer_contact_email": "buyer@mail.com",
                "nb_flags": 1,
                "nb_client_filters": 4,
                "nb_integration_ids": 10,
                "nb_client_ca": 13,
                "nb_all_ca": 15,
                "nb_draft_ca": 0,
                "nb_requested_ca": 6,
                "nb_in_progress_ca": 0,
                "nb_rejected_ca": 0,
                "nb_completed_ca": 0,
                "nb_overdue_ca": 9,
                "nb_no_validation_ca": 15,
                "nb_not_validated_ca": 0,
                "nb_validated_ca": 0,
                "nb_closed_ca": 0,
                "next_deadline": "2025-02-02",
                "last_modification": "2024-07-18",
                "nb_documents": 0,
                "target_company_name": None,
                "target_company_country": None,
                "target_company_EVID": None,
                "target_progress_status": None,
                "target_progress_status_ID": None,
                "target_current_stage": None,
                "target_current_stage_ID": None,
                "target_request_outcome": None,
                "target_request_outcome_ID": None,
                "target_sharing_status": None,
                "target_sharing_status_ID": None,
                "target_global_score": None,
                "target_env_score": None,
                "target_lab_score": None,
                "target_fbp_score": None,
                "target_sup_score": None,
                "target_published_date": None,
                "target_scorecard_link": None
            }
        ]
    else:
        return [
            {
                "integration_ids": [
                    "12351235"
                ],
                "extreme_string":"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula",
                "extreme_number":"12345678912345678900",
                "ev_supplier_name": "Microsoft",
                "client_supplier_name": "Microsoft",
                "parent_company": None,
                "vat_number": None,
                "tax_number": None,
                "siret_number": None,
                "active": True,
                "evid": "LB208766",
                "city": None,
                "state": "BERGAMO",
                "country": "Italy",
                "address_1": None,
                "address_2": None,
                "website": None,
                "isic_category": "Manufacture of basic pharmaceutical products and pharmaceutical preparations",
                "employee_range": "500-999",
                "size": "M",
                "turnover": None,
                "risk_country": False,
                "supplier_contact_first_name": "@FirstName",
                "supplier_contact_last_name": "@SupLast",
                "supplier_contact_email": "email@email.com",
                "supplier_contact_phone": "@Phone",
                "campaign_name": "IQ Directory Invitation 2024 for Sector Initiative EcoVadis Dummy Sector Initiative",
                "campaign_type": "Standard",
                "rfp_campaign_icon": "",
                "current_stage": "Questionnaire (not my company`s request)",
                "progress_status": "Answering",
                "sharing_status": "Accepted",
                "request_outcome": "Sharing request accepted",
                "current_stage_code": 7,
                "progress_status_code": 6,
                "sharing_status_code": 2,
                "request_outcome_code": 6,
                "source": "Invited",
                "launch_date": None,
                "deadline": "2024-12-06",
                "declined": False,
                "declined_date": None,
                "last_comment": None,
                "comment_date": None,
                "buyer_action": "No",
                "specific_comment": None,
                "buyer_last_contacted": None,
                "published_date": "2023-11-15",
                "status_last_update": "2024-10-25",
                "global_score": 83,
                "env_score": 90,
                "lab_score": 80,
                "fbp_score": 80,
                "sup_score": 80,
                "global_trend": "https://resources.ecovadis-survey.com/integrationapi/images/vh.gif",
                "env_trend": "https://resources.ecovadis-survey.com/integrationapi/images/A-plus.gif",
                "lab_trend": "https://resources.ecovadis-survey.com/integrationapi/images/B-B.gif",
                "fbp_trend": "https://resources.ecovadis-survey.com/integrationapi/images/B-A.gif",
                "sup_trend": "https://resources.ecovadis-survey.com/integrationapi/images/B-A.gif",
                "scorecard_link": "https://integration.ecovadis-survey.com/?key=hgYFm5IwXFGKLk8k/P/ADOILbpw1P8FQMRUS6ExLknTnUGhCbyez+BhOerNV+TecU+nGivL/ilg3ZTSXMA8Ihw==",
                "expired": True,
                "documents_number": 145,
                "scope_change": False,
                "initial_requested_scope": None,
                "buyer_contact_first_name": "@BuyFirstName",
                "buyer_contact_last_name": "@BuyLastName",
                "buyer_contact_email": "buyer@mail.com",
                "nb_flags": 1,
                "nb_client_filters": 0,
                "nb_integration_ids": 1,
                "nb_client_ca": 0,
                "nb_all_ca": 0,
                "nb_draft_ca": 0,
                "nb_requested_ca": 0,
                "nb_in_progress_ca": 0,
                "nb_rejected_ca": 0,
                "nb_completed_ca": 0,
                "nb_overdue_ca": 0,
                "nb_no_validation_ca": 0,
                "nb_not_validated_ca": 0,
                "nb_validated_ca": 0,
                "nb_closed_ca": 0,
                "next_deadline": None,
                "last_modification": None,
                "nb_documents": 0,
                "target_company_name": None,
                "target_company_country": None,
                "target_company_EVID": None,
                "target_progress_status": None,
                "target_progress_status_ID": None,
                "target_current_stage": None,
                "target_current_stage_ID": None,
                "target_request_outcome": None,
                "target_request_outcome_ID": None,
                "target_sharing_status": None,
                "target_sharing_status_ID": None,
                "target_global_score": None,
                "target_env_score": None,
                "target_lab_score": None,
                "target_fbp_score": None,
                "target_sup_score": None,
                "target_published_date": None,
                "target_scorecard_link": None
            }
        ]
        

@app.get("/dataProviders")
async def dataProviders():
    return {
        "ext_data_provider_id":101,
        "ext_data_provider_code":"DNB",
        "ext_data_provider_name":"Dun and Bradstreet",
        "primary_flag":"Y",
        "enabled_flag":"Y",
        "search_api_url":"autoSuggest",
        "company_name_provider_attr":"organization.primaryName",
        "provider_attribute1":"organization.iconUrl",
        "provider_attribute2":"organization.duns",
        "provider_attribute3":"organization.primaryAddress.addressRegion.name",
        "provider_attribute4":None,
        "provider_attribute5":None,
        "provider_identifier":"organization.duns",
        "search_candidates":"searchCandidates"
    }


@app.get("/autoSuggest")
async def autoSuggest(searchText: str = Query(None)):
    f = open('companies.json')
    companies=json.load(f)["comp"]
    if searchText:
        searchText = searchText.lower() 
        res = [val for val in companies if searchText in val['organization']['primaryName'].lower()]
        return {
            "transactionDetail": {
                "transactionID": "rrt-051d25cbd8f15f5a9-b-ea-20648-54309783-3",
                "transactionTimestamp": "2018-02-28T17:11:06.454Z",
                "inLanguage": "en-US",
                "serviceVersion": "1"
            },
            "inquiryDetail": {
                "countryISOAlpha2Code": "US",
                "searchTerm": "Gor"
            },
            "candidatesReturnedQuantity": 2,
            "candidatesMatchedQuantity": 23,
            "searchCandidates": res
        }
    else:
        return {
            "transactionDetail": {
                "transactionID": "rrt-051d25cbd8f15f5a9-b-ea-20648-54309783-3",
                "transactionTimestamp": "2018-02-28T17:11:06.454Z",
                "inLanguage": "en-US",
                "serviceVersion": "1"
            },
            "inquiryDetail": {
                "countryISOAlpha2Code": "US",
                "searchTerm": "Gor"
            },
            "candidatesReturnedQuantity": 2,
            "candidatesMatchedQuantity": 23,
            "searchCandidates": []
        }

@app.get("/v1/data/duns/{dunsNumber}")
async def companyDetails(dunsNumber:str, blockIDs:str = Query(None)):
    if (blockIDs==None):
        return {"msg":"BlockIds missing"}
    else:
        f = open('dataBlocks-sample.json')
        return json.load(f)[dunsNumber]

@app.get("/search={searchText}")
async def getSearchRes(searchText: str):
    res = [
        {"logo":"https://logotyp.us/file/oracle.svg","companyName": "Oracle Corporation", "address": "2300 Oracle Way Austin, TX, 78741-1400 United States", "website": "https://www.oracle.com/", "dunsNumber": "144709193"},
        {"logo":"https://logotyp.us/file/oracle.svg","companyName": "ORACLE EMEA LIMITED", "address": "EAST POINT BUSINESS PARK FAIRVIEW DUBLIN, 3 Ireland", "website": "https://www.oracle.com/", "dunsNumber": "238480123"},
        {"logo":"https://logotyp.us/file/oracle.svg","companyName": "ORACLE SYSTEMS LIMITED", "address": "Floor 2, 58 Akropoleos Strovolos, 2012 Cyprus", "website": "http://www.oracle.com/", "dunsNumber": "356990528"},
        {"logo":"https://logotyp.us/file/oracle.svg","companyName": "ORACLE CAPAC SERVICES UNLIMITED COMPANY", "address": "EASTPOINT BUSINESS PARK FAIRVIEW DUBLIN 3, DO3 E8N6 Ireland", "website": "http://www.oracle.com/", "dunsNumber": "896728230"},
        {"logo":"https://logotyp.us/file/oracle.svg","companyName": "Oracle America, Inc.", "address": "500 Oracle Pkwy Redwood City, CA, 94065-1677 United States", "website": "http://www.oracle.com/", "dunsNumber": "13044532"},
        {"logo":"https://logotyp.us/file/oracle.svg","companyName": "ORACLE INDIA PRIVATE LIMITED", "address": "One Horizon Center, Levels 7, 8 and 9, DLF City V, Sector 43, Gurugram, Haryana, 122003 India", "website": "http://www.oracle.com/", "dunsNumber": "862165896"},
        {"logo":"https://logotyp.us/file/oracle.svg","companyName": "ORACLE CORPORATION UK LIMITED", "address": "ORACLE PARKWAY, THAMES VALLEY PARK (TVP) READING, RG6 1RA United Kingdom", "website": "http://www.oracle.com/", "dunsNumber": "291601524"},
        {"logo":"https://logotyp.us/file/oracle.svg","companyName": "ORACLE CORPORATION JAPAN", "address": "2-5-8, KITAAOYAMA ORAKURUAOYAMASENTA- MINATO-KU, TOKYO, 107-0061 Japan", "website": "http://www.oracle.com/jp/", "dunsNumber": "692770886"},
        {"logo":"https://logotyp.us/file/oracle.svg","companyName": "ORACLE CONSOLIDATION ALSTRALIA DTV ITO", "address": "4 Julius Ave North Ryde, NEW SOUTH WALES, 2113 Australia", "website": "http://www.oracle.com/", "dunsNumber": "753586882"},
        {"logo":"https://logotyp.us/file/oracle.svg","companyName": "ORACLE FRANCE", "address": "15 BD CHARLES DE GAULLE 92715, COLOMBES CEDEX, ILE DE FRANCE France", "website": "http://www.oracle.com/", "dunsNumber": "391129939"},
    ]
    
    result = [c for c in res if searchText.lower() in c['companyName'].lower()]
    
    print(result)
    return result

@app.get("/supplier/{dunsNumber}")
async def getSupp(dunsNumber : str):
    obj = {"13044532":{"Company":"Oracle America, Inc.","DUNS":"13044532","Website":"https://www.oracle.com/","Country":"US","TaxpayerID":"631-602-703","PrimaryIndustryCode":174,"NumberOfEmployees":46800,"RiskScore":"2","ComplianceScore":"2","OnGovtSanctionList":"No"},"144709193":{"Company":"Oracle Corporation","DUNS":"144709193","Website":"https://www.oracle.com/","Country":"US","TaxpayerID":"315-116-367","PrimaryIndustryCode":8781,"NumberOfEmployees":14900,"RiskScore":"2","ComplianceScore":"2","OnGovtSanctionList":"No"},"238480123":{"Company":"ORACLE EMEA LIMITED","DUNS":"238480123","Website":"https://www.oracle.com/","Country":"US","TaxpayerID":"23-657-805","PrimaryIndustryCode":342,"NumberOfEmployees":98300,"RiskScore":"2","ComplianceScore":"2","OnGovtSanctionList":"No"},"291601524":{"Company":"ORACLE CORPORATION UK LIMITED","DUNS":"291601524","Website":"https://www.oracle.com/","Country":"US","TaxpayerID":"265-990-656","PrimaryIndustryCode":7454,"NumberOfEmployees":80100,"RiskScore":"2","ComplianceScore":"2","OnGovtSanctionList":"No"},"356990528":{"Company":"ORACLE SYSTEMS LIMITED","DUNS":"356990528","Website":"https://www.oracle.com/","Country":"US","TaxpayerID":"312-809-222","PrimaryIndustryCode":9433,"NumberOfEmployees":4000,"RiskScore":"2","ComplianceScore":"2","OnGovtSanctionList":"No"},"391129939":{"Company":"ORACLE FRANCE","DUNS":"391129939","Website":"https://www.oracle.com/","Country":"US","TaxpayerID":"971-787-824","PrimaryIndustryCode":1944,"NumberOfEmployees":91600,"RiskScore":"2","ComplianceScore":"2","OnGovtSanctionList":"No"},"692770886":{"Company":"ORACLE CORPORATION JAPAN","DUNS":"692770886","Website":"https://www.oracle.com/","Country":"US","TaxpayerID":"537-57-985","PrimaryIndustryCode":5600,"NumberOfEmployees":11700,"RiskScore":"2","ComplianceScore":"2","OnGovtSanctionList":"No"},"753586882":{"Company":"ORACLE CONSOLIDATION ALSTRALIA DTV ITO","DUNS":"753586882","Website":"https://www.oracle.com/","Country":"US","TaxpayerID":"210-179-85","PrimaryIndustryCode":5221,"NumberOfEmployees":57800,"RiskScore":"2","ComplianceScore":"2","OnGovtSanctionList":"No"},"862165896":{"Company":"ORACLE INDIA PRIVATE LIMITED","DUNS":"862165896","Website":"https://www.oracle.com/","Country":"US","TaxpayerID":"348-807-151","PrimaryIndustryCode":318,"NumberOfEmployees":19700,"RiskScore":"2","ComplianceScore":"2","OnGovtSanctionList":"No"},
           "896728230":{"Company":"ORACLE CAPAC SERVICES UNLIMITED COMPANY","DUNS":"896728230","Website":"https://www.oracle.com/","Country":"US","TaxpayerID":"661-135-870","PrimaryIndustryCode":5402,"NumberOfEmployees":24300,"RiskScore":"2","ComplianceScore":"2","OnGovtSanctionList":"No"}}
    print(obj.keys())
    if dunsNumber in obj.keys():
        return obj[dunsNumber]
    else:
        return obj["13044532"]

@app.get("/mappings")
async def mappings():
    f = open('mappings.json')
    return json.load(f)

# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
