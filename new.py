
companies=[
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
print([val for val in companies if "ora" in val['name']])