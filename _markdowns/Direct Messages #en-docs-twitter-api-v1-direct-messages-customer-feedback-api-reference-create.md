



POST feedback/create.json | Docs | Twitter Developer Platform 





































































































POST feedback/create.json



create

POST feedback/create.json
=========================


Sends Feedback prompt along with a Direct Message (DM) to a specified
user. The DM message is required. Sending Feedback inherits the Direct
Message restrictions and behavior from POST
direct\_messages/events/new.


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | 1,000 and 1 per recipient |


**Note**


Handles can be added to an allowlist to receive more than 1 new
feedback request per 24 hours. Please send a list of @handles to your
account manager.


Parameters¶
-----------




|  |  |
| --- | --- |
| **type** (required) | The Feedback type. Possible values: csat, nps (case sensitive) |
| **to\_user\_id** (required) | The ID of the user who should receive the Feedback prompt in a
direct message. |
| **message** (required) | The Direct Message text used to introduce the Feedback prompt. |
| **privacy\_url** (required) | The URL to the sender’s hosted privacy policy. The sender is the
business owner of the @username. |
| **external\_id** (optional) | An open field to track case IDs, conversation IDs, etc with a max
length of 256 characters. |
| **question\_variant\_id** (optional) | The ID of the relative question variant text that will override the
default text. See NPS Question Variants and CSAT Question Variants
sections. Default value is 0 if not provided. |
| **display\_name** (optional) | Overrides the display name in the question text only (i.e. "How
likely are you to recommend <display\_name> to a friend?" Max
length of 20 characters.)Confirmation messaging uses the default
Twitter display name from the business’ profile. |
| **test** (optional) | Boolean value. Default is false. If true, we will exclude this
feedback from analytics / aggregations.This value should be used
for any testing activity. |


Example Result¶
---------------



```
{
  "created_at":"SatDec1517:58:20+00002015",
  "updated_at":"SatDec1517:59:22+00002015",
  "id":"123456789",
  "type":"nps",
  "test":false,
  "dm_id":"8989898989",
  "from_user_id":"1212121212121",
  "to_user_id":"343434343434",
  "privacy_url":"https://my­business.domain/privacy",
  "external_id":"ticket_5555",
  "question_variant_id":"3",
  "display_name":"MyBusinessName"
}
```

NPS Question Variants¶
----------------------




| ID | Text |
| --- | --- |
| 0 | What is your overall satisfaction with <display\_name>? |
| 1 | How satisfied are you with <display\_name>? |
| 2 | Overall, how satisfied were you with your recent
<display\_name> experience? |
| 3 | How would you rate the overall experience with
<display\_name>? |
| 4 | How would you rate your overall experience with
<display\_name>? |
| 5 | How would you rate your experience so far with
<display\_name>? |


CSAT Question Variants¶
-----------------------




| ID | Text |
| --- | --- |
| 0 | What is your overall satisfaction with <display\_name>? |
| 1 | How satisfied are you with <display\_name>? |
| 2 | Overall, how satisfied were you with your recent
<display\_name> experience? |
| 3 | How would you rate the overall experience with
<display\_name>? |
| 4 | How would you rate your overall experience with
<display\_name>? |
| 5 | How would you rate your experience so far with
<display\_name>? |
| 6 | How would you rate your experience on Twitter with
<display\_name>? |
| 7 | Were you satisfied with your recent experience with
<display\_name>? |
| 8 | How well does <display\_name> meet your expectations? |
| 9 | How would you rate your guest experience with
<display\_name>? |
| 10 | How would you rate your service experience with
<display\_name>? |
| 11 | How would you rate your recent service experience with
<display\_name>? |
| 12 | How would you rate the service you received from
<display\_name>? |
| 13 | Were you satisfied with the result of your interaction with
<display\_name>? |
| 14 | How would you rate the ability to resolve your issue with
<display\_name>? |
| 15 | How would you rate the response time from <display\_name>? |
| 16 | How would you rate the speed of service from
<display\_name>? |
| 17 | How would you rate the time to resolution with
<display\_name>? |
| 18 | How would you rate the time to resolve your issue with
<display\_name>? |
| 19 | How would you rate the speed of resolution with
<display\_name>? |
| 20 | How would you rate the <display\_name> advisor's
expertise? |
| 21 | How satisfied were you with the <display\_name> agent who
helped you? |
| 22 | How satisfied were you with the <display\_name> specialist who
helped you? |
| 23 | How satisfied were you with the <display\_name> representative
who helped you? |
| 24 | How would you rate your recent banking experience with
<display\_name>? |
| 25 | How would you rate the overall event experience at
<display\_name>? |
| 26 | How would you rate your bill pay experience with
<display\_name>? |
| 27 | How would you rate your purchase experience with
<display\_name>? |
| 28 | How would you rate your shopping experience with
<display\_name>? |
| 29 | How would you rate your delivery experience with
<display\_name>? |
| 30 | How would you rate your rental experience with
<display\_name>? |
| 31 | How would you rate your recent <display\_name> store
visit? |
| 32 | How would you rate your recent <display\_name> hotel stay? |
| 33 | How would you rate your recent flight with
<display\_name>? |
| 34 | How would you rate your recent ride with <display\_name>? |
| 35 | How would you rate your recent trip with <display\_name>? |
| 36 | How would you rate your recent visit to <display\_name>? |
| 37 | How would you rate your recent meal at <display\_name>? |



















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















