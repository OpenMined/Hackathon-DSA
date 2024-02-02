<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Features are authorization mechanisms that allow apps to access specific
types of data through our various APIs. In this way they are similar to
Permissions, however Features cannot be granted to an app by an app
user. Instead, Features are active or inactive depending on the app
user\'s relationship to the app and the app\'s mode when it is being
used.

For apps in Development Mode, all Features except for Page Public
Content Access and Page Public Metadata Access are active for any app
user who has a Role on the app or a Role in a Business that has claimed
the app.

For apps in Live Mode, only Features approved through App Review are
active for app users. This also applies to app users who have a Role on
the app or Business.

For Business app types (which have access levels instead of modes),
Features are active for any app users who have a Role on the app or in a
Business that has claimed the app, unless access has been removed. In
order for a Feature to be active for app users without a Role on the app
or Business, it must first be approved through App Review.

Access to any Feature that is granted by default or through App Review
can be used to request analytics insights to improve your app and for
marketing or advertising purposes, through the use of aggregated and
de-identified or anonymized information (provided such data cannot be
re-identified).

Unlike Permissions, Features do not expire, their approval will not be
revoked, if they are unused.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
::: _57-c
Feature
:::
:::
:::

</div>

</div>

Description

[Ad Targeting Data
Access](https://developers.facebook.com/docs/features-reference/ad-targeting-data-access)

The **Ad Targeting Data Access** feature allows access to ad targeting
data within the Facebook Open Research and Transparency tool for
election, political, and social issue ads that are run on Facebook from
Meta and Instagram from Meta.

**Allowed Usage**

-   To conduct research about Meta\'s role in society

[Business Asset User Profile
Access](https://developers.facebook.com/docs/features-reference/business-asset-user-profile-access)

The **Business Asset User Profile Access** feature allows your app to
read the [User Fields](/docs/graph-api/reference/user#fields) for users
engaging with your business assets such as id, ids_for_business, name,
and picture.

**Allowed Usage**

You can use this feature if your app uses one or more of the User Fields
in its business app experience.

[Ads Management Standard
Access](https://developers.facebook.com/docs/features-reference/ads-management-standard-access)

The **Ads Management Standard Access** feature allows your app to access
the Marketing API.

**Allowed Usage**

-   Enable an unlimited number of ad accounts and lower rate limiting.

-   To read ads reports for ad accounts you own or have been granted
    access to by the ad account owner, request **Ads Management Standard
    Access** , along with the **ads_read** permission.

-   To read and manage ads for ad accounts you own or have been granted
    access to by the ad account owner, request **Ads Management Standard
    Access** , along with the **ads_management** permission.

-   To pull ads reports from a set of clients, and to read and manage
    ads from another set of clients, request **Ads Management Standard
    Access** , along with both **ads_read** and **ads_management**
    permissions.

[Business Asset User Profile
Access](https://developers.facebook.com/docs/features-reference/business-asset-user-profile-access)

The **Business Asset User Profile Access** feature allows your app to
read the [User Fields](/docs/graph-api/reference/user#fields) for users
engaging with your business assets such as id, ids_for_business, name,
and picture.

**Allowed Usage**

You can use this feature if your app uses one or more of the User Fields
in its business app experience.

[Groups
API](https://developers.facebook.com/docs/features-reference/groups-api)

The **Groups API** feature allows your app to access content in a
Facebook Group.

**Allowed Usage**

-   Help people manage the posts and content published to their Group.

-   Help people get information about content posted to their Group.

-   Let people publish content from your app to their Facebook Group.

-   Help people get aggregated insights about activity happening in
    their Group.

[Human
Agent](https://developers.facebook.com/docs/features-reference/human-agent)

The **Human Agent** feature allows your app to have a human agent
respond to user messages using the **human_agent** tag within 7 days of
a user\'s message.

**Allowed Usage**

-   Provide human agent support in cases where a user's issue cannot be
    resolved in the standard messaging window.

[Instagram Public Content
Access](https://developers.facebook.com/docs/features-reference/instagram-public-content-access)

The **Instagram Public Content Access** feature allows your app to
access Instagram Graph API\'s Hashtag Search endpoints.

**Allowed Usage**

-   Discover content associated with its current campaign.

-   Provide customer support.

-   Identify entrants to its contests, competitions, or sweepstakes.

-   Understand public sentiment around brand.

-   Understand and manage their audience, develop their content strategy
    and obtain digital rights.

[Live Video
API](https://developers.facebook.com/docs/features-reference/live-video-api)

The **Live Video API** feature allows an app to manage live videos to
Pages, Groups and User timelines when combined with the correct matching
permission.

**Allowed Usage**

-   App users can publish live video content from your app to Facebook.

[oEmbed Read](/docs/features-reference/oembed_read)

The **oEmbed Read** feature allows your app to get embed HTML and basic
metadata for public Facebook and Instagram pages, posts, and videos.

**Allowed Usage**

-   Provide front-end views of Facebook and Instagram pages, posts, and
    videos.

[Page
Mentioning](https://developers.facebook.com/docs/features-reference/page-mentioning)

The **Page Mentioning** feature allows your app mention any Facebook
Page when publishing posts on the Pages managed by your app.

**Allowed Usage**

-   Allow people to use your app to publish Page posts that mention
    other Pages.

-   Mention Pages relevant to the content in your page post.

[Page Public Content
Access](https://developers.facebook.com/docs/features-reference/page-public-content-access)

The **Page Public Content Access** feature allows your app access to the
Pages Search API and to read public data for Pages for which you lack
the [pages_read_engagement
permission](/docs/permissions/reference/pages_read_engagement) and the
[pages_read_user_content
permission](/docs/permissions/reference/pages_read_user_content) .
Readable data includes business metadata, public comments and posts.

**Allowed Usage**

-   Analyze and/or display posts and engagement on Pages.

[Page Public Metadata
Access](https://developers.facebook.com/docs/features-reference/page-public-metadata-access)

The **Page Public Metadata Access** feature allows your app access to
the Pages Search API and to read public data for Pages for which you
lack the [public Page
fields](/docs/graph-api/reference/page#public-page-data) and the [Pages
Search API](/docs/pages/searching) .

**Allowed Usage**

-   Analyze engagement with public Pages by viewing Like and follower
    counts.

-   Aggregate public-facing \"about\" Page information from multiple,
    disparate pages.

[Threat
Exchange](https://developers.facebook.com/docs/features-reference/threat-exchange)

The **ThreatExchange** feature allows your app to share threat data
among a select group of vetted industry partners.

**Allowed Usage**

-   Share threat data with a specific group of partners to achieve their
    security goals.
