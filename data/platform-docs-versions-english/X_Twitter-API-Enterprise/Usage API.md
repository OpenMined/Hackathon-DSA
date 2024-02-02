Overview

Overview
--------

Enterprise

The Usage API is a free REST API that provides programmatic access and visibility into activity consumption across products for your enterprise account. It is the most important and _best_ tool for helping to monitor and manage usage across the different APIs under your account.

**Important Disclaimer:**

The usage counts returned from the Usage API may not match those on a billing invoice due to trials and other billing adjustments. All numbers are based on deduped activities consumed within a given day (in UTC).

### Features

* Programmatically retrieving usage data that is available in the console.gnip.com UI
* Stream level usage data - provides usage data at the stream level (e.g., dev and prod) in addition to the product level
* Granular and descriptive data - search "requests" are broken out by Full-Archive and 30-Day Search products 
* Historical PowerTrack “days” and “jobs” 

Supported APIs
--------------

Below is a list of the APIs currently supported by the Usage API:

* PowerTrack API enterprise
* 30-Day Search API enterprise
* Full-Archive Search API enterprise
* Historical PowerTrack enterprise

  
Limitations
--------------

* The Usage API allows you to access usage data since May 1, 2018.  After July 1, 2019 Usage API allows you to access usage data for the **trailing 13 calendar months**  
    
* You have the ability to access usage data in **three month intervals** defined with a fromDate and toDate

See below for a request & response:

      `curl -u<username>:<password> \ "https://gnip-api.twitter.com/metrics/usage/accounts/<account-name>.json?bucket=month"`
    

      `{   "account": {     "name": "accountnamehere"   },   "publishers": [     {       "type": "twitter",       "used": [         {           "timePeriod": "201805010000",           "activities": 1235,           "searchRequests30Day": 3,           "searchRequestsFullArchive": 19,           "historicalPowertrackDays": 0,           "historicalPowertrackJobs": 0         },         {           "timePeriod": "201806010000",           "activities": 23467,           "searchRequests30Day": 0,           "searchRequestsFullArchive": 66,           "historicalPowertrackDays": 0,           "historicalPowertrackJobs": 0         },         {           "timePeriod": "201807010000",           "activities": 431,           "searchRequests30Day": 11,           "searchRequestsFullArchive": 4,           "historicalPowertrackDays": 0,           "historicalPowertrackJobs": 0         }       ],       "projected": {         "timePeriod": "201807010000",         "activities": 803,         "searchRequests30Day": 20,         "searchRequestsFullArchive": 7,         "historicalPowertrackDays": 0,         "historicalPowertrackJobs": 0       },       "products": [         {           "type": "Historical PowerTrack Subscription",           "used": [             {               "timePeriod": "201805010000",               "activities": 0,               "days": 0,               "jobs": 0             },             {               "timePeriod": "201806010000",               "activities": 0,               "days": 0,               "jobs": 0             },             {               "timePeriod": "201807010000",               "activities": 0,               "days": 0,               "jobs": 0             }           ],           "projected": {             "timePeriod": "201807010000",             "activities": 0,             "days": 0,             "jobs": 0           }         },         {           "type": "PowerTrack",           "used": [             {               "timePeriod": "201805010000",               "activities": 267             },             {               "timePeriod": "201806010000",               "activities": 3             },             {               "timePeriod": "201807010000",               "activities": 32             }           ],           "projected": {             "timePeriod": "201807010000",             "activities": 59           },           "endpoints": [             {               "type": "PowerTrack 2.0",               "label": "actformat",               "used": [                 {                   "timePeriod": "201805010000",                   "activities": 0                 },                 {                   "timePeriod": "201806010000",                   "activities": 0                 },                 {                   "timePeriod": "201807010000",                   "activities": 0                 }               ],               "projected": {                 "timePeriod": "201807010000",                 "activities": 0               }             },               {               "type": "PowerTrack Replay 2.0",               "label": "ogformat",               "used": [                 {                   "timePeriod": "201805010000",                   "activities": 0                 },                 {                   "timePeriod": "201806010000",                   "activities": 0                 },                 {                   "timePeriod": "201807010000",                   "activities": 0                 }               ],               "projected": {                 "timePeriod": "201807010000",                 "activities": 0               }             }           ]         },         {           "type": "Search API (30-Day) 2.0",           "used": [             {               "timePeriod": "201805010000",               "activities": 10,               "searchRequests30Day": 3             },             {               "timePeriod": "201806010000",               "activities": 0,               "searchRequests30Day": 0             },             {               "timePeriod": "201807010000",               "activities": 23,               "searchRequests30Day": 11             }           ],           "projected": {             "timePeriod": "201807010000",             "activities": 42,             "searchRequests30Day": 20           },           "endpoints": [             {               "type": "Search API (30-Day) 2.0",               "label": "ogformat",               "used": [                 {                   "timePeriod": "201805010000",                   "activities": 10,                   "searchRequests30Day": 3                 },                 {                   "timePeriod": "201806010000",                   "activities": 0,                   "searchRequests30Day": 0                 },                 {                   "timePeriod": "201807010000",                   "activities": 21,                   "searchRequests30Day": 10                 }               ],               "projected": {                 "timePeriod": "201807010000",                 "activities": 39,                 "searchRequests30Day": 18               }             }           ]         },         {           "type": "Search API (Full-Archive)",           "used": [             {               "timePeriod": "201805010000",               "activities": 961,               "searchRequestsFullArchive": 19             },             {               "timePeriod": "201806010000",               "activities": 23466,               "searchRequestsFullArchive": 66             },             {               "timePeriod": "201807010000",               "activities": 379,               "searchRequestsFullArchive": 4             }           ],           "projected": {             "timePeriod": "201807010000",             "activities": 706,             "searchRequestsFullArchive": 7           },           "endpoints": [             {               "type": "Search API (Full-Archive)",               "label": "actformat",               "used": [                 {                   "timePeriod": "201805010000",                   "activities": 1,                   "searchRequestsFullArchive": 3                 },                 {                   "timePeriod": "201806010000",                   "activities": 0,                   "searchRequestsFullArchive": 0                 },                 {                   "timePeriod": "201807010000",                   "activities": 2,                   "searchRequestsFullArchive": 1                 }               ],               "projected": {                 "timePeriod": "201807010000",                 "activities": 3,                 "searchRequestsFullArchive": 1               }             },             {               "type": "Search API (Full-Archive)",               "label": "ogformat",               "used": [                 {                   "timePeriod": "201805010000",                   "activities": 961,                   "searchRequestsFullArchive": 16                 },                 {                   "timePeriod": "201806010000",                   "activities": 23466,                   "searchRequestsFullArchive": 66                 },                 {                   "timePeriod": "201807010000",                   "activities": 379,                   "searchRequestsFullArchive": 3                 }               ],               "projected": {                 "timePeriod": "201807010000",                 "activities": 706,                 "searchRequestsFullArchive": 5               }             }           ]         }       ]     }   ],   "bucket": "month",   "fromDate": "201805010000",   "toDate": "201808010000" }`
    

