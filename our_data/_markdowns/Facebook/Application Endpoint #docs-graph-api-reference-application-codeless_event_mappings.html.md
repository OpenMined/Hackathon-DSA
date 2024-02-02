Graph API Reference v19.0: Application Codeless Event Mappings - Documentation - Meta for Developers

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
Graph API Versionv19.0Application Codeless Event Mappings
===================================
Reading
-------
You can't perform this operation on this endpoint.Creating
--------
You can make a POST request to `codeless_event_mappings` edge from the following paths: * `/{application_id}/codeless_event_mappings`
When posting to this edge, an Application will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `mappings`array<JSON object> | The event to UI component mappings of the app
Required |
| `method`enum {INFERENCE, MANUAL, CONFIRMED\_INFERENCE, BUTTON\_INDEXING, UNKNOWN} | method
Required |
| `event_name`string | event\_name
Required |
| `event_type`enum {CLICK, SELECTED, TEXT\_CHANGED} | event\_type
Required |
| `app_version`string | app\_version
Required |
| `parameters`array<JSON object> | parameters
 |
| `name`string | name
Required |
| `path`array<JSON object> | path
Required |
| `class_name`string | class\_name
Required |
| `index`int64 | index
Required |
| `id`int64 | id
 |
| `text`string | text
 |
| `tag`string | tag
 |
| `description`string | description
 |
| `hint`string | hint
 |
| `match_bitmask`int64 | match\_bitmask
 |
| `path_type`enum {ABSOLUTE, RELATIVE} | Default value: `"ABSOLUTE"`path\_type
 |
| `component_id`string | component\_id
Required |
| `path`array<JSON object> | path
Required |
| `class_name`string | class\_name
Required |
| `index`int64 | index
Required |
| `id`int64 | id
 |
| `text`string | text
 |
| `tag`string | tag
 |
| `description`string | description
 |
| `hint`string | hint
 |
| `match_bitmask`int64 | match\_bitmask
 |
| `component_id`string | component\_id
Required |
| `path_type`enum {ABSOLUTE, RELATIVE} | Default value: `"ABSOLUTE"`path\_type
 |
| `screenshot_handle`string | screenshot\_handle
 |
| `dimensions`array<JSON object> | dimensions
 |
| `top`int64 | top
Required |
| `left`int64 | left
Required |
| `width`int64 | width
Required |
| `height`int64 | height
Required |
| `activity_name`string | activity\_name
 |
| `mutation_method`enum {REPLACE, ADD, DELETE} | Detailed mutation type like replace, add
Required |
| `platform`enum {ANDROID, IOS} | The platform of the app being indexed
Required |
| `post_method`enum {EYMT, CODELESS} | Default value: `"CODELESS"`Whether the api is called by codeless or EYMT
 |
### Return Type
 Struct {`num_updated`: int32, `num_invalid`: int32, }### Error Codes

| Error | Description |
| --- | --- |
| 105 | The number of parameters exceeded the maximum for this operation |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.