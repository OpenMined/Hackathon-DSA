



POST
account/update\_profile\_banner | Docs | Twitter Developer Platform 





































































































POST
account/update\_profile\_banner



post-account-update\_profile\_banner

POST
account/update\_profile\_banner
====================================




Uploads a profile banner on behalf of the authenticating user. More
information about sizing variations can be found in User
Profile Images and Banners and GET
users / profile\_banner.


Profile banner images are processed asynchronously. The
profile\_banner\_url and its variant sizes will not necessary be available
directly after upload.


HTTP Response Codes¶
--------------------




|  |  |
| --- | --- |
| Code(s) | Meaning |
| 200, 201, 202 | Profile banner image successfully uploaded |
| 400 | Either an image was not provided, or the image data could not be
processed |
| 422 | The image could not be resized, or is too large. |


Resource URL¶
-------------


`https://api.twitter.com/1.1/account/update_profile_banner.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| banner | required | The Base64-encoded or raw image data being uploaded as the user's
new profile banner. |  |  |
| width | optional | The width of the preferred section of the image being uploaded in
pixels. Use with *height* , *offset\_left* , and
*offset\_top* to select the desired region of the image to
use. |  |  |
| height | optional | The height of the preferred section of the image being uploaded in
pixels. Use with *width* , *offset\_left* , and
*offset\_top* to select the desired region of the image to
use. |  |  |
| offset\_left | optional | The number of pixels by which to offset the uploaded image from the
left. Use with *height* , *width* , and
*offset\_top* to select the desired region of the image to
use. |  |  |
| offset\_top | optional | The number of pixels by which to offset the uploaded image from the
top. Use with *height* , *width* , and
*offset\_left* to select the desired region of the image to
use. |  |  |


Example Request¶
----------------


`POST https://api.twitter.com/1.1/account/update_profile_banner.json?width=1500&height=500&offset_top=0&offset_left=0&banner=FILE_DATA`



















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















