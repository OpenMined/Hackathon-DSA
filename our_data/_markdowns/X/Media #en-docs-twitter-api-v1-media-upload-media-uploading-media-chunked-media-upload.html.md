
Chunked media upload | Docs | Twitter Developer Platform 

Chunked media upload

Example of chunked video media/upload
-------------------------------------

Using the chunked POST media/upload endpoints requires an adjusted workflow from single image uploads. For video or chunked uploads, you must:

* Initialize the upload using the INIT command
* Upload each chunk of bytes using the APPEND command
* Complete the upload using the FINALIZE command

See the large video upload sample for an example written in Python.

Below is a working example using the command-line twurl utility. To see full headers of the requests and responses when using twurl, use the -t option to enable trace mode.

**INIT**

```
      twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=INIT&media_type=video/mp4&total_bytes=4430752"
```

Code copied to clipboard

```
      {
  "media_id": 601413451156586496,
  "media_id_string": "601413451156586496",
  "expires_after_secs": 3599
}
```

**APPEND**  

```
      twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=APPEND&media_id=601413451156586496&segment_index=0" --file /path/to/video.mp4 --file-field "media"
```

Code copied to clipboard

HTTP 2XX will be returned with an empty response body on successful upload.  

**FINALIZE**

```
      twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=FINALIZE&media_id=601413451156586496"
```

Code copied to clipboard

```
      {
  "media_id": 601413451156586496,
  "media_id_string": "601413451156586496",
  "size": 4430752,
  "expires_after_secs": 3600,
  "video": {
    "video_type": "video/mp4"
  }
}
```

Troubleshooting
---------------

For issues with the Media APIs:

* Browse the Media API category in the developer forums.

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