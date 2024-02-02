
Generate an Access Token Using Postman - LinkedIn | Microsoft Learn

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

Generate an Access Token - Getting Started with Postman
=======================================================

* Article
* 05/08/2023
* 2 contributors

Feedback

In this article
---------------

Summary
-------

The full process your application will need to implement for 3-legged tokens is described in Authorization Code Flow and 2-legged tokens is described in Client Credentials Flow. The steps outlined below describe the process for using LinkedIn's Public Postman workspaces to generate OAuth tokens for testing. For any specific examples, we will use the Marketing Solutions workspace, but all steps should easily apply to all workspaces. These steps assume you have already created a free Postman account.

### Step 1 - Application

Go to the LinkedIn Developer Portal, select the app you'll be using, click the "Auth" tab, and locate your Client ID and Client Secret. Please note these values for use later during this process.

### Step 2 - Auth Settings

From the same "Auth" tab, scroll to the bottom of the page. Under "OAuth 2.0 Settings", add the Postman callback URLs `https://oauth.pstmn.io/v1/callback` and `https://oauth.pstmn.io/v1/browser-callback` to your Redirect URL list.

Caution

Postman uses the term "Callback URL"  
LinkedIn uses the term "Redirect URL"

### Step 3 - Fork Collections and Environments

Navigate to LinkedIn's public Postman workspaces:

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
	+ Note the Callback URL should be `https://oauth.pstmn.io/v1/callback` with the "Authorize using browser" box checked if you are using the Postman Desktop app
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

Learn more about Postman variables in Postman's online documentation

Note that some requests dynamically set variables via a script that runs post request execution. You will know if a script is set to run for a request if there is a green dot next to the Tests tab.

To see an example sample response, view the saved example.

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