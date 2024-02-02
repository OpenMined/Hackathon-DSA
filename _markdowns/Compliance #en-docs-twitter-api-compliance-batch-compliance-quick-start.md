::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Working with the batch compliance endpoints generally involves 5 steps:

1.  Creating a compliance job
2.  Preparing the list of Tweet IDs or user IDs
3.  Uploading the list of Tweet IDs or user IDs
4.  Checking the status of the compliance job
5.  Downloading the results

In this section, we will learn how to go through each of these steps
using the command line. If you would like to see sample code in
different programming languages, please visit our [Twitter API v2 sample
code GitHub
repository](https://github.com/twitterdev/Twitter-API-v2-sample-code) .
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
To complete this guide, you will need to have a set of [keys and
tokens](/en/docs/authentication) to authenticate your request. You can
generate these keys and tokens by following these steps:

-   [Sign up for a developer account](/en/apply-for-access) and receive
    approval.
-   Create a [Project](/en/docs/projects) and an associated [developer
    App](/en/docs/apps) in the developer portal.
-   Navigate to your App\'s "Keys and tokens" page to generate the
    required credentials. Make sure to save all credentials in a secure
    location.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
First, you will have to create a compliance job and specify whether you
will be uploading Tweet IDs or user IDs (using the [ type
]{.code-inline} parameter). Optionally, you can also give your job a
name (using the [ name ]{.code-inline} parameter).

To authorize this request, you will need to use [OAuth 2.0
App-Only](/en/docs/authentication/oauth-2-0/application-only) . To do
so, make sure to replace the [ \$APP_ACCESS_TOKEN ]{.code-inline} below
with your [App Access
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) that you can
generate in your [Twitter App](/en/docs/apps) on the developer portal.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl --request POST 'https://api.twitter.com/2/compliance/jobs' \
--header 'Authorization: Bearer $APP_ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{"type": "tweets"}'

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If your API call is successful, you will get a response similar to the
following:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 {
   "data": {
       "download_expires_at": "2021-08-18T19:42:55.000Z",
       "status": "created",
       "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1425543269983784962/submission/1202726487847104512_1425543269983784962?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210811%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210811T194255Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=355e4c4739ae508304d3df15b4e13e64b6c7752d8d79d73676a4d8e60dc5241f83924ad2a1f8b7bddcc768062bb9c64d39b8e8f7cce7f66ffbea9f9ed33a4da975b3a2c127fb738c1c1ff3c3964bd4d9dc0706e6c8a70e67522160ea774e090d2793e06f890d1158ce86be3031c1c471b74f961b6f18743a28730611000336286ad0111b41fb5d14aa813ff00cf06b3572dc68d0b3c6fdc07f25c1b1196c1af4325a9ead68994944bbef0d2123585ea051deb9765aa7f5832446440bc9ba76af327b69df1fd7b1a99bd4419c128f1f697dbbacbc62bbc7c2c9aebc82a2128be0ed05d48a54d814162daad1232a0d13081e9543ab8557f567149af82281193f37",
       "created_at": "2021-08-11T19:42:55.000Z",
       "resumable": false,
       "id": "1425543269983784962",
       "type": "tweets",
       "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1425543269983784962/delivery/1202726487847104512_1425543269983784962?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210811%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210811T194255Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=0a11dd5a3c5adb508f32ce904568abada863dc9499ba2adeafb3452ccee0dcb3dade17910dbc502dcbe54c130ac4d8638eb176c8b7344de068139b06c970794efa6312f0a5149f40da441eafcaf475f670c93ca73951999902a531d34dfab1e5490918929e5b06ae803b5604e0c0c26852255ccdbc79a2c1e2eefe924e5e6bf5b6603a7f287d1621333b9548ec6cc203716070528bebc2e67c12e92b1f4e54471db92c15a54799f2b855ae224250ca44c47993fd7d79a4940a0f68fe09f73fc8b291e88cfd10ade860b4b35c2b964d1777c1d93cd300c313138d9ca90aa8b3ecd3bf9dc73d3ebe32ba7634228fe07e1e4ecdda57cd94c802afc520162735d5a3",
       "upload_expires_at": "2021-08-11T19:57:55.000Z"
   }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Take note of the value from the [ upload_url ]{.code-inline} , [
download_url ]{.code-inline} , and [ id ]{.code-inline} fields; you will
need those in the following steps.
:::
:::

::: c01-rich-text-editor
::: is-table-default
Create a text file with Tweet IDs or user IDs, where each line contains
a Tweet ID or user ID. The contents of the text file can look something
like this:

[ 1417856744319971329 ]{.code-inline}

[ 1415457498803232770 ]{.code-inline}

[ 1415348607813832708 ]{.code-inline}

[ 1413515358766452738 ]{.code-inline}

[ . . . ]{.code-inline}

[ . . . ]{.code-inline}
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Note** : The file above can either contain Tweet IDs or User IDs and
can not be a mix of both.

You can upload your file directly to this URL via a **PUT** request.
Note that the URL is already signed with an authentication token, which
means you will not authenticate by passing your App Access Token again.
Make sure to pass a [ Content-Type ]{.code-inline} header to signal you
are uploading a text file and replace the [ \$FILE_LOCATION
]{.code-inline} below with the path to your file.
:::
:::
:::
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl -X PUT  \
 -H "Content-Type: text/plain" \
 --data-binary @$FILE_LOCATION \
"https://storage.googleapis.com/twitter-compliance/customer_test_object_123456_d8ske9.json?X-Goog-Algorithm=\nGOOG4-RSA-SHA256&X-Goog-Credential=example%40example-project.iam.gserviceaccount\n.com%2F20181026%2Fus-central-1%2Fstorage%2Fgoog4_request&X-Goog-Date=20181026T18\n1309Z&X-Goog-Expires=900&X-Goog-SignedHeaders=host&X-Goog-Signature=247a2aa45f16\n9edf4d187d54e7cc46e4731b1e6273242c4f4c39a1d2507a0e58706e25e3a85a7dbb891d62afa849\n6def8e260c1db863d9ace85ff0a184b894b117fe46d1225c82f2aa19efd52cf21d3e2022b3b868dc\nc1aca2741951ed5bf3bb25a34f5e9316a2841e8ff4c530b22ceaa1c5ce09c7cbb5732631510c2058\n0e61723f5594de3aea497f195456a2ff2bdd0d13bad47289d8611b6f9cfeef0c46c91a455b94e90a\n66924f722292d21e24d31dcfb38ce0c0f353ffa5a9756fc2a9f2b40bc2113206a81e324fc4fd6823\na29163fa845c8ae7eca1fcf6e5bb48b3200983c56c5ca81fffb151cca7402beddfc4a76b13344703\n2ea7abedc098d2eb14a7"
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
A status code [ 200 ]{.code-inline} will indicate that the upload was
successful.

#### Step three (optional): Check your job status

Large uploads may take some time to process. You can request a status
update from the content compliance job endpoint by specifying the job ID
you received in the first step.

Again, make sure to replace the [ \$APP_ACCESS_TOKEN ]{.code-inline}
below with your App Access Token, and replace the [ \$ID ]{.code-inline}
with your job ID from the first step.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl --request GET 'https://api.twitter.com/2/compliance/jobs/$ID' \
--header 'Authorization: Bearer $APP_ACCESS_TOKEN'
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The response will include information about the job.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 {
   "data": {
       "upload_expires_at": "2021-08-05T01:50:11.000Z",
       "type": "tweets",
       "resumable": false,
       "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423095206576984067/delivery/1202726487847104512_1423095206576984067?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=09de4feae68a6d4449eb7ce1f8f3551996552e7fba103005b3bd50ab318bb5215e4f5396ef29d17755deb6bf172b9d1dab61a04b249d39e87f6e2dbb31632b7e5f2d35f4f534e1f1522c9d7958b8745dd62471deb8d6992c80fd418628404f5f14eda3f557adf709403058910ea009e0c88ce81458ec9b915016a5c5901e2365b130db00b18fcb7da1b082e1a5c75f7bf7eeab8783675d1b6a56441ac6e9ffc972b1278a5853d2b94dda55e1a6e2068bc0ddd3cddc9213ec9cebb7cb5be931977bb28dda12c7c5e69d1f876b243f0f224076bf1b81149603319a2fc9cb82337bdbe05e7bbf184bcbdc17d43b3f5efbae72ea386d955ca10e702e00df31aabf32",
       "id": "1423095206576984067",
       "status": "expired",
       "created_at": "2021-08-05T01:35:11.000Z",
       "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423095206576984067/submission/1202726487847104512_1423095206576984067?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=ba08f588bea3873aa0465cf22015e583c2851a5ff14891d22430b1127288728f1aa303673e6895694e7017739871ff5ae59bbcde7d4ac7a14aaaafba98ad22ca818e99fb3ec7eaaf74b3ecfecbfb33711869b2e85d7666609276666ef4a8b396ae9616743a0cbd773962e5850f2942cd76be7373d608a140e041ca8492017d43fac9220fa145d0b2ecaf9f752d71fc8c4b81b67c5c22aa59ac87666f7d83714fdace72894d2911a3e36dd42028d0222e71054d6b28c8ef63d0f0000f228c8680bab9c8011b87d1a6c9a60e8cc9e8b6a83abf7c47a57772746c83b19849f5b4c938ccd0922990da5f2a81ff806edcb4667bb402fb1f1f6f5162768e0661648b21",
       "download_expires_at": "2021-08-12T01:35:11.000Z"
   }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
A [ complete ]{.code-inline} status means the results are ready for you
to download. Note: The other values of statuses can be [ created
]{.code-inline} , [ complete ]{.code-inline} , [ in_progress
]{.code-inline} , [ failed ]{.code-inline} and [ expired ]{.code-inline}

#### Step four: Download the results

As you receive a job completion status, you can download the compliance
results from the URL indicated in the [ download_url ]{.code-inline}
field (also generated in the first step). This URL is already signed
with an authentication token, which means you will not need authenticate
by passing your App Access Token again.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl --request GET \
'https://storage.googleapis.com/twttr-tweet-compliance/1423047488781488129/delivery/1202726487847104512_1423047488781488129?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210804%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210804T222534Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=8ed0fe9e9748f6be5e7e052f6635c8b5cbe62fb2d3a165278b922b28a48fb79b02d74f0bd31b4fdb32532bc6746c6082aaff2154cdab4b59c4c6561ff2c840e5f32dd13c09ff5b52376dfac1b7f97807c72209d2844a6c078b71fddf22a5493f88118802e98a60e16ce5715fce0242baddd17d4598d31be59393e1dacd22fc1eeb532572cc4e784402c5fbeb84a22dd308922e937a26fa99cb717bb26fb61b657403010121a996691814b7aeb00bc05ed25f15d394fd46899dd9390be6d5da44960e81d8018318c325c70b39d0a4fc9d65fea2b8b3355d4c7dd7c386eac1d9c09233462bde40fa3f4023d1cd6470b0346f9f36d74665dde3f716940312019703'
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The result will contain a set of JSON objects (one object per line).
Each object will contain a Tweet or user ID, the Tweet or user's
creation date (useful to locate Tweets organized by date), required
action, the reason for the compliance action, and its date:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 {"id":"1265324480517361664","action":"delete","created_at":"2019-10-29T17:02:47.000Z","redacted_at":"2020-07-29T17:02:47.000Z","reason":"deleted"}
{"id":"1263926741774581761","action":"delete","created_at":"2019-10-29T17:02:47.000Z","redacted_at":"2020-07-29T17:02:47.000Z","reason":"protected"}
{"id":"1265324480517361669","action":"delete","created_at":"2019-10-29T17:02:47.000Z","redacted_at":"2020-07-29T17:02:47.000Z","reason":"suspended"}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Your code can parse each JSON line to locate the Tweet or user ID and
delete the Tweets and users with those IDs from your dataset to stay in
compliance. If there is no corresponding JSON object for an ID you
uploaded, you can assume that ID is in compliance.
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Note** : Not all compliance events will include the [ redacted_at
]{.code-inline} field.
:::
:::
:::
:::
:::
:::
:::
