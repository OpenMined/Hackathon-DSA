::: markdown-body
Welcome to the CrowdTangle API! You can use the CrowdTangle API to
access posts, the leaderboard and the link-checker. Please contact your
CrowdTangle representative for access. If you have access to the API,
you can locate your API token via your dashboard under Settings \> API
Access.

#### [![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIGhlaWdodD0iMTYiIHdpZHRoPSIxNiI+IDxwYXRoPiA8L3BhdGg+IDwvc3ZnPg==){.octicon .octicon-link}](#authentication){#user-content-authentication .anchor} Authentication

The CrowdTangle API expects the API token to be included either as a
custom header with the name ` x-api-token ` or as a ` token ` query
parameter.

::: {.snippet-clipboard-content .notranslate .position-relative .overflow-auto}
``` notranslate
// as a custom header
curl "https://api.crowdtangle.com/posts"
  -H "x-api-token: your-api-token"

// as a query parameter 
curl "https://api.crowdtangle.com/posts?token=your-api-token"
```
:::

#### [![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIGhlaWdodD0iMTYiIHdpZHRoPSIxNiI+IDxwYXRoPiA8L3BhdGg+IDwvc3ZnPg==){.octicon .octicon-link}](#making-a-request){#user-content-making-a-request .anchor} Making a Request

All requests to the CrowdTangle API are made via GET to
` https://api.crowdtangle.com/ ` . You must use https. Please visit the
[API Cheat
Sheet](https://help.crowdtangle.com/en/articles/3443476-api-cheat-sheet)
to understand how pagination works with our API.

Below are the available endpoints:

##### [![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIGhlaWdodD0iMTYiIHdpZHRoPSIxNiI+IDxwYXRoPiA8L3BhdGg+IDwvc3ZnPg==){.octicon .octicon-link}](#get-posts){#user-content-get-posts .anchor} [GET /posts](https://github.com/CrowdTangle/API/wiki/Posts)

##### [![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIGhlaWdodD0iMTYiIHdpZHRoPSIxNiI+IDxwYXRoPiA8L3BhdGg+IDwvc3ZnPg==){.octicon .octicon-link}](#get-post){#user-content-get-post .anchor} [GET /post](https://github.com/CrowdTangle/API/wiki/Posts#get-postid)

##### [![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIGhlaWdodD0iMTYiIHdpZHRoPSIxNiI+IDxwYXRoPiA8L3BhdGg+IDwvc3ZnPg==){.octicon .octicon-link}](#get-postssearch){#user-content-get-postssearch .anchor} [GET /posts/search](https://github.com/CrowdTangle/API/wiki/Search)

##### [![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIGhlaWdodD0iMTYiIHdpZHRoPSIxNiI+IDxwYXRoPiA8L3BhdGg+IDwvc3ZnPg==){.octicon .octicon-link}](#get-leaderboard){#user-content-get-leaderboard .anchor} [GET /leaderboard](https://github.com/CrowdTangle/API/wiki/Leaderboard)

##### [![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIGhlaWdodD0iMTYiIHdpZHRoPSIxNiI+IDxwYXRoPiA8L3BhdGg+IDwvc3ZnPg==){.octicon .octicon-link}](#get-links){#user-content-get-links .anchor} [GET /links](https://github.com/CrowdTangle/API/wiki/Links)

##### [![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIGhlaWdodD0iMTYiIHdpZHRoPSIxNiI+IDxwYXRoPiA8L3BhdGg+IDwvc3ZnPg==){.octicon .octicon-link}](#get-lists){#user-content-get-lists .anchor} [GET /lists](https://github.com/CrowdTangle/API/wiki/Lists)

##### [![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIGhlaWdodD0iMTYiIHdpZHRoPSIxNiI+IDxwYXRoPiA8L3BhdGg+IDwvc3ZnPg==){.octicon .octicon-link}](#postman-template){#user-content-postman-template .anchor} Postman Template

[Postman](https://www.getpostman.com/) is a free API management
software. [Click here to download a JSON file that you can import into
Postman (unzip the file to
access)](https://www.crowdtangle.com/assets/API-Demo.postman_collection.json.zip)
, and get a template for each endpoint. Please note that all parameters
may not be present in the template; please view the Github API
documentation to explore all parameter options.

Happy coding!
:::
