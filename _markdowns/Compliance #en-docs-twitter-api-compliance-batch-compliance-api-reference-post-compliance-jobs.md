



POST /2/compliance/jobs | Docs | Twitter Developer Platform 





































































































POST /2/compliance/jobs



 POST /2/compliance/jobs
=======================

"Creates a new compliance job for Tweet IDs or user IDs.  
  
A compliance job will contain an ID and a destination URL. The destination URL represents the location that contains the list of IDs consumed by your App.  
  
You can run one batch job at a time."


Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/compliance/jobs`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 App-only |
| Rate limit | App rate limit (Application-only): 150 requests per 15-minute window shared among all users of your app |

### JSON body parameters



| Name | Type | Description |
| --- | --- | --- |
| `type` Required  | enum (`tweets`, `users`) | Specify whether you will be uploading tweet or user IDs. You can either specify tweets or users. |
| `name` Optional  | string | A name for this job, useful to identify multiple jobs using a label you define. |
| `resumable` Optional  | boolean | Specifies whether to enable the upload URL with support for resumable uploads. If true, this endpoint will return a pre-signed URL with resumable uploads enabled. |

  
  
### Example code with offical SDKs








* TypeScript
* Java


















 TypeScript
 

 Java
 
















```

      (async () => {
  try {
    const createComplianceJob =
      await twitterClient.compliance.createBatchComplianceJob({
        type: "tweets", // Type of compliance job to create - value can be "tweets" or "users"
        resumable: true, //Optional - Specifies whether to enable the upload URL with support for resumable uploads. If true, this endpoint will return a pre-signed URL with resumable uploads enabled.
        name: "Job name", //Optional - A name for this job, useful to identify multiple jobs using a label you define.
      });
    console.dir(createComplianceJob, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // Set the params values

CreateBatchComplianceJobRequest createBatchComplianceJobRequest = new CreateBatchComplianceJobRequest();

//ComplianceJobType | Type of compliance job to create
ComplianceJobType jobType = ComplianceJobType.fromValue("tweets");

createBatchComplianceJobRequest.type(jobType);

//Optional - A name for this job, useful to identify multiple jobs using a label you define.
createBatchComplianceJobRequest.name("job name");

//Optional - Specifies whether to enable the upload URL with support for resumable uploads. If true, this endpoint will return a pre-signed URL with resumable uploads enabled.
createBatchComplianceJobRequest.resumable(true);

try {
    SingleComplianceJobResponse result = apiInstance.compliance().createBatchComplianceJob(createBatchComplianceJobRequest);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ComplianceApi#createBatchComplianceJob");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

    
```












### Example responses








* Successful response


















 Successful response
 
















```

      {
  "data": {
    "resumable": false,
    "type": "tweets",
    "download_expires_at": "2021-08-13T17:04:26.000Z",
    "created_at": "2021-08-06T17:04:26.000Z",
    "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423691444842209280/submission/1202726487847104512_1423691444842209280?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210806%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210806T170426Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=b057f9d07f80c7d4d73dc1184e2801e495054f61ff48ee1f6a74b7125bb62b02f3afa66a445e57634a0e78a546308632d845e28e092c10ae90cadb8655b0daafcee9ec8c7d95d2099437117db61d6789c8334e55ce5ee7b76c0d7dd383bd270d0c5a266ebbe0aa51365b332fe2c04942937526102871faa72e9255d2a8683d2dadcbd5ece0de18144a6dc74a6a53cdd4e5bb98261032047bf7d085be44a0126300aa3bb94d0657e532b538303ff217e20aaacbf638393addb6d7705966f1e5334040f150d930b857593e3e365381c0cf6e6ac4a24584c762adc75a27b769333e9a299dc16f4d771661d7aecc44d583bea1ff5f99fe9d08c87e55865610efdde2",
    "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423691444842209280/delivery/1202726487847104512_1423691444842209280?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210806%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210806T170426Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=840f364a22c259458b8705f8c96781db09c31a0bd844974f2a88b0a45f3455bc8e2f6ecc6c349abc8311a0040278114af3771ff0de3de6fee4230761573a44244aa5bb2d763829680d3d6bfee2a01538021fbb2f7b9d718e376945aea6355bf861618b968db597027eec317efaf434702d940ba805299ebfdae7af7f028a5ea89e74dd990920e0e879036cc0e2044228195356f0aa63ab89bfef5d6ede2fbf1789c2fe1a3e73dc58236775409e15f49acf72f5f91585a8ad0e5b073e5d6197cf8437aab82358ac9b0df81b5cdb2d6864f8d6e9725587ab92b5dbfc2d3968a5ee796d3940fd1594933f5a9653191dcfbbd63a8ccd02a56c2ef17764000591739d",
    "id": "1423691444842209280",
    "status": "created",
    "upload_expires_at": "2021-08-06T17:19:26.000Z"
  }
}
    
```












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



















Developer policy and terms


Follow @XDevelopers


Subscribe to developer news












#### 
 X platform


* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app




#### 
 X Corp.


* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors




#### 
 Help


* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us




#### 
 Developer resources


* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms




#### 
 Business resources


* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy









 © 2024 X Corp.
 


Cookies


Privacy


Terms and conditions






















**Did someone say … cookies?**  
  


 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.


 




* Accept all cookies
* Refuse non-essential cookies















