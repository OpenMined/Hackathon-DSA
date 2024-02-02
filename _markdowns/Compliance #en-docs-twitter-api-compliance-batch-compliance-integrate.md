::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
When using the Batch compliance endpoints, developers can batch upload
large amounts of Twitter data and understand what action is needed to
ensure that their datasets reflect user intent and the current state of
the content on Twitter. Uploading large amounts of data to a remote
server is a relatively straightforward operation when systems and
connectivity are stable and reliable. However, this may not always be
the case. Some environments may impose a connection timeout, effectively
cutting the connection between your app and the upload server after a
set amount of time; you may also encounter connection issues, for
example when trying to upload a large file from your laptop over a wi-fi
connection. In these circumstances, it's desirable to upload smaller
portions of that file at a time, rather than having one single
continuous connection.

Twitter's batch compliance endpoints rely on Google Cloud Storage to
process large files. This type of storage is optimized for various
applications; Cloud Storage supports a technique to manage large files
called resumable uploads.

If the upload goes wrong at any point, Google Cloud Storage is able to
resume the operation from where it was left off.

### Creating a resumable job

#### Step one:

First, you will have to create a compliance job and specify whether you
will be uploading Tweet IDs or user IDs (using the [ type
]{.code-inline} parameter). Additionally, add [ resumable
]{.code-inline} to the body and set it to [ true ]{.code-inline} . Make
sure to replace the [ \$BEARER_TOKEN ]{.code-inline} below with your
bearer token below.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl --request POST \
 'https://api.twitter.com/2/compliance/jobs' --header 'Authorization: Bearer $BEARER_TOKEN --header 'Content-Type: application/json' --data-raw '{
   "type": "tweets",
   "resumable": true
}'
    
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
``` {.line-numbers .t05__pre--with-button}
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
Take note of the value from the [ upload_url ]{.code-inline} , you will
need it in the following steps.

#### Step two:

Next, you will need to initiate the resumable upload. In order to do so,
make a **POST** call to the [ upload_url ]{.code-inline} from the
previous step and make sure to include the following headers:

[ Content-Type: text/plain ]{.code-inline}

[ Content-Length: 0 ]{.code-inline}

[ x-goog-resumable: start ]{.code-inline}
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl --request POST \
'https://storage.googleapis.com/twttr-tweet-compliance/1430227686685757442/submission/1202726487847104512_1430227686685757442?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210824%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210824T175707Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-length%3Bcontent-type%3Bhost%3Bx-goog-resumable&X-Goog-Signature=890d958f9c7dcb7f238e4971b59da5afc5b8329fb197c67b5930fe0f9dfe180afe2d4bec341111809b88ccfab46ab1f81f4242abc1af7b67c6e8977c52e6d486f5f43ce6a37a7a6530d25f15e2bcd9bb54655fe4ee22b26f8886ba71b67b7b11afd1198d658d1b6f0c41260f55260a260e1be0239977feba43dce40bc0e8e6293a4a3a3f7ee0afc74d3d2f7f2d3d514f108d5887a52ac85760385e5b9bb67cd26bfcf6b1c19151ea8111e217a29407722dc0dc9ab373334e88c18159546237ec9334f9a1e33717dc82800c6a45bba82706d5aece84ecdf3fcac52b21c8a3085a639047cf2707a8b9e4c296fc7cf05edbb110f07b89e38f0f5ea77e8b313cade7' \
--header 'Content-Type: text/plain' --header \
 'Content-Length: 0' --header \
 'x-goog-resumable: start
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If this call is successful, you will get a [ 201 ]{.code-inline}
response code. Then, in the response header, copy the value for the
location header which will look something like this:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 https://storage.googleapis.com/twttr-tweet-compliance/1430227686685757442/submission/1202726487847104512_1430227686685757442?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210824%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210824T175707Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-length%3Bcontent-type%3Bhost%3Bx-goog-resumable&X-Goog-Signature=890d958f9c7dcb7f238e4971b59da5afc5b8329fb197c67b5930fe0f9dfe180afe2d4bec341111809b88ccfab46ab1f81f4242abc1af7b67c6e8977c52e6d486f5f43ce6a37a7a6530d25f15e2bcd9bb54655fe4ee22b26f8886ba71b67b7b11afd1198d658d1b6f0c41260f55260a260e1be0239977feba43dce40bc0e8e6293a4a3a3f7ee0afc74d3d2f7f2d3d514f108d5887a52ac85760385e5b9bb67cd26bfcf6b1c19151ea8111e217a29407722dc0dc9ab373334e88c18159546237ec9334f9a1e33717dc82800c6a45bba82706d5aece84ecdf3fcac52b21c8a3085a639047cf2707a8b9e4c296fc7cf05edbb110f07b89e38f0f5ea77e8b313cade7&upload_id=ADPycds-_Ow7aqcpbG4XguXSVAgd_2fy-XiDA2qm-It9PCwBlZhF4e2bfOAQzEmRJ4T_l6jU6LfYdfrKa_KlFFBOyx3PjYzrxQ
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
You can then upload your Tweet or User IDs to this location by following
step two onwards, [from the quick start
guide](/content/developer-twitter/en/docs/twitter-api/compliance/batch-compliance/quick-start)
.

\
Because of their technical complexity, resumable uploads are best used
in conjunction with code. This guide will use Node.js with the [needle
request library](https://www.npmjs.com/package/needle) .

### Install the dependencies

Before proceeding, you should have a Node.js environment installed; you
can obtain Node.js from its website. Once installed, Node.js will
contain a utility called [ npm ]{.code-inline} ; make sure both [ Node
]{.code-inline} and [ npm ]{.code-inline} are installed by calling the
following command, and ensure it doesn't result in an error.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 $ npm -v
6.4.1
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
A version number similar to this signifies your environment is ready
(note that your version number may differ). We will use [ npm
]{.code-inline} to install the upload library. Run this command:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 $ npm install -g needle
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
You're all set; there is no additional configuration required.

#### Request a resumable destination

When creating a new job, set the [ resumable ]{.code-inline} parameter
to [ true ]{.code-inline} so you can get a destination that supports a
resumable upload. In the response payload, you will receive an [
upload_url ]{.code-inline} value.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 "upload_url":\
"https://storage.googleapis.com/compliance_tweet_ids/customer_test_object_12950882_GlYjiE?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=193969463581-compute%40developer.gserviceaccount.com%2F20200618%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20200618T184154Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=b7bdcf32479b08715be91ed47b06471b8acdcdb319f8e4f423bf3a3056dfa03ed83e47446f33338e292967a15c08fa5ba34395edaf057a2ac975b88e710ca994adb023a9e1673a7c58ce2fa0d73537f72812af78e92b708dfe6b907a7d75bd0f6cfa61fec867e80ac83ced0725d1ee59787c9dbca50d41f7b0f513dad63a7564136b1a70042a2ec6ba6b697cbe480a4405362f7a08255a5e8205aa7baa562f99e6a092f0420f33d67ffaeb132f877fbaf16c969630b5f173e8a3f31c473707241fa4e28f4bed13fb2ea01d3af1c449321a2e6ee9ec1e331b447cabcfc6f9d1f99f564d180f0cc1d28ea54972c996102c67c6501c6c16a00c13d17756f960e0e1"
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
By default, the library will create a new upload destination by
accepting an upload location (called bucket) and the name of the file
you wish to upload. Because the batch compliance endpoints create their
own destination, we will need to tell the library we already have a
location ready to accept our upload.

\
We will need to pass this value to the upload library, along with the
name of the file containing the data to upload. Create a file, and name
it ***twitter-upload.js*** . Add the following code:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 const needle = require('needle');
const fs = require('fs');
const path = require('path');

const [, scriptName, filename, uploadURL] = process.argv;
if (!filename || !uploadURL) {
  console.error(`Usage: node ${path.basename(scriptName)} filename upload_url`);
  process.exit(-1);
}

async function uploadFile(file, url) {
  // rangeEnd is the index of the last byte in the file, i.e. number of bytes in file
  const rangeEnd = (await fs.promises.stat(file)).size;
  
  let options = {
    headers: {
      'Content-Range': `bytes */${rangeEnd}`,
    },
  };
  
  const response = await needle('put', url, null, options);

  switch (response.statusCode) {
    case 200:
    case 201:
      console.log('Upload complete');
      return;
    case 308:
      return resumeUpload(response, file, url);
    default: 
      console.log('Got unexpected response code: ', response.statusCode);
      return;
  }
}

async function resumeUpload(response, file, url) {
  console.log('Upload not completed, resuming');
  if (response.headers.range) {      
    let resumeOffset = Number(response.headers.range.split('-')[1]) + 1;
    
    let options = {
      headers: {
        'Content-Range': `bytes ${resumeOffset}-${rangeEnd-1}/${rangeEnd}`,
        'Content-Length': `${rangeEnd-resumeOffset}`,
      },
    };
    
    let readStream = fs.createReadStream(file, {start: resumeOffset});
    return needle('put', url, readStream, options);
  } else {
    console.log('Initiating upload');
    let options = {
      headers: {
        'Content-Type': 'text/plain'
      }
    };
    
    let readStream = fs.createReadStream(file);
    return needle('put', url, readStream, options);
  }
}

// Request resumable session URL
async function requestResumableSession(url) {
  const options = {
    headers: {
      'Content-Type': 'text/plain',
      'Content-Length': '0',
      'x-goog-resumable': 'start',
    },
  };

  const res = await needle('post', url, null, options);
  if (res.statusCode === 201) {
    const resumableSessionURL = res.headers['location'];
    console.log('Starting upload to: ', resumableSessionURL);
    
    await uploadFile(filename, resumableSessionURL);
  } else {
    console.log('Failed to create resumable session URI');
  }
  
}

requestResumableSession(uploadURL).then(result => console.log('Upload complete'));
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Save the file wherever it makes the most sense. Next, in your command
line, invoke the script and pass two parameters:

1.  The first will be the location of the file (with the Tweet or User
    IDs) that you wish to upload.
2.  The second will be the upload URL we received from the compliance
    endpoint response.

Ensure the URL is surrounded in double-quotes, and do the same for your
file name if it contains spaces or other characters: \
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 node twitter-upload.js compliance_upload.txt\
"https://storage.googleapis.com/compliance_tweet_ids/customer_test_object_12950882_GlYjiE?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=193969463581-compute%40developer.gserviceaccount.com%2F20200618%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20200618T184154Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=b7bdcf32479b08715be91ed47b06471b8acdcdb319f8e4f423bf3a3056dfa03ed83e47446f33338e292967a15c08fa5ba34395edaf057a2ac975b88e710ca994adb023a9e1673a7c58ce2fa0d73537f72812af78e92b708dfe6b907a7d75bd0f6cfa61fec867e80ac83ced0725d1ee59787c9dbca50d41f7b0f513dad63a7564136b1a70042a2ec6ba6b697cbe480a4405362f7a08255a5e8205aa7baa562f99e6a092f0420f33d67ffaeb132f877fbaf16c969630b5f173e8a3f31c473707241fa4e28f4bed13fb2ea01d3af1c449321a2e6ee9ec1e331b447cabcfc6f9d1f99f564d180f0cc1d28ea54972c996102c67c6501c6c16a00c13d17756f960e0e1"
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
You will see output similar to this:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 Starting upload to:  https://storage.googleapis.com/twttr-tweet-compliance/<redacted>
Upload not completed, resuming
Initiating upload

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
You can pause the upload at any time by pressing Ctrl + C or closing
your command line. You will be able to resume the upload from where you
left off when you invoke the same command at a later stage. Once the
file has been completely uploaded, you will see the following message:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 Upload complete
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
At this point, you will be able to use the [compliance status
endpoint](https://developer-staging.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs-id)
to check on the status of your compliance job, and you will be able to
download the compliance result when complete.
:::
:::
:::
