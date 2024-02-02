Content Publishing Limit - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG User Content Publishing Limit
================================

Represents an IG User's current content publishing usage.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}/content_publishing_limit`**

Get the number of times an IG User has published and IG Container within a given time period. Refer to the Content Publishing guide for complete publishing steps.

### Requirements

 Type | Requirement || Access Tokens | User |
| Permissions | `instagram_basic`
`instagram_content_publish`
`pages_read_engagement`
If the app user was granted a role via the Business Manager on the Page connected to the targeted IG User, you will also need one of:
`ads_management`
`business_management` |
### Request Syntax

```
GET https://graph.facebook.com/v9.0/{ig-user-id}/content_publishing_limit
  ?fields={fields}
  &since={since}
  &access_token={access-token}
```
### Query String Parameters

 Placeholder
  | 
 Value Description
  || `{access-token}`
**Required**
*String* | The app user's User Access Token. |
| `{fields}`
*Comma-separated list* | A comma-separated list of fields you want returned. If omitted, the `quota_usage` field will be returned by default. |
| `{since}`
*Unix timestamp* | A Unix timestamp no older than 24 hours. |
### Fields

 Field
  | 
 Value Description
  || `config`
*Object* | Returns these values:* `quota_total` — The maximum number of IG Containers the app user can publish within the `quota_duration` time period (currently `50`).
* `quota_duration` — The period of time in seconds against which the `quota_total` is calculated (currently `86400` seconds, or 24 hours).
 |
| `quota_usage`
*Comma-separated list* | The number of times the app user has published an IG Container since the time specified in the `since` query string parameter. If the `since` parameter is omitted, this value will be the number of times the app user has published a container within the last 24 hours. This field is returned by default if the `fields` query string parameter is omitted from the query. |
### Sample Request

```
curl -X GET \
  'https://graph.facebook.com/v19.0/17841405822304914/content_publishing_limit?fields=quota_usage,rate_limit_settings&since=1609969714&access_token=IGQVJ...'
```
### Sample Response

```
{
  "data": [
    {
      "quota_usage": 2,
      "config": {
        "quota_total": 50,
        "quota_duration": 86400
      }
    }
  ]
}
```
Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.