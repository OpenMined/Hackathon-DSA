



GET /2/compliance/jobs | Docs | Twitter Developer Platform 





































































































GET /2/compliance/jobs



 GET /2/compliance/jobs
======================

Returns a list of recent compliance jobs.

Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/compliance/jobs`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 App-only |
| Rate limit | App rate limit (Application-only): 150 requests per 15-minute window shared among all users of your app |

### Query parameters



| Name | Type | Description |
| --- | --- | --- |
| `type` Required  | enum (`tweets`, `users`) | Allows to filter by job type - either by tweets or user ID. Only one filter (tweets or users) can be specified per request. |
| `status` Optional  | enum (`created`, `in_progress`, `failed`, `complete`) | Allows to filter by job status. Only one filter can be specified per request.Default: `all` |

  
  
### Example code with offical SDKs








* TypeScript
* Java


















 TypeScript
 

 Java
 
















```

      (async () => {
  try {
    const getListComplianceJobs =
      await twitterClient.compliance.listBatchComplianceJobs({
        type: "tweets", // type value can be "tweets" or "users"
        status: "created", // status values can be "created", "in_progress", "completed" or "failed"
      });
    console.dir(getListComplianceJobs, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // Set the params values

// ComplianceJobType | Type of compliance job to list
ComplianceJobType type = ComplianceJobType.fromValue("tweets");

// ComplianceJobStatus | Status of compliance job to list
ComplianceJobStatus status = ComplianceJobStatus.fromValue("created");
try {
    MultiComplianceJobResponse result = apiInstance.compliance().listBatchComplianceJobs(type, status);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ComplianceApi#listBatchComplianceJobs");
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
  "data": [
    {
      "type": "tweets",
      "id": "1421185651106480129",
      "resumable": false,
      "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1421185651106480129/submission/1202726487847104512_1421185651106480129?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210730%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210730T190718Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=5c197d6e2b54cd941006904d7f96a3ac4985f19b5b770c4b334d4defe495ccebda71650d8636fcfc7266b8e609c0de29255b6b46bf1ad883522fac78010a2936fdd46dd3afa1925a674311b51e1d6d19ab249aa51cc6d1afb65203847a1f998be41aff209d465d74d20b4b26898951035808afd5bd022445d0aeb7ffd8aa20486ee1b3e2ea3b6f9709dfd849fbdfacfb1542dca965d8473e6bfc9596df85fd1be716dd7ebbb4c6b995a0775472145bd778ec4175f2934f2823b21bba6604696301168e55d614098512ffee2bd1b0e363106fc6197e15d833c41bf83598dc4ce7e7f7e2edea0c07e3a55f815e1e28abeb5a24a3e5768fbaa70cf19e85c269d530",
      "upload_expires_at": "2021-07-30T19:22:18.000Z",
      "download_expires_at": "2021-08-06T19:07:18.000Z",
      "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1421185651106480129/delivery/1202726487847104512_1421185651106480129?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=09de4feae68a6d4449eb7ce1f8f3551996552e7fba103005b3bd50ab318bb5215e4f5396ef29d17755deb6bf172b9d1dab61a04b249d39e87f6e2dbb31632b7e5f2d35f4f534e1f1522c9d7958b8745dd62471deb8d6992c80fd418628404f5f14eda3f557adf709403058910ea009e0c88ce81458ec9b915016a5c5901e2365b130db00b18fcb7da1b082e1a5c75f7bf7eeab8783675d1b6a56441ac6e9ffc972b1278a5853d2b94dda55e1a6e2068bc0ddd3cddc9213ec9cebb7cb5be931977bb28dda12c7c5e69d1f876b243f0f224076bf1b81149603319a2fc9cb82337bdbe05e7bbf184bcbdc17d43b3f5efbae72ea386d955ca10e702e00df31aabf32",
      "created_at": "2021-07-30T19:07:18.000Z",
      "status": "complete"
    },
    {
      "type": "tweets",
      "id": "1423095206576984067",
      "resumable": false,
      "upload_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423095206576984067/submission/1202726487847104512_1423095206576984067?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=ba08f588bea3873aa0465cf22015e583c2851a5ff14891d22430b1127288728f1aa303673e6895694e7017739871ff5ae59bbcde7d4ac7a14aaaafba98ad22ca818e99fb3ec7eaaf74b3ecfecbfb33711869b2e85d7666609276666ef4a8b396ae9616743a0cbd773962e5850f2942cd76be7373d608a140e041ca8492017d43fac9220fa145d0b2ecaf9f752d71fc8c4b81b67c5c22aa59ac87666f7d83714fdace72894d2911a3e36dd42028d0222e71054d6b28c8ef63d0f0000f228c8680bab9c8011b87d1a6c9a60e8cc9e8b6a83abf7c47a57772746c83b19849f5b4c938ccd0922990da5f2a81ff806edcb4667bb402fb1f1f6f5162768e0661648b21",
      "upload_expires_at": "2021-08-05T01:50:11.000Z",
      "download_expires_at": "2021-08-12T01:35:11.000Z",
      "download_url": "https://storage.googleapis.com/twttr-tweet-compliance/1423095206576984067/delivery/1202726487847104512_1423095206576984067?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=complianceapi-public-svc-acct%40twttr-compliance-public-prod.iam.gserviceaccount.com%2F20210805%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210805T013511Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=09de4feae68a6d4449eb7ce1f8f3551996552e7fba103005b3bd50ab318bb5215e4f5396ef29d17755deb6bf172b9d1dab61a04b249d39e87f6e2dbb31632b7e5f2d35f4f534e1f1522c9d7958b8745dd62471deb8d6992c80fd418628404f5f14eda3f557adf709403058910ea009e0c88ce81458ec9b915016a5c5901e2365b130db00b18fcb7da1b082e1a5c75f7bf7eeab8783675d1b6a56441ac6e9ffc972b1278a5853d2b94dda55e1a6e2068bc0ddd3cddc9213ec9cebb7cb5be931977bb28dda12c7c5e69d1f876b243f0f224076bf1b81149603319a2fc9cb82337bdbe05e7bbf184bcbdc17d43b3f5efbae72ea386d955ca10e702e00df31aabf32",
      "created_at": "2021-08-05T01:35:11.000Z",
      "status": "expired"
    }
  ]
}
    
```












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















