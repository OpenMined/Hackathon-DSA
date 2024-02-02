<div>

::: c01-rich-text-editor
Submits a request to retrieve activities from up to the past five days
from all subscriptions present during the date and time windows
specified in the request. If your webhook has active user subscriptions,
you will concurrently receive those events as well. Note: We do perform
a CRC before delivering replay events.

  ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Request Method**            HTTP POST
  **URL**                       /1.1/account_activity/replay/webhooks/:webhook_id/subscriptions/all.json?from_date=yyyymmddhhmm&to_date=yyyymmddhhmm
  **Response Format**           JSON
  **Requires Authentication**   Yes (application only - bearer token)
  **Rate Limit**                5 requests per 15 minutes. There is currently no maximum on the number of replay jobs that can requested.
  **from_date**                 The oldest (starting) UTC timestamp from which the events will be provided, must be in \'yyyymmddhhmm\' format. Timestamp is in minute granularity and is inclusive (i.e. 12:00 includes the 00 minute). Valid times must be within the last 5 days, UTC time, and no more recent than 31 minutes before the current point in time. It\'s recommended that the from_date and to_date should be within \~2 hours.
  **to_date**                   The latest (ending) UTC timestamp to which the event will be provided, must be in \'yyyymmddhhmm\' format. Timestamp is in minute granularity and is exclusive (i.e. 12:30 does not include the 30th minute of the hour). Valid times must be within the last 5 days, UTC time, and no more recent than 10 minutes before the current point in time.
  ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

#### Responses

The following responses may be returned by the API. Most error codes are
returned with a string including additional details in the body. For
non-200 responses, you should resolve the error and try again.

  ----- ----------------------- ----- ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  202   Accepted                N/A   The request was successful and the activities will be sent.                                 N/A
  400   Bad Request             214   Webhook has been marked as invalid.                                                         Webhook is marked invalid and requires a CRC check.
  400   Bad Request             357   Query parameter is missing.                                                                 
  400   Bad Request             358   Route or query parameter is malformed.                                                      Unable to parse
  400   Bad Request             360   Route parameter is negative.                                                                webhook_id: \[\] is not greater than or equal to 0.
  400   Bad Request             368   from_date or to_date is not in the past.                                                    : \[\<field_value\>\] is not in the past.
  400   Bad Request             356   from_date must be before to_date.                                                           from_date must be before to_date.
  400   Bad Request             356   from_date must be within the past 5 days.                                                   from_date must be within the past 5 days.
  401   Unauthorized            32    HTTP authentication failed due to 3-legged auth provided.                                   Invalid authentication method. Please use application-only authentication.
  401   Unauthorized            61    Client is not permitted to request this method.                                             Client is not permitted to request this method.
  403   Forbidden               200   Client does not have an enterprise account with Replay enabled.                             Account Activity API enterprise account with replay is required. Please confirm you have an enterprise account and replay is enabled.
  404   Not Found               34    Non-existing webhook_id; webhook_id-application_id mismatch.                                Webhook does not exist or is associated with a different twitter application.
  409   Conflict                355   There is a request in flight and it will need to finish processing before making another.   A replay job is already in progress for this webhook.
  429   Too Many Requests       88    Rate limited (hit limit of the number of requests per time period)                          Too many requests. Please back off your API request rate.
  500   Internal Server Error   0     Internal server error.                                                                      Internal server error.
  503   Service Unavailable     67    One or more dependent services at Twitter is unavailable.                                   Twitter server error. Retry using an exponential backoff pattern.
  ----- ----------------------- ----- ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

\

#### \"Job completed successfully" message

Once your job successfully completes, Account Activity Replay API will
deliver the following job completion event. Once you receive this event,
the job has finished running and another can be submitted.


    {
      "replay_job_status": {
        "webhook_id": "1234577122340233217",
        "job_state": "Complete",
        "job_state_description": "Job completed successfully"
        "job_id": "1095098195724558337"
      }
    }

#### \"Job failed to complete\" message

In the event your job does not complete successfully, we will return the
following message encouraging you to retry your Replay job. Once you
receive this event, the job has finished running and another can be
submitted.

    {
      "replay_job_status": {
        "webhook_id": "123451374207332352",
        "job_state": "Incomplete",
        "job_state_description": "Job failed to deliver all events, please retry your replay job",
        "job_id": "1093226942650736640"
      }
    }

#### Example curl request

    curl --request POST  --url 'https://api.twitter.com/1.1/account_activity/replay/webhooks/:webhook_id/subscriptions/all.json?from_date=yyyymmddhhmm&to_date=yyyymmddhhmm'
    --header 'authorization: Bearer TOKEN'

#### Example response

    HTTP 202

    {
      "job_id": "1234567890",
      "created_at": "2016-06-02T23:54:02Z"
    }
:::

</div>
