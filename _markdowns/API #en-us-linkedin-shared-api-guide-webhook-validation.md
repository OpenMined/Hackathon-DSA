::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

Webhooks allow you to receive real-time HTTP notifications for
subscribed events. This functionality is only available for applications
with an approved use case for webhooks.

## Webhook Registration and Validation

Notifications will only be sent to webhooks that are registered and
validated.

To begin, register your webhook in the \"Webhooks\" tab of your
application in the [developer
portal](https://www.linkedin.com/developers/apps) .

::: NOTE
Note

The Webhooks tab is only enabled for applications with a use case for
webhooks. For Lead Syncing use cases, webhook subscriptions must be
created via the Lead Notification Subscriptions API and cannot be
created via the UI.
:::

### Fields

  Field Name          Description                                                                                                                                                                                                                                                      Required
  ------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------
  applicationId       ID of the Developer Application being validated. Only sent for integrations with parent-child applications such as [Apply Connect](../../talent/apply-connect) . Indicates which application\'s ` clientSecret ` to use for generating the challenge response.   False
  challengeCode       Randomly generated type-4 UUID string created by LinkedIn.                                                                                                                                                                                                       True
  challengeResponse   Hex-encoded HMACSHA256 signature for the ` challengeCode ` using its ` clientSecret ` as the secret key. ` challengeResponse = Hex-encoded(HMACSHA256(challengeCode, clientSecret)) `                                                                            True

### Validating the Webhook Endpoint

LinkedIn validates the ownership of a webhook URL before it can be
registered by an application. The validation flow leverages the
application\'s ` clientSecret ` as the secret key along with the
universally-known HMACSHA256 algorithm to generate and validate the
application\'s response to a challenge code.

1.  Before initiating the validation flow, LinkedIn will generate a
    string that will act as the ` challengeCode ` .
2.  LinkedIn will use the ` challengeCode ` as a query parameter to make
    an HTTP GET to your webhook endpoint. Integrations using
    parent-child applications will also receive an ` applicationId `
    query parameter.

``` lang-http
GET https://webhooks.example.com/linkedin?challengeCode=890e4665-4dfe-4ab1-b689-ed553bceeed0
```

1.  Your application must compute the challengeResponse (Hex-encoded
    HMACSHA256 signature for the challengeCode) using its clientSecret
    as the secret key. If you received an applicationId query parameter
    in the previous step, use the clientSecret associated with the
    challenged application. Return both the challengeCode and
    challengeResponse in a JSON payload with a 200 OK status within 3
    seconds. See the example below. The response should have header
    \"content-type\" value set to \"application/json\".

```{=html}
<!-- -->
```
    challengeResponse = Hex-encoded(HMACSHA256(challengeCode, clientSecret))

``` lang-json
{
 "challengeCode" : "890e4665-4dfe-4ab1-b689-ed553bceeed0",
 "challengeResponse" : "27b1d19678542072a7f1d0ce845d0c78cec22567f413697e25648f44fa3d1514"
}
```

1.  On receiving the validation response, LinkedIn will verify by
    computing the challenge response and comparing it with the
    ` challengeResponse ` returned by the app.
2.  If the ` challengeResponse ` is successfully verified, then the
    webhook is ready to be used in subscriptions. If the verification
    fails, an error will be thrown with the message:
    ` This URL did not pass the security challenge check ` .

### Re-validation and Blocked Endpoints

Webhook endpoints will be periodically re-validated after the initial
validation every 2 hours. If the re-validation check fails 3 times in a
row, the endpoint will move to a blocked state where events will no
longer be sent.

Developers associated with that developer application will receive
warning emails for any failed validation attempts. After re-validation
checks fail 3 times in a row, an email will be sent notifying developers
that the webhook has been blocked. The endpoint will also show as
\"Blocked\" in the developer portal.

After resolving the issue, developers can manually kick off another
validation check from the developer portal.

## Requirements for Processing Notifications

Upon receiving notifications from LinkedIn, your webhook must fulfill
the following requirements:

The POST request sent by LinkedIn will include a header called
` X-LI-Signature ` . The value of this header is the HMACSHA256 hash of
the JSON-encoded string representation of the POST body prefixed by
` hmacsha256= ` and it is computed using your app's clientSecret. On
receiving the push event, you must compute the signature on the POST
body prefixed by ` hmacsha256= ` using the HMACSHA256 hashing algorithm
and your clientSecret. Discard the event if your computed value does not
match the value sent in the ` X-LI-Signature ` header.

#### Deduplicate notifications

A notification can occasionally be delivered multiple times to your
webhook. Your webhook must be able to deduplicate notifications using
the Notification ID included in the payload.

For each notification delivered to your webhook, it must return a 2xx
HTTP status code to indicate successful delivery of the notification to
your webhook. Any other response code returned will be treated by
LinkedIn as a failure.

#### Test with lambda/serverless functions on a cloud provider

We recommend testing webhooks processing using lambda/serverless
functions on a cloud provider.

::: NOTE
Note

ngrok URIs are not supported.
:::
:::
