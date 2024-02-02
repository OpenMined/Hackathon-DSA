
Best Practices for Application Development - LinkedIn | Microsoft Learn

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

Best Practices for Application Development
==========================================

* Article
* 05/08/2023
* 4 contributors

Feedback

In this article
---------------

LinkedIn members are more comfortable trusting your application when you are transparent about how you will use their data. We recommend following these best practices to help your application deliver the most value.

Authentication
--------------

* Whenever possible, **remind the member that they are logged in** to your application by displaying their name, portrait, and/or account settings somewhere on the page.
* **Avoid having to log in multiple times**. When a member is integrated for multiple permissions, combine the permissions into a single request rather than asking the member to reauthenticate and grant consent each time.
* **Avoid generating an access token for each API call.Cache the member's access token** after they grant your application access, and do not re-authenticate the member unless they log out or the access token expires.
* Make sure you **allow the member to log out**, and when they do log out, ensure you destroy their access token and refresh token, as applicable.
* Validate the member access token using Token Introspection or by calling any API before making the access token call.
* Whenever the access token gets expired, make use of the refresh token, if applicable, to exchange for a new access token, unless the refresh token has also expired or been revoked.
* Reintroduce the member into the authentication flow only when both the access token and the refresh token have expired or been revoked.
* If you authorize the member through the JS SDK, do not send the member through the REST authorization flow. If you do, users will have to re-authorize your application. You can exchange the JS SDK token for an OAuth 2.0 REST access token if you want to make REST calls. Otherwise, use the JS SDK token to make calls with the JS SDK.

If a member authorizes your application through the REST workflow, it does not mean they are automatically logged in to the linkedin.com website. You should not assume that the member has access to resources that are on the LinkedIn website while using your application.

Error Handling and Logging
--------------------------

### System Outages

Due to the nature of cloud APIs, LinkedIn's services are occasionally interrupted or temporarily unavailable for reasons outside of LinkedIn's control. Assume that any API call you make to LinkedIn or any third party could potentially fail. Always include error-handling logic in your requests. See the Errors page for API error codes and messages.

### Errors

A `500 Internal Server Error` indicates that LinkedIn is experiencing an internal error. If you continue to receive server errors, record the following details:

* Request: `url`, `method`, `header`, e.g., `access_token`, `body`
* Response: `header`, e.g., `x-li-uuid`, `x-li-fabric`, `x-li-request-id`, `body`
* Your application configuration, e.g., `client_id`

If you continue to receive errors, reach out to your partner technical support channel, or view our Developer Support Knowledge.

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