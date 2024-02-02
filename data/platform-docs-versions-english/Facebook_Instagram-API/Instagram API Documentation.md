Instagram Graph API
===================

The Instagram Graph API allows [Instagram Professionals](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F502981923235522&h=AT3haoot-kjaIWyBVRisL4Gb9JImxBM2_2BQGGcilktW5zx8EBoMQ-ynypQ0QyjB2m88Fj5SrPSvw05ldCkEVAlAj-27JI4Q9DAhQq3WdyHum1BadgleYzCS2JTVy6dJTq_RfQhHsOYb6_7v6Kye4A) — Businesses and Creators — to use your app to manage their presence on Instagram. The API can be used to get and publish their media, manage and reply to comments on their media, identify media where they have been @mentioned by other Instagram users, find hashtagged media, and get basic metadata and metrics about other Instagram Businesses and Creators.

The API is intended for Instagram Businesses and Creators who need insight into, and full control over, all of their social media interactions. If you are building an app for consumers or you only need to get an app user's basic profile information, photos, and videos, consider the [Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api) instead.

The API is built on the Facebook Graph API. If you are unfamiliar with the Facebook Graph API, please read our [Facebook Graph API documentation](https://developers.facebook.com/docs/graph-api/) to learn how it works before proceeding.

Common Uses
-----------

* [Getting](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#get-media) and [managing](https://developers.facebook.com/docs/instagram-api/reference/ig-media) published photos, videos, and stories
* [Getting basic data about other Instagram Business and Creator accounts](https://developers.facebook.com/docs/instagram-api/guides/business-discovery)
* [Moderating comments and their replies](https://developers.facebook.com/docs/instagram-api/guides/comment-moderation)
* [Measuring media and profile interaction](https://developers.facebook.com/docs/instagram-api/guides/insights)
* [Discovering hashtagged media](https://developers.facebook.com/docs/instagram-api/guides/hashtag-search)
* [Discovering @mentions](https://developers.facebook.com/docs/instagram-api/guides/mentions)
* [Publishing photos and videos](https://developers.facebook.com/docs/instagram-api/guides/content-publishing)

[](#)

Limitations
-----------

* The API cannot access Instagram consumer accounts (i.e., non-Business or non-Creator Instagram accounts). If you are building an app for consumer users, use the [Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api) instead.
* [Content Publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) is available to all Instagram Professional accounts, except Stories, which are only available to business accounts.
* [Ordering results](https://developers.facebook.com/docs/graph-api/using-graph-api#ordering) is not supported
* All endpoints support cursor-based [pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#paging), but the [User Insights](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights) edge is the only endpoint that supports time-based pagination

[](#)

Documentation Contents
----------------------

|     |     |
| --- | --- |
| ### [Overview](https://developers.facebook.com/docs/instagram-api/overview)<br><br>Explanations of core concepts and usage requirements. | ### [Get Started](https://developers.facebook.com/docs/instagram-api/getting-started)<br><br>A short tutorial to get you up and running. |
| ### [Guides](https://developers.facebook.com/docs/instagram-api/guides)<br><br>Use case based guides to help you perform specific actions. | ### [Reference](https://developers.facebook.com/docs/instagram-api/reference)<br><br>Component and endpoint references. |

[](#)

See Also
--------

* [Facebook Graph API](https://developers.facebook.com/docs/graph-api/)
* [Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api)
* [Instagram Professional accounts](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F502981923235522&h=AT1cX6a7TfHHHnf-lpds4o4ULfwf8CADUu08ahq9_k_R3x8NzmITQ8MgE3tjpYbKTMdGPibSlG9bfBbkDcmMhDrwokDxas2exXIdcs0nZU7m2oDZwkL6v_pCwoyuefyI4qiFmvH2PLxvql4yJe5vcA)
* [Set Up a Professional Account on Instagram](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F502981923235522&h=AT2pFyBQV12duyYmqWYyqmhCybzl9HiN2Vgpsf_wbO8OLR5vpqqkzLrjvMUSjPsGAJzYG8WBnOSxYmVIkSVK8ZoSrhGUOqdJhsD6ie0MPifSox9tMCFNmgW0xegBOYid-uP46WNicCwOx3vGr2CDLQ)
* [Instagram Messaging with Messenger Platform](https://developers.facebook.com/docs/messenger-platform/instagram)

[](#)

[](#)

Overview
========

The Instagram Graph API is a collection of Facebook Graph API endpoints that allow apps to access data in [Instagram Professional accounts](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F502981923235522&h=AT2xnCTuoXq61yyY63zGMHDbJJ4Bu4lewH7FYJWLUubN-JVY6K-NhfkEXLOlwEJroL9pxwjXXatdXn8WvlDUTfkybKKeODaTXe7s2WyOvGrFSMZkBcjkKy5JZ12f8oiAgyNaoYwEnxCsw3HnuxWP5A) (both Business and Creator accounts). If you are unfamiliar with the Facebook Graph API, please read our [Graph API documentation](https://developers.facebook.com/docs/graph-api/) before proceeding.

Base URL
--------

All endpoints can be accessed via the `graph.facebook.com` host.

[](#)

App Users
---------

Instagram Professional accounts are accessed indirectly through Facebook accounts so your app users must have a Facebook account and use it when signing into your app. In addition, the Facebook account must be able to perform admin-equivalent [Tasks](#tasks) on a Facebook Page that has been [connected to the Instagram account](#pages) they are trying to access.

These requirements apply to all app users, even those who have a Role on your app or a Role on a Business that has claimed your app.

[](#)

Authentication
--------------

App user authentication is handled through access tokens. Instagram Professional accounts are accessed indirectly through Facebook accounts, so all API requests must include your app users's Facebook [User access token](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens). You can get tokens from app users by implementing [Facebook Login](https://developers.facebook.com/docs/facebook-login). Note that Facebook Login does not support Instagram credentials so app users must sign in using a Facebook account.

[](#)

Authorization
-------------

Endpoint authorization is handled through [permissions](https://developers.facebook.com/docs/permissions/reference) and [features](https://developers.facebook.com/docs/apps/features-reference). Before your app can use an endpoint to access an app user's Instagram data, you must first request all permissions required by those endpoints from the app user. The app user must then grant those permissions to your app. Once granted, you can query the endpoints to access the user's data.

Note that a permission only allows access to data created by the user who granted the permission. There are a few endpoints that allow apps to access data not created by the app user, but the accessible data is limited and public.

You can request permissions from app users by implementing [Facebook Login](https://developers.facebook.com/docs/facebook-login). App users who have a [role](https://developers.facebook.com/docs/development/build-and-test/app-roles) on your app can grant any requested permissions. App users who do not have a role on your app can only grant permissions and features that have been approved through the [App Review](#app-review) process.

The API uses the following permissions and features:

* [`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)
* [`instagram_content_publish`](https://developers.facebook.com/docs/permissions/reference/instagram_content_publish)
* [`instagram_manage_comments`](https://developers.facebook.com/docs/permissions/reference/instagram_manage_comments)
* [`instagram_manage_insights`](https://developers.facebook.com/docs/permissions/reference/instagram_manage_insights)
* [`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)
* [`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)
* [`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement)
* [Instagram Public Content Access](https://developers.facebook.com/docs/features-reference/instagram-public-content-access)

Refer to our [endpoint reference](https://developers.facebook.com/docs/instagram-api/reference) to determine which permission and features your app will need to request from app users.

### Instagram Messaging

If you plan to implement Instagram Messaging from Messenger Platform, you will need to include the `instagram_manage_messages` permission. [Learn more about Instagram Messaging. ![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/276034258_1045248339390233_3876773921429146148_n.png?_nc_cat=110&ccb=1-7&_nc_sid=e280be&_nc_ohc=kWYSfOaIwQkAX9VVnhY&_nc_ht=scontent-cdg4-1.xx&oh=00_AfAuH2lq4HPEeN7nvbLZ7LwMLkfrn8ZieGVSbVxs8Mnwwg&oe=65C38335)](https://developers.facebook.com/docs/messenger-platform/overview#permissions) 

[](#)

Collaborators
-------------

The [Instagram Collab](https://www.facebook.com/help/instagram/291200585956732) feature allows Instagram app users to co-author content (i.e. publish media) with other accounts (collaborators).

With a few exceptions, data on or about co-authored media can only be accessed through the API by the user who published the media; collaborators are unable to access this data via the API. The only exceptions are when searching for top performing media or recently published media that has been tagged with a specific hashtag. See [Hashtag Search](https://developers.facebook.com/docs/instagram-api/guides/hashtag-search).

[](#)

Pages
-----

[Instagram Professional accounts](#instagram-professional-accounts) must be connected to a [Facebook Page](https://www.facebook.com/business/pages) before their data can be accessed through the API. Once connected, any Facebook User who is able to perform [Tasks](#tasks) on that Page can grant your app an access token, which can then be used in API requests.

Our [Add or change the Facebook Page connected to your Instagram professional account](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F570895513091465&h=AT0H0SmsHn4Z6djWH6jYof87d_0-Rgx6JeNkKrw6dPFrMTVJuEAzXXprIPQ1Rlum09M8wHTviDIRTu0rSHqq-nWCAPjy_Ib5f24eodAmVcVgqubTGwpICWS9kN-H3KuGpGDHlGMVPkpHOH6Mjo6J5w) help article explains how to connect to a Facebook Page to an Instagram Professional account.

[](#)

Tasks
-----

In order for an app user to grant your app permissions, the app user must be able to perform [tasks](https://developers.facebook.com/docs/pages/access-tokens#page-tasks) on the Facebook Page connected to the Instagram account they are attempting to access. App users may grant your app permissions based on tasks they are able to perform as follows:

| Permission | `MANAGE` | `CREATE_CONTENT` | `MODERATE` | `ADVERTISE` | `ANALYZE` |
| --- | --- | --- | --- | --- | --- |
| instagram\_basic | ✔   | ✔   | ✔   | ✔   | ✔   |
| instagram\_content\_publish | ✔   | ✔   |     |     |     |
| instagram\_manage\_comments | ✔   | ✔   | ✔   |     |     |
| instagram\_manage\_insights | ✔   | ✔   | ✔   | ✔   | ✔   |

You can determine which tasks an app user is able to perform on a Page by querying the [`GET /me/accounts`](https://developers.facebook.com/docs/graph-api/reference/user/accounts#Reading) endpoint with the app user's User access token. The endpoint will return a list of Pages that the app user is able to perform tasks on, and indicate which tasks the user can perform on each of them.

Refer to the [reference documentation](https://developers.facebook.com/docs/instagram-api/reference/) to see which permissions each endpoint requires. The API does not support [Business Manager System Users](https://developers.facebook.com/docs/marketing-api/system-users), or app users who have the Live Contributor role.

### Referring to tasks

If you need to inform your app users about tasks (and which ones are required to use your app properly), here's how tasks are referred to in our various UIs.

#### Classic Pages

[Classic Pages](https://www.facebook.com/help/135275340210354) refer to tasks as **roles**. App users with an Admin role on a Page can grant your app any permission. App users with other roles can grant permissions as follows:

| Role | Grantable Permissions |
| --- | --- |
| Editor | instagram\_basic  <br>instagram\_content\_publish |
| Moderator | instagram\_basic  <br>instagram\_manage\_comments  <br>instagram\_manage\_insights |
| Advertiser | instagram\_basic  <br>instagram\_manage\_insights |
| Analyst | instagram\_basic  <br>instagram\_manage\_insights |

#### New Experience Pages

[New Experience Pages](https://www.facebook.com/business/help/782660422528806) refer to tasks as either Facebook Access or Task Access. App users with Facebook Access on a Page can grant your app any permission. App users with Task Access can grant permissions as follows:

| Task Access | Grantable Permissions |
| --- | --- |
| Ads | instagram\_basic |
| Content | instagram\_basic  <br>instagram\_content\_publish |
| Insights | instagram\_basic  <br>instagram\_manage\_insights |
| Messages & Community Activity | instagram\_basic  <br>instagram\_manage\_comments |

To determine if a Page is using the new experience, request its [`has_transitioned_to_new_page_experience`](https://developers.facebook.com/docs/graph-api/reference/page/#Reading) field. This value return `true` if the Page uses the new experience.

[](#)

App Review
----------

Your app must complete [App Review](https://developers.facebook.com/docs/app-review) before it can be used by [app users](#app-users) who do not have a [Role](https://developers.facebook.com/docs/apps#roles) on your app or a [Role](https://www.facebook.com/business/help/623924618023072?id=2190812977867143) on a Business that has claimed your app. If your app will only be used by app users who have a Role on your app or Business, you do not need to complete App Review.

Your App Review submission does not need to include any [Facebook test user](https://developers.facebook.com/docs/apps/test-users) credentials if you have implemented [Facebook Login](https://developers.facebook.com/docs/facebook-login) and your app is publicly available. However, if our reviewers need to sign into a non-Facebook account in order to trigger your implementation of Facebook Login, you must include the non-Facebook account credentials in your submission.

### Private Apps

If our reviewers are unable to test your app because it is behind a private intranet, has no user interface, or has not implemented Facebook Login, you may only request approval for these Permissions:

* [instagram\_basic](https://developers.facebook.com/docs/permissions/reference/instagram_basic)
* [instagram\_manage\_comments](https://developers.facebook.com/docs/permissions/reference/instagram_manage_comments)

[](#)

Business Verification
---------------------

You must complete [Business Verification](https://developers.facebook.com/docs/apps#business-verification) if your app will be used by app users who do not have a Role on the app itself, or a Role in a Business that has claimed the app.

[](#)

Rate Limiting
-------------

All endpoints are subject to [Instagram Business Use Case rate limiting](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#instagram-graph-api) except for [Business Discovery](https://developers.facebook.com/docs/instagram-api/guides/business-discovery) and [Hashtag Search](https://developers.facebook.com/docs/instagram-api/guides/hashtag-search) endpoints, which are subject to [Platform Rate limiting](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#platform-rate-limits).

[](#)

Webhooks
--------

You can use Webhooks to have notifications sent to you whenever someone comments on your app users' media objects or when any of their stories expire. Refer to our [Webhooks documentation](https://developers.facebook.com/docs/graph-api/webhooks) to learn how to use Webhooks, then set up a webhook for the `Instagram` topic and subscribe to its `comments` and `story_insights` fields.

[](#)

Instagram Messaging
-------------------

Several Instagram Graph API endpoints are used in conjunction with the Messenger Platform endpoints to allow your app users to interact with direct messages sent to their Instagram Professional accounts. Refer to the Messenger Platform's [Instagram Messaging](https://developers.facebook.com/docs/messenger-platform/instagram) documentation to learn how to access messages in Instagram Business accounts.

[](#)

[](#)

Getting Started
===============

This document explains how to successfully call the Instagram Graph API with your app and get an Instagram Business or Creator Account's media objects. It assumes you are familiar with the [Graph API](https://developers.facebook.com/docs/graph-api) and [Facebook Login](https://developers.facebook.com/docs/facebook-login), and know how to perform REST API calls. If you do not have an app yet, you can use the [Graph API Explorer](https://developers.facebook.com/tools/explorer) instead and skip steps 1 and 2.

Before You Start
----------------

You will need access to the following:

* An [Instagram Business Account](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F502981923235522&h=AT1bHFwoiRjgd-B4GuzIy3Jc6r2FOe8XhT4v_UwX97nlcnhcEkl7GwpxgSR9sX86uVd-AC4ccDhDnh8zMYl1y1EjKM7V8feUL3vV5-j_jEmNbFY7mLVvRD7efvcqNaoPNC-SHn94qz93RtmZXWns4Q) or [Instagram Creator Account](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1158274571010880&h=AT1TTSleH-jldObZFpSq9_9IkoHxzed2fCxwmTaQgoplXaYajROpCtFOnDMD2aEPRV4_gHWuOS4b4Sit1KSH-u3Wtn-p5LCKczfeJV01xRzYvuk9msBXpSiwt2nOu73IBhlhrysIAnhOwtbUE4sH-g)
* A [Facebook Page connected to that account](https://developers.facebook.com/docs/instagram-api/overview#pages)
* A Facebook Developer account that can perform [Tasks on that Page](https://developers.facebook.com/docs/instagram-api/overview#tasks)
* A [registered Facebook App](https://developers.facebook.com/docs/development/register) with **Basic** settings configured

[](#)

1\. Configure Facebook Login
----------------------------

Add the Facebook Login product to your app in the App Dashboard.

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/57313411_166141971002334_3488307145718366208_n.png?_nc_cat=104&ccb=1-7&_nc_sid=e280be&_nc_ohc=DB8k-vZ1fLIAX9LpSV-&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDLugCP47nvXMHgC3ZODO_8WVvnDyeHrrwAAbqHarcwQQ&oe=65C37A46)

You can leave all settings on their defaults. If you are implementing Facebook Login manually (which we don't recommend), enter your `redirect_uri` in the **Valid OAuth redirect URIs** field. If you will be using one of our SDKs, you can leave it blank.

[](#)

2\. Implement Facebook Login
----------------------------

Follow our [Facebook Login documentation](https://developers.facebook.com/docs/facebook-login) for your platform and implement Facebook Login into your app. Set up your implementation to request these permissions:

* [`instagram_basic`](https://developers.facebook.com/docs/apps/review/login-permissions#instagram-basic)
* [`pages_show_list`](https://developers.facebook.com/docs/apps/review/login-permissions#pages-show-list)

[](#)

3\. Get a User Access Token
---------------------------

Once you've implemented Facebook Login, make sure you are signed into your Facebook Developer account, then access your app and trigger the Facebook Login modal. Remember, your Facebook Developer account must be able to perform [Tasks](https://developers.facebook.com/docs/instagram-api/overview#tasks) on the [Facebook Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the Instagram account you want to query.

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/57343078_287134128874563_1329098073791528960_n.png?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=iHlpwe4qpv4AX-l-K1O&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDdRNYQqpedpvNfShkUT2vHJkS01rot3Xe1YUsW1qRPwQ&oe=65C37239)

Once you have triggered the modal, click **OK** to grant your app the `instagram_basic` and `pages_show_list` permissions.

The API should return a User access token. Capture the token so your app can use it in the next few queries. If you are using the Graph API Explorer, it will be captured automatically and displayed in the **Access Token** field for reference:

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/57308062_276123556625959_4652658984229011456_n.png?_nc_cat=110&ccb=1-7&_nc_sid=e280be&_nc_ohc=AIjxhhFz5jgAX_6luoJ&_nc_ht=scontent-cdg4-1.xx&oh=00_AfBB5p3Xn6LfJQsEUoA_idlUQuFQoTnuUi5oKUbWiOchjQ&oe=65C3851F)

[](#)

4\. Get the User's Pages
------------------------

Query the `GET /me/accounts` endpoint (this translates to `GET /{user-id}/accounts`, which perform a `GET` on the Facebook [User](https://developers.facebook.com/docs/graph-api/reference/user) node, based on your access token).

curl \-i \-X GET \\
 "https://graph.facebook.com/`v18.0`/me/accounts?access\_token={access-token}"

This should return a collection of Facebook Pages that the current Facebook User can perform the `MANAGE`, `CREATE_CONTENT`, `MODERATE`, or `ADVERTISE` tasks on:

{
  "data": \[
    {
      "access\_token": "EAAJjmJ...",
      "category": "App Page",
      "category\_list": \[
        {
          "id": "2301",
          "name": "App Page"
        }
      \],
      "name": "Metricsaurus",
      "id": "134895793791914",  // capture the Page ID
      "tasks": \[
        "ANALYZE",
        "ADVERTISE",
        "MODERATE",
        "CREATE\_CONTENT",
        "MANAGE"
      \]
    }
  \]
}

Capture the ID of the Facebook Page that's connected to the Instagram account that you want to query. Keep in mind that your app users may be able to perform tasks on multiple pages, so you eventually will have to introduce logic that can determine the correct Page ID to capture (or devise a UI where your app users can identify the correct Page for you).

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/57437240_2085096038272793_3947769475595501568_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=FVVIXaHgG6IAX_09EcU&_nc_ht=scontent-cdg4-3.xx&oh=00_AfBNAiL95Vw5cWF4yCfZN4AZsx8VUBKk281vg_EgXHSO3w&oe=65C37446)

[](#)

5\. Get the Page's Instagram Business Account
---------------------------------------------

Use the Page ID you captured to query the `GET /{page-id}?fields=instagram_business_account` endpoint:

curl \-i \-X GET \\
 "https://graph.facebook.com/`v18.0`/134895793791914?fields=instagram\_business\_account&access\_token={access-token}"

This should return the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) — an Instagram Business or Creator Account — that's connected to the Facebook Page.

{
  "instagram\_business\_account": {
    "id": "17841405822304914"  // Connected IG User ID
  },
  "id": "134895793791914"  // Facebook Page ID
}

Capture the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) ID.

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/57462471_316665542380805_102061440998834176_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=v4o-WnHYZ_4AX9n6Jyp&_nc_ht=scontent-cdg4-2.xx&oh=00_AfAYR4C1rUtX9kyKEX5f5V89DruUv2Xr2U_b6b0AA9ifqw&oe=65C391B9)

[](#)

6\. Get the Instagram Business Account's Media Objects
------------------------------------------------------

Use the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) ID you captured to query the `GET /{ig-user-id}/media` endpoint:

curl \-i \-X GET \\
 "https://graph.facebook.com/`v18.0`/17841405822304914/media?access\_token={access-token}"

This should return the IDs of all the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user):

{
  "data": \[
    {
      "id": "17918195224117851"
    },
    {
      "id": "17895695668004550"
    },
    {
      "id": "17899305451014820"
    },
    {
      "id": "17896450804038745"
    },
    {
      "id": "17881042411086627"
    },
    {
      "id": "17869102915168123"
    }
  \],
  "paging": {
    "cursors": {
      "before": "QVFIUkdGRXA2eHNNTUs4T1ZAXNGFxQTAtd3U4QjBLd1B2NXRMM1NkcnhqRFdBcEUzSDVJZATFoLWtXMWZAGU2VrRTk2RHVtTVlDckI2NjN0UERFa2JrUk4yMW13",
      "after": "QVFIUmlwbnFsM3N2cV9lZAFdCa0hDeV9qMVliT0VuMmJyNENxZA180c0t6VjFQVEJaTE9XV085aU92OUFLNFB6Szd2amo5aV9rTlVBcnNlWmEtMzYxcE1HSFR3"
    }
  }
}

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/57261700_588761411631102_2933352179429277696_n.png?_nc_cat=110&ccb=1-7&_nc_sid=e280be&_nc_ohc=7Sjvw7K_RT8AX9AApwH&_nc_ht=scontent-cdg4-1.xx&oh=00_AfBNlOcbGCvU4oMgg5Xfq1ozHjhijgCrXIQ_MOcrS5n95Q&oe=65C389BD)

If you are able to perform this final query successfully, you should be able to perform queries using any of the Instagram Graph API endpoints — just refer to our various guides and references to learn what each endpoint can do and what permissions they require.

[](#)

Next Steps
----------

* Develop your app further so it can successfully use any other endpoints it needs, and keep track of the permissions each endpoint requires
    * If you plan to implement [Instagram Messaging from Messenger Platform](https://developers.facebook.com/docs/messenger-platform//instagram) you will need additional permissions
* Complete the [App Review](https://developers.facebook.com/docs/instagram-api/overview#app-review) process and request approval for all of the permissions your app will need so your app users can grant them while your app is in [Live Mode](https://developers.facebook.com/docs/development/build-and-test/app-modes#live-mode)
* Switch your app to Live Mode and market it to potential users

Once your app is in Live Mode, any Facebook User who you've made your app available to can access an Instagram Business or Creator Account's data, as long as they have a Facebook User account that can perform Tasks on the Page connected to that Instagram Business or Creator Account.

[](#)

[](#)

Guides
======

Business Discovery
------------------

The [Business Discovery](https://developers.facebook.com/docs/instagram-api/guides/business-discovery) guide explains how to get basic metadata and metrics about other Instagram Business [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

[](#)

Comment Moderation
------------------

The [Comment Moderation](https://developers.facebook.com/docs/instagram-api/guides/comment-moderation) guide explains how to reply to comments, delete comments, hide/unhide comments, and disable/enable comments on [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects owned by [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

[](#)

Content Publishing
------------------

The [Content Publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) guide explains how to publish [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on Instagram Business [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

[](#)

Hashtag Search
--------------

The [Hashtag Search](https://developers.facebook.com/docs/instagram-api/guides/hashtag-search) guide explains how to find public photos and videos that have been tagged with specific hashtags.

[](#)

Insights
--------

The [Insights](https://developers.facebook.com/docs/instagram-api/guides/insights) guide explains how to get social interaction metrics for [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user) and their [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects.

[](#)

Mentions
--------

The [Mentions](https://developers.facebook.com/docs/instagram-api/guides/mentions) guide explains how to identify [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) and [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been tagged or @mentioned.

[](#)

Webhooks
--------

The [Webhooks](https://developers.facebook.com/docs/instagram-api/guides/webhooks) guide explains how to get real-time notifications whenever Instagram users comment on any of an [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects, @mention an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) on other Instagram users' [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects, or when an [IG User's](https://developers.facebook.com/docs/instagram-api/reference/ig-user) stories expire.

[](#)

[](#)

Business Discovery
==================

You can use the Instagram Graph API to get basic metadata and metrics about other Instagram Business and Creator Accounts.

Limitations
-----------

Data about age-gated Instagram Business Accounts will not be returned.

[](#)

Endpoints
---------

The API consists of the following endpoints. Refer to the endpoint's reference documentation for parameter and permission requirements.

* [`GET /{ig-user-id}/business_discovery`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/business_discovery)

[](#)

Examples
--------

### Getting an Account's Follower & Media Count

This sample query shows how to get the number of followers and number of published media objects on the [Blue Bottle Coffee](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fbluebottle%2F&h=AT2jbnIX5izMz6Ye8R5ytg6noryJYvWvV7-XQoxcgEfDHPbwFONod2hJNKUQPHwlhr5KDjLM-zMro_bPxC_RB_D-8piBYkwm30isnP2S8ZSEqo6qj8hpbuwXlTC2pWtaP3v4K8Mc0SaMl1v_3ct6Dw) Instagram Business Account. Notice that business discovery queries are performed on the Instagram Business or Creator Account's ID (in this case, `17841405309211844`), not the username of the Instagram Business or Creator Account that you are attempting to get data about (`bluebottle` in this example).

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/v3.2/17841405309211844?fields=business\_discovery.username(bluebottle){followers\_count,media\_count}&access\_token={access-token}"

#### Sample Response

{
  "business\_discovery": {
    "followers\_count": 267793,
    "media\_count": 1205,
    "id": "17841401441775531" // Blue Bottle's Instagram Account ID
  },
  "id": "17841405309211844"  // ID of the Instagram account performing the query
}

### Getting Media

Since you can make nested requests by specifying an edge via the `fields` parameter, you can request the targeted Business or Creator Account's `media` edge to get all of its published media objects:

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/v3.2/17841405309211844?fields=business\_discovery.username(bluebottle){followers\_count,media\_count,media}&access\_token={access-token}"

#### Sample Response

{
  "business\_discovery": {
    "followers\_count": 267793,
    "media\_count": 1205,
    "media": {
      "data": \[
        {
          "id": "17858843269216389"
        },
        {
          "id": "17894036119131554"
        },
        {
          "id": "17894449363137701"
        },
        {
          "id": "17844278716241265"
        },
        ... // results truncated for brevity
      \],
    "id": "17841401441775531"
  },
  },
  "id": "17841405309211844"
}

### Getting Basic Metrics on Media

You can use both nested requests and field expansion to get public fields for a Business or Creator Account's media objects. Note that this does not grant you permission to access media objects directly — performing a `GET` on any returned [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) will fail due to insufficient permissions.

For example, here's how to get the number of comments and likes for each of the media objects published by Blue Bottle Coffee:

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/v3.2/17841405309211844?fields=business\_discovery.username(bluebottle){followers\_count,media\_count,media{comments\_count,like\_count}}&access\_token={access-token}"

#### Sample Response

{
  "business\_discovery": {
    "followers\_count": 267793,
    "media\_count": 1205,
    "media": {
      "data": \[
        {
          "comments\_count": 50,
          "like\_count": 5841,
          "id": "17858843269216389"
        },
        {
          "comments\_count": 11,
          "like\_count": 2998,
          "id": "17894036119131554"
        },
        {
          "comments\_count": 28,
          "like\_count": 3644,
          "id": "17894449363137701"
        },
        {
          "comments\_count": 43,
          "like\_count": 4943,
          "id": "17844278716241265"
        },
        {
          "comments\_count": 60,
          "like\_count": 9347,
          "id": "17899363132086521"
        },
        {
          "comments\_count": 63,
          "like\_count": 6913,
          "id": "17893114378137541"
        },
        {
          "comments\_count": 16,
          "like\_count": 2791,
          "id": "17886057709171561"
        },
        {
          "comments\_count": 15,
          "like\_count": 3895,
          "id": "17856337633208377"
        },
      \],
    },
    "id": "17841401441775531"
  },
  "id": "17841405976406927"
}

[](#)

[](#)

Content Publishing
==================

You can use the Instagram Graph API to publish single images, videos, reels (i.e., single media posts), or posts containing multiple images and videos (carousel posts) on Instagram Professional accounts.

Beginning July 1, 2023, all single feed videos published through the Instagram Content Publishing API will be shared as reels.

Requirements
------------

### Access Tokens

All requests must include the app user's [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access token.

### Permissions

Publishing relies on a combination of the following permissions. The exact combination depends on which [endpoints](#endpoints) your app uses. Refer to our [endpoint](#endpoints) references to determine which permissions each endpoint requires.

* [ads\_management](https://developers.facebook.com/docs/permissions/reference/ads_management)
* [business\_management](https://developers.facebook.com/docs/permissions/reference/business_management)
* [instagram\_basic](https://developers.facebook.com/docs/permissions/reference/instagram_basic)
* [instagram\_content\_publish](https://developers.facebook.com/docs/permissions/reference/instagram_content_publish)
* [pages\_read\_engagement](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement)

If your app will be used by app users who do not have a [role](https://developers.facebook.com/docs/development/build-and-test/app-roles) on your app or a role in a [Business](https://www.facebook.com/business/help/442345745885606?id=180505742745347) that has claimed your app, you must request approval for each permission via [App Review](https://developers.facebook.com/docs/app-review) before non-role app users can grant them to your app.

### Public Server

We cURL media used in publishing attempts so the media must be hosted on a publicly accessible server at the time of the attempt.

### Page Publishing Authorization

Instagram Professional accounts connected to a [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) that requires [Page Publishing Authorization](https://www.facebook.com/business/m/one-sheeters/page-publishing-authorization) (PPA) cannot be published to until PPA has been completed.

It's possible that an app user may be able to perform [Tasks](https://developers.facebook.com/docs/instagram-api/overview#tasks) on a Page that initially does not require PPA but later requires it. In this scenario, the app user would not be able to publish content to their Instagram Professional account until completing PPA. Since there's no way for you to determine if an app user's Page requires PPA, we recommend that you advise app users to preemptively complete PPA.

### Limitations

* JPEG is the only image format supported. Extended JPEG formats such as MPO and JPS are not supported.
* Shopping tags are not supported.
* Branded content tags are not supported.
* Filters are not supported.
* Publishing to Instagram TV is not supported.

For additional limitations, refer to each [endpoint's](#endpoints) reference.

### Rate Limit

Instagram accounts are limited to 50 API-published posts within a 24-hour moving period. Carousels count as a single post. This limit is enforced on the [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish) endpoint when attempting to publish a media container. We recommend that your app also enforce the publishing rate limit, especially if your app allows app users to schedule posts to be published in the future.

To check an Instagram Professional account's current rate limit usage, query the [`GET /{ig-user-id}/content_publishing_limit`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/content_publishing_limit) endpoint.

Endpoints
---------

The API consists of the following endpoints. Refer to each endpoint's reference document for usage requirements.

* [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) — upload media and create media containers.
* [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish#creating) — publish uploaded media using their media containers.
* [`GET /{ig-container-id}?fields=status_code`](https://developers.facebook.com/docs/instagram-api/reference/ig-container#reading) — check media container publishing eligibility and status.
* [`GET /{ig-user-id}/content_publishing_limit`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/content_publishing_limit) — check app user's current publishing rate limit usage.

[](#)

Single Media Posts
------------------

Publishing single image, video, story or reel is a two-step process:

1. Use the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint to create a container from an image or video hosted on your public server.
2. Use the [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish#creating) endpoint to publish the container.

Step 1 of 2: Create Container

Let's say you have an image at...

https://www.example.com/images/bronz-fonz.jpg

... that you want to publish with the hashtag "#BronzFonz" as its caption. Send a request to the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint:

#### Sample Request

POST https://graph.facebook.com/`v18.0`/17841400008460056/media
  ?image\_url\=https://www.example.com/images/bronz-fonz.jpg
  &caption\=#BronzFonz

This returns a container ID for the image.

#### Sample Response

{
  "id": "17889455560051444"  // IG Container ID
}

Step 2 of 2: Publish Container

Use the `POST /{ig-user-id}/media_publish` endpoint to publish the container ID returned in the previous step.

#### Sample Request

POST https://graph.facebook.com/`v18.0`/17841400008460056/media\_publish
  ?creation\_id=17889455560051444

#### Sample Response

{
  "id": "17920238422030506" // IG Media ID
}

[](#)

Carousel Posts
--------------

You may publish up to 10 images, videos, or a mix of the two in a single post (a carousel post). Publishing carousels is a three step process:

1. Use the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint to create individual item containers for each image and video that will appear in the carousel.
2. Use the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint again to create a single carousel container for the items.
3. Use the [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish#creating) endpoint to publish the carousel container.

Carousel posts count as a single post against the account's [rate limit](#rate-limit).

Limitations

* Carousels cannot be boosted.
* Carousels are limited to 10 images, videos, or a mix of the two.
* Carousel images are all cropped based on the first image in the carousel, with the default being a 1:1 aspect ratio.

Step 1 of 3: Create item container

Use the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint to create an item container for the image or video that will appear in a carousel. Carousels may have up to 10 total images, videos, or a mix of the two.

POST /{ig\-user\-id}/media

#### Parameters

The following parameters are **required**. Refer to the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint reference for additional supported parameters.

* `is_carousel_item` — Set to `true`. Indicates image or video will appear in a carousel.
* `image_url` — (images only) The path to the image. We will cURL your image using the passed in URL so it must be on a public server.
* `media_type` — (videos only) Set to `VIDEO`. Indicates media is a video.
* `video_url` — (videos only) Path to the video. We will cURL your video using the passed in URL so it must be on a public server.

If the operation is successful, the API will return an item container ID which can be used when creating the carousel container.

Repeat this process for each image or video that should appear in the carousel.

#### Sample Request

curl \-i \-X POST \\

"https://graph.facebook.com/`v18.0`/90010177253934/media?image\_url=https%3A%2F%2Fsol...&is\_carousel\_item=true&access\_token=EAAOc..."

#### Sample Response

{
  "id": "17899506308402767"
}

Step 2 of 3: Create carousel container

Use the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint to create a carousel container.

POST /{ig\-user\-id}/media

#### Parameters

The following parameters are **required**. Refer to the [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) endpoint reference for additional supported parameters.

* `media_type` — Set to `CAROUSEL`. Indicates container is for a carousel.
* `children` — An array of up to 10 container IDs of each image and video that should appear in the published carousel. Carousels can have up to 10 total images, videos, or a mix of the two.

#### Sample Request

curl \-i \-X POST \\

"https://graph.facebook.com/`v18.0`/90010177253934/media?caption=Fruit%20candies&media\_type=CAROUSEL&children=17899506308402767%2C18193870522147812%2C17853844403701904&access\_token=EAAOc..."

#### Sample Response

{
  "id": "18000748627392977"
}

Step 3 of 3: Publish carousel container

Use the [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish#creating) endpoint to publish a carousel container (a carousel post). Accounts are limited to 50 published posts within a 24-hour period. Publishing a carousel counts as a single post.

POST /{ig\-user\-id}/media\_publish

#### Parameters

The following parameters are required.

* `creation_id` — The carousel container ID.

If the operation is successful the API will return a carousel album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) ID.

#### Sample Request

curl \-i \-X POST \\

"https://graph.facebook.com/`v18.0`/90010177253934/media\_publish?creation\_id=18000748627392977&access\_token=EAAOc..."

#### Sample Response

{
  "id": "90010778390276"
}

[](#)

Reels Posts
-----------

Reels are short-form videos that are eligible to appear in the **Reels** tab of the Instagram app if they meet certain [specifications](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#reel-specifications) and are selected by our algorithm. To publish a reel, follow the steps for publishing a [single media post](#single-media-posts) and include the `media_type=REELS` parameter along with the path to the video using the `video_url` parameter.

Reels are not a new media type, even though you set `media_type=REELS` when you publish a reel. If you publish a reel and then request its `media_type` field, the value returned is `VIDEO`. To determine if a published video has been designated as a reel, request its `media_product_type` field instead.

You can use the [code sample on GitHub (insta\_reels\_publishing\_api\_sample)](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffbsamples%2Freels_publishing_apis%2Ftree%2Fmain%2Finsta_reels_publishing_api_sample&h=AT1iZheD6FZrTLkD8_OI8dviVeZAUQyFA1w8AcPp9M3yB8smwwgLCihBK-2-yDUwO5yCqs9e24n1C_xbI7prbdrVC7UdsCDxOcdzDOW14pMGjqjSA6j8QLHuzJe84nswRJ8CR4B9BF8IEs_b1wdqaQ) to learn how to publish Reels to Instagram.

To make it more convenient for developers, Meta has published the full set of Graph API calls for Instagram Reels on the Postman API Platform. For more information, see [Postman Collections for Facebook Reels and Instagram Reels](https://developers.facebook.com/docs/reels/postman).

For more information about Reels, see [Reels Developer Documentation](https://developers.facebook.com/docs/reels).

[](#)

Story Posts
-----------

Only business accounts can publish stories with the Content Publising API at this time.

Stories are videos and images that are posted as IG stories on Instagram. To publish a story, follow the same steps for publishing a single media post and include the `media_type=STORIES` parameter along with the path to the image/video using the `image_url` or `video_url` parameter.

**Note:** Stories are not a new media type even though you are setting `media_type=STORIES` when publishing a story. If you publish a story and then request its `media_type` field, the value will be returned as `IMAGE/VIDEO`. To determine if a published image/video has been designated as a story, request its `media_product_type` field instead.

[](#)

Collaborator Tags
-----------------

You can add public Instagram users in an image, carousel and reel as a collaborators and they will receive an invite to be a collaborator for that particular media. To tag users in an image, follow the Single Media Posts steps above, but when creating the media container, include the collaborators parameter and an array of strings indicating the Instagram usernames of users whom you want to invite as a collaborator on the media.

#### Sample Requeset

POST graph.facebook.com/17841400008460056/media
?image\_url\=https://www.example.com/images/bronzed-fonzes.jpg
&caption\=#BronzedFonzes!
&collaborators\= \[‘username1’,’username2’\]

#### Notes

* The collaborators value must be an array of strings.
* You can only tag users with public Instagram accounts.
* No more than 3 collaborators can be added to a media.
* Collaborators cannot be added to Story media.

[](#)

Location Tags
-------------

You can use the [Pages Search API ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22)](https://developers.facebook.com/docs/pages/searching) , be sure to include the \`location\` field in your query, to search for Pages whose names match a search string. Then, parse the results to identify any Pages that have been created for a physical location. If you include a Page's ID when publishing an image or video, it will be tagged with the location associated with that Page.

#### Limitations

To be eligible for tagging, a Page must have latitude and longitude location data.

Verify that the Page you want to use has latitude and longitude data in the response. Attempting to create a container using a Page that has no location data will fail with coded exception `INSTAGRAM_PLATFORM_API__INVALID_LOCATION_ID`.

Once you have the Page ID, assign it to the `location_id` parameter when publishing [single media](#single-media-posts) or [carousel](#carousel-posts) item containers.

[](#)

Product Tags
------------

You can publish both single media posts and carousel posts tagged with [Instagram Shopping](https://www.facebook.com/help/instagram/1187859655048322) products. Refer to the [Product Tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging) guide to learn how.

[](#)

User Tags
---------

You can tag public Instagram users in an image and they will receive a notification that they have been tagged.

To tag users in an image, follow the [Single Media Posts](#single-media-posts) steps above, but when creating the media container, include the `user_tags` parameter and an array of objects indicating the Instagram users in the image as well as their x/y coordinates within the image itself.

#### Sample Request

POST graph.facebook.com/17841400008460056/media
  ?image\_url=https://www.example.com/images/bronzed-fonzes.jpg
  &caption=#BronzedFonzes!
  &user\_tags=
   \[
     {
       username:'kevinhart4real',
       x: 0.5,
       y: 0.8
     },
     {
       username:'therock',
       x: 0.3,
       y: 0.2
     }
   \]

This returns a container ID which you then publish using the [IG User Media Publish](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish#creating) endpoint.

#### Notes

* The `user_tags` value must be an array of objects formatted with JSON.
* You can only tag users with public Instagram accounts.
* The object must contain all three properties (`username`, `x`, and `y`) for each user.
* `x` and `y` values must be `float` numbers that originate from the top-left of the image, with a range of `0.0`–`1.0`.
* User tags can be used with images in carousels.

[](#)

Troubleshooting
---------------

If you are able to create a container for a video but the [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish#creating) endpoint does not return the published media ID, you can get the container's publishing status by querying the `GET /{ig-container-id}?fields=status_code` endpoint. This endpoint will return one of the following:

* `EXPIRED` — The container was not published within 24 hours and has expired.
* `ERROR` — The container failed to complete the publishing process.
* `FINISHED` — The container and its media object are ready to be published.
* `IN_PROGRESS` — The container is still in the publishing process.
* `PUBLISHED` — The container's media object has been published.

We recommend querying a container's status once per minute, for no more than 5 minutes.

[](#)

Errors
------

See the [Error Codes](https://developers.facebook.com/docs/instagram-api/reference/error-codes) reference.

[](#)

[](#)

Comment Moderation
==================

You can use the Instagram Graph API to get comments, reply to comments, delete comments, hide/unhide comments, and disable/enable comments on IG Media owned by your app users.

You can use the [Instagram Messaging API](https://developers.facebook.com/docs/messenger-platform/instagram) to send private replies (direct messages) to users who have commented on your app users' live video IG Media. Refer to the Instagram Messaging's [private replies](https://developers.facebook.com/docs/messenger-platform/instagram/features/private-replies) documentation to learn how.

Endpoints
---------

The API consists of the following endpoints. Refer to each endpoint's reference documentation for parameter and permission requirements.

* [`GET /{ig-media-id}/comments`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/comments#reading) — Get comments on an IG Media.
* [`GET /{ig-comment-id}/replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-comment/replies#read) — Get replies on an IG Comment.
* [`POST /{ig-comment-id}/replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-comment/replies#create) — Reply to an IG Comment.
* [`POST /{ig-comment-id}`](https://developers.facebook.com/docs/instagram-api/reference/ig-comment#update) — Hide/unhide an IG Comment.
* [`POST /{ig-media-id}`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#update) — Disable/enable comments on an IG Media.
* [`DELETE /{ig-comment-id}`](https://developers.facebook.com/docs/instagram-api/reference/ig-comment#delete) — Delete an IG Comment.

[](#)

Examples
--------

### Getting & Replying to Comments

You can get all of the comments on a media object, analyze and filter the returned data set against specific criteria, then reply to any comments that match your criteria.

First, query the [`GET /{ig-media-id}/comments`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/comments#read) endpoint to get all of the comments and their IDs on the media object:

#### Sample Request

GET graph.facebook.com
  /17895695668004550/comments

#### Sample Response

{
  "data": \[
    {
      "timestamp": "2017-08-31T18:10:30+0000",
      "text": "I love this!",
      "id": "17873440459141021"
    },
    {
      "timestamp": "2017-08-31T19:16:02+0000",
      "text": "This is awesome!",
      "id": "17870913679156914"
    },
    ... // results truncated for brevity
  \]
}

Next, parse the returned results for comments that match whatever criteria you are using and use the matching comments to [reply in the comment thread to the Instagram users](https://developers.facebook.com/docs/instagram-api/reference/ig-comment/replies#replying) who made the comments:

#### Sample Request

POST graph.facebook.com
  /17870913679156914/replies?message\=Thanks%20for%20sharing!

#### Sample Response

{
  "id": "17873440459141029"
}

If you have a lot of comments that you want to reply to, you could [batch the replies into a single request](https://developers.facebook.com/docs/graph-api/making-multiple-requests/).

[](#)

[](#)

Copyright Detection
===================

This guide shows you how to detect copyright violations for a video uploaded or published to Instagram using the Instagram Graph API.

Before you start
----------------

Before you start you will need the following:

* All requirements and limitations for accessing the Instagram Container and Instagram Media endpoints apply

### Best practices

When testing an API call, you can include the `access_token` parameter set to your access token. However, when making secure calls from your app, use the [access token class.](https://developers.facebook.com/docs/facebook-login/guides/access-tokens#portabletokens)

Check an uploaded video
-----------------------

To check the copyright status for a video that have been uploaded, but not yet published, send a `GET` request to the `/{ig-containter-id}` endpoint with the `fields` parameter set to `copyright_check_status`.

### Sample Request

curl \-i \-X GET "https://graph.facebook.com/`v18.0`/{ig-containter-id}?fields=copyright\_check\_status"
    

On success, your app receives a JSON response with a `copyright_check_status` object with the following key-value pairs:

* `status` set to `completed`, `error`, `in_progress`, or `not_started`
* `matches_found` set to:
    * `false` if none are detected
    * `true` if violations are detected and `author`, `content_title`, `matched_segments`, and `owner_copyright_policy` values

### Sample Responses

|     |     |
| --- | --- |
| #### Violation found<br><br>{<br>  "copyright\_check\_status": {<br>    "status": "complete",<br>    "matches\_found": true<br>  },<br>  "id": "{ig-containter-id}"<br>} | #### No violation found<br><br>{<br>  "copyright\_check\_status": {<br>      "status": "in\_progress",<br>      "matches\_found": false<br>  }<br>} |

[](#)

Check a published video
-----------------------

To check the copyright status for a video that has been published, send a `GET` request to the `/{ig-media-id}` endpoint with the `fields` parameter set to `copyright_check_information`.

### Sample Request

curl \-i \-X GET "https://graph.facebook.com/`v18.0`/{ig-media-id}?fields=copyright\_check\_information"
    

On success, your app receives a JSON response with the `id` set to the video being checked and the `copyright_check_information` object with the following:

* `status` set to a `status` object set to `completed`, `error`, `in_progress`, or `not_started`
* `copyright_matches` set to:
    * `false` – Returned when no copyright violations are detected
    * `true` – Returned when copyright violations are detected and includes the `copyright_check_information` object that contains information about the copyright owner, policy, mitigation steps, and sections of the media that violated the copyright.

### Sample Responses

|     |     |
| --- | --- |
| #### Violation found<br><br>{<br>  "copyright\_check\_information": {<br>     "status": {<br>       "status": "complete",<br>       "matches\_found": true<br>     },<br>     "copyright\_matches": \[<br>       {<br>         "content\_title": "In My Feelings",<br>         "author": "Drake",<br>         "owner\_copyright\_policy": {<br>           "name": "UMG",<br>           "actions": \[<br>             {<br>               "action": "BLOCK",<br>               "territories": "3",<br>               "geos": \[<br>                 "Canada",<br>                 "India",<br>                 "United States of America"<br>               \]<br>             },<br>             {<br>               "action": "MUTE",<br>               "territories": "4",<br>               "geos": \[<br>                 "Taiwan",<br>                 "Tanzania",<br>                 "Saudi Arabia",<br>                 "United Kingdom of Great Britain and Northern Ireland"<br>               \]<br>             }<br>           \]<br>         },<br>         "matched\_segments": \[<br>          {<br>            "start\_time\_in\_seconds": 2.4,<br>            "duration\_in\_seconds": 5.1,<br>            "segment\_type": "AUDIO"<br>          },<br>          {<br>            "start\_time\_in\_seconds": 10.2,<br>            "duration\_in\_seconds": 4.5,<br>            "segment\_type": "VIDEO"<br>          }<br>        \]<br>      }<br>    \]<br>  },<br>  "id": "90012800291314"<br>} | #### No violation found<br><br>{<br>  "copyright\_check\_information": {<br>    "status": {<br>      "status": "complete",<br>      "matches\_found": false<br>    }<br>  },<br>  "id": "{ig-media-id}"<br>} |

[](#)

See also
--------

* [Instagram Container Reference ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22)](https://developers.facebook.com/docs/instagram-api/reference/ig-container) 
    
* [Instagram Media Reference ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22)](https://developers.facebook.com/docs/instagram-api/reference/ig-media) 
    

[](#) 

[](#)

Hashtag Search
==============

Find public IG Media that has been tagged with specific hashtags.

Limitations
-----------

* You can query a maximum of 30 unique hashtags on behalf of an Instagram Business or Creator Account within a rolling, 7 day period. Once you query a hashtag, it will [count against this limit](https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags) for 7 days. Subsequent queries on the same hashtag within this time frame will not count against your limit, and will not reset its initial query 7 day timer.
* Personally identifiable information will not be included in responses.
* You cannot comment on hashtagged media objects discovered through the API.
* Hashtags on Stories are not supported.
* Emojis in hashtag queries are not supported.
* The API will return a generic error for any requests that include hashtags that we have deemed sensitive or offensive.

[](#)

Requirements
------------

In order to use this API, you must undergo [App Review](https://developers.facebook.com/docs/apps/review) and request approval for:

* the [`Instagram Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-INSTAGRAM_PUBLIC_CONTENT_ACCESS) feature
* the [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic) permission

[](#)

Endpoints
---------

The Hashtag Search API consists of the following nodes and edges:

* [`GET /ig_hashtag_search`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag-search#reading) — to get a specific hashtag's node ID
* [`GET /{ig-hashtag-id}`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag#reading) — to get data about a hashtag
* [`GET /{ig-hashtag-id}/top_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/top-media#reading) — to get the most popular photos and videos that have a specific hashtag
* [`GET /{ig-hashtag-id}/recent_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/recent-media#reading) — to get the most recently published photos and videos that have a specific hashtag
* [`GET /{ig-user-id}/recently_searched_hashtags`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags) — to determine the unique hashtags an Instagram Business or Creator Account has searched for in the current week

Refer to each endpoint's reference documentation for supported fields, parameters, and usage requirements.

[](#)

Common Uses
-----------

### Getting Media Tagged With A Hashtag

To get all of the photos and videos that have a specific hashtag, first use the `/ig_hashtag_search` endpoint and include the hashtag and ID of the Instagram Business or Creator Account making the query. For example, if the query is being made on behalf of the Instagram Business Account with the ID `17841405309211844`, you could get the ID for the "#coke" hashtag by performing the following query:

GET graph.facebook.com/ig\_hashtag\_search
  ?user\_id\=17841405309211844
  &q\=coke

This will return the ID for the “#Coke” hashtag node:

{
  "id" : "17873440459141021"
}

Now that you have the hashtag ID (`17873440459141021`), you can query its `/top_media` or `/recent_media` edge and include the Business Account ID to get a collection of media objects that have the “#coke” hashtag. For example:

GET graph.facebook.com/17873440459141021/recent\_media
  ?user\_id\=17841405309211844

This would return a response that looks like this:

{
  "data": \[
    {
      "id": "17880997618081620"
    },
    {
      "id": "17871527143187462"
    },
    {       
      "id": "17896450804038745"     
    }
  \]
}

[](#)

[](#)

Insights
========

You can use the Instagram Graph API to get social interaction metrics for [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user) and their [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects. Amounts for each metric are calculated upon API request.

Due to privacy rules, messaging-related Story IG Media interactions performed by users in some regions will no longer be included in some metric calculations. These regions include: Europe starting December 1, 2020 and Japan starting April 14, 2021.

* For Stories created by users in affected regions, the [`replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights#metrics) metric will now return a value of `0`.
* For Stories created by users outside affected regions, the [`replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights#metrics) metric will return the number of replies, but replies made by users in affected regions will not be included in the calculation.

Limitations
-----------

* Some metrics are [not available](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights#limitations) on IG Users with fewer than 100 followers.
* The API only reports organic interaction metrics; interactions on ads containing a media object are not counted.
* Metrics data is stored for 2 years.
* You can only get insights for a single user at a time.
* You cannot get insights for Facebook Pages.
* Stories insights are only available for 24 hours, even if the stories are archived or highlighted. If you want to get the latest insights for a story before it expires, set up a [Webhook](https://developers.facebook.com/docs/instagram-api/guides/webhooks) for the [`Instagram`](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/) topic and subscribe to the [`story_insights`](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/#story_insights) field.
* Insights on album child IG Media is not supported.
* If insights data you are requesting does not exist or is currently unavailable the API will return an empty data set instead of `0` for individual metrics.

[](#)

UTC
---

Timestamps in API responses use UTC with zero offset and are formatted using ISO-8601. For example: `2019-04-05T07:56:32+0000`

[](#)

Endpoints
---------

The API consists of the following endpoints:

* [`GET /{ig-media-id}/insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights) — gets metrics on a media object
* [`GET /{ig-user-id}/insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights) — gets metrics on an Instagram Business Account or Instagram Creator account.

Refer to each endpoint's reference documentation for available metrics, parameters, and permission requirements.

[](#)

Examples
--------

### Getting Account Metrics

To get metrics on an Instagram Business or Creator Account, query the [`GET /{ig-user-id}/insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights) edge and specify the metrics you want returned.

#### Sample Request

GET graph.facebook.com/17841405822304914/insights
    ?metric\=impressions,reach,profile\_views
    &period\=day

#### Sample Response

{
  "data": \[
    {
      "name": "impressions",
      "period": "day",
      "values": \[
        {
          "value": 32,
          "end\_time": "2018-01-11T08:00:00+0000"
        },
        {
          "value": 32,
          "end\_time": "2018-01-12T08:00:00+0000"
        }
      \],
      "title": "Impressions",
      "description": "Total number of times the Business Account's media objects have been viewed",
      "id": "instagram\_business\_account\_id/insights/impressions/day"
    },
    {
      "name": "reach",
      "period": "day",
      "values": \[
        {
          "value": 12,
          "end\_time": "2018-01-11T08:00:00+0000"
        },
        {
          "value": 12,
          "end\_time": "2018-01-12T08:00:00+0000"
        }
      \],
      "title": "Reach",
      "description": "Total number of times the Business Account's media objects have been uniquely viewed",
      "id": "instagram\_business\_account\_id/insights/reach/day"
    },
    {
      "name": "profile\_views",
      "period": "day",
      "values": \[
        {
          "value": 15,
          "end\_time": "2018-01-11T08:00:00+0000"
        },
        {
          "value": 15,
          "end\_time": "2018-01-12T08:00:00+0000"
        }
      \],
      "title": "Profile Views",
      "description": "Total number of users who have viewed the Business Account's profile within the specified period",
      "id": "instagram\_business\_account\_id/insights/profile\_views/day"
    }
  \]
}

### Getting Media Metrics

To get metrics on a media object, query the [`GET /{ig-media-id}/insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights) edge and specify the metrics you want returned.

#### Sample Request

GET graph.facebook.com/{media\-id}/insights
    ?metric\=engagement,impressions,reach

#### Sample Response

{
  "data": \[
    {
      "name": "engagement",
      "period": "lifetime",
      "values": \[
        {
          "value": 8
        }
      \],
      "title": "Engagement",
      "description": "Total number of likes and comments on the media object",
      "id": "media\_id/insights/engagement/lifetime"
    },
    {
      "name": "impressions",
      "period": "lifetime",
      "values": \[
        {
          "value": 13
        }
      \],
      "title": "Impressions",
      "description": "Total number of times the media object has been seen",
      "id": "media\_id/insights/impressions/lifetime"
    },
    {
      "name": "reach",
      "period": "lifetime",
      "values": \[
        {
          "value": 13
        }
      \],
      "title": "Reach",
      "description": "Total number of unique accounts that have seen the media object",
      "id": "media\_id/insights/reach/lifetime"
    }
  \]
}

[](#)

[](#)

Mentions
========

Identify captions, comments, and IG Media in which an Instagram Business or Creator's alias has been tagged or @mentioned.

Limitations
-----------

* Mentions on Stories are not supported.
* Commenting on photos in which you were tagged is not supported.
* [Webhooks](#webhooks) will not be sent if the Media upon which the comment or @mention appears was created by an account that is set to [private](https://www.facebook.com/help/instagram/448523408565555).

[](#)

Endpoints
---------

The API consists of the following endpoints:

* [`GET /{ig-user-id}/tags`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/tags) — to get the media objects in which a Business or Creator Account has been tagged
* [`GET /{ig-user-id}?fields=mentioned_comment`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_comment#reading) — to get data about a comment that an Business or Creator Account has been @mentioned in
* [`GET /{ig-user-id}?fields=mentioned_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_media#reading) — to get data about a media object on which a Business or Creator Account has been @mentioned in a caption
* [`POST /{ig-user-id}/mentions`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentions#creating) — to reply to a comment or media object caption that a Business or Creator Account has been @mentioned in by another Instagram user

Refer to each endpoint reference document for usage instructions.

[](#)

Webhooks
--------

Subscribe to the `mentions` field to recieve [Instagram Webhooks](https://developers.facebook.com/docs/instagram-api/guides/webhooks) notifications whenever an Instagram user mentions an Instagram Business or Creator Account. Note that we do not store Webhooks notification data, so if you set up a Webhook that listens for mentions, you should store any received data if you plan on using it later.

[](#)

Examples
--------

### Listening for and Replying to Comment @Mentions

You can listen for comment @mentions and reply to any that meet your criteria:

1. Set up an [Instagram webhook](https://developers.facebook.com/docs/instagram-api/guides/webhooks) that's subscribed to the `mentions` field.
2. Set up a script that can parse the Webhooks notifications and identify comment IDs.
3. Use the IDs to query the `GET /{ig-user-id}/mentioned_comment` endpoint to get more information about each comment.
4. Analyze the returned results to identify any comments that meet your criteria.
5. Use the `POST /{ig-user-id}/mentions` endpoint to [reply to those comments](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentions#creating).

The reply will appear as a sub-thread comment on the comment in which the Business or Creator Account was mentioned.

### Listening for and Replying to Caption @Mentions

You can listen for caption @mentions and reply to any that meet your criteria:

1. Set up an [Instagram webhook](https://developers.facebook.com/docs/instagram-api/guides/webhooks) that's subscribed to the `mentions` field.
2. Set up a script that can parse the Webhooks notifications and identify media IDs.
3. Use the IDs to query the `GET /{ig-user-id}/mentioned_media` endpoint to get more information about each media object.
4. Analyze the returned results to identify media objects with captions that meet your criteria.
5. Use the `POST /{ig-user-id}/mentions` endpoint to [comment on those media objects](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentions#creating).

[](#)

[](#)

Product Tagging
===============

You can use the Instagram Graph API to create and manage [Instagram Shopping Product Tags](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F2022466637835789&h=AT3yeJqP6HVaU2lve_hAFmw5XIYaBQzkja4gHl0o-URn_XZNbD_URVZrSIDmcFwxknn3aBTmCZKp6URIZnrQwd3QTlODCvQFpsOolSWmL6kYcO13Pus5JZJqVd29QEuM9U7_LzKTiVx5Ldvp3wZYZQ) on an Instagram Business's [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/).

**Note:** Beginning August 10, 2023, some businesses without checkout-enabled Shops will no longer be able to tag their products using the Content Publishing API. This will impact both API and native interfaces, and will remove tags to products from previous posts.Customers will still be able to tag products from Shops with checkout enabled on Facebook and Instagram. You can still refer to `shopping_product_tag_eligibility` field to check if an Instagram account is eligible to tag their products using Content Publishing API.

The general flow for tagging products is:

1. Check if the Instagram Business is [eligible for product tagging](#get-eligibility).
2. If the Instagram Business is eligible, [get its product catalogs](#get-available-catalogs).
3. [Search each catalog for products](#get-catalog-products) that are eligible for tagging.
4. [Create a tagged media container](#post-media).
5. [Publish the tagged media container](#post-media-publish).

Limitations
-----------

* All [content publishing limitations](https://developers.facebook.com/docs/instagram-api/guides/content-publishing#limitations) apply to product tagging.
* Product tagging is not supported for Stories and Live.
* Product tagging is not supported for Instagram Creator accounts.
* Accounts are limited to 25 tagged media posts within a 24 hour period. Carousel albums count as a single post.

[](#)

Requirements
------------

* Refer to each endpoint's reference document to determine which permissions, features, and [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access tokens are required for each operation.
* The Instagram Business account (IG User) that owns the IG Media (to be tagged) must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0qoE3VZM94zqpzik-A1-wRBoWDtQSRpQUKwrBy9ef7y-y8XsQERaqDGgSJfAO3mWfyBY16uzUOPIixregwcRk3Qjj-xmuogqadgiUfOJvJT69UOfmUURe4jlX2T_b8SwpCTX6ctpnSeFAij3ardg) with a product catalog containing products. In-app and external Instagram Shop [checkout methods](https://www.facebook.com/business/help/449169642911614) are supported.
* The app user must have an [admin role](https://www.facebook.com/business/help/442345745885606) on the [Business Manager](https://business.facebook.com/) that owns the Instagram Shop whose products are being used to tag media.
* In order to request [App Review](https://developers.facebook.com/docs/app-review) approval for the [`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products) and [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management) permissions, which are required by several product tagging endpoints, your app must be associated with a [verified business](https://developers.facebook.com/docs/development/release/business-verification).

[](#)

Endpoints
---------

* [`GET /{ig-user-id}`](https://developers.facebook.com/docs/instagram-api/reference/ig-user#read) — Check the app user's tagging eligibility.
* [`GET /{ig-user-id}/available_catalogs`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/available_catalogs#reading) — Get a list of the app user's product catalogs.
* [`GET /{ig-user-id}/catalog_product_search`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/catalog_product_search#reading) — Get a list of tag eligible products in the app user's catalog.
* [`POST /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) — Create a tagged media container (step 1 of publishing process).
* [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish) — Publish a tagged media container (step 2 of publishing process).
* [`GET /{ig-media-id}/product_tags`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags#reading) — Get tags on published IG Media.
* [`DELETE /{ig-media-id}/product_tags`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags#deleting) — Delete tags on published IG Media.
* [`POST /{ig-media-id}/product_tags`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags#creating) — Create or update tags on published IG Media.
* [`GET /{ig-user-id}/product_appeal`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/product_appeal#reading) — Get product appeal information.
* [`POST /{ig-user-id}/product_appeal`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/product_appeal#creating) — Appeal a product rejection.
* [`GET /{ig-media-id}/children`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/children#read) — Get a list of child IG Media in a carousel IG Media.

[](#)

Get User Eligibility
--------------------

Request the `shopping_product_tag_eligibility` field on the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) endpoint to determine if the Instagram Business account has set up an [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT21nwWiIas4YNl3oi3FqU2ZMnby9dkct6n3Y8lT5xRKBc7VNVoPwX8tvJB27DdWLzy7DWYVJHAxAeCbxSyKnxxq1MrepYseZzcR4NeHfLgowufaBRco5bB_Xzgdx_rRPRwbCXlcG0hGkEH8bdNPAA). Accounts that have not set up an Instagram Shop are ineligible for product tagging.

GET /{ig\-user\-id}?fields\=shopping\_product\_tag\_eligibility

Returns `true` if the Instagram Business account has been associated with a [Business Manager's](https://business.facebook.com/) approved Instagram Shop, otherwise returns `false`.

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/`v18.0`/90010177253934?fields=shopping\_product\_tag\_eligibility&access\_token=EAAOc..."

#### Sample Response

{
  "shopping\_product\_tag\_eligibility": true,
  "id": "90010177253934"
}

[](#)

Get Catalogs
------------

Use the [IG User Available Catalogs](https://developers.facebook.com/docs/instagram-api/reference/ig-user/available_catalogs) endpoint to get the Instagram Business account's product catalog.

GET /{ig\-user\-id}/available\_catalogs

Returns an array of catalogs and their metadata. Responses can include the following catalog fields:

* `catalog_id` — Catalog ID.
* `catalog_name` — Catalog name.
* `shop_name` — Shop name.
* `product_count` — Total number of products in the catalog.

#### Limitations

Collaborative catalogs such as shopping partner catalogs or affiliate creator catalogs are not supported.

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/`v18.0`/90010177253934?fields=available\_catalogs&access\_token=EAAOc..."

#### Sample Response

{
  "available\_catalogs": {
    "data": \[
      {
        "catalog\_id": "960179311066902",
        "catalog\_name": "Jay's Favorite Snacks",
        "shop\_name": "Jay's Bespoke",
        "product\_count": 11
      }
    \]
  },
  "id": "90010177253934"
}

[](#)

Get Eligible Products
---------------------

Use the [IG User Catalog Product Search](https://developers.facebook.com/docs/instagram-api/reference/ig-user/catalog_product_search) endpoint to get a collection of products in the catalog that can be used to tag media. Product variants are supported.

Although the API will not return an error when publishing a post tagged with an unapproved product, the tag will not appear on the published post until the product has been approved. Therefore, we recommend that you only allow your app users to publish posts with tags whose products have a `review_status` of `approved`. This field is returned for each product by default when you get an app user's eligible products.

GET /{ig\-user\-id}/catalog\_product\_search

#### Parameters

* `catalog_id` — **(required)** Catalog ID.
* `q` — A string to search for in each product's name, or a product's SKU number (the **Content ID** column in the catalog management interface). If no string is specified, all tag-eligible products will be returned.

Returns an object containing an array of tag-eligible products and their metadata. Supports [cursor-based pagination](https://developers.facebook.com/docs/graph-api/results#cursors). Responses can include the following product fields:

* `image_url` — Product image URL.
* `is_checkout_flow` — If `true`, product can be purchased directly in the Instagram app. If `false`, product must be purchased in the app user's app/website.
* `merchant_id` — Merchant ID.
* `product_id` — Product ID.
* `product_name` — Product name.
* `retailer_id` — Retailer ID.
* `review_status` — Review status. Values can be `approved`, `outdated`, `pending`, `rejected`. An approved product can appear in the app user's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0MV9YbV_4Y9TW40JAXiPB7fB6sVXXR5ah6SeYvVAIvlS-pnR28f0U2-v2tJM5oQgAAlkh7G55OA7ciJmIuAY5hHLMlBWO8TzKIupY0cuADPfbm7UHikcPGpJfuI0YdOj4u1MN8YPe75uujO8uY2Q), but an approved status does not indicate product availability (e.g, the product could be out of stock). Only tags associated with products that have a `review_status` of `approved` can appear on published posts.
* `product_variants` — Product IDs (`product_id`) and variant names (`variant_name`) of [product variants](https://developers.facebook.com/docs/marketing-api/catalog/guides/product-variants).

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/`v18.0`/90010177253934/catalog\_product\_search?catalog\_id=960179311066902&q=gummy&access\_token=EAAOc..."

#### Sample Response

{
  "data": \[
    {
      "product\_id": 3231775643511089,
      "merchant\_id": 90010177253934,
      "product\_name": "Gummy Wombats",
      "image\_url": "https://scont...",
      "retailer\_id": "oh59p9vzei",
      "review\_status": "approved",
      "is\_checkout\_flow": true,
      "product\_variants": \[
            {
              "product\_id": 5209223099160494
            },
            {
              "product\_id": 7478222675582505,
              "variant\_name": "Green Gummy Wombats"
            }
          \]
    }
  \]
}

[](#)

Create a Tagged Container for Images or Videos
----------------------------------------------

Use the [IG User Media](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media) endpoint to create a media container for an [image](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#create-photo-container) or [video](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#create-video-container). Alternatively, see [Create Tagged Media Container for Reels](#post-media-reels) or [Carousels](#carousels).

POST /{ig\-user\-id}/media

#### Parameters

* `image_url` — (**required** for images only) The path to the image. Your image must be on a public server.
* `user_tags` — (images only) An array of public usernames and x/y coordinates for any public Instagram users who you want to tag in the image. The array must be formatted in JSON and contain a `username`, `x`, and `y` property. For example, `[{username:'natgeo',x:0.5,y:1.0}]`. `x` and `y` values must be floats that originate from the top-left of the image, with a range of `0.0`–`1.0`. Tagged users will receive a notification when the media is published.
* `video_url` — (**required** for videos only) The path to the video. Your video must be on a public server.
* `thumb_offset` — (videos only) The location, in milliseconds, of the frame for the video's cover thumbnail image. The default value is `0`, which is the first frame of the video.
* `product_tags` — (**required**) An array of objects specifying the product tags to add to the image or video. You can specify up to 20 tags for photo and video feed posts and up to 20 tags total per carousel post (up to 5 per carousel slide).
    * The tags and product IDs must be unique.
    * Tags for out-of-stock products are supported.
    * Each object should have the following information:  
        * `product_id` — (**required**) Product ID.
        * `x` — (images only) A float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.
    * `y` — (images only) A float that indicates percentage distance from top edge of the pu blished media image. Value must be within `0.0`–`1.0` range.

If the operation is successful the API returns a container ID which you can use to [publish the container](#post-media-publish).

#### Sample Request

curl \-i \-X POST \\
 "https://graph.facebook.com/`v18.0`/90010177253934/media?image\_url=https%3A%2F%2Fupl...&location\_id=7640348500&product\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3231775643511089'%2C%0A%20%20%20%20x%3A%200.5%2C%0A%20%20%20%20y%3A%200.8%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/v12.0/90010177253934/media?image\_url=https://upl...&location\_id=7640348500
&product\_tags=\[
  {
    product\_id:'3231775643511089',
    x: 0.5,
    y: 0.8
  }
\]&access\_token=EAAOc...

#### Sample Response

{
  "id": "17969578066508312"
}

[](#)

Create a Tagged Container for Reels
-----------------------------------

Use the [IG User Media](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media) endpoint to create a media container for Reels. Alternatively, see [Create Tagged Media Container](#post-media) or [Carousels](#carousels).

POST /{ig\-user\-id}/media

#### Parameters

* `media_type` — You must specify the media type `REELS`.
* `video_url` — The path to the video for the Reel. Your video must be on a public server. Your video must meet the [Reels Specifications](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#reel-specifications).
* `thumb_offset` — The location, in milliseconds, of the frame for the video's cover thumbnail image. The default value is `0`, which is the first frame of the video.
* `caption` — The caption for the Reel.
* `product_tags` — (**required**) An array of objects specifying the product tags to add to the Reel. You can specify up to 30 tags, and the tags and product IDs must be unique. Tags for out-of-stock products are supported. Each object should have the following information:  
    * `product_id` — (**required**) Product ID.
* `location_id` — The ID of a Page associated with a location that you want to tag the video with. For details, see [IG User Media Query String Parameters](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#query-string-parameters).
* `share_to_feed` — `true` to request that the video appears on both the Feed and Reels tabs. `false` to request that the video appears only on the Reels tab.
* `access_token` — Your [User Access Token](https://developers.facebook.com/docs/facebook-login/guides/access-tokens).

If the operation is successful the API returns a container ID which you can use to [publish the container](#post-media-publish).

#### Sample Request

curl \-i \-X POST \\
 "https://graph.facebook.com/`v18.0`/90010177253934/media?media\_type=REELS&video\_url=https://upl...&product\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3231775643511089'%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/v12.0/90010177253934/media?media\_type=REELS&video\_url=https://upl...
&product\_tags=\[
  {
    product\_id:'3231775643511089'
  }
\]&access\_token=EAAOc...

#### Sample Response

{
  "id": "17969578066508312"
}

[](#)

Publish a Tagged Media Container
--------------------------------

Use the [IG User Media Publish](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish) endpoint to publish the tagged media container. You may publish up to 25 tagged media containers on behalf of an app user within a 24 hour moving period. If you are publishing a carousel, see [Carousels](#carousels). Only products that have a `review_status` of `approved` will appear on published posts. If any of these products are out of stock, their tags will still appear on the published post.

POST /{ig\-user\-id}/media\_publish

#### Parameters

* `creation_id` — (**required**) The carousel container ID.

If the operation is successful the API will return an IG Media ID.

#### Sample Request

curl \-i \-X POST \\
 "https://graph.facebook.com/`v18.0`/90010177253934/media\_publish?creation\_id=17969578066508312&access\_token=EAAOc"

#### Sample Response

{
  "id": "90010778325754"
}

[](#)

Get Tags On Media
-----------------

Use the [IG Media Product Tags](https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags#reading) endpoint to get tags on published media.

GET /{ig\-media\-id}/product\_tags

Returns an array of product tags and their metadata on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/). Responses can include the following product tag fields:

* `product_id` — Product ID.
* `merchant_id` — Merchant ID.
* `name` — Product name.
* `price_string` — Product price.
* `image_url` — Product image URL.
* `review_status` — Indicates product tag eligibility status. Values can be:
* `approved` — Product is approved.
* `rejected` — Product was rejected.
* `pending` — Still undergoing review.
* `outdated` — Product was approved but has been edited and requires reapproval.
* `""` — No review status.
* `no_review` — No review status.
* `is_checkout` — If `true`, product can be purchased directly through the Instagram app. If `false`, product can only be purchased on the merchant's website.
* `stripped_price_string` — Product short price string (price displayed in constrained spaces, such as `$100` instead of `100 USD`).
* `string_sale_price_string` — Product sale price.
* `x` — A float that indicates percentage distance from left edge of media image. Value within `0.0`–`1.0` range.
* `y` — A float that indicates percentage distance from top edge of media image. Value within `0.0`–`1.0` range.

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/`v18.0`/90010778325754/product\_tags?access\_token=EAAOc..."

#### Sample Response

{
  "data": \[
    {
      "product\_id": 3231775643511089,
      "merchant\_id": 90010177253934,
      "name": "Gummy Wombats",
      "price\_string": "$3.50",
      "image\_url": "https://scont...",
      "review\_status": "approved",
      "is\_checkout": true,
      "stripped\_price\_string": "$3.50",
      "x": 0.5,
      "y": 0.80000001192093
    }
  \]
}

[](#)

Tag Existing Media
------------------

Use the [IG Media Product Tags](https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags#creating) endpoint to create or update tags on existing [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/).

POST /{ig\-media\-id}/product\_tags

#### Parameters

* `updated_tags` — (**required**) An array of objects specifying which product tags to tag the image or video with (maximum of 5; tags and product IDs must be unique). Each object should have the following information:
* `product_id` — (**required**) Product ID. If the IG Media has not been tagged with this ID the tag will be added to the IG Media. If the media has already been tagged with this ID, the tag's display coordinates will be updated.
* `x` — (images only, **required**) A float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.
* `y` — (images only, **required**) A float that indicates percentage distance from top edge of the published media image. Value must be within `0.0`–`1.0` range.

Tagging media is additive until the 5 tag limit has been reached. If the targeted media has already been tagged by a product in the request, the old tag's `x` and `y` values will be updated with their new values (a new tag will not be added).

Returns `true` if able to update the product, otherwise returns `false`.

#### Sample Request

curl \-i \-X POST \\
 "https://graph.facebook.com/`v18.0`/90010778325754/product\_tags?updated\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3859448974125379'%2C%0A%20%20%20%20x%3A%200.5%2C%0A%20%20%20%20y%3A%200.8%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/v12.0/90010778325754/product\_tags?updated\_tags=\[
  {
    product\_id:'3859448974125379',
    x: 0.5,
    y: 0.8
  }
\]&access\_token=EAAOc...

#### Sample Response

{
  "success": true
}

[](#)

Delete Tags
-----------

Use the [IG Media Product Tags](https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags#deleting) endpoint to delete tags on a published [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) including Reels.

DELETE /{ig\-media\-id}/product\_tags

#### Parameters

* `deleted_tags` — (**required**) An array containing the following information for each product tag to be deleted:
* `merchant_id` — (**required**) Merchant ID.
* `product_id` — (**required**) Product ID.

Returns `true` if tag deletion successful, otherwise returns `false`.

#### Sample Request

curl \-i \-X DELETE \\
 "https://graph.facebook.com/`v18.0`/90010778325754/product\_tags?deleted\_tags=%5B%0A%20%20%7B%0A%20%20%20%20product\_id%3A'3859448974125379'%2C%0A%20%20%20%20merchant\_id%3A'90010177253934'%0A%20%20%7D%0A%5D&access\_token=EAAOc..."

For reference, here is the HTML-decoded POST payload string:

https://graph.facebook.com/v12.0/90010778325754/product\_tags?deleted\_tags=\[
  {
    product\_id:'3859448974125379',
    merchant\_id:'90010177253934'
  }
\]&access\_token=EAAOc...

#### Sample Response

{
  "success": true
}

[](#)

Appeal Product Rejection
------------------------

Use the [IG User Product Appeal](https://developers.facebook.com/docs/instagram-api/reference/ig-user/product_appeal#creating) endpoint it you want to provide a way for your app users to appeal product [rejections](https://www.facebook.com/help/instagram/1907693709488725) (tags of rejected products will not appear on published posts). Although not required, we do recommend that you provide a way for app users to appeal rejections, or advise them to appeal rejections [using the Business Manager](https://www.facebook.com/business/help/494867298080532).

POST /{ig\-user\-id}/product\_appeal

#### Parameters

* `appeal_reason` — (**required**) Explanation of why the product should be approved.
* `product_id` — (**required**) Product ID.

Returns `true` if we are able to receive your request, otherwise returns `false`. Response does not indicate appeal outcome.

#### Sample Request

curl \-i \-X POST \\

"https://graph.facebook.com/`v18.0`/90010177253934/product\_appeal?appeal\_reason=product%20is%20a%20toy%20and%20not%20a%20real%20weapon&product\_id=4382881195057752&access\_token=EAAOc..."

#### Sample Response

{
  "success": true
}

[](#)

Get Appeal Status
-----------------

Use the [IG User Product Appeal](https://developers.facebook.com/docs/instagram-api/reference/ig-user/product_appeal#reading) endpoint to get the status of an appeal for a given [rejected](https://www.facebook.com/help/instagram/1907693709488725) product:

GET /{ig\-user\-id}/product\_appeal

#### Parameters

* `product_id` — (**required**) Product ID.

Returns appeal status metadata. Responses can include the following appeal fields:

* `eligible_for_appeal` — Indicates if decision can be appealed (yes if `true`, no if `false`).
* `product_id` — Product ID.
* `review_status` — Review status. Value can be:
* `approved` — Product is approved.
* `rejected` — Product was rejected.
* `pending` — Still undergoing review.
* `outdated` — Product was approved but has been edited and requires reapproval.
* `""` — No review status.
* `no_review` — No review status.

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/`v18.0`/90010177253934/product\_appeal?product\_id=4029274203846188&access\_token=EAAOc..."

#### Sample Response

{
  "data": \[
    {
      "product\_id": 4029274203846188,
      "review\_status": "approved",
      "eligible\_for\_appeal": false
    }
  \]
}

[](#)

Carousels
---------

You can publish carousels (albums) containing up to 10 total tagged images, videos, or a mix of the two. To do this, when performing step 1 of 3 of the [carousel posts](https://developers.facebook.com/docs/instagram-api/guides/content-publishing#carousel-posts) publishing process, simply create [tagged media containers](#create-tagged-media-container) for each tagged image or video that you want to appear in the album carousel and continue with the carousel publishing processs as you normally would.

### Get child media in a carousel

To get the IDs of IG Media in an album carousel, use the [IG Media Children](https://developers.facebook.com/docs/instagram-api/reference/ig-media/children) endpoint.

[](#)

[](#)

The following content is from the [Webhooks product documentation](https://developers.facebook.com/docs/graph-api/webhooks). Please refer to the Webhooks documentation if you are unfamiliar with Webhooks.

Set Up Webhooks for Instagram
=============================

Webhooks for [Instagram](https://developers.facebook.com/docs/instagram-api) allow you to receive real-time notifications whenever someone comments on the Media objects of your app users; [@mentions](https://developers.facebook.com/docs/pages/mentions) your app users; or when Stories of your app users expire.

[](#)

Receive Live Webhook Notifications
----------------------------------

To receive live webhook notifications, the following conditions must be satisfied:

* Your app must have **Instagram** webhooks configured and appropriate **fields** subscribed to in the App Dashboard.
* For [Consumer apps](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#consumer), they must be in [Live Mode.](https://developers.facebook.com/docs/development/build-and-test/app-modes#live-mode)
* For [Business apps](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#business), they must have permissions with an [Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels#advanced-access) level. You can request Advanced Access for permissions as shown here:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/277167266_482444906912677_1666124645911161205_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=nsfuyyt9TswAX83DrLO&_nc_oc=AQkHGfXzNUVolzf3lDqBu4rw4oNpYynpkuw7paVX4T9tSo6pQWpVsmCmXReHb77eSao&_nc_ht=scontent-cdg4-3.xx&oh=00_AfBcH9lp-iFiFCXLYJKR3mYeSoaRG4J33IAWez9WfrPIRw&oe=65AE3490)

If the app permissions don't have an access level of **Advanced Access**, the app doesn't receive webhook notifications.

* The app user must have granted your app appropriate permissions ([instagram\_manage\_insights](https://developers.facebook.com/docs/permissions/reference/instagram_manage_insights) for Stories, [instagram\_manage\_comments](https://developers.facebook.com/docs/permissions/reference/instagram_manage_comments) for Comments and @Mentions).
* The Page connected to the app user's account must have [Page subscriptions enabled](https://developers.facebook.com/docs/instagram-api/guides/webhooks/#step-2--enable-page-subscriptions).
* The Business connected to the app user's Page must be **verified**.
* The owner of the Media object upon which the comment or @mention appears must not have set their account to [private](https://www.facebook.com/help/instagram/448523408565555).

### Limitations

* Webhook notifications for Comments on albums don't include the album ID. Get the album ID by querying the Comment ID in the webhook and request its `media` field.
* Apps don't receive a webhook notifications if the Media where the comment or @mention appears was created by a [private account](https://www.facebook.com/help/instagram/448523408565555).
* Story insights metrics with counts of less than 5 are returned as `-1`.
* Apps only receive webhook notifications for comments on live [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) if the media is on broadcast.
* Reels are not supported.
* Your app must have successfully completed App Review (advanced access) to receive webhooks notifications for `comments` and `live_comments` webhooks fields.

[](#)

Step 1: Create an Endpoint
--------------------------

[Create an endpoint](https://developers.facebook.com/docs/graph-api/webhooks/getting-started) that accepts and processes webhooks. During the [configuration](https://developers.facebook.com/docs/graph-api/webhooks/getting-started#configure-webhooks-product), select the **Instagram Graph API** object, click **Set up**, and subscribe to one or more [Instagram fields](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/).

### Instagram Fields

| Field | Description | Permissions Required |
| --- | --- | --- |
| [`comments`](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/#comments) | Comments on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) owned by your app's Instagram user.<br><br>The `ad_id` and `ad_title` will be returned in the media object when a person comments on a boosted Instagram post or Instagram ads post. This may result in duplicate webhook notifications. | * [instagram\_manage\_comments](https://developers.facebook.com/docs/permissions/reference/instagram_manage_comments)<br>* [pages\_manage\_metadata](https://developers.facebook.com/docs/permissions/reference/pages_manage_metadata)<br>* [pages\_read\_engagement](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement) **or**  <br>    [pages\_show\_list](https://developers.facebook.com/docs/permissions/reference/pages_show_list) |
| [`live_comments`](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/#live_comments) | Comments on a live [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) owned by your app's Instagram user. | * [instagram\_manage\_comments](https://developers.facebook.com/docs/permissions/reference/instagram_manage_comments)<br>* [pages\_manage\_metadata](https://developers.facebook.com/docs/permissions/reference/pages_manage_metadata)<br>    <br>* [pages\_read\_engagement](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement) **or**  <br>    [pages\_show\_list](https://developers.facebook.com/docs/permissions/reference/pages_show_list) |
| [`mentions`](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/#mentions) | @mentions for your app's Instagram user in a comment. | * [instagram\_manage\_comments](https://developers.facebook.com/docs/permissions/reference/instagram_manage_comments)<br>* [pages\_manage\_metadata](https://developers.facebook.com/docs/permissions/reference/pages_manage_metadata)<br>    <br>* [pages\_read\_engagement](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement) **or**  <br>    [pages\_show\_list](https://developers.facebook.com/docs/permissions/reference/pages_show_list) |
| [`story_insights`](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/#story_insights) | Metrics describing interactions on a story. Sent 1 hour after the story expires. | * [instagram\_manage\_insights](https://developers.facebook.com/docs/permissions/reference/instagram_manage_insights)<br>* [pages\_manage\_metadata](https://developers.facebook.com/docs/permissions/reference/pages_manage_metadata)<br>    <br>* [pages\_read\_engagement](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement) **or**  <br>    [pages\_show\_list](https://developers.facebook.com/docs/permissions/reference/pages_show_list) |

[](#)

Step 2: Enable Page Subscriptions
---------------------------------

Your app must enable Page subscriptions on the Page connected to the app user's account by sending a `POST` request to the [Page Subscribed Apps](https://developers.facebook.com/docs/graph-api/reference/page/subscribed_apps#Creating) edge and subscribing to any Page field.

### Endpoint Requirements

* the app user's Page Access Token
* [pages\_manage\_metadata](https://developers.facebook.com/docs/instagram-api/guides/docs/permissions/reference/pages_manage_metadata)

#### Request Syntax

POST /{page\-id}/subscribed\_apps
  ?access\_token\={access\-token}
  &subscribed\_fields\={fields}

#### Request Parameters

| Value Placeholder | Value Description |
| --- | --- |
| `{page_id}` | ID of the Page connected to the app user's account. |
| `{access_token}` | App user's Page access tToken. |
| `{fields}` | A Page field (example: `feed`). |

Your app does not receive notifications for changes to a field unless you configure Page subscriptions in the App Dashboard and subscribe to that field.

#### Sample Request

curl \-i \-X POST \\
  "https://graph.facebook.com/`v18.0`/1755847768034402/subscribed\_apps?subscribed\_fields=feed&access\_token=EAAFB..."

##### Sample Response

{
  "success": true
}

[](#)

Common Uses
-----------

### Capture Story Insights

If you subscribe to the `story_insights` field, we send your endpoint a webhook notification containing user interaction metrics on a story, after the story has expired.

#### Sample Story Insights Payload

\[
  {
    "entry": \[
      {
        "changes": \[
          {
            "field": "story\_insights",
            "value": {
              "media\_id": "18023345989012587",
              "exits": 1,
              "replies": 0,
              "reach": 17,
              "taps\_forward": 12,
              "taps\_back": 0,
              "impressions": 28
            }
          }
        \],
        "id": "17841405309211844",  // Instagram Business or Creator Account ID
        "time": 1547687043
      }
    \],
    "object": "instagram"
  }
\]

### Reply to Comment @Mentions

If you subscribe to the `mentions` field, we send your endpoint a webhook notification whenever an Instagram user @mentions an Instagram Business or Creator Account in a comment or caption.

For example, here's a sample comment webhook notification payload sent for an Instagram Business Account (`17841405726653026`):

#### Sample Comment @Mention Payload

\[
  {
    "entry": \[
      {
        "changes": \[
          {
            "field": "mentions",
            "value": {
              "comment\_id": "17894227972186120",
              "media\_id": "17918195224117851"
            }
          }
        \],
        "id": "17841405726653026",
        "time": 1520622968
      }
    \],
    "object": "instagram"
  }
\]

### Get the Comment's Contents

To get the comment's contents, use the `comment_id` property to query the [`GET /{ig-user-id}/mentioned_comment`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_comment) edge:

#### Sample Query

GET https://graph.facebook.com/17841405726653026
  ?fields=mentioned\_comment.comment\_id(17894227972186120)

#### Sample Response

{
  "mentioned\_comment": {
    "timestamp": "2018-03-20T00:05:29+0000",
    "text": "@bluebottle challenge?",
    "id": "17894227972186120"
  },
  "id": "17841405726653026"
}

### Parse the Payload and Respond

When you get the response, parse the payload for the `text` property to determine if you want to respond to the comment. To respond, use the webhook notification payload's `caption_id` and `media_id` property values to query the [`POST /{ig-user-id}/mentions`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentions) endpoint:

#### Sample Query

curl \-i \-X POST \\
  \-d "comment\_id=17894227972186120" \\
  \-d "media\_id=17918195224117851" \\
  \-d "message=Challenge%20accepted!" \\
  \-d "access\_token={access-token}" \\
  "https://graph.facebook.com/17841405726653026/mentions"

#### Sample Response

{
  "id": "17911496353086895"
}

### Reply to Caption @Mentions

If you subscribe to the `mentions` field, we send your endpoint a webhook notification whenever a user @mentions an Instagram Business or Creator Account in a comment or caption on a media object not owned by the Business or Creator.

For example, here's a sample caption @mention webhook notification sent for an Instagram Business Account (`17841405726653026`):

#### Sample Caption @Mention Webhook Notification

\[
  {
    "entry": \[
      {
        "changes": \[
          {
            "field": "mentions",
            "value": {
              "media\_id": "17918195224117851"
            }
          }
        \],
        "id": "17841405726653026",
        "time": 1520622968
      }
    \],
    "object": "instagram"
  }
\]

### Get the Caption's Contents

To get the caption's contents, use the `media_id` property to query the [`GET /{ig-user-id}/mentioned_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_media) edge:

#### Sample Query

GET https://graph.facebook.com/17841405726653026
  ?fields=mentioned\_media.media\_id(17918195224117851){caption,media\_type}

#### Sample Response

{
  "mentioned\_media": {
    "caption": "@bluebottle There can be only one!",
    "media\_type": "IMAGE",
    "id": "17918195224117851"
  },
  "id": "17841405726653026"
}

### Parse the Payload and Respond

When you get the response, parse the payload for the `caption` property to determine if you want to respond to the comment. To respond, use the webhook `media_id` property to query the [`POST /{ig-user-id}/mentions`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentions) edge:

#### Sample Query

curl \-i \-X POST \\
  \-d "media\_id=17918195224117851" \\
  \-d "message=MacLeod%20agrees!" \\
  \-d "access\_token={access-token}" \\
  "https://graph.facebook.com/17841405726653026/mentions"

#### Sample Response

{
  "id": "17911496353086895"
}

[](#)

[](#)

Changelog
=========

This changelog refers to changes made for the Instagram Graph API.

### Related Changelogs

* [Graph API Changelog ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22)](https://developers.facebook.com/docs/graph-api/changelog) 
    
* [Messenger Platform Changelog ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22)](https://developers.facebook.com/docs/messenger-platform/changelog) (includes Instagram Messaging)
    
* [Marketing API Changelog ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22)](https://developers.facebook.com/docs/graph-api/changelog) 
    

September 12, 2023
------------------

#### Deprecation of Media and User Insights

_Applies to v18.0+. Will apply to all versions on December 11, 2023._

Duplicative and legacy Instagram insight metrics are being deprecated. Please see documentation for the endpoints and [Instagram Insights](https://developers.facebook.com/docs/instagram-api/guides/insights) for more information on which metrics to use in their place.

The following endpoints and metrics are affected:

* [`GET /{ig-user-id}/insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights)
    * `AUDIENCE_GENDER_AGE`
    * `AUDIENCE_LOCALE`
    * `AUDIENCE_COUNTRY`
    * `AUDIENCE_CITY`
* [`GET /{ig-media-id}/insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights)
    * `CAROUSEL_ALBUM_IMPRESSIONS`
    * `CAROUSEL_ALBUM_REACH`
    * `CAROUSEL_ALBUM_ENGAGEMENT`
    * `CAROUSEL_ALBUM_SAVED`
    * `CAROUSEL_ALBUM_VIDEO_VIEWS`
    * `TAPS_FORWARD`
    * `TAPS_BACK`
    * `EXITS`
    * `ENGAGEMENT`

**Note:** `total_interactions`, which is listed as an alternative for some of the deprecated metrics, is currently only available using version 18.0 and does not work with older versions. When querying older versions before Dec 11, 2023, please use the `engagement` metric.`total_interactions`, which is listed as an alternative for some of the deprecated metrics, is currently only available using version 18.0 and does not work with older versions. When querying older versions before Dec 11, 2023, please use the `engagement` metric.

[](#)

[](#)

November 9, 2022
----------------

#### Instagram Webhooks

_Applies to all versions._

The `ad_id` and `ad_title` will be returned in the `media` object of the `comments` field's `value` object when a person comments on a [boosted Instagram post or Instagram ads post](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1067656009937668&h=AT0FLA6Ts5AR3NldH39gwLESbYVRIxT27y9lkp9YMHDiLmspV04QMc4K0jjrpttfRV9NjYFOxE-vRm02eAixTb5VspeCB1xELwY_JMIZei76UF2rq20kXJPUitG5bf702EceuVNnvkJqiFmg8BVKrw).

[](#)

October 31st
------------

#### Reels – Product Tags

_Applies to all versions._

Instagram Product Tagging API for Reels is made available. You can tag up to 30 products when publishing a reel.

[](#)

June 28, 2022
-------------

#### Reels

_Applies to all versions._

Reels are now supported. To publish a video as a reel, set the `media_type` parameter to `REELS` when creating a [single media post](https://developers.facebook.com/docs/instagram-api/guides/content-publishing#single-media-posts) container. Refer to the [`POST /ig-user/media endpoint`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) reference to learn which parameters can be used with reels as well as requirements for reels videos.

**Note:** Beginning November 9, 2023, the `VIDEO` value for `media_type` will no longer be supported. Use the `REELS` media type to publish a video to your feed.

[](#)

June 27, 2022
-------------

#### Legacy Instagram API Documentation

_Applies to all versions._

The [Legacy Instagram API developer documentation](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fdeveloper%2F&h=AT20CBm_KVpAzyC0HS57TFJT_btVDTZZT4jaPWc9Usr6DM8D-g-XHPfgjF0oBCQRz2oy4dhBiKt4LDVpPkZoNlI-IWUQM5Wh_Pos-UmnPYB_Ib64c3qZAPqWTlK6wOMe_Wx1rNCcMXHisLnQF_Spyg) has been removed and now redirects to the [Instagram Platform](https://developers.facebook.com/docs/instagram) developer documentation.

[](#)

June 20, 2022
-------------

#### Product Tagging

_Applies to all versions._

You can now create and manage [Instagram Shopping Product Tags](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F2022466637835789&h=AT0ScVB5HSkQReWcNaTD8olXFgT22gfYQRAcKaycWZp_EZKM-f7EgPpd5wZknfQcZPz-oEsOBUcE1MEqRS69wT4JB6231Z2j3Z-sNeb1zbwxmvBxkfF--mdXgLKqXayH7FbgX3lGJVFs1migp04xWg) on an Instagram Business's published media. Refer to the [Product Tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging) guide to learn how.

[](#)

May 27, 2022
------------

#### Product Variants

_Applies to all versions._

For partners in the [Product Tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging) beta, all [product variants](https://developers.facebook.com/docs/marketing-api/catalog/guides/product-variants) that match a query's search criteria will now be returned when [searching a catalog for products](https://developers.facebook.com/docs/instagram-api/guides/product-tagging#get-eligible-products).

[](#)

March 15, 2022
--------------

#### Carousel Posts

_Applies to all versions._

You can now use the Instagram API to publish posts containing multiple images and videos ([carousel posts](https://developers.facebook.com/docs/instagram-api/guides/content-publishing#carousel-posts)). Refer to the [Content Publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) guide for complete publishing steps.

If your app has already been approved for [permissions](https://developers.facebook.com/docs/instagram-api/guides/content-publishing#permissions) required for content publishing, it does not need to undergo [App Review](https://developers.facebook.com/docs/app-review) again to take advantage of this functionality.

[](#)

November 9, 2021
----------------

#### Live Videos

_Applies to all versions._

You can now use the Instagram API to get live video IG Media being broadcast by your app users, get comments on those videos, and use the Instagram Messaging API to send private replies (direct messages) to the comment authors. To support this functionality, the following changes have been made:

* a new [GET /ig-user/live\_media](https://developers.facebook.com/docs/instagram-api/reference/ig-user/live_media#reading) edge can return live video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) being broadcast by your app user at the time of the request
* the `media` field on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment/) now returns and object containing both the ID (`id`) and published location (`media_product_type`) of the media upon which the comment was made
* a new [`live_comments`](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/#live_comments) Instagram Webhooks field can send notifications containing live comments made on your app users' live videos as they are being broadcast

Please refer to the [Instagram Messaging API](https://developers.facebook.com/docs/messenger-platform/instagram) private replies documentation to learn how to send [private replies](https://developers.facebook.com/docs/messenger-platform/instagram/features/private-replies) to users who have commented on your app users' live video IG Media.

[](#)

October 20, 2021
----------------

#### IG Comments

_Applies to all versions._

Two new [fields](https://developers.facebook.com/docs/instagram-api/reference/ig-comment#fields) have been added to [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment):

* `from` — returns an object containing the [IGSID](https://developers.facebook.com/docs/messenger-platform/instagram/overview#igsid) (`id`) and username (`username`) of the comment creator.
* `parent_id` — returns the ID of the parent IG Comment if this comment was created on another IG Comment (i.e. a reply to another comment).

#### Instagram Webhooks

_Applies to all versions._

The `comments` Instagram webhooks [field](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/#comments) now includes the following properties in the `value` field object:

* `from.id` — [IGSID](https://developers.facebook.com/docs/messenger-platform/instagram/overview#igsid) of the Instagram user who created the comment.
* `from.username` — Username of the Instagram user who created the comment
* `media.id` — ID of the IG Media upon which the comment was made.
* `media.media_product_type` — Surface (published location) of the IG Media upon which the comment was made.
* `parent_id` — ID of parent IG Comment if this comment was created on another IG Comment (i.e. a reply to another comment).

[](#)

October 5, 2021
---------------

The following changes apply to Instagram TV videos created on or after October 5, 2021. Instagram TV videos created before this date are exempt from these changes.

* the `media_product_type` [field](https://developers.facebook.com/docs/instagram-api/reference/ig-media/#fields) will return `FEED` instead of `IGTV`
* the `video_title` [field](https://developers.facebook.com/docs/instagram-api/reference/ig-media/#fields) will not be returned
* [Instagram Webhooks](https://developers.facebook.com/docs/instagram-api/guides/webhooks) `comments` and `mentions` fields are now supported

On January 3, 2022, the changes above will apply to all API versions and all Instagram TV videos, regardless of video creation date. This means that starting January 3, 2022, apps using older API versions will be able to query Instagram TV videos (read support was introduced in v10.0 and limited to v10.0+).

Starting with v14.0, the `video_title` field will no longer be supported and the API will throw an error if the field is requested.

[](#)

June 8, 2021
------------

#### Like Counts

_Applies to v11.0+. Will apply to all versions September 7, 2021._

If indirectly querying an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) through another endpoint or field expansion, the [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.

  

#### Time-based Pagination

_Applies to v11.0+_.

Added [`since`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/#query-string-parameters) and [`until`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/#query-string-parameters) parameters to the [`GET /{ig-user-id}/media`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/#reading) endpoint to support [time-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#time).

[](#)

May 26, 2021
------------

If indirectly querying an IG Media through another endpoint, the [like\_count](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will now return `0` if the app user does not [own](https://developers.facebook.com/docs/instagram-api/overview#authorization) the media and the media owner has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts on it. Directly querying the IG Media, which can only be done by the IG Media owner, will return the actual like count, even if the owner has hidden like counts on the media.

[](#)

May 4, 2021
-----------

Made a minor change to how we calculate the [`online_followers`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights#metrics-and-periods) metric on IG Users.

[](#)

April 14, 2021
--------------

Story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights#metrics) interactions performed by users in Japan are no longer included in some `replies` metric calculations:

* For stories created by users in Japan, the `replies` metric will now return a value of `0`.
* For stories created by users outside Japan, the `replies` metric will return the number of replies, but replies made by users in Japan will not be included in the calculation.

[](#)

April 12, 2021
--------------

Fixed a minor bug with reach [metrics](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights#metrics) on story IG Media.

[](#)

April 9, 2021
-------------

* The `status` field on an [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) now returns an [error subcode](https://developers.facebook.com/docs/instagram-api/reference/error-codes) if the container's `error_code` field value is `ERROR`.
* The [IG Media Insights](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights) `video_views` metric now supports albums and will return the sum of `video_views` on all videos in the album instead of `0`.

[](#)

March 16, 2021
--------------

IGTV media is [now supported in v10.0+](https://developers.facebook.com/blog/post/2021/03/15/igtv-media-mmetrics-instagram-graph-api/). This applies to all endpoints except those used for content publishing and webhooks. To support this change, new `media_product_type` and `video_title` fields have been added to the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) node. IGTV media must have been shared to Instagram at the time of publish (**Post a Preview** or **Share Preview** to Feed enabled) in order to be accessible via the API.

[](#)

Januray 26, 2021
----------------

The Content Publishing beta has ended and all developers can now publish media on Instagram Professional accounts. Refer to the [Content Publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) guide for usage details.

[](#)

December 2, 2020
----------------

In compliance with the European Union's [ePrivacy Directive](https://l.facebook.com/l.php?u=https%3A%2F%2Feur-lex.europa.eu%2Flegal-content%2FEN%2FTXT%2F%3Furi%3DCELEX%253A02002L0058-20091219&h=AT13E7YFWryPPoYL1_geokNynBd5lQ15OugVKAmqbi6B935kVqnFv634xzOCU7Cbc6HlXYzL0NHGCAtuGbzEiI7BwXXOYOlgvyunJI6BAgj0BMihTGkBas8Ap6G4C52eCzykvnUCwGloMyb-wUjASA), messaging-related Story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) interactions performed by users in the European Economic Area (EEA) after December 1, 2020, will no longer be included in some metric calculations:

* For Stories created by users in the EEA, the [`replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights#metrics) metric will now return a value of `0`.
* For Stories created by users outside the EEA, the [`replies`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights#metrics) metric will return the number of replies, but replies made my users in the EEA will not be included in its calculation.

This change applies to all versions.

[](#)

November 10, 2020
-----------------

* **IG User Insights** — The [`follower_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights) values now align more closely with their corresponding values displayed in the Instagram app. In addition, [`follower_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights) now returns a maximum of 30 days of data instead of 2 years. This change applies to v9.0+ and will apply to all versions May 9, 2021.

[](#)

May 5, 2020
-----------

* **Hashtag Search** — _This change applies to v7.0+_ — You can now request the `timestamp` field on [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) returned by [`GET /{ig-hashtag-id}/top_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/top-media#reading) and [`GET /{ig-hashtag-id}/recent_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/recent-media#reading) [Hashtag Search](https://developers.facebook.com/docs/instagram-api/guides/hashtag-search) queries. For example: `GET /{ig-hashtag-id}/top_media?fields=timestamp`.

[](#)

December 3, 2019
----------------

* **Insights** — To align API behavior with Instagram app behavior, insights on [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user/) are now only available on IG Users that have 100 or more followers.

[](#)

August 13, 2019
---------------

* **Business Discovery** — The [Business Discovery API](https://developers.facebook.com/docs/instagram-api/reference/ig-user/business_discovery) can now be used to get data about other Instagram Creator accounts.

[](#)

May 22, 2019
------------

* **Instagram Creator Accounts** — The API now supports [Instagram Creator Accounts](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1158274571010880&h=AT2vnZ3GvBjlfKJl1ALTXxp9OC_8bBsuWXjXVukmhRzE9vwG6aOhpuYho_eLIJm0Fp0_Z9TSBVd_CBbjoQTRe0Eozx9aYXCsUVUEYF6fQQ_bfl5bYT5yFKqRRtQq1U1RruJPu-Dmarc_SMydAsQ77A), with two exceptions. (1) The [Content Publishing API](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) cannot be used by Instagram Creators, and (2) the [Business Discovery API](https://developers.facebook.com/docs/instagram-api/guides/business-discovery) can be used by Creators but can only target Businesses.

[](#)

May 9, 2019
-----------

* **Webhooks** — The `story_insights` field now requires the `instagram_manage_insights` permission instead of `instagram_manage_comments`.

[](#)

October 31, 2018
----------------

* **Hashtag Search API** — You can now search for media tagged with specific hashtags by using our new [Hashtag Search API](https://developers.facebook.com/docs/instagram-api/guides/hashtag-search). `#spooky`!

[](#)

October 23, 2018
----------------

* `/{ig-media-id}/comments` edge — `GET` requests made using API version 3.1 or older will have results returned in chronological order. Requests made using version 3.2+ will have results returned in reverse chronological order.

[](#)

June 7, 2018
------------

* `/{ig-media-id}` node — You can now use field expansion to get the `permalink` field on media objects.

[](#)

May 1, 2018
-----------

* **Business Verification** — In order to use the Instagram Graph API, all apps must undergo [Business Verification](https://developers.facebook.com/docs/apps/review), which is part of the App Review process and now required for all Instagram Graph API endpoints. Apps previously reviewed before May 1st, 2018, have to be reviewed again, and have until August 1st, 2018 to do so, or lose access to the API.

[](#)

April 24, 2018
--------------

* `/{ig-comment-id}` node:
    
    * Added a new `username` field.
    * For `GET` requests, the `user` field will not be included in responses unless the User making the request owns the Comment; instead, we will return `username` for all commenters. This also applies to queries on Comments made through other APIs, such as the Mentions API.
    
* `/{ig-media-id}` node:
    
    * Added a new `username` field.
    * For `GET` requests, the `owner` field will not be included in responses unless the User making the request owns the media object; instead, we will return `username` for all commenters. This also applies to queries on media objects made through other APIs, such as the Mentions API.
    

[](#)

April 23, 2018
--------------

* **Insights API** — Insights will now include ad activity generated through the API, Facebook ads interfaces, and Instagram's Promote feature. This affects the following metrics:
    
    * `impressions`
    * `reach`
    

[](#)

March 13, 2018
--------------

* **Content Publishing API** — Beta partners can now use the `/{ig-user-id}/media` edge to tag [locations](https://developers.facebook.com/docs/instagram-api/guides/content-publishing#publish-with-locations) and public Instagram [users](https://developers.facebook.com/docs/instagram-api/guides/content-publishing#publish-with-tagged-users) when publishing photos.

[](#)

March 8, 2018
-------------

* **Public fields** — The `timestamp` field on the `/{ig-media-id}` node is now a public field and can be returned via field expansion.

[](#)

February 22, 2018
-----------------

* **Public fields** — The `/{ig-user-id}`, `/{ig-comment-id}`, and `/{ig-media-id}` nodes will now return all public fields when accessed through an edge via field expansion. Refer to each node's reference document to see which fields are public.

[](#)

February 8, 2018
----------------

* **Content Publishing API** — Beta partners can now include hashtags when publishing photos via the `/{ig-user-id}/media` edge. `#crazywildebeest` FTW!

[](#)

[](#)