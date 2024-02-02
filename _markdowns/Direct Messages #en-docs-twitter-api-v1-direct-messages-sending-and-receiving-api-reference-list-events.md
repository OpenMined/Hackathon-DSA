<div>

::: c01-rich-text-editor
Returns all Direct Message events (both sent *and* received) within the
last 30 days. Sorted in reverse-chronological order.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/events/list.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15/user
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ----------------------- ---------------------------------------------------------------------------------------------------------------
  **count** (optional)    Max number of events to be returned. 20 default. 50 max.
  **cursor** (optional)   For paging through result sets greater than 1 page, use the "next_cursor" property from the previous request.
  ----------------------- ---------------------------------------------------------------------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X GET /1.1/direct_messages/events/list.json

## Example Response [¶](#example-response){.headerlink}

Events are returned in the ` events ` array. A ` next_cursor ` property
will be returned if there are more events to be retrieved.

> **Note**
>
> To determine if there are more event to retrieve, always look for the
> presence of a ` next_cursor ` . In rare cases the ` events ` array may
> be empty.

    {
      "next_cursor": "AB345dkfC",
      "events": [
        { "id": "110", "created_timestamp": "5300", ... },
        { "id": "109", "created_timestamp": "5200", ... },
        { "id": "108", "created_timestamp": "5200", ... },
        { "id": "107", "created_timestamp": "5200", ... },
        { "id": "106", "created_timestamp": "5100", ... },
        { "id": "105", "created_timestamp": "5100", ... },
        ...
      ]
    }
:::

</div>
