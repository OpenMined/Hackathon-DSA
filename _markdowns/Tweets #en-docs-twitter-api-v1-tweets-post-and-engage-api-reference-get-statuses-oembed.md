<div>

::: c01-rich-text-editor
Returns a single Tweet, specified by either a Tweet web URL or the Tweet
ID, in an [oEmbed](http://oembed.com/) -compatible format. The returned
HTML snippet will be automatically recognized as an [Embedded
Tweet](/web/embedded-tweets) when [Twitter\'s widget JavaScript is
included on the page](/web/javascript/loading) .

The oEmbed endpoint allows customization of the final appearance of an
Embedded Tweet by setting the corresponding properties in HTML markup to
be interpreted by Twitter\'s JavaScript bundled with the HTML response
by default. The format of the returned markup may change over time as
Twitter adds new features or adjusts its Tweet representation.

The Tweet fallback markup is meant to be cached on your servers for up
to the suggested cache lifetime specified in the ` cache_age ` .

  ------------------------------ ----------------------------------------
  **Resource URL**               ` https://publish.twitter.com/oembed `
  **Response formats**           JSON
  **Requires authentication?**   No
  **Rate limited?**              No
  ------------------------------ ----------------------------------------

## Parameters [¶](#parameters){.headerlink}

  --------------------------------------------------------------------------------------------- ----------------------- --------------------------------------------------------------
  ` url ` [ required ]{.required}\                                                                                      The URL of the Tweet to be embedded
  String                                                                                                                

  ` maxwidth `\                                                                                 ` 325 `                 The maximum width of a rendered Tweet in whole pixels. A
  Int ` [220..550] `                                                                                                    supplied value under or over the allowed range will be
                                                                                                                        returned as the minimum or maximum supported width
                                                                                                                        respectively; the reset width value will be reflected in the
                                                                                                                        returned ` width ` property. Note that Twitter does not
                                                                                                                        support the oEmbed ` maxheight ` parameter. Tweets are
                                                                                                                        fundamentally text, and are therefore of unpredictable height
                                                                                                                        that cannot be scaled like an image or video. Relatedly, the
                                                                                                                        oEmbed response will not provide a value for ` height ` .
                                                                                                                        Implementations that need consistent heights for Tweets should
                                                                                                                        refer to the ` hide_thread ` and ` hide_media ` parameters
                                                                                                                        below.

  ` hide_media `\                                                                               ` false `               When set to ` true ` , ` "t" ` , or ` 1 ` links in a Tweet are
  Boolean, String or Int                                                                                                not expanded to photo, video, or link previews.

  ` hide_thread `\                                                                              ` false `               When set to ` true ` , ` "t" ` , or ` 1 ` a collapsed version
  Boolean, String or Int                                                                                                of the previous Tweet in a conversation thread will not be
                                                                                                                        displayed when the requested Tweet is in reply to another
                                                                                                                        Tweet.

  ` omit_script `\                                                                              ` false `               When set to ` true ` , ` "t" ` , or ` 1 ` the ` <script> `
  Boolean, String or Int                                                                                                responsible for loading ` widgets.js ` will not be returned.
                                                                                                                        Your webpages should include their own reference to
                                                                                                                        ` widgets.js ` for use across all Twitter widgets including
                                                                                                                        [Embedded Tweets](/web/embedded-tweets) .

  ` align `\                                                                                    ` none `                Specifies whether the embedded Tweet should be floated left,
  Enum ` {left,right,center,none} `                                                                                     right, or center in the page relative to the parent element.

  ` related `\                                                                                                          A comma-separated list of Twitter usernames related to your
  String                                                                                                                content. This value will be forwarded to [Tweet action
                                                                                                                        intents](/web/intents) if a viewer chooses to reply, like, or
                                                                                                                        retweet the embedded Tweet.

  ` lang `\                                                                                     ` en `                  Request returned HTML and a rendered Tweet in the specified
  Enum(                                                                                                                 [Twitter language supported by embedded
  [Language](/en/docs/twitter-for-websites/twitter-for-websites-supported-languages/overview) )                         Tweets](/web/overview/languages) .

  ` theme `\                                                                                    ` light `               When set to ` dark ` , the Tweet is displayed with light text
  Enum ` {light, dark} `                                                                                                over a dark background.

  ` link_color `\                                                                                                       Adjust the color of Tweet text links with a [hexadecimal color
  String                                                                                                                value](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet) .

  ` widget_type `\                                                                                                      Set to ` video ` to return a Twitter Video embed for the given
  Enum ` {video} `                                                                                                      Tweet.

  ` dnt `\                                                                                      ` false `               When set to ` true ` , the Tweet and its embedded page on your
  Boolean                                                                                                               site are not used for purposes that include [personalized
                                                                                                                        suggestions](https://support.twitter.com/articles/20169421)
                                                                                                                        and [personalized
                                                                                                                        ads](https://support.twitter.com/articles/20170405) .
  --------------------------------------------------------------------------------------------- ----------------------- --------------------------------------------------------------

## Example Request [¶](#example-request){.headerlink}

``` bash
curl 'https://publish.twitter.com/oembed?url=https%3A%2F%2Ftwitter.com%2FInterior%2Fstatus%2F507185938620219395'
```

## Example Response [¶](#example-response){.headerlink}

``` json
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
:::

</div>
