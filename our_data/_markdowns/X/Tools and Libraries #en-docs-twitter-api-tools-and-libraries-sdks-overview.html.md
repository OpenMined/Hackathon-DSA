
Overview | Docs | Twitter Developer Platform 

Overview

Introduction
------------

A software development kit (SDK) is a set of software tools and programs tailored for a specific platform or API. The purpose of an SDK is to build or extend functionality of applications by providing libraries or codebases that developers can use within their applications, efficiently and with minimal coding. This significantly speeds up the development process, saving time, money, and effort.

The Twitter Developer Platform now offers 2 official SDKs for those who develop in TypeScript/Javascript and Java. These will allow developers to build more effectively by eliminating the need to manually program the complexities around the Twitter API v2, utilizing the pre-built functions for all available v2 endpoints as well as simplifying the authentication process. As these are built and maintained by the Developer Platform team, they will always be up to date with future releases to the Twitter API v2

Since these SDKs wrap the Twitter API, you must have a developer account to authenticate requests using the credentials from a developer App, located within a Project.

#### Installing

* Java
* TypeScript

 Java

 TypeScript

There are a few ways to install the Java package (requires Java 1.8+)  

* Maven users - add this dependency to your project's POM file:

```
      <dependency>
  <groupId>com.twitter</groupId>
  <artifactId>twitter-api-java-sdk</artifactId>
  <version>1.1.4</version>
</dependency>
```

Code copied to clipboard

* Grade users - add this dependency to your project's build file:

                implementation "com.twitter:twitter-api-java-sdk:1.1.4"

* Others - first generate the JAR by running the following command

                mvn clean package

                Then manually install the following JARs:

                        target/twitter-api-java-sdk-1.1.4.jar

                        target/lib/\*.jar

This package supports Node.js 14+, to install, run the following command in the directory of the Node project:

                npm install twitter-api-sdk

#### Client basics

Import the classes (Java) and package (TypeScript) at the top of a working file to gain access to the authentication and library clients. In order to use the methods from the library client, authentication credentials must be passed, this could either be Bearer Token (App-only) or client id/client secret if authenticating with OAuth 2.0 user context.

Here are examples of how this would look:

 Java

 TypeScript

```
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

Code copied to clipboard

```
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

Code copied to clipboard

#### Authentication Flow

If you are using the application only option to authenticate the SDKs, you will only need to provide the token and the library client will be ready to use the endpoint methods right away. Keep in mind, application only tokens cannot be used on endpoints that require user context authentication.

OAuth 2.0 user context authentication requires a few extra steps after creating the auth client. 

* Generate authorization URL
* Authorize the application from the authorization URL
* Redirects to callback (this should be matching the callback URL set in the auth settings page in the Developer Portal).
* Parse code verifier to exchange for access token

The SDKs provide methods on the auth client that simplifies these steps. For a full example of how to make a request authenticating with OAuth 2.0 user context, check out the GitHub repositories.

* TypeScript
* Java

#### Endpoint methods

The methods provided within the library client are clearly named to correspond with every endpoint and all parameters are passed in as arguments.

Here is an example of Tweet lookup by ID:

 Java

 TypeScript

```
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

Code copied to clipboard

```
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

Code copied to clipboard

Developer policy and terms

Follow @XDevelopers

Subscribe to developer news

#### 
 X platform

* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app

#### 
 X Corp.

* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors

#### 
 Help

* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us

#### 
 Developer resources

* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms

#### 
 Business resources

* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy

 © 2024 X Corp.

Cookies

Privacy

Terms and conditions

**Did someone say … cookies?**  

 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.

* Accept all cookies
* Refuse non-essential cookies