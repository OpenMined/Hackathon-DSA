::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
A software development kit (SDK) is a set of software tools and programs
tailored for a specific platform or API. The purpose of an SDK is to
build or extend functionality of applications by providing libraries or
codebases that developers can use within their applications, efficiently
and with minimal coding. This significantly speeds up the development
process, saving time, money, and effort.
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
The Twitter Developer Platform now offers 2 official SDKs for those who
develop in TypeScript/Javascript and Java. These will allow developers
to build more effectively by eliminating the need to manually program
the complexities around the Twitter API v2, utilizing the pre-built
functions for all available v2 endpoints as well as simplifying the
authentication process. As these are built and maintained by the
Developer Platform team, they will always be up to date with future
releases to the Twitter API v2
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
:::

::: c01-rich-text-editor
::: is-table-default
Import the classes (Java) and package (TypeScript) at the top of a
working file to gain access to the authentication and library clients.
In order to use the methods from the library client, authentication
credentials must be passed, this could either be Bearer Token (App-only)
or client id/client secret if authenticating with OAuth 2.0 user
context.

Here are examples of how this would look:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t04-numbered-code-snippet
::: t04__container
::: {#t04__tab--0 .t04__tab .t04__tab--active}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 // Import classes:
import com.twitter.clientlib.ApiClient;
import com.twitter.clientlib.ApiException;
import com.twitter.clientlib.Configuration;
import com.twitter.clientlib.auth.*;
import com.twitter.clientlib.model.*;
import com.twitter.clientlib.TwitterCredentialsBearer;
import com.twitter.clientlib.api.TwitterApi;

// Instantiate library client
TwitterApi apiInstance = new TwitterApi();
 
// Instantiate auth credentials (App-only example)
TwitterCredentialsBearer credentials = new TwitterCredentialsBearer(System.getenv("APP-ONLY-ACCESS-TOKEN"));
 
// Pass credentials to library client
apiInstance.setTwitterCredentials(credentials);
    
```
:::
:::

::: {#t04__tab--1 .t04__tab}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 //Import package
import { Client, auth } from "twitter-api-sdk";
 
// Initialize auth client first
const authClient = new auth.OAuth2User({
 client_id: process.env.CLIENT_ID as string,
 client_secret: process.env.CLIENT_SECRET as string,
 callback: "YOUR-CALLBACK",
 scopes: ["tweet.read", "users.read", "offline.access"],
});

 // Pass auth credentials to the library client 
 const twitterClient = new Client(authClient);
    
```
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If you are using the application only option to authenticate the SDKs,
you will only need to provide the token and the library client will be
ready to use the endpoint methods right away. Keep in mind, application
only tokens cannot be used on endpoints that require user context
authentication.

OAuth 2.0 user context authentication requires a few extra steps after
creating the auth client.

-   Generate authorization URL
-   Authorize the application from the authorization URL
-   Redirects to callback (this should be matching the callback URL set
    in the auth settings page in the Developer Portal).
-   Parse code verifier to exchange for access token

The SDKs provide methods on the auth client that simplifies these steps.
For a full example of how to make a request authenticating with OAuth
2.0 user context, check out the GitHub repositories.
:::
:::

::: c01-rich-text-editor
::: is-table-default
The methods provided within the library client are clearly named to
correspond with every endpoint and all parameters are passed in as
arguments.

Here is an example of Tweet lookup by ID:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t04-numbered-code-snippet
::: t04__container
::: {#t04__tab--0 .t04__tab .t04__tab--active}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 String id = "1511757922354663425"; // String | A single Tweet ID.
Set<String> expansions = new HashSet<>(Arrays.asList("author_id")); // Set<String> | A comma separated list of fields to expand.
Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at", "lang", "context_annotations")); // Set<String> | A comma separated list of Tweet fields to display.
Set<String> userFields = new HashSet<>(Arrays.asList("created_at", "description", "name")); // Set<String> | A comma separated list of User fields to display.
 
try {
 SingleTweetLookupResponse result = apiInstance.tweets().findTweetById(id, expansions, tweetFields, userFields, null, null, null);
 System.out.println(result);
} catch (ApiException e) {
 System.err.println("Exception when calling TweetsApi#findTweetById");
 System.err.println("Status code: " + e.getCode());
 System.err.println("Reason: " + e.getResponseBody());
 System.err.println("Response headers: " + e.getResponseHeaders());
 e.printStackTrace();
}
    
```
:::
:::

::: {#t04__tab--1 .t04__tab}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 const lookupTweetById = await client.tweets.findTweetById(
  // Tweet ID
  "1511757922354663425",
  {
    // Optional parameters
    expansions: ["author_id"],
    "user.fields": ["created_at", "description", "name"],
  }
);
    
```
:::
:::
:::
:::
:::
:::
:::
