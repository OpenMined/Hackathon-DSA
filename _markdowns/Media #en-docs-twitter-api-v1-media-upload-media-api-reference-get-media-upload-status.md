<div>

::: c01-rich-text-editor
The ` STATUS ` command is used to periodically poll for updates of media
processing operation. After the ` STATUS ` command response returns
` succeeded ` , you can move on to the next step which is usually create
Tweet with media_id.

## Request [¶](#request){.headerlink}

It should be a HTTP GET request with url params.

**Note:** The domain for this endpoint is **upload.twitter.com**

## Response [¶](#response){.headerlink}

The response body contains ` processing_info ` field which provides
information about current state of media processing operation. It
contains a ` state ` field which has transition flow: "pending" -\>
"in_progress" -\> \["failed" \| "succeeded"\]. You can not use the
media_id to create Tweet or other entities before the state field is set
to "succeeded".

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ---------- ---------- ------------------------------------------------------ --------------- ---------
  Name       Required   Description                                            Default Value   Example
  command    required   Must be set to ` STATUS ` (case sensitive).                            
  media_id   required   The ` media_id ` returned from the ` INIT ` command.                   
  ---------- ---------- ------------------------------------------------------ --------------- ---------

## Example request [¶](#example-request){.headerlink}

` GET https://upload.twitter.com/1.1/media/upload.json?command=STATUS&media_id=710511363345354753 `

## Example Result [¶](#example-result){.headerlink}

    // Example of an in_progress response:

    {
      "media_id":710511363345354753,
      "media_id_string":"710511363345354753",
      "expires_after_secs":3595,
      "processing_info":{
        "state":"in_progress", // state transition flow is pending -> in_progress -> [failed|succeeded]
        "check_after_secs":10, // check for the update after 10 seconds
        "progress_percent":8 // Optional [0-100] int value. Please don't use it as a replacement of "state" field.
      }
    }

    // Example of a failed response:

    {
      "media_id":710511363345354753,
      "media_id_string":"710511363345354753",
      "processing_info":{
        "state":"failed",
        "progress_percent":12,
        "error":{
          "code":1,
          "name":"InvalidMedia",
          "message":"Unsupported video format"
        }
      }
    }

    // Example of a succeeded response:

    {
      "media_id":710511363345354753,
      "media_id_string":"710511363345354753",
      "expires_after_secs":3593,
      "video":{
        "video_type":"video/mp4"
      },
      "processing_info":{
        "state":"succeeded",
        "progress_percent":100,
      }
    }
:::

</div>
