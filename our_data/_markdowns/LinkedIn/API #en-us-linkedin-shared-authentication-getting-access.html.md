
Getting Access to LinkedIn APIs - LinkedIn | Microsoft Learn

Skip to main content

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

Download Microsoft Edge
More info about Internet Explorer and Microsoft Edge

Table of contents 

Exit focus mode

Read in English

Save

Table of contents
Read in English

Save
Edit

Print

Twitter
LinkedIn
Facebook
Email

Table of contents

Getting Access to LinkedIn APIs
===============================

* Article
* 07/25/2023
* 10 contributors

Feedback

In this article
---------------

The LinkedIn API uses OAuth 2.0 for user authorization and API authentication. Applications must be authorized and authenticated before they can fetch data from LinkedIn or get access to member data. This page summarizes the available permissions and partner programs available for accessing LinkedIn APIs. Most permissions and partner programs require explicit approval from LinkedIn. Open Permissions are the only permissions that are available to all developers without special approval.

All permissions listed below are used in either Member Authentication Flow (3-legged) or Application Authentication Flow (2-legged). More about these permission types can be found in Authenticating with OAuth 2.0 Overview.

Open Permissions (Consumer)
---------------------------

The following permissions are available to all developers, and may be added via self-service through the LinkedIn Developer Portal, under the Products tab on your application page. LinkedIn products can be enabled after creating a new application.

| Product/Program | Permission | Description |
| --- | --- | --- |
| Sign in with LinkedIn using OpenID Connect | profile | **Member Auth**: Retrieve authenticated member's name, headline, and photo. |
| Sign in with LinkedIn using OpenID Connect | email | **Member Auth**: Retrieve authenticated member's primary email address. |
| Share on LinkedIn | w\_member\_social | **Member Auth**: Post, comment and like posts on behalf of an authenticated member. |

Learning
--------

Developers seeking to build a learning related integration should refer to the Request API Access page within the LinkedIn Learning API space.

Marketing
---------

Developers seeking to build a marketing related integration using Advertising APIs permissions must be approved. You can apply for access through the Developer Portal. This can be done by selecting your app from My Apps, navigate to the Products tab, and add the Marketing Developer Platform product. Qualifications to be an Advertising APIs partner are available at Become a Partner.

Audiences permissions may be applied for after being an approved Marketing Developer Platform partner. Contact support or your partner rep for application information.

| Product/Program | Permission | Description |
| --- | --- | --- |
| Advertising APIs | rw\_organization\_admin | **Member Auth**: Manage an authenticated member’s company pages and retrieve reporting data. |
| Advertising APIs | r\_organization\_admin | **Member Auth**: Retrieve an authenticated member’s company pages and their reporting data. |
| Advertising APIs | w\_organization\_social | **Member Auth**: Post, comment and like posts on behalf of an organization. Restricted to organizations in which the authenticated member has one of the following company page roles. - `ADMINISTRATOR`
- `DIRECT_SPONSORED_CONTENT_POSTER`
- `LEAD_GEN_FORMS_MANAGER`
 |
| Advertising APIs | r\_organization\_social | **Member Auth**: Retrieve organizations' posts, comments, and likes. |
| Marketing Developer Platform (MDP) | w\_member\_social | **Member Auth**: Post, comment, and like posts on behalf of an authenticated member. |
| Advertising APIs | rw\_ads | **Member Auth**: Manage and read an authenticated member's ad accounts. Restricted to ad accounts in which the authenticated member has one of the following ad account roles. - `ACCOUNT_BILLING_ADMIN`
- `ACCOUNT_MANAGER`
- `CAMPAIGN_MANAGER`
- `CREATIVE_MANAGER`
 |
| Advertising APIs | r\_ads | **Member Auth**: Read an authenticated member's ad accounts. Restricted to ad accounts in which the authenticated member has one of the following ad account roles: * `ACCOUNT_BILLING_ADMIN`
* `ACCOUNT_MANAGER`
* `CAMPAIGN_MANAGER`
* `CREATIVE_MANAGER`
* `VIEWER`
 |
| Advertising APIs | r\_ads\_reporting | **Member Auth**: Retrieve reporting for advertising accounts. |
| Advertising APIs | r\_1st\_connections\_size | **Member Auth**: Retrieve the count of an authenticated member's 1st-degree connections. |
| Advertising APIs | r\_basicprofile | **Member Auth**: Read an authenticated member's basic profile including name, photo, headline, and public profile URL. |
| Lead Sync | r\_marketing\_leadgen\_automation | **Member Auth**: Access your lead generation forms and retrieve leads (including event leads, ad leads, and organization page leads). |
| Audiences | rw\_dmp\_segments | **Member Auth**: Create and manage matched audiences. |

Sales
-----

Developers seeking to build sales related integration using one of the permissions below must be approved as a Sales Navigator Application Platform (SNAP) partner. Apply here to be a SNAP partner.

| Product/Program | Permission | Description |
| --- | --- | --- |
| Sales Navigator Application Platform(SNAP) | r\_sales\_nav\_analytics | **Member Auth**: Enables access to Sales Navigator Analytics retrieval. |
| Sales Navigator Application Platform(SNAP) | r\_sales\_nav\_display | **Member Auth**: Display Services permission for Sales Navigator. |
| Sales Navigator Application Platform(SNAP) | r\_sales\_nav\_validation | **Application Auth**: Access Sales Navigator endpoints for CRM data validation. |
| Sales Navigator Application Platform(SNAP) | r\_sales\_nav\_profiles | **Application Auth**: Access Sales Navigator endpoints that present matched, publicly available member profile information. |

Talent
------

Developers seeking to build talent related integrations through one of the programs listed below can apply here. We recommend familiarizing yourself with the types of partner integrations available before applying by visiting here and here.

* Recruiter System Connect (RSC)
* Apply Connect
* Talent Hub
* Apply with LinkedIn
* Premium Job Posting
* Easy Apply

Compliance (Closed)
-------------------

The following permissions used for Compliance integrations are listed for reference purposes only. Access is closed and may not be requested.

| Product/Program | Permission | Description |
| --- | --- | --- |
| Compliance | r\_compliance | **Member Auth**: Retrieve activities for compliance monitoring and archiving |
| Compliance | w\_compliance | **Member Auth**: Manage and delete data for compliance. |

---

Feedback
--------

Was this page helpful?

Yes

No

Provide product feedback

Feedback
--------

Submit and view feedback for

This product
This page

View all page feedback

---

Additional resources
--------------------

California Consumer Privacy Act (CCPA) Opt-Out Icon

Your Privacy Choices

Theme

* Light
* Dark
* High contrast

* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2024

Additional resources
--------------------

### In this article

California Consumer Privacy Act (CCPA) Opt-Out Icon

Your Privacy Choices

Theme

* Light
* Dark
* High contrast

* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2024