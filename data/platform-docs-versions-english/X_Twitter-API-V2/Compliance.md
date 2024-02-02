Introduction

Introduction
------------

Twitter is committed to our community of developers who build with the Twitter API. As part of this commitment, we aim to make our API open and fair to developers, safe for people on Twitter, and beneficial for the Twitter platform as a whole. It is crucial that any developer who stores Twitter content offline, ensures the data reflects user intent and the current state of content on Twitter. For example,when someone on Twitter deletes a Tweet or their account, protects their Tweets, or scrubs the geo information from their Tweets, it is critical for both Twitter and our developers to honor that person’s expectations and intent. The batch compliance endpoints provide developers an easy tool to help maintain Twitter data in compliance with the [Twitter Developer Agreement and Policy](https://developer.twitter.com/en/developer-terms/policy). 

These batch compliance endpoints allow you to upload large datasets of Tweet or user IDs to retrieve their compliance status in order to determine what data requires action in order to bring your datasets into compliance. Please note, use of the batch compliance endpoints is restricted to aforementioned use cases, and any other purpose is prohibited and may result in enforcement action.

Typically, there are 4 steps involved in working with this endpoint:

1. **Create a compliance job**  
    You can specify the job type (with the value tweets or users to indicate whether the dataset you want to upload has Tweet IDs or user IDs. You can have one concurrent job per job type at any time.
2. **Upload your dataset to the upload\_url**  
    Next, you upload your dataset as a plain text file to the provided upload\_url, with each line of the file containing a single Tweet ID or user ID. The upload\_url expires after 15 minutes.
3. **(Optional) Check the job status**  
    You can check the status of your compliance job to see whether it is created, in\_progress, failed or complete.
4. **Download the results**  
    When your job is complete, you can download the results using the download\_url. The download\_url expires after one week (from when the job was created).  
      
    This result will contain a set of JSON objects (one object per line). Each object will contain a Tweet ID, the Tweet’s creation date (useful to locate Tweets organized by date), required action, the reason for the compliance action, and the date the user was suspended.

You will receive the following compliance event types in your results:

* deleted - indicates that the Tweet or User account was deleted
* deactivated - indicates that the Tweet or User account has been deactivated
* scrub\_geo - indicates that the geo information associated with the Tweet or User was removed
* protected - indicates the account that made the Tweet became private
* suspended - indicates the account that made the Tweet was suspended

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/quick-start)

[Jump to example requests](https://github.com/twitterdev/Twitter-API-v2-sample-code/tree/main/Batch-Compliance)

[Python client](https://github.com/twitterdev/compliant-client)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/compliance/jobs)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference "Visit the API reference page for this endpoint")

Quick start

Getting started with the batch compliance endpoints
---------------------------------------------------

Working with the batch compliance endpoints generally involves 5 steps:

1. Creating a compliance job
2. Preparing the list of Tweet IDs or user IDs
3. Uploading the list of Tweet IDs or user IDs
4. Checking the status of the compliance job
5. Downloading the results

In this section, we will learn how to go through each of these steps using the command line. If you would like to see sample code in different programming languages, please visit our [Twitter API v2 sample code GitHub repository](https://github.com/twitterdev/Twitter-API-v2-sample-code).

### Prerequisites

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

#### Step one: Create a compliance job

First, you will have to create a compliance job and specify whether you will be uploading Tweet IDs or user IDs (using the type parameter). Optionally, you can also give your job a name (using the name parameter). 

To authorize this request, you will need to use [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only). To do so, make sure to replace the $APP\_ACCESS\_TOKEN below with your [App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) that you can generate in your [Twitter App](https://developer.twitter.com/en/docs/apps) on the developer portal.

      `curl --request POST 'https://api.twitter.com/2/compliance/jobs' \ --header 'Authorization: Bearer $APP_ACCESS_TOKEN' \ --header 'Content-Type: application/json' \ --data-raw '{"type": "tweets"}'`
    

If your API call is successful, you will get a response similar to the following:

      `{    "data": {        "download_expires_at": "2021-08-18T19:42:55.000Z",        "status": "created",        "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1425543269983784962/submission/1202726487847104512_1425543269983784962?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210811%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210811T194255Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=355e4c4739ae508304d3df15b4e13e64b6c7752d8d79d73676a4d8e60dc5241f83924ad2a1f8b7bddcc768062bb9c64d39b8e8f7cce7f66ffbea9f9ed33a4da975b3a2c127fb738c1c1ff3c3964bd4d9dc0706e6c8a70e67522160ea774e090d2793e06f890d1158ce86be3031c1c471b74f961b6f18743a28730611000336286ad0111b41fb5d14aa813ff00cf06b3572dc68d0b3c6fdc07f25c1b1196c1af4325a9ead68994944bbef0d2123585ea051deb9765aa7f5832446440bc9ba76af327b69df1fd7b1a99bd4419c128f1f697dbbacbc62bbc7c2c9aebc82a2128be0ed05d48a54d814162daad1232a0d13081e9543ab8557f567149af82281193f37",        "created_at": "2021-08-11T19:42:55.000Z",        "resumable": false,        "id": "1425543269983784962",        "type": "tweets",        "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1425543269983784962/delivery/1202726487847104512_1425543269983784962?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210811%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210811T194255Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=0a11dd5a3c5adb508f32ce904568abada863dc9499ba2adeafb3452ccee0dcb3dade17910dbc502dcbe54c130ac4d8638eb176c8b7344de068139b06c970794efa6312f0a5149f40da441eafcaf475f670c93ca73951999902a531d34dfab1e5490918929e5b06ae803b5604e0c0c26852255ccdbc79a2c1e2eefe924e5e6bf5b6603a7f287d1621333b9548ec6cc203716070528bebc2e67c12e92b1f4e54471db92c15a54799f2b855ae224250ca44c47993fd7d79a4940a0f68fe09f73fc8b291e88cfd10ade860b4b35c2b964d1777c1d93cd300c313138d9ca90aa8b3ecd3bf9dc73d3ebe32ba7634228fe07e1e4ecdda57cd94c802afc520162735d5a3",        "upload_expires_at": "2021-08-11T19:57:55.000Z"    } }`
    

Take note of the value from the upload\_url, download\_url, and id fields; you will need those in the following steps.

#### Step two: Prepare a list of Tweet IDs or user IDs

Create a text file with Tweet IDs or user IDs, where each line contains a Tweet ID or user ID. The contents of the text file can look something like this:

1417856744319971329

1415457498803232770

1415348607813832708

1413515358766452738

. . .

. . .

**Note**: The file above can either contain Tweet IDs or User IDs and can not be a mix of both.

You can upload your file directly to this URL via a **PUT** request. Note that the URL is already signed with an authentication token, which means you will not authenticate by passing your App Access Token again. Make sure to pass a Content-Type header to signal you are uploading a text file and replace the $FILE\_LOCATION below with the path to your file.

      `curl -X PUT  \  -H "Content-Type: text/plain" \  --data-binary @$FILE_LOCATION \ "https://storage.googleapis.com/twitter-compliance/customer_test_object_123456_d8ske9.json?X-Goog-Algorithm=\nGOOG4-RSA-SHA256&X-Goog-Credential=example%40example-project.iam.gserviceaccount\n.com%2F20181026%2Fus-central-1%2Fstorage%2Fgoog4_request&X-Goog-Date=20181026T18\n1309Z&X-Goog-Expires=900&X-Goog-SignedHeaders=host&X-Goog-Signature=247a2aa45f16\n9edf4d187d54e7cc46e4731b1e6273242c4f4c39a1d2507a0e58706e25e3a85a7dbb891d62afa849\n6def8e260c1db863d9ace85ff0a184b894b117fe46d1225c82f2aa19efd52cf21d3e2022b3b868dc\nc1aca2741951ed5bf3bb25a34f5e9316a2841e8ff4c530b22ceaa1c5ce09c7cbb5732631510c2058\n0e61723f5594de3aea497f195456a2ff2bdd0d13bad47289d8611b6f9cfeef0c46c91a455b94e90a\n66924f722292d21e24d31dcfb38ce0c0f353ffa5a9756fc2a9f2b40bc2113206a81e324fc4fd6823\na29163fa845c8ae7eca1fcf6e5bb48b3200983c56c5ca81fffb151cca7402beddfc4a76b13344703\n2ea7abedc098d2eb14a7"`
    

A status code 200 will indicate that the upload was successful.

#### Step three (optional): Check your job status

Large uploads may take some time to process. You can request a status update from the content compliance job endpoint by specifying the job ID you received in the first step.

Again, make sure to replace the $APP\_ACCESS\_TOKEN below with your App Access Token, and replace the $ID with your job ID from the first step.

      `curl --request GET 'https://api.twitter.com/2/compliance/jobs/$ID' \ --header 'Authorization: Bearer $APP_ACCESS_TOKEN'`
    

The response will include information about the job.

      `{    "data": {        "upload_expires_at": "2021-08-05T01:50:11.000Z",        "type": "tweets",        "resumable": false,        "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423095206576984067/delivery/1202726487847104512_1423095206576984067?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=09de4feae68a6d4449eb7ce1f8f3551996552e7fba103005b3bd50ab318bb5215e4f5396ef29d17755deb6bf172b9d1dab61a04b249d39e87f6e2dbb31632b7e5f2d35f4f534e1f1522c9d7958b8745dd62471deb8d6992c80fd418628404f5f14eda3f557adf709403058910ea009e0c88ce81458ec9b915016a5c5901e2365b130db00b18fcb7da1b082e1a5c75f7bf7eeab8783675d1b6a56441ac6e9ffc972b1278a5853d2b94dda55e1a6e2068bc0ddd3cddc9213ec9cebb7cb5be931977bb28dda12c7c5e69d1f876b243f0f224076bf1b81149603319a2fc9cb82337bdbe05e7bbf184bcbdc17d43b3f5efbae72ea386d955ca10e702e00df31aabf32",        "id": "1423095206576984067",        "status": "expired",        "created_at": "2021-08-05T01:35:11.000Z",        "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423095206576984067/submission/1202726487847104512_1423095206576984067?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=ba08f588bea3873aa0465cf22015e583c2851a5ff14891d22430b1127288728f1aa303673e6895694e7017739871ff5ae59bbcde7d4ac7a14aaaafba98ad22ca818e99fb3ec7eaaf74b3ecfecbfb33711869b2e85d7666609276666ef4a8b396ae9616743a0cbd773962e5850f2942cd76be7373d608a140e041ca8492017d43fac9220fa145d0b2ecaf9f752d71fc8c4b81b67c5c22aa59ac87666f7d83714fdace72894d2911a3e36dd42028d0222e71054d6b28c8ef63d0f0000f228c8680bab9c8011b87d1a6c9a60e8cc9e8b6a83abf7c47a57772746c83b19849f5b4c938ccd0922990da5f2a81ff806edcb4667bb402fb1f1f6f5162768e0661648b21",        "download_expires_at": "2021-08-12T01:35:11.000Z"    } }`
    

A complete status means the results are ready for you to download. Note: The other values of statuses can be created, complete, in\_progress, failed and expired

#### Step four: Download the results

As you receive a job completion status, you can download the compliance results from the URL indicated in the download\_url field (also generated in the first step). This URL is already signed with an authentication token, which means you will not need authenticate by passing your App Access Token again.

      `curl --request GET \ 'https://storage.googleapis.com/twttr-tweet-compliance/1423047488781488129/delivery/1202726487847104512_1423047488781488129?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210804%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210804T222534Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=8ed0fe9e9748f6be5e7e052f6635c8b5cbe62fb2d3a165278b922b28a48fb79b02d74f0bd31b4fdb32532bc6746c6082aaff2154cdab4b59c4c6561ff2c840e5f32dd13c09ff5b52376dfac1b7f97807c72209d2844a6c078b71fddf22a5493f88118802e98a60e16ce5715fce0242baddd17d4598d31be59393e1dacd22fc1eeb532572cc4e784402c5fbeb84a22dd308922e937a26fa99cb717bb26fb61b657403010121a996691814b7aeb00bc05ed25f15d394fd46899dd9390be6d5da44960e81d8018318c325c70b39d0a4fc9d65fea2b8b3355d4c7dd7c386eac1d9c09233462bde40fa3f4023d1cd6470b0346f9f36d74665dde3f716940312019703'`
    

The result will contain a set of JSON objects (one object per line). Each object will contain a Tweet or user ID, the Tweet or user’s creation date (useful to locate Tweets organized by date), required action, the reason for the compliance action, and its date:

      `{"id":"1265324480517361664","action":"delete","created_at":"2019-10-29T17:02:47.000Z","redacted_at":"2020-07-29T17:02:47.000Z","reason":"deleted"} {"id":"1263926741774581761","action":"delete","created_at":"2019-10-29T17:02:47.000Z","redacted_at":"2020-07-29T17:02:47.000Z","reason":"protected"} {"id":"1265324480517361669","action":"delete","created_at":"2019-10-29T17:02:47.000Z","redacted_at":"2020-07-29T17:02:47.000Z","reason":"suspended"}`
    

Your code can parse each JSON line to locate the Tweet or user ID and delete the Tweets and users with those IDs from your dataset to stay in compliance. If there is no corresponding JSON object for an ID you uploaded, you can assume that ID is in compliance.

**Note**: Not all compliance events will include the redacted\_atfield.

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Integrate

Working with resumable uploads
------------------------------

When using the Batch compliance endpoints, developers can batch upload large amounts of Twitter data and understand what action is needed to ensure that their datasets reflect user intent and the current state of the content on Twitter. Uploading large amounts of data to a remote server is a relatively straightforward operation when systems and connectivity are stable and reliable. However, this may not always be the case. Some environments may impose a connection timeout, effectively cutting the connection between your app and the upload server after a set amount of time; you may also encounter connection issues, for example when trying to upload a large file from your laptop over a wi-fi connection. In these circumstances, it’s desirable to upload smaller portions of that file at a time, rather than having one single continuous connection.

Twitter’s batch compliance endpoints rely on Google Cloud Storage to process large files. This type of storage is optimized for various applications; Cloud Storage supports a technique to manage large files called resumable uploads.

If the upload goes wrong at any point, Google Cloud Storage is able to resume the operation from where it was left off.

### Creating a resumable job

#### Step one:

First, you will have to create a compliance job and specify whether you will be uploading Tweet IDs or user IDs (using the type parameter). Additionally, add resumable to the body and set it to true. Make sure to replace the $BEARER\_TOKEN below with your bearer token below.

      `curl --request POST \  'https://api.twitter.com/2/compliance/jobs' --header 'Authorization: Bearer $BEARER_TOKEN --header 'Content-Type: application/json' --data-raw '{    "type": "tweets",    "resumable": true }'`
    

If your API call is successful, you will get a response similar to the following:

      `{    "data": {        "download_expires_at": "2021-08-18T19:42:55.000Z",        "status": "created",        "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1425543269983784962/submission/1202726487847104512_1425543269983784962?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210811%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210811T194255Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=355e4c4739ae508304d3df15b4e13e64b6c7752d8d79d73676a4d8e60dc5241f83924ad2a1f8b7bddcc768062bb9c64d39b8e8f7cce7f66ffbea9f9ed33a4da975b3a2c127fb738c1c1ff3c3964bd4d9dc0706e6c8a70e67522160ea774e090d2793e06f890d1158ce86be3031c1c471b74f961b6f18743a28730611000336286ad0111b41fb5d14aa813ff00cf06b3572dc68d0b3c6fdc07f25c1b1196c1af4325a9ead68994944bbef0d2123585ea051deb9765aa7f5832446440bc9ba76af327b69df1fd7b1a99bd4419c128f1f697dbbacbc62bbc7c2c9aebc82a2128be0ed05d48a54d814162daad1232a0d13081e9543ab8557f567149af82281193f37",        "created_at": "2021-08-11T19:42:55.000Z",        "resumable": false,        "id": "1425543269983784962",        "type": "tweets",        "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1425543269983784962/delivery/1202726487847104512_1425543269983784962?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210811%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210811T194255Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=0a11dd5a3c5adb508f32ce904568abada863dc9499ba2adeafb3452ccee0dcb3dade17910dbc502dcbe54c130ac4d8638eb176c8b7344de068139b06c970794efa6312f0a5149f40da441eafcaf475f670c93ca73951999902a531d34dfab1e5490918929e5b06ae803b5604e0c0c26852255ccdbc79a2c1e2eefe924e5e6bf5b6603a7f287d1621333b9548ec6cc203716070528bebc2e67c12e92b1f4e54471db92c15a54799f2b855ae224250ca44c47993fd7d79a4940a0f68fe09f73fc8b291e88cfd10ade860b4b35c2b964d1777c1d93cd300c313138d9ca90aa8b3ecd3bf9dc73d3ebe32ba7634228fe07e1e4ecdda57cd94c802afc520162735d5a3",        "upload_expires_at": "2021-08-11T19:57:55.000Z"    } }`
    

Take note of the value from the upload\_url, you will need it in the following steps.

#### Step two: 

Next, you will need to initiate the resumable upload. In order to do so, make a **POST** call to the upload\_url from the previous step and make sure to include the following headers:

Content-Type: text/plain

Content-Length: 0

x-goog-resumable: start

      `curl --request POST \ 'https://storage.googleapis.com/twttr-tweet-compliance/1430227686685757442/submission/1202726487847104512_1430227686685757442?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210824%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210824T175707Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-length%3Bcontent-type%3Bhost%3Bx-goog-resumable&X-Goog-Signature=890d958f9c7dcb7f238e4971b59da5afc5b8329fb197c67b5930fe0f9dfe180afe2d4bec341111809b88ccfab46ab1f81f4242abc1af7b67c6e8977c52e6d486f5f43ce6a37a7a6530d25f15e2bcd9bb54655fe4ee22b26f8886ba71b67b7b11afd1198d658d1b6f0c41260f55260a260e1be0239977feba43dce40bc0e8e6293a4a3a3f7ee0afc74d3d2f7f2d3d514f108d5887a52ac85760385e5b9bb67cd26bfcf6b1c19151ea8111e217a29407722dc0dc9ab373334e88c18159546237ec9334f9a1e33717dc82800c6a45bba82706d5aece84ecdf3fcac52b21c8a3085a639047cf2707a8b9e4c296fc7cf05edbb110f07b89e38f0f5ea77e8b313cade7' \ --header 'Content-Type: text/plain' --header \  'Content-Length: 0' --header \  'x-goog-resumable: start`
    

If this call is successful, you will get a 201 response code. Then, in the response header, copy the value for the location header which will look something like this:

      `https://storage.googleapis.com/twttr-tweet-compliance/1430227686685757442/submission/1202726487847104512_1430227686685757442?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210824%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210824T175707Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-length%3Bcontent-type%3Bhost%3Bx-goog-resumable&X-Goog-Signature=890d958f9c7dcb7f238e4971b59da5afc5b8329fb197c67b5930fe0f9dfe180afe2d4bec341111809b88ccfab46ab1f81f4242abc1af7b67c6e8977c52e6d486f5f43ce6a37a7a6530d25f15e2bcd9bb54655fe4ee22b26f8886ba71b67b7b11afd1198d658d1b6f0c41260f55260a260e1be0239977feba43dce40bc0e8e6293a4a3a3f7ee0afc74d3d2f7f2d3d514f108d5887a52ac85760385e5b9bb67cd26bfcf6b1c19151ea8111e217a29407722dc0dc9ab373334e88c18159546237ec9334f9a1e33717dc82800c6a45bba82706d5aece84ecdf3fcac52b21c8a3085a639047cf2707a8b9e4c296fc7cf05edbb110f07b89e38f0f5ea77e8b313cade7&upload_id=ADPycds-_Ow7aqcpbG4XguXSVAgd_2fy-XiDA2qm-It9PCwBlZhF4e2bfOAQzEmRJ4T_l6jU6LfYdfrKa_KlFFBOyx3PjYzrxQ`
    

You can then upload your Tweet or User IDs to this location by following step two onwards, [from the quick start guide](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/compliance/batch-compliance/quick-start).

  
Because of their technical complexity, resumable uploads are best used in conjunction with code. This guide will use Node.js with the [needle request library](https://www.npmjs.com/package/needle).

### Install the dependencies

Before proceeding, you should have a Node.js environment installed; you can obtain Node.js from its website. Once installed, Node.js will contain a utility called npm; make sure both Node and npm are installed by calling the following command, and ensure it doesn’t result in an error.

      `$ npm -v 6.4.1`
    

A version number similar to this signifies your environment is ready (note that your version number may differ). We will use npm to install the upload library. Run this command:

      `$ npm install -g needle`
    

You’re all set; there is no additional configuration required.

#### Request a resumable destination

When creating a new job, set the resumable parameter to true so you can get a destination that supports a resumable upload. In the response payload, you will receive an upload\_url value.

      `"upload_url":\ "https://storage.googleapis.com/compliance_tweet_ids/customer_test_object_12950882_GlYjiE?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=193969463581-compute%40developer.gserviceaccount.com%2F20200618%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20200618T184154Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=b7bdcf32479b08715be91ed47b06471b8acdcdb319f8e4f423bf3a3056dfa03ed83e47446f33338e292967a15c08fa5ba34395edaf057a2ac975b88e710ca994adb023a9e1673a7c58ce2fa0d73537f72812af78e92b708dfe6b907a7d75bd0f6cfa61fec867e80ac83ced0725d1ee59787c9dbca50d41f7b0f513dad63a7564136b1a70042a2ec6ba6b697cbe480a4405362f7a08255a5e8205aa7baa562f99e6a092f0420f33d67ffaeb132f877fbaf16c969630b5f173e8a3f31c473707241fa4e28f4bed13fb2ea01d3af1c449321a2e6ee9ec1e331b447cabcfc6f9d1f99f564d180f0cc1d28ea54972c996102c67c6501c6c16a00c13d17756f960e0e1"`
    

#### Prepare the code to upload a file

By default, the library will create a new upload destination by accepting an upload location (called bucket) and the name of the file you wish to upload. Because the batch compliance endpoints create their own destination, we will need to tell the library we already have a location ready to accept our upload. 

  
We will need to pass this value to the upload library, along with the name of the file containing the data to upload. Create a file, and name it _**twitter-upload.js**_. Add the following code:

      ``const needle = require('needle'); const fs = require('fs'); const path = require('path');  const [, scriptName, filename, uploadURL] = process.argv; if (!filename || !uploadURL) {   console.error(`Usage: node ${path.basename(scriptName)} filename upload_url`);   process.exit(-1); }  async function uploadFile(file, url) {   // rangeEnd is the index of the last byte in the file, i.e. number of bytes in file   const rangeEnd = (await fs.promises.stat(file)).size;      let options = {     headers: {       'Content-Range': `bytes */${rangeEnd}`,     },   };      const response = await needle('put', url, null, options);    switch (response.statusCode) {     case 200:     case 201:       console.log('Upload complete');       return;     case 308:       return resumeUpload(response, file, url);     default:        console.log('Got unexpected response code: ', response.statusCode);       return;   } }  async function resumeUpload(response, file, url) {   console.log('Upload not completed, resuming');   if (response.headers.range) {           let resumeOffset = Number(response.headers.range.split('-')[1]) + 1;          let options = {       headers: {         'Content-Range': `bytes ${resumeOffset}-${rangeEnd-1}/${rangeEnd}`,         'Content-Length': `${rangeEnd-resumeOffset}`,       },     };          let readStream = fs.createReadStream(file, {start: resumeOffset});     return needle('put', url, readStream, options);   } else {     console.log('Initiating upload');     let options = {       headers: {         'Content-Type': 'text/plain'       }     };          let readStream = fs.createReadStream(file);     return needle('put', url, readStream, options);   } }  // Request resumable session URL async function requestResumableSession(url) {   const options = {     headers: {       'Content-Type': 'text/plain',       'Content-Length': '0',       'x-goog-resumable': 'start',     },   };    const res = await needle('post', url, null, options);   if (res.statusCode === 201) {     const resumableSessionURL = res.headers['location'];     console.log('Starting upload to: ', resumableSessionURL);          await uploadFile(filename, resumableSessionURL);   } else {     console.log('Failed to create resumable session URI');   }    }  requestResumableSession(uploadURL).then(result => console.log('Upload complete'));``
    

Save the file wherever it makes the most sense. Next, in your command line, invoke the script and pass two parameters:

1. The first will be the location of the file (with the Tweet or User IDs) that you wish to upload.
2. The second will be the upload URL we received from the compliance endpoint response.

Ensure the URL is surrounded in double-quotes, and do the same for your file name if it contains spaces or other characters:  

      `node twitter-upload.js compliance_upload.txt\ "https://storage.googleapis.com/compliance_tweet_ids/customer_test_object_12950882_GlYjiE?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=193969463581-compute%40developer.gserviceaccount.com%2F20200618%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20200618T184154Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=b7bdcf32479b08715be91ed47b06471b8acdcdb319f8e4f423bf3a3056dfa03ed83e47446f33338e292967a15c08fa5ba34395edaf057a2ac975b88e710ca994adb023a9e1673a7c58ce2fa0d73537f72812af78e92b708dfe6b907a7d75bd0f6cfa61fec867e80ac83ced0725d1ee59787c9dbca50d41f7b0f513dad63a7564136b1a70042a2ec6ba6b697cbe480a4405362f7a08255a5e8205aa7baa562f99e6a092f0420f33d67ffaeb132f877fbaf16c969630b5f173e8a3f31c473707241fa4e28f4bed13fb2ea01d3af1c449321a2e6ee9ec1e331b447cabcfc6f9d1f99f564d180f0cc1d28ea54972c996102c67c6501c6c16a00c13d17756f960e0e1"`
    

You will see output similar to this:

      `Starting upload to:  https://storage.googleapis.com/twttr-tweet-compliance/<redacted> Upload not completed, resuming Initiating upload`
    

You can pause the upload at any time by pressing Ctrl + C or closing your command line. You will be able to resume the upload from where you left off when you invoke the same command at a later stage. Once the file has been completely uploaded, you will see the following message:

      `Upload complete`
    

At this point, you will be able to use the [compliance status endpoint](https://developer-staging.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs-id) to check on the status of your compliance job, and you will be able to download the compliance result when complete.

Next steps
----------

[Visit the API reference page to customize your request](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference "Visit the API reference page to customize your request")

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list:

|     |     |
| --- | --- |
| **Creates a new compliance job** | `[POST /2/compliance/jobs](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/post-compliance-jobs)` |
| **Returns status and download information about a specified compliance job** | `[GET /2/compliance/jobs/:job_id](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs-id)` |
| **Returns a list of recent compliance jobs** | [GET /2/compliance/jobs](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs) |

GET /2/compliance/jobs/:id

GET /2/compliance/jobs/:id
==========================

Get a single compliance job with the specified ID.

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fcompliance%2Fjobs%2F%7Bid%7D&method=get) 

### Endpoint URL

`https://api.twitter.com/2/compliance/jobs/:id`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 150 requests per 15-minute window shared among all users of your app |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | number | The unique identifier for the compliance job you want to retrieve. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const getComplianceJob =       await twitterClient.compliance.getBatchComplianceJob(         //ID of the compliance job to retrieve         1382081613278814209       );     console.dir(getComplianceJob, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | ID of the compliance job to retrieve. String id = "1382081613278814209";  try {     SingleComplianceJobResponse result = apiInstance.compliance().getBatchComplianceJob(id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ComplianceApi#getBatchComplianceJob");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "download_expires_at": "2021-08-12T01:35:11.000Z",     "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423095206576984067/delivery/1202726487847104512_1423095206576984067?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=09de4feae68a6d4449eb7ce1f8f3551996552e7fba103005b3bd50ab318bb5215e4f5396ef29d17755deb6bf172b9d1dab61a04b249d39e87f6e2dbb31632b7e5f2d35f4f534e1f1522c9d7958b8745dd62471deb8d6992c80fd418628404f5f14eda3f557adf709403058910ea009e0c88ce81458ec9b915016a5c5901e2365b130db00b18fcb7da1b082e1a5c75f7bf7eeab8783675d1b6a56441ac6e9ffc972b1278a5853d2b94dda55e1a6e2068bc0ddd3cddc9213ec9cebb7cb5be931977bb28dda12c7c5e69d1f876b243f0f224076bf1b81149603319a2fc9cb82337bdbe05e7bbf184bcbdc17d43b3f5efbae72ea386d955ca10e702e00df31aabf32",     "resumable": false,     "upload_expires_at": "2021-08-05T01:50:11.000Z",     "created_at": "2021-08-05T01:35:11.000Z",     "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423095206576984067/submission/1202726487847104512_1423095206576984067?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=ba08f588bea3873aa0465cf22015e583c2851a5ff14891d22430b1127288728f1aa303673e6895694e7017739871ff5ae59bbcde7d4ac7a14aaaafba98ad22ca818e99fb3ec7eaaf74b3ecfecbfb33711869b2e85d7666609276666ef4a8b396ae9616743a0cbd773962e5850f2942cd76be7373d608a140e041ca8492017d43fac9220fa145d0b2ecaf9f752d71fc8c4b81b67c5c22aa59ac87666f7d83714fdace72894d2911a3e36dd42028d0222e71054d6b28c8ef63d0f0000f228c8680bab9c8011b87d1a6c9a60e8cc9e8b6a83abf7c47a57772746c83b19849f5b4c938ccd0922990da5f2a81ff806edcb4667bb402fb1f1f6f5162768e0661648b21",     "id": "1423095206576984067",     "type": "tweets",     "status": "expired"   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | The unique identifier for this job. |
| `created_at` | date (ISO 8601) | The date and time when the job was created. |
| `type` | enum (`tweets`, `users`) | The type of the job, whether tweets or users. |
| `name` | string | The user defined job name. Only returned if specified when the job was created. |
| `upload_url` | string | A URL representing the location where to upload IDs consumed by your app. This URL is already signed with an authentication key, so you will not need to pass any additional credentials or headers to authenticate the request. |
| `upload_expires_at` | date (ISO 8601) | The date and time until which the upload URL will be available (usually 15 minutes from the request time). |
| `download_url` | string | The predefined location where to download the results from the compliance job. This URL is already signed with an authentication key, so you will not need to pass any additional credential or header to authenticate the request. |
| `download_expires_at` | date (ISO 8601) | The date and time until which the download URL will be available (usually 7 days from the request time). |
| `error` | string | Only returned when `jobs.status` is `failed`. Specifies the reason why the job did not complete successfully. |

GET /2/compliance/jobs

GET /2/compliance/jobs
======================

Returns a list of recent compliance jobs.

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fcompliance%2Fjobs&method=get) 

### Endpoint URL

`https://api.twitter.com/2/compliance/jobs`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 150 requests per 15-minute window shared among all users of your app |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `type`  <br> Required | enum (`tweets`, `users`) | Allows to filter by job type - either by tweets or user ID. Only one filter (tweets or users) can be specified per request. |
| `status`  <br> Optional | enum (`created`, `in_progress`, `failed`, `complete`) | Allows to filter by job status. Only one filter can be specified per request.  <br>Default: `all` |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const getListComplianceJobs =       await twitterClient.compliance.listBatchComplianceJobs({         type: "tweets", // type value can be "tweets" or "users"         status: "created", // status values can be "created", "in_progress", "completed" or "failed"       });     console.dir(getListComplianceJobs, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // ComplianceJobType | Type of compliance job to list ComplianceJobType type = ComplianceJobType.fromValue("tweets");  // ComplianceJobStatus | Status of compliance job to list ComplianceJobStatus status = ComplianceJobStatus.fromValue("created"); try {     MultiComplianceJobResponse result = apiInstance.compliance().listBatchComplianceJobs(type, status);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ComplianceApi#listBatchComplianceJobs");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": [     {       "type": "tweets",       "id": "1421185651106480129",       "resumable": false,       "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1421185651106480129/submission/1202726487847104512_1421185651106480129?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210730%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210730T190718Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=5c197d6e2b54cd941006904d7f96a3ac4985f19b5b770c4b334d4defe495ccebda71650d8636fcfc7266b8e609c0de29255b6b46bf1ad883522fac78010a2936fdd46dd3afa1925a674311b51e1d6d19ab249aa51cc6d1afb65203847a1f998be41aff209d465d74d20b4b26898951035808afd5bd022445d0aeb7ffd8aa20486ee1b3e2ea3b6f9709dfd849fbdfacfb1542dca965d8473e6bfc9596df85fd1be716dd7ebbb4c6b995a0775472145bd778ec4175f2934f2823b21bba6604696301168e55d614098512ffee2bd1b0e363106fc6197e15d833c41bf83598dc4ce7e7f7e2edea0c07e3a55f815e1e28abeb5a24a3e5768fbaa70cf19e85c269d530",       "upload_expires_at": "2021-07-30T19:22:18.000Z",       "download_expires_at": "2021-08-06T19:07:18.000Z",       "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1421185651106480129/delivery/1202726487847104512_1421185651106480129?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=09de4feae68a6d4449eb7ce1f8f3551996552e7fba103005b3bd50ab318bb5215e4f5396ef29d17755deb6bf172b9d1dab61a04b249d39e87f6e2dbb31632b7e5f2d35f4f534e1f1522c9d7958b8745dd62471deb8d6992c80fd418628404f5f14eda3f557adf709403058910ea009e0c88ce81458ec9b915016a5c5901e2365b130db00b18fcb7da1b082e1a5c75f7bf7eeab8783675d1b6a56441ac6e9ffc972b1278a5853d2b94dda55e1a6e2068bc0ddd3cddc9213ec9cebb7cb5be931977bb28dda12c7c5e69d1f876b243f0f224076bf1b81149603319a2fc9cb82337bdbe05e7bbf184bcbdc17d43b3f5efbae72ea386d955ca10e702e00df31aabf32",       "created_at": "2021-07-30T19:07:18.000Z",       "status": "complete"     },     {       "type": "tweets",       "id": "1423095206576984067",       "resumable": false,       "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423095206576984067/submission/1202726487847104512_1423095206576984067?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=ba08f588bea3873aa0465cf22015e583c2851a5ff14891d22430b1127288728f1aa303673e6895694e7017739871ff5ae59bbcde7d4ac7a14aaaafba98ad22ca818e99fb3ec7eaaf74b3ecfecbfb33711869b2e85d7666609276666ef4a8b396ae9616743a0cbd773962e5850f2942cd76be7373d608a140e041ca8492017d43fac9220fa145d0b2ecaf9f752d71fc8c4b81b67c5c22aa59ac87666f7d83714fdace72894d2911a3e36dd42028d0222e71054d6b28c8ef63d0f0000f228c8680bab9c8011b87d1a6c9a60e8cc9e8b6a83abf7c47a57772746c83b19849f5b4c938ccd0922990da5f2a81ff806edcb4667bb402fb1f1f6f5162768e0661648b21",       "upload_expires_at": "2021-08-05T01:50:11.000Z",       "download_expires_at": "2021-08-12T01:35:11.000Z",       "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423095206576984067/delivery/1202726487847104512_1423095206576984067?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=09de4feae68a6d4449eb7ce1f8f3551996552e7fba103005b3bd50ab318bb5215e4f5396ef29d17755deb6bf172b9d1dab61a04b249d39e87f6e2dbb31632b7e5f2d35f4f534e1f1522c9d7958b8745dd62471deb8d6992c80fd418628404f5f14eda3f557adf709403058910ea009e0c88ce81458ec9b915016a5c5901e2365b130db00b18fcb7da1b082e1a5c75f7bf7eeab8783675d1b6a56441ac6e9ffc972b1278a5853d2b94dda55e1a6e2068bc0ddd3cddc9213ec9cebb7cb5be931977bb28dda12c7c5e69d1f876b243f0f224076bf1b81149603319a2fc9cb82337bdbe05e7bbf184bcbdc17d43b3f5efbae72ea386d955ca10e702e00df31aabf32",       "created_at": "2021-08-05T01:35:11.000Z",       "status": "expired"     }   ] }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | The unique identifier for this job. |
| `created_at` | date (ISO 8601) | The date and time when the job was created. |
| `type` | enum (`tweets`, `users`) | The type of the job, whether tweets or users. |
| `name` | string | The user defined job name. Only returned if specified when the job was created. |
| `upload_url` | string | A URL representing the location where to upload IDs consumed by your app. This URL is already signed with an authentication key, so you will not need to pass any additional credentials or headers to authenticate the request. |
| `upload_expires_at` | date (ISO 8601) | The date and time until which the upload URL will be available (usually 15 minutes from the request time). |
| `download_url` | string | The predefined location where to download the results from the compliance job. This URL is already signed with an authentication key, so you will not need to pass any additional credential or header to authenticate the request. |
| `download_expires_at` | date (ISO 8601) | The date and time until which the download URL will be available (usually 7 days from the request time). |
| `status` | enum (`in_progress`, `failed`, `complete`) | Current status of this job. |
| `error` | string | Only returned when `jobs.status` is `failed`. Specifies the reason why the job did not complete successfully. |

POST /2/compliance/jobs

POST /2/compliance/jobs
=======================

"Creates a new compliance job for Tweet IDs or user IDs.  
  
A compliance job will contain an ID and a destination URL. The destination URL represents the location that contains the list of IDs consumed by your App.  
  
You can run one batch job at a time."

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Fcompliance%2Fjobs&method=post) 

### Endpoint URL

`https://api.twitter.com/2/compliance/jobs`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 150 requests per 15-minute window shared among all users of your app |

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `type`  <br> Required | enum (`tweets`, `users`) | Specify whether you will be uploading tweet or user IDs. You can either specify tweets or users. |
| `name`  <br> Optional | string | A name for this job, useful to identify multiple jobs using a label you define. |
| `resumable`  <br> Optional | boolean | Specifies whether to enable the upload URL with support for resumable uploads. If true, this endpoint will return a pre-signed URL with resumable uploads enabled. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const createComplianceJob =       await twitterClient.compliance.createBatchComplianceJob({         type: "tweets", // Type of compliance job to create - value can be "tweets" or "users"         resumable: true, //Optional - Specifies whether to enable the upload URL with support for resumable uploads. If true, this endpoint will return a pre-signed URL with resumable uploads enabled.         name: "Job name", //Optional - A name for this job, useful to identify multiple jobs using a label you define.       });     console.dir(createComplianceJob, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  CreateBatchComplianceJobRequest createBatchComplianceJobRequest = new CreateBatchComplianceJobRequest();  //ComplianceJobType | Type of compliance job to create ComplianceJobType jobType = ComplianceJobType.fromValue("tweets");  createBatchComplianceJobRequest.type(jobType);  //Optional - A name for this job, useful to identify multiple jobs using a label you define. createBatchComplianceJobRequest.name("job name");  //Optional - Specifies whether to enable the upload URL with support for resumable uploads. If true, this endpoint will return a pre-signed URL with resumable uploads enabled. createBatchComplianceJobRequest.resumable(true);  try {     SingleComplianceJobResponse result = apiInstance.compliance().createBatchComplianceJob(createBatchComplianceJobRequest);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ComplianceApi#createBatchComplianceJob");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "resumable": false,     "type": "tweets",     "download_expires_at": "2021-08-13T17:04:26.000Z",     "created_at": "2021-08-06T17:04:26.000Z",     "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423691444842209280/submission/1202726487847104512_1423691444842209280?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210806%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210806T170426Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=b057f9d07f80c7d4d73dc1184e2801e495054f61ff48ee1f6a74b7125bb62b02f3afa66a445e57634a0e78a546308632d845e28e092c10ae90cadb8655b0daafcee9ec8c7d95d2099437117db61d6789c8334e55ce5ee7b76c0d7dd383bd270d0c5a266ebbe0aa51365b332fe2c04942937526102871faa72e9255d2a8683d2dadcbd5ece0de18144a6dc74a6a53cdd4e5bb98261032047bf7d085be44a0126300aa3bb94d0657e532b538303ff217e20aaacbf638393addb6d7705966f1e5334040f150d930b857593e3e365381c0cf6e6ac4a24584c762adc75a27b769333e9a299dc16f4d771661d7aecc44d583bea1ff5f99fe9d08c87e55865610efdde2",     "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423691444842209280/delivery/1202726487847104512_1423691444842209280?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210806%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210806T170426Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=840f364a22c259458b8705f8c96781db09c31a0bd844974f2a88b0a45f3455bc8e2f6ecc6c349abc8311a0040278114af3771ff0de3de6fee4230761573a44244aa5bb2d763829680d3d6bfee2a01538021fbb2f7b9d718e376945aea6355bf861618b968db597027eec317efaf434702d940ba805299ebfdae7af7f028a5ea89e74dd990920e0e879036cc0e2044228195356f0aa63ab89bfef5d6ede2fbf1789c2fe1a3e73dc58236775409e15f49acf72f5f91585a8ad0e5b073e5d6197cf8437aab82358ac9b0df81b5cdb2d6864f8d6e9725587ab92b5dbfc2d3968a5ee796d3940fd1594933f5a9653191dcfbbd63a8ccd02a56c2ef17764000591739d",     "id": "1423691444842209280",     "status": "created",     "upload_expires_at": "2021-08-06T17:19:26.000Z"   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | The unique identifier for this job. |
| `created_at` | date (ISO 8601) | The date and time when the job was created. |
| `type` | enum (`tweets`, `users`) | The type of the job, whether tweets or users. |
| `name` | string | The user defined job name. Only returned if specified when the job was created. |
| `upload_url` | string | A URL representing the location where to upload Tweet IDs consumed by your App. This URL is already signed with an authentication key, so you will not need to pass any additional credentials or headers to authenticate the request. |
| `upload_expires_at` | date (ISO 8601) | The date and time until which the upload URL will be available (usually 15 minutes from the request time). |
| `download_url` | string | The predefined location where to download the results from the compliance job. This URL is already signed with an authentication key, so you will not need to pass any additional credentials or headers to authenticate the request. |
| `download_expires_at` | date (ISO 8601) | The date and time until which the download URL will be available (usually seven days from the request time). |

Introduction

Introduction
------------

Twitter is committed to our community of developers who build with the Twitter API. As part of this commitment, we aim to make our API open and fair to developers, safe for people on Twitter, and beneficial for the Twitter platform as a whole. It is crucial that any developer who stores Twitter content offline, ensures the data reflects user intent and the current state of content on Twitter. For example, when someone on Twitter deletes a Tweet or their account, protects their Tweets, edits a Tweet, or scrubs the geo information from their Tweets, it is critical for both Twitter and our developers to honor that person’s expectations and intent.

Real-time streams of compliance events provide developers the tools to maintain Twitter data in compliance with the [Twitter Developer Agreement and Policy](https://developer.twitter.com/en/developer-terms/policy). 

There are two c_ompliance event_ streams, one for _Tweet compliance_ events, and one for _User compliance_ events. These streams are available with Enterprise access and are designed to help partners that ingest high volumes of data 'listen' for compliance events such as Tweet edit events.

These streams provide the following events: 

**Tweet compliance stream:** 

* delete - indicates that the Tweet was deleted.
    
* tweet\_edit \- indicates a Tweet has been edited and provides the ID of the updated Tweet. 
    
* withheld - indicates that the Tweet has been withheld from one or more countries. 
    
* drop \- indicates that the Tweet should be removed from public view.  
    
* undrop - indicates that the Tweet may be displayed again and treated as public.
    

**User compliance stream:**   

* user\_delete - indicates that the User account was deleted
    
* user\_undelete - indicates that the User account was undeleted
    
* user\_protect - indicates that the User account became private
    
* user\_unprotect - indicates that the User account became public
    
* user\_withheld - indicates that the User account has been withheld from one or more countries. 
    
* user\_suspend - indicates that the User account was suspended
* user\_unsuspend - indicates that the User account was unsuspended
* user\_profile\_modification - indicates that the User profile has been updated. This includes an updated description, name, location, and URL. 

* ****scrub\_geo**** - indicates that the location information associated with the User was removed
    

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance1/quick-start.html)

[Jump to example requests](https://github.com/twitterdev/Twitter-API-v2-sample-code/tree/main/Batch-Compliance)

[Python client](https://github.com/twitterdev/compliant-client)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/compliance/jobs)

Supporting resources
--------------------

[Learn how to use Postman to make requests](https://developer.twitter.com/en/docs/tutorials/postman-getting-started "Learn how to use Postman to make requests")

[Troubleshoot an error](https://developer.twitter.com/en/support/twitter-api "Troubleshoot an error")

[Visit the API reference page for this endpoint](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance1/api-reference "Visit the API reference page for this endpoint")

Quick start

Getting started with the compliance stream endpoints
----------------------------------------------------

This quick start guide will help you make your first request to the compliance stream endpoints using a cURL request. cURL is a command line tool which allows you to make requests with minimal configuration.

If you would like to see sample code in different programming languages, please visit our [Twitter API v2 sample code GitHub repository](https://github.com/twitterdev/Twitter-API-v2-sample-code).  

### Prerequisites

The compliance streams is available with Enterprise access.

To complete this guide, you will need to have a set of [keys and tokens](https://developer.twitter.com/en/docs/authentication) to authenticate your request. You can generate these keys and tokens by following these steps:

* [Sign up for a developer account](https://developer.twitter.com/en/apply-for-access) and receive approval.  
* Create a [Project](https://developer.twitter.com/en/docs/projects) and an associated [developer App](https://developer.twitter.com/en/docs/apps) in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

Steps to build a compliance stream request
------------------------------------------

#### Step one: Start with a cURL command

In this quick start, we are going to use a simple cURL request to connect to a single partition of the Tweet compliance stream. There are 4 partitions in all, so 4 connections must be maintained to receive all events. The Tweet compliance stream endpoint is a very simple one. All you will have to do is replace or add a couple of elements of the below request and submit it to your command line tool.

      `curl -X GET "https://api.twitter.com/2/tweets/compliance/stream?partition=1" \  -H "Authorization: Bearer $APP_ACCESS_TOKEN"`
    

To connect to the User compliance stream, update the request URL to  "https://api.twitter.com/2/users/compliance/stream?partition=1"

#### Step two: Authenticate your request

Since the compliance stream endpoints require [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) authentication, you will need to replace $APP\_ACCESS\_TOKEN with the App Access Token that you generated in the prerequisites. 

#### Step three: Make your request and review your response

Once you have everything set up, you can submit your request to Twitter using the cURL command-line tool. If done successfully, you will receive a live stream of Tweet compliance events with payloads similar to the following:

      `{"data":{"delete":{"tweet":{"id":"1543734217692828673","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.052Z"}}} {"data":{"delete":{"tweet":{"id":"1518339433317514240","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.098Z"}}} {"data":{"delete":{"tweet":{"id":"1543019691868381185","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.156Z"}}} {"data":{"delete":{"tweet":{"id":"1545202024509778944","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.090Z"}}}`
    

If you would like to close your connection, you can press Control-C in your command line tool on either Mac or Windows systems to break the connection, or you can also close the window. 

Your code can parse each JSON line to locate the Tweet (or User ID if using the User compliance stream) and delete the Tweets (or Users) with those IDs from your dataset to stay in compliance. 

Next steps
----------

[Customize your request using the API Reference](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance1/api-reference "Customize your request using the API Reference")

[Reach out to the community for help](https://twittercommunity.com/ "Reach out to the community for help")

Integrating compliance streams

The Tweet and User compliance streams are realtime streaming endpoints that delivers compliance events that occur on the Twitter platform. For an understanding of compliance events and how they are generated on Twitter, please reference our article, [Honoring User Intent on Twitter](https://developer.twitter.com/en/docs/twitter-api/compliance/streams/integrate/honoring-user-intent.html).

It is important to note that Tweet and User events are delivered independently and that each should be processed independently (i.e. a Tweet delete doesn’t imply a User event, and vice versa.) Several User events are not necessarily permanent and can toggle between states infinitely. These include: user\_delete,user\_undelete, user\_protect, user\_unprotect and user\_suspend, user\_unsuspend.

User\_deletes are followed by Tweet deletes 30 days later only if the user has not selected to user\_undelete their account. It is possible that a user\_delete is reversed by the user and deletes for all of their Tweets 30 days later do not occur.

User\_suspend is an action that remains true unless the user is subject to an user\_unsuspend event. These are not subject to any changes on a 30 day time period.

It is never suitable to display compliance events directly to users of your software or to otherwise incorporate them into your products or customer experiences. They are intended solely for maintaining compliance and honoring the actions of Twitter users.

Integrating the compliance streams
----------------------------------

To integrate the compliance streams into your system, you will need to build an integration that can do the following:

1. Establish a streaming connection to each streaming endpoint partition of the compliance streams. The Tweet and User streams are both split into 4 partitions, and a connect must be established for each partition. 
2. Handle high data volumes – de-couple stream ingestion from additional processing using asynchronous processes
3. Reconnect to the stream partitions automatically when disconnected for any reason. After a disconnection, reconnect using the 'backfill\_minutes' request parameter to avoid missing any events. Your system needs to be tolerant of duplicate events. 
4. Process compliance events that are relevant to Tweet and User data you have stored in accordance with the guidance presented above

Honoring user intent on Twitter

We believe that respecting the privacy and intent of Twitter users is critically important to the long term health of one of the largest public, real-time information platforms in the world. Twitter puts privacy controls in the hands of its users, giving individuals the ability to control their own Twitter experience. As business consumers of Twitter data, we have a collective responsibility to honor the privacy and actions of end users in order to maintain this environment of trust and respect.  

There are a variety of things that can happen to Tweets and User accounts that impact how they are displayed on the platform. The actions that affect privacy and intent are defined at both the Tweet and User levels. These actions include:

### User

| Action | Description |
| --- | --- |
| Protect Account | A Twitter user can protect or unprotect their account at any time. Protected accounts require manual user approval of every person who is allowed to view their account's Tweets.   <br>For more information, see [About Public and Protected Tweets](https://support.twitter.com/articles/14016-about-public-and-protected-tweets). |
| Delete Account | A Twitter user can decide to delete their account and all associated Tweets at any time. Twitter retains the account information for 30 days after deletion in case the user decides to undelete and effectively reactivate their account. |
| Scrub Geo | A Twitter user can remove all location data from past Tweets at any time. This known as “scrub geo”. |
| Suspend Account | Twitter retains the right to suspend accounts that are in violation of the Twitter Rules or if an account is suspected to have been hacked or compromised. Account suspensions can only be reversed (unsuspend) by Twitter. |
| Withhold Account | Twitter retains the right to reactively withhold access to certain content in a specific country from time to time. A withheld account can only be made unwithheld by Twitter.   <br>For more information, see [Country Withheld Content](https://support.twitter.com/articles/20169222-country-withheld-content). |

### Tweet

| Action | Description |
| --- | --- |
| Delete Tweet | A Twitter user can delete a Tweet at any point in time. Deleted Tweets cannot be reversed and are permanently deleted. |
| Withhold Tweet | Twitter retains the right to reactively withhold access to certain content in a specific country from time to time. A withheld Tweet can only be made unwithheld by Twitter.   <br>For more information, see [Country Withheld Content](https://support.twitter.com/articles/20169222-country-withheld-content). |

### Keeping Track of User and Tweet Changes

The state of a User or Tweet can change at any time due to one of the actions above, and this impacts how consumers of Twitter data are expected to treat the availability and privacy of all associated content. When these actions happen, a corresponding compliance message is sent that indicates that the state of a Tweet or User has changed.

Compliance Best Practices

Recommendations & Best Practices
--------------------------------

* **Build Data Storage Schemas That Store Numeric Tweet ID and User ID**: User messages require action to be taken on all Tweets from that User. Therefore, since all compliance messages are delivered only by numeric ID, it is important to design storage schemas that maintain the relationship between Tweet and User based on numeric IDs. Data consumers will need to monitor compliance events by both Tweet ID and User ID and be able to update the local data store appropriately.
    
* **Build Schemas That Address All Compliance Statuses**: Depending on how compliance activities will be addressed in various applications, it may be required to add other metadata to the data store. For instance, data consumers may decide to add metadata to an existing database to facilitate restricting the display of content in countries affected by a tweet\_withheld message.
    
* **Handling Retweet Deletes**: Retweets are a special kind of Tweet where the original message is nested in an object within the Retweet. In this case, there are two Tweet IDs referenced in a Retweet – the ID for the Retweet, and the ID for the original message (included in the nested object). When an original message is deleted, a Tweet delete message is issued for the original ID. Tweet deletion events typically trigger delete events for all Retweets. It is a best practice to reference the original Tweet ID when storing Retweets, and deleting all referenced Retweets when receiving Tweet delete events.

Compliance Data Objects

Possible types of compliance events will include Tweet events and User events, for which there are multiple types described below.    

Please note:

* Read more about Tweet visibility [here](https://support.twitter.com/articles/14016) and our developer policy around deleted Tweets [here](https://dev.twitter.com/overview/terms/policy#3.Update_Respect_Users_Control_and_Privacy).
* The Tweet Compliance stream includes events triggered by Tweets getting edited. See the 'tweet\_edit' example event below.  
* Several User delete, protect and suspend events are not necessarily permanent and can toggle between states infinitely. These include: user\_delete, user\_undelete, user\_protect, user\_unprotect and user\_suspend, user\_unsuspend.
* User\_deletes are followed by Tweet deletes 30 days later only if the user has not selected to user\_undelete their account. It is possible that a user\_delete is reversed by the user and deletes for all of their Tweets 30 days later do not occur.
* User\_suspend is an action that remains true unless the user is subject to an user\_unsuspend event. These are not subject to any changes on a 30 day time period.

Refer to the ‘Recommended Action’ column to understand how to process each type of event in order to respect the privacy and intent of the end user.  
  

Payload examples
----------------

See the payload examples below for each compliance event described in the table above.

#### Tweet delete

      `{ 	"data": { 		"delete": { 			"tweet": { 				"id": "601430178305220608", 				"author_id": "3198576760" 			}, 			"event_at": "2022-12-23T12:34:56.789Z" 		} 	}  }`
    

When a deleted Tweet has been Quote Tweeted, there will be an additional Tweet 'delete' event with a "quote\_tweet\_id" attribute for each Quote Tweet. 

#### Tweet edit

      `{ 	"data": { 		"tweet_edit": { 			"tweet": { 				"id": "1567233994734948354" 			}, 			"initial_tweet_id": "1567233844205453313", 			"edit_tweet_ids": [ 				"1567233844205453313", 				"1567233994734948354" 			], 			"event_at": "2022-09-06T19:31:16.801Z" 		} 	} }`
    

#### Tweet withheld  

      `{ 	"data": { 		"withheld": { 			"tweet": { 				"id": "601430178305220608", 				"author_id": "3198576760" 			}, 			"withheld_in_countries": [ 				"XY" 			], 			"event_at": "2022-12-23T12:34:56.789Z" 		} 	} }`
    

When a withheld Tweet has been Quote Tweeted, there will be an additional Tweet 'withheld' event with a "quote\_tweet\_id" attribute for each Quote Tweet. 

#### Tweet Drop

      `{ 	"data": { 		"drop": { 			"tweet": { 				"id": "601430178305220600", 				"author_id": "3198576760" 			}, 			"event_at": "2022-12-23T12:34:56.789Z" 		} 	} }`
    

#### Tweet Undrop

      `{   "data":       {        "undrop": {           "tweet": {              "id": "601430178305220600",              "author_id": "3198576760"            },          "event_at": "2022-12-23T12:34:56.789Z"         }      } }`
    

#### User scrub geo

      `{    "data":      {       "scrub_geo": {         "user": {           "id": "1375036644"         },       "up_to_tweet_id": "411552403083628544",       "event_at": "2022-06-27T23:49:41.839+00:00"       }     } }`
    

#### User delete

      `{ 	"data": { 		"user_delete": { 			"user": { 				"id": "1375036644" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User undelete

      `{ 	"data": { 		"user_undelete": { 			"user": { 				"id": "1375036644" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User withheld

      `{ 	"data": { 		"user_withheld": { 			"user": { 				"id": "1375036644" 			}, 			"withheld_in_countries": [ 				"XY" 			], 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User protect

      `{ 	"data": { 		"user_protect": { 			"user": { 				"id": "3182003550" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User unprotect

      `{ 	"data": { 		"user_unprotect": { 			"user": { 				"id": "3182003550" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User suspend

      `{ 	"data": { 		"user_suspend": { 			"user": { 				"id": "1375036644" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User unsuspend

      `{ 	"data": { 		"user_unsuspend": { 			"user": { 				"id": "1375036644" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

**User profile modification**

      `{   "data": {     "user_profile_modification": {       "user": {         "id": "906948460078698496"       },       "event_at": "2022-07-12T19:47:59.442Z",       "profile_field": "profile.description",       "new_value": "Home of the @SnowbotDev chatbot."     }   } }`
    

The "profile\_field" attribute indicates what in the User profile changed, and can contain the following values: 

* "profile.name"  
    
* "profile.location"
* "profile.description"
* "profile.url"
* "profile.profileBanner"
* "profile.profileBanner.url"
* "profile.profileImage"
* "profile.profileImage.url"

API reference

API reference index
-------------------

For the complete API reference, select an endpoint from the list:

|     |     |
| --- | --- |
| **Connect to Tweet Compliance event stream** | `[GET /2/tweets/compliance/stream](https://developer.twitter.com/en/docs/twitter-api/compliance/streams/api-reference/get-users-compliance-stream)` |
| **Connect to User Compliance event stream** | `[GET /2/users/compliance/stream](https://developer.twitter.com/en/docs/twitter-api/compliance/streams/api-reference/get-tweets-compliance-stream)` |

GET /2/users/compliance/stream

GET /2/users/compliance/stream
==============================

Connect to one of four partitions of the User compliance stream.

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2User%2Fcompliance%2Fstream%2F%7Bid%7D&method=get) 

### Endpoint URL

`https://api.twitter.com/2/users/compliance/stream`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 100 requests per 15-minute window shared among all users of your app |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `partition`  <br> Required | number | Must be set to 1, 2, 3 or 4. User compliance events are split across 4 partitions, so 4 separate streams are needed to receive all events. |
| `backfill_minutes`  <br> Optional | number | By passing this parameter, you can recover up to five minutes worth of data that you might have missed during a disconnection. The backfilled events will automatically flow through a reconnected stream, with older events generally being delivered before any newer events. You must include a whole number between 1 and 5 as the value to this parameter. nThis feature will deliver all events that published during the timeframe selected, meaning that if you were disconnected for 90 seconds, and you requested two minutes of backfill, you will receive 30 seconds worth of duplicate events. Due to this, you should make sure your system is tolerant of duplicate data. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const userComplianceStream = await twitterClient.users.complianceStream();     console.dir(userComplianceStream, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `try {     InputStream result = apiInstance.users().complianceStream(null, null, null, null, null, null, null);     try{         JSON json = new JSON();         Type localVarReturnType = new TypeToken<StreamingUserCompliance>(){}.getType();         BufferedReader reader = new BufferedReader(new InputStreamReader(result));         String line = reader.readLine();         while (line != null) {           System.out.println(json.getGson().fromJson(line, localVarReturnType).toString());           line = reader.readLine();         }     } catch (Exception e) {       e.printStackTrace();       System.out.println(e);     } } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#usersComplianceStream");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "user_protect": {       "user": {         "id": "906948460078698496"       },       "event_at": "2022-07-01T21:44:57.895Z"     }   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `user_delete` | string | A delete user event. |
| `user_undelete` | string | A undelete user event. |
| `user_withheld` | string | A withheld user event. |
| `user_protect` | string | A protect user event. |
| `user_unprotect` | string | A unprotect user event. |
| `user_suspend` | string | A suspend user event. |
| `user_unsuspend` | string | A unsuspend user event. |
| `scrub_geo` | string | A geo scrub user event. |
| `user_profile_modification` | string | A modified user profile event. |
| `id` | string | The ID of the user triggering a compliance event. |
| `event_at` | date (ISO 8601) | Time of when event happended. |
| `withheld_in_countries` | string | Country where user is withheld. |
| `up_to_tweet_id` | string | Provided when a user removes their geo metadata. |
| `profile_field` | string | Indicates what Profile attribute was updated. |

GET /2/tweets/compliance/stream

GET /2/tweets/compliance/stream
===============================

Connect to one of four partitiona of the Tweet compliance stream.

[Build request with API Explorer ❯](https://developer.twitter.com/apitools/api?endpoint=%2F2Tweet%2Fcompliance%2Fstream%2F%7Bid%7D&method=get) 

### Endpoint URL

`https://api.twitter.com/2/tweets/compliance/stream`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 100 requests per 15-minute window shared among all users of your app |

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `partition`  <br> Required | number | Must be set to 1, 2, 3 or 4. Tweet compliance events are split across 4 partitions, so 4 separate streams are needed to receive all events. |
| `backfill_minutes`  <br> Optional | number | By passing this parameter, you can recover up to five minutes worth of data that you might have missed during a disconnection. The backfilled events will automatically flow through a reconnected stream, with older events generally being delivered before any newer events. You must include a whole number between 1 and 5 as the value to this parameter. nThis feature will deliver all events that published during the timeframe selected, meaning that if you were disconnected for 90 seconds, and you requested two minutes of backfill, you will receive 30 seconds worth of duplicate events. Due to this, you should make sure your system is tolerant of duplicate data. |

  
  

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const tweetComplianceStream = await twitterClient.tweets.complianceStream();     console.dir(tweetComplianceStream, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `try {     InputStream result = apiInstance.tweets().complianceStream(null, null, null, null, null, null, null);     try{         JSON json = new JSON();         Type localVarReturnType = new TypeToken<StreamingTweetCompliance>(){}.getType();         BufferedReader reader = new BufferedReader(new InputStreamReader(result));         String line = reader.readLine();         while (line != null) {           System.out.println(json.getGson().fromJson(line, localVarReturnType).toString());           line = reader.readLine();         }     } catch (Exception e) {       e.printStackTrace();       System.out.println(e);     } } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#tweetsComplianceStream");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`    
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "delete": {       "tweet": {         "id": "1542870758724145153",         "author_id": "906948460078698496"       },       "event_at": "2022-07-01T21:48:43.030Z"     }   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `delete` | string | A delete Tweet event. |
| `withheld` | string | A withheld Tweet event. |
| `drop` | string | A drop Tweet event. |
| `undrop` | string | A undrop Tweet event. |
| `id` | string | The ID of the Tweet triggering a compliance event. |
| `author_id` | string | The ID of the author of a Tweet triggering a compliance event. |
| `event_at` | date (ISO 8601) | Time of when event happended. |