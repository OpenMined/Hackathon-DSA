::: main-content__wrapper
::: c01-rich-text-editor
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
To complete this guide, you will need to have a set of [keys and
tokens](/en/docs/authentication) to authenticate your request. You can
generate these keys and tokens by following these steps:

-   [Sign up for a developer account](/en/apply-for-access) and receive
    approval.
-   Create a [Project](/en/docs/projects) and an associated [developer
    App](/en/docs/apps) in the developer portal.
-   Navigate to your App\'s "Keys and tokens" page to generate the
    required credentials. Make sure to save all credentials in a secure
    location.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
In this example, in one request, we\'ll create a new group conversation
and add our first message to it. We\'ll then add a second message to the
created conversation.

#### Step one: Start with a tool or library

To begin working with the manage Direct Message endpoints, we are going
to use the Postman tool to simplify the process. A TwitterDev-authored
collection of example Twitter API v2 requests will be used to explore
six endpoints used to create new Direct Messages and to list Direct
Message conversation events.

While most of the collection is pre-filled, there are a few details that
you\'ll need to provide that are based on the Twitter App created to
host these API requests. First, let\'s get the collection
loaded/updated.

To load the Twitter API v2 Postman collection into your environment,
please click on the following button:
:::
:::

::: b03-button-v3
[](https://t.co/twitter-api-postman){.chirp-btn .twtr-spacing--mb-500
.chirp-btn--primary .chirp-btn--icon .chirp-btn--icon-end
.twtr-scribe-clicks}

::: chirp-btn__icon
![](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/m1_vnext/carat.svg){.chirp-btn__icon--img}
:::

Add Twitter API v2 to Postman
:::

::: c01-rich-text-editor
::: is-table-default
Once you have the Twitter API v2 collection loaded in Postman, navigate
to the "Manage Direct Messages" folder. This folder\'s Authorization tab
has been pre-filled where possible, and you can update a few settings to
share your Twitter App\'s authentication details. This folder also
contains three endpoints for creating new Direct Messages. Note that
there is also a \"Direct Message lookup\" folder with three available
endpoints for retrieving Direct Message conversation events, including
sending and receiving messages, and when conversation participants join
and leave..

Since creating group conversations is an exciting new feature of the
Twitter API v2, this example will focus on that. We will be working with
the \"New group DM and conversation\" example. We will use this request
to create a Direct Message group conversation.

The next step is to authenticate with the endpoint.

**Step two: Authenticate your request** \

To properly make a request to the Twitter API, you need to verify that
you have permission to do so. To make a successful request to this
endpoint, we will be using [OAuth 2.0 Authorization Code Flow with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) . You can
generate an access token within Postman.

With Postman you can set the authentication method at the folder level
or at the request level. Here we will be configuring the authentication
details at the folder level.

Navigate to the \"Manage Direct Messages\" folder, select the
\"Authorization\" tab and confirm that the Type to set to "OAuth 2.0,"
and \"Add auth data to\" is set to \"Request Headers.\" In the \"Current
Token\" section, make sure the \"header Prefix\" is set to Bearer.

To configure and generate a new token:

1.  Create a Token Name, such as \"Manage DMs.\"

2.  Confirm that **Grant Type** is set to Authorization Code (with
    PKCE).

3.  Set your **Callback URL** . You will want to update your Callback
    URL to exactly match the Callback URL associated with your
    application in the [v2 Dev
    Portal](https://developer.twitter.com/en/portal/dashboard) . With
    the Twitter App used with this example, the Callback URL is set to -
    [*https://www.example.com* .](https://www.example.com/) (Note that
    since this must match exactly,
    [*https://example.com*](https://example.com) would not work.)

4.  Confirm that **Auth URL** is set to [[
    https://twitter.com/i/oauth2/authorize
    ]{.code-inline}](https://twitter.com/i/oauth2/authorize) .

5.  Confirm that **Access Token URL** is set to [[
    https://api.twitter.com/2/oauth2/token ]{.code-inline} .\
    ](https://api.twitter.com/2/oauth2/token) **Client ID** - Copy and
    paste OAuth 2.0 client ID from the Developer Portal\
    **Client Secret** - You will need this only if you are using an App
    type that is a confidential client. If so, copy and paste the OAuth
    2.0 Client Secret from the Developer Portal.

6.  Confirm that **Scope** is set to [ dm.read ]{.code-inline} , [
    dm.write ]{.code-inline} , [ tweet.read ]{.code-inline} , and [
    users.read ]{.code-inline} .

7.  Confirm that **State** is set to "state."

8.  Confirm that **Client Authentication** is set to Send as Basic Auth
    header.

9.  Click where it says **Get New Access Token** , click \"Authorize
    app\" as part of the \"Sign-in with Twitter\" process.

10. Click the \"Proceed\" button and then the \"Use Token\" to generate
    a token.

11. Click on the \"Save\" button to save these configuration details.

You may get a message that you are not logged into Twitter. If you get
this error, you will need to log in to the Twitter account you are
trying to post on behalf of inside of Postman.

Now that these OAuth 2.0 details have been set at the folder level,
navigate to each of the examples and their \"Authorization\" tab and
confirm that they have their Type set to \"Inherit auth from parent.\"

Note that this token will expire soon, and you\'ll need to regenerate it
by clicking on the \"Get New Access Token\" button. Clicking that will
trigger the \"Sign-in with Twitter\" process and generate a fresh token
to make requests with.

#### Step three: Specify the Direct Message conversation participants and message contents

Navigate to the "Body" tab and make updates to the example JSON object.
Set the [ participant_ids ]{.code-inline} attribute to the accounts you
want to send the Direct Message to.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
   "message": {"text": "Hello to just you two, this is a new group conversation."},
   "participant_ids": ["944480690","906948460078698496"],
   "conversation_type": "Group"       
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Once you have everything set up, hit the \"Send\" button, and you will
receive a similar response to the example response below. A reminder
that if your token has expired since you created it above, you can
return to the folder\'s Authorization tab and click on the \"Get New
Access Token\" to create a fresh token.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
   "data": {
       "dm_conversation_id": "1582103724607971328",
       "dm_event_id": "1582103724607971332"
   }
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If the returned response \"data\" object contains a [ dm_conversation_id
]{.code-inline} and an [ dm_event_id ]{.code-inline} , you have
successfully created a new Direct Message conversation. To start looking
up events associated with this conversation, head over to the Direct
Message lookup Quick start guide.

#### Step five: Add another message to that group conversation

Now select the \"Add DM to conversation\" example, and select the
\"Params\" tab. Under \"Path Variables\" , update the [
dm_conversation_id ]{.code-inline} to the ID of the conversation you
created above.

  -------------------- ---------------------
  **Key**              **Value**
  dm_conversation_id   1582103724607971328
  -------------------- ---------------------

Using this conversation ID, the request path will resolve to: [
https://api.twitter.com/2/dm_conversations/1582103724607971328/messages
]{.code-inline}

Also, update the \"Body\" tab with request JSON containing the message
text you want to send:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
   "text": "Adding a new message to our group conversation..."
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Once you have everything set up, hit the \"Send\" button, and you will
receive a similar response to the following example response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
   "data": {
       "dm_conversation_id": "1582103724607971328",
       "dm_event_id": "1582106224379559940"
   }
}
    
```
:::
:::
:::
:::
