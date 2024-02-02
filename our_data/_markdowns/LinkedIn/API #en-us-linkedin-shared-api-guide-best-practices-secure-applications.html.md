
Best Practices for Secure Applications - LinkedIn | Microsoft Learn

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

Best Practices for Secure Applications
======================================

* Article
* 05/08/2023
* 4 contributors

Feedback

In this article
---------------

At LinkedIn, we take the privacy of our members very seriously. When we grant access to APIs, we expect developers to take member privacy just as seriously as we do. The LinkedIn platform uses permissions to protect and prevent abuse of our members' information. By using the OAuth 2.0 authentication protocol, we allow an application to access LinkedIn data while protecting members' credentials. Because of this protocol, members are ensured that applications on our platform are easy to use *and* protect their privacy and security.

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

LinkedIn has a DigiCert SHA2 Secure Server Certificate (padlock) that can be viewed prior to the URL in the browser. The base URL hostname is always "https://www.linkedin.com/...". Beware of URLs that try to mimic LinkedIn by using common misspellings or swapping similar characters such as "1" (one) for "l" (letter 'L'), e.g., "l1inkedIn.com/", or "linked1n.com/".

Cross-Site Request Forgery
--------------------------

To protect against CSRF attacks, during authorization, you must pass a `state` parameter. This should be a unique string value (for each request) that is unique, difficult to guess, and should not contain private or sensitive information.

### Sample State Value

```
state=760iz0bjh9gy71asfFqa
```
On successful authorization, the redirected URL should look like:

### Sample Callback URL

```
https://OAUTH2_REDIRECT_URI/?code=AUTH_CODE&state=760iz0bjh9gy71asfFqa
```
Make sure that the state parameter in the response matches the one you passed in your authorization request. If the state does not match, the request may be a result of CSRF and should be rejected.

### Third-Party Libraries

When using a third-party library to interact with LinkedIn's APIs, make sure that the library is from a trusted source. Read reviews, look at the code, and do research to make sure the library is not malicious and does not behave unexpectedly.

LinkedIn **does not officially support third-party libraries**. Contact that library’s development team if you have technical questions or concerns.

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