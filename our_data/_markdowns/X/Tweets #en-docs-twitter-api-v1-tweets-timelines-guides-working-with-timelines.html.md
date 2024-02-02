
Working with timelines | Docs | Twitter Developer Platform 

Working with timelines

**Please note:**  

We launched a new version of the standard v1.1 statuses/user\_timeline and statuses/mentions\_timeline endpoints as part of Twitter API v2: Early Access. If you are currently using either of these endpoints, you can use our migration materials to start working with the newer endpoint.

Working with timelines
----------------------

The Twitter API has several methods, such as GET statuses / user\_timeline and GET statuses / home\_timeline, which return a timeline of Tweet data. Such timelines can grow very large, so there are limits to how much of a timeline a client application may fetch in a single request. Applications must therefore iterate through timeline results in order to build a more complete list.

Because of Twitter’s realtime nature and the volume of data which is constantly being added to timelines, standard paging approaches are not always effective. The goal of this page is to demonstrate the issues Twitter developers may face when paging through result sets and to give best practices for processing a timeline.

### The problem with “pages”

In an ideal world, paging would be very easy to implement. Consider the case where a timeline has 10 reverse-chronologically sorted Tweets. An application might attempt to read the entire timeline in two requests by setting a page size of 5 elements and requesting the first page, then the second page. 

The problem with this method is that Twitter timelines are constantly having new Tweets added to their front. Consider the previous example. If two new Tweets are added to the timeline between the first and second calls, the second fetch retrieves two Tweets which were returned in the previous call.

In fact, if 5 or more Tweets were added between calls, subsequent calls would eventually retrieve all the Tweets returned from the first request - making an entire API request completely redundant.

### The max\_id parameter

The solution to the issue described above is to use a technique for working with streams of data called cursoring. Instead of reading a timeline relative to the top of the list (which changes frequently), an application should read the timeline relative to the IDs of Tweets it has already processed. This is achieved through the use of the max\_id request parameter.

To use max\_id correctly, an application’s first request to a timeline endpoint should only specify a count. When processing this and subsequent responses, keep track of the lowest ID received. This ID should be passed as the value of the max\_id parameter for the next request, which will only return Tweets with IDs lower than or equal to the value of the max\_id parameter. Note that since the max\_id parameter is inclusive, the Tweet with the matching ID will actually be returned again.

### Optimizing max\_id for environments with 64-bit integers

While one redundant Tweet is not inefficient, it is still possible to optimize max\_id requests to address this problem if your platform is capable of working with 64-bit integers. **Environments where a Tweet ID cannot be represented as an integer with 64 bits of precision (such as JavaScript) should skip this step.** Subtract 1 from the lowest Tweet ID returned from the previous request and use this for the value of max\_id. It does not matter if this adjusted max\_id is a valid Tweet ID, or if it corresponds with a Tweet posted by a different user - the value is just used to decide which Tweets to filter. When adjusted in this manner, it is possible to page through a timeline without receiving redundant Tweets.

### Using since\_id for the greatest efficiency

Applications which process a timeline, wait some quantity of time, and then need to process new Tweets which have been added since the last time the timeline was processed can make one more optimization using the since\_id parameter.

Consider the previous example where Tweets 1 through 10 were processed. Now imagine that Tweets 11 through 18 were added to the timeline since the processing in the previous example began. An inefficient approach to process the new Tweets would be to iterate from the start of the list until Tweet 10 appeared. This causes two Tweets which have already been processed to be returned again.

This problem is avoided by setting the since\_id parameter to the greatest ID of all the Tweets your application has already processed. Unlike max\_id the since\_id parameter is not inclusive, so it is not necessary to adjust the ID in any way. As shown in the following image, Twitter will only return Tweets with IDs higher than the value passed for since\_id.

Applications which use both the max\_id and since\_id parameters correctly minimize the amount of redundant data they fetch and process, while retaining the ability to iterate over the entire available contents of a timeline.

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