



Introduction | Docs | Twitter Developer Platform 





































































































Introduction



Introduction
------------


Twitter is committed to our community of developers who build with the Twitter API. As part of this commitment, we aim to make our API open and fair to developers, safe for people on Twitter, and beneficial for the Twitter platform as a whole. It is crucial that any developer who stores Twitter content offline, ensures the data reflects user intent and the current state of content on Twitter. For example,when someone on Twitter deletes a Tweet or their account, protects their Tweets, or scrubs the geo information from their Tweets, it is critical for both Twitter and our developers to honor that person’s expectations and intent. The batch compliance endpoints provide developers an easy tool to help maintain Twitter data in compliance with the Twitter Developer Agreement and Policy. 


These batch compliance endpoints allow you to upload large datasets of Tweet or user IDs to retrieve their compliance status in order to determine what data requires action in order to bring your datasets into compliance. Please note, use of the batch compliance endpoints is restricted to aforementioned use cases, and any other purpose is prohibited and may result in enforcement action.






Typically, there are 4 steps involved in working with this endpoint:


1. **Create a compliance job**  

You can specify the job type (with the value tweets or users to indicate whether the dataset you want to upload has Tweet IDs or user IDs. You can have one concurrent job per job type at any time.
2. **Upload your dataset to the upload\_url**  

Next, you upload your dataset as a plain text file to the provided upload\_url, with each line of the file containing a single Tweet ID or user ID. The upload\_url expires after 15 minutes.
3. **(Optional) Check the job status**  

You can check the status of your compliance job to see whether it is created, in\_progress, failed or complete.
4. **Download the results**  

When your job is complete, you can download the results using the download\_url. The download\_url expires after one week (from when the job was created).  

  

This result will contain a set of JSON objects (one object per line). Each object will contain a Tweet ID, the Tweet’s creation date (useful to locate Tweets organized by date), required action, the reason for the compliance action, and the date the user was suspended.


 


You will receive the following compliance event types in your results:


* deleted - indicates that the Tweet or User account was deleted
* deactivated - indicates that the Tweet or User account has been deactivated
* scrub\_geo - indicates that the geo information associated with the Tweet or User was removed
* protected - indicates the account that made the Tweet became private
* suspended - indicates the account that made the Tweet was suspended











**Account setup**


To access these endpoints, you will need:


* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.


Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.












Quick start


Jump to example requests


Python client


Run in Postman


Try with API Explorer











Supporting resources
--------------------






Learn how to use Postman to make requests


Troubleshoot an error


Visit the API reference page for this endpoint



















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