Sample Payload
--------------

Below is a sample of the payload:

      `{   "account": {     "name": "gnip-username"   },   "bucket": "month",   "publishers": [     {       "type": "automattic",       "used": [         {           "activities": 0,           "timePeriod": "201603010000"         }       ],       "projected": {         "activities": 0,         "timePeriod": "201603010000"       },       "products": [         {           "type": "PowerTrack",           "used": [             {               "timePeriod": "201603010000",               "activities": 0             }           ],           "projected": {             "timePeriod": "201603010000",             "activities": 0           },           "endpoints": [             {               "type": "PowerTrack",               "label": "dev",               "used": [                 {                   "timePeriod": "201603010000",                   "activities": 0                 }               ],               "projected": {                 "timePeriod": "201603010000",                 "activities": 0               }             }           ]         }       ]     },     {       "type": "twitter",       "used": [         {           "activities": 84,           "searchRequests30Day": 4,           "searchRequestsFullArchive": 0,           "historicalPowertrackDays": 0,           "historicalPowertrackJobs": 0,           "timePeriod": "201603010000"         }       ],       "projected": {         "activities": 0,         "searchRequests30Day": 0,         "searchRequestsFullArchive": 0,         "historicalPowertrackDays": 0,         "historicalPowertrackJobs": 0,         "timePeriod": "201601010000"       },       "products": [         {           "type": "Historical PowerTrack 2.0",           "used": [             {               "timePeriod": "201511010000",               "activities": 11884,               "days": 5,               "jobs": 5             },             {               "timePeriod": "201512010000",               "activities": 0,               "days": 0,               "jobs": 0             },             {               "timePeriod": "201601010000",               "activities": 0,               "days": 0,               "jobs": 0             }           ]         },         {           "type": "PowerTrack",           "used": [             {               "timePeriod": "201511010000",               "activities": 0             },             {               "timePeriod": "201512010000",               "activities": 27456             },             {               "timePeriod": "201601010000",               "activities": 0             }           ],           "projected": {             "timePeriod": "201601010000",             "activities": 0           },           "endpoints": [             {               "type": "PowerTrack",               "label": "devel",               "used": [                 {                   "timePeriod": "201511010000",                   "activities": 0                 },                 {                   "timePeriod": "201512010000",                   "activities": 2930                 },                 {                   "timePeriod": "201601010000",                   "activities": 0                 }               ],               "projected": {                 "timePeriod": "201601010000",                 "activities": 0               }             },             {               "type": "PowerTrack 2.0",               "label": "devel-v2",               "used": [                 {                   "timePeriod": "201511010000",                   "activities": 0                 },                 {                   "timePeriod": "201512010000",                   "activities": 24542                 },                 {                   "timePeriod": "201601010000",                   "activities": 0                 }               ],               "projected": {                 "timePeriod": "201601010000",                 "activities": 0               }             },             {               "type": "PowerTrack 2.0",               "label": "devel-v2-1",               "used": [                 {                   "timePeriod": "201511010000",                   "activities": 0                 },                 {                   "timePeriod": "201512010000",                   "activities": 0                 },                 {                   "timePeriod": "201601010000",                   "activities": 0                 }               ],               "projected": {                 "timePeriod": "201601010000",                 "activities": 0               }             }           ]         },         {           "type": "Search API",           "used": [             {               "timePeriod": "201511010000",               "activities": 0,               "searchRequests30Day": 0             },             {               "timePeriod": "201512010000",               "activities": 0,               "searchRequests30Day": 0             },             {               "timePeriod": "201601010000",               "activities": 0,               "searchRequests30Day": 0             }           ],           "projected": {             "timePeriod": "201601010000",             "activities": 0,             "searchRequests30Day": 0           },           "endpoints": [             {               "type": "Search API",               "label": "devel",               "used": [                 {                   "timePeriod": "201511010000",                   "activities": 0,                   "searchRequests30Day": 0                 },                 {                   "timePeriod": "201512010000",                   "activities": 0,                   "searchRequests30Day": 0                 },                 {                   "timePeriod": "201601010000",                   "activities": 0,                   "searchRequests30Day": 0                 }               ],               "projected": {                 "timePeriod": "201601010000",                 "activities": 0,                 "searchRequests30Day": 0               }             }           ]         },         {           "type": "Search API (30-Day)",           "used": [             {               "timePeriod": "201511010000",               "activities": 0,               "searchRequests30Day": 0             },             {               "timePeriod": "201512010000",               "activities": 0,               "searchRequests30Day": 0             },             {               "timePeriod": "201601010000",               "activities": 0,               "searchRequests30Day": 0             }           ],           "projected": {             "timePeriod": "201601010000",             "activities": 0,             "searchRequests30Day": 0           },           "endpoints": [             {               "type": "Search API (30-Day)",               "label": "devel",               "used": [                 {                   "timePeriod": "201511010000",                   "activities": 0,                   "searchRequests30Day": 0                 },                 {                   "timePeriod": "201512010000",                   "activities": 0,                   "searchRequests30Day": 0                 },                 {                   "timePeriod": "201601010000",                   "activities": 0,                   "searchRequests30Day": 0                 }               ],               "projected": {                 "timePeriod": "201601010000",                 "activities": 0,                 "searchRequests30Day": 0               }             }           ]         },         {           "type": "Search API (Full-Archive)",           "used": [             {               "timePeriod": "201511010000",               "activities": 0,               "searchRequestsFullArchive": 0             },             {               "timePeriod": "201512010000",               "activities": 0,               "searchRequestsFullArchive": 0             },             {               "timePeriod": "201601010000",               "activities": 0,               "searchRequestsFullArchive": 0             }           ],           "projected": {             "timePeriod": "201601010000",             "activities": 0,             "searchRequestsFullArchive": 0           },           "endpoints": [             {               "type": "Search API (Full-Archive)",               "label": "devel",               "used": [                 {                   "timePeriod": "201511010000",                   "activities": 0,                   "searchRequestsFullArchive": 0                 },                 {                   "timePeriod": "201512010000",                   "activities": 0,                   "searchRequestsFullArchive": 0                 },                 {                   "timePeriod": "201601010000",                   "activities": 0,                   "searchRequestsFullArchive": 0                 }               ],               "projected": {                 "timePeriod": "201601010000",                 "activities": 0,                 "searchRequestsFullArchive": 0               }             }           ]         }       ]     }   ] }`

