LinkedIn API Overview
=====================

LinkedIn's home for API documentation for all LinkedIn business lines. Our API documentation is organized by business lines covering Consumer, Compliance, Learning, Marketing, Sales, and Talent Solutions. Follow the links below to learn more about business lines and their possible integration types.

Getting Access to LinkedIn APIs
===============================

The LinkedIn API uses [OAuth 2.0](http://oauth.net/2/) for user authorization and API authentication. Applications must be authorized and authenticated before they can fetch data from LinkedIn or get access to member data. This page summarizes the available permissions and partner programs available for accessing LinkedIn APIs. Most permissions and partner programs require explicit approval from LinkedIn. [Open Permissions](#open-permissions-consumer) are the only permissions that are available to all developers without special approval.

All permissions listed below are used in either [Member Authentication Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) (3-legged) or [Application Authentication Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow) (2-legged). More about these permission types can be found in [Authenticating with OAuth 2.0 Overview](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication).

Open Permissions (Consumer)
---------------------------

The following permissions are available to all developers, and may be added via self-service through the LinkedIn [Developer Portal](https://www.linkedin.com/developers/), under the Products tab on your application page. LinkedIn products can be enabled after creating a new application.

| Product/Program | Permission | Description |
| --- | --- | --- |
| Sign in with LinkedIn using OpenID Connect | profile | **Member Auth**: Retrieve authenticated member's name, headline, and photo. |
| Sign in with LinkedIn using OpenID Connect | email | **Member Auth**: Retrieve authenticated member's primary email address. |
| Share on LinkedIn | w\_member\_social | **Member Auth**: Post, comment and like posts on behalf of an authenticated member. |

Learning
--------

Developers seeking to build a learning related integration should refer to the [Request API Access](https://learn.microsoft.com/en-us/linkedin/learning/getting-started/request-access) page within the LinkedIn Learning API space.

Marketing
---------

Developers seeking to build a marketing related integration using Advertising APIs permissions must be approved. You can apply for access through the [Developer Portal](https://www.linkedin.com/developers/). This can be done by selecting your app from [My Apps](https://www.linkedin.com/developers/apps), navigate to the Products tab, and add the Marketing Developer Platform product. Qualifications to be an Advertising APIs partner are available at [Become a Partner](https://business.linkedin.com/marketing-solutions/marketing-partners/become-a-partner/marketing-developer-program).

Audiences permissions may be applied for after being an approved Marketing Developer Platform partner. Contact support or your partner rep for application information.

| Product/Program | Permission | Description |
| --- | --- | --- |
| Advertising APIs | rw\_organization\_admin | **Member Auth**: Manage an authenticated member’s company pages and retrieve reporting data. |
| Advertising APIs | r\_organization\_admin | **Member Auth**: Retrieve an authenticated member’s company pages and their reporting data. |
| Advertising APIs | w\_organization\_social | **Member Auth**: Post, comment and like posts on behalf of an organization. Restricted to organizations in which the authenticated member has one of the following company page roles.* `ADMINISTRATOR`<br>* `DIRECT_SPONSORED_CONTENT_POSTER`<br>* `LEAD_GEN_FORMS_MANAGER` |
| Advertising APIs | r\_organization\_social | **Member Auth**: Retrieve organizations' posts, comments, and likes. |
| Marketing Developer Platform (MDP) | w\_member\_social | **Member Auth**: Post, comment, and like posts on behalf of an authenticated member. |
| Advertising APIs | rw\_ads | **Member Auth**: Manage and read an authenticated member's ad accounts. Restricted to ad accounts in which the authenticated member has one of the following ad account roles.* `ACCOUNT_BILLING_ADMIN`<br>* `ACCOUNT_MANAGER`<br>* `CAMPAIGN_MANAGER`<br>* `CREATIVE_MANAGER` |
| Advertising APIs | r\_ads | **Member Auth**: Read an authenticated member's ad accounts. Restricted to ad accounts in which the authenticated member has one of the following ad account roles:<br><br>* `ACCOUNT_BILLING_ADMIN`<br>* `ACCOUNT_MANAGER`<br>* `CAMPAIGN_MANAGER`<br>* `CREATIVE_MANAGER`<br>* `VIEWER` |
| Advertising APIs | r\_ads\_reporting | **Member Auth**: Retrieve reporting for advertising accounts. |
| Advertising APIs | r\_1st\_connections\_size | **Member Auth**: Retrieve the count of an authenticated member's 1st-degree connections. |
| Advertising APIs | r\_basicprofile | **Member Auth**: Read an authenticated member's basic profile including name, photo, headline, and public profile URL. |
| Lead Sync | r\_marketing\_leadgen\_automation | **Member Auth**: Access your lead generation forms and retrieve leads (including event leads, ad leads, and organization page leads). |
| Audiences | rw\_dmp\_segments | **Member Auth**: Create and manage matched audiences. |

Sales
-----

Developers seeking to build sales related integration using one of the permissions below must be approved as a Sales Navigator Application Platform (SNAP) partner. [Apply here](https://business.linkedin.com/sales-solutions/partners/become-a-partner) to be a SNAP partner.

| Product/Program | Permission | Description |
| --- | --- | --- |
| Sales Navigator Application Platform(SNAP) | r\_sales\_nav\_analytics | **Member Auth**: Enables access to Sales Navigator Analytics retrieval. |
| Sales Navigator Application Platform(SNAP) | r\_sales\_nav\_display | **Member Auth**: Display Services permission for Sales Navigator. |
| Sales Navigator Application Platform(SNAP) | r\_sales\_nav\_validation | **Application Auth**: Access Sales Navigator endpoints for CRM data validation. |
| Sales Navigator Application Platform(SNAP) | r\_sales\_nav\_profiles | **Application Auth**: Access Sales Navigator endpoints that present matched, publicly available member profile information. |

Talent
------

Developers seeking to build talent related integrations through one of the programs listed below can [apply here](https://business.linkedin.com/talent-solutions/ats-partners/partner-application). We recommend familiarizing yourself with the types of partner integrations available before applying by visiting [here](https://business.linkedin.com/talent-solutions/ats-partners#all) and [here](https://business.linkedin.com/talent-solutions/talent-hub/integrations#all).

* [Recruiter System Connect (RSC)](https://learn.microsoft.com/en-us/linkedin/talent/recruiter-system-connect)
* [Apply Connect](https://learn.microsoft.com/en-us/linkedin/talent/apply-connect)
* [Talent Hub](https://learn.microsoft.com/en-us/linkedin/talent/talent-hub-integrations)
* [Apply with LinkedIn](https://learn.microsoft.com/en-us/linkedin/talent/apply-with-linkedin/apply-with-linkedin)
* [Premium Job Posting](https://learn.microsoft.com/en-us/linkedin/talent/premium-job-posting)
* [Easy Apply](https://learn.microsoft.com/en-us/linkedin/talent/easy-apply)

Compliance (Closed)
-------------------

The following permissions used for Compliance integrations are listed for reference purposes only. Access is closed and may not be requested.

| Product/Program | Permission | Description |
| --- | --- | --- |
| Compliance | r\_compliance | **Member Auth**: Retrieve activities for compliance monitoring and archiving |
| Compliance | w\_compliance | **Member Auth**: Manage and delete data for compliance. |

Overview
========

The LinkedIn API uses [OAuth 2.0](http://oauth.net/2/) for member (user) authorization and API authentication. Applications must be authorized and authenticated before they can fetch data from LinkedIn or get access to LinkedIn member data.

There are two types of Authorization Flows available:

* [**Member Authorization (3-legged OAuth)**](#member-authorization-3-legged-oauth-flow)
* [**Application Authorization (2-legged OAuth)**](#application-authorization-2-legged-oauth-client-credential-flow)

Depending on the type of permissions your integration will require, follow one of the authorization flows to get started.

Note

* There are several third-party libraries in the open source community which abstract the OAuth 2.0 authentication process in every major programming language.
* LinkedIn does not support TLS 1.0.

Member Authorization (3-legged OAuth Flow)
------------------------------------------

The Member Authorization grants permissions to your application by a LinkedIn member to access the member’s resources on LinkedIn. Your application has no access to these resources without member approval. The Member Auth uses the 3-legged OAuth code flow. For step-by-step instructions on how to implement 3-legged OAuth, see [**Authorization Code Flow (3-legged OAuth)**](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) page.

Tip

**When to use 3-legged OAuth**  
Use this flow if you are requesting access to a member's account to use their data and make requests on their behalf. This is the most commonly used permission type across LinkedIn APIs. Open permissions available to all applications are of this type such as `r_liteprofile`, `r_emailaddress`, and `w_member_social`.

### Member Auth Permissions

**Member Authorization Permissions** are granted by a LinkedIn member to access members resources on LinkedIn. Permissions are authorization consents to access LinkedIn resources. The LinkedIn platform uses permissions to protect and prevent abuse of member data. Your application must have the appropriate permissions before it can access data. To see the list of permissions, descriptions and access details, refer to [Getting Access to LinkedIn APIs](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access) page.

Application Authorization (2-legged OAuth Client Credential Flow)
-----------------------------------------------------------------

Application Authorization or using 2-Legged OAuth grants permissions to your application to access protected LinkedIn resources. If you are accessing APIs that are not member specific, use this flow. Not all APIs support Application Authorization. For example, Marketing APIs you must use Member Authorization explained above. For step-by-step instructions on how to implement 2-legged OAuth, see [**Client Credential Flow (2-legged OAuth)**](https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow?context=linkedin/context) page.

Note

Always request the minimal permission scopes necessary for your use case.

### Application Auth Permissions

Application Authorization Permissions are granted to applications to access LinkedIn protected resources. To see the list of permissions, descriptions and access details, refer to [Getting Access to LinkedIn APIs](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access) page.

### Sample Application

You can explore the [OAuth Sample Applications](https://learn.microsoft.com/en-us/linkedin/shared/authentication/sample-applications) that enables you to try out RESTful OAuth calls to the LinkedIn Authentication server. The sample app is available in Java.

Additionally, you can also explore the [Marketing Sample Application](https://learn.microsoft.com/en-us/linkedin/marketing/sample-apps-lms).

Authorization Code Flow (3-legged OAuth)
========================================

The Authorization Code Flow is used for applications to request permission from a LinkedIn member to access their account data. The level of access or profile detail is explicitly requested using the `scope` parameter during the [authorization](#step-2-request-an-authorization-code) process outlined below. This workflow will send a consent prompt to a selected member, and once approved your application may begin making API calls on behalf of that member.

This approval process ensures that LinkedIn members are aware of what level of detail an application may access or action it may perform on their behalf.

If multiple scopes are requested, the user must be consent to all of them and may not select individual scopes. For the benefit of your LinkedIn users, please ensure that your application requests the least number of scope permissions.

Note

**Generate a Token Manually Using the Developer Portal**  
The LinkedIn Developer Portal has a token generator for manually creating tokens. Visit the [LinkedIn Developer Portal Token Generator](https://www.linkedin.com/developers/tools/oauth/token-generator) or follow the steps outlined in [Developer Portal Tools.](https://learn.microsoft.com/en-us/linkedin/shared/authentication/developer-portal-tools)

Authorization Code Flow
-----------------------

1. Configure your application in the Developer Portal to obtain _Client ID_ and _Client Secret_.
2. Your application directs the browser to LinkedIn's OAuth 2.0 authorization page where the member authenticates.
3. After authentication, LinkedIn's authorization server passes an authorization code to your application.
4. Your application sends this code to LinkedIn and LinkedIn returns an access token.
5. Your application uses this token to make API calls on behalf of the member.

How to Implement 3-legged OAuth
-------------------------------

Follow the steps given below to implement the 3-legged OAuth for LinkedIn APIs:

### Prerequisites

* A LinkedIn Developer application to [create a new application](https://www.linkedin.com/developer/apps/new?csrfToken=ajax%3A8674117952230020505) or [select your existing application](https://www.linkedin.com/developers/apps)
* Prior authorization access granted for at least one 3-legged OAuth permission.

The permission request workflow is outlined in the [Getting Access](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access) section.

Step 1: Configure Your Application
----------------------------------

1. Select your application in the [LinkedIn Developer Portal](https://www.linkedin.com/developers/apps).
2. Click the **Auth** tab to view your application credentials.
3. Add the redirect (callback) URL via `HTTPS` to your server.

Note

LinkedIn servers will only communicate with URLs that you have identified as trusted.

* URLs must be absolute:
    * `https://dev.example.com/auth/linkedin/callback`
    * _not_ `/auth/linkedin/callback`
* parameters are ignored:
    * `https://dev.example.com/auth/linkedin/callback?id=1`
    * _will be_ `https://dev.example.com/auth/linkedin/callback`
* URLs cannot include a #
    * `https://dev.example.com/auth/linkedin/callback#linkedin` is invalid.

If you are using Postman to test this flow, use `https://oauth.pstmn.io/v1/callback` as your redirect URL and enable **Authorize using browser**.

Each application is assigned a unique **Client ID** (Consumer key/API key) and **Client Secret**. Please make a note of these values as they will be integrated into your application. Your **Client Secret** protects your application's security so be sure to keep it secure!

Warning

Do not share your _Client Secret_ value with anyone, and **do not** pass it in the URL when making API calls, or URI query-string parameters, or post in support forums, chat, etc.

Step 2: Request an Authorization Code
-------------------------------------

To request an authorization code, you must direct the member's browser to LinkedIn's OAuth 2.0 authorization page, where the member either accepts or denies your application's permission request.

Once the request is made, one of the following occurs:

1. If it is a first-time request, the permission request timed out, or was manually revoked by the member: the browser is redirected to LinkedIn's authorization consent window.
    
2. If there is an existing permission grant from the member: the authorization screen is bypassed and the member is immediately redirected to the URL provided in the `redirect_uri` query parameter.
    

When the member completes the authorization process, the browser is redirected to the URL provided in the `redirect_uri` query parameter.

Note

If the `scope` permissions are changed in your app, your users must re-authenticate to ensure that they have explicitly granted your application all of the permissions that it is requesting on their behalf.

    GET https://www.linkedin.com/oauth/v2/authorization
    

| Parameter | Type | Description | Required |
| --- | --- | --- | --- |
| response\_type | string | The value of this field should always be: `code` | Yes |
| client\_id | string | The _API Key_ value generated when you registered your application. | Yes |
| redirect\_uri | url | The URI your users are sent back to after authorization. This value must match one of the _Redirect URLs_ defined in your [application configuration](https://www.linkedin.com/developers/). For example, `https://dev.example.com/auth/linkedin/callback`. | Yes |
| state | string | A unique string value of your choice that is hard to guess. Used to prevent [CSRF](http://en.wikipedia.org/wiki/Cross-site_request_forgery). For example, `state=DCEeFWf45A53sdfKef424`. | No  |
| scope | string | URL-encoded, space-delimited list of member permissions your application is requesting on behalf of the user. These must be explicitly requested. For example, `scope=liteprofile%20emailaddress%20w_member_social`. See [Permissions](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication) and [Best Practices for Application Development](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/application-development?context=linkedin/context) for additional information. | Yes |

The scopes available to your app depend on which Products or Partner Programs your app has access to. This information is available in the [Developer Portal](https://www.linkedin.com/developers/apps). Your app's Auth tab will show current scopes available. You can apply for new Products under the Products tab. If approved, your app will have access to new scopes.

#### Sample Request

    GET https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={your_client_id}&redirect_uri={your_callback_url}&state=foobar&scope=liteprofile%20emailaddress%20w_member_social
    

Once redirected, the member is presented with LinkedIn's authentication screen. This identifies your application and outlines the particular member permissions/scopes that your application is requesting. You can change the logo and application name in the Developer Portal under My apps > [Settings](https://www.linkedin.com/developers/apps)

#### Member Approves Request

By providing valid LinkedIn credentials and clicking **Allow**, the member approves your application's request to access their member data and interact with LinkedIn on their behalf. This approval instructs LinkedIn to redirect the member to the redirect URL that you defined in your `redirect_uri`parameter.

    https://dev.example.com/auth/linkedin/callback?state=foobar&code=AQTQmah11lalyH65DAIivsjsAQV5P-1VTVVebnLl_SCiyMXoIjDmJ4s6rO1VBGP5Hx2542KaR_eNawkrWiCiAGxIaV-TCK-mkxDISDak08tdaBzgUYfnTJL1fHRoDWCcC2L6LXBCR_z2XHzeWSuqTkR1_jO8CeV9E_WshsJBgE-PWElyvsmfuEXLQbCLfj8CHasuLafFpGb0glO4d7M
    

Attached to the `redirect_uri` are two important URL arguments that you need to read from the request:

* `code` — The OAuth 2.0 authorization code.
* `state` — A value used to test for possible [CSRF](http://en.wikipedia.org/wiki/Cross-site_request_forgery) attacks.

The `code` is a value that you exchange with LinkedIn for an OAuth 2.0 access token in the next step of the authentication process. For security reasons, the authorization code has a 30-minute lifespan and must be used immediately. If it expires, you must repeat all of the previous steps to request another authorization code.

Warning

Before you use the authorization code, your application should ensure that the value returned in the `state` parameter matches the `state` value from your original authorization code request. This ensures that you are dealing with the real member and not a malicious script. If the state values do not match, you are likely the victim of a [CSRF](http://en.wikipedia.org/wiki/Cross-site_request_forgery) attack and your application should return a `401 Unauthorized` error code in response.

#### Failed Requests

If the member chooses to cancel, or the request fails for any reason, the client is redirected to your `redirect_uri` with the following additional query parameters appended:

* `error` - A code indicating one of these errors:
    * `user_cancelled_login` - The member declined to log in to their LinkedIn account.
    * `user_cancelled_authorize` - The member refused to authorize the permissions request from your application.
* `error_description` - A URL-encoded textual description that summarizes the error.
* `state` - A value passed by your application to prevent [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) attacks.

For more error details, refer [here](#oauthv2authorization)

Step 3: Exchange Authorization Code for an Access Token
-------------------------------------------------------

The next step is to get an access token for your application using the authorization code from the previous step.

    POST https://www.linkedin.com/oauth/v2/accessToken
    

To do this, make the following HTTP POST request with a `Content-Type` header of `x-www-form-urlencoded` using the following parameters:

| Parameter | Type | Description | Required |
| --- | --- | --- | --- |
| grant\_type | string | The value of this field should always be: `authorization_code` | Yes |
| code | string | The authorization code you received in Step 2. | Yes |
| client\_id | string | The Client ID value generated in Step 1. | Yes |
| client\_secret | string | The Secret Key value generated in Step 1. See the [Best Practices Guide](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/secure-applications?context=linkedin/context) for ways to keep your `client_secret` value secure. | Yes |
| redirect\_uri | url | The same `redirect_uri` value that you passed in the previous step. | Yes |

#### Sample Request

* [https](#tabpanel_1_HTTPS1)
* [curl](#tabpanel_1_cURL1)

    POST  https://www.linkedin.com/oauth/v2/accessToken
     
    Content-Type: application/x-www-form-urlencoded
    grant_type=authorization_code
    code={authorization_code_from_step2_response}
    client_id={your_client_id}
    client_secret={your_client_secret}
    redirect_uri={your_callback_url}
    

    curl --location --request POST 'https://www.linkedin.com/oauth/v2/accessToken' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=authorization_code' \
    --data-urlencode 'code={authorization_code_from_step2_response}' \
    --data-urlencode 'client_id={your_client_id}' \
    --data-urlencode 'client_secret={your_client_secret}' \
    --data-urlencode 'redirect_uri={your_callback_url}'
    

#### Response

A successful access token request returns a [JSON](http://www.json.org/) object containing the following fields:

| Parameter | Type | Description |
| --- | --- | --- |
| access\_token | string | The access token for the application. This value must be kept secure as specified in the [API Terms of Use](https://www.linkedin.com/legal/l/api-terms-of-use). The length of access tokens is ~500 characters. We recommend that you plan for your application to handle tokens with length of at least 1000 characters to accommodate any future expansion plans. This applies to both access tokens and refresh tokens. |
| expires\_in | int | The number of seconds remaining until the token expires. Currently, all access tokens are issued with a 60-day lifespan. |
| refresh\_token | string | Your refresh token for the application. This token must be kept secure. |
| refresh\_token\_expires\_in | int | The number of seconds remaining until the refresh token expires. Refresh tokens usually have a longer lifespan than access tokens. |
| scope | string | URL-encoded, space-delimited list of member permissions your application has requested on behalf of the user. |

    {  
    "access_token":"AQUvlL_DYEzvT2wz1QJiEPeLioeA",
    "expires_in":5184000,
    "scope":"r_basicprofile"
    }
    

For more error details, refer to the [API Error Details](#oauthv2accesstoken) table.

Note

**Access Token Scopes and Lifetime**  
Access tokens stay valid until the number of seconds indicated in the `expires_in` field in the API response. You can go through the OAuth flow on multiple clients (browsers or devices) and simultaneously hold multiple valid access tokens if the same scope is requested. If you request a different scope than the previously granted scope, all the previous access tokens are invalidated.

Step 4: Make Authenticated Requests
-----------------------------------

Once you've obtained an access token, you can start making authenticated API requests on behalf of the member by including an `Authorization` header in the HTTP call to LinkedIn's API.

#### Sample Request

    curl -X GET https://api.linkedin.com/v2/me' \
    -H 'Authorization: Bearer {INSERT_TOKEN}'
    

Step 5: Refresh Access Token
----------------------------

Tip

To protect members' data, LinkedIn does not generate long-lived access tokens.

> Make sure your application refreshes access tokens before they expire, to avoid unnecessarily sending your application's users through the authorization process again.

Refreshing an access token is a seamless user experience. To refresh an access token, go through the [authorization process](#step-2-request-an-authorization-code) again to fetch a new token. This time however, in the refresh workflow, the authorization screen is bypassed, and the member is redirected to your redirect URL, provided the following conditions are met:

* The member is still logged into [www.linkedin.com](https://www.linkedin.com/)
* The member's current access token has not expired

If the member is no longer logged in to [www.linkedin.com](https://www.linkedin.com/) or their access token has expired, they are sent through the normal [authorization process](#step-2-request-an-authorization-code).

Programmatic refresh tokens are available for a limited set of partners. If this feature has been enabled for your application, see [Programmatic Refresh Tokens](https://learn.microsoft.com/en-us/linkedin/shared/authentication/programmatic-refresh-tokens?context=linkedin/context) for instructions.

API Error Details
-----------------

Following are the API errors and its resolution for 3-legged OAuth. If you wish to view the standard HTTP status codes and its meaning, see [Error Handling](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling) page.

#### /oauth/v2/authorization

| HTTP STATUS CODE | ERROR MESSAGE | ERROR DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- |
| 401 | Redirect\_uri doesn’t match | Redirect URI passed in the request does not match the redirect URI added to the developer application. | Ensure that the redirect URI passed in the request match the redirect URI added in the developer application under the Authorization tab. |
| 401 | Client\_id doesn’t match | Client ID passed in the request does not match the client ID of the developer application. | Ensure that the client ID passed is in match with the developer application. |
| 401 | Invalid scope | Permissions passed in the request is invalid | Ensure that the permissions sent in scope parameter is assigned to the developer application in the developer portal. |

#### /oauth/v2/accessToken

| HTTP STATUS CODE | ERROR MESSAGE | ERROR DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- |
| 401 | invalid\_request "Unable to retrieve access token: authorization code not found" | Authorization code sent is invalid or not found. | Check whether the sent authorization code is valid. |
| 400 | invalid\_request "A required parameter "redirect\_uri" is missing" | Redirect\_uri in the request is missing. It is mandatory parameter. | Pass the redirect\_uri in the request to route user back to correct landing page. |
| 400 | invalid\_request "A required parameter "code" is missing" | Authorization code in the request is missing. It is mandatory parameter. | Pass the Authorization code received as part of authorization API call. |
| 400 | invalid\_request "A required parameter "grant\_type" is missing" | Grant type in the request is missing. It is mandatory parameter. | Add grant\_type as "authorization\_code" in the request. |
| 400 | invalid\_request "A required parameter "client\_id" is missing" | Client ID in the request is missing. It is mandatory parameter. | Pass the client id of the app in request. |
| 400 | invalid\_request "A required parameter "client\_secret" is missing" | Client Secret in the request is missing. It is mandatory parameter. | Pass the client secret of the app in request. |
| 400 | invalid\_redirect\_uri "Unable to retrieve access token: appid/redirect uri/code verifier does not match authorization code. Or authorization code expired. Or external member binding exists" | Invalid redirect uri is passed in the request. | Pass the right redirect uri tagged to the developer application. |
| 400 | invalid\_redirect\_uri "Unable to retrieve access token: appid/redirect uri/code verifier does not match authorization code. Or authorization code expired. Or external member binding exists | Invalid Authorization code is sent as part of the request" | Authorization code expired and re-authenticate member to generate new authorization code and pass the fresh authorization code to exchange for access token. |

Client Credential Flow (2-legged OAuth)
=======================================

If your application needs to access APIs that are not member specific, use the Client Credential Flow. Your application **cannot** access these APIs by default.

Learn more:

* [LinkedIn Developer Enterprise products](https://www.linkedin.com/developers/products) and permission requests.
* [LinkedIn Developers Platform](https://www.linkedin.com/help/linkedin/topics/6400/6401/112189) knowledge base.

Important

2-legged OAuth authentication is not available for [Marketing APIs](https://learn.microsoft.com/en-us/linkedin/marketing/getting-started)

Note

**Generate a Token Manually Using the Developer Portal**  
The LinkedIn Developer Portal has a token generator for manually creating tokens. Visit the [LinkedIn Developer Portal Token Generator](https://www.linkedin.com/developers/tools/oauth/token-generator) or follow the steps outlined in [Developer Portal Tools.](https://learn.microsoft.com/en-us/linkedin/shared/authentication/developer-portal-tools)

Step 1: Get Client ID and Client Secret
---------------------------------------

* Getting started? [Create a new application](https://www.linkedin.com/developers/) on the Developer Portal.
* Existing application? Go to [My apps](https://www.linkedin.com/developers/apps) to modify your app settings.

Each application is assigned a unique _Client ID_ (Consumer key/API key) and _Client Secret_. Please make a note of these values as they will be integrated into your application config files. Your _Client Secret_ protects your application's security so be sure to keep it secure!

Warning

Do not share your _Client Secret_ value with anyone, and **do not** pass it in the URL when making API calls, or URI query-string parameters, or post in support forums, chat, etc.

Step 2: Generate an Access Token
--------------------------------

To generate an access token, issue a HTTP POST against `accessToken` with a `Content-Type` header of `x-www-form-urlencoded` and the following parameters in the request body:

    https://www.linkedin.com/oauth/v2/accessToken
    

| Parameter | Description | Required |
| --- | --- | --- |
| grant\_type | The value of this field should always be `client_credentials` | Yes |
| client\_id | The _Client ID_ value generated when you registered your application | Yes |
| client\_secret | The _Client Secret_ value generated when you registered your application | Yes |

* View the [Best Practices for Secure Applications](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/secure-applications?context=linkedin/context) page for more security info.

### Sample Request (Secure Approach)

    POST https://www.linkedin.com/oauth/v2/accessToken HTTP/1.1
    
    Content-Type: application/x-www-form-urlencoded
    grant_type=client_credentials
    client_id={your_client_id}
    client_secret={your_client_secret}
    

A successful access token request returns a [JSON](http://www.json.org/) object containing the following fields:

* `access_token` — The access token for the application. This token must be kept secure.
* `expires_in` — Seconds until token expiration.
    * The access token has a 30-minute lifespan and must be used immediately. You may request a new token once your current token expires.

### Sample Response

    {
        "access_token": "AQV8...",
        "expires_in": "1800"
    }
    

For error details, refer the [API Error Details](#api-error-details) section.

Step 3: Make API Requests
-------------------------

Once you've received an access token, you can make API requests by including an _Authorization_ header with your token in the HTTP call to LinkedIn's API.

### Sample Request

    GET https://api.linkedin.com/v2/jobs HTTP/1.1
    
    Connection: Keep-Alive
    Authorization: Bearer {access_token}
    

API Error Details
-----------------

| HTTP STATUS CODE | ERROR MESSAGE | DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- |
| 401 | invalid\_client\_id "Client authentication failed" | Client Authentication failed due to bad client credentials passed as part of the request. | Check whether the right **Client ID**, **Client Secret** are passed as part of the request. |
| 401 | access\_denied "This application is not allowed to create application tokens" | The developer application doesn’t have enough permission to generate 2L application token. | Reach out to the LinkedIn Relationship Manager or Business Development team to get the necessary access. |
| 400 | invalid\_request "A required parameter "grant\_type" is missing" | Grant type in the request is missing. It is a mandatory parameter. | Add grant\_type as `client_credentials` in the request. |
| 400 | invalid\_request "A required parameter "client\_id" is missing" | Client ID in the request is missing. It is a mandatory parameter. | Pass the Client ID of the developer application in request. |
| 400 | invalid\_request "A required parameter "client\_secret" is missing" | Client Secret in the request is missing. It is a mandatory parameter. | Pass the Client Secret of the developer application in the request. |
| 400 | invalid\_client\_id "The passed in client\_id is invalid "abcdefghijk"" | Invalid client ID is passed in the request. | Pass the right client ID from the developer application. |

Generate an Access Token - Getting Started with Postman
=======================================================

Summary
-------

The full process your application will need to implement for 3-legged tokens is described in [Authorization Code Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) and 2-legged tokens is described in [Client Credentials Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow). The steps outlined below describe the process for using LinkedIn's Public Postman workspaces to generate OAuth tokens for testing. For any specific examples, we will use the Marketing Solutions workspace, but all steps should easily apply to all workspaces. These steps assume you have already created a [free Postman account](https://www.postman.com/postman-account/).

### Step 1 - Application

Go to the [LinkedIn Developer Portal](https://www.linkedin.com/developers/apps), select the app you'll be using, click the "Auth" tab, and locate your Client ID and Client Secret. Please note these values for use later during this process.

### Step 2 - Auth Settings

From the same "Auth" tab, scroll to the bottom of the page. Under "OAuth 2.0 Settings", add the Postman callback URLs `https://oauth.pstmn.io/v1/callback` and `https://oauth.pstmn.io/v1/browser-callback` to your Redirect URL list.

Caution

Postman uses the term "Callback URL"  
LinkedIn uses the term "Redirect URL"

### Step 3 - Fork Collections and Environments

Navigate to LinkedIn's public Postman workspaces:

[](https://www.postman.com/linkedin-developer-apis?tab=workspaces)

Choose a workspace and fork the collections and relevant environments of interest. Each collection will have an environment it should be used with. For example, if you were to navigate to the LinkedIn Marketing Solutions workspace, the Campaign Management collection should be used with the `campaign-management-env` environment.

#### Fork a Postman Collection

Fork a collection:

Fork an environment:

### Step 4 - Fill in Environment Variables

Fill in the Client ID and Client Secret environment variables before moving onto the next step. Don't forget to save your changes!

### Step 5 - Headers

Each collection in each workspace will have its OAuth 2.0 Authorization settings pre-populated with the correct URLs, environment variables, and scopes to be able to successfully run the requests within the corresponding Use Cases folder. Click on a collection title to open it's Authorization tab. Ensure that the correct environment is selected and click "Get new access token":

* Grant Type: Authorization Code (3-legged token) or Client Credentials (2-legged token)
* Callback (Redirect) URL: `https://oauth.pstmn.io/v1/browser-callback`
    * Note the Callback URL should be `https://oauth.pstmn.io/v1/callback` with the "Authorize using browser" box checked if you are using the Postman Desktop app
* Auth URL: `https://www.linkedin.com/oauth/v2/authorization`
* Access Token URL: `https://www.linkedin.com/oauth/v2/accessToken`
* Client ID: {using the client\_id from the environment variables}
* Client Secret: {using the client\_secret from the environment variables}
* Scope: Differs per collection but an example is {`rw_ads,r_basicprofile,w_organization_social,w_member_social,rw_organization_admin`}
* Client Authentication: `Send client credentials in body` when the Grant Type is Authorization Code. `Send as Basic Auth header` when the Grant Type is Client Credentials.

### Step 6 - Identity Authentication

If the Grant Type in Step 5 was Authorization Code then Postman will take you to the LinkedIn authorization page, where you may be prompted to log into LinkedIn. Click "Allow" to authorize the request. The prompt on the authorization page is dictated by the requested scopes in the previous step.

### Step 7 - Use Token

Postman will then display your access token to be used for testing. Choose the 'Use Token' button to set this as the currently used token. The token will automatically be propagated to all requests within the corresponding collection. The video below shows an example of requesting a 3-legged token via the Authorization Code Grant Type.

### Step 8 - Testing

Finally, send a request within the Use Cases folder. Ensure the correct environment is selected and that if any environment or collection level variables are being used in the request, ensure they are set. For example, in the screenshot below, the request uses the `sponsoredaccount_id` variable from the `campaign-management-env` environment.

Learn more about Postman variables in [Postman's online documentation](https://learning.postman.com/docs/sending-requests/variables/#variable-scopes)

Note that some requests dynamically set variables via a script that runs post request execution. You will know if a script is set to run for a request if there is a green dot next to the Tests tab.

To see an example sample response, view the saved example.

Refresh Tokens with OAuth 2.0
=============================

LinkedIn supports programmatic refresh tokens for all approved Marketing Developer Platform (MDP) partners.

Introduction
------------

Refresh tokens are used to get a new access token when your current access token expires. For more information, see the OAuth 2.0 [RFC](https://tools.ietf.org/html/rfc6749#section-1.5).

LinkedIn offers programmatic refresh tokens that are valid for a fixed length of time. By default, access tokens are valid for 60 days and programmatic refresh tokens are valid for a year. The member must reauthorize your application when refresh tokens expire.

When you use a refresh token to generate a new access token, the lifespan or Time To Live (TTL) of the refresh token remains the same as specified in the initial OAuth flow (365 days), and the new access token has a new TTL of 60 days.

For example, on:

* Day 1 - Your refresh token has a TTL of 365 days, and your access token has a TTL of 60 days.
* Day 59 - If you generate a new access token using the refresh token, the access token will have a TTL of 60 days and the refresh token will have a TTL of 306 days (365-59=306).
* Day 360- If you generate a new access token, your access token and refresh token will both expire in 5 days (365-360=5) and you must get your application reauthorized by the member using the authorization flow.

Note

Refresh Tokens are useful in minting new Access tokens and allow for seamless operations for extended periods of time. However, LinkedIn reserves the right to revoke Refresh Tokens or Access Tokens at any time due to technical or policy reasons. In such scenarios, the expectation from products leveraging Refresh Tokens is to fallback to the standard OAuth flow, and present the login screen to the end users.

### Step 1: Getting a Refresh Token

Use the [Authorization Code Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin/context) to get both a refresh token and access token. If your application is authorized for programmatic refresh tokens, the following fields are returned when you exchange the authorization code for an access token:

* `refresh_token` — Your refresh token for the application. This token must be kept secure.
* `refresh_token_expires_in` — The number of seconds remaining until the refresh token expires. Refresh tokens usually have a longer lifespan than access tokens.
* `scope` — URL-encoded, space-delimited list of member permissions your application has requested on behalf of the user.|

#### Sample Response

    {
      "access_token": "AQXNnd2kXITHELmWblJigbHEuoFdfRhOwGA0QNnumBI8XOVSs0HtOHEU-wvaKrkMLfxxaB1O4poRg2svCWWgwhebQhqrETYlLikJJMgRAvH1ostjXd3DP3BtwzCGeTQ7K9vvAqfQK5iG_eyS-q-y8WNt2SnZKZumGaeUw_zKqtgCQavfEVCddKHcHLaLPGVUvjCH_KW0DJIdUMXd90kWqwuw3UKH27ki5raFDPuMyQXLYxkqq4mYU-IUuZRwq1pcrYp1Vv-ltbA_svUxGt_xeWeSxKkmgivY_DlT3jQylL44q36ybGBSbaFn-UU7zzio4EmOzdmm2tlGwG7dDeivdPDsGbj5ig",
      "expires_in": 86400,
      "refresh_token": "AQWAft_WjYZKwuWXLC5hQlghgTam-tuT8CvFej9-XxGyqeER_7jTr8HmjiGjqil13i7gMFjyDxh1g7C_G1gyTZmfcD0Bo2oEHofNAkr_76mSk84sppsGbygwW-5oLsb_OH_EXADPIFo0kppznrK55VMIBv_d7SINunt-7DtXCRAv0YnET5KroQOlmAhc1_HwW68EZniFw1YnB2dgDSxCkXnrfHYq7h63w0hjFXmgrdxeeAuOHBHnFFYHOWWjI8sLLenPy_EBrgYIitXsAkLUGvZXlCjAWl-W459feNjHZ0SIsyTVwzAQtl5lmw1ht08z5Du-RiQahQE0sv89eimHVg9VSNOaTvw",
      "refresh_token_expires_in": 525600,
      "scope":"r_basicprofile"
    
    }
    

Note

Refresh tokens are approximately 500 characters long. We recommend that your application stack be made to handle tokens of at least 1000 characters to accommodate future expansion plans. This applies to access tokens as well as refresh tokens.

### Step 2: Exchanging a Refresh Token for a New Access Token

You can exchange the refresh token for a new access token by making the following HTTP POST request with a `Content-Type` header of `x-www-form-urlencoded` and the following parameters in the request body:

    https://www.linkedin.com/oauth/v2/accessToken
    

| Parameter | Description | Required |
| --- | --- | --- |
| grant\_type | The value of this field should always be refresh\_token. | Yes |
| refresh\_token | The refresh token from Step 1. | Yes |
| client\_id | The Client ID value generated when you registered your application. | Yes |
| client\_secret | The Client Secret value generated when you registered your application. | Yes |

#### Sample Request

    POST https://www.linkedin.com/oauth/v2/accessToken
    
    Content-Type: application/x-www-form-urlencoded
    grant_type=refresh_token&refresh_token=AQQOMeCIQMa6-zjU-02w8EJW67wPVk3hjJE5x1lZhU013LihKD8i1DpvaAl2jnuP8F1uXMgkm8nzjPfnaJR_kQNOxsLRLZWnAMzHMm81S0yQlkBYicw&client_id=861hhm46p48to2&client_secret=gPecS7yqHkyyShvR
    

A successful request returns a new access token with a new expiration time and the refresh token.

    {
      "access_token": "BBBB2kXITHELmWblJigbHEuoFdfRhOwGA0QNnumBI8XOVSs0HtOHEU-wvaKrkMLfxxaB1O4poRg2svCWWgwhebQhqrETYlLikJJMgRAvH1ostjXd3DP3BtwzCGeTQ7K9vvAqfQK5iG_eyS-q-y8WNt2SnZKZumGaeUw_zKqtgCQavfEVCddKHcHLaLPGVUvjCH_KW0DJIdUMXd90kWqwuw3UKH27ki5raFDPuMyQXLYxkqq4mYU-IUuZRwq1pcrYp1Vv-ltbA_svUxGt_xeWeSxKkmgivY_DlT3jQylL44q36ybGBSbaFn-UU7zzio4EmOzdmm2tlGwG7dDeivdPDsGbj5ig",
      "expires_in": 86400,
      "refresh_token": "AQWAft_WjYZKwuWXLC5hQlghgTam-tuT8CvFej9-XxGyqeER_7jTr8HmjiGjqil13i7gMFjyDxh1g7C_G1gyTZmfcD0Bo2oEHofNAkr_76mSk84sppsGbygwW-5oLsb_OH_EXADPIFo0kppznrK55VMIBv_d7SINunt-7DtXCRAv0YnET5KroQOlmAhc1_HwW68EZniFw1YnB2dgDSxCkXnrfHYq7h63w0hjFXmgrdxeeAuOHBHnFFYHOWWjI8sLenPy_EBrgYIitXsAkLUGvZXlCjAWl-W459feNjHZ0SIsyTVwzAQtl5lmw1ht08z5Du-RiQahQE0sv89eimHVg9VSNOaTvw",
      "refresh_token_expires_in": 439200,
      "scope":"r_basicprofile"
    }
    

#### API Error Details

| HTTP STATUS CODE | ERROR MESSAGE | ERROR DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- |
| 400 | invalid\_request "The provided authorization grant or refresh token is invalid, expired or revoked" | Invalid or expired or revoked refresh token is sent as part of the request. | Refresh Token expired or revoked or invalid, hence reauthenticate the member to generate the new refresh token. |
| 400 | invalid\_request "A required parameter "redirect\_uri" is missing" | Redirect\_URI in the request is missing. It is mandatory parameter. | Pass the Redirect\_URI in the request to route user back to correct landing page. |
| 400 | invalid\_request "A required parameter "grant\_type" is missing" | Grant type in the request is missing. It is mandatory parameter. | Add grant\_type as "refresh\_token" in the request. |
| 400 | invalid\_request "A required parameter "client\_id" is missing" | Client ID in the request is missing. It is mandatory parameter. | Pass the client id of the app in request. |
| 400 | invalid\_request "A required parameter "refresh\_token" is missing" | Refresh Token in the request is missing. It is mandatory parameter. | Pass the stored Refresh Token received as part of initial access token call. |

Developer Portal Tools
======================

The LinkedIn Developer Portal Token Generator Tool allows a quick and easy method for generating an access token to make authenticated API calls.

Generate a Token in the Developer Portal
----------------------------------------

Once a token is generated, users are redirected to the token information page which includes details like OAuth scopes and token time to live (TTL) for reference during development activities.

1. Visit the [LinkedIn Developer Portal Token Generator](https://www.linkedin.com/developers/tools/oauth/token-generator) tool.
    
2. Select the app you'd like to generate a token for.
    
3. Select OAuth flow and permission scopes.
    
4. Member approval
    

The authenticated member will receive a request for your app to access to their profile.

5. Token Generation

Once the token is generated, the "Token Details" will be shown along with the token. Click "Copy token" to paste it into your application code.

Should you wish to verify this an existing token, the [Token Inspector tool](https://www.linkedin.com/developers/tools/oauth/token-inspector) is available on the same page as the token generator.

Developer Portal Token Inspector
--------------------------------

LinkedIn's Developer Portal has a token inspector tool to make token validation as simple as copy and paste. The same Token validation is available through the API or the UI. The [OAuth 2.0 token inspector](https://www.linkedin.com/developers/tools/oauth/token-inspector) is accessible from the developer portal under "Docs and Tools" in the navigation bar.

The tool requires you to select a developer application either from a dropdown or by entering the client ID if you have more than 10 developer applications. Make sure you have created at least one developer application or have been added as an Admin team member to a developer application before using the tool. You may only inspect tokens generated by the selected developer application.

The tool can also be used to generate a curl request to the token introspection endpoint. Simply paste a token in the text box, click "Inspect", and use the "Copy cUrl request" button.

Token Introspection
===================

Introduction
------------

The token inspector tool enables developers to check the Time to Live (TTL) and status (active/expired) for all tokens (including Enterprise tokens.) For [Authorization Code Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) (3-legged OAuth) tokens, permission scopes will be displayed. You can fetch access token data using the `/introspectToken` endpoint or the [Token Inspector Tool](https://www.linkedin.com/developers/tools/oauth/token-inspector) in the UI.

### API Details

    POST https://www.linkedin.com/oauth/v2/introspectToken
    
    Content-Type: application/x-www-form-urlencoded
    

#### Sample Request

* [http](#tabpanel_1_http)
* [curl](#tabpanel_1_curl)

    POST https://www.linkedin.com/oauth/v2/introspectToken
    

    curl --location --request POST 'https://www.linkedin.com/oauth/v2/introspectToken' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'client_id=<Application Client ID>' \
    --data-urlencode 'client_secret=<Application Client Secret>' \
    --data-urlencode 'token=<Token Value>'
    

#### Request Body

| Field | Type | Description |
| --- | --- | --- |
| client\_id | string | Required. Application client id |
| client\_secret | string | Required. Application client secret |
| token | string | Required. The string value of the token returned using [Client Credential Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow) (2-legged OAuth), [Authorization Code Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) (3-legged OAuth), or `Enterprise_User` (Enterprise OAuth Flow). |

#### Sample Response

    {
        "active": true,
        "client_id": "xxxxxxxx",
        "authorized_at": 1493055596,
        "created_at": 1493055596,
        "status": "active",
        "expires_at": 1497497620,
        "scope": "r_liteprofile,r_emailaddress,w_member_social",
        "auth_type": "_see note below_" 
    }
    

Note

Possible `auth-type` values returned are:  
"auth\_type": "2L"  
"auth\_type": "3L"  
"auth\_type": "Enterprise\_User"

#### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| active | boolean | Required. Boolean indicator of whether or not the returned token is currently active |
| status | string | Optional. An enum string with values:  <br>`revoked` - Token has been revoked  <br>`expired` - Token has expired due to the "expires\_at" TTL  <br>`active` - Token is active |
| scope | string | Optional. A string containing a comma-separated list of scopes associated with this token.  <br>Returned only for token obtained via [Authorization Code Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) (3-legged OAuth) |
| client\_id | string | Optional. Optional. Application Client ID |
| created\_at | long | Optional. Epoch time in seconds, indicating when this token was originally issued |
| expires\_at | long | Optional. Epoch time in seconds, indicating when this token will expire |
| authorized\_at | long | Optional. Epoch time in seconds, indicating when the token was authorized |
| auth\_type | string | Optional. String with values:  <br>`3L` - 3-legged member token  <br>`2L` - 2-legged application token  <br>`Enterprise_User` - Enterprise member token |

##### HTTP Response Status Codes

The response will vary depending on the status of the token and its authenticity.

| Status Code | Description |
| --- | --- |
| 200 | Success |
| 400 | Invalid `client id` or `token` |
| 401 | Invalid `client secret` |

Note

If the credentials are valid but do not match the client information in the token, you will receive a successful response (status 200 OK), however with `"active": false,` in the response body.

Concepts
========

LinkedIn's v2 REST APIs contain a number of concepts that help apply standard RESTful principles at scale, model data consistently, and ultimately provide a well-structured end-to-end developer experience.

    host: api.linkedin.com
    basePath: /v2
    scheme: https
    

Note

The `/V2` basePath is used for _most_ LinkedIn API calls.  
The [_authentication procedure_](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication) uses host: `www.linkedin.com`

* [Data Formats](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/data-formats?context=linkedin/context)
* [Decoration](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin/context)
* [Errors](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling?context=linkedin/context)
* [Methods](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods?context=linkedin/context)
* [Pagination](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/pagination?context=linkedin/context)
* [Projections](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/projections?context=linkedin/context)
* [Protocol Version](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/protocol-version?context=linkedin/context)
* [Rate Limits](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/rate-limits?context=linkedin/context)
* [URNs](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/urns?context=linkedin/context)

Data Formats
============

Input
-----

When you create or update existing entities, specify all input in JSON format and use the following HTTP Content Type:

`Content-Type: application/json`

XML input is not supported.

Output
------

The output is returned in JSON format as the following HTTP Content Type:

`Content-Type: application/json`

XML output is not supported.

Error Handling
==============

HTTP requests can fail for a variety of reasons. LinkedIn provides standard HTTP status codes and clear and concise messages to help you easily understand these errors.

#### Sample Response

    {
        "message": "Empty oauth2_access_token",
        "serviceErrorCode": 401,
        "status": 401
    }
    

Error responses have the following details:

* `message` - A description of the error.
* `serviceErrorCode` - A subcode that further classifies the error.
* `status` - The type of error (status code).

HTTP Status Codes and Error Types
---------------------------------

LinkedIn uses [standard HTTP status codes](https://tools.ietf.org/html/rfc2616#section-10) for each API’s response.

Status codes are divided into the following five categories:

* 1xx: Informational - Communicates transfer protocol-level information.
* 2xx: Success - The request was successful.
* 3xx: Redirection - The client must take some additional action to complete the request.
* 4xx: Client Error - Failed request due to client error.
* 5xx: Server Error - Failed request due to server error.

400 Bad Request
---------------

A `400 Bad Request` error means that the server was unable to proceed with the request. The most common cause of the error is bad syntax in the request URL or body. To fix a `400 Bad Request` error, do the following:

* Check if an invalid character is included in the [URL](https://www.w3.org/TR/url/#canonicalize-a-url).
* Check API examples.
* Ask your colleagues for help.
* Talk to the [rubber duck](https://en.wikipedia.org/wiki/Rubber_duck_debugging).

401 Unauthorized
----------------

`401 Unauthorized` errors are usually caused by a problem in the request header of your API call. For example, if you don't use a valid access token when you make an API call on behalf of a LinkedIn member, a `401 Unauthorized` error is returned. Some common cases are:

| Error Type | Fix |
| --- | --- |
| Unknown authentication schema | Unrecognized authentication header schema. Make sure the authentication header follows the format `Authorization: Bearer (your access token)` |
| Empty OAuth2 access token | The authentication header is missing or empty. Make sure the authentication header follows the format `Authorization: Bearer (your access token)` |
| Invalid access token | Incorrect access token, make sure you follow the [authentication procedure](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication) to get a correct access token. |
| Expired access token | The access token has expired, see [how to refresh your access token](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) |
| The token has been revoked | The access token has been revoked by the member from their privacy settings on LinkedIn’s website. To continue using your application, the member has to re-authenticate to get a new access token for your application. |

Note

Access token downstream verification failures return a [`500 Internal Server Error`](#500-internal-server-error).

403 Access Denied
-----------------

When your application makes an API call with a member’s access token, LinkedIn checks if the access token has permission to access the API. If the access token does not have the correct permissions, a `403 Access Denied` error is returned. When this happens, check the following:

* Does your application have permissions to make the API call?
* Does your application ask the user to enable these permissions?
* Did your application [change the scope](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin/context) while requesting an access token?  
    

If you continue to see the error, reach out to your partner technical support channel or [https://developer.linkedin.com/support](https://developer.linkedin.com/support).

404 Resource Not Found
----------------------

This error occurs when your application tries to call an API or fetch an entity that does not exist. For example, the API to get a friend’s profile is `/v2/people/id={personId}`, not `/v2/person/id={personId}`. In some cases (Ads, for example), a 404 error is returned when attempting to access a restricted API. See [403 Access Denied](#403-access-denied) and contact your partner technical support channel if you continue to see the error.

405 Method Not Allowed
----------------------

This error indicates that the HTTP protocol methods in your request are not supported. Check the documentation for the API to see supported methods.

411 Length Required
-------------------

This error indicates that the server refuses to accept the request without a defined `Content-Length` header. Please make sure POST requests with an empty body have a `Content-Length` header specified.

429 Rate Limit
--------------

On LinkedIn's platform, all API requests that you make are [rate limited](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/rate-limits?context=linkedin/context) to prevent abuse and to ensure service stability. These errors will return an error message of "Resource level throttle limit for calls to this resource is reached." If you get a `429 Rate Limit` error, check if too many redundant calls are being made and review your application’s Usage & Limits in the Developer Portal. If you've confirmed that the current rate limits do not meet your application’s needs, contact us if you are our partner, or join our partner program through [https://developer.linkedin.com/partner-programs](https://developer.linkedin.com/partner-programs).

In rare cases, LinkedIn may also return a 429 response as part of infrastructure protection. API service will return to normal automatically.

500 Internal Server Error
-------------------------

A `500 Internal Server Error` indicates that LinkedIn is experiencing an internal error. If you continue to receive server errors, record the following details and report it to your partner technical support channel or [https://developer.linkedin.com/support](https://developer.linkedin.com/support):

* Request: `url`, `method`, `header`. For example, `access_token`, `body`.
* Response: `header`. For example, `x-li-uuid`, `x-li-fabric`, `x-li-request-id`, `body`.
* Your application configuration. For example, Client ID.

504 Gateway Timeout
-------------------

A `504 Gateway Timeout` error happens when it takes too long for LinkedIn to process your API call. Due to the nature of cloud APIs, LinkedIn's services may be occasionally interrupted or temporarily unavailable for reasons outside of its control. Make sure you have proper error handling logic, such as caching and retry patterns, to cover these issues. If your application continues to receive these errors, contact [https://developer.linkedin.com/support](https://developer.linkedin.com/support) to report the issue.

Field Projections
=================

Field projection controls how much of an entity's data is displayed in response to an API request.

All APIs have a default set of field projections that control which fields are returned. If you don't need certain fields, you can decrease response time and payload size by using a projection to ask only for the fields your application is interested in.

By default, services may not always return all of the information that your application requests. In these cases, you'll need to use a projection to retrieve any non-default fields.

Field projections are defined using the `&fields=` query parameter and narrowed by providing a comma-separated list of field names that you want returned as the value of the parameter.

In the following example, a service returns these types of objects:

#### Sample Objects

    {
        "id" : int,      <- Default projection field
        "foo": string,   <- Default projection field
        "bar": boolean,
        "baz": Object
    }
    

A GET call to retrieve one of these objects provides the following response:

    GET https://api.linkedin.com/v2/sampleService/42
    

#### Sample Response

    {
        "foo": "Zing!",
        "id": 42
    }
    

Notice how the `bar` and `baz` fields were not returned in the response. This is because they are not part of the service's default field projection.

If you want to get `id`, `bar`, and `baz` back in the response (but not `foo`, because it's irrelevant to your application), use a field projection:

    GET https://api.linkedin.com/v2/sampleService/42?fields=id,bar,baz
    

#### Sample Response

    {
        "bar": true,
        "baz": {
            "beep": "Yay!",
            "bloop": "Meh",
            "blorp": "Boo!"
        },
        "id": 42
    }
    

Child Objects
-------------

In the above example, `baz` is returned in the response due to the field projection specified because `baz` is an object that has its own fields. Use field projections to select the data you need.

Use the `parentField:(child**Field_1,…,childField_n**)` syntax to select fields for a child object:

    GET https://api.linkedin.com/v2/sampleService/42?fields=id,baz:(beep)
    

#### Sample Response

    {
        "baz": {
            "beep": "Yay!"
        },
        "id": 42
    }
    

Parent Field as Map
-------------------

Objects can have nested objects with child fields of their own such as the example below:

#### Sample Data

    {
        "baz": {
            "1": {
                "beep": "Yay!",
                "foo": "foo1"
            },
            "2": {
                "beep": "Nay!",
                "foo": "foo2"
            }
        },
        "id": 42
    }
    

Use the `$*:(childField_1,…,childField_n)` syntax to control the fields requested from nested objects:

    GET https://api.linkedin.com/v2/sampleService/42?fields=id,baz:($*:(beep))
    

#### Sample Response

    {
        "baz": {
            "1": {
                "beep": "Yay!"
            },
            "2": {
                "beep": "Nay!"
            }
        },
        "id": 42
    }

Pagination
==========

API calls that return a large number of entities are broken up into multiple pages of results. You might need to make multiple API calls with slightly varied paging parameters to iteratively collect all the data you are trying to gather.

Use the following query parameters to paginate through results:

Parameters
----------

| Name | Description | Default |
| --- | --- | --- |
| start | The index of the first item you want results for. | 0   |
| count | The number of items you want included on each page of results. There could be fewer items remaining than the value you specify. | 10  |

To paginate through results, begin with a `start` value of 0 and a `count` value of N. To get the next page, set `start` value to N, while the `count` value stays the same. Subsequent pages start at 2N, 3N, 4N, and so on.

Samples
-------

#### Sample Request

    GET https://api.linkedin.com/v2/{service}
    

#### Sample Response

    "elements": [
        {"Result #0"},
        {"Result #1"},
        {"Result #2"},
        {"Result #3"},
        {"Result #4"},
        {"Result #5"},
        {"Result #6"},
        {"Result #7"},
        {"Result #8"},
        {"Result #9"}
    ],
    "paging": {
        "count": 10,
        "start": 0
    }
    

#### Sample Request

    GET https://api.linkedin.com/v2/{service}?start=10&count=10
    

#### Sample Response

    "elements": [
        {"Result #10"},
        {"Result #11"},
        {"Result #12"},
        {"Result #13"},
        {"Result #14"},
        {"Result #15"},
        {"Result #16"},
        {"Result #17"},
        {"Result #18"},
        {"Result #19"}
    ],
    "paging": {
        "count": 10,
        "start": 10
    }
    

### End of the Dataset

You have reached the end of the dataset when your response contains fewer elements in the `entities` block of the response than your `count` parameter request.

Protocol Versions
=================

LinkedIn V2 APIs support two protocol versions: 1.0 and 2.0. See the following syntax differences to help you migrate from 1.0 to 2.0.

LinkedIn plans to deprecate protocol version 1.0 in the near future. We strongly encourage developers to migrate as soon as possible and take advantage of the performance improvements in protocol version 2.0.

To use version 2.0, you must pass `X-Restli-Protocol-Version: 2.0.0` as the header in your API requests. If you don't pass a header, your call will default to version 1.0.

Single Resource Key
-------------------

When performing a GET, PARTIAL\_UPDATE, or DELETE on a resource, you must supply the resource key. See the following protocol version 1.0 example:

    GET https://api.linkedin.com/urn:li:endorsement:(urn:li:person:2qXA98-mVk,65761962366)
    

In protocol version 2.0, you must URL encode the entire resource key. The `(` must be encoded to `%28`, `)` to `%29`, `:` to `%3A` and `,` to `%2C`. See the following example:

    GET https://api.linkedin.com/v2/endorsement/urn%3Ali%3Aendorsement%3A%28urn%3Ali%3Aperson%3A2qXA98-mVk%2C65761962366%29
    

Note that special characters in a params string not part of a resource key should not be encoded. See the following example where parentheses are not encoded:

    GET https://api.linkedin.com/v2/ugcPosts?q=authors&authors=List(urn%3Ali%3Aorganization%3A12345)
    

In cases where only numeric ID are passed in as the primary resource key, nothing will change from 1.0 to 2.0. Some APIs require a compound or complex key. The following table lists the syntax differences:

| Key Type | Version 1.0 | Version 2.0 |
| --- | --- | --- |
| primitive key, long | 3   | 3   |
| primitive key, string | someString | someString |
| compound key with association | stringKey=string&longKey=5 | (stringKey:string,longKey:5) |
| complex key | $param.a=value&$param.b=value &keyPart1=value1&keyPart2=value2 | ($param:(a:value,b:value), keyPart1:value1,keyPart2=value2) |

Multiple Resource Keys
----------------------

To perform a `BATCH_GET` in protocol version 1.0:

    GET https://api.linkedin.com/people?ids=1&ids=2&ids=3
    

In protocol version 2.0, you must change this query to a `List` syntax:

    GET https://api.linkedin.com/v2/people?ids=List(1,2,3,4)
    

Complex Keys
------------

In protocol version 1.0, if a resource has complex keys:

    GET https://api.linkedin.com/people?ids[0].$params.a=value0A&ids[0].$params.b=value0B&ids[1].$params.a=value1A&ids[1].$params.b=value1B&ids[2].$params.a=value2A&ids[2].$params.b=value2B
    

In protocol version 2.0, if a resource has complex keys:

    GET https://api.linkedin.com/people?ids=List(($params.a:value0A,$params.b:value0B),($params.a:value1A,$params.b:value1B),($params.a:value2A,$params.b:value2B))
    

Note

The values and the resource parameters must be URL encoded but not the `,` grouping the fields and values. The single resource key had the `,` encoded because it was part of the whole value.

Parameters
----------

When performing a `FINDER` in version 1.0, you often have query parameters such as filters represented as an array:

    GET https://api.linkedin.com/resource?q=FinderParam&param.aList[0]=foo&param.aList[1]=bar&param.aList[2]=baz& param.anObject.aField=1&param.anObject.anotherField=value
    

In protocol version 2.0, you must change this query to a `List` syntax, much like the multiple keys:

    GET https://api.linkedin.com/resource?q=myFinder&param=(aList:List(foo,bar,baz),anObject:(aField:1,anotherField:value))
    

Note

The values and the resource parameters must be URL encoded but not the `,` grouping the fields and values. The single resource key had the `,` encoded because it was part of the whole value.

Query Tunneling
===============

To improve our network infrastructure and better serve API traffic globally, LinkedIn will begin rejecting API calls not meeting new criteria.

Note

For more information about API specific examples, see our [_Migration Guide_](https://learn.microsoft.com/en-us/linkedin/shared/references/migrations/query-tunneling-migration).

Requirements
------------

Ensure your LinkedIn API requests comply with the following size requirements. If your request exceeds any of the size requirements listed below, your request will receive a 414 response.

| Request parameter | Size in KB |
| --- | --- |
| Raw URL | 8 KB max length (scheme + hostname + port + path + query string of the URL) |
| Query String | 4 KB max length |
| Request URL | 28 KB max length (headers + cookies + URI + queryString, but excluding POST data) |
| URL path segment | 4 KB max characters (the area between slashes in a URL) |

Query Tunneling
---------------

To support these requirements, we’re introducing the concept of query tunneling. This feature allows you to modify your existing requests with a custom header to easily resolve offending requests.

### Requests without Body

1. Change the request from `GET` to `POST`.
2. Add the `X-HTTP-Method-Override` header, using the original HTTP method (-H "X-HTTP-Method-Override: GET").
3. Add the `Content-Type` header (-H "Content-Type: application/x-www-form-urlencoded").
4. Move the query string to the body of the request.

#### Example

Let’s use the example request below to see how we can quickly convert our existing request to the organizationalEntityAcls API using query tunneling.

##### Current Request

    curl -X GET 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
    -H 'Authorization: Bearer redacted'
    

1. Change the request type from GET to POST.

    curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
    -H 'Authorization: Bearer redacted'
    

2. Add the method override header and append the original GET request type.

    curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
    -H 'X-HTTP-Method-Override: GET'
    -H 'Authorization: Bearer redacted'
    

3. Add the `Content-Type` header.

    curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
    -H 'X-HTTP-Method-Override: GET'
    -H 'Content-Type: application/x-www-form-urlencoded'
    -H 'Authorization: Bearer redacted'
    

4. Move the query string of the request URL to the request body.

    curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls' \
    -H 'X-HTTP-Method-Override: GET'
    -H 'Content-Type: application/x-www-form-urlencoded' 
    -H 'Authorization: Bearer redacted'
    --data 'q=roleAssignee&projection=(elements*(organizationalTarget~))'
    

### Requests with Body

1. Change the request type from PUT to POST if the original request type was PUT. If the original request type was POST, keep it as POST.
2. Add the X-HTTP-Method-Override header using the original HTTP method `-H 'X-HTTP-Method-Override: POST'` for POSTs or `-H 'X-HTTP-Method-Override: PUT'` for PUTs.
3. Add the Content-Type header `-H 'Content-Type: multipart/mixed; boundary=xyz'`. Note that here we need to specify a boundary delimiter (here we use `xyz` for illustration) for multipart body, this delimiter needs to be unique and not appearing in your request content body or url.
4. Move the query string and original request body to body as two sections explained above.

#### Example

Let’s use the example request below to see how we can quickly convert our existing request to the adCreativesV2 API using query tunneling.

###### Current Request

    curl -X POST 'https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196)' \
    -H 'Authorization: Bearer redacted' \
    -H 'Content-Type: application/json' \
    -H 'X-Restli-Protocol-Version: 2.0.0' \
    -H 'X-RestLi-Method:  BATCH_PARTIAL_UPDATE' \
    --data '{"entities": {"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}'
    

1. Change the request type from PUT to POST if the original request type was PUT. If the original request type was POST, keep it as POST.

    curl -X POST https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196) \
      -H 'Authorization: Bearer redacted' \
      -H 'X-RestLi-Method: BATCH_PARTIAL_UPDATE' \
      -H 'X-RestLi-Protocol-Version: 2.0.0' \
      --data ${"entities": {{"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}}'
    

2. Add the X-HTTP-Method-Override header using the original HTTP method `-H 'X-HTTP-Method-Override: POST'` for POSTs or `-H 'X-HTTP-Method-Override: PUT'` for PUTs.

    curl -X POST https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196) \
      -H 'X-HTTP-Method-Override: POST' \
      -H 'Authorization: Bearer redacted' \
      -H 'X-RestLi-Method: BATCH_PARTIAL_UPDATE' \
      -H 'X-RestLi-Protocol-Version: 2.0.0' \
      --data ${"entities": {{"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}}'
    

3. Add the Content-Type header `-H 'Content-Type: multipart/mixed; boundary=xyz'`.

    curl -X POST https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196) \
      -H 'X-HTTP-Method-Override: POST' \
      -H 'Content-Type: multipart/mixed; boundary=xyz' \
      -H 'Authorization: Bearer redacted' \
      -H 'X-RestLi-Method: BATCH_PARTIAL_UPDATE' \
      -H 'X-RestLi-Protocol-Version: 2.0.0' \
      --data ${"entities": {{"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}}'
    

4. Move the query string and original request body to body as two sections.

    curl -X POST https://api.linkedin.com/v2/adCreativesV2 \
      -H 'X-HTTP-Method-Override: POST' \
      -H 'Content-Type: multipart/mixed; boundary=xyz' \
      -H 'Authorization: Bearer redacted' \
      -H 'X-Restli-Protocol-Version: 2.0.0' \
      -H 'X-RestLi-Method:  BATCH_PARTIAL_UPDATE' \
      --data $'--xyz\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\nids=List(47770196)\r\n--xyz\r\n 
             Content-Type: application/json\r\n\r\n{"entities": {"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}\r\n--xyz--'

Rate Limiting
=============

To prevent abuse and ensure service stability, all API requests are rate limited. Rate limits specify the maximum number of API calls that can be made in a 24 hour period. These limits reset at midnight [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) every day.

There are two kinds of limits that affect your application:

* **Application** — The total number of calls that your application can make in a day.
* **Member** — The total number of calls that a single member per application can make in a day.

Note

The term `Member` refers to a LinkedIn user whose token is used to initiate API calls from the developer application. For example, a partner is responsible for managing multiple members. This member-level designation indicates the permissible number of API calls the partner can initiate from their application on behalf of a member token.

Rate limited requests will receive a 429 response. In rare cases, LinkedIn may also return a 429 response as part of infrastructure protection. API service will return to normal automatically.

Your application's daily rate limit varies based on which API endpoint you are using. Standard rate limits are not published in documentation. You can look up the rate limit of any endpoint your app has access to through the [Developer Portal](https://www.linkedin.com/developers/apps). Select your app from the list and navigate to its Analytics tab. This page will only show usage and rate limits for endpoints you have made at least 1 request to today(UTC). If you want to look up a rate limit for an endpoint not listed in your app's Analytics page, make 1 test call to that endpoint and refresh the Analytics page.

Request Methods
===============

LinkedIn's APIs have an expressive set of methods for interacting.

GET
---

The GET method requests a single, specific entity/object from a service. This method leverages the traditional HTTP GET method.

    GET https://api.linkedin.com/v2/{service}/{resourceIdentifier}
    

GET\_ALL
--------

The GET\_ALL method requests all entities/objects from a service. GET\_ALL requests never provide resource identifiers to a service. This method uses the traditional HTTP GET method.

    GET https://api.linkedin.com/v2/{service}
    

BATCH\_GET
----------

The BATCH\_GET method requests more than one specific entity/object from a service. This method uses the traditional HTTP GET method.

    GET https://api.linkedin.com/v2/{service}?ids=List(resourceIdentifier_1,...,resourceIdentifier_n)
    

FINDER {finderName}
-------------------

Conceptually, FINDER methods are similar to GET/BATCH\_GET calls. The main difference between these methods is that you use FINDER queries when you don't have an identifier to directly retrieve an entity. These methods use the HTTP GET method with a `q={finderName}` request parameter which identifies the type of query being made. FINDER methods can return zero, one, or more results, depending on the number of entities that match the query input.

    GET https://api.linkedin.com/v2/{service}?q={finderName}
    

CREATE
------

The CREATE method indicates to a service that it should use the information provided in the request body to create a new entity. This method uses the traditional HTTP POST method.

    POST https://api.linkedin.com/v2/{service}/{Request Body}
    

BATCH\_CREATE
-------------

The BATCH\_CREATE method indicates to a service that it should use the information provided in the request body to create multiple new entities. This method uses the traditional HTTP POST method.

    POST https://api.linkedin.com/v2/{service}/{Request Body}
    

UPDATE
------

The UPDATE method indicates to a service that it should use the information provided in the request body to overwrite the entire definition of an existing entity. This method uses the traditional HTTP PUT method.

    PUT https://api.linkedin.com/v2/{service}/{Request Body}
    

BATCH\_UPDATE
-------------

The BATCH\_UPDATE method indicates to a service that it should use the information provided in the request body to overwrite the entire definitions of multiple existing entities. This method uses the traditional HTTP `PUT` method.

    PUT https://api.linkedin.com/v2/{service}/{Request Body}
    

PARTIAL\_UPDATE
---------------

The PARTIAL\_UPDATE method indicates to a service that it should use the information provided in the request body to update only specific portions of an existing entity rather than overwriting the entire definition of the entity. This method uses the traditional HTTP POST method.

Note

For the server to differentiate between a PARTIAL\_UPDATE and an UPDATE, you must include `X-Restli-Method: PARTIAL_UPDATE` as the header value in your request.

    POST https://api.linkedin.com/v2/{service}/{Request Body}
    

BATCH\_PARTIAL\_UPDATE
----------------------

The BATCH\_PARTIAL\_UPDATE method indicates to a service that it should use the multiple pieces of information provided in the request body to update specific portions of multiple specified entities, rather than overwriting them entirely. This method uses the traditional HTTP POST method.

Note

For the server to differentiate between a `BATCH_PARTIAL_UPDATE` and a `BATCH_UPDATE`, you must include `X-Restli-Method: BATCH_PARTIAL_UPDATE` as the header value in your request.

    POST https://api.linkedin.com/v2/{service}/{Request Body}
    

DELETE
------

The DELETE method indicates to a service that it should delete an identified object/entity. This method uses the traditional HTTP DELETE method.

    DELETE https://api.linkedin.com/v2/{service}/{resourceIdentifier}
    

BATCH\_DELETE
-------------

The BATCH\_DELETE method indicates to a service that it should delete multiple identified objects/entities. This method uses the traditional HTTP DELETE method.

    DELETE https://api.linkedin.com/v2/{service}?ids=List({resourceIdentifier_1},...,{resourceIdentifier_n})
    

BATCH\_FINDER {finderName}
--------------------------

Conceptually, BATCH\_FINDER methods are similar to BATCH\_GET calls. The main difference between these methods is that you use BATCH\_FINDER queries when you don't have identifiers to directly retrieve entities. These methods use the HTTP GET method with a bq={batchFinderName} request parameter which identifies the type of query being made. BATCH\_FINDER methods accept a list of filters set. Instead of calling multiple finders with different filter values, we call one BATCH\_FINDER method with a list of filters. BATCH\_FINDER methods can return zero, one, or more results, depending on the number of entities that match the query input.

    GET https://api.linkedin.com/v2/{service}?bq={batchFinderName}
    

ACTION {actionName}
-------------------

The ACTION method is a flexible method that does not specify any type of standard behavior. It uses the HTTP POST method, with a special `action={actionName}` request parameter, which identifies the specific type of action to take.

    POST https://api.linkedin.com/v2/{service}?action={actionName}

Response Decoration
===================

Warning

**Deprecation Notice**  
The use of Response Decoration is deprecated in some versions of LMS APIs. Please refer the [Recent Changes](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/recent-changes) page for information on the specific API versions that are affected by this deprecation.

When you call an API, the response may contain [URNs](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/urns?context=linkedin/context) referencing the different types of objects provided by LinkedIn's services. These URNs are valuable on their own; however, there may be instances when you want to expand a URN and access the values associated with the entity.

Decoration is a mechanism in LinkedIn's APIs to fetch data belonging to a URN object without having to make an extra call to that object's API. Decoration uses a syntax very similar to LinkedIn's [Field Projections](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/projections?context=linkedin/context).

See the following example of a service that returns URN references to another type of entity:

#### Sample Request

    GET https://api.linkedin.com/v2/{service}/1234
    

#### Sample Response

    {
        "id": 1234,
        "relatedEntity": "urn:li:relatedEntity:6789"
    }
    

Rather than taking the `relatedEntity` URN value and making a second GET call to its parent service, you can use decoration to define how you'd like the `relatedEntity` object to be expanded within the original API request. To do this, append the `~` character to the entity you wish to expand, and then provide the field projection in parentheses afterwards. For example:

#### Sample Request

    GET https://api.linkedin.com/v2/{service}/1234&projection=(id,relatedEntity~($URN,foo,bar))
    

#### Sample Response

    {
        "id": 1234,
        "relatedEntity": {
            "$URN": "urn:li:relatedEntity:6789",
            "bar": "bloop",
            "foo": "bleep"
        }
    }
    

Decorating within Arrays/Lists
------------------------------

In some circumstances, a service might return a collection of URNs that are not all of the same type. In this case, provide multiple decoration instructions to tell the service how to deal with any potential URN type that is returned. See the following sample request and the list of different URN types that it returns within entities:

#### Sample Request

    GET https://api.linkedin.com/v2/{service}/1234
    

#### Sample Data

    {
        "entities": [
            "urn:li:foo:123",
            "urn:li:bar:234",
            "urn:li:baz:345"
        ],
        "id": 1234
    }
    

To decorate each of the `foo`, `bar`, and `baz` URN types in this response, use the following projection syntax in your request:

#### Sample Request

    GET https://api.linkedin.com/v2/{service}/1234?projection=entities*~foo(a,b)~bar(c,d)~baz(e,f))
    

#### Sample Response

    {
        "entities": [
            {
                "a": 1,
                "b": 2
            },
            {
                "c": 10,
                "d": 20
            },
            {
                "e": 100,
                "f": 200
            }
        ],
        "id": 1234
    }
    

Sample Projections
------------------

Consider the following data model of a sample resource and review the below samples showing how to access various parts of this data in order to decorate.

    {
        "person": {
            "current_position": {
                "company": "urn:li:company:1",
                "from": "2009",
                "job_title": "SWE"
            },
            "firstname": "First Name",
            "following_companies": [
                "urn:li:company:1",
                "urn:li:company:2"
            ],
            "lastname": "Last Name",
            "messages": {
                "urn:li:message:1": {
                    "bcc": [
                        "urn:li:person:1",
                        "urn:li:person:39"
                    ],
                    "content": "xyz",
                    "from": "urn:li:person:99"
                },
                "urn:li:message:2": {
                    "bcc": [
                        "urn:li:person:1",
                        "urn:li:person:80"
                    ],
                    "content": "abc",
                    "count": 1929
                }
            },
            "phone": "200-100-200",
            "position_history": [
                {
                    "company": "urn:li:company:4888383",
                    "from": "2006",
                    "job_title": "SSE",
                    "to": "2009"
                },
                {
                    "company": "urn:li:company:39939",
                    "from": "1999",
                    "job_title": "SE",
                    "to": "2006"
                }
            ]
        }
    }
    

Accessing URN within a child object
-----------------------------------

**`(person(current_position(company)))`**

    {
        "person": {
            "current_position": {
                "company": "urn:li:company:1"
            }
        }
    }
    

Accessing URNs within an array of child objects
-----------------------------------------------

**`(person(position_history(*(company))))`**

    {
        "person": {
            "position_history": [
                {
                    "company": "urn:li:company:4888383"
                },
                {
                    "company": "urn:li:company:39939"
                }
            ]
        }
    }
    

Accessing URNs within an array of URNs
--------------------------------------

**`(person(following_companies(*)))`**

    {
        "person": {
            "following_companies": [
                "urn:li:company:1",
                "urn:li:company:2"
            ]
        }
    }
    

Selecting a single child field with a URN and expanding the URN
---------------------------------------------------------------

**`(person(current_position(company~)))`**

    {
        "person": {
            "current_position": {
                "company": "urn:li:company:1",
                "company~": {
                    "active": true,
                    "administrators": [
                        "urn:li:person:6611647"
                    ],
                    "allEmployeesAsAdmins": false,
                    "attributes": {
                        "disableThirdPartyNews": false,
                        "enableStatusUpdate": false,
                        "owns300x250RightAdSlot": false,
                        "paidCareers": false,
                        "paidGoldPlusCareers": false,
                        "paidPlatinumCareers": false,
                        "paidProducts": false,
                        "paidSilverCareers": false,
                        "paidSilverPlusCareers": false,
                        "showAnalytics": false,
                        "showBrandTree": false,
                        "showNews": true,
                        "showPastEmployees": false,
                        "silverProducts": false,
                        "useParentCareers": false
                    },
                    "companyId": 1,
                    "companyType": "PUBLIC_COMPANY",
                    "creationTime": 1375816467585,
                    "creator": "urn:li:person:6611647",
                    "dataVersion": 4,
                    "descriptions": [
                        {
                            "description": "test test test testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest test",
                            "locale": "en_US"
                        }
                    ],
                    "employeeCountRange": "MYSELF_ONLY",
                    "heroImage": {
                        "cropHeight": 220,
                        "cropWidth": 646,
                        "cropXPosition": 0,
                        "cropYPosition": 0,
                        "croppedImage": "urn:li:media:/p/2/005/045/187/3d49ef0.png",
                        "height": 220,
                        "uncroppedImage": "urn:li:media:/p/2/005/045/187/3b333d8.png",
                        "width": 646
                    },
                    "images": [
                        {
                            "originalMedia": "urn:li:media:/p/2/005/045/188/1d5f329.png",
                            "type": "SQUARE_LOGO_LEGACY",
                            "urn": "urn:li:media:/p/2/005/045/188/1d5f329.png"
                        },
                        {
                            "originalMedia": "urn:li:media:/p/2/005/045/188/24809b3.png",
                            "type": "LOGO_LEGACY",
                            "urn": "urn:li:media:/p/2/005/045/188/24809b3.png"
                        }
                    ],
                    "industries": [
                        "ACCOUNTING"
                    ],
                    "lastEditor": "urn:li:person:6611647",
                    "lastModifiedTime": 1375816467585,
                    "logo": "urn:li:media:/p/2/005/045/188/24809b3.png",
                    "names": [
                        {
                            "active": true,
                            "locale": "en_US",
                            "name": "r-NQkR5TwJ",
                            "type": "CANONICAL"
                        }
                    ],
                    "organizationalEntity": "urn:li:organization:1",
                    "squareLogo": "urn:li:media:/p/2/005/045/188/1d5f329.png",
                    "status": "OPERATING",
                    "stockSymbol": "",
                    "twitterId": "",
                    "universalName": "r-nqkr5twj",
                    "websiteUrl": "https://www.whatismyreferer.com/"
                }
            }
        }
    }
    

Selecting all child fields and fully expanding a child field containing a URN
-----------------------------------------------------------------------------

**`(person(current_position(*,company~)))`**

    {
        "person": {
            "current_position": {
                "company": "urn:li:company:1",
                "company~": {
                    "active": true,
                    "administrators": [
                        "urn:li:person:6611647"
                    ],
                    "allEmployeesAsAdmins": false,
                    "attributes": {
                        "disableThirdPartyNews": false,
                        "enableStatusUpdate": false,
                        "owns300x250RightAdSlot": false,
                        "paidCareers": false,
                        "paidGoldPlusCareers": false,
                        "paidPlatinumCareers": false,
                        "paidProducts": false,
                        "paidSilverCareers": false,
                        "paidSilverPlusCareers": false,
                        "showAnalytics": false,
                        "showBrandTree": false,
                        "showNews": true,
                        "showPastEmployees": false,
                        "silverProducts": false,
                        "useParentCareers": false
                    },
                    "companyId": 1,
                    "companyType": "PUBLIC_COMPANY",
                    "creationTime": 1375816467585,
                    "creator": "urn:li:person:6611647",
                    "dataVersion": 4,
                    "descriptions": [
                        {
                            "description": "test test test testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest test",
                            "locale": "en_US"
                        }
                    ],
                    "employeeCountRange": "MYSELF_ONLY",
                    "heroImage": {
                        "cropHeight": 220,
                        "cropWidth": 646,
                        "cropXPosition": 0,
                        "cropYPosition": 0,
                        "croppedImage": "urn:li:media:/p/2/005/045/187/3d49ef0.png",
                        "height": 220,
                        "uncroppedImage": "urn:li:media:/p/2/005/045/187/3b333d8.png",
                        "width": 646
                    },
                    "images": [
                        {
                            "originalMedia": "urn:li:media:/p/2/005/045/188/1d5f329.png",
                            "type": "SQUARE_LOGO_LEGACY",
                            "urn": "urn:li:media:/p/2/005/045/188/1d5f329.png"
                        },
                        {
                            "originalMedia": "urn:li:media:/p/2/005/045/188/24809b3.png",
                            "type": "LOGO_LEGACY",
                            "urn": "urn:li:media:/p/2/005/045/188/24809b3.png"
                        }
                    ],
                    "industries": [
                        "ACCOUNTING"
                    ],
                    "lastEditor": "urn:li:person:6611647",
                    "lastModifiedTime": 1375816467585,
                    "logo": "urn:li:media:/p/2/005/045/188/24809b3.png",
                    "names": [
                        {
                            "active": true,
                            "locale": "en_US",
                            "name": "r-NQkR5TwJ",
                            "type": "CANONICAL"
                        }
                    ],
                    "organizationalEntity": "urn:li:organization:1",
                    "squareLogo": "urn:li:media:/p/2/005/045/188/1d5f329.png",
                    "status": "OPERATING",
                    "stockSymbol": "",
                    "twitterId": "",
                    "universalName": "r-nqkr5twj",
                    "websiteUrl": "https://www.whatismyreferer.com/"
                },
                "from": "2009",
                "job_title": "SWE"
            }
        }
    }
    

Selecting all child fields and expanding child field with a URN for a single value
----------------------------------------------------------------------------------

**`(person(current_position(*,company~(vanityName))))`**

    {
        "person": {
            "current_position": {
                "company": "urn:li:company:1",
                "company~": {},
                "from": "2009",
                "job_title": "SWE"
            }
        }
    }
    

Accessing complex type object
-----------------------------

When a URN is a field’s key and the value is an object, it is called a complex type object. In the following example, the `messages` field maps to an object with 2 fields that are `MessageUrns`. These 2 `MessageUrns` are keys that map to objects containing data such as `bcc`,`count`, and `content`. To access the `bcc` values for each `MessageUrn`, use the decoration `(person(messages()))(person(messages(*(from,bcc(*)))))`.

**`(person(messages()))`**

    {
        "person": {
            "messages": {
                "urn:li:message:1": {
                    "bcc": [
                        "urn:li:personr:1",
                        "urn:li:person:39"
                    ],
                    "content": "xyz",
                    "from": "urn:li:person:99"
                },
                "urn:li:message:2": {
                    "bcc": [
                        "urn:li:person:1",
                        "urn:li:person:80"
                    ],
                    "content": "abc",
                    "count": 1929
                }
            }
        }
    }
    

**`(person(messages(*(from,bcc(*)))))`**

    {
        "person": {
            "messages": {
                "urn:li:message:1": {
                    "bcc": [
                        "urn:li:person:1",
                        "urn:li:person:39"
                    ],
                    "from": "urn:li:person:99"
                },
                "urn:li:message:2": {
                    "bcc": [
                        "urn:li:person:1",
                        "urn:li:person:80"
                    ]
                }
            }
        }
    }
    

Accessing all URNs within any array from a BATCH\_GET call
----------------------------------------------------------

Note that a BATCH\_GET call returns a `results` field by default.

**`(results(*(person(following_companies(*)))))`**

#### Sample Data

    {
        "results": {
            "123123": {
                "person": {
                    "current_position": {
                        "company": "urn:li:company:1",
                        "from": "2009",
                        "job_title": "SWE"
                    },
                    "firstname": "First Name",
                    "following_companies": [
                        "urn:li:company:1",
                        "urn:li:company:2"
                    ],
                    "lastname": "Last Name",
                    "messages": {
                        "urn:li:message:1": {
                            "bcc": [
                                "urn:li:person:1",
                                "urn:li:person:39"
                            ],
                            "content": "xyz",
                            "from": "urn:li:person:99"
                        },
                        "urn:li:message:2": {
                            "bcc": [
                                "urn:li:person:1",
                                "urn:li:person:80"
                            ],
                            "content": "abc",
                            "count": 1929
                        }
                    },
                    "phone": "200-100-200",
                    "position_history": [
                        {
                            "company": "urn:li:company:4888383",
                            "from": "2006",
                            "job_title": "SSE",
                            "to": "2009"
                        },
                        {
                            "company": "urn:li:company:39939",
                            "from": "1999",
                            "job_title": "SE",
                            "to": "2006"
                        }
                    ]
                }
            }
        }
    }
    

**`(results(*(person(following_companies(*)))))`**

    {
        "results": {
            "123123": {
                "person": {
                    "following_companies": [
                        "urn:li:company:1",
                        "urn:li:company:2"
                    ]
                }
            }
        }
    }
    

Note

Always use `entity~` in the projection parameter to make the expansion request. If the `entity` is expanded, the response returns `entity~`. If for some reason the `entity` cannot be expanded, the response returns `entity!`.

Rate Limiting
-------------

Response decoration makes calls to other services in order to resolve the requested, decorated entity. These calls are subject to rate limiting. It is possible for calls to return a 200 while the decoration call is rate limited.

The following example makes a request to the `/me` endpoint and uses response decoration to resolve the `digitalMediaAsset` URN in the `displayImage` field. The call to the `/me` endpoint is successful, but the decoration call to resolve `displayImage` is rate limited.

    GET https://api.linkedin.com/v2/me?projection=(id,profilePicture(displayImage~(*)))
    

    {
        "profilePicture": {
            "displayImage!": {
                "serviceErrorCode": 101,
                "message": "Resource level throttle limit for calls to this resource is reached.",
                "status": 429
            },
            "displayImage": "urn:li:digitalmediaAsset:C4D03AQGFBHiaY1XXNA"
        },
        "id": "z6_nnTIGu-"
    }

URNs and IDs
============

URNs
----

[URNs](http://www.ietf.org/rfc/rfc2141.txt) are used to represent foreign associations to an entity (persons, organizations, and so on) in an API. A URN is a string-based identifier with the format:

`urn:{namespace}:{entityType}:{id}`

For example:

* `urn:li:person:123`
* `urn:li:organization:456`
* `urn:li:sponsoredAccount:789`

URNs encode more information, including the entity type. Using the entity type, it's possible to dereference a URN and access the underlying data of the entity using a process called [decoration](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin/context).

URN values returned from LinkedIn's APIs are a maximum of 255 characters in length.

IDs
---

Simple integer IDs are returned to represent an object's primary key. Your application should support transforming URNs into IDs and vice versa.

IDs versus URNs
---------------

IDs are self-referencing identifiers similar to a primary key. URNs are Globally Unique Identifiers (GUID) used to represent an entity's foreign associations.

In the example below, we fetch details about a share and use a [projection](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/projections?context=linkedin/context) to limit the results to the `id` and `owner` fields. The `shares` API returns an `id` that is the primary key and an `owner` that is a foreign reference to the person who created the share in the form of a `URN`.

| Resource Type | URN | ID  |
| --- | --- | --- |
| Share | `urn:li:share:1234` | 1234 |
| Person | `urn:li:person:-f_Ut43FoQ` | \-f\_Ut43FoQ |

#### Sample Request

    GET https://api.linkedin.com/v2/shares/1234?projection=(id,owner)
    

    {
        "id": "1234",
        "owner": "urn:li:person:-f_Ut43FoQ"
    }
    

URN Deconstruction
------------------

To get more information about the owner of the share, we can deconstruct the URN by removing the `urn:li:person` prefix and making an additional call to the `people` API. We need to deconstruct the URN and parse the ID because the `people` API expects an ID.

#### Sample Request

    GET https://api.linkedin.com/v2/people/id=-f_Ut43FoQ?projection=(id,localizedFirstName,localizedLastName)
    

    {
        "id": "-f_Ut43FoQ",
        "localizedFirstName": "Dwight",
        "localizedLastName": "Schrute"
    }
    

URN Decoration
--------------

To make this query more efficient, we can use [decoration](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/decoration?context=linkedin/context) to expand the share owner URN and return the owner's first and last name in a single call. This saves an API call by not having to make a separate call to the `people` API.

#### Sample Request

    GET https://api.linkedin.com/v2/shares/1234?projection=(id,owner~(localizedFirstName,localizedLastName))
    

    {
        "id": "1234",
        "owner": "urn:li:person:-f_Ut43FoQ",
        "owner~": {
            "localizedFirstName": "Schrute",
            "localizedLastName": "Dwight"
        }
    }
    

URNs and Namespaces
-------------------

For common URNs and their namespace conversions, see [URN Namespaces](https://learn.microsoft.com/en-us/linkedin/shared/references/v2/urn-namespace?context=linkedin/context).

Webhooks
========

Webhooks allow you to receive real-time HTTP notifications for subscribed events. This functionality is only available for applications with an approved use case for webhooks.

Webhook Registration and Validation
-----------------------------------

Notifications will only be sent to webhooks that are registered and validated.

To begin, register your webhook in the "Webhooks" tab of your application in the [developer portal](https://www.linkedin.com/developers/apps).

Note

The Webhooks tab is only enabled for applications with a use case for webhooks. For Lead Syncing use cases, webhook subscriptions must be created via the Lead Notification Subscriptions API and cannot be created via the UI.

### Fields

| Field Name | Description | Required |
| --- | --- | --- |
| applicationId | ID of the Developer Application being validated. Only sent for integrations with parent-child applications such as [Apply Connect](https://learn.microsoft.com/en-us/linkedin/talent/apply-connect). Indicates which application's `clientSecret` to use for generating the challenge response. | False |
| challengeCode | Randomly generated type-4 UUID string created by LinkedIn. | True |
| challengeResponse | Hex-encoded HMACSHA256 signature for the `challengeCode` using its `clientSecret` as the secret key. `challengeResponse = Hex-encoded(HMACSHA256(challengeCode, clientSecret))` | True |

### Validating the Webhook Endpoint

LinkedIn validates the ownership of a webhook URL before it can be registered by an application. The validation flow leverages the application's `clientSecret` as the secret key along with the universally-known HMACSHA256 algorithm to generate and validate the application's response to a challenge code.

1. Before initiating the validation flow, LinkedIn will generate a string that will act as the `challengeCode`.
2. LinkedIn will use the `challengeCode` as a query parameter to make an HTTP GET to your webhook endpoint. Integrations using parent-child applications will also receive an `applicationId` query parameter.

    GET https://webhooks.example.com/linkedin?challengeCode=890e4665-4dfe-4ab1-b689-ed553bceeed0
    

3. Your application must compute the challengeResponse (Hex-encoded HMACSHA256 signature for the challengeCode) using its clientSecret as the secret key. If you received an applicationId query parameter in the previous step, use the clientSecret associated with the challenged application. Return both the challengeCode and challengeResponse in a JSON payload with a 200 OK status within 3 seconds. See the example below. The response should have header "content-type" value set to "application/json".

    challengeResponse = Hex-encoded(HMACSHA256(challengeCode, clientSecret))
    

    {
     "challengeCode" : "890e4665-4dfe-4ab1-b689-ed553bceeed0",
     "challengeResponse" : "27b1d19678542072a7f1d0ce845d0c78cec22567f413697e25648f44fa3d1514"
    }
    

4. On receiving the validation response, LinkedIn will verify by computing the challenge response and comparing it with the `challengeResponse` returned by the app.
5. If the `challengeResponse` is successfully verified, then the webhook is ready to be used in subscriptions. If the verification fails, an error will be thrown with the message: `This URL did not pass the security challenge check`.

### Re-validation and Blocked Endpoints

Webhook endpoints will be periodically re-validated after the initial validation every 2 hours. If the re-validation check fails 3 times in a row, the endpoint will move to a blocked state where events will no longer be sent.

Developers associated with that developer application will receive warning emails for any failed validation attempts. After re-validation checks fail 3 times in a row, an email will be sent notifying developers that the webhook has been blocked. The endpoint will also show as "Blocked" in the developer portal.

After resolving the issue, developers can manually kick off another validation check from the developer portal.

Requirements for Processing Notifications
-----------------------------------------

Upon receiving notifications from LinkedIn, your webhook must fulfill the following requirements:

#### Verify the integrity of the push event and prevent malicious entities from impersonating LinkedIn as the sender

The POST request sent by LinkedIn will include a header called `X-LI-Signature`. The value of this header is the HMACSHA256 hash of the JSON-encoded string representation of the POST body prefixed by `hmacsha256=` and it is computed using your app’s clientSecret. On receiving the push event, you must compute the signature on the POST body prefixed by `hmacsha256=` using the HMACSHA256 hashing algorithm and your clientSecret. Discard the event if your computed value does not match the value sent in the `X-LI-Signature` header.

#### Deduplicate notifications

A notification can occasionally be delivered multiple times to your webhook. Your webhook must be able to deduplicate notifications using the Notification ID included in the payload.

#### Respond with an HTTP response

For each notification delivered to your webhook, it must return a 2xx HTTP status code to indicate successful delivery of the notification to your webhook. Any other response code returned will be treated by LinkedIn as a failure.

#### Test with lambda/serverless functions on a cloud provider

We recommend testing webhooks processing using lambda/serverless functions on a cloud provider.

Note

ngrok URIs are not supported.

LinkedIn API Clients
====================

Background
----------

The [Rest.li protocol](https://linkedin.github.io/rest.li/spec/protocol) defines 14 resource methods as a higher-level abstraction on top of the standard HTTP methods, each with its own standardized interface and intended semantics.

For example, to retrieve one or more entities, any one of these Rest.li methods can be implemented for a resource, depending on the use case: [GET](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods#get), [BATCH\_GET](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods#batch_get), [GET\_ALL](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods#get_all), [FINDER](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods#finder-findername), or [BATCH\_FINDER](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods#batch_finder-findername). Each of those Rest.li methods would have its own standard request and response interfaces.

The Rest.li protocol also supports complex resource keys and query parameters, and it has a custom protocol for encoding them.

Nearly all of LinkedIn's APIs are built on the Rest.li framework with additional LinkedIn-specific details, which results in a robust yet complex protocol that can be challenging to implement correctly.

API Client Overview
-------------------

To simplify development, we have released API client libraries in the following languages, each of which contains comprehensive documentation and examples in their corresponding GitHub repository:

| Language | Installation and API Reference Docs | Examples |
| --- | --- | --- |
| JavaScript | [link](https://github.com/linkedin-developers/linkedin-api-js-client#linkedin-api-javascript-client) | [link](https://github.com/linkedin-developers/linkedin-api-js-client/tree/master/examples#linkedin-api-javascript-client-examples) |
| Python | [link](https://github.com/linkedin-developers/linkedin-api-python-client#linkedin-api-python-client) | [link](https://github.com/linkedin-developers/linkedin-api-python-client/tree/main/examples) |

Note that these client libraries do not support specific APIs - they provide an abstraction on top of the Rest.li protocol, making it easier to construct API requests to LinkedIn. This simplifies the process for you to build your higher-level clients for specific APIs.

Some of the key features of the LinkedIn API Client Libraries include:

* RestliClient with support for all Rest.li methods
* AuthClient with support for token creation/management
* Typed interfaces to enable code completion and inline documentation in IDEs
* Rest.li protocol 2.0 support
* Automatic key/query parameter encoding
* Support for versioned APIs
* Automatic [query tunneling](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/query-tunneling) of requests, if required

Example
-------

To illustrate the benefits of using these API clients, consider [searching for ad accounts](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-accounts#search-for-accounts) using our Advertising API. For a NodeJS application using an HTTP client library like [axios](https://axios-http.com/), there are quite a few details to get right to perform a working request, as shown in the following sample code: base URL, resource prefix, auth and custom headers, and correct encoding of complex query parameters. The result can be difficult to write and maintain and doesn’t account for edge cases requiring query tunneling.

    const axios = require('axios');
    
    const ACCESS_TOKEN = "AQX5…";
    const API_VERSION = '202302';
    
    // Define a generic function to search ad accounts by references
    function searchForAdAccountsByReferences(
     references,
     count = 10,
     sortField = 'ID',
     sortOrder = 'ASCENDING'
    ) {
     return axios.request({
       baseURL: 'https://api.linkedin.com',
       url: '/rest/adAccounts',
       method: 'get',
       headers: {
         'Authorization': `Bearer ${ACCESS_TOKEN}`,
         'X-RestLi-Method': 'finder',
         'X-RestLi-Protocol-Version': '2.0.0',
         'Connection': 'Keep-Alive',
         'LinkedIn-Version': API_VERSION
       },
       params: {
         q: 'search',
         search: `(reference:(values:List(${references.map(encodeURIComponent).join(',')})))`,
         count,
         sort: `(field:${sortField},order:${sortOrder})`
       },
       paramsSerializer: {
         // Can't use default encoding
         encode: (val) => val
       }
     }).then(response => response.data.elements);
    }
    
    // Search for ad accounts by a list of organizations, with up to 20 results
    const orgs = ['urn:li:organization:123', 'urn:li:organization:456'];
    searchForAdAccountsByReferences(orgs, 20).then(adAccounts => {
     console.log(adAccounts);
    });
    

Compare that to this code utilizing the LinkedIn API client. The client abstracts much of the complexities of constructing the request. It allows passing in objects, arrays, and strings with special characters as is, making the code easy to write and maintain. Furthermore, it handles edge cases where query tunneling may be required.

    const { RestliClient } = require('linkedin-api-client');
    
    const restliClient = new RestliClient();
    const ACCESS_TOKEN = "AQX5...";
    const API_VERSION = '202302';
    
    // Define a generic function to search ad accounts by references
    function searchForAdAccountsByReferences(
      references,
      count = 10,
      sortField = 'ID',
      sortOrder = 'ASCENDING'
    ) {
      return restliClient.finder({
        resourcePath: '/adAccounts',
        finderName: 'search',
        queryParams: {
          search: {
            reference: {
              values: references
            },
          },
          count,
          sort: {
            field: sortField,
            order: sortOrder
          }
        },
        versionString: API_VERSION,
        accessToken: ACCESS_TOKEN
      }).then(response => response.data.elements);
    }
    
    // Search for ad accounts by a list of organizations, with up to 20 results
    const orgs = ['urn:li:organization:123', 'urn:li:organization:456'];
    searchForAdAccountsByReferences(orgs, 20).then(adAccounts => {
      console.log(adAccounts);
    });
    

In summary, using these API clients can speed up and simplify the development process and make your application code maintainable and robust. If any issues arise, the corresponding Github repository is available for bug reports and enhancement suggestions.

OAuth Sample Application
========================

Overview
--------

The OAuth Sample Application is a ready-to-use code example that you can readily use to try out RESTful OAuth calls to the LinkedIn Authentication server. This version of the sample application is based on Java. The OAuth sample application shown below provides scalable and customizable code for your requirements as you begin API development with LinkedIn.

The sample application contains the client and server components you can use to manage your request calls to LinkedIn's APIs. The server creates and stores your access token and invokes APIs upon request from the client application.You can download or clone the OAuth sample application and try out these APIs as shown in the demo.

The OAuth sample application uses the following development tools:

* Spring Boot: provides the web server framework \[[https://spring.io/projects/spring-boot](https://spring.io/projects/spring-boot)\]
* LinkedIn OAuth 2.0: user authorization and API authentication
* Maven: app building and management
* Java: requires SE 7 or later versions for development

Prerequisites
-------------

* Register your application in the [LinkedIn Developer Portal](https://developer.linkedin.com/). After registration of the application, note down the Client ID and Client Secret for your future reference
* Add [http://localhost:8080/login](http://localhost:8080/login) to the Authorized Redirect URLs under the **Authentication** section
* Configure your application build by installing and using [Apache Maven](https://maven.apache.org/install.html)
* Download the OAuth sample application from [Sample Application Repository](https://github.com/linkedin-developers/java-sample-application)

Configure the OAuth sample application
--------------------------------------

**Configure the client app:**

1. Access the `application.properties` file. This file is located at `/client/src/main/resources/application.properties`
    
2. Enter the `server.port` and `SERVER_URL` in the noted fields:
    
        server.port = <replace_with_required_port_no>
        SERVER_URL = <replace_with_required_server_url>
        
    
3. Save your changes.
    

**Configure the server app:**

1. Access the `config.properties` file. This file is located at `/server/src/main/resources/config.properties`
    
2. Enter your client credential values in the noted fields:
    
        clientId = <replace_with_client_id>
        clientSecret = <replace_with_client_secret>
        redirectUri = <replace_with_redirect_url_set_in_developer_portal>
        scope = <replace_with_api_scope> 
        client_url = <replace_with_client_url>
        
    
3. Save your changes.
    

Start the OAuth sample application
----------------------------------

**To start the server:**

1. Access the server folder.
2. Open the terminal/command prompt and run the following command to install dependencies: `mvn install`
3. Execute the following command to run the spring-boot server: `mvn spring-boot:run`

Note

The server runs on `http://localhost:8080/`

**To start the client:**

1. Access the client folder.
2. Open the terminal/command prompt and run the following command to install dependencies: `mvn install`
3. Execute the following command to run the spring-boot server: `mvn spring-boot:run`

> **Note**: The client runs on `http://localhost:8989/`

Sample Application Demo
-----------------------

This demo shows an overall execution of the LinkedIn OAuth Sample Application. The demo contains clickable areas on the screen, which you can use to navigate.

Note

You can reset the demo by refreshing the page.

### Next Steps

If you are interested in exploring the sample application for Marketing, see [Marketing Sample Application](https://learn.microsoft.com/en-us/linkedin/marketing/sample-apps-lms).

### List of dependencies

| Component Name | License | Linked | Modified |
| --- | --- | --- | --- |
| [boot:spring-boot-starter-parent:2.5.2](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-parent/2.5.2) | Apache 2.0 | Static | No  |
| [boot:spring-boot-starter-parent:2.5.2](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-parent/2.5.2) | Apache 2.0 | Static | No  |
| [org.springframework.boot:spring-boot-starter-thymeleaf:2.2.2.RELEASE](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-thymeleaf/2.2.2.RELEASE) | Apache 2.0 | Static | No  |
| [org.springframework.boot:spring-boot-devtools:2.6.0](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-devtools/2.6.0) | Apache 2.0 | Static | No  |
| [com.fasterxml.jackson.core:jackson-databind:2.13.0](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind/2.13.0) | Apache 2.0 | Static | No  |
| [com.fasterxml.jackson.core:jackson-core:2.13.0](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-core/2.13.0) | Apache 2.0 | Static | No  |
| [org.springframework.boot:spring-boot-starter-web:2.5.2](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-web/2.5.2) | Apache 2.0 | Static | No  |
| [org.springframework.boot:spring-boot-starter-test:2.6.0](https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-test/2.6.0) | Apache 2.0 | Static | No  |
| [org.springframework:spring-core:5.3.13](https://mvnrepository.com/artifact/org.springframework/spring-core/5.3.13) | Apache 2.0 | Static | No  |

LinkedIn API Best Practices
===========================

LinkedIn enables application development via a robust collection of APIs. See [Getting Access](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access) for details on how to get access.

Use the following guidelines to build an application that members will trust to handle and secure their sensitive data.

* [Application Development](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/application-development): Discover best practices for implementing authorization and error handling.
* [Building Secure Applications](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/secure-applications): Use these guidelines to secure your application and members' data against threats such as phishing and cross-site request forgery.
* [Breaking Changes](https://learn.microsoft.com/en-us/linkedin/shared/breaking-change-policy): A breaking change is a change that may require you to make changes to your application to avoid disruption to your integration.
* [Endpoint Catalog](https://www.linkedin.com/developers/news/featured-updates/introducing-the-api-product-endpoint-catalog): This tool provides a view of the endpoints and permissions your application has access to. view, sort, and filter all the endpoints associated with an API product.
* [LinkedIn Developer News](https://www.linkedin.com/content/developers/news): Stay on top of what’s new with our portal, products, and programs.

Best Practices for Application Development
==========================================

LinkedIn members are more comfortable trusting your application when you are transparent about how you will use their data. We recommend following these best practices to help your application deliver the most value.

Authentication
--------------

* Whenever possible, **remind the member that they are logged in** to your application by displaying their name, portrait, and/or account settings somewhere on the page.
* **Avoid having to log in multiple times**. When a member is integrated for multiple permissions, combine the permissions into a single request rather than asking the member to reauthenticate and grant consent each time.
* **Avoid generating an access token for each API call.Cache the member's access token** after they grant your application access, and do not re-authenticate the member unless they log out or the access token expires.
* Make sure you **allow the member to log out**, and when they do log out, ensure you destroy their access token and refresh token, as applicable.
* Validate the member access token using [Token Introspection](https://learn.microsoft.com/en-us/linkedin/shared/authentication/token-introspection) or by calling any API before making the access token call.
* Whenever the access token gets expired, make use of the refresh token, if applicable, to exchange for a new access token, unless the refresh token has also expired or been revoked.
* Reintroduce the member into the authentication flow only when both the access token and the refresh token have expired or been revoked.
* If you authorize the member through the JS SDK, do not send the member through the REST authorization flow. If you do, users will have to re-authorize your application. You can exchange the JS SDK token for an OAuth 2.0 REST access token if you want to make REST calls. Otherwise, use the JS SDK token to make calls with the JS SDK.

If a member authorizes your application through the REST workflow, it does not mean they are automatically logged in to the linkedin.com website. You should not assume that the member has access to resources that are on the LinkedIn website while using your application.

Error Handling and Logging
--------------------------

### System Outages

Due to the nature of cloud APIs, LinkedIn's services are occasionally interrupted or temporarily unavailable for reasons outside of LinkedIn's control. Assume that any API call you make to LinkedIn or any third party could potentially fail. Always include error-handling logic in your requests. See the [Errors](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling?context=linkedin/context) page for API error codes and messages.

### Errors

A `500 Internal Server Error` indicates that LinkedIn is experiencing an internal error. If you continue to receive server errors, record the following details:

* Request: `url`, `method`, `header`, e.g., `access_token`, `body`
* Response: `header`, e.g., `x-li-uuid`, `x-li-fabric`, `x-li-request-id`, `body`
* Your application configuration, e.g., `client_id`

If you continue to receive errors, reach out to your partner technical support channel, or view our [Developer Support Knowledge](https://developer.linkedin.com/support).

Best Practices for Secure Applications
======================================

At LinkedIn, we take the privacy of our members very seriously. When we grant access to APIs, we expect developers to take member privacy just as seriously as we do. The LinkedIn platform uses permissions to protect and prevent abuse of our members' information. By using the [OAuth 2.0](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) authentication protocol, we allow an application to access LinkedIn data while protecting members' credentials. Because of this protocol, members are ensured that applications on our platform are easy to use _and_ protect their privacy and security.

Note

You should always request the minimal scopes necessary and only request permissions that are needed for application functionality.

Ensure your application follows these best practices.

Access Tokens
-------------

Using access tokens, you can access a member's private information through the LinkedIn APIs. To keep access tokens safe:

* Do not store them in insecure or easily accessible locations. Client-side files, such as JavaScript or HTML files, should never be used to store sensitive information, as these can easily be accessed.
* Do not store access tokens in code files that can be decompiled, such as Native iOS, Android, or Windows Application code files.
* When making calls, always pass access tokens over a secure (HTTPS) connection.

API Key and Secret Key
----------------------

Two pieces of identifiable information are required to make calls to the LinkedIn API: `Client ID` (Consumer Key/API key) and `Client Secret`.

The Client ID is a public identifier of your application.  
The Client Secret is confidential and should only be used to authenticate your application and make requests to LinkedIn's APIs.

Both the Client ID and Client Secret are needed to confirm your application’s identity and it is critical that you do not expose your Client Secret. Follow these suggestions to keep the secret safe:

* Do not share your access tokens with anyone, and **do not** pass it in the URL when making API calls, or URI query-string parameters, or post in support forums, chat, etc.
* When creating a native mobile application, do not store it locally on a mobile device.
* Do not expose files such as JavaScript or HTML files in client-side code.
* Do not store it in files on a web server that can be viewed externally. For example, configuration files, include files, etc.
* Do not store it in log files or error messages.

Remember that when exchanging an OAuth 2.0 authorization code for an access token, `client_secret` is passed as part of the request. Make sure you **do not expose this request publicly!**

Secure APIs
-----------

To prevent others from reading your requests and to prevent man-in-the-middle attacks, all OAuth 2.0 requests to our authentication servers must be done over HTTPS. Your application should also be hosted on a secure server, particularly for pages where a member enters private information (such as their password for your site) and for any URLs where you ask LinkedIn to redirect the member as part of the OAuth authorization flow.

Phishing Prevention
-------------------

Cybercriminals often create websites that look and feel authentic but are really just replicas created to steal user credentials. Educate your users to look for signs to ensure they are entering credentials for a real LinkedIn application. Note that browsers may look different, and this may not always be enough to differentiate a legitimate site from a phishing site. Alert members not to enter credentials when in doubt and to contact you when they suspect suspicious activity.

LinkedIn has a DigiCert SHA2 Secure Server Certificate (padlock) that can be viewed prior to the URL in the browser. The base URL hostname is always "[https://www.linkedin.com/](https://www.linkedin.com/)...". Beware of URLs that try to mimic LinkedIn by using common misspellings or swapping similar characters such as "1" (one) for "l" (letter 'L'), e.g., "l1inkedIn.com/", or "linked1n.com/".

Cross-Site Request Forgery
--------------------------

To protect against [CSRF attacks](http://en.wikipedia.org/wiki/Cross-site_request_forgery), during authorization, you must pass a `state` parameter. This should be a unique string value (for each request) that is unique, difficult to guess, and should not contain private or sensitive information.

### Sample State Value

    state=760iz0bjh9gy71asfFqa
    

On successful authorization, the redirected URL should look like:

### Sample Callback URL

    https://OAUTH2_REDIRECT_URI/?code=AUTH_CODE&state=760iz0bjh9gy71asfFqa
    

Make sure that the state parameter in the response matches the one you passed in your authorization request. If the state does not match, the request may be a result of CSRF and should be rejected.

### Third-Party Libraries

When using a third-party library to interact with LinkedIn's APIs, make sure that the library is from a trusted source. Read reviews, look at the code, and do research to make sure the library is not malicious and does not behave unexpectedly.

LinkedIn **does not officially support third-party libraries**. Contact that library’s development team if you have technical questions or concerns.

LinkedIn API Breaking Change Policy
===================================

Overview
--------

As our APIs evolve, LinkedIn will make reasonable efforts to notify you of breaking changes in advance with sufficient time to adapt to these changes.

Important

We may make changes without prior notice if the change is considered non-breaking, or if it is a breaking change being made to address critical product bugs or legal, security, or privacy concerns.

Review this guide carefully to understand what kind of changes we consider to be breaking and non-breaking, and how to ensure that your application can adapt automatically to any change we categorize as non-breaking.

Definition
----------

A **breaking change** is a change that may require you to make changes to your application in order to avoid disruption to your integration. The following are a few examples of changes we consider breaking:

* Changes to existing permission definitions
* Removal of an allowed parameter, request field or response field
* Addition of a required parameter or request field without default values
* Changes to the intended functionality of an endpoint. _For example, if a DELETE request previously used to archive the resource but now hard deletes the resource._
* Introduction of a new validation

A **non-breaking change** is a change that you can adapt to at your own discretion and pace without disruption. In most cases, we will communicate non-breaking changes after they are already made. Ensure that your application is designed to be able to handle the following types of non-breaking changes without prior notice from LinkedIn:

* Addition of new endpoints
* Addition of new methods to existing endpoints
* Addition of new fields in the following scenarios:
    * New fields in responses
    * New optional request fields or parameters
    * New required request fields that have default values
* Addition of a new value returned for an existing text field
* Changes to the order of fields returned within a response
* Addition of an optional request header
* Removal of redundant request header
* Changes to the length of data returned within a field
* Changes to the overall response size
* Changes to error messages. _We do not recommend parsing error messages to perform business logic. Instead, you should only rely on HTTP response codes and error codes._
* Fixes to HTTP response codes and error codes from incorrect code to correct code

Communication
-------------

Please look out for email communication from LinkedIn where we may notify you about breaking and non-breaking changes to our APIs. For breaking change notices, the email notice will usually include the future release date of the breaking change as well as instructions on what actions you need to take. To avoid disruption to your users, ensure that you perform the recommended actions by LinkedIn before the release date of the breaking change.