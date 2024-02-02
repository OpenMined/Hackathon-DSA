



get-usage | Docs | Twitter Developer Platform 





































































































get-usage



get-usage

Methods¶
--------




| Method | Description |
| --- | --- |
| GET
/metrics/usage/accounts/{ACCOUNT\_NAME}.json | Retrieve usage data |


Where:


* :account\_name is the (case-sensitive) name associated with your
account, as displayed at console.gnip.com


Authentication and Rate
Limit¶
------------------------------


#### Authentication


All requests to the Usage API require HTTP Basic Authentication,
using any of the email/password credentials enabled on your account to
log into your account at console.gnip.com or connect to any Gnip
stream.


#### Rate Limit


The Usage API enforces a rate limit of two requests per minute.


Best Practices &
Limitations¶
-----------------------------


#### Data Availability


Usage data is based on deduped activities consumed through the last
full time period (UTC) that data was processed. Data is generally
processed and updated up to the minute, except in cases where Gnip is
deploying systems.


* The Usage API allows you to access usage data since May 1, 2018.  After July 1, 2019 Usage API allows you to access usage data for the **trailing 13 calendar months**.
* You have the ability to access usage data in **three month intervals** defined with a fromDate and toDate


Requesting and Receiving
Data¶
------------------------------


The Usage API works by issuing an HTTP GET request with HTTP
BASIC-AUTH credentials to the API endpoint for your account.


#### GET Request:


Make a GET request to the following endpoint with your user
credentials and account name:



```

https://gnip-api.twitter.com/metrics/usage/accounts/:account_name.json

```

  

**Additional Parameters**
  



|  |  |
| --- | --- |
| bucket | Optional. The unit of time for which usage data will be provided.
Usage data can be returned with daily or monthly granularity.
Requests made without a specified bucket will return monthly
granularity. Options: 'month' or 'day' |
| fromDate (YYYYMMDDHHMM) | Optional. Usage data is only available starting from May 1, 2018.
The oldest UTC timestamp from which the usage data will be provided.
Timestamp is in day granularity and is inclusive (i.e., 201805010000
includes the 0501 day). Requests that contain values other than '0000'
for hour and minute granularity will be defaulted to '0000'. 
Requests made without a fromDate or toDate will return usage data by
month for the current month and include a historical reference for the
past two months.**Please note:** Starting June 1,
2019, you can access the past 13 calendar months of usage data. For
example, if it was the 10th of October, you can access usage data back
to September 1st of the previous year. **Example:**
201810010000 will return data starting October 1st, 2018 onward,
including October 1st. |
| toDate (YYYYMMDDHHMM) | Optional. The latest UTC timestamp to which the usage data will be
provided. Timestamp is in day granularity and is not inclusive (i.e.,
201703020000 does not include data for the 0302 day). When a toDate is
specified for either the current day or a day in the future, usage data
will be returned up to the last full day (UTC). Requests that contain
values other than '0000' for hour and minute granularity will be
defaulted to '0000'. A request with no toDate, will default to
the next bucket (tomorrow for bucket=day and next month for
bucket=month). A request made with no fromDate and toDate will default
to bucket=month, and show data for the current month plus the two
immediately previous months.**Example:**
201703050000 will return data to March 5, 2017, not including any data
from March 5th. |


  

**Example GET Request**
This request will return data by month granularity from March 1, 2017
to March 5, 2017, not including any data from March 5, 2017.



```

curl -u "https://gnip-api.twitter.com/metrics/usage/accounts/:account_name.json?bucket=month&fromdate=201403010000&toDate=201403150000"

```

  

Data
Format¶
------------


The following tables describe the root-level data structures for
usage data returned from the Usage API. For fields with multiple levels
of sub-fields, click the links provided to reveal details about the
sub-fields.


If you would like to see an sample of a full Usage API payload,
please visit this
page.




|  |  |
| --- | --- |
| **account** | An object representing the account for which usage data was
requested. |
| **bucket** | The unit of time for which usage data is provided. Can be either
'day' or 'month'. |
| **fromDate** | The earliest UTC timestamp for which you want to pull usage data
(inclusive). |
| **toDate** | The latest UTC timestamp for which you want to pull usage data
(exclusive). |
| **publishers** | Includes three primary objects: Used, projected, and
products. |



















Developer policy and terms


Follow @XDevelopers


Subscribe to developer news












#### 
 X platform


* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app




#### 
 X Corp.


* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors




#### 
 Help


* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us




#### 
 Developer resources


* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms




#### 
 Business resources


* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy









 © 2024 X Corp.
 


Cookies


Privacy


Terms and conditions






















**Did someone say … cookies?**  
  


 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.


 




* Accept all cookies
* Refuse non-essential cookies















