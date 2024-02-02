::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick overview will help you make your first request to the manage
List endpoints using
[Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman)
.

If you would like to see sample code in different languages, please
visit our [Twitter API v2 sample
code](https://github.com/twitterdev/Twitter-API-v2-sample-code)
GitHub repository.

**Note:** For this example, we will make a request to the *Create a
List* endpoint, but you can apply the learnings from this quick start to
other manage requests as well.
:::
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
There are several different tools, code examples, and libraries that you
can use to make a request to this endpoint, but we will use the Postman
tool here to simplify the process.

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
to the "List" folder, select another folder "Manage List", and then
choose \"Create a List\".

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that
you have permission to do so. To do this with the manage Tweets
endpoints, you must authenticate your request using either [OAuth 1.0a
User Context](/en/docs/authentication/oauth-1-0a) or [OAuth 2.0
Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) .

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens (and specifically your API Key, API
Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access
Token Secret) to Postman. You can do this by selecting the environment
named "Twitter API v2" (in the top-right corner of Postman), and adding
your keys and tokens to the \"initial value\" and \"current value\"
fields (by clicking the eye icon next to the environment dropdown).

If you\'ve done this correctly, these variables will automatically be
pulled into the request\'s authorization tab.\
:::
:::

::: c01-rich-text-editor
::: is-table-default
When creating a new List with this endpoint, a [ name ]{.code-inline}
for the List is a required body parameter. Optionally, you can provide a
description and specify whether the List is private.

In Postman, navigate to the "Body" tab and enter the name of the List as
the value for the [ name ]{.code-inline} parameter. Additionally, if you
wish to add a [ description ]{.code-inline} for the List, simply add a
new key labeled description in the same fashion as the [ name
]{.code-inline} , followed by the description of the List as the value.
Making a List private will follow the same pattern, but only [ true
]{.code-inline} or [ false ]{.code-inline} values are accepted for this
parameter.

  ------------------------------- ------------------------------------- --------------------
  **Key**                         **Value**                             **Parameter type**
  [ ` name ` ]{.code-inline}      Name of the list (required)           body
  [ description ]{.code-inline}   Description for the list (optional)   body
  [ private ]{.code-inline}       true or false (optional)              body
  ------------------------------- ------------------------------------- --------------------

You should now see a similar URL next to the \"Send\" button:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.t05__pre--with-button .t05__pre--wrap-text}
 https://api.twitter.com/2/lists
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Step four: Make your request and review your response \

Once you have everything set up, hit the \"Send\" button, and you will
receive a similar response to the following example response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "data": {
    "id": "1441162269824405510",
    "name": "New list created from Postman"
  }
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If the returned response object contains an [ id ]{.code-inline} and the
[ name ]{.code-inline} of your List, you have successfully created the
List.

To delete a List, select the "Delete a List" request also found in the
"Lists" folder of the Twitter API v2 collection loaded in Postman. This
endpoint requires the ID of the List you wish to delete. In the "Params"
tab, enter the ID of the List you wish to delete as the value for the [
id ]{.code-inline} column.

On successful delete request, you will receive a response similar to the
following example:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "data": {
    "deleted": true
  }
}
    
```
:::
:::
:::
:::
