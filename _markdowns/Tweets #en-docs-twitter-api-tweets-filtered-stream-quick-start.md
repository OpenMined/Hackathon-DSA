



Filtered stream quick start guide | Docs | Twitter Developer Platform 





































































































Quick start



Getting started with the filtered stream endpoints
--------------------------------------------------


This quick start guide will help you make your first request to the filtered stream endpoint group using a cURL request. cURL is a command line tool which allows you to make requests with minimal configuration.


If you would like to see sample code in different languages, please visit our Twitter API v2 sample code GitHub repository. 











### Prerequisites


To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:


* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.









 


### Steps to build a filtered stream request using cURL


#### Step one: Create a rule


Rules are made up of one or many different operators that are combined using boolean logic and parentheses to help define which Tweets will deliver to your stream. In this guide, we will filter the stream to find Tweets that contain both the keyword “cat” and images. Here is our rule:


cat has:images


#### 
Step two: Add a tag to your rule


You can add multiple concurrent rules to your stream. When you open your streaming connection, Tweets that match any of these rules will flow through the same streaming connection. To ensure that you know which Tweet matches which rule, you can pass a tag along with your rule creation request. Each Tweet that matches that rule will then include a tag field within the Tweet payload noting which rule it matched. For this rule, we are going to assign the following tag:


cats with images


#### 
Step three: Add your rule to the stream


This endpoint requires you to pass an application/JSON body along with this request that contains your rule and its tag. You will also notice that we have included the rule value and tag within an add object since we are trying to add this rule to the stream. This JSON body will look like this:



```

{
  "add": [
    {"value": "cat has:images", "tag": "cats with images"}
  ]
}

```

  

Now that you have fully set up this JSON body, you can add that to a cURL request, which will look like the following. This request isn't ready yet, so please hold off on submitting it until a later step.












```

      curl -X POST 'https://api.twitter.com/2/tweets/search/stream/rules' \
-H "Content-type: application/json" \
-H "Authorization: Bearer $APP_ACCESS_TOKEN" -d \
'{
  "add": [
    {"value": "cat has:images", "tag": "cats with images"}
  ]
}'

    
```





Code copied to clipboard








#### 
Step four: Authenticate your request


Since the filtered stream rules endpoints require OAuth 2.0 App-Only authentication, you will need to replace $APP\_ACCESS\_TOKEN in the cURL command from step three with the App Access Token that you generated in the prerequisites.   

 


#### Step five: Add your rule to the stream


Next step is to execute your cURL request, which will add the rule to your stream. Copy and paste the cURL command into your command line interface and press "return". 


If your cURL request was successful, you’ll receive a response containing data about your value, tag, and id (serves as a unique identifier for your rule). This response will look similar to this:  

 












```

      {
	"data": [{
		"value": "cat has:images",
		"tag": "cats with images",
		"id": "1273026480692322304"
	}],
	"meta": {
		"sent": "2020-06-16T22:55:39.356Z",
		"summary": {
			"created": 1,
			"not_created": 0,
			"valid": 1,
			"invalid": 0
		}
	}
}

    
```






  

  

You can validate that your rule was added successfully by sending the following GET request to the rules endpoint, once again making sure to replace $APP\_ACCESS\_TOKEN with your token. This request will return a full list of all the rules that have been added to your stream.












```

      curl -X GET 'https://api.twitter.com/2/tweets/search/stream/rules' \
-H "Authorization: Bearer $APP_ACCESS_TOKEN" 

    
```





Code copied to clipboard








  

If your cURL request was successful, you should receive the following:  

 












```

      {
	"data": [{
		"id": "1273028376882589696",
		"value": "cat has:images",
		"tag": "cats with images"
	}],
	"meta": {
		"sent": "2020-06-16T23:14:06.498Z"
	}
}

    
```






#### 
Step six: Identify and specify which fields you would like to retrieve


If you connect to the stream after step five, you will receive the default Tweet object fields in your response: id , text, and edit\_history\_tweet\_ids. If you would like to receive additional fields beyond these, you will have to specify those fields in your request with the field and/or expansion parameters.


For this exercise, we will request a three different sets of fields from different objects:


1. The additional tweet.created\_at field in the primary Tweet objects.
2. The associated authors’ user object’s default fields for the returned Tweets: id, name, and username
3. The additional  user.created\_at field in the associated user objects.


To request these fields, you will need to pass the following in your request:




|  |  |  |
| --- | --- | --- |
| Key | Value | Returned fields |
| tweet.fields | created\_at | tweets.created\_at |
| expansions | author\_id | includes.users.id, includes.users.name, includes.users.username |
| user.fields | created\_at | includes.users.created\_at |


Now that you know this, you can piece together your request URL to connect to the stream, which will look like this:  

 












```

      https://api.twitter.com/2/tweets/search/stream?tweet.fields=created_at&expansions=author_id&user.fields=created_at
    
```





Code copied to clipboard








#### 
Step seven: Connect to the stream and review your response


Now that your rule is in place and you’ve specified which fields you want returned, you’re ready to connect to the stream, which will deliver Tweet objects that match the rule you’ve submitted. This is what the cURL command looks like once you’ve added the URL from step six into your request:  

 












```

      curl -X GET -H "Authorization: Bearer $APP_ACCESS_TOKEN" "https://api.twitter.com/2/tweets/search/stream?tweet.fields=created_at&expansions=author_id&user.fields=created_at"
    
```





Code copied to clipboard








  

Once again, this request must be authenticated using OAuth 2.0 App-Only, so make sure to replace $APP\_ACCESS\_TOKEN with your credentials before copying and pasting it into your command line tool.


Once you are connected to the filtered stream you will start to receive Tweets that match your rules in the following JSON format:  

 












```

      
{
  "data": [
    {
      "author_id": "2244994945",
      "created_at": "2022-09-14T19:00:55.000Z",
      "id": "1228393702244134912",
      "edit_history_tweet_ids": ["1228393702244134912"],
      "text": "What did the developer write in their Valentine’s card?\n  \nwhile(true) {\n    I = Love(You);  \n}"
    },
    {
      "author_id": "2244994945",
      "created_at": "2022-09-12T17:09:56.000Z",
      "id": "1227640996038684673",
       "edit_history_tweet_ids": ["1227640996038684673"],
      "text": "Doctors: Googling stuff online does not make you a doctor\n\nDevelopers: https://t.co/mrju5ypPkb"
    },
    {
      "author_id": "2244994945",
      "created_at": "2022-09-27T20:26:41.000Z",
      "id": "1199786642791452673",
      "edit_history_tweet_ids": ["1199786642791452673"],
      "text": "C#"
    }
  ],
  "includes": {
    "users": [
      {
        "created_at": "2013-12-14T04:35:55.000Z",
        "id": "2244994945",
        "name": "Twitter Dev",
        "username": "TwitterDev"
      }
    ]
  }
}

    
```






  

If you would like to close your connection, you can press Control-C in your command line tool on either Mac or Windows systems to break the connection, or you can also close the window. 










Next steps
----------






Customize your request using the API Reference


Learn how to stream Tweets in real-time


Learn how to listen for important events


Build a trends dashboard with Twitter API Toolkit for Google Cloud


Learn how to build an app that streams real-time Tweets


Ask the community for help


Check out some sample code for these endpoints



















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















