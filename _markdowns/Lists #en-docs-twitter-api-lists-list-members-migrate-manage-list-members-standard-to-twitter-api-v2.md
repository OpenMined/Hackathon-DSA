::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
If you have been working with the standard v1.1 [POST
lists/members/create](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create)
and [POST
lists/members/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-destroy)
endpoints, the goal of this guide is to help you understand the
similarities and differences between the standard v1.1 and Twitter API
v2 manage List members endpoints.

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
manage List member endpoints, you can continue using the same
authentication method if you migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ POST https://api.twitter.com/1.1/lists/members/create.json\
        ]{.code-inline} (Adds a member to a specified List)
    -   [ POST https://api.twitter.com/1.1/lists/members/destroy.json\
        ]{.code-inline} (Removes a member from a specified List)
-   Twitter API v2 endpoint:
    -   [ POST https://api.twitter.com/2/lists/:id/members\
        ]{.code-inline} (Adds a member to a specified List)\
    -   [ DELETE https://api.twitter.com/2/lists/:id/members/:user_id\
        ]{.code-inline} (Removes a member from a specified List)

#### 

#### Rate limits

+-----------------------------------+-----------------------------------+
| **Standard v1.1**                 | **Twitter API v2**                |
+===================================+===================================+
| [ /1.1/lists/members/create.json  | [ /2/lists/:id/members            |
| ]{.code-inline}                   | ]{.code-inline}                   |
|                                   |                                   |
| none                              | 300 requests per 15-minute window |
|                                   | with OAuth 1.0a User Context      |
|                                   |                                   |
|                                   | 300 requests per 15-minute window |
|                                   | with OAuth 2.0 Authorization Code |
|                                   | with PKCE                         |
+-----------------------------------+-----------------------------------+
| [ /1.1/lists/members/destroy.json | [ /2/lists/:id/members/:user_id   |
| ]{.code-inline}                   | ]{.code-inline}                   |
|                                   |                                   |
| none                              | 300 requests per 15-minute window |
|                                   | with OAuth 1.0a User Context      |
|                                   |                                   |
|                                   | 300 requests per 15-minute window |
|                                   | with OAuth 2.0 Authorization Code |
|                                   | with PKCE                         |
+-----------------------------------+-----------------------------------+

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](https://developer.twitter.com/en/docs/apps) that is
associated with a
[Project](https://developer.twitter.com/en/docs/projects) when
authenticating your requests. All Twitter API v1.1 endpoints can use
credentials from standalone Apps or Apps related to a project.

#### 

#### Request parameters

The following standard v1.1 request parameters have equivalents in
Twitter API v2:

  **Standard v1.1**                     **Twitter API v2**
  ------------------------------------- ----------------------
  [ list_id ]{.code-inline}             [ id ]{.code-inline}
  [ slug ]{.code-inline}                No equivalent
  [ screen_name ]{.code-inline}         No equivalent
  [ owner_screen_name ]{.code-inline}   No equivalent
  [ owner_id ]{.code-inline}            No equivalent
:::
:::
:::
:::
:::
:::
:::
:::
