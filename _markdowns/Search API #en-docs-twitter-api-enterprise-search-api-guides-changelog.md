::: is-table-default
That article discusses how the historical changes of the full-archive
roadmap affects creating the filters needed to find your historical
signal of interest. This article and a complementary [article about
Historical
PowerTrack](/en/docs/twitter-api/enterprise/historical-powertrack-api/guides/hpt-timeline)
, will serve as a 'compare and contrast' discussion of the two Twitter
historical products.\

### Product overview

The enterprise-tier Full-archive Search was launched in August 2015, and
the premium-tier version was launched in February 2018. These search
products enable customers to immediately access any publicly available
Tweet. With Full-archive Search you submit a single query and receive a
response in classic RESTful fashion. Full-archive Search implements (up
to) 500-Tweets-per-response pagination, and supports up to a
60-requests-per-minute (rpm) rate-limit for premium, 120 rpm for
enterprise. Given these details, Full-archive Search can be used to
rapidly retrieve Tweets, and at large scale using concurrent requests.

Unlike Historical PowerTrack, whose archive is based on a set of Tweet
flat-files on disk, the Full-archive Search Tweet archive is much like
an on-line database. As with all databases, it supports making queries
on its contents. It also makes use of an *index* to enable
high-performance data retrieval. With Full-archive search endpoints, the
querying language is made up of PowerTrack Operators, and these
Operators each correspond to a Tweet JSON attribute that is indexed.

Also, like Historical PowerTrack, there are Tweet attributes that are
current to the time a query is made. For example, if you are using
Search API to access a Tweet posted in 2010 today, the user\'s profile
description, account \'home\' location, display name, and Tweet metrics
for Favorites and Retweet counts will be updated to today's values and
not what they were in 2010.

### Metadata timelines

Below is a timeline of when Full-archive search endpoint Operators begin
matching. In some cases Operator matching began well *after* a
'communication convention' became commonplace on Twitter. For example,
\@Replies emerged as a user convention in 2006, but did not become a
*first-class object* or *event* with 'supporting' JSON until early 2007.
Accordingly, matching on \@Replies in 2006 requires an examination of
the Tweet body, rather than relying on the ` to: ` and
` in_reply_to_status_id: ` PowerTrack Operators.

The details provided here were generated using Full-Archive Search (a
product of hundreds of searches). This timeline is not 100% complete or
precise. If you identify another filtering/metadata "born on date"
fundamental to your use-case, please let us know.

Note that the underlying Search index is subject to being rebuilt.
Accordingly, these timeline details are subject to change.

#### 2006

-   March 26 - ` lang: ` . An example of Tweet metadata being backfilled
    while generating the Search index.
-   July 13 - ` has:mentions ` begins matching.
-   October 6 - ` has:symbols ` . \$cashtags (or symbols) for discussing
    stock symbols does not become common until early 2009. Until then
    most usages were probably slang (e.g., \$slang).
-   October 26 - ` has:links ` begins matching.
-   November 23 - ` has:hashtags ` begins matching.

#### 2007

-   January 30 - First first-class \@reply (in_reply_to_user_id),
    ` reply_to_status_id: ` begins matching.
-   August 23 - Hashtags emerge as a common convention for organizing
    topics and conversations. First real use a week later.

#### 2009

-   May 15 - ` is:retweet ` . Note that this Operator starts matching
    with the 'beta' release of official Retweets and its "Via @'
    pattern. During this beta period, the Tweet verb is 'post' and the
    original Tweet is not included in the payload.
-   August 13 - Final version of official Retweets is released with "RT
    @" pattern, a verb set to 'share', and the 'retweet_status'
    attribute containing the original Tweet (thus approximately doubling
    the JSON payload size).

#### 2010

-   March 6 - ` has:geo ` , ` bounding_box: ` and ` point_radius: ` geo
    Operators begin matching.
-   August 28 - ` has:videos ` (Until February 2015, this Operator
    matches on Tweets with links to select video hosting sites such as
    youtube.com, vimeo.com, and vivo.com).

#### 2011

-   July 20 - ` has:media ` and ` has:images ` begin matching. Native
    photos officially announced August 9, 2010.

#### 2014

-   December 3 - (Approximately) *Some* [Enhanced URL
    metadata](/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls)
    with HTML title and description begins in payloads. Enhanced
    metadata more fully emerged in May 2016.

#### 2015

-   February 10 - ` has:videos ` matches on 'native' Twitter videos.
-   February 17 - ` has:profile_geo ` , ` profile_country: ` ,
    ` profile_region: ` , ` profile_locality: ` [Profile
    Geo](/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/profile-geo)
    Operators begin matching.
-   February 17 - ` place_country: ` and ` place: ` Tweet geo Operators
    begin matching.

#### 2016

#### 2017

-   February 22 - Poll metadata become available in enriched native
    format. No associated Operators for these metadata.

#### 2022

-   September 27 - All Tweet objects created since this date have Edited
    Tweet metadata available. All Enterprise endpoints that provide
    Tweet objects were updated to provide this metadata starting on this
    date. The edit metadata provided includes [ edit_history
    ]{.code-inline} and [ edit_controls ]{.code-inline} objects. These
    metadata will not be returned for Tweets that were created before
    September 27, 2022. Currently, there are no Enterprise Operators
    available that match these metadata.  To learn more about Edit Tweet
    metadata, check out the [Edit Tweets
    fundamentals](/content/developer-twitter/en/docs/twitter-api/enterprise/edit-tweets)
    page.

