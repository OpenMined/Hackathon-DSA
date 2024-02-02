<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
This guide shows you how to detect copyright violations for a video
uploaded or published to Instagram using the Instagram Graph API.

## Before you start

Before you start you will need the following:

-   All requirements and limitations for accessing the Instagram
    Container and Instagram Media endpoints apply

### Best practices

<div>

When testing an API call, you can include the ` access_token ` parameter
set to your access token. However, when making secure calls from your
app, use the [access token
class.](https://developers.facebook.com/docs/facebook-login/guides/access-tokens#portabletokens)

</div>
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
To check the copyright status for a video that have been uploaded, but
not yet published, send a ` GET ` request to the ` /{ig-containter-id} `
endpoint with the ` fields ` parameter set to ` copyright_check_status `
.

### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X GET "https://graph.facebook.com/v18.0/{ig-containter-id}?fields=copyright_check_status" 
```

On success, your app receives a JSON response with a
` copyright_check_status ` object with the following key-value pairs:

-   ` status ` set to ` completed ` , ` error ` , ` in_progress ` , or
    ` not_started `
-   ` matches_found ` set to:
    -   ` false ` if none are detected
    -   ` true ` if violations are detected and ` author ` ,
        ` content_title ` , ` matched_segments ` , and
        ` owner_copyright_policy ` values

### Sample Responses

+-----------------------------------+-----------------------------------+
| ``` {._5s-8 .prett                | ``` {._5s-8 .prett                |
| yprint .lang-json .prettyprinted} | yprint .lang-json .prettyprinted} |
| { "c                              | { "copyright_                     |
| opyright_check_status": { "status | check_status": { "status": "in_pr |
| ": "complete", "matches_found": t | ogress", "matches_found": false } |
| rue }, "id": "{ig-containter-id}" | }                                 |
| }                                 | ```                               |
| ```                               |                                   |
+-----------------------------------+-----------------------------------+
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
To check the copyright status for a video that has been published, send
a ` GET ` request to the ` /{ig-media-id} ` endpoint with the ` fields `
parameter set to ` copyright_check_information ` .

### Sample Request {#sample-request-2}

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X GET "https://graph.facebook.com/v18.0/{ig-media-id}?fields=copyright_check_information" 
```

On success, your app receives a JSON response with the ` id ` set to the
video being checked and the ` copyright_check_information ` object with
the following:

-   ` status ` set to a ` status ` object set to ` completed ` ,
    ` error ` , ` in_progress ` , or ` not_started `
-   ` copyright_matches ` set to:
    -   ` false ` -- Returned when no copyright violations are detected
    -   ` true ` -- Returned when copyright violations are detected and
        includes the ` copyright_check_information ` object that
        contains information about the copyright owner, policy,
        mitigation steps, and sections of the media that violated the
        copyright.

### Sample Responses {#sample-responses-2}

+-----------------------------------+-----------------------------------+
| <div>                             | <div>                             |
|                                   |                                   |
| ``` {._5s-8 .prett                | ``` {._5s-8 .prett                |
| yprint .lang-json .prettyprinted} | yprint .lang-json .prettyprinted} |
| { "copyright_chec                 | { "copyright_check_               |
| k_information": { "status": { "st | information": { "status": { "stat |
| atus": "complete", "matches_found | us": "complete", "matches_found": |
| ": true }, "copyright_matches": [ |  false } }, "id": "{ig-media-id}" |
|  { "content_title": "In My Feelin | }                                 |
| gs", "author": "Drake", "owner_co | ```                               |
| pyright_policy": { "name": "UMG", |                                   |
|  "actions": [ { "action": "BLOCK" | </div>                            |
| , "territories": "3", "geos": [ " |                                   |
| Canada", "India", "United States  |                                   |
| of America" ] }, { "action": "MUT |                                   |
| E", "territories": "4", "geos": [ |                                   |
|  "Taiwan", "Tanzania", "Saudi Ara |                                   |
| bia", "United Kingdom of Great Br |                                   |
| itain and Northern Ireland" ] } ] |                                   |
|  }, "matched_segments": [ { "star |                                   |
| t_time_in_seconds": 2.4, "duratio |                                   |
| n_in_seconds": 5.1, "segment_type |                                   |
| ": "AUDIO" }, { "start_time_in_se |                                   |
| conds": 10.2, "duration_in_second |                                   |
| s": 4.5, "segment_type": "VIDEO"  |                                   |
| } ] } ] }, "id": "90012800291314" |                                   |
| }                                 |                                   |
| ```                               |                                   |
|                                   |                                   |
| </div>                            |                                   |
+-----------------------------------+-----------------------------------+
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
-   ::: fcb
    [Instagram Container Reference
    ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22){.img
    width="10px"
    srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22"}](https://developers.facebook.com/docs/instagram-api/reference/ig-container)
    :::

-   ::: fcb
    [Instagram Media Reference
    ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22){.img
    width="10px"
    srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=0iqM6GOMcgMAX-Sufh2&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBhUHzPDjdzkuY0wzYMWRnR31Z8YvejaG8Y6FlqaccnFQ&oe=65C36E22"}](https://developers.facebook.com/docs/instagram-api/reference/ig-media)
    :::
:::
:::

</div>
