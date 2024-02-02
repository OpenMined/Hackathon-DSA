



Attaching media | Docs | Twitter Developer Platform 





































































































Attaching media



Attaching media
---------------


POST direct\_messages/events/new supports media attachments of type image, GIF and video. The process is similar to attaching media to Tweets:


1. Chunk upload the image, GIF or video.
2. Send Direct Message with media attachment.


It is possible to attach the same media asset to multiple Direct Messages. However, you must get users’ express consent to set media as “shared,” and must provide them with clear notice that “shared” media will be viewable by anyone with the media’s URL. See the documented process below for how to set media to "shared."


**Note:** Media for use with Direct Messages should be uploaded using the asynchronous chunked upload process described on this page.  

 


### 1. Chunk upload media


* Chunk upload the media file starting with POST media/upload (INIT).
* Set the media\_category to dm\_image, dm\_gif or dm\_video appropriately.
* If reusing the media asset across multiple Direct Messages, you must set shared to true during the initial upload.
* If attaching a media asset to a Welcome Message, you must set shared to true during the initial upload.
* Uploaded media can only be shared across Direct Messages created by the same user.
* See Uploading Media for subsequent APPEND and FINALIZE steps.
* The returned media ID will be used when sending the Direct Message. If you did not set shared to true the media ID can only be used in a single Direct Message.


Once a media ID is generated, it must be attached to a Direct Message within 24 hours.


#### Parameters




|  |  |
| --- | --- |
| **media\_category**(required) | The media category: dm\_image, dm\_gif, dm\_video |
| **shared** | Set to true if media asset will be reused for multiple Direct Messages. Default is false. |


See POST media/upload (INIT) documentation for all parameters and full details.  

 


### 2. Send Direct Message with media attachment


* Define an attachment object in the message\_data object in the Direct Message event json body.
* Set attachment type property to media.
* Set the media.id property to the media ID returned in the previous chunk upload process.


#### Parameters




|  |  |
| --- | --- |
| **attachment.type**(required) | Must be set to media. |
| **attachment.media.id**(required) | A media ID to associate with the message. A Direct Message may only reference a single media id. |


See POST direct\_messages/events/new documentation for all parameters and full details.



















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