### 

#### 2022

-   September 29 - All Tweet objects created since this date have Edited
    Tweet metadata available. All Enterprise endpoints that provide
    Tweet objects were updated to provide this metadata starting on this
    date. The edit metadata provided includes [ edit_history
    ]{.code-inline} and [ edit_controls ]{.code-inline} objects. These
    metadata will not be returned for Tweets that were created before
    September 27, 2022. Currently, there are no Enterprise Operators
    available matching these metadata.  To learn more about Edit Tweet
    metadata, check out the [Edit Tweets
    fundamentals](/content/developer-twitter/en/docs/twitter-api/enterprise/edit-tweets)
    page.

### 

### Filtering tips

Given all the above timeline information, it is clear that there are a
lot of details to consider when writing Search APIs filters. There are
two key things to consider:

-   Some metadata have 'born-on' dates so filters can result in *false
    negatives* . Such searches include Operators reliant on metadata
    that did not exist for all of part of the search period. For
    example, if you are searching for Tweets with the ` has:images `
    Operator, you will not have any matches for periods before
    July 2011. That is because that Operator matches on *native* photos
    (attached to a Tweet using the Twitter user-interface). For a more
    complete data set of photo-sharing Tweets, filters for before July
    2011 would need to contain rule clauses that match on common URLs
    for photo hosting.
-   Some metadata has been backfilled with metadata from a time *after*
    the Tweet was posted.

There are several attribute types that are commonly focused on when
creating PowerTrack queries:

-   Twitter Profiles
-   Original or shared Tweets
-   Tweet language classification
-   Geo-referencing Tweets
-   Shared links media

Some of these have product-specific behavior while others have identical
behavior. See below for more details.

#### Twitter Profiles

The Search APIs serves historical Tweets with the user profile data set
as it is at the *time of retrieval* . If you request a Tweet from 2014,
the user's profile metadata will reflect how it exists at query-time.

#### Original Tweets and Retweets

The PowerTrack ` `*`is:retweet`*` ` Operator enables users to either
include or exclude Retweets. Users of this Operator need to have two
strategies for Retweet matching (or not matching) for data before August
2009. Before August 2009, the Tweet message itself needs to be checked,
using exact phrase matching, for matches on the "@RT " pattern
(Actually, if you are filtering on Retweets from between May-August
2009, the "Via @" pattern should be included). For periods after August
2009, the *is:retweet* Operator is available.

#### Tweet language classifications

For filtering on a Tweet's language classification, Twitter's historical
products are quite different. When the Search archive was built, all
Tweets were backfilled with the Twitter language classification.
Therefore the lang: Operator is available for the entire Tweet archive.

#### Geo-referencing Tweets

There are three primary ways to geo-reference Tweets:

-   **Geographical references in Tweet message.** Matching on geographic
    references in the Tweet message, while often the most challenging
    method since it depends on local knowledge, is an option for the
    entire Tweet archive. [Here](https://twitter.com/biz/statuses/28311)
    is an example geo-referenced match from 2006 for the San Francisco
    area based on a 'golden gate' filter.

-   **Tweets geo-tagged by the user.** With the search APIs the ability
    to start matching on Tweets with some Geo Operators started in March
    2010, and with others in February 2015:

    -   March 6, 2010: ` has:geo ` , ` bounding_box: ` and
        ` point_radius: `
    -   February 17, 2015: ` place_country: ` and ` place: `

-   **Account profile 'home' location set by the user.** Profile Geo
    Operators are available in both Historical PowerTrack and the Search
    APIs. With the Search APIs, these Profile Geo metadata is available
    starting in February 2015. For Tweets posted before Profile Geo
    metadata became available, the ` bio_location: ` Operator is
    available which can be used to match on non-normalized user input.

#### Shared links and media

In March 2012, the expanded URL enrichment was introduced. Before this
time, the Tweet payloads included only the URL as provided by the user.
So, if the user included a shortened URL it can be challenging to match
on (expanded) URLs of interest. With the Search APIs, these metadata are
available starting in March 2012.

In July 2016, the enhanced URL enrichment was introduced. This enhanced
version provides a web site's HTML title and description in the Tweet
payload, along with Operators for matching on those. These metadata
begin emerging in December 2014.

In September 2016 Twitter introduced 'native attachments' where a
trailing shared link is not counted against the 140 Tweet character
limit. Both URL enrichments still apply to these shared links.

Here are when related Search Operators begin matching:

-   2006 October 26 - ` has:links `
-   2011 July 20 - ` has:images ` and ` has:media `
-   2011 August - ` url: ` with the [Expanded URLs
    enrichment](/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls)
    As early as September 2006
    ` (url:"spotify.com" OR url:gnip OR url:microsoft OR url:google OR url:youtube) `
    matches http://twitter.com/Adam/statuses/16602, even though there is
    no urls\[\] metadata in twitter_entities and gnip objects.
    "youtube.com" is an example of message content that, without any
    urls\[\] metadata, matches url:youtube.
-   2015 February 10 - ` has:videos ` for native videos. Between
    2010/08/28 and 2015/02/10, this Operator matches on Tweets with
    links to select video hosting sites such as youtube.com, vimeo.com,
    and vivo.com.
-   2016 May 1 - ` url_title: ` and ` url_description: ` , based on the
    [Enhanced URLs
    enrichment](/content/developer-twitter/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls)
    , generally available. First Enhanced URL metadata began appearing
    in December 2014.

### Next steps
:::
