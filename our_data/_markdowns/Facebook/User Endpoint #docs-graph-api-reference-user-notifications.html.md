Graph API Reference v19.0: User Notifications - Documentation - Meta for Developers

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
Graph API Versionv19.0User Notifications
==================
Reading
-------
You can't perform this operation on this endpoint.Creating
--------
You can make a POST request to `notifications` edge from the following paths: * `/{user_id}/notifications`
When posting to this edge, no Graph object will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `bot_message_payload_elements`string | Optional bot message payload used for sending a customizable generic template XMA to the recipient if a bot message is sent. If not specified, then a standard generic template XMA will be sent using just the message title and body.
 |
| `filtering`list<enum{groups, groups\_social, ema}> | Notification filters to apply.
 |
| `href` | The relative path and GET params used in the a2u target url.
 |
| `label`string | Optional label to group similar updates.
 |
| `message`JSON object | Contains the title, main message body, and media image for the notification.
 |
| `title`string | title
Required |
| `body`string | body
Required |
| `media_url`URI | media\_url
 |
| `notif_ids`list<string> | The notification ids to act on.
 |
| `payload`string | Optional custom payload that will be added to the URL encoding of the game that is generated when the notification is clicked.
 |
| `read`boolean | Indicates that the provided notification ids should be marked as read
 |
| `ref`string | A reference param used for logging
 |
| `schedule_interval`int64 | Time from now (in seconds) that the notification will be sent
 |
| `seen`boolean | Indicates that the provided notification ids should be marked as seen
 |
| `template` | Used for creating a2u notifications.
Supports Emoji |
| `type`enum{generic, content\_update} | Notification type
 |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, `notification_id`: int32, }### Error Codes

| Error | Description |
| --- | --- |
| 288 | Sending notificatons to user requires the extended permission app\_notifications  |
| 100 | Invalid parameter |
| 613 | Calls to this api have exceeded the rate limit. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.