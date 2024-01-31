WhatsApp Business Account
=========================

[](#)

Represents a specific [WhatsApp Business Account (WABA)](https://www.facebook.com/business/help/1499554293524119). Make the API call to the WABA ID.

  

To find the ID of a WhatsApp Business Account, go to [**Business Manager**](https://business.facebook.com/) > **Business Settings** > **Accounts** > **WhatsApp Business Accounts**. Find the account you want to use and click on it. A panel opens, with information about the account, including the ID.

  

For more information on how to use the API, see [WhatsApp Business Management API](https://developers.facebook.com/docs/whatsapp/business-account-management-api).

The following API calls are subject to [Business Use Case Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#wa-biz-api):

* `GET`, `POST`, and `DELETE` calls to `/{whats-app-business-account-id}/assigned_users`
* `GET` calls to `/{whats-app-business-account-id}`

[](#)

Reading
-------

Returns the account information of a WhatsApp Business Account

### Example

Requirements

* whatsapp\_business\_management permission
    
* whatsapp\_business\_messaging permission
    
* public\_profile permission
    
* WhatsApp Business Account (WABA) ID
    
* USER ACCESS TOKEN
    

Request

cURLAndroid SDKObjective-C

    curl -i -X GET \
     "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID?access_token=USER-ACCESS-TOKEN"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/WHATSAPP-BUSINESS-ACCOUNT-ID",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID"
               parameters:nil
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

Response

{
  "id": "WHATSAPP-BUSINESS-ACCOUNT-ID",
  "name": "Test WhatsApp Business Account",
  "timezone\_id": "1",
  "message\_template\_namespace": "MESSAGE-TEMPLATE-NAMESPACE"
}

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | ID of the WhatApp Business Account.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `account_review_status`<br><br>enum | Status from account review process. |
| `analytics`<br><br>[WABAAnalytics](https://developers.facebook.com/docs/graph-api/reference/waba-analytics/) | Used to designate which analytics metrics you want returned. See [Analytics](https://developers.facebook.com/docs/whatsapp/business-management-api/analytics). |
| `business_verification_status`<br><br>enum | Current status of business verification of Meta Business Account which owns this WhatsApp Business Account |
| `country`[](#)<br><br>string | country of the WhatsApp Business Account's owning Meta Business account |
| `currency`<br><br>string | The currency in which the payment transactions for the WhatsApp Business Account will be processed<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `is_enabled_for_insights`<br><br>bool | If `true`, indicates the WhatsApp Business Account enabled template analytics. See [Analytics](https://developers.facebook.com/docs/whatsapp/business-management-api/analytics). |
| `message_template_namespace`<br><br>string | Namespace string for the message templates that belong to the WhatsApp Business Account<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `name`<br><br>string | User-friendly name to differentiate WhatsApp Business Accounts<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `on_behalf_of_business_info`<br><br>WABAOnBehalfOfComputedInfo | The "on behalf of" information for the WhatsApp Business Account |
| `ownership_type`[](#)<br><br>enum | Ownership type of the WhatsApp Business Account |
| `primary_funding_id`<br><br>numeric string | Primary funding ID for the WhatsApp Business Account paid service |
| `purchase_order_number`<br><br>string | The purchase order number supplied by the business for payment management purposes |
| `timezone_id`<br><br>string | The timezone of the WhatsApp Business Account<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

### Edges

| Edge | Description |
| --- | --- |
| [`conversation_analytics`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/conversation_analytics/) | Analytics data of the WhatsApp Business Account with conversation based pricing |
| [`dcc_config`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/dcc_config/) | Returns a list of DCC configs |
| [`message_template_previews`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_template_previews/) | Retrieves a preview of a message template based on the provided configuration |
| [`message_templates`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/) | Message templates that belong to the WhatsApp Business Account |
| [`phone_numbers`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/phone_numbers/) | The phone numbers that belong to the WhatsApp Business Account |
| [`product_catalogs`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/product_catalogs/) | product\_catalogs |
| [`subscribed_apps`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/subscribed_apps/) | List of apps that are subscribed to webhooks updates for this WABA |
| [`template_performance_metrics`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/template_performance_metrics/) | template\_performance\_metrics |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 131009 | Parameter value is not valid |
| 200 | Permissions error |
| 80008 | There have been too many calls to this WhatsApp Business account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 131031 | Business Account locked |
| 131000 | Something went wrong |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can update a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a POST request to [`/{whats_app_business_account_id}/assigned_users`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/assigned_users/).

### Parameters

| Parameter | Description |
| --- | --- |
| `tasks`<br><br>array<enum {MANAGE, DEVELOP, MANAGE\_TEMPLATES, MANAGE\_PHONE, VIEW\_COST, MANAGE\_EXTENSIONS, VIEW\_PHONE\_ASSETS, MANAGE\_PHONE\_ASSETS, VIEW\_TEMPLATES}> | Permissions on WhatsApp Business Account<br><br>Required |
| `user`<br><br>UID | Business user ID<br><br>Required |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Deleting
--------

You can dissociate a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) from a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a DELETE request to [`/{whats_app_business_account_id}/assigned_users`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/assigned_users/).

### Parameters

| Parameter | Description |
| --- | --- |
| `user`<br><br>UID | Business user ID<br><br>Required |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Supported values
----------------

### Currencies

Supported values for currency codes can be found in [currencies](https://developers.facebook.com/docs/marketing-api/currencies).

### Time Zones

Supported values for time zones can be found in [timezone ids](https://developers.facebook.com/docs/marketing-api/reference/ad-account/timezone-ids/v10.0).

[](#)

Whats App Business Account Assigned Users
=========================================

[](#)

Represents users assigned to a specific WhatsApp Business Account (WABA).

  

To find the ID of a WhatsApp Business Account, go to [**Business Manager**](https://business.facebook.com/) > **Business Settings** > **Accounts** > **WhatsApp Business Accounts**. Find the account you want to use and click on it. A panel opens, with information about the account, including the ID.

[](#)

Reading
-------

Returns the WhatsApp Business Account's assigned users.

### Example

Requirements

* whatsapp\_business\_management permission
    
* whatsapp\_business\_messaging permission
    
* public\_profile permission
    
* BUSINESS ID (also referred to as BUSINESS MANAGER ID in Business Settings)
    
* WhatsApp Business Account (WABA) ID
    
* USER ACCESS TOKEN
    

Request

cURLAndroid SDKObjective-C

    curl -i -X GET \
     "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID/assigned_users?
            business=BUSINESS-ID&
            access_token=USER-ACCESS-TOKEN"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/WHATSAPP-BUSINESS-ACCOUNT-ID/assigned_users",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    Bundle parameters = new Bundle();
    parameters.putString("business", "BUSINESS-ID");
    request.setParameters(parameters);
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID/assigned_users"
               parameters:@{ @"business": @"BUSINESS-ID",}
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

Response

{
  "data": \[
    {
      "id": "ASSIGNED-USER-ID",
      "name": " ",
      "tasks": \[
        "MANAGE"
      \]
    }
  \],
  "paging": {
    "cursors": {
      "before": "BEFORE-CURSOR",
      "after": "AFTER-CURSOR"
    }
  }
}

### Parameters

| Parameter | Description |
| --- | --- |
| `business`<br><br>business id ID | business<br><br>Required |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of AssignedUser nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `tasks`<br><br>list<string> | Tasks the user has on the WABA<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | Total count |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can update a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a POST request to [`/{whats_app_business_account_id}/assigned_users`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/assigned_users/).

### Parameters

| Parameter | Description |
| --- | --- |
| `tasks`<br><br>array<enum {MANAGE, DEVELOP, MANAGE\_TEMPLATES, MANAGE\_PHONE, VIEW\_COST, MANAGE\_EXTENSIONS, VIEW\_PHONE\_ASSETS, MANAGE\_PHONE\_ASSETS, VIEW\_TEMPLATES}> | Permissions on WhatsApp Business Account<br><br>Required |
| `user`<br><br>UID | Business user ID<br><br>Required |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Deleting
--------

You can dissociate a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) from a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a DELETE request to [`/{whats_app_business_account_id}/assigned_users`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/assigned_users/).

### Parameters

| Parameter | Description |
| --- | --- |
| `user`<br><br>UID | Business user ID<br><br>Required |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Whats App Business Account Dcc Config
=====================================

[](#)

Reading
-------

return a list of DCC configs

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bwhats-app-business-account-id%7D%2Fdcc_config&version=v18.0)

    GET /v18.0/{whats-app-business-account-id}/dcc_config HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{whats-app-business-account-id}/dcc_config',
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
        "/{whats-app-business-account-id}/dcc_config",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{whats-app-business-account-id}/dcc_config",
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
                                   initWithGraphPath:@"/{whats-app-business-account-id}/dcc_config"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of WhatsAppBusinessDirectConnectionExternalConfig nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Whats App Business Account Message Template Previews
====================================================

[](#)

Represents a collection of WhatsApp authentication template previews. See [Authentication Templates](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates) for additional information about authentication templates.

[](#)

Reading
-------

Get previews of [authentication template](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates) text in various language, based on parameters include in the request.

### Requirements

| Type | Description |
| --- | --- |
| Access Tokens | [User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#user-access-tokens) or [System User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens) |
| Permissions | [whatsapp\_business\_management](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_management) |

### Request Syntax

GET /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID\>/message\_template\_previews
  ?category\=AUTHENTICATION,
  &language\=<LANGUAGE\>,
  &add\_security\_recommendation\=<ADD\_SECURITY\_RECOMMENDATION\>,
  &code\_expiration\_minutes\=<CODE\_EXPIRATION\_MINUTES\>,
  &button\_types\=<BUTTON\_TYPES\>

### Response

A list of [WhatsApp Business Account Message Template Preview](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account-message-template-preview/) nodes.

### Sample Request

curl 'https://graph.facebook.com/`v18.0`/102290129340398/message\_template\_previews?category=AUTHENTICATION&languages=en\_US%2Ces\_ES&add\_security\_recommendation=true&code\_expiration\_minutes=10&button\_types=OTP' \\
\-H 'Authorization: Bearer EAAJB...'

### Sample Response

{
  "data": \[
    {
      "body": "\*{{1}}\* is your verification code. For your security, do not share this code.",
      "buttons": \[
        {
          "autofill\_text": "Autofill",
          "text": "Copy code"
        }
      \],
      "footer": "This code expires in 10 minutes.",
      "language": "en\_US"
    },
    {
      "body": "Tu código de verificación es \*{{1}}\*. Por tu seguridad, no lo compartas.",
      "buttons": \[
        {
          "autofill\_text": "Autocompletar",
          "text": "Copiar código"
        }
      \],
      "footer": "Este código caduca en 10 minutos.",
      "language": "es\_ES"
    }
  \]
}

### Parameters

| Parameter | Description |
| --- | --- |
| `add_security_recommendation`<br><br>boolean | Default value: `false`<br><br>  <br>Set to `true` if you want the security recommendation body string included in the response.<br><br>  <br>If omitted, the security recommendation string will not be included. |
| `button_types`<br><br>array<enum {OTP}> | Default value: `[]`<br><br>  <br>Comma-separated list of strings indicating button type.<br><br>  <br>If included, the response will include the button text for each button in the response.<br><br>  <br>For authentication templates, this value must be `OTP`. |
| `category`<br><br>enum {AUTHENTICATION} | The category of the message template. Set to `AUTHENTICATION` for authentication templates.<br><br>Required |
| `code_expiration_minutes`<br><br>int64 | For authentication templates, set to an integer if you want the code expiration footer string included in the response.<br><br>  <br>If omitted, the code expiration footer string will not be included.<br><br>  <br>Value indicates number of minutes until code expires.<br><br>  <br>Minimum `1`, maximum `90`. |
| `languages`<br><br>array<string> | Default value: `["af","sq","ar","az","bn","bg","ca","zh_CN","zh_HK","zh_TW","hr","cs","da","nl","en","en_GB","en_US","et","fil","fi","fr","ka","de","el","gu","ha","he","hi","hu","id","ga","it","ja","kn","kk","ko","ky_KG","lo","lv","lt","mk","ml","ms","mr","nb","fa","pl","pt_BR","pt_PT","pa","ro","ru","rw_RW","sr","sk","sl","es","es_AR","es_ES","es_MX","sw","sv","ta","te","th","tr","uk","ur","uz","vi","zu"]`<br><br>  <br>Comma-separated list of language and locale codes of language versions you want returned.<br><br>  <br>If omitted, versions of all supported languages will be returned. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [WhatsAppBusinessAccountMessageTemplatePreview](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account-message-template-preview/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Whats App Business Account Message Templates
============================================

[](#)

Represents a collection of templates on a [WhatsApp Business Account](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/). See [Templates](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates).

[](#)

Reading
-------

Get a list of templates on a WhatsApp Business Account.

### Requirements

| Type | Description |
| --- | --- |
| Access Tokens | [User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#user-access-tokens) or [System User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens) |
| Permissions | [whatsapp\_business\_management](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_management) |

### Request Syntax

GET /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID\>/message\_templates
  ?category\=<CATEGORY\>,
  &content\=<CONTENT\>,
  &language\=<LANGUAGE\>,
  &name\=<NAME\>,
  &name\_or\_content\=<NAME\_OR\_CONTENT\>,
  &quality\_score\=<QUALITY\_SCORE\>,
  &status\=<STATUS\>

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | WhatsApp Business Account ID. |

### Response

A list of [WhatsApp Message Template](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/) nodes.

### Sample Request

curl 'https://graph.facebook.com/v16.0/102290129340398/message\_templates?category=utility' \\
\-H 'Authorization: Bearer EAAJB...'

### Sample Response

{
  "data": \[
    {
      "name": "order\_delivery\_update",
      "components": \[
        {
          "type": "HEADER",
          "format": "LOCATION"
        },
        {
          "type": "BODY",
          "text": "Good news {{1}}! Your order #{{2}} is on its way to the location above. Thank you for your order!",
          "example": {
            "body\_text": \[
              \[
                "Mark",
                "566701"
              \]
            \]
          }
        },
        {
          "type": "FOOTER",
          "text": "To stop receiving delivery updates, tap the button below."
        },
        {
          "type": "BUTTONS",
          "buttons": \[
            {
              "type": "QUICK\_REPLY",
              "text": "Stop Delivery Updates"
            }
          \]
        }
      \],
      "language": "en\_US",
      "status": "APPROVED",
      "category": "UTILITY",
      "id": "1667192013751005"
    },
    ...
  \],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MjQZD"
    }
  }
}

### Parameters

| Parameter | Description |
| --- | --- |
| `category`<br><br>array<enum {ACCOUNT\_UPDATE, PAYMENT\_UPDATE, PERSONAL\_FINANCE\_UPDATE, SHIPPING\_UPDATE, RESERVATION\_UPDATE, ISSUE\_RESOLUTION, APPOINTMENT\_UPDATE, TRANSPORTATION\_UPDATE, TICKET\_UPDATE, ALERT\_UPDATE, AUTO\_REPLY, TRANSACTIONAL, OTP, UTILITY, MARKETING, AUTHENTICATION}> | The category for a template |
| `content`<br><br>string | The content for a template |
| `language`<br><br>array<string> | A list of supported languages that are available for each template |
| `name`<br><br>string | The name for a message template |
| `name_or_content`<br><br>string | Returns a list of message templates where the value for `name` or `content` match this value |
| `quality_score`<br><br>array<enum {GREEN, YELLOW, RED, UNKNOWN}> | The quality score for a template |
| `status`<br><br>array<enum {APPROVED, IN\_APPEAL, PENDING, REJECTED, PENDING\_DELETION, DELETED, DISABLED, PAUSED, LIMIT\_EXCEEDED}> | The review status for a template |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [WhatsAppBusinessHSM](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | The total number of message templates that belong to a WhatsApp Business Account |
| `message_template_count`<br><br>int32 | The current number of message templates that belong to the WhatsApp Business Account |
| `message_template_limit`<br><br>int32 | The maximum number of message templates that can belong to a WhatsApp Business Account |
| `are_translations_complete`<br><br>bool | The status for template translations |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 80008 | There have been too many calls to this WhatsApp Business account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

[](#)

Creating
--------

You can make a POST request to `message_templates` edge from the following paths:

* [`/{whats_app_business_account_id}/message_templates`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/)

When posting to this edge, a [WhatsAppMessageTemplate](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/) will be created.

### Requirements

| Type | Description |
| --- | --- |
| Access Tokens | [User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#user-access-tokens) or [System User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens) |
| Permissions | [whatsapp\_business\_management](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_management) |

### Request Syntax

POST /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID\>/message\_templates

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | ID of the WhatsApp Business Account to create the template on. |

### Post Body

See [Parameters](#parameters-2) for property descriptions.

{
  "allow\_category\_change": <ALLOW\_CATEGORY\_CHANGE\>,
  "name": "<NAME>",
  "language": "<LANGUAGE>",
  "category": "<CATEGORY>",
  "components": \[<COMPONENTS\>\]
}

### Response

See [Return Type](#return-type).

### Sample Request

curl 'https://graph.facebook.com/`v18.0`/102290129340398/message\_templates' \\
\-H 'Content-Type: application/json' \\
\-H 'Authorization: Bearer EAAJB...' \\
\-d '
{
  "name": "seasonal\_promotion",
  "language": "en",
  "category": "MARKETING",
  "components": \[
    {
      "type": "HEADER",
      "format": "TEXT",
      "text": "Our {{1}} is on!",
      "example": {
        "header\_text": \[
          "Summer Sale"
        \]
      }
    },
    {
      "type": "BODY",
      "text": "Shop now through {{1}} and use code {{2}} to get {{3}} off of all merchandise.",
      "example": {
        "body\_text": \[
          \[
            "the end of August","25OFF","25%"
          \]
        \]
      }
    },
    {
      "type": "FOOTER",
      "text": "Use the buttons below to manage your marketing subscriptions"
    },
    {
      "type":"BUTTONS",
      "buttons": \[
        {
          "type": "QUICK\_REPLY",
          "text": "Unsubcribe from Promos"
        },
        {
          "type":"QUICK\_REPLY",
          "text": "Unsubscribe from All"
        }
      \]
    }
  \]
}'

### Sample Response

{
    "id": "594425479261596",
    "status": "PENDING",
    "category": "MARKETING"
}

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

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can dissociate a [WhatsAppMessageTemplate](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/) from a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a DELETE request to [`/{whats_app_business_account_id}/message_templates`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/).

### Requirements

| Type | Description |
| --- | --- |
| Access Tokens | [User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#user-access-tokens) or [System User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens) |
| Permissions | [whatsapp\_business\_management](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_management) |

### Request Syntax

DELETE /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID\>/message\_templates

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | ID of the WhatsApp Business Account that owns the template. |

### Response

See [Return Type](#return-type-2).

### Sample Request

curl \-X DELETE 'https://graph.facebook.com/`v18.0`/102290129340398/message\_templates?name=order\_confirmation' \\
\-H 'Authorization: Bearer EAAJB...'

### Sample Response

{
  "success": true
}

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

[](#)

[WhatsApp Business Platform](https://developers.facebook.com/docs/whatsapp) | [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api) | [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises) | [Business Management API](https://developers.facebook.com/docs/whatsapp/business-management-api)

[](#)

[](#)

Whats App Business Account Product Catalogs
===========================================

[](#)

Reading
-------

Returns the product catalog connected to the WhatsApp Business Account

### Example

Requirements

* whatsapp\_business\_management permission
    
* whatsapp\_business\_messaging permission
    
* public\_profile permission
    
* WHATSAPP BUSINESS ACCOUNT ID
    
* USER ACCESS TOKEN
    

Request

cURLAndroid SDKObjective-C

    curl -i -X GET \
     "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID/product_catalogs?access_token=USERS-ACCESS-TOKEN"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/WHATSAPP-BUSINESS-ACCOUNT-ID/product_catalogs",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID/product_catalogs"
               parameters:nil
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

Response

{
  "data": \[
  \]
}

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ProductCatalog](https://developers.facebook.com/docs/marketing-api/reference/product-catalog/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can make a POST request to `product_catalogs` edge from the following paths:

* [`/{whats_app_business_account_id}/product_catalogs`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/product_catalogs/)

When posting to this edge, no Graph object will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `catalog_id`<br><br>Product Catalog ID | catalog\_id<br><br>Required |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Whats App Business Account Subscribed Apps
==========================================

[](#)

Reading
-------

Get a list of apps subscribed to webhooks for the WABA.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bwhats-app-business-account-id%7D%2Fsubscribed_apps&version=v18.0)

    GET /v18.0/{whats-app-business-account-id}/subscribed_apps HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{whats-app-business-account-id}/subscribed_apps',
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
        "/{whats-app-business-account-id}/subscribed_apps",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{whats-app-business-account-id}/subscribed_apps",
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
                                   initWithGraphPath:@"/{whats-app-business-account-id}/subscribed_apps"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of WhatsAppApplication nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 80008 | There have been too many calls to this WhatsApp Business account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

[](#)

Creating
--------

You can make a POST request to `subscribed_apps` edge from the following paths:

* [`/{whats_app_business_account_id}/subscribed_apps`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/subscribed_apps/)

When posting to this edge, a [WhatsAppApplication](https://developers.facebook.com/docs/graph-api/reference/whats-app-application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `override_callback_uri`<br><br>URI | **Required if overriding the callback URL.**<br><br>  <br>New callback URL. See [Overriding the Callback URL](https://developers.facebook.com/docs/whatsapp/embedded-signup/webhooks#overriding-the-callback-url). |
| `verify_token`<br><br>string | **Required if overriding the callback URL.**<br><br>  <br>Callback verification token. See [Overriding the Callback URL](https://developers.facebook.com/docs/whatsapp/embedded-signup/webhooks#overriding-the-callback-url). |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 2200 | subscription validation failed |
| 2201 | received an invalid hub.challenge while validating endpoint |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can dissociate a [WhatsAppApplication](https://developers.facebook.com/docs/graph-api/reference/whats-app-application/) from a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a DELETE request to [`/{whats_app_business_account_id}/subscribed_apps`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/subscribed_apps/).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Whats App Business Account Phone Numbers
========================================

[](#)

Represents a collection of business phone numbers associated with a WhatsApp Business Account (WABA).

To find the ID of a WhatsApp Business Account, go to [**Business Manager**](https://business.facebook.com/) > **Business Settings** > **Accounts** > **WhatsApp Business Accounts**. Find the account you want to use and click on it. A panel opens, with information about the account, including the ID.

  

For more information on how to use the API, see [WhatsApp Business Management API](https://developers.facebook.com/docs/whatsapp/business-account-management-api).

[](#)

Reading
-------

Get a list of phone numbers associated with a WhatsApp Business Account.

### Requirements

| Type | Description |
| --- | --- |
| Access Tokens | [User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#user-access-tokens) or [System User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens) |
| Permissions | [whatsapp\_business\_management](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_management)  <br>[whatsapp\_business\_messaging](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_messaging) |

### Request Syntax

GET https://graph.facebook.com/<API\_VERSION>/<WABA\_ID>/phone\_numbers

### Response

A list of [WhatsApp Business Phone Number](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account-to-number-current-status/) nodes and their default fields.

### Sample Request

curl \\
'https://graph.facebook.com/v15.0/102289599326934/phone\_numbers' \\
\-H 'Authorization: Bearer EAAJi...'

### Sample Response

{
  "data" : \[
    {
      "code\_verification\_status" : "VERIFIED",
      "display\_phone\_number" : "+1 555-555-5555",
      "id" : "106853218861309",
      "quality\_rating" : "GREEN",
      "verified\_name" : "Jaspers Market"
    }
  \],
  "paging" : {
    "cursors" : {
      "after" : "QVFIU...",
      "before" : "QVFIU..."
    }
  }
}

### Sample Request with Filtering

See [Filtering Phone Numbers](https://developers.facebook.com/docs/whatsapp/business-management-api/manage-phone-numbers#filter-phone-numbers).

curl GET \\
"https://graph.facebook.com/`v18.0`/102289599326934/phone\_numbers \\
 ?fields=id,is\_official\_business\_account,display\_phone\_number,verified\_name \\
 &filtering=\[{'field':'account\_mode','operator':'EQUAL','value':'SANDBOX'}\]" \\
\-H 'Authorization: Bearer EAAJi...'

### Sample Response 2

{   
   "id" : "106853218861309", 
   "is\_official\_business\_account" : true,
   "display\_phone\_number" : "+1 555-555-5555",      
   "verified\_name" : "Jaspers Market"
}

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [WhatsAppBusinessAccountToNumberCurrentStatus](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account-to-number-current-status/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | The current number of phone numbers that belong to a WhatsApp Business Account |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 80008 | There have been too many calls to this WhatsApp Business account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

[](#)

Creating
--------

Create a business phone number on a WhatsApp Business Account.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/guides/access-tokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) or [System User](https://www.facebook.com/business/help/503306463479099). |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [whatsapp\_business\_management](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_management)  <br>[whatsapp\_business\_messaging](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_messaging) |

### Sample Request

cURLAndroid SDKObjective-C

    curl -i -X POST \
     "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID/phone_numbers?
      cc=COUNTRY-CODE&
      phone_number=PHONE-NUMBER&
      migrate_phone_number=true&
      access_token=USER-ACCESS-TOKEN"

    GraphRequest request = GraphRequest.newPostRequest(
      accessToken,
      "/WHATSAPP-BUSINESS-ACCOUNT-ID/phone_numbers",
      new JSONObject("{\"cc\":\"COUNTRY-CODE\",\"phone_number\":\"PHONE-NUMBER\",\"migrate_phone_number\":true}"),
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID/phone_numbers"
               parameters:@{ @"cc": @"COUNTRY-CODE",@"phone_number": @"PHONE-NUMBER",@"migrate_phone_number": @"true",}
               HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

### Sample Response

{
  "id": "POST-ID"
}

You can make a POST request to `phone_numbers` edge from the following paths:

* [`/{whats_app_business_account_id}/phone_numbers`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/phone_numbers/)

When posting to this edge, a [WhatsAppBusinessPhoneNumber](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account-to-number-current-status/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `cc`<br><br>string | Country dial code of the phone number (for example, `1`). |
| `migrate_phone_number`<br><br>boolean | Set to `true` to migrate a registered WhatsApp Business Phone Number from one WhatsApp Business Account to another. |
| `phone_number`<br><br>string | Phone number without the country code or plus symbol (`+`). |
| `preverified_id`<br><br>string | Preverified ID related to this phone number |
| `verified_name`<br><br>string | Name of the business as it appears in the WhatsApp app or WhatsApp Business app profile. |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Whats App Business Account Conversation Analytics
=================================================

[](#)

Reading
-------

Enables one to retrieve the conversation based pricing analytics data for this WhatsApp Business Account

### Example

Requirements

* whatsapp\_business\_management permission
    
* whatsapp\_business\_messaging permission
    
* public\_profile permission
    
* WHATSAPP BUSINESS ACCOUNT ID
    
* USER ACCESS TOKEN
    

Request

_Formatted for readability._

cURLAndroid SDKObjective-C

    curl -i -X GET \ 
    "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID?fields=conversation_analytics.start(1651698000).end(1652302800).granularity(DAILY).phone_numbers(PHONE-NUMBER).country_codes().metric_types().conversation_types().conversation_directions().dimensions(CONVERSATION_DIRECTIONCONVERSATION_TYPECOUNTRYPHONE)&
    access_token=USER-ACCESS-TOKEN"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/WHATSAPP-BUSINESS-ACCOUNT-ID",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    Bundle parameters = new Bundle();
    parameters.putString("fields", "conversation_analytics.start(1651698000).end(1652302800).granularity(DAILY).phone_numbers(["PHONE-NUMBER "]).country_codes([]).metric_types([]).conversation_types([]).conversation_directions([]).dimensions(["CONVERSATION_DIRECTION","CONVERSATION_TYPE","COUNTRY","PHONE"])");
    request.setParameters(parameters);
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID"
               parameters:@{ @"fields": @"conversation_analytics.start(1651698000).end(1652302800).granularity(DAILY).phone_numbers(["PHONE-NUMBER"]).country_codes([]).metric_types([]).conversation_types([]).conversation_directions([]).dimensions(["CONVERSATION_DIRECTION","CONVERSATION_TYPE","COUNTRY","PHONE"])",}
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

Response

{
  "conversation\_analytics": {
    "data": \[
      {
        "data\_points": \[
          {
            "start": 1651698000,
            "end": 1651784400,
            "conversation": 281,
            "phone\_number": "PHONE-NUMBER",
            "country": "US",
            "conversation\_type": "FREE\_TIER",
            "conversation\_direction": "BUSINESS\_INITIATED",
            "cost": 0
          },
          {
            "start": 1652130000,
            "end": 1652216400,
            "conversation": 631,
            "phone\_number": "PHONE-NUMBER",
            "country": "US",
            "conversation\_type": "FREE\_TIER",
            "conversation\_direction": "BUSINESS\_INITIATED",
            "cost": 0
          }
        \]
      }
    \]
  },
  "id": "WHATSAPP-BUSINESS-ACCOUNT-ID"
}

### Parameters

| Parameter | Description |
| --- | --- |
| `conversation_categories`<br><br>array<enum {UNKNOWN, MARKETING, UTILITY, AUTHENTICATION, SERVICE, MARKETING\_OPTIMIZED\_DELIVERY}> | Default value: `[]`<br><br>list of conversation categories |
| `conversation_directions`<br><br>array<enum {UNKNOWN, BUSINESS\_INITIATED, USER\_INITIATED}> | Default value: `[]`<br><br>list of conversation directions |
| `conversation_types`<br><br>array<enum {UNKNOWN, REGULAR, FREE\_ENTRY\_POINT, FREE\_TIER}> | Default value: `[]`<br><br>list of conversation types |
| `country_codes`<br><br>array<string> | Default value: `[]`<br><br>list of country codes |
| `dimensions`<br><br>array<enum {UNKNOWN, PHONE, COUNTRY, CONVERSATION\_TYPE, CONVERSATION\_DIRECTION, CONVERSATION\_CATEGORY}> | Default value: `[]`<br><br>list of breakdown dimensions |
| `end`<br><br>int64 | end time<br><br>Required |
| `granularity`<br><br>enum {HALF\_HOUR, DAILY, MONTHLY} | data granularity<br><br>Required |
| `metric_types`<br><br>array<enum {UNKNOWN, CONVERSATION, COST}> | Default value: `[]`<br><br>list of metric types |
| `phone_numbers`<br><br>array<string> | Default value: `[]`<br><br>list of phone numbers |
| `start`<br><br>int64 | start time<br><br>Required |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of WABAConversationAnalytics nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 131009 | Parameter value is not valid |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Whats App Business Account Template Performance Metrics
=======================================================

[](#)

Reading
-------

Get a performance metrics on a WhatsApp template.

### Limitations

Businesses, WhatsApp Businesses, and business phone numbers originating in the EU or Japan are not supported.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bwhats-app-business-account-id%7D%2Ftemplate_performance_metrics&version=v18.0)

    GET /v18.0/{whats-app-business-account-id}/template_performance_metrics HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{whats-app-business-account-id}/template_performance_metrics',
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
        "/{whats-app-business-account-id}/template_performance_metrics",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{whats-app-business-account-id}/template_performance_metrics",
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
                                   initWithGraphPath:@"/{whats-app-business-account-id}/template_performance_metrics"
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
| `name`<br><br>string | name |
| `template_id`<br><br>whatsapp business hsm ID | template\_id |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of WhatsAppBusinessHSMWhatsAppBusinessPerformanceMetrics nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Whats App Business Account Upsert Message Templates
===================================================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can make a POST request to `upsert_message_templates` edge from the following paths:

* [`/{whats_app_business_account_id}/upsert_message_templates`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/upsert_message_templates/)

When posting to this edge, no Graph object will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `category`<br><br>enum {AUTHENTICATION} | Template category. See Template Categories.<br><br>Required |
| `components`<br><br>array<JSON object> | Array of components that make up the template. See Template Components.<br><br>Required |
| `type`<br><br>enum {HEADER, BODY, FOOTER, BUTTONS, CAROUSEL, LIMITED\_TIME\_OFFER} | type<br><br>Required |
| `add_security_recommendation`<br><br>boolean | Set to true if you want the template to include the string, For your security, do not share this code. Set to false to exclude the string. |
| `code_expiration_minutes`<br><br>int64 | Indicates number of minutes the password or code is valid.<br><br>If omitted, the code expiration warning will not be displayed in the delivered message.<br><br>Minimum 1, maximum 90. |
| `buttons`<br><br>array<JSON object> | Button components to be used in the template. |
| `type`<br><br>enum {OTP} | type<br><br>Required |
| `otp_type`<br><br>enum {COPY\_CODE, ONE\_TAP} | Indicates button type. Set to COPY\_CODE if you want the template to use a copy code button, or ONE\_TAP to have it use a one-tap autofill button. |
| `package_name`<br><br>string | One-tap buttons only.<br><br>Your Android app's package name. |
| `signature_hash`<br><br>string | One-tap buttons only.<br><br>Your app signing key hash. |
| `languages`<br><br>array<string> | array of Template location and locale code.<br><br>Required |
| `name`<br><br>string | Template name.<br><br>Required |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`data`: List \[

Struct {

`id`: numeric string,

`status`: enum,

`language`: string,

}

\],

}

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)