::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
  --------------------------------------- ----------------------------
  [GET /{stream-type}/:stream](#Stream)   Connect to the data stream
  --------------------------------------- ----------------------------

All requests to the Volume Stream APIs must use HTTP Basic
Authentication, constructed from a valid email address and password
combination used to log into your account at console.gnip.com.
Credentials must be passed as the Authorization header for each request.
So confirm that your client is adding the \"Authentication: Basic\" HTTP
header (with encoded credentials over HTTPS) to all API requests.

## GET /{stream-type}/:stream []{#Stream .tall} [¶](#get-stream-type-stream-){.headerlink} {#get-stream-type-stream-}

Establishes a persistent connection to the Firehose stream, through
which the realtime data will be delivered.

**Note:** Please see [this
article](/en/docs/tutorials/consuming-streaming-data) for additional
details on consuming streaming data after the connection is established.

#### Request Specifications

+-----------------------------------+-----------------------------------+
| **Request Method**                | HTTP GET                          |
+-----------------------------------+-----------------------------------+
| **Connection Type**               | Keep-Alive                        |
|                                   |                                   |
|                                   | This should be specified in the   |
|                                   | header of the request.            |
+-----------------------------------+-----------------------------------+
| **URL**                           | Found on the stream\'s API Help   |
|                                   | page of your dashboard, using the |
|                                   | following structure:              |
|                                   |                                   |
|                                   | Decahose:                         |
|                                   |                                   |
|                                   |     https://gnip-stream.t         |
|                                   | witter.com/stream/sample10/accoun |
|                                   | ts/:account_name/publishers/twitt |
|                                   | er/:stream_label.json?partition=1 |
+-----------------------------------+-----------------------------------+
| **Partition (required)**          | ` partition={#} ` - Partitioning  |
|                                   | is now required in order to       |
|                                   | consume the full stream. You will |
|                                   | need to connect to the stream     |
|                                   | with the partition parameter      |
|                                   | specified. Below is the number of |
|                                   | partitions per stream:            |
+-----------------------------------+-----------------------------------+
| **Compression**                   | Gzip. To connect to the stream    |
|                                   | using Gzip compression, simply    |
|                                   | send an Accept-Encoding header in |
|                                   | the connection request. The       |
|                                   | header should look like the       |
|                                   | following:                        |
|                                   |                                   |
|                                   | Accept-Encoding: gzip             |
+-----------------------------------+-----------------------------------+
| **Character Encoding**            | UTF-8                             |
+-----------------------------------+-----------------------------------+
| **Response Format**               | JSON. The header of your request  |
|                                   | should specify JSON format for    |
|                                   | the response.                     |
+-----------------------------------+-----------------------------------+
| **Rate Limit**                    | 10 requests per 60 seconds.       |
+-----------------------------------+-----------------------------------+
| **Backfill Parameter**            | If you have purchased a stream    |
|                                   | with Backfill enabled, you\'ll    |
|                                   | need to add the                   |
|                                   | \"backfillMinutes\" parameter     |
|                                   | into GET request to enable it.    |
+-----------------------------------+-----------------------------------+
| **Read Timeout**                  | Set a read timeout on your        |
|                                   | client, and ensure that it is set |
|                                   | to a value beyond 30 seconds.     |
+-----------------------------------+-----------------------------------+
| **Support for Tweet edits**       | All Tweet objects will include    |
|                                   | Tweet edit metadata describing    |
|                                   | the Tweet\'s edit history. See    |
|                                   | the [\"Edit Tweets\" fundamentals |
|                                   | page](https:/                     |
|                                   | /developer.twitter.com/en/docs/tw |
|                                   | itter-api/enterprise/edit-tweets) |
|                                   | for more details.                 |
+-----------------------------------+-----------------------------------+

#### Responses

The following responses may be returned by the API for these requests.
Most error codes are returned with a string with additional details in
the body. For non-200 responses, clients should attempt to reconnect.

+-----------------------+-----------------------+-----------------------+
| 200                   | Success               | The connection was    |
|                       |                       | successfully opened,  |
|                       |                       | and new activities    |
|                       |                       | will be sent through  |
|                       |                       | as they arrive.       |
+-----------------------+-----------------------+-----------------------+
| 401                   | Unauthorized          | HTTP authentication   |
|                       |                       | failed due to invalid |
|                       |                       | credentials. Log in   |
|                       |                       | to console.gnip.com   |
|                       |                       | with your credentials |
|                       |                       | to ensure you are     |
|                       |                       | using them correctly  |
|                       |                       | with your request.    |
+-----------------------+-----------------------+-----------------------+
| 406                   | Not Acceptable        | Generally, this       |
|                       |                       | occurs where your     |
|                       |                       | client fails to       |
|                       |                       | properly include the  |
|                       |                       | headers to accept     |
|                       |                       | gzip encoding from    |
|                       |                       | the stream, but can   |
|                       |                       | occur in other        |
|                       |                       | circumstances as      |
|                       |                       | well.                 |
|                       |                       |                       |
|                       |                       | Will contain a JSON   |
|                       |                       | message similar to    |
|                       |                       | \"This connection     |
|                       |                       | requires compression. |
|                       |                       | To enable             |
|                       |                       | compression, send an  |
|                       |                       | \'Accept-Encoding:    |
|                       |                       | gzip\' header in your |
|                       |                       | request and be ready  |
|                       |                       | to uncompress the     |
|                       |                       | stream as it is read  |
|                       |                       | on the client end.\"  |
+-----------------------+-----------------------+-----------------------+
| 429                   | Rate Limited          | Your app has exceeded |
|                       |                       | the limit on          |
|                       |                       | connection requests.  |
+-----------------------+-----------------------+-----------------------+
| 503                   | Service Unavailable   | Twitter server issue. |
|                       |                       | Reconnect using an    |
|                       |                       | exponential backoff   |
|                       |                       | pattern. If no notice |
|                       |                       | about this issue has  |
|                       |                       | been posted on the    |
|                       |                       | [Twitter API Status   |
|                       |                       | Page](https:/         |
|                       |                       | /api.twitterstat.us/) |
|                       |                       | , contact support or  |
|                       |                       | emergency if unable   |
|                       |                       | to connect after 10   |
|                       |                       | minutes.              |
+-----------------------+-----------------------+-----------------------+

#### Example curl Request

The following example request is accomplished using cURL on the command
line. However, note that these requests may also be sent with the
programming language of your choice:

    curl --compressed -v -uexample@customer.com "https://gnip-stream.twitter.com/stream/firehose/accounts/:account_name/publishers/twitter/:stream_label.json?partition={#}"

## Replay API []{#replay_api .tall} [¶](#replay-api-){.headerlink} {#replay-api-}

The Replay API is an important complement to realtime Volume streams.
Replay is a data recovery tool that provides streaming access to a
rolling window of recent Twitter historical data.
:::
:::
:::
:::
:::
:::
:::
