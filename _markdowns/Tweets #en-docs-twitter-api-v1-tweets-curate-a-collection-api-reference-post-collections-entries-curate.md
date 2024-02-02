<div>

::: c01-rich-text-editor
Curate a Collection by adding or removing Tweets in bulk. Updates must
be limited to 100 cumulative additions or removals per request.

Use [POST collections / entries /
add](/en/docs/tweets/curate-a-collection/api-reference/post-collections-entries-add)
and [POST collections / entries /
remove](/en/docs/tweets/curate-a-collection/api-reference/post-collections-entries-remove)
to add or remove a single Tweet.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/collections/entries/curate.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------ ---------- ------------- --------------- ---------
  Name   Required   Description   Default Value   Example
  ------ ---------- ------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/collections/entries/curate.json `

## Example Response [¶](#example-response){.headerlink}

    POST /1.1/collections/entries/curate.json
    Content-Type: application/json
    Content-Length: 226

    {"id":"custom-388061495298244609","changes":[{"op":"add","tweet_id":"390897780949925889"},{"op":"add","tweet_id":"390853164611555329"},{"op":"add","tweet_id":"390892747810295808"},{"op":"add","tweet_id":"390898463090561024"}]} 

## Success: [¶](#success-){.headerlink} {#success-}

    {"objects":{},"response":{"errors":[]}}

## Failure: [¶](#failure-){.headerlink} {#failure-}

    {"objects":{},"response":{"errors":[{"reason":"duplicate","change":{"op":"add","tweet_id":"390897780949925889"}},{"reason":"duplicate","change":{"op":"add","tweet_id":"390853164611555329"}},{"reason":"duplicate","change":{"op":"add","tweet_id":"390892747810295808"}},{"reason":"duplicate","change":{"op":"add","tweet_id":"390898463090561024"}}]}}
:::

</div>
