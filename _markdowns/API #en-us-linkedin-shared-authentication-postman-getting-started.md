::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

The full process your application will need to implement for 3-legged
tokens is described in [Authorization Code
Flow](authorization-code-flow) and 2-legged tokens is described in
[Client Credentials Flow](client-credentials-flow) . The steps outlined
below describe the process for using LinkedIn\'s Public Postman
workspaces to generate OAuth tokens for testing. For any specific
examples, we will use the Marketing Solutions workspace, but all steps
should easily apply to all workspaces. These steps assume you have
already created a [free Postman
account](https://www.postman.com/postman-account/) .

### Step 1 - Application

Go to the [LinkedIn Developer
Portal](https://www.linkedin.com/developers/apps) , select the app
you\'ll be using, click the \"Auth\" tab, and locate your Client ID and
Client Secret. Please note these values for use later during this
process.

![LinkedIn Auth Tab](../../media/linkedin-auth-tab.png)

### Step 2 - Auth Settings

From the same \"Auth\" tab, scroll to the bottom of the page. Under
\"OAuth 2.0 Settings\", add the Postman callback URLs
` https://oauth.pstmn.io/v1/callback ` and
` https://oauth.pstmn.io/v1/browser-callback ` to your Redirect URL
list.

::: CAUTION
Caution

Postman uses the term \"Callback URL\"\
LinkedIn uses the term \"Redirect URL\"
:::

![Postman Callback URL](../../media/postman-callback-url.png)

### Step 3 - Fork Collections and Environments

Navigate to LinkedIn\'s public Postman workspaces:

[![Try in
Postman](../../media/postman-button.png)](https://www.postman.com/linkedin-developer-apis?tab=workspaces)

Choose a workspace and fork the collections and relevant environments of
interest. Each collection will have an environment it should be used
with. For example, if you were to navigate to the LinkedIn Marketing
Solutions workspace, the Campaign Management collection should be used
with the ` campaign-management-env ` environment.

#### Fork a Postman Collection

Fork a collection:

Fork an environment:

Fill in the Client ID and Client Secret environment variables before
moving onto the next step. Don\'t forget to save your changes!

![Environment Variables](../../media/postman-environment-variables.png)

Each collection in each workspace will have its OAuth 2.0 Authorization
settings pre-populated with the correct URLs, environment variables, and
scopes to be able to successfully run the requests within the
corresponding Use Cases folder. Click on a collection title to open
it\'s Authorization tab. Ensure that the correct environment is selected
and click \"Get new access token\":

-   Grant Type: Authorization Code (3-legged token) or Client
    Credentials (2-legged token)
-   Callback (Redirect) URL:
    ` https://oauth.pstmn.io/v1/browser-callback `
    -   Note the Callback URL should be
        ` https://oauth.pstmn.io/v1/callback ` with the \"Authorize
        using browser\" box checked if you are using the Postman Desktop
        app
-   Auth URL: ` https://www.linkedin.com/oauth/v2/authorization `
-   Access Token URL: ` https://www.linkedin.com/oauth/v2/accessToken `
-   Client ID: {using the client_id from the environment variables}
-   Client Secret: {using the client_secret from the environment
    variables}
-   Scope: Differs per collection but an example is {
    ` rw_ads,r_basicprofile,w_organization_social,w_member_social,rw_organization_admin `
    }
-   Client Authentication: ` Send client credentials in body ` when the
    Grant Type is Authorization Code. ` Send as Basic Auth header ` when
    the Grant Type is Client Credentials.

![Set Authorization
Parameters](../../media/postman-get-access-token.png)

### Step 6 - Identity Authentication

If the Grant Type in Step 5 was Authorization Code then Postman will
take you to the LinkedIn authorization page, where you may be prompted
to log into LinkedIn. Click \"Allow\" to authorize the request. The
prompt on the authorization page is dictated by the requested scopes in
the previous step.

![Authorize Scopes](../../media/postman-authorization-page.png)

### Step 7 - Use Token

Postman will then display your access token to be used for testing.
Choose the \'Use Token\' button to set this as the currently used token.
The token will automatically be propagated to all requests within the
corresponding collection. The video below shows an example of requesting
a 3-legged token via the Authorization Code Grant Type.

Finally, send a request within the Use Cases folder. Ensure the correct
environment is selected and that if any environment or collection level
variables are being used in the request, ensure they are set. For
example, in the screenshot below, the request uses the
` sponsoredaccount_id ` variable from the ` campaign-management-env `
environment.

Learn more about Postman variables in [Postman\'s online
documentation](https://learning.postman.com/docs/sending-requests/variables/#variable-scopes)

![Make First API Call](../../media/postman-send-request.png)

Note that some requests dynamically set variables via a script that runs
post request execution. You will know if a script is set to run for a
request if there is a green dot next to the Tests tab. ![Test
Script](../../media/postman-test-script.png)

To see an example sample response, view the saved example. ![View
Example Response](../../media/postman-example-response.png)
:::
