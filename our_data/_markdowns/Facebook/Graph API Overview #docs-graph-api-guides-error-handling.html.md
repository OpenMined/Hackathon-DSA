Handle Errors - Graph API - Documentation - Meta for Developers

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
Handling Errors
===============

Requests made to our APIs can result in several different error responses. The following document describes the recovery tactics and provides a list of error values with a map to the most common recovery tactic to use.

Error Responses
---------------

The following represents a common error response resulting from a failed API request:

```
{
  "error": {
    "message": "Message describing the error", 
    "type": "OAuthException", 
    "code": 190,
    "error_subcode": 460,
    "error_user_title": "A title",
    "error_user_msg": "A message",
    "fbtrace_id": "EJplcsCHuLu"
  }
}
```
* `message`: A human-readable description of the error.
* `code`: An error code. Common values are listed below, along with common recovery tactics.
* `error_subcode`: Additional information about the error. Common values are listed below.
* `error_user_msg`: The message to display to the user. The language of the message is based on the locale of the API request.
* `error_user_title`: The title of the dialog, if shown. The language of the message is based on the locale of the API request.
* `fbtrace_id`: Internal support identifier. When reporting a bug related to a Graph API call, include the `fbtrace_id` to help us find log data for debugging. However, this ID will expire shortly. To help the support team reproduce your issue, please attach a saved graph explorer session.

### Error Codes

Code or Type
 | 
Name
 | 
What To Do
 || OAuthException |  | If no subcode is present, the login status or access token has expired, been revoked, or is otherwise invalid. Get a new access token.
If a subcode is present, see the subcode. |
| 102 | API Session | If no subcode is present, the login status or access token has expired, been revoked, or is otherwise invalid. Get a new access token.
If a subcode is present, see the subcode. |
| 1 | API Unknown | Possibly a temporary issue due to downtime. Wait and retry the operation. If it occurs again, check that you are requesting an existing API. |
| 2 | API Service | Temporary issue due to downtime. Wait and retry the operation. |
| 3 | API Method | Capability or permissions issue. Make sure your app has the necessary capability or permissions to make this call. |
| 4 | API Too Many Calls | Temporary issue due to throttling. Wait and retry the operation, or examine your API request volume. |
| 17 | API User Too Many Calls | Temporary issue due to throttling. Wait and retry the operation, or examine your API request volume. |
| 10 | API Permission Denied | Permission is either not granted or has been removed. Handle the missing permissions. |
| 190 | Access token has expired | Get a new access token. |
| 200-299 | API Permission (Multiple values depending on permission) | Permission is either not granted or has been removed. Handle the missing permissions. |
| 341 | Application limit reached | Temporary issue due to downtime or throttling. Wait and retry the operation, or examine your API request volume. |
| 368 | Temporarily blocked for policies violations | Wait and retry the operation. |
| 506 | Duplicate Post | Duplicate posts cannot be published consecutively. Change the content of the post and try again. |
| 1609005 | Error Posting Link | There was a problem scraping data from the provided link. Check the URL and try again. |
### Authentication Error Subcodes

Code
 | 
Name
 | 
What To Do
 || 458 | App Not Installed | The User has not logged into your app. Reauthenticate the User. |
| 459 | User Checkpointed | The User needs to log in at https://www.facebook.com or https://m.facebook.com to correct an issue. |
| 460 | Password Changed | On iOS 6 and above, if the person logged in using the OS-integrated flow, direct them to Facebook OS settings on the device to update their password. Otherwise, they must log in to the app again. |
| 463 | Expired | Login status or access token has expired, been revoked, or is otherwise invalid. Handle expired access tokens. |
| 464 | Unconfirmed User | The User needs to log in at https://www.facebook.com or https://m.facebook.com to correct an issue. |
| 467 | Invalid Access Token | Access token has expired, been revoked, or is otherwise invalid. Handle expired access tokens. |
| 492 | Invalid Session | User associated with the Page access token does not have an appropriate role on the Page. |
### Rate Limiting Error Codes

Visit the Graph API Rate Limits guide for more information about Rate Limiting Error Codes.