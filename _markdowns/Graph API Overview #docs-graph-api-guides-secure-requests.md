::: {._4-u3 ._588p}
Access tokens are portable. It\'s possible to take an access token
generated on a client by Meta\'s SDK, send it to a server and then make
calls from that server on behalf of the client. An access token can also
be stolen by malicious software on a person\'s computer or a man in the
middle attack. Then that access token can be used from an entirely
different system that\'s not the client and not your server, generating
spam or stealing data.

Calls from a server can be better secured by adding a parameter called
` appsecret_proof ` . The app secret proof is a sha256 hash of your
access token, using your app secret as the key. The app secret can be
found in your app dashboard in **Settings \> Basic** .

If you\'re using the official PHP SDK, the ` appsecret_proof ` parameter
is automatically added.

### Generate the Proof

The following code example is what the call looks like in PHP:

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
$appsecret_proof= hash_hmac('sha256', $access_token, $app_secret); 
```

### Add the Proof

You add the result as an ` appsecret_proof ` parameter to each call you
make:

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
curl \ -F 'access_token=<access_token>' \ -F 'appsecret_proof=<app secret proof>' \ -F 'batch=[{"method":"GET", "relative_url":"me"},{"method":"GET", "relative_url":"me/friends?limit=50"}]' \ https://graph.facebook.com
```

### Require the Proof

In the **Settings \> Advanced** section of your app dashboard in the
**Security** section, you enable **Require App Secret** . When this is
enabled, we will only allow API calls that include the
` appsecret_proof ` .
:::
