
Pagination | Docs | Twitter Developer Platform 

Pagination

Introduction
------------

Pagination is a feature in Twitter API v2 endpoints that return more results than can be returned in a single response. When that happens, the data is returned in a series of 'pages'. Pagination refers to methods for programatically requesting all of the pages, in order to retrieve the entire result data set. Not all API endpoints support or require pagination, but it is often used when result sets are large.  

### Use cases for pagination

**To retrieve all results for a request:** Pagination should most often be used to receive all relevant data related to a specific request and parameters. Pagination is required in cases where there are more matching results than the max\_results for a request. Integrating pagination token data into looping requests will allow you to retrieve all results. Once a response is returned without a next\_token value, it can be assumed that all results have been paged through. Pagination should not be used for polling purposes. To get the most recent results since a previous request, review polling with since\_id.

**To traverse through the results of a request:** Pagination provides directional options for navigating through results from a request, using next\_token and previous\_token values from responses. These tokens can be set as the pagination\_token in the following request, to go to the next or the previous page of results.  

### Pagination token definitions

next\_token - Opaque string returned within the meta object response on endpoints which support pagination. Indicates that more results are available and can be used as the pagination\_token parameter in the next request to return the next page of results. The last page of results will not have a next\_token present.

previous\_token - Opaque string returned within the meta object response on endpoints which support pagination. Indicates that there is a previous page of results available, and can be set as the pagination\_token parameter in the next request to return the previous page of results.

pagination\_token - Parameter used in pagination requests. Set to the value of next\_token for the next page of results. Set to the value of previous\_token for the previous page of results.  

### Fundamentals of pagination

* Endpoints which use pagination, will respond to an initial request with the first page of results, and provide a next\_token within the meta object in the JSON response if additional pages of results are available. To receive all results, this process can be repeated until no next\_token is included in the response.

* Results are delivered in reverse-chronological order. This is true within individual pages, as well as across multiple pages:
	+ The first Tweet in the first response will be the most recent.
	+ The last Tweet in the last response will be the oldest.

* The max\_results request parameter enables you to configure the number of Tweets returned per response page. There will be a default max\_results and a maximum max\_results.
* Every pagination implementation will involve parsing tokens from the response payload, which can be used in subsequent requests. See below for more details on how to construct these requests.

* In some circumstances you may get less than the max\_results page of results. Do not rely on the results per page to always equal the max\_results parameter value.
* The best ways to successfully use pagination for complete results are by using loop logic within integration code, or by using a library that supports Twitter API v2.

### Pagination example

Here, there are three pages of results because max\_results is set to 100 and there are a total of ~295 Tweets created by user ID 2244994945 (@TwitterDev) between January 1st, 2019 at 17:00:00 UTC and December 12th at 00:00:00 UTC. The first Tweet on the first page (1337498609819021312) is the most recent, and the last Tweet on the third page of results (1082718487011885056) is the oldest.  

#### Initial request

```
      https://api.twitter.com/2/users/2244994945/tweets?tweet.fields=created_at&max_results=100&start_time=2019-01-01T17:00:00Z&end_time=2020-12-12T01:00:00Z
```

Code copied to clipboard

#### Sequence

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **First Request** | **Second page** | **Third page** | **Fourth page** |
| **Request Parameters** | max\_results=100
tweet.fields=created\_at
start\_time=2019-01-01T17:00:00Z
end\_time=2020-12-12T01:00:00Z | max\_results=100
tweet.fields=created\_at
start\_time=2019-01-01T17:00:00Z
end\_time=2020-12-12T01:00:00Z
pagination\_token=7140w | max\_results=100
tweet.fields=created\_at
start\_time=2019-01-01T17:00:00Z
end\_time=2020-12-12T01:00:00Z
pagination\_token=7140k9 | max\_results=100
tweet.fields=created\_at
start\_time=2019-01-01T17:00:00Z
end\_time=2020-12-12T01:00:00Z
pagination\_token=71408hi |
| **Response** | 
```
{
  "data": [
    {
      "created_at": "2020-12-11T20:44:52.000Z",
      "id": "1337498609819021312",
      "text": "Thanks to everyone who tuned in today..."
    },
    .
    .
    .
   {
      "created_at": "2020-05-06T17:24:31.000Z",
      "id": "1258085245091368960",
      "text": "It’s now easier to understand Tweet impact..."
    }
  ],
  "meta": {
    "oldest_id": "1258085245091368960",
    "newest_id": "1337498609819021312",
    "result_count": 100,
    "next_token": "7140w"
  }
}
```
 | 
```
{
  "data": [
    {
      "created_at": "2020-04-29T17:01:44.000Z",
      "id": "1255542797765013504",
      "text": "Our developer community is full of inspiring ideas..."
    },
    .
    .
    .
    {
      "created_at": "2019-11-21T16:17:23.000Z",
      "id": "1197549579035496449",
      "text": "Soon, we'll be releasing tools in..."
    }
  ],
  "meta": {
    "oldest_id": "1197549579035496449",
    "newest_id": "1255542797765013504",
    "result_count": 100,
    "next_token": "7140k9",
    "previous_token": "77qp8"
  }
}
```
 | 
```
{
  "data": [
    {
      "created_at": "2019-11-21T16:17:23.000Z",
      "id": "1197549578418941952",
      "text": "We know that some people who receive a large volume of replies may..."
    },
    .
    .
    .
    { 
      "created_at": "2019-01-08T19:19:37.000Z",
      "id": "1082718487011885056",
      "text": "Updates to Grid embeds..."
    }
  ],
  "meta": {
    "oldest_id": "1082718487011885056",
    "newest_id": "1197549578418941952",
    "result_count": 95,
    "next_token": "71408hi",
    "previous_token": "77qplte"
  }
}
```
 | 
```
{
 "meta": {
    "result_count": 0,
    "previous_token": "77qpw8l"
  }
}
```
 |
| **Actions to take for next request** | To get the next page, take the next\_token value directly from the response (7140w) and set it as the pagination\_token for the next request call. | To continue to get all results: take the next\_token value directly from the response (7140k9) and set it as the pagination\_token for the next request call.

To traverse to previous page: take the previous\_token value directly from the response (77qp8) and set it as the pagination\_token for the next request call. | To continue to get all results: take the next\_token value directly from the response (71408hi) and set it as the pagination\_token for the next request call.

To traverse to previous page: take the previous\_token value directly from the response (77qplte) and set it as the pagination\_token for the next request call. | Note that there is no next\_token, which indicates that all results have been received.

To traverse to previous page: take the previous\_token value directly from the response (77qpw8l) and set it as the pagination\_token for the next request call. |

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