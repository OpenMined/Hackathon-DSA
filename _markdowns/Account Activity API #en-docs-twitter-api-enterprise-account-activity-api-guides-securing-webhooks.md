::: is-table-default
Twitter\'s webhook-based APIs provide two methods for confirming the
security of your webhook server:

1.  The challenge-response checks enable Twitter to confirm the
    ownership of the web app receiving webhook events.
2.  The signature header in each POST request enables you to confirm
    that Twitter is the source of the incoming webhooks.

### Challenge-Response Checks

In order to verify that you are both the owner of the app and the
webhook URL, Twitter will perform a Challenge-Response Check (CRC),
which is not to be confused with a cyclic redundancy check. When a CRC
is sent, Twitter will make a GET request of your web app with a ;
*` crc_token `* parameter. When that request is received, your web app
needs to build an encrypted ` response_token ` based on the
*` crc_token `* parameter and your app\'s Consumer Secret (details
below). The [ response_token ]{.code-inline} must be encoded in JSON
(see example below) and returned within three seconds. When successful,
a webhook ` id ` will be returned.

A CRC will be sent when you register your webhook URL, so implementing
your CRC response code is a fundamental first step. Once your webhook is
established, Twitter will trigger a CRC roughly every 24 hours from the
last time we received a successful response. Your app can also trigger a
CRC when needed by making a PUT request with your webhook ` id ` .
Triggering a CRC is useful as you develop your webhook application,
after deploying new code and restarting your service.

The *` crc_token `* should be expected to change for each incoming CRC
request and should be used as the message in the calculation, where your
Consumer Secret is the key.

In the event that the response is not posted within 3 seconds or becomes
invalid, events will cease to be sent to the registered webhook.

#### The CRC request will occur: 

-   When a webhook URL is registered.
-   Approximately *hourly* to validate your webhook URL.
-   You can manually trigger a CRC by making a PUT request. As you
    develop your webhook client, you should plan on manually triggering
    the CRC as you develop your CRC response.\

#### Response requirements:

-   A base64 encoded HMAC SHA-256 hash created from the ` crc_token `
    and your app Consumer Secret
-   Valid response_token and JSON format.
-   Latency less than 3 seconds.
-   200 HTTP response code.\

#### Language-specific HMAC libraries:

-   [Java/Scala](https://docs.oracle.com/javase/8/docs/api/index.html?javax/crypto/Mac.html)
-   [Ruby](http://ruby-doc.org/stdlib-2.1.0/libdoc/openssl/rdoc/OpenSSL/HMAC.html)
-   [Node.js](https://nodejs.org/api/crypto.html#crypto_class_hmac)
-   [Python\
    ](https://docs.python.org/2/library/hmac.html)

#### Example response token generation in Python:

The following defines a route in a Python 2.7 Flask webapp that will
respond to the challenge response check correctly.

    import base64
    import hashlib
    import hmac
    import json


    # Defines a route for the GET request
    @app.route('/webhooks/twitter', methods=['GET'])
    def webhook_challenge():

      # creates HMAC SHA-256 hash from incomming token and your consumer secret
      sha256_hash_digest = hmac.new(TWITTER_CONSUMER_SECRET, msg=request.args.get('crc_token'), digestmod=hashlib.sha256).digest()

      # construct response data with base64 encoded hash
      response = {
        'response_token': 'sha256=' + base64.b64encode(sha256_hash_digest)
      }

      # returns properly formatted json response
      return json.dumps(response)

#### 

#### Example JSON response: 

With the route defined as above your webapp should return a response
similar to below when navigating to
https://your-app-domain/webhooks/twitter?crc_token=foo in your web
browser.

    {
      "response_token": "sha256=x0mYd8hz2goCTfcNAaMqENy2BFgJJfJOb4PdvTffpwg="
    }

#### 

#### Other examples:

-   [HERE](https://github.com/twitterdev/account-activity-dashboard/blob/master/helpers/security.js)
    is an example CRC response method written in Node/JS.
-   [HERE](https://github.com/twitterdev/SnowBotDev/blob/master/app/controllers/snow_bot_dev_app.rb)
    is an example CRC response method written in Ruby (see the
    *generate_crc_response* and the /GET route that receives CRC
    events).

### Optional signature header validation

When receiving a POST request from Twitter, sending a GET request to
create a webhook, or sending a GET request to perform a manual CRC, a
hash signature will be passed in the headers as
x-twitter-webhooks-signature. This signature can be used to validate the
source of the data is Twitter. The POST hash signature starts with
sha256= indicating the use of HMAC SHA-256 to encrypt your Twitter App
Consumer Secret and payload. The GET hash is calculated from the query
parameter string crc_token=\$token&nonce=\$nonce.

**Steps to validate a request**

1.  Create a hash using your consumer secret and incoming payload body.
2.  Compare created hash with the base64
    encoded x-twitter-webhooks-signature value. Use a method like
    [compare_digest](https://docs.python.org/2/library/hmac.html) to
    reduce the vulnerability to timing attacks.

### Additional security guidelines

The following are additional security guidelines to consider for your
web application. Not having these guidelines implemented will not
prevent your webhook from functioning, but are highly reccomended by the
Twitter Information Security team. If you are unfamilair with the below
recommendations consult with your server administrator.

#### Twitter aggregate network blocks 

For added security you may wish to add the following aggregate network
blocks to an allowlist:

-   199.59.148.0/22
-   199.16.156.0/22
-   192.133.77.0/26
-   64.63.15.0/24\
-   64.63.31.0/24
-   64.63.47.0/24
-   202.160.128.0/24
-   202.160.129.0/24
-   202.160.130.0/24

#### Recommended server configurations

-   \"A\" rating on [ssllabs.com](http://ssllabs.com/) test
-   **Enable TLS 1.2**
-   Enable Forward Secrecy
-   Turn off SSLv2
-   Turn off SSLv3 (because of POODLE)
-   Turn off TLS 1.0
-   Turn off TLS 1.1
-   Turn off TLS Compression
-   Turn off Session Tickets unless you rotate session ticket keys.
-   Set the "ssl_prefer_server_ciphers" or "SSLHonorCipherOrder" option
    in the SSL Configuration "on".
-   Ensure the list of ciphers is a modern list such as:\
    ` ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES128-SHA256:AES128-SHA:AES256-GCM-SHA384:AES256-SHA256:AES256-SHA:ECDHE-RSA-DES-CBC3-SHA:DES-CBC3-SHA `\

### 

### Next steps
:::
