Scraper for PH Election Results 2025
-----------------------------------

[Work-in-progress]

# Navigating the Available Regions, Election Results, and their URIs

Overview:
```
Category Code 0 (Top-level)
|-> Category Code 2
      (Regions / Overseas Voter Types)
      |-> Category Code 3
            (Provinces / Global Regions)
            |-> Category Code 4
               (Municipalities / Countries)
               |-> Category Code 5
                     (Baranggays / Jurisdictions)
                     |-> Category Code null
                           (Precinct-level Election Results)
```

## Category Code 0: Top-level

Returns a JSON object of regions within.

### `local`
URL: [https://2025electionresults.comelec.gov.ph/data/regions/local/0.json](https://2025electionresults.comelec.gov.ph/data/regions/local/0.json)

<details>
<summary>Sample Results (click to expand)</summary>

```
{
   "regions":[
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"9706000",
         "name":"BARMM / RBOC"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R001000",
         "name":"REGION I"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R002000",
         "name":"REGION II"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R003000",
         "name":"REGION III"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R005000",
         "name":"REGION V"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R006000",
         "name":"REGION VI"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R007000",
         "name":"REGION VII"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R008000",
         "name":"REGION VIII"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R009000",
         "name":"REGION IX"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R00LAV0",
         "name":"LAV"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R00NIR0",
         "name":"NIR"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R010000",
         "name":"REGION X"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R011000",
         "name":"REGION XI"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R012000",
         "name":"REGION XII"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R013000",
         "name":"REGION XIII"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R04A000",
         "name":"REGION IV-A"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R04B000",
         "name":"REGION IV-B"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R0BARMM",
         "name":"BARMM"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R0CAR00",
         "name":"CORDILLERA ADMINISTRATIVE REGION"
      },
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R0NCR00",
         "name":"NATIONAL CAPITAL REGION"
      }
   ]
}
```
</details>


### `overseas`
URL: [https://2025electionresults.comelec.gov.ph/data/regions/overseas/0.json](https://2025electionresults.comelec.gov.ph/data/regions/overseas/0.json)

<details>
<summary>Sample Results (click to expand)</summary>

```
{
   "regions":[
      {
         "categoryCode":"2",
         "masterCode":"0",
         "code":"R0OAV00",
         "name":"OAV"
      }
   ]
}
```
</details>

## Category Code 2: Regions / Overseas Voter Types
**Local top-level**: Returns a JSON object of provinces within the region with specified `code`.

**Overseas top-level**: Returns a JSON object of global regions belonging to the overseas voter type with specified `code`. As of writing, only the Overseas Absentee Voters (OAV) type is available.

### URL Structure:
https://2025electionresults.comelec.gov.ph/data/regions/_<`top-level-region`>_/_<`code`>_.json

* _<`top-level-region`>_: e.g. `local` or `overseas`
* _<`code`>_: from the JSON object obtained from the category code 0 response, e.g. `R04A000`

### Local Example:
[https://2025electionresults.comelec.gov.ph/data/regions/local/R04A000.json](https://2025electionresults.comelec.gov.ph/data/regions/local/R04A000.json)

<details>
<summary>Sample Local Results (click to expand)</summary>

```
{
   "regions":[
      {
         "categoryCode":"3",
         "masterCode":"R04A000",
         "code":"1000000",
         "name":"BATANGAS"
      },
      {
         "categoryCode":"3",
         "masterCode":"R04A000",
         "code":"2100000",
         "name":"CAVITE"
      },
      {
         "categoryCode":"3",
         "masterCode":"R04A000",
         "code":"3400000",
         "name":"LAGUNA"
      },
      {
         "categoryCode":"3",
         "masterCode":"R04A000",
         "code":"5600000",
         "name":"QUEZON"
      },
      {
         "categoryCode":"3",
         "masterCode":"R04A000",
         "code":"5800000",
         "name":"RIZAL"
      }
   ]
}
```
</details>

### Overseas Example:
[https://2025electionresults.comelec.gov.ph/data/regions/overseas/R0OAV00.json](https://2025electionresults.comelec.gov.ph/data/regions/overseas/R0OAV00.json)

<details>
<summary>Sample Overseas Results (click to expand)</summary>

```
{
   "regions":[
      {
         "categoryCode":"3",
         "masterCode":"R0OAV00",
         "code":"9000000",
         "name":"ASIA PACIFIC"
      },
      {
         "categoryCode":"3",
         "masterCode":"R0OAV00",
         "code":"9100000",
         "name":"NORTH AND LATIN AMERICAS"
      },
      {
         "categoryCode":"3",
         "masterCode":"R0OAV00",
         "code":"9200000",
         "name":"MIDDLE EAST AND AFRICAS"
      },
      {
         "categoryCode":"3",
         "masterCode":"R0OAV00",
         "code":"9300000",
         "name":"EUROPE"
      }
   ]
}
```
</details>

## Category Code 3: Provinces / Global Regions
**Local**: Returns a JSON object of municipalities within the province with specified `code`.

**Global**: Returns a JSON object of countries within the global region with specified `code`.

### URL:
https://2025electionresults.comelec.gov.ph/data/regions/_<`top-level-region`>_/_<`code`>_.json

* _<`top-level-region`>_: e.g. `local` or `overseas`
* _<`code`>_: from the JSON object obtained from the category code 2 response, e.g. `3400000`

### Local Example:
[https://2025electionresults.comelec.gov.ph/data/regions/local/3400000.json](https://2025electionresults.comelec.gov.ph/data/regions/local/3400000.json)

<details>
<summary>Sample Results (click to expand)</summary>

```
{
   "regions":[
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3401000",
         "name":"ALAMINOS"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3402000",
         "name":"BAY"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3403000",
         "name":"CITY OF BIÑAN"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3404000",
         "name":"CITY OF CABUYAO"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3405000",
         "name":"CITY OF CALAMBA"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3406000",
         "name":"CALAUAN"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3407000",
         "name":"CAVINTI"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3408000",
         "name":"FAMY"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3409000",
         "name":"KALAYAAN"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3410000",
         "name":"LILIW"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3411000",
         "name":"LOS BAÑOS"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3412000",
         "name":"LUISIANA"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3413000",
         "name":"LUMBAN"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3414000",
         "name":"MABITAC"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3415000",
         "name":"MAGDALENA"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3416000",
         "name":"MAJAYJAY"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3417000",
         "name":"NAGCARLAN"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3418000",
         "name":"PAETE"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3419000",
         "name":"PAGSANJAN"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3420000",
         "name":"PAKIL"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3421000",
         "name":"PANGIL"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3422000",
         "name":"PILA"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3423000",
         "name":"RIZAL"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3424000",
         "name":"CITY OF SAN PABLO"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3425000",
         "name":"CITY OF SAN PEDRO"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3426000",
         "name":"SANTA CRUZ"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3427000",
         "name":"SANTA MARIA"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3428000",
         "name":"CITY OF SANTA ROSA"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3429000",
         "name":"SINILOAN"
      },
      {
         "categoryCode":"4",
         "masterCode":"3400000",
         "code":"3430000",
         "name":"VICTORIA"
      }
   ]
}
```
</details>

### Overseas Example:
[https://2025electionresults.comelec.gov.ph/data/regions/overseas/9300000.json](https://2025electionresults.comelec.gov.ph/data/regions/overseas/9300000.json)

<details>
<summary>Sample Results (click to expand)</summary>

```
{
   "regions":[
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9301000",
         "name":"TÜRKIYE"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9302000",
         "name":"GREECE"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9303000",
         "name":"GERMANY"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9304000",
         "name":"SWITZERLAND"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9305000",
         "name":"BELGUIM"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9306000",
         "name":"HUNGARY"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9307000",
         "name":"DENMARK"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9308000",
         "name":"PORTUGAL"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9309000",
         "name":"UNITED KINGDOM OF GREAT BRITAIN"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9310000",
         "name":"SPAIN"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9311000",
         "name":"RUSSIA"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9312000",
         "name":"NORWAY"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9313000",
         "name":"FRANCE"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9314000",
         "name":"CZECH REPUBLIC"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9315000",
         "name":"ITALY"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9316000",
         "name":"SWEDEN"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9317000",
         "name":"THE NETHERLANDS"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9318000",
         "name":"HOLY SEE"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9319000",
         "name":"AUSTRIA"
      },
      {
         "categoryCode":"4",
         "masterCode":"9300000",
         "code":"9320000",
         "name":"POLAND"
      }
   ]
}
```
</details>

## Category Code 4: Municipalities / Countries
**Local**: Returns a JSON object of baranggays within the municipality with specified `code`.

**Overseas**: Returns a JSON object of jurisdictions within the country with specified `code`.

### URL:
https://2025electionresults.comelec.gov.ph/data/regions/_<`top-level-region`>_/_<`code`>_.json

* _<`top-level-region`>_: e.g. `local` or `overseas`
* _<`code`>_: from the JSON object obtained from the category code 3 response, e.g. `3403000`

### Local Example:
[https://2025electionresults.comelec.gov.ph/data/regions/local/3403000.json](https://2025electionresults.comelec.gov.ph/data/regions/local/3403000.json)
<details>
<summary>Sample Results (click to expand)</summary>

```
{
   "regions":[
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403001",
         "name":"BIÑAN"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403002",
         "name":"BUNGAHAN"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403003",
         "name":"SANTO TOMAS"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403004",
         "name":"CANLALAY"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403005",
         "name":"CASILE"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403006",
         "name":"DE LA PAZ"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403007",
         "name":"GANADO"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403008",
         "name":"SAN FRANCISCO"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403009",
         "name":"LANGKIWA"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403011",
         "name":"LOMA"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403012",
         "name":"MALABAN"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403013",
         "name":"MALAMIG"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403014",
         "name":"MAMPALASAN"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403015",
         "name":"PLATERO"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403016",
         "name":"POBLACION"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403018",
         "name":"SANTO NIÑO"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403019",
         "name":"SAN ANTONIO"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403020",
         "name":"SAN JOSE"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403021",
         "name":"SAN VICENTE"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403022",
         "name":"SORO-SORO"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403023",
         "name":"SANTO DOMINGO"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403024",
         "name":"TIMBAO"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403025",
         "name":"TUBIGAN"
      },
      {
         "categoryCode":"5",
         "masterCode":"3403000",
         "code":"3403026",
         "name":"ZAPOTE"
      }
   ]
}
```
</details>

### Overseas Example:
[https://2025electionresults.comelec.gov.ph/data/regions/overseas/9315000.json](https://2025electionresults.comelec.gov.ph/data/regions/overseas/9315000.json)
<details>
<summary>Sample Results (click to expand)</summary>

```
{
   "regions":[
      {
         "categoryCode":"5",
         "masterCode":"9315000",
         "code":"9315001",
         "name":"ROME PE"
      },
      {
         "categoryCode":"5",
         "masterCode":"9315000",
         "code":"9315005",
         "name":"MILAN PCG"
      }
   ]
}
```
</details>

## Category Code 5: Baranggays / Jurisdictions
**Local**: Returns a JSON object of the precincts within the baranggay with specified `code`.

**Overseas**: Returns a JSON object of the precincts within the jurisdiction with specified `code`.

### URL:
https://2025electionresults.comelec.gov.ph/data/regions/precinct/_<`first_2_characters_of_code`>_/_<`code`>_.json

* _<`code`>_: from the JSON object obtained from the category 4 response, e.g. `3403008`
* _<`first_2_characters_of_code`>_: e.g. `34`

### Local Example:
[https://2025electionresults.comelec.gov.ph/data/regions/precinct/34/3403008.json](https://2025electionresults.comelec.gov.ph/data/regions/precinct/34/3403008.json)
<details>
<summary>Sample Results (click to expand)</summary>

```
{
   "regions":[
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030158",
         "name":"34030158"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030159",
         "name":"34030159"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030160",
         "name":"34030160"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030161",
         "name":"34030161"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030162",
         "name":"34030162"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030163",
         "name":"34030163"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030164",
         "name":"34030164"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030165",
         "name":"34030165"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030166",
         "name":"34030166"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030167",
         "name":"34030167"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030168",
         "name":"34030168"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030169",
         "name":"34030169"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030170",
         "name":"34030170"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030171",
         "name":"34030171"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030172",
         "name":"34030172"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030173",
         "name":"34030173"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030174",
         "name":"34030174"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030175",
         "name":"34030175"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030176",
         "name":"34030176"
      },
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"34030177",
         "name":"34030177"
      }
   ]
}
```
</details>

### Overseas Example:
[https://2025electionresults.comelec.gov.ph/data/regions/precinct/93/9315005.json](https://2025electionresults.comelec.gov.ph/data/regions/precinct/93/9315005.json)
<details>
<summary>Sample Results (click to expand)</summary>

```
{
   "regions":[
      {
         "categoryCode":null,
         "masterCode":null,
         "code":"93150005",
         "name":"93150005"
      }
   ]
}
```
</details>

## Category Code null: Precinct-level Election Results
### URL:
https://2025electionresults.comelec.gov.ph/data/er/_<`first_3_characters_of_code`>_/_<`code`>_.json

* _<`code`>_: from the JSON object obtained from the category code 5 response, e.g. `34030158`
* _<`first_3_characters_of_code`>_: e.g. `340`

### Example:
[https://2025electionresults.comelec.gov.ph/data/er/340/34030158.json](https://2025electionresults.comelec.gov.ph/data/er/340/34030158.json)
<details>
<summary>Sample Results (click to expand)</summary>

```
{
   "totalErReceived":100.0,
   "information":{
      "machineId":"34030158",
      "location":"REGION IV-A, LAGUNA, CITY OF BIÑAN, SAN FRANCISCO",
      "votingCenter":"SILMER VILLAGE, BARANGAY SAN FRANCISCO",
      "precinctId":"34030158",
      "precinctInCluster":"0115A, 0115B, 0115C, 0115D",
      "abstentions":0,
      "numberOfRegisteredVoters":748,
      "numberOfActuallyVoters":506,
      "numberOfValidBallot":506,
      "turnout":67.65
   },
   "national":[
      {
         "contestCode":"00399000",
         "contestName":"SENATOR of PHILIPPINES",
         "statistic":{
            "overVotes":144,
            "underVotes":1116,
            "validVotes":8976,
            "obtainedVotes":4812
         },
         "candidates":{
            "candidates":[
               {
                  "name":"1. ABALOS, BENHUR (PFP)",
                  "votes":175,
                  "percentage":3.64
               },
               {
                  "name":"2. ADONIS, JEROME (MKBYN)",
                  "votes":5,
                  "percentage":0.1
               },
               {
                  "name":"3. AMAD, WILSON (IND)",
                  "votes":6,
                  "percentage":0.12
               },
               {
                  "name":"4. ANDAMO, NARS ALYN (MKBYN)",
                  "votes":9,
                  "percentage":0.19
               },
               {
                  "name":"5. AQUINO, BAM (KNP)",
                  "votes":328,
                  "percentage":6.82
               },
               {
                  "name":"6. ARAMBULO, RONNEL (MKBYN)",
                  "votes":61,
                  "percentage":1.27
               },
               {
                  "name":"7. ARELLANO, ERNESTO (KTPNAN)",
                  "votes":4,
                  "percentage":0.08
               },
               {
                  "name":"8. BALLON, ROBERTO (IND)",
                  "votes":43,
                  "percentage":0.89
               },
               {
                  "name":"9. BINAY, ABBY (NPC)",
                  "votes":145,
                  "percentage":3.01
               },
               {
                  "name":"10. BONDOC, JIMMY (PDPLBN)",
                  "votes":77,
                  "percentage":1.6
               },
               {
                  "name":"11. BONG REVILLA,RAMON, JR.(LAKAS)",
                  "votes":49,
                  "percentage":1.02
               },
               {
                  "name":"12. BOSITA, COLONEL (IND)",
                  "votes":166,
                  "percentage":3.45
               },
               {
                  "name":"13. BROSAS, ARLENE (MKBYN)",
                  "votes":98,
                  "percentage":2.04
               },
               {
                  "name":"14. CABONEGRO, ROY (DPP)",
                  "votes":1,
                  "percentage":0.02
               },
               {
                  "name":"15. CAPUYAN, ALLEN (PPP)",
                  "votes":6,
                  "percentage":0.12
               },
               {
                  "name":"16. CASIÑO, TEDDY (MKBYN)",
                  "votes":140,
                  "percentage":2.91
               },
               {
                  "name":"17. CASTRO, TEACHER FRANCE (MKBYN)",
                  "votes":106,
                  "percentage":2.2
               },
               {
                  "name":"18. CAYETANO, PIA (NP)",
                  "votes":162,
                  "percentage":3.37
               },
               {
                  "name":"19. D'ANGELO, DAVID (BUNYOG)",
                  "votes":6,
                  "percentage":0.12
               },
               {
                  "name":"20. DE ALBAN,ATTORNEY ANGELO (IND)",
                  "votes":50,
                  "percentage":1.04
               },
               {
                  "name":"21. DE GUZMAN, KA LEODY (PLM)",
                  "votes":86,
                  "percentage":1.79
               },
               {
                  "name":"22. DELA ROSA, BATO (PDPLBN)",
                  "votes":132,
                  "percentage":2.74
               },
               {
                  "name":"23. DORINGO, NANAY MIMI (MKBYN)",
                  "votes":10,
                  "percentage":0.21
               },
               {
                  "name":"24. ESCOBAL, ARNEL (PM)",
                  "votes":4,
                  "percentage":0.08
               },
               {
                  "name":"25. ESPIRITU, LUKE (PLM)",
                  "votes":159,
                  "percentage":3.3
               },
               {
                  "name":"26. FLORANDA, MODY PISTON (MKBYN)",
                  "votes":7,
                  "percentage":0.15
               },
               {
                  "name":"27. GAMBOA, MARC LOUIE (IND)",
                  "votes":15,
                  "percentage":0.31
               },
               {
                  "name":"28. GO, BONG GO    (PDPLBN)",
                  "votes":183,
                  "percentage":3.8
               },
               {
                  "name":"29. GONZALES, NORBERTO (PDSP)",
                  "votes":9,
                  "percentage":0.19
               },
               {
                  "name":"30. HINLO, JAYVEE (PDPLBN)",
                  "votes":54,
                  "percentage":1.12
               },
               {
                  "name":"31. HONASAN, GRINGO (RP)",
                  "votes":106,
                  "percentage":2.2
               },
               {
                  "name":"32. JOSE, RELLY JR. (KBL)",
                  "votes":2,
                  "percentage":0.04
               },
               {
                  "name":"33. LACSON, PING (IND)",
                  "votes":232,
                  "percentage":4.82
               },
               {
                  "name":"34. LAMBINO,  RAUL  (PDPLBN)",
                  "votes":64,
                  "percentage":1.33
               },
               {
                  "name":"35. LAPID, LITO (NPC)",
                  "votes":38,
                  "percentage":0.79
               },
               {
                  "name":"36. LEE, MANOY WILBERT (AKSYON)",
                  "votes":4,
                  "percentage":0.08
               },
               {
                  "name":"37. LIDASAN, AMIRAH (MKBYN)",
                  "votes":14,
                  "percentage":0.29
               },
               {
                  "name":"38. MARCOLETA, RODANTE (IND)",
                  "votes":137,
                  "percentage":2.85
               },
               {
                  "name":"39. MARCOS, IMEE R. (NP)",
                  "votes":109,
                  "percentage":2.27
               },
               {
                  "name":"40. MARQUEZ, NORMAN (IND)",
                  "votes":15,
                  "percentage":0.31
               },
               {
                  "name":"41. MARTINEZ, ERIC (IND)",
                  "votes":4,
                  "percentage":0.08
               },
               {
                  "name":"42. MATA, DOC MARITES (IND)",
                  "votes":64,
                  "percentage":1.33
               },
               {
                  "name":"43. MATULA,  ATTY.  SONNY (WPP)",
                  "votes":97,
                  "percentage":2.02
               },
               {
                  "name":"44. MAZA, LIZA (MKBYN)",
                  "votes":78,
                  "percentage":1.62
               },
               {
                  "name":"45. MENDOZA, HEIDI (IND)",
                  "votes":230,
                  "percentage":4.78
               },
               {
                  "name":"46. MONTEMAYOR,  JOEY  (IND)",
                  "votes":1,
                  "percentage":0.02
               },
               {
                  "name":"47. MUSTAPHA, SUBAIR (WPP)",
                  "votes":1,
                  "percentage":0.02
               },
               {
                  "name":"48. OLIVAR, JOSE JESSIE (IND)",
                  "votes":2,
                  "percentage":0.04
               },
               {
                  "name":"49. ONG, DOC WILLIE (AKSYON)",
                  "votes":99,
                  "percentage":2.06
               },
               {
                  "name":"50. PACQUIAO, MANNY PACMAN (PFP)",
                  "votes":74,
                  "percentage":1.54
               },
               {
                  "name":"51. PANGILINAN, KIKO (LP)",
                  "votes":258,
                  "percentage":5.36
               },
               {
                  "name":"52. QUERUBIN,  ARIEL PORFIRIO (NP)",
                  "votes":94,
                  "percentage":1.95
               },
               {
                  "name":"53. QUIBOLOY, APOLLO (IND)",
                  "votes":30,
                  "percentage":0.62
               },
               {
                  "name":"54. RAMOS, DANILO (MKBYN)",
                  "votes":69,
                  "percentage":1.43
               },
               {
                  "name":"55. REVILLAME, WILLIE WIL (IND)",
                  "votes":25,
                  "percentage":0.52
               },
               {
                  "name":"56. RODRIGUEZ, ATTY. VIC (IND)",
                  "votes":75,
                  "percentage":1.56
               },
               {
                  "name":"57. SAHIDULLA, NUR-ANA (IND)",
                  "votes":5,
                  "percentage":0.1
               },
               {
                  "name":"58. SALVADOR, PHILLIP IPE (PDPLBN)",
                  "votes":28,
                  "percentage":0.58
               },
               {
                  "name":"59. SOTTO, TITO (NPC)",
                  "votes":167,
                  "percentage":3.47
               },
               {
                  "name":"60. TAPADO, MICHAEL BONGBONG (PM)",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"61. TOLENTINO, FRANCIS TOL (PFP)",
                  "votes":97,
                  "percentage":2.02
               },
               {
                  "name":"62. TULFO, BEN BITAG (IND)",
                  "votes":84,
                  "percentage":1.75
               },
               {
                  "name":"63. TULFO, ERWIN (LAKAS)",
                  "votes":121,
                  "percentage":2.51
               },
               {
                  "name":"64. VALBUENA, MAR MANIBELA (IND)",
                  "votes":6,
                  "percentage":0.12
               },
               {
                  "name":"65. VERCELES, LEANDRO (IND)",
                  "votes":6,
                  "percentage":0.12
               },
               {
                  "name":"66. VILLAR, CAMILLE (NP)",
                  "votes":80,
                  "percentage":1.66
               }
            ]
         }
      },
      {
         "contestCode":"01199000",
         "contestName":"PARTY LIST of PHILIPPINES",
         "statistic":{
            "overVotes":11,
            "underVotes":96,
            "validVotes":748,
            "obtainedVotes":399
         },
         "candidates":{
            "candidates":[
               {
                  "name":"1 4PS",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"2 PPP",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"3 FPJ PANDAY BAYANIHAN",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"4 KABATAAN",
                  "votes":3,
                  "percentage":0.75
               },
               {
                  "name":"5 DUTERTE YOUTH",
                  "votes":16,
                  "percentage":4.01
               },
               {
                  "name":"6 ML",
                  "votes":32,
                  "percentage":8.02
               },
               {
                  "name":"7 PBBM",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"8 P3PWD",
                  "votes":5,
                  "percentage":1.25
               },
               {
                  "name":"9 MURANG KURYENTE",
                  "votes":4,
                  "percentage":1.0
               },
               {
                  "name":"10 BICOL SARO",
                  "votes":6,
                  "percentage":1.5
               },
               {
                  "name":"11 IPATUPAD",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"12 PATROL",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"13 JUAN PINOY",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"14 ARTE",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"15 WIFI",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"16 MAAGAP",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"17 UNITED SENIOR CITIZENS",
                  "votes":16,
                  "percentage":4.01
               },
               {
                  "name":"18 EPANAW SAMBAYANAN",
                  "votes":4,
                  "percentage":1.0
               },
               {
                  "name":"19 AKO PADAYON",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"20 TUCP",
                  "votes":3,
                  "percentage":0.75
               },
               {
                  "name":"21 ACT TEACHERS",
                  "votes":4,
                  "percentage":1.0
               },
               {
                  "name":"22 1PACMAN",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"23 TGP",
                  "votes":13,
                  "percentage":3.26
               },
               {
                  "name":"24 DUMPER PTDA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"25 ANAKALUSUGAN",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"26 AKSYON DAPAT",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"27 BHW",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"28 SULONG DIGNIDAD",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"29 BATANG QUIAPO",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"30 PBA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"31 GILAS",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"32 AKO ILOCANO AKO",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"33 PAMILYANG MAGSASAKA",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"34 CLICK PARTY",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"35 ABANTE BISDAK",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"36 MANILA TEACHERS",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"37 PAMANA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"38 NANAY",
                  "votes":14,
                  "percentage":3.51
               },
               {
                  "name":"39 KM NGAYON NA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"40 BABAE AKO",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"41 ARISE",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"42 MAGDALO",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"43 APEC",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"44 MAGBUBUKID",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"45 SSS-GSIS PENSYONADO",
                  "votes":4,
                  "percentage":1.0
               },
               {
                  "name":"46 GABRIELA",
                  "votes":7,
                  "percentage":1.75
               },
               {
                  "name":"47 TINGOG",
                  "votes":7,
                  "percentage":1.75
               },
               {
                  "name":"48 APAT-DAPAT",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"49 AHON MAHIRAP",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"50 UGB",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"51 AKBAYAN",
                  "votes":75,
                  "percentage":18.8
               },
               {
                  "name":"52 AGIMAT",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"53 PHILRECA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"54 KAPUSO PM",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"55 ILOCANO DEFENDERS",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"56 1-RIDER PARTY-LIST",
                  "votes":10,
                  "percentage":2.51
               },
               {
                  "name":"57 TICTOK",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"59 BAYAN MUNA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"60 ANG PROBINSIYANO",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"61 BANAT",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"62 SBP",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"63 BUHAY",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"64 TULUNGAN TAYO",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"65 SAGIP",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"66 BTS BAYANING TSUPER",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"67 VENDORS",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"68 ACT-CIS",
                  "votes":10,
                  "percentage":2.51
               },
               {
                  "name":"69 AKTIBONG KAAGAPAY",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"70 ASENSO PINOY",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"71 SOLO PARENTS",
                  "votes":3,
                  "percentage":0.75
               },
               {
                  "name":"72 ANG KOMADRONA",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"73 PROMDI",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"74 PUSONG PINOY",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"75 KUSUG TAUSUG",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"76 DAMAYANG FILIPINO",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"77 MPBL",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"78 ANGAT",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"79 KALINGA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"80 BOSES PARTY-LIST",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"81 ARANGKADA PILIPINO",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"82 AANGAT TAYO",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"83 OFW",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"84 BIDA KATAGUMPAY",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"85 KAMANGGAGAWA",
                  "votes":3,
                  "percentage":0.75
               },
               {
                  "name":"86 BFF",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"87 BUNYOG",
                  "votes":4,
                  "percentage":1.0
               },
               {
                  "name":"88 AGRI",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"89 SENIOR CITIZENS",
                  "votes":25,
                  "percentage":6.27
               },
               {
                  "name":"90 4K",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"91 PBP",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"92 ONE COOP",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"93 CIBAC",
                  "votes":7,
                  "percentage":1.75
               },
               {
                  "name":"94 BH - BAGONG HENERASYON",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"95 1AGILA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"96 EDUAKSYON",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"97 ANG TINIG NG SENIORS",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"98 BG PARTY-LIST",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"99 PINOY AKO",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"100 H.E.L.P. PILIPINAS",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"101 HEALTH WORKERS",
                  "votes":5,
                  "percentage":1.25
               },
               {
                  "name":"102 PEOPLE'S CHAMP",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"103 AA-KASOSYO PARTY",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"104 SOLID NORTH PARTY",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"105 ABAMIN",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"106 TRABAHO",
                  "votes":16,
                  "percentage":4.01
               },
               {
                  "name":"107 ANGKASANGGA",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"108 TODA AKSYON",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"109 TURISMO",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"110 ABONO",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"111 ASAP NA",
                  "votes":6,
                  "percentage":1.5
               },
               {
                  "name":"112 LINGAP",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"113 UNITED FRONTLINERS",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"114 KASAMBAHAY",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"115 TUTOK TO WIN",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"116 AKO OFW",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"117 AGAP",
                  "votes":4,
                  "percentage":1.0
               },
               {
                  "name":"118 1TAHANAN",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"119 COOP-NATCCO",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"120 KABAYAN",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"121 1MUNTI",
                  "votes":3,
                  "percentage":0.75
               },
               {
                  "name":"122 PINOY WORKERS",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"123 API PARTY",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"124 AKO BISAYA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"125 KAMALAYAN",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"126 AKO TANOD",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"127 PROBINSYANO AKO",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"128 KABABAIHAN",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"129 RAM",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"130 ALONA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"131 AKO BICOL",
                  "votes":5,
                  "percentage":1.25
               },
               {
                  "name":"132 GP (GALING SA PUSO)",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"133 KAUNLAD PINOY",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"134 ABP",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"135 CWS",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"136 LPGMA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"137 A TEACHER",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"138 SWERTE",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"139 GABAY",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"140 MALASAKIT@BAYANIHAN",
                  "votes":5,
                  "percentage":1.25
               },
               {
                  "name":"141 AKAY NI SOL",
                  "votes":12,
                  "percentage":3.01
               },
               {
                  "name":"142 LUNAS",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"143 DIWA",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"144 PINUNO",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"145 PAMILYA MUNA",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"146 BAGONG PILIPINAS",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"147 HUGPONG FEDERAL",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"148 TUPAD",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"149 LAANG KAWAL",
                  "votes":3,
                  "percentage":0.75
               },
               {
                  "name":"150 PAMILYA KO",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"151 BBM",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"152 HEAL PH",
                  "votes":0,
                  "percentage":0.0
               },
               {
                  "name":"153 ABANG LINGKOD",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"154 MAGSASAKA",
                  "votes":2,
                  "percentage":0.5
               },
               {
                  "name":"155 MAHARLIKA",
                  "votes":1,
                  "percentage":0.25
               },
               {
                  "name":"156 USWAG ILONGGO",
                  "votes":1,
                  "percentage":0.25
               }
            ]
         }
      }
   ],
   "local":[
      {
         "contestCode":"00734030",
         "contestName":"MEMBER, HOUSE OF REPRESENTATIVES of LAGUNA - CITY OF BIÑAN - LONE LEGDIST",
         "statistic":{
            "overVotes":2,
            "underVotes":24,
            "validVotes":748,
            "obtainedVotes":480
         },
         "candidates":{
            "candidates":[
               {
                  "name":"1. DIMAGUILA, ATTY. ARMAN (LAKAS)",
                  "votes":362,
                  "percentage":75.42
               },
               {
                  "name":"2. YATCO, PARENG MIKE YATCO (PFP)",
                  "votes":118,
                  "percentage":24.58
               }
            ]
         }
      },
      {
         "contestCode":"00434000",
         "contestName":"PROVINCIAL GOVERNOR of LAGUNA",
         "statistic":{
            "overVotes":11,
            "underVotes":22,
            "validVotes":748,
            "obtainedVotes":473
         },
         "candidates":{
            "candidates":[
               {
                  "name":"1. AGAPAY, KAREN (PFP)",
                  "votes":74,
                  "percentage":15.64
               },
               {
                  "name":"2. ARAGONES, SOL (AKAY)",
                  "votes":180,
                  "percentage":38.05
               },
               {
                  "name":"3. FERNANDEZ, DAN (NUP)",
                  "votes":118,
                  "percentage":24.95
               },
               {
                  "name":"4. HERNANDEZ, RUTH (LAKAS)",
                  "votes":91,
                  "percentage":19.24
               },
               {
                  "name":"5. REYES, CALOY (IND)",
                  "votes":3,
                  "percentage":0.63
               },
               {
                  "name":"6. SAMIA, KOYANG NOLI (IND)",
                  "votes":4,
                  "percentage":0.85
               },
               {
                  "name":"7. TOLENTINO, ALEXANDER (IND)",
                  "votes":3,
                  "percentage":0.63
               }
            ]
         }
      },
      {
         "contestCode":"00534000",
         "contestName":"PROVINCIAL VICE-GOVERNOR of LAGUNA",
         "statistic":{
            "overVotes":2,
            "underVotes":56,
            "validVotes":748,
            "obtainedVotes":448
         },
         "candidates":{
            "candidates":[
               {
                  "name":"1. BUERA, MARY (IND)",
                  "votes":15,
                  "percentage":3.35
               },
               {
                  "name":"2. CARAIT, ATTY. JM (LAKAS)",
                  "votes":301,
                  "percentage":67.19
               },
               {
                  "name":"3. EJERCITO, JORGE JERICO (IND)",
                  "votes":46,
                  "percentage":10.27
               },
               {
                  "name":"4. PEREZ, PEEWEE PLATON (AKAY)",
                  "votes":22,
                  "percentage":4.91
               },
               {
                  "name":"5. RETUERTO, GEM AMANTE (NUP)",
                  "votes":50,
                  "percentage":11.16
               },
               {
                  "name":"6. ZUÑIGA, LORENZO (PFP)",
                  "votes":14,
                  "percentage":3.13
               }
            ]
         }
      },
      {
         "contestCode":"00634030",
         "contestName":"MEMBER, SANGGUNIANG PANLALAWIGAN of LAGUNA - CITY OF BIÑAN - LONE PROVDIST",
         "statistic":{
            "overVotes":10,
            "underVotes":232,
            "validVotes":1496,
            "obtainedVotes":770
         },
         "candidates":{
            "candidates":[
               {
                  "name":"1. ALATIIT, GAB (PFP)",
                  "votes":136,
                  "percentage":17.66
               },
               {
                  "name":"2. ASIÑO, ENGR. JR (IND)",
                  "votes":34,
                  "percentage":4.42
               },
               {
                  "name":"3. BEJASA, BONGBEJASA (LAKAS)",
                  "votes":210,
                  "percentage":27.27
               },
               {
                  "name":"4. GARCIA, ALVIN (NUP)",
                  "votes":93,
                  "percentage":12.08
               },
               {
                  "name":"5. PARON, THERESA YATCO (AKAY)",
                  "votes":73,
                  "percentage":9.48
               },
               {
                  "name":"6. PECAÑA, JIGCY (LAKAS)",
                  "votes":94,
                  "percentage":12.21
               },
               {
                  "name":"7. SORDILLA, IZEL (IND)",
                  "votes":18,
                  "percentage":2.34
               },
               {
                  "name":"8. SOUZA, JAY (NUP)",
                  "votes":112,
                  "percentage":14.55
               }
            ]
         }
      },
      {
         "contestCode":"00834030",
         "contestName":"MAYOR of LAGUNA - CITY OF BIÑAN",
         "statistic":{
            "overVotes":0,
            "underVotes":16,
            "validVotes":748,
            "obtainedVotes":490
         },
         "candidates":{
            "candidates":[
               {
                  "name":"1. ALONTE, GEL (NUP)",
                  "votes":324,
                  "percentage":66.12
               },
               {
                  "name":"2. YATCO, COOKIE (AKSYON)",
                  "votes":166,
                  "percentage":33.88
               }
            ]
         }
      },
      {
         "contestCode":"00934030",
         "contestName":"VICE-MAYOR of LAGUNA - CITY OF BIÑAN",
         "statistic":{
            "overVotes":0,
            "underVotes":34,
            "validVotes":748,
            "obtainedVotes":472
         },
         "candidates":{
            "candidates":[
               {
                  "name":"1. ABALOS- YATCO, JOY (AKSYON)",
                  "votes":169,
                  "percentage":35.81
               },
               {
                  "name":"2. REYES, DADA (NUP)",
                  "votes":303,
                  "percentage":64.19
               }
            ]
         }
      },
      {
         "contestCode":"01034030",
         "contestName":"MEMBER, SANGGUNIANG PANLUNGSOD of LAGUNA - CITY OF BIÑAN - LONE DIST",
         "statistic":{
            "overVotes":144,
            "underVotes":2081,
            "validVotes":8976,
            "obtainedVotes":3847
         },
         "candidates":{
            "candidates":[
               {
                  "name":"1. ALATIIT, JEDI (NUP)",
                  "votes":268,
                  "percentage":6.97
               },
               {
                  "name":"2. ALBA, TOPPE (NUP)",
                  "votes":132,
                  "percentage":3.43
               },
               {
                  "name":"3. ALMEDA, INGRID (LAKAS)",
                  "votes":164,
                  "percentage":4.26
               },
               {
                  "name":"4. ALZONA, DOC POL (LAKAS)",
                  "votes":102,
                  "percentage":2.65
               },
               {
                  "name":"5. ALZONA, DOK WILLIE (AKAY)",
                  "votes":80,
                  "percentage":2.08
               },
               {
                  "name":"6. AMBROSIO, BATANGQUIAPO(AKSYON)",
                  "votes":41,
                  "percentage":1.07
               },
               {
                  "name":"7. BAUTISTA, BOSSENG TITUS(LAKAS)",
                  "votes":137,
                  "percentage":3.56
               },
               {
                  "name":"8. BEDIA, DOC ELVIS (NUP)",
                  "votes":194,
                  "percentage":5.04
               },
               {
                  "name":"9. BORJA, BOBET (AKAY)",
                  "votes":118,
                  "percentage":3.07
               },
               {
                  "name":"10. BORRES, KELVIN (AKSYON)",
                  "votes":78,
                  "percentage":2.03
               },
               {
                  "name":"11. CARDAMA, MARIANO (AKSYON)",
                  "votes":53,
                  "percentage":1.38
               },
               {
                  "name":"12. CARDEÑO, LIZA (LAKAS)",
                  "votes":264,
                  "percentage":6.86
               },
               {
                  "name":"13. CARIÑO, BING MALAMBING (NUP)",
                  "votes":181,
                  "percentage":4.7
               },
               {
                  "name":"14. CARRILLO, DONDON (AKAY)",
                  "votes":112,
                  "percentage":2.91
               },
               {
                  "name":"15. DESUASIDO, ECHIT (LAKAS)",
                  "votes":189,
                  "percentage":4.91
               },
               {
                  "name":"16. DICDICAN, ROMMEL (NUP)",
                  "votes":155,
                  "percentage":4.03
               },
               {
                  "name":"17. DIMAGUILA, ARTHUR (LAKAS)",
                  "votes":235,
                  "percentage":6.11
               },
               {
                  "name":"18. DIMARANAN, ELMER (NUP)",
                  "votes":188,
                  "percentage":4.89
               },
               {
                  "name":"19. ESCUETA, ATTY. DAVID (IND)",
                  "votes":123,
                  "percentage":3.2
               },
               {
                  "name":"20. ESCUETA, DOC VICO (AKSYON)",
                  "votes":118,
                  "percentage":3.07
               },
               {
                  "name":"21. JUNTILLA, COACHJOEWILL(AKSYON)",
                  "votes":34,
                  "percentage":0.88
               },
               {
                  "name":"22. LAMPAAN, VICTOR JR. (IND)",
                  "votes":44,
                  "percentage":1.14
               },
               {
                  "name":"23. LIMOSINERO, EDGAR (AKSYON)",
                  "votes":92,
                  "percentage":2.39
               },
               {
                  "name":"24. LOYOLA, FRANCIS (AKSYON)",
                  "votes":76,
                  "percentage":1.98
               },
               {
                  "name":"25. MARCOS, JOHN WILSON (AKSYON)",
                  "votes":58,
                  "percentage":1.51
               },
               {
                  "name":"26. OLIVARES, ANGELI (AKAY)",
                  "votes":73,
                  "percentage":1.9
               },
               {
                  "name":"27. REYES, ANGELYN (AKSYON)",
                  "votes":93,
                  "percentage":2.42
               },
               {
                  "name":"28. TAN GANA, JUN (AKSYON)",
                  "votes":149,
                  "percentage":3.87
               },
               {
                  "name":"29. TOMACRUZ, TOM (AKSYON)",
                  "votes":42,
                  "percentage":1.09
               },
               {
                  "name":"30. YATCO, DONNA (AKSYON)",
                  "votes":254,
                  "percentage":6.6
               }
            ]
         }
      }
   ]
}
```
</details>