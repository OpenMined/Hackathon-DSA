
User profile images and banners | Docs | Twitter Developer Platform 

User profile images and banners

Profile images
--------------

Profile images (also known as avatars) are an important component of a Twitter account’s expression of identity. Use POST account/update\_profile\_image to upload a profile image on behalf of a user.  

### Alternative image sizes for user profile images¶

Obtain a user’s most recent profile image, along with the other components comprising their identity on Twitter, from GET users/show. The user object contains the `profile\_image\_url` and `profile\_image\_url\_https` fields. These fields will contain the resized “normal” variant of the user’s uploaded image. This “normal” variant is typically 48px by 48px.

By modifying the URL, it is possible to retrieve other variant sizings such as “bigger”, “mini”, and “original”. Consult the table below for more examples:

| Variant | Dimensions | Example URL |
| normal | 48x48 | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_normal.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_normal.png |
| bigger | 73x73 | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_bigger.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_bigger.png |
| mini | 24x24 | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_mini.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3\_mini.png |
| original | original | http://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3.png https://pbs.twimg.com/profile\_images/2284174872/7df3h38zabcvjylnyfe3.png
*Omit the underscore and variant to retrieve the original image. The images can be very large.* |

### Default profile images¶

Some users may not have uploaded a profile image. Users who have not uploaded a profile image can be identified by the `default\_profile\_image` field of their user object having a `true` value.

The `profile\_image\_url` and `profile\_image\_url\_https` URLs provided for users in this case will indicate Twitter’s default profile photo, which is https://abs.twimg.com/sticky/default\_profile\_images/default\_profile\_normal.png.

The table above can be used to determine how to retrieve different size variants of the default image.  

### Outdated profile images¶

If a 403 or 404 error is returned when trying to access a profile image, refresh the user object using GET users/show to retrieve the most recent `profile\_image\_url` or `profile\_image\_url\_https`. The URL may have changed, which happens for instance when the user updates their profile image.  

Profile banners¶
----------------

Profile banners allow users to further customize the expressiveness of their profiles. Use POST account/update\_profile\_banner to upload a profile banner on behalf of a user.

Profile banners come in a variety of display-enhanced sizes. The variant sizes are available through a request to GET users/profile\_banner or by modifying the final path component of the `profile\_banner\_url` found in a user object according to the table below.

The profile banner data available at each size variant’s URL is in PNG format.

The following sizes are available:

| Dimensions | Example URL |
| 1500x500 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/1500x500 |
| 600x200 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/600x200 |
| 300x100 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/300x100 |

The following sizes are available for the certain screen types:

| Screen Type | Dimensions | Example URL |
| web | 520x260 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/web |
| web\_retina | 1040x520 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/web\_retina |
| ipad | 626x313 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/ipad |
| ipad\_retina | 1252x626 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/ipad\_retina |
| mobile | 320x160 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/mobile |
| mobile\_retina | 640x320 | https://pbs.twimg.com/profile\_banners/6253282/1431474710/mobile\_retina |

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