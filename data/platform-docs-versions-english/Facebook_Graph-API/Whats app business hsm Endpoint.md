WhatsApp Message Template
=========================

Represents a specific [message template](https://developers.facebook.com/docs/whatsapp/overview/messages#message-templates). Make the API call to the message template ID.

  

To find a message template ID, call ``https://graph.facebook.com/`v19.0`/{whatsapp-business-account-ID}/message_templates``.

  

For more information on how to use the API, see [WhatsApp Business Management API](https://developers.facebook.com/docs/whatsapp/business-account-management-api).

Reading
-------

Retrieves information about the message template

### Example

Requirements

* whatsapp\_business\_management permission
    
* whatsapp\_business\_messaging permission
    
* public\_profile permission
    
* WHATSAPP MESSAGE TEMPLATE ID
    
* USER ACCESS TOKEN
    

Request

cURLAndroid SDKObjective-C

    curl -i -X GET \
     "https://graph.facebook.com/LATEST-VERSION/WHATS-APP-MESSAGE-TEMPLATE-ID?access_token=USER-ACCESS-TOKEN"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/WHATS-APP-MESSAGE-TEMPLATE-ID",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/WHATS-APP-MESSAGE-TEMPLATE-ID"
               parameters:nil
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

Response

{
  "name": "shiptest",
  "components": \[
    {
      "type": "BODY",
      "text": "testing"
    }
  \],
  "language": "en\_US",
  "status": "REJECTED",
  "category": "TRANSACTIONAL",
  "id": "WHATS-APP-MESSAGE-TEMPLATE-ID"
}

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | ID  |
| `category`<br><br>enum | The category type of the message template<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `components`<br><br>[list<WhatsAppBusinessHSMWhatsAppHSMComponentGet>](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm-whats-app-hsm-component-get/) | An array of JSON objects describing the message template components.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `cta_url_link_tracking_opted_out`<br><br>bool | Optional boolean field for opting out/in of link tracking at template level |
| `language`<br><br>string | The language (and locale) of the element translation<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `message_send_ttl_seconds`<br><br>integer | Time to live for message template sent. If users are offline for more than TTL duration after message template is sent, message will be dropped from message queue and will not be delivered.<br><br>Only allowed for authentication message templates.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `name`<br><br>string | The message template name<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `previous_category`<br><br>enum | Previous category of the template. See [Template Categories](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates#categories).<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `quality_score`<br><br>[WhatsAppBusinessHSMWhatsAppBusinessHSMQualityScoreShape](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm-whats-app-business-hsm-quality-score-shape/) | Quality score of the HSM |
| `rejected_reason`<br><br>enum | The reason the message template was rejected<br><br>enum {ABUSIVE\_CONTENT, INVALID\_FORMAT, NONE, PROMOTIONAL, TAG\_CONTENT\_MISMATCH, SCAM} |
| `status`<br><br>enum | The status of the message template<br><br>enum {APPROVED, IN\_APPEAL, PENDING, REJECTED, PENDING\_DELETION, DELETED, DISABLED, PAUSED, LIMIT\_EXCEEDED}<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `sub_category`<br><br>enum | Sub category of the template<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

### Edges

| Edge | Description |
| --- | --- |
| [`compare`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/compare/) | compare |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80008 | There have been too many calls to this WhatsApp Business account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

Creating
--------

You can make a POST request to `message_templates` edge from the following paths:

* [`/{whats_app_business_account_id}/message_templates`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/)

When posting to this edge, a [WhatsAppMessageTemplate](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `allow_category_change`<br><br>boolean | Set to `true` to allow us to assign a category based on our [template guidelines](https://developers.facebook.com/docs/whatsapp/updates-to-pricing/new-template-guidelines) and the template's contents. This can prevent the template `status` from immediately being set to `REJECTED` upon creation due to miscategorization.<br><br>  <br>If omitted, template will not be auto-assigned a category and its status may be set to `REJECTED` if determined to be miscategorized.<br><br>  <br>See [Template Categories](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/#categories). |
| `category`<br><br>enum {UTILITY, MARKETING, AUTHENTICATION} | Template category. See [Template Categories](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/#categories).<br><br>Required |
| `components`<br><br>array<JSON object> | Array of components that make up the template. See [Template Components](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/components).<br><br>  <br>For types `HEADER`, `BODY`, `FOOTER`, `text` is required.<br><br>Required |
| `type`<br><br>enum {HEADER, BODY, FOOTER, BUTTONS, CAROUSEL, LIMITED\_TIME\_OFFER} | Component type.<br><br>Required |
| `format`<br><br>enum {TEXT, IMAGE, DOCUMENT, VIDEO, LOCATION} | Component format. |
| `text`<br><br>string | **Required for components with type `HEADER`,`BODY`, or `FOOTER`.**<br><br>  <br>Component text. |
| `buttons`<br><br>array<JSON object> | Button components to be used in the template. |
| `type`<br><br>enum {QUICK\_REPLY, URL, PHONE\_NUMBER, OTP, MPM, CATALOG, VOICE\_CALL} | Button type.<br><br>Required |
| `text`<br><br>string | Button text. |
| `url`<br><br>URI | url |
| `phone_number`<br><br>phone number string | phone\_number |
| `example`<br><br>array<string> | example |
| `flow_id`<br><br>int64 | flow\_id |
| `zero_tap_terms_accepted`<br><br>boolean | zero\_tap\_terms\_accepted |
| `example`<br><br>JSON object | Placeholder examples. Templates will not be approved without examples. |
| `header_text`<br><br>array<string> | header\_text |
| `body_text`<br><br>array<array<string>> | body\_text |
| `header_handle`<br><br>array<string> | header\_handle |
| `language`<br><br>string | Template [location and locale code](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/supported-languages).<br><br>Required |
| `name`<br><br>string | Template name.<br><br>Required |
| `sub_category`<br><br>enum {CUSTOM, ORDER\_DETAILS, ORDER\_STATUS} | Sub category of the template |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`id`: numeric string,

`status`: enum,

`category`: enum,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80008 | There have been too many calls to this WhatsApp Business account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 192 | Invalid phone number |
| 200 | Permissions error |
| 200002 | HSM Template creation failed |

Updating
--------

You can update a [WhatsAppMessageTemplate](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/) by making a POST request to [`/{whats_app_message_template_id}`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/).

### Parameters

| Parameter | Description |
| --- | --- |
| `category`<br><br>enum {UTILITY, MARKETING, AUTHENTICATION} | category |
| `components`<br><br>array<JSON object> | The array containing all the content of the message template |
| `type`<br><br>enum {HEADER, BODY, FOOTER, BUTTONS, CAROUSEL, LIMITED\_TIME\_OFFER} | Component type.<br><br>Required |
| `format`<br><br>enum {TEXT, IMAGE, DOCUMENT, VIDEO, LOCATION} | Component format. |
| `text`<br><br>string | **Required for components with type `HEADER`,`BODY`, or `FOOTER`.**<br><br>  <br>Component text. |
| `buttons`<br><br>array<JSON object> | Button components to be used in the template. |
| `type`<br><br>enum {QUICK\_REPLY, URL, PHONE\_NUMBER, OTP, MPM, CATALOG, VOICE\_CALL} | Button type.<br><br>Required |
| `text`<br><br>string | Button text. |
| `url`<br><br>URI | url |
| `phone_number`<br><br>phone number string | phone\_number |
| `flow_id`<br><br>int64 | flow\_id |
| `zero_tap_terms_accepted`<br><br>boolean | zero\_tap\_terms\_accepted |
| `message_send_ttl_seconds`<br><br>int64 | Time to live for message template sent. If users are offline for more than TTL duration after message template is sent, message will be dropped from message queue and will not be delivered.<br><br>Only allowed for authentication message templates. |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80012 | There have been too many calls to this message template. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 192 | Invalid phone number |

Deleting
--------

You can dissociate a [WhatsAppMessageTemplate](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/) from a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a DELETE request to [`/{whats_app_business_account_id}/message_templates`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/).

### Parameters

| Parameter | Description |
| --- | --- |
| `hsm_id`<br><br>whatsapp business hsm ID | ID of template to be deleted. Required if deleting a template by ID. |
| `name`<br><br>string | Name of template to be deleted.<br><br>Required |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[WhatsApp Business Platform](https://developers.facebook.com/docs/whatsapp) | [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api) | [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises) | [Business Management API](https://developers.facebook.com/docs/whatsapp/business-management-api)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Whats App Message Template Compare
==================================

Compare template send counts and block ratios. See [Template Comparison](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/template-comparison).

Reading
-------

Compare the WhatsApp message template's send count and block ratio to another WhatsApp message template's send count and block ratio.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/guides/access-tokens) | [User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#user-access-tokens) or [System User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#user-access-tokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [business\_management](https://developers.facebook.com/docs/permissions/reference/business_management) |

### Limitations

* Only two templates can be compared at a time.
* Templates must have been sent at least 1,000 times in the queries specified timeframe.
* Timeframes are limited to 7, 30, 60 and 90 day lookbacks from the time of the request.

### Request Syntax

GET /<WHATSAPP\_MESSAGE\_TEMPLATE\_ID>/compare
  ?template\_ids=\[<TEMPLATE\_IDS\]
  &start=<START>
  &end=<END>

### Response

{
  "data": \[
    {
      "metric": "BLOCK\_RATE",
      "type": "RELATIVE",
      "order\_by\_relative\_metric": \[<ORDER\_BY\_RELATIVE\_METRIC>\]
    },
    {
      "metric": "MESSAGE\_SENDS",
      "type": "NUMBER\_VALUES",
      "number\_values": \[<NUMBER\_VALUES>\]
    },
    {
      "metric": "TOP\_BLOCK\_REASON",
      "type": "STRING\_VALUES",
      "string\_values": \[<STRING\_VALUES>\]
    }
  \]
}

### Sample Request

curl -X GET 'https://graph.facebook.com/`v19.0`/5289179717853347/compare?template\_ids=\[1533406637136032\]&start=1674844791182&end=1674845395982' \\
-H 'Authorization: Bearer EAAJB...'

### Sample Response

{
  "data": \[
    {
      "metric": "BLOCK\_RATE",
      "type": "RELATIVE",
      "order\_by\_relative\_metric": \[
        "1533406637136032",
        "5289179717853347"
      \]
    },
    {
      "metric": "MESSAGE\_SENDS",
      "type": "NUMBER\_VALUES",
      "number\_values": \[
        {
          "key": "5289179717853347",
          "value": 1273
        },
        {
          "key": "1533406637136032",
          "value": 1042
        }
      \]
    },
    {
      "metric": "TOP\_BLOCK\_REASON",
      "type": "STRING\_VALUES",
      "string\_values": \[
        {
          "key": "5289179717853347",
          "value": "UNKNOWN\_BLOCK\_REASON"
        },
        {
          "key": "1533406637136032",
          "value": "UNKNOWN\_BLOCK\_REASON"
        }
      \]
    }
  \]
}

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bwhats-app-message-template-id%7D%2Fcompare&version=v19.0)

    GET /v19.0/{whats-app-message-template-id}/compare HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{whats-app-message-template-id}/compare',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{whats-app-message-template-id}/compare",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{whats-app-message-template-id}/compare",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{whats-app-message-template-id}/compare"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `end`<br><br>datetime/timestamp | UNIX timestamp indicating end of timeframe. Timeframes are limited to 7, 30, 60 and 90 day lookbacks from the time of the request. To define a timeframe, set your end date to the current time as a UNIX timestamp, then subtract the number of days for your desired timeframe, in seconds, from that value:<br><br>Required |
| `start`<br><br>datetime/timestamp | UNIX timestamp indicating start of timeframe. Timeframes are limited to 7, 30, 60 and 90 day lookbacks from the time of the request. To define a timeframe, set your end date to the current time as a UNIX timestamp, then subtract the number of days for your desired timeframe, in seconds, from that value:<br><br>Required |
| `template_ids`<br><br>array<EntWhatsAppBusinessHSM ID> | ID of the WhatsApp Message Template to compare the target to.<br><br>Required |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [WhatsAppBusinessHSMComparison](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm-comparison/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)