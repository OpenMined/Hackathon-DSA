
Tweet lookup standard v1.1 to v2 migration guide | Docs | Twitter Developer Platform 

Standard v1.1 compared to Twitter API v2

Standard v1.1 compared to Twitter API v2
----------------------------------------

If you have been working with the standard v1.1 GET statuses/show and GET statuses/lookup, the goal of this guide is to help you understand the similarities and differences between the standard and Twitter API v2 Tweets lookup endpoints..

You may also be interested in our visual data format migration tool to help you quickly see the differences between the Twitter API v1.1 data format and the Twitter API v2 format.

* **Similarities**
	+ OAuth 1.0a User Context
	+ Tweets per request limits
	+ Support for Tweet edit history and metadata
* **Differences**
	+ Endpoint URLs
	+ App and Project requirements
	+ Response data format
	+ Request parameters

### Similarities

#### OAuth 1.0a User Context authentication method

The standard endpoint supports OAuth 1.0a User Context, while the new Twitter API v2 Tweet lookup endpoint supports both OAuth 1.0a User Context and OAuth 2.0 App-Only. Therefore, if you were previously using one of the standard v1.1 Tweet lookup endpoints, you can continue using the same authentication method if you migrate to the Twitter API v2 version. 

Depending on your authentication library/package of choice, App-Only authentication is probably the easiest way to get started and can be set with a simple request header. To learn how to generate an App Access Token, see this OAuth 2.0 App-only guide.   

#### Tweets per request limits

The v1.1 GET statuses/lookup endpoint allows you to specify 100 Tweets per request. This also goes for the GET /tweets endpoint. To specify a full 100 Tweets, you will need to pass the ids parameter as a query parameter rather than a path parameter and include the list of Tweet IDs in a comma-separated list.   

**Support for Tweet edit history and metadata**  

Both versions provide metadata that describes any edit history. Check out the Tweet lookup API References and the Edit Tweets fundamentals page for more details. 

### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
	+ https://api.twitter.com/1.1/statuses/show
	+ https://api.twitter.com/1.1/statuses/lookup
* Twitter API v2 endpoint:
	+ https://api.twitter.com/2/tweets
	+ https://api.twitter.com/2/tweets/:id

#### 

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a developer App that is associated to a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a Project.   

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default, and then have the option to use parameters to identify which fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the Tweet id and text fields by default. To request any additional fields or objects, you will need to use the fields and expansions parameters. Any Tweet fields that you request from these endpoints will return in the primary Tweet object. Any expanded user, media, poll, or place objects and fields will return in an includes object within your response. You can then match any expanded objects back to the Tweet object by matching the IDs located in both the Tweet and the expanded object. 

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on how to use fields and expansions. 

We have also put together a data format migration guide which can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.   

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including Tweet and user objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array.
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed.
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like.
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have a non-null values.

We also introduced a new set of fields to the Tweet object including the following:

* A conversation\_id field
* Two new annotations fields, including context and entities
* Several new metrics fields
* A new reply\_setting field, which shows you who can reply to a given Tweet

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

|  |  |
| --- | --- |
| **Standard** | **Twitter API v2** |
| id | ids |

There are also a set of standard v1.1 Tweet lookup request parameters **not** supported in Twitter API v2:

| Standard | Comment |
| --- | --- |
| tweet\_mode | This parameter enables developers to request a series of different extended fields that had been introduced in the years since statuses/show and statuses/lookup were introduced. It has been replaced with the fields and expansions functionality. |
| trim\_user | This parameter is used to reduce the number of fields that deliver in the user object that comes alongside each Tweet. It has been replaced with the additive fields and expansions functionality.
To request user information alongside your requested Tweet, you will need to use a combination of the author\_id expansion and the user.fields parameter with a set of specified user fields. |
| include\_my\_retweet | This parameter includes the ID of the source Tweet for those specified Tweets that were Retweeted by the authenticating user. |
| include\_entities | This parameter is used to remove the entities node from the Tweet payload. It has been replaced with the additive fields and expansions functionality. |
| include\_ext\_alt\_text | This parameter adds an additional ext\_alt\_text field in the media entity if that media has alt text attached to it. |
| include\_card\_uri | This parameters adds a card\_uri attribute when there is an ads card attached. |
| map | This parameter would return the Tweet ID and nullified fields for unavailable Tweets. 
In v2, we return the Tweet ID and a detailed error message for unavailable Tweets. |

### cURL requests

#### The following section displays cURL requests for the standard v1.1 endpoints and their equivalent endpoints in v2.

The requests are made using OAuth 2.0 App-Only. In order to run the following cURL requests, you will need to replace ACCESS\_TOKEN in the authorization header with your app access token. For v2 endpoints, your app access token must belong to a developer App within a Project. 

The response payloads returned by v1.1 endpoints will be different from the response payloads returned by v2 endpoints. With v2, responses will include the default fields, as well as any other fields requested with the fields and expansions parameters. You can use these parameters to request a different set of fields to be returned.  

**Standard v1.1 GET statuses/lookup and v2 GET /tweets endpoints**

```
      curl --request GET \
  --url 'https://api.twitter.com/1.1/statuses/lookup.json?id=1460323737035677698%2C1460323743339741184' \
  --header 'Authorization: Bearer $ACCESS_TOKEN' 
```

Code copied to clipboard

```
      curl --request GET \
  --url 'https://api.twitter.com/2/tweets?ids=1460323737035677698%2C1460323743339741184&tweet.fields=created_at&expansions=author_id&user.fields=created_at' \
  --header 'Authorization: Bearer $ACCESS_TOKEN'
```

Code copied to clipboard

**Standard v1.1 GET statuses/show/:id and v2 GET /tweets/:id endpoints**

```
      curl --request GET \
  --url 'https://api.twitter.com/1.1/statuses/show.json?id=1460323737035677698' \
  --header 'Authorization: Bearer $ACCESS_TOKEN'
```

Code copied to clipboard

```
      curl --request GET \
  --url 'https://api.twitter.com/2/tweets/1460323737035677698?tweet.fields=created_at&expansions=author_id&user.fields=created_at' \
  --header 'Authorization: Bearer $ACCESS_TOKEN'
```

Code copied to clipboard

Next steps
----------

Quick start guide

API reference

Sample code

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