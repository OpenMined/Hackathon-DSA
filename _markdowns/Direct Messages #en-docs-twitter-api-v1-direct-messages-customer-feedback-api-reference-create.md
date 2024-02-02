<div>

::: c01-rich-text-editor
Sends Feedback prompt along with a Direct Message (DM) to a specified
user. The DM message is required. Sending Feedback inherits the Direct
Message restrictions and behavior from [POST
direct_messages/events/new](/en/docs/direct-messages/sending-and-receiving/api-reference/new-event)
.

  --------------------------------------- ---------------------------
  Response formats                        JSON
  Requires authentication?                Yes (user context only)
  Rate limited?                           Yes
  Requests / 24 hour window (user auth)   1,000 and 1 per recipient
  --------------------------------------- ---------------------------

**Note**

Handles can be added to an allowlist to receive more than 1 new feedback
request per 24 hours. Please send a list of \@handles to your account
manager.

## Parameters [¶](#parameters){.headerlink}

+-----------------------------------+-----------------------------------+
| **type** (required)               | The Feedback type. Possible       |
|                                   | values: csat, nps (case           |
|                                   | sensitive)                        |
+-----------------------------------+-----------------------------------+
| **to_user_id** (required)         | The ID of the user who should     |
|                                   | receive the Feedback prompt in a  |
|                                   | direct message.                   |
+-----------------------------------+-----------------------------------+
| **message** (required)            | The Direct Message text used to   |
|                                   | introduce the Feedback prompt.    |
+-----------------------------------+-----------------------------------+
| **privacy_url** (required)        | The URL to the sender's hosted    |
|                                   | privacy policy. The sender is the |
|                                   | business owner of the \@username. |
+-----------------------------------+-----------------------------------+
| **external_id** (optional)        | An open field to track case IDs,  |
|                                   | conversation IDs, etc with a max  |
|                                   | length of 256 characters.         |
+-----------------------------------+-----------------------------------+
| **question_variant_id**           | The ID of the relative question   |
| (optional)                        | variant text that will override   |
|                                   | the default text. See NPS         |
|                                   | Question Variants and CSAT        |
|                                   | Question Variants sections.       |
|                                   | Default value is 0 if not         |
|                                   | provided.                         |
+-----------------------------------+-----------------------------------+
| **display_name** (optional)       | Overrides the display name in the |
|                                   | question text only (i.e. \"How    |
|                                   | likely are you to recommend       |
|                                   | \<display_name\> to a friend?\"   |
|                                   | Max length of 20 characters.)     |
|                                   |                                   |
|                                   | Confirmation messaging uses the   |
|                                   | default Twitter display name from |
|                                   | the business' profile.            |
+-----------------------------------+-----------------------------------+
| **test** (optional)               | Boolean value. Default is false.  |
|                                   | If true, we will exclude this     |
|                                   | feedback from analytics /         |
|                                   | aggregations.                     |
|                                   |                                   |
|                                   | This value should be used for any |
|                                   | testing activity.                 |
+-----------------------------------+-----------------------------------+

## Example Result [¶](#example-result){.headerlink}

    {
      "created_at":"SatDec1517:58:20+00002015",
      "updated_at":"SatDec1517:59:22+00002015",
      "id":"123456789",
      "type":"nps",
      "test":false,
      "dm_id":"8989898989",
      "from_user_id":"1212121212121",
      "to_user_id":"343434343434",
      "privacy_url":"https://my­business.domain/privacy",
      "external_id":"ticket_5555",
      "question_variant_id":"3",
      "display_name":"MyBusinessName"
    }

## NPS Question Variants [¶](#nps-question-variants){.headerlink}

  --- -------------------------------------------------------------------------------
  0   What is your overall satisfaction with \<display_name\>?
  1   How satisfied are you with \<display_name\>?
  2   Overall, how satisfied were you with your recent \<display_name\> experience?
  3   How would you rate the overall experience with \<display_name\>?
  4   How would you rate your overall experience with \<display_name\>?
  5   How would you rate your experience so far with \<display_name\>?
  --- -------------------------------------------------------------------------------

## CSAT Question Variants [¶](#csat-question-variants){.headerlink}

  ---- ---------------------------------------------------------------------------------
  0    What is your overall satisfaction with \<display_name\>?
  1    How satisfied are you with \<display_name\>?
  2    Overall, how satisfied were you with your recent \<display_name\> experience?
  3    How would you rate the overall experience with \<display_name\>?
  4    How would you rate your overall experience with \<display_name\>?
  5    How would you rate your experience so far with \<display_name\>?
  6    How would you rate your experience on Twitter with \<display_name\>?
  7    Were you satisfied with your recent experience with \<display_name\>?
  8    How well does \<display_name\> meet your expectations?
  9    How would you rate your guest experience with \<display_name\>?
  10   How would you rate your service experience with \<display_name\>?
  11   How would you rate your recent service experience with \<display_name\>?
  12   How would you rate the service you received from \<display_name\>?
  13   Were you satisfied with the result of your interaction with \<display_name\>?
  14   How would you rate the ability to resolve your issue with \<display_name\>?
  15   How would you rate the response time from \<display_name\>?
  16   How would you rate the speed of service from \<display_name\>?
  17   How would you rate the time to resolution with \<display_name\>?
  18   How would you rate the time to resolve your issue with \<display_name\>?
  19   How would you rate the speed of resolution with \<display_name\>?
  20   How would you rate the \<display_name\> advisor\'s expertise?
  21   How satisfied were you with the \<display_name\> agent who helped you?
  22   How satisfied were you with the \<display_name\> specialist who helped you?
  23   How satisfied were you with the \<display_name\> representative who helped you?
  24   How would you rate your recent banking experience with \<display_name\>?
  25   How would you rate the overall event experience at \<display_name\>?
  26   How would you rate your bill pay experience with \<display_name\>?
  27   How would you rate your purchase experience with \<display_name\>?
  28   How would you rate your shopping experience with \<display_name\>?
  29   How would you rate your delivery experience with \<display_name\>?
  30   How would you rate your rental experience with \<display_name\>?
  31   How would you rate your recent \<display_name\> store visit?
  32   How would you rate your recent \<display_name\> hotel stay?
  33   How would you rate your recent flight with \<display_name\>?
  34   How would you rate your recent ride with \<display_name\>?
  35   How would you rate your recent trip with \<display_name\>?
  36   How would you rate your recent visit to \<display_name\>?
  37   How would you rate your recent meal at \<display_name\>?
  ---- ---------------------------------------------------------------------------------
:::

</div>
