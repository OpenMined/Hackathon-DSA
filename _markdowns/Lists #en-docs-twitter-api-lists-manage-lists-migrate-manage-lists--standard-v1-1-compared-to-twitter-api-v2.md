::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
If you have been working with the standard v1.1 [POST
lists/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-create)
, [POST
lists/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-destroy)
, and [POST
lists/update](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-update)
endpoints, the goal of this guide is to help you understand the
similarities and differences between the standard v1.1 and Twitter API
v2 manage List endpoints.

-   **Similarities**
-   **Differences**
    -    Endpoint URLs
    -   App and Project requirements
    -   HTTP methods
    -   Rate limits
    -   Request parameters

### Similarities

####   **Authentication**  

Both endpoint versions support [OAuth 1.0a User
Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a)
. Therefore, if you were previously using one of the standard v1.1
manage Lists endpoints, you can continue using the same authentication
method if you migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ POST https://api.twitter.com/1.1/lists/create.json\
        ]{.code-inline} (Creates a List)
    -   [ POST https://api.twitter.com/1.1/lists/destroy.json\
        ]{.code-inline} (Deletes a List)
    -   [ POST https://api.twitter.com/1.1/lists/update.json\
        ]{.code-inline} (Updates a List)
-   Twitter API v2 endpoint:
    -   [ POST https://api.twitter.com/2/lists\
        ]{.code-inline} (Creates a List)\
    -   [ DELETE https://api.twitter.com/2/lists/:id\
        ]{.code-inline} (Deletes a List)\
    -   [ PUT https://api.twitter.com/2/lists/:id\
        ]{.code-inline} (Updates a List)

#### Rate limits

+-----------------------------------+-----------------------------------+
| **Standard v1.1**                 | **Twitter API v2**                |
+===================================+===================================+
| [ /1.1/lists/create.json          | [ /2/lists ]{.code-inline}        |
| ]{.code-inline}                   |                                   |
|                                   | 300 requests per 15-minute window |
| none                              | with OAuth 1.0a User Context      |
+-----------------------------------+-----------------------------------+
| [ /1.1/lists/destroy.json         | [ /2/lists/:id ]{.code-inline}    |
| ]{.code-inline}                   |                                   |
|                                   | 300 requests per 15-minute window |
| none                              | with OAuth 1.0a User Context      |
+-----------------------------------+-----------------------------------+
| [ /1.1/lists/update.json          | [ /2/lists/:id ]{.code-inline}    |
| ]{.code-inline}                   |                                   |
|                                   | 300 requests per 15-minute window |
| none                              | with OAuth 1.0a User Context      |
+-----------------------------------+-----------------------------------+

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](https://developer.twitter.com/en/docs/apps) associated
with a [Project](https://developer.twitter.com/en/docs/projects) when
authenticating your requests. All Twitter API v1.1 endpoints can use
credentials from standalone Apps or Apps related to a project.

#### Request parameters

The following standard v1.1 request parameters have equivalents in
Twitter API v2:

**Create a List**\

  **Standard**                    **Twitter API v2**
  ------------------------------- -------------------------------
  [ name ]{.code-inline}          [ name ]{.code-inline}
  [ mode ]{.code-inline}          [ private ]{.code-inline}
  [ description ]{.code-inline}   [ description ]{.code-inline}

**Delete/Update a List**

  **Standard**                          **Twitter API v2**
  ------------------------------------- ----------------------
  [ owner_screen_name ]{.code-inline}   No equivalent
  [ owner_id ]{.code-inline}            No equivalent
  [ list_id ]{.code-inline}             [ id ]{.code-inline}
  [ slug ]{.code-inline}                No equivalent
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Please note:** Standard v1.1 parameters are passed as query
parameters, whereas the Twitter API v2 parameters are passed as body
parameters (for the POST endpoint) or path parameters (for the DELETE
and PUT endpoints).
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
