



Make your first request to the Twitter API | Docs | Twitter Developer Platform 





































































































Make your first request



Make your first request to the Twitter API
------------------------------------------


This guide will walk you through some steps that you could follow to make your first request. This is a great resource to help you once you’ve signed up for a Twitter account. 


If you are interested in using code samples, more technical guides, or a graphical tool like Postman, please consider using the following guides to make your first request:


* Step-by-step guide to making your first request to the Twitter API
* A quick start guide to making your first request to the post Tweet endpoint
* Getting started with Postman - best for beginners
* Twitter API v2 code samples
* Tweet lookup API reference


This guide assumes that you have collected your API key and secret, user Access Token and Secret, App Access Token, and have stored them in a secure location. You can learn how to do this by following the steps in the getting access to the Twitter API guide.   

 


### Step 1. Identify which endpoint you would like to use


The Twitter API allows you to perform a variety of different actions using code that you might be able to perform on the Twitter website or mobile application. 


We have a complete list of the endpoints that are available via the API listed within our API Reference Index, but we recommend sticking to one of the following for simplicity’s sake:


* Manage Tweets > Post a Tweet
* Search Tweets
* User lookup


 


### Step 2. Choose a tool to make your request


While some requests can be straightforward, others can be tricky to build. That’s why the amazing community of developers have developed tools to abstract away some of the complexity. 


The following are some recommended tools and details on how to use them:


#### Postman


Postman is a visual tool that you can use to make requests to REST endpoints. We’ve created some great materials around Postman to help you get started with and explore the different endpoints available via the Twitter API. 


We recommend you read through our "Getting started with Postman" tutorial to learn how to add your keys and tokens and make your first request. 


We’ve also produced a quick start guide for each of our Twitter API v2 endpoints, most of which use Postman. You can find these guides in each respective endpoint section, but here is a link to a few:


* Quick start: Post a Tweet
* Quick start: Search for Tweets
* Quick start: Lookup a user


Please note that you can’t make requests to streaming endpoints using Postman. Please visit the filtered stream or 1% ampled stream quick start guide to learn how to work with those endpoints.


If you prefer a more simple graphical tool, you should also consider using Insomnia.   

 


#### Sample code


If you are interested in using some simple code to make your request, we’ve put together sample code in multiple different languages for each of our Twitter API v2 endpoints. 


You can find the code samples via our Github repo, Twitter-API-v2-sample-code, which also contains a README file that you can use to learn how to set up your credentials to properly work with the requests. 


For example, here is a cURL example for the user lookup endpoint. All you have to do to use this request is replace the $ACCESS\_TOKEN and $USERNAME with your App Access Token and Twitter handle. Then, copy and paste this code into your command line tool and press ‘Return’ or ‘Enter’.












```

      curl "https://api.twitter.com/2/users/by/username/$USERNAME" -H "Authorization: Bearer $ACCESS_TOKEN"

    
```





Code copied to clipboard








### 


#### Libraries


The amazing TwitterDev community has also built libraries in a variety of different coding languages that can be used to make requests to the Twitter API.


We’ve built out a "Tools and libraries" page that lists all of the community libraries that we are aware of. Each library should have a ReadMe file that can be used to learn how to set up the repo on your machine and make your first request.


 













|  |
| --- |
| **Please note:** If you run into any problems, please read through our developer docs for the endpoint that you are making a request to, our support section, or reach out to the community on our forums for help. We’ll get you to a successful request! |









### Step 3. Review the response


Once you’ve made a successful request, you will receive a payload with metadata related to the request. 


If you used an endpoint that utilizes a GET HTTP method, you will receive metadata related to the resource (Tweet, user, List, Space, etc) that you made the request to in JSON format. Review the different fields that returned and see if you can map the information that you requested to the content on Twitter.


If you used an endpoint that utilizes a POST, PUT, or DELETE HTTP method, you performed an action on Twitter. Go to Twitter.com or the mobile app and see if you can track down that action. 


 


### Step 4. Adjust your request using parameters


Each endpoint has a different set of parameters that you can use to alter your request. For example, you can request additional metadata fields when using GET endpoints with the fields and expansions parameters. You can also experiment with a variety of different filtering tools with endpoints such as search Tweets, Tweet counts, and filtered stream to help narrow down the data you receive to just those Tweets that you are interested in. 


You can find a full list of the request parameters and fields in the API Reference for the endpoint that you are working with, and a host of other helpful integration information in our integration guides and fundamentals pages. 


You can learn more about all of the educational materials we’ve made available to you via our Important resources guide. 


 



















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















