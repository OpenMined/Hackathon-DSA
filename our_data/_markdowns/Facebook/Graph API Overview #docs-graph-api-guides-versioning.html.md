Versioning - Graph API - Documentation - Meta for Developers

Graph API* Overview
* Get Started
* Batch Requests
* Debug Requests
* Handle Errors
* Field Expansion
* Secure Requests
* Resumable Upload API
* Changelog
* Features Reference
* Permissions Reference
* Reference
Platform Versioning
===================

Facebook's Platform supports versioning so that app builders can roll out changes over time. This document explains how SDKs and APIs affected by versions and how to use those versions in your requests.

Versioning
----------

Not all APIs and SDKs share the same versioning system. For example, the Graph API is versioned with a different pace and numbering compared to the Facebook SDK for iOS. All Facebook SDKs support the ability to interact with different versions of our APIs. Multiple versions of APIs or SDKs can exist at the same time with different functionality in each version.

### What is the latest Graph API Version?

The latest Graph API version is `v19.0`
### Why do we have versions?

The goal for having versioning is for developers building apps to be able to understand in advance when an API or SDK might change. They help with web development, but are critical with mobile development because a person using your app on their phone may take a long time to upgrade (or may never upgrade).

Each version will remain for at least 2 years from release giving you a solid timeline for how long your app will remain working, and how long you have to update it to newer versions.

### Version Schedules

Each version is guaranteed to operate for at least two years. **A version will no longer be usable two years after the date that the subsequent version is released.** For example, if API version v2.3 is released on March 25th, 2015 and API version v2.4 is released August 7th, 2015 then v2.3 would expire on August 7th, 2017, two years after the release of v2.4.

For APIs, once a version is no longer usable, any calls made to it will be defaulted to the next oldest, usable version. Here is a timeline example:

For SDKs, a version will always remain available as it is a downloadable package. However, the SDK may rely upon APIs or methods which no longer work, so you should assume an end-of-life SDK is no longer functional.

You can find specific information about our version timelines, changes, and release dates on our changelog page.

### Will everything remain completely unchanged in a version?

Facebook does reserve the right to make changes in any API in a short period of time for issues related to security or privacy. These changes don't happen often, but they do happen.

### What happens if I don't specify a version for an API?

We refer to an API call made without specifying a version as an **unversioned** call. For example, let's say the current version is v4.0. The call is as follows:

```
curl -i -X "https://graph.facebook.com/v4.0/{my-user-id}&access_token={access-token}"
```
The same unversioned call is as follows:

```
curl -i -X "https://graph.facebook.com/{my-user-id}&access_token={access-token}"
```
An unversioned call uses the version set in the app dashboard **Upgrade API Version** card under **Settings > Advanced**. In following example, the version set in the app dashboard is v2.10 and the unversioned call is equivalent to:

```
curl -i -X "https://graph.facebook.com/v2.10/{my-user-id}&access_token={access-token}"
```
We recommend you always specify the version where possible.

#### Limitations

* You can not make unversioned API calls to the Facebook JavaScript SDK.

### Can my app make calls to versions older than the current version?

You can specify older versions in your API calls as long as they are available and your app has made calls to that version. For example, if your app was created after v2.0 was released and makes calls using v2.0, it will be able to make calls to v2.0 until the version expires even after newer versions have been released. If you created your app after v2.0 but did not make any calls until v2.2, your app will not be able to make calls using v2.0 or to v2.1. It will only be able to make calls using v2.2 and newer versions.

### Marketing API Versioning

The Marketing API has its own versioning scheme. Both version numbers and their schedules are different from the Graph API's state of things.

Learn more about Marketing API VersioningMaking Versioned Requests
-------------------------

### Graph API

Whether core or extended, almost all Graph API endpoints are available through a versioned path. We've a full guide to using versions with the Graph API in our Graph API quickstart guide.

### Dialogs

Versioned paths aren't just true for API endpoints, they're also true for dialogs and social plugins. For example, if you want to generate the Facebook Login dialog for a web app, you can prepend a version number to the endpoint that generates the dialog:

```
https://www.facebook.com/v19.0/dialog/oauth?
  client_id={app-id}
  &redirect_uri={redirect-uri}
```
### Social Plugins

If you're using the HTML5 or xfbml versions of our social plugins, the version rendered will be determined by the version specified when you're initialising the JavaScript SDK.

If you're inserting an iframe or plain link version of one of our plugins, you'd prepend the version number to the source path of the plugin:

```
<iframe
  src="//www.facebook.com/v19.0/plugins/like.php?href=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;width&amp;layout=standard&amp;action=like&amp;show_faces=true&amp;share=true&amp;height=80&amp;appId=634262946633418" 
  scrolling="no" 
  frameborder="0" 
  style="border:none; overflow:hidden; height:80px;" 
  allowTransparency="true">
</iframe>
```
Making Versioned Requests from SDKs
-----------------------------------

If you're using the Facebook SDK for iOS, Android or JavaScript, making versioning calls is largely automatic. Note that this is distinct from each SDKs own versioning system.

### JavaScript

The JavaScript SDK can only use different API versions if you're using the `sdk.js` path.

If you're using `FB.init()` from the JavaScript SDK, you need to use the version parameter, like this:

```
FB.init({
  appId      : '{app-id}',
  version    : 'v19.0'
});
```
If you set the version flag in the init, then any calls to `FB.api()` will automatically have the version prepended to the path that's called. The same is true for any dialogs for Facebook Login that happen to get called. You will get the Facebook Login dialog for that version of the API.

If you need to, you can override a version by just prepending the version to the path of the endpoint in the `FB.api()` call.

### iOS

Each version of the Facebook SDK for iOS that's released is tied to the version that's available on the date of release. This means that if you're upgrading to a new SDK you're also upgrading to the latest API version as well (although you can manually specify any earlier, available API version with `[FBSDKGraphRequest initWithGraphPath]`). The API version is listed with the release of each version of the Facebook SDK for iOS.

Much like the JavaScript SDK, the version is prepended to any calls you make to the graph API through the Facebook SDK for iOS. For example, if `v2.7` was the most recent version of the API, the call `/me/friends` - used in the following code sample - will actually call `/v2.7/me/friends`:

```
[[[FBSDKGraphRequest alloc] initWithGraphPath:@"me/friends"
  parameters:@{@"fields": @"cover,name,start_time"}]
    startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        (...)
    }];
```
You can override the version of the call with `[FBSDKGraphRequestConnection overrideVersionPartWith]`.

### Android

Each version of the Facebook SDK for Android that's released is tied to the version that's available on the date of release. This means that if you're upgrading to a new SDK you're also upgrading to the latest API version as well (although you can manually specify any earlier, available API version with `GraphRequest.setVersion()`). The API version is listed with the release of each version of the Facebook SDK for Android.

Much like the JavaScript SDK, the version is prepended to any calls you make to the graph API through the Facebook SDK for Android. For example, if `v2.7` was the most recent version of the API, the call `/me` - used in the following code sample - will actually call `/v2.7/me`:

```
GraphRequest request = GraphRequest.newGraphPathRequest (
        accessToken,
        "/me/friends",
        new GraphRequest.GraphJSONObjectCallback() {
            @Override
            public void onCompleted(
                   JSONObject object,
                   GraphResponse response) {
                // Application code
            }
        });
Bundle parameters = new Bundle();
parameters.putString("fields", "id,name,link");
request.setParameters(parameters); 
request.executeAsync();
```
You can override the version of the call with `GraphRequest.setVersion()`.