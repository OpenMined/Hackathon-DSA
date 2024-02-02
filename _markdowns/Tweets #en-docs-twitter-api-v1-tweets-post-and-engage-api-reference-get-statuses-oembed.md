



GET statuses/oembed | Docs | Twitter Developer Platform 





































































































GET statuses/oembed



get-statuses-oembed

GET statuses/oembed
===================




Returns a single Tweet, specified by either a Tweet web URL or the
Tweet ID, in an oEmbed-compatible
format. The returned HTML snippet will be automatically recognized as an
Embedded Tweet when Twitter's widget JavaScript is included
on the page.


The oEmbed endpoint allows customization of the final appearance of
an Embedded Tweet by setting the corresponding properties in HTML markup
to be interpreted by Twitter's JavaScript bundled with the HTML response
by default. The format of the returned markup may change over time as
Twitter adds new features or adjusts its Tweet representation.


The Tweet fallback markup is meant to be cached on your servers for
up to the suggested cache lifetime specified in the
`cache_age`.


Resource Information¶
---------------------




|  |  |
| --- | --- |
| **Resource URL** | `https://publish.twitter.com/oembed` |
| **Response formats** | JSON |
| **Requires authentication?** | No |
| **Rate limited?** | No |


Parameters¶
-----------




| Name | Default | Description |
| --- | --- | --- |
| `url`requiredString |  | The URL of the Tweet to be embedded |
| `maxwidth`Int `[220..550]` | `325` | The maximum width of a rendered Tweet in whole pixels. A supplied
value under or over the allowed range will be returned as the minimum or
maximum supported width respectively; the reset width value will be
reflected in the returned `width` property. Note that Twitter
does not support the oEmbed `maxheight` parameter. Tweets are
fundamentally text, and are therefore of unpredictable height that
cannot be scaled like an image or video. Relatedly, the oEmbed response
will not provide a value for `height`. Implementations that
need consistent heights for Tweets should refer to the
`hide_thread` and `hide_media` parameters
below. |
| `hide_media`Boolean, String or Int | `false` | When set to `true`, `"t"`, or `1`
links in a Tweet are not expanded to photo, video, or link
previews. |
| `hide_thread`Boolean, String or Int | `false` | When set to `true`, `"t"`, or `1` a
collapsed version of the previous Tweet in a conversation thread will
not be displayed when the requested Tweet is in reply to another
Tweet. |
| `omit_script`Boolean, String or Int | `false` | When set to `true`, `"t"`, or `1`
the `<script>` responsible for loading
`widgets.js` will not be returned. Your webpages should
include their own reference to `widgets.js` for use across
all Twitter widgets including Embedded
Tweets. |
| `align`Enum
`{left,right,center,none}` | `none` | Specifies whether the embedded Tweet should be floated left, right,
or center in the page relative to the parent element. |
| `related`String |  | A comma-separated list of Twitter usernames related to your content.
This value will be forwarded to Tweet action
intents if a viewer chooses to reply, like, or retweet the embedded
Tweet. |
| `lang`Enum(Language) | `en` | Request returned HTML and a rendered Tweet in the specified Twitter language supported by embedded
Tweets. |
| `theme`Enum `{light, dark}` | `light` | When set to `dark`, the Tweet is displayed with light
text over a dark background. |
| `link_color`String |  | Adjust the color of Tweet text links with a hexadecimal
color value. |
| `widget_type`Enum `{video}` |  | Set to `video` to return a Twitter Video embed for the
given Tweet. |
| `dnt`Boolean | `false` | When set to `true`, the Tweet and its embedded page on
your site are not used for purposes that include personalized
suggestions and personalized
ads. |


Example Request¶
----------------



```
curl 'https://publish.twitter.com/oembed?url=https%3A%2F%2Ftwitter.com%2FInterior%2Fstatus%2F507185938620219395'
```

Example Response¶
-----------------



```
{
  "url": "https://twitter.com/Interior/status/507185938620219395",
  "author_name": "US Dept of Interior",
  "author_url": "https://twitter.com/Interior",
  "html": "<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Happy 50th anniversary to the Wilderness Act! Here&#39;s a great wilderness photo from <a href="https://twitter.com/YosemiteNPS">@YosemiteNPS</a>. <a href="https://twitter.com/hashtag/Wilderness50?src=hash">#Wilderness50</a> <a href="http://t.co/HMhbyTg18X">pic.twitter.com/HMhbyTg18X</a></p>&mdash; US Dept of Interior (@Interior) <a href="https://twitter.com/Interior/status/507185938620219395">September 3, 2014</a></blockquote>n<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>",
  "width": 550,
  "height": null,
  "type": "rich",
  "cache_age": "3153600000",
  "provider_name": "Twitter",
  "provider_url": "https://twitter.com",
  "version": "1.0"
}
```


















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