get-usage

get-usage

Methods [¶](#methods- "Permalink to this headline")
---------------------------------------------------

| Method | Description |
| --- | --- |
| [GET /metrics/usage/accounts/{ACCOUNT\_NAME}.json](#GETData) | Retrieve usage data |

Where:

* :account\_name is the (case-sensitive) name associated with your account, as displayed at console.gnip.com

Authentication and Rate Limit [¶](#authentication-and-rate-limit- "Permalink to this headline")
-----------------------------------------------------------------------------------------------

#### Authentication

All requests to the Usage API require HTTP Basic Authentication, using any of the email/password credentials enabled on your account to log into your account at console.gnip.com or connect to any Gnip stream.

#### Rate Limit

The Usage API enforces a rate limit of two requests per minute.

Best Practices & Limitations [¶](#best-practices-limitations- "Permalink to this headline")
-------------------------------------------------------------------------------------------

#### Data Availability

Usage data is based on deduped activities consumed through the last full time period (UTC) that data was processed. Data is generally processed and updated up to the minute, except in cases where Gnip is deploying systems.

* The Usage API allows you to access usage data since May 1, 2018.  After July 1, 2019 Usage API allows you to access usage data for the **trailing 13 calendar months**.   
    
* You have the ability to access usage data in **three month intervals** defined with a fromDate and toDate

Requesting and Receiving Data [¶](#requesting-and-receiving-data- "Permalink to this headline")
-----------------------------------------------------------------------------------------------

The Usage API works by issuing an HTTP GET request with HTTP BASIC-AUTH credentials to the API endpoint for your account.

#### GET Request:

Make a GET request to the following endpoint with your user credentials and account name:

https://gnip-api.twitter.com/metrics/usage/accounts/:account\_name.json

  
**Additional Parameters**  

|     |     |
| --- | --- |
| bucket | Optional. The unit of time for which usage data will be provided. Usage data can be returned with daily or monthly granularity.  <br>  <br>Requests made without a specified bucket will return monthly granularity.  <br>  <br>Options: 'month' or 'day' |
| fromDate (YYYYMMDDHHMM) | Optional. Usage data is only available starting from May 1, 2018. The oldest UTC timestamp from which the usage data will be provided. Timestamp is in day granularity and is inclusive (i.e., 201805010000 includes the 0501 day). Requests that contain values other than '0000' for hour and minute granularity will be defaulted to '0000'.  <br>  <br>Requests made without a fromDate or toDate will return usage data by month for the current month and include a historical reference for the past two months.  <br>  <br>**Please note:** Starting June 1, 2019, you can access the past 13 calendar months of usage data. For example, if it was the 10th of October, you can access usage data back to September 1st of the previous year.  <br>**Example:** 201810010000 will return data starting October 1st, 2018 onward, including October 1st. |
| toDate (YYYYMMDDHHMM) | Optional. The latest UTC timestamp to which the usage data will be provided. Timestamp is in day granularity and is not inclusive (i.e., 201703020000 does not include data for the 0302 day). When a toDate is specified for either the current day or a day in the future, usage data will be returned up to the last full day (UTC). Requests that contain values other than '0000' for hour and minute granularity will be defaulted to '0000'.  <br>  <br>A request with no toDate, will default to the next bucket (tomorrow for bucket=day and next month for bucket=month). A request made with no fromDate and toDate will default to bucket=month, and show data for the current month plus the two immediately previous months.  <br>  <br>**Example:** 201703050000 will return data to March 5, 2017, not including any data from March 5th. |

  
**Example GET Request**

This request will return data by month granularity from March 1, 2017 to March 5, 2017, not including any data from March 5, 2017.

curl -u "https://gnip-api.twitter.com/metrics/usage/accounts/:account\_name.json?bucket=month&fromdate=201403010000&toDate=201403150000"

  

Data Format [¶](#data-format- "Permalink to this headline")
-----------------------------------------------------------

The following tables describe the root-level data structures for usage data returned from the Usage API. For fields with multiple levels of sub-fields, click the links provided to reveal details about the sub-fields.

If you would like to see an sample of a full Usage API payload, please visit [this page](https://developer.twitter.com/en/docs/developer-utilities/usage-api/overview).

|     |     |
| --- | --- |
| **account** | An object representing the account for which usage data was requested. |
| **bucket** | The unit of time for which usage data is provided. Can be either 'day' or 'month'. |
| **fromDate** | The earliest UTC timestamp for which you want to pull usage data (inclusive). |
| **toDate** | The latest UTC timestamp for which you want to pull usage data (exclusive). |
| **publishers** | Includes three primary objects: Used, projected, and products. |