::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The v2 Tweet counts endpoint will eventually replace the [enterprise
Search API's counts
endpoint](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search)
. If you have code, apps, or tools that use an older version of a Tweet
counts endpoint and are considering migrating to the newer Twitter API
v2 endpoints, then this guide is for you.

This page contains two comparison tables:

-   [Recent Tweet counts](#recent)
-   [Full-archive Tweet counts](#full-archive)
-   [Filtering operator comparison](#operator)

### []{#recent} Recent Tweet counts comparison

The enterprise version of the Tweet counts endpoints allow you to pull
counts for either 30 days or from the full-archive. Therefore, the v2
recent Tweet counts endpoint, which looks at a 7 day time period, is not
a direct replacement for either of the aforementioned endpoints.

However, to help with comparisons, we will look at how the v2 recent
Tweet counts endpoint compares to the enterprise 30-day endpoint.

The following table compares the various types of recent Tweet counts
endpoints:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Description**                                                                        **Enterprise**                                            **Twitter API v2**
  -------------------------------------------------------------------------------------- --------------------------------------------------------- --------------------------------------------------------
  Host domain                                                                            [ https://gnip-api.twitter.com ]{.code-inline}            [ https://api.twitter.com ]{.code-inline}

  Endpoint path                                                                          [ /search/30day/accounts/:account_name/:label/counts.json [ /2/tweets/counts/recent ]{.code-inline}
                                                                                         ]{.code-inline}                                           

  [Authentication](https://developer.twitter.com/en/docs/authentication)                 Basic authentication                                      OAuth 2.0 Bearer Token

  Timestamp format                                                                       YYYYMMDDhhmm                                              YYYY-MM-DDTHH:mm:ssZ\
                                                                                                                                                   [ISO 8601 / RFC
                                                                                                                                                   3339](https://tools.ietf.org/html/rfc3339#section-5.6)

  Returns counts of Tweets that are no older than                                        31 days                                                   7 days

  HTTP methods supported                                                                 GET                                                       GET

  Default request rate limits                                                            20 requests per 1 sec, aggregated across search data and  180 requests per 15 min per user\
                                                                                         counts requests\                                          450 requests per 15 min per App
                                                                                         The per minute rate limit will vary by partner as         
                                                                                         specified in your contract.                               

  Supports filtering using                                                                                                                         ✔
  [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations)                                                                     

  Supports filtering using                                                                                                                         ✔
  [conversation_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id)                                                             

  JSON key name for Tweet data array                                                     [ results ]{.code-inline}                                 [ data ]{.code-inline}

  Time granularity                                                                       Day, hour, or minute                                      Day, hour, or minute

  Timezone                                                                               UTC                                                       UTC

  Request parameters for selecting time period                                           [ fromDate ]{.code-inline}\                               [ start_time ]{.code-inline}\
                                                                                         [ toDate ]{.code-inline}                                  [ end_time ]{.code-inline}

  Request parameters for navigating by Tweet ID                                                                                                    [ since_id ]{.code-inline}\
                                                                                                                                                   [ until_id ]{.code-inline}

  Requires the use of credentials from a [developer                                                                                                ✔
  App](https://developer.twitter.com/en/docs/apps) associated with a                                                                               
  [project](https://developer.twitter.com/en/docs/projects)                                                                                        
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 

[]{#full-archive} Full-archive Tweet counts comparison

The following table compares the various types of full-archive search
endpoints:

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Description                                                                            Enterprise                                                 Twitter API v2
  -------------------------------------------------------------------------------------- ---------------------------------------------------------- --------------------------------------------------------
  Host domain                                                                            [ https://gnip-api.twitter.com ]{.code-inline}             [ https://api.twitter.com ]{.code-inline}

  Endpoint path                                                                          [ /search/fullarchive/accounts/:account_name/:label/counts [ /2/tweets/counts/all ]{.code-inline}
                                                                                         ]{.code-inline}                                            

  [Authentication](https://developer.twitter.com/en/docs/authentication)                 Basic auth                                                 OAuth 2.0 Bearer Token

  Timestamp format                                                                       YYYYMMDDHHMM                                               YYYY-MM-DDTHH:mm:ssZ\
                                                                                                                                                    [ISO 8601 / RFC
                                                                                                                                                    3339](https://tools.ietf.org/html/rfc3339#section-5.6)

  Returns Tweet counts that are no older than                                            The full archive since March 2006                          The full archive since March 2006

  HTTP methods supported                                                                 GET\                                                       GET
                                                                                         POST                                                       

  Default request rate limits                                                            The per minute rate limit will vary by partner as          300 requests per 15 min per App\
                                                                                         specified in your contract.\                               1 request per 1 sec per App
                                                                                         20 requests per sec                                        

  Granularity                                                                            Day, hour, minute                                          Day, hour, minute

  Supports filtering using                                                                                                                          ✔
  [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations)                                                                      

  Supports filtering using                                                                                                                          ✔
  [conversation_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id)                                                              

  JSON key name for Tweet data array                                                     [ results ]{.code-inline}                                  [ data ]{.code-inline}

  Request parameters for selecting time period                                           [ fromDate ]{.code-inline}\                                [ start_time ]{.code-inline}\
                                                                                         [ toDate ]{.code-inline}                                   [ end_time ]{.code-inline}

  Request parameters for navigating by Tweet ID                                                                                                     [ since_id ]{.code-inline}\
                                                                                                                                                    [ until_id ]{.code-inline}

  JSON key name for pagination                                                           [ next ]{.code-inline}                                     [ meta.next_token ]{.code-inline}

  Request parameter for pagination                                                       [ next_token ]{.code-inline}                               [ next_token ]{.code-inline} or [ pagination_token
                                                                                                                                                    ]{.code-inline}

  Timezone                                                                               UTC                                                        UTC

  Requires the use of credentials from a [developer                                                                                                 ✔
  App](https://developer.twitter.com/en/docs/apps) associated with a                                                                                
  [Project](/en/docs/projects) that has [Academic Research                                                                                          
  access](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)                                                                   
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 

[]{#operator} Filtering operator comparison

The two different versions (enterprise, and v2) of Tweet counts differ
in which operators are available, and also have varying levels of
operator availability within each version, which are explained below.

Enterprise

-   There are no sub-tiers of enterprise operators. All enterprise
    operators are available to all enterprise users.

Twitter API v2

-   **Core:** These operators are available to any v2 user.
-   **Advanced:** These operators are only available to users that have
    been approved for Academic Research access.

You can learn more about each of these sets of operators in their
respective guides:

-   [Enterprise
    operators](/en/docs/twitter-api/enterprise/search-api/guides/operators)
-   [Twitter API v2
    operators](/en/docs/twitter-api/tweets/search/integrate/build-a-query)

Now that we understand these different operator levels within Twitter
API v2, here is the table that maps out operator availability for Tweet
counts (note that if the cell is left blank, the operator is not
available):

                     Enterprise   v2
  ------------------ ------------ ------------------------------------------
  keyword            Available    Core
  emoji              Available    Core
  "exact phrase"     Available    Core
  \#                 Available    Core
  \$                 Available    Advanced
  @                  Available    Core
  from:              Available    Core
  to:                Available    Core
  url:               Available    Core
  retweets_of:       Available    Core
  context:                        Core
  entity:                         Core - Only available with recent search
  conversation_id:                Core
  place:             Available    Advanced
  place_country:     Available    Advanced
  point_radius:      Available    Advanced
  bounding_box:      Available    Advanced
  is:retweet         Available    Core
  is:reply           Available    Core
  is:quote           Available    Core
  is:verified        Available    Core
  -is:nullcast       Available    Advanced
  has:hashtags       Available    Core
  has:cashtags       Available    Advanced
  has:links          Available    Core
  has:mentions       Available    Core
  has:media          Available    Core
  has:images         Available    Core
  has:videos         Available    Core
  has:geo            Available    Advanced
  lang:              Available    Core
  list:                           Advanced
  has:profile_geo    Available    
  profile_country    Available    
  profile_locality   Available    
  profile_region     Available    
  proximity          Available    
:::
:::
:::
:::
:::
:::
:::
:::
