::: {._4-u3 ._588p}
If you\'re using the Facebook SDK for iOS, Android or JavaScript, making
versioning calls is largely automatic. Note that this is distinct from
each SDKs own versioning system.

### JavaScript {#jssdkcalls}

The JavaScript SDK can only use different API versions if you\'re [using
the ` sdk.js ` path](/docs/apps/changelog/#v2_0_js_sdk) .

If you\'re using ` FB.init() ` from the [JavaScript
SDK](/docs/javascript) , you need to use the version parameter, like
this:

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
FB.init({ appId : '{app-id}', version : 'v18.0'
});
```

If you set the version flag in the init, then any calls to
[` FB.api() `](/docs/javascript/reference/FB.api) will automatically
have the version prepended to the path that\'s called. The same is true
for any dialogs for Facebook Login that happen to get called. You will
get the Facebook Login dialog for that version of the API.

If you need to, you can override a version by just prepending the
version to the path of the endpoint in the ` FB.api() ` call.

### iOS {#ioscalls}

Each version of the Facebook SDK for iOS that\'s released is tied to the
version that\'s available on the date of release. This means that if
you\'re upgrading to a new SDK you\'re also upgrading to the latest API
version as well (although you can manually specify any earlier,
available API version with
[` [FBSDKGraphRequest initWithGraphPath] `](/docs/reference/ios/current/class/FBSDKGraphRequest/#initWithGraphPath:parameters:)
). The API version is listed with the release of each version of the
[Facebook SDK for iOS](/docs/ios) .

Much like the JavaScript SDK, the version is prepended to any calls you
make to the graph API through the Facebook SDK for iOS. For example, if
` v2.7 ` was the most recent version of the API, the call
` /me/friends ` - used in the following code sample - will actually call
` /v2.7/me/friends ` :

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
[[[FBSDKGraphRequest alloc] initWithGraphPath:@"me/friends" parameters:@{@"fields": @"cover,name,start_time"}] startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) { (...) }];
```

You can override the version of the call with
[` [FBSDKGraphRequestConnection overrideVersionPartWith] `](/docs/reference/ios/current/class/FBSDKGraphRequestConnection/#overrideVersionPartWith:)
.

### Android {#androidcalls}

Each version of the Facebook SDK for Android that\'s released is tied to
the version that\'s available on the date of release. This means that if
you\'re upgrading to a new SDK you\'re also upgrading to the latest API
version as well (although you can manually specify any earlier,
available API version with ` GraphRequest.setVersion() ` ). The API
version is listed with the release of each version of the Facebook SDK
for Android.

Much like the JavaScript SDK, the version is prepended to any calls you
make to the graph API through the Facebook SDK for Android. For example,
if ` v2.7 ` was the most recent version of the API, the call ` /me ` -
used in the following code sample - will actually call ` /v2.7/me ` :

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
GraphRequest request = GraphRequest.newGraphPathRequest ( accessToken, "/me/friends", new GraphRequest.GraphJSONObjectCallback() { @Override public void onCompleted( JSONObject object, GraphResponse response) { // Application code } });
Bundle parameters = new Bundle();
parameters.putString("fields", "id,name,link");
request.setParameters(parameters); request.executeAsync();
```

You can override the version of the call with
` GraphRequest.setVersion() ` .
:::
