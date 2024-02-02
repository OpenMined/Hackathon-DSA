



Replay API | Docs | Twitter Developer Platform 





































































































Replay API



replay-api

Replay API
==========


POST
/1.1/account\_activity/replay/webhooks/:webhook\_id/subscriptions/all.json¶
--------------------------------------------------------------------------------


Submits a request to retrieve activities from up to the past five
days from all subscriptions present during the date and time windows
specified in the request. If your webhook has active user subscriptions,
you will concurrently receive those events as well. Note: We do perform
a CRC before delivering replay events.




|  |  |
| --- | --- |
| **Request Method** | HTTP POST |
| **URL** | /1.1/account\_activity/replay/webhooks/:webhook\_id/subscriptions/all.json?from\_date=yyyymmddhhmm&to\_date=yyyymmddhhmm |
| **Response Format** | JSON |
| **Requires Authentication** | Yes (application only - bearer token) |
| **Rate Limit** | 5 requests per 15 minutes. There is currently no maximum on the
number of replay jobs that can requested. |
| **from\_date** | The oldest (starting) UTC timestamp from which the events will be
provided, must be in 'yyyymmddhhmm' format. Timestamp is in minute
granularity and is inclusive (i.e. 12:00 includes the 00 minute). Valid
times must be within the last 5 days, UTC time, and no more recent than
31 minutes before the current point in time. It's recommended that the
from\_date and to\_date should be within ~2 hours. |
| **to\_date** | The latest (ending) UTC timestamp to which the event will be
provided, must be in 'yyyymmddhhmm' format. Timestamp is in minute
granularity and is exclusive (i.e. 12:30 does not include the 30th
minute of the hour). Valid times must be within the last 5 days, UTC
time, and no more recent than 10 minutes before the current point in
time. |


  

#### Responses


The following responses may be returned by the API. Most error codes
are returned with a string including additional details in the body. For
non-200 responses, you should resolve the error and try again.




| Status | Text | Error Code | Description | Message |
| --- | --- | --- | --- | --- |
| 202 | Accepted | N/A | The request was successful and the activities will be sent. | N/A |
| 400 | Bad Request | 214 | Webhook has been marked as invalid. | Webhook is marked invalid and requires a CRC check. |
| 400 | Bad Request | 357 | Query parameter is missing. | : queryParam is required. |
| 400 | Bad Request | 358 | Route or query parameter is malformed. | Unable to parse  parameter. |
| 400 | Bad Request | 360 | Route parameter is negative. | webhook\_id: [] is not greater than or equal to 0. |
| 400 | Bad Request | 368 | from\_date or to\_date is not in the past. | : [<field\_value>] is not in the past. |
| 400 | Bad Request | 356 | from\_date must be before to\_date. | from\_date must be before to\_date. |
| 400 | Bad Request | 356 | from\_date must be within the past 5 days. | from\_date must be within the past 5 days. |
| 401 | Unauthorized | 32 | HTTP authentication failed due to 3-legged auth provided. | Invalid authentication method. Please use application-only
authentication. |
| 401 | Unauthorized | 61 | Client is not permitted to request this method. | Client is not permitted to request this method. |
| 403 | Forbidden | 200 | Client does not have an enterprise account with Replay enabled. | Account Activity API enterprise account with replay is required.
Please confirm you have an enterprise account and replay is
enabled. |
| 404 | Not Found | 34 | Non-existing webhook\_id; webhook\_id-application\_id mismatch. | Webhook does not exist or is associated with a different twitter
application. |
| 409 | Conflict | 355 | There is a request in flight and it will need to finish processing
before making another. | A replay job is already in progress for this webhook. |
| 429 | Too Many Requests | 88 | Rate limited (hit limit of the number of requests per time
period) | Too many requests. Please back off your API request rate. |
| 500 | Internal Server Error | 0 | Internal server error. | Internal server error. |
| 503 | Service Unavailable | 67 | One or more dependent services at Twitter is unavailable. | Twitter server error. Retry using an exponential backoff
pattern. |


  

#### "Job completed successfully”
message


Once your job successfully completes, Account Activity Replay API
will deliver the following job completion event. Once you receive this
event, the job has finished running and another can be submitted.



```


{
  "replay_job_status": {
    "webhook_id": "1234577122340233217",
    "job_state": "Complete",
    "job_state_description": "Job completed successfully"
    "job_id": "1095098195724558337"
  }
}

```

#### "Job failed to complete"
message


In the event your job does not complete successfully, we will return
the following message encouraging you to retry your Replay job. Once you
receive this event, the job has finished running and another can be
submitted.



```

{
  "replay_job_status": {
    "webhook_id": "123451374207332352",
    "job_state": "Incomplete",
    "job_state_description": "Job failed to deliver all events, please retry your replay job",
    "job_id": "1093226942650736640"
  }
}

```

#### Example curl request



```
curl --request POST  --url 'https://api.twitter.com/1.1/account_activity/replay/webhooks/:webhook_id/subscriptions/all.json?from_date=yyyymmddhhmm&to_date=yyyymmddhhmm'
--header 'authorization: Bearer TOKEN'
```

#### Example response



```

HTTP 202

{
  "job_id": "1234567890",
  "created_at": "2016-06-02T23:54:02Z"
}

```


















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















