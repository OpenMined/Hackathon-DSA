
Retrieving media | Docs | Twitter Developer Platform 

Retrieving media

Retrieving media
----------------

Media in direct messages must be retrieved via an authenticated app-user GET request.  It is advised that applications store user's access tokens to use for direct message media retrieval.

For media in direct messages, `media_url` is the same https URL as `media_url_https` and must be accessed by signing a request with the user’s access token using OAuth 1.0A.

You can no longer access media via an authenticated www.twitter.com session. We cannot prescribe how you should update your integration if you are affected by this change. However, here is one implementation path to address this that we endorse:

* Make sure you’re storing a user’s Twitter access token, if you’re not already
* Set up an endpoint to make OAuth requests to Twitter to retrieve DM images on behalf of the user using the user’s Twitter access token:
	+ The endpoint should be a GET endpoint
	+ The endpoint must be authenticated
	+ The endpoint must deny all cross-origin requests
	+ The endpoint must only be used for making requests to retrieve DM images, and must deny requests to other Twitter APIs

Example request:

```
      curl --request GET \
  --url https://ton.twitter.com/1.1/ton/data/dm/1034828552951160836/1034828533812486145/oP5p359h.jpg \
  --header 'authorization: OAuth 
oauth_consumer_key="6NxxxxxxCS", 
oauth_nonce="Sbxxxxxx2G", 
oauth_signature="637xxxxxxM%3D", 
oauth_signature_method="HMAC-SHA1", 
oauth_timestamp="1535557741", 
oauth_token="600-SQxxxxxxcqIF", 
oauth_version="1.0"'
```

Code copied to clipboard

If you display images in a web interface, the URL from the newly created endpoint could be used in a <img> tag to display to users of your products.

Example:

```
      <img src="fetch_dm_image?url=https://ton.twitter.com/i/ton/data/dm/xx.jpg">
```

Code copied to clipboard

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