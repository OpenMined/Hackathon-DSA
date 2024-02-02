
Connecting to a streaming endpoint | Docs | Twitter Developer Platform 

Connecting to a streaming endpoint

Connecting to a streaming endpoint
==================================

Establishing a connection to the streaming APIs means making a very long lived HTTP request, and parsing the response incrementally. Conceptually, you can think of it as downloading an infinitely long file over HTTP.

Authentication
--------------

The following authentication methods are supported by the Streaming APIs:

|  |  |  |
| --- | --- | --- |
| Auth Type | Supported APIs | Description |
| OAuth | * Track API Stream
 | Requests must be authorized according to the OAuth specification . |
| Basic auth | * PowerTrack API
* Decahose stream
 | Requests must use of HTTP Basic Authentication, constructed from a valid email address and password combination. |

Connecting
----------

To connect to the Streaming API, form a HTTP request and consume the resulting stream for as long as is practical. Our servers will hold the connection open indefinitely, barring server-side error, excessive client-side lag, network hiccups, routine server maintenance or duplicate logins.

The method to form an HTTP request and parse the response will be different for every language or framework, so consult the documentation for the HTTP library you are using.

Some HTTP client libraries only return the response body after the connection has been closed by the server. These clients will not work for accessing the Streaming API. You must use an HTTP client that will return response data incrementally. Most robust HTTP client libraries will provide this functionality. The Apache HttpClient will handle this use case, for example.

Disconnections
--------------

Twitter will close a streaming connection for the following reasons:

* A client establishes too many connections with the same credentials. When this occurs, the oldest connection will be terminated. This means you have to be careful not to run two reconnecting clients in parallel with the same credentials, or else they will take turns disconnecting each other.
* A client stops reading data suddenly. If the rate of Tweets being read off of the stream drops suddenly, the connection will be closed.
* A client reads data too slowly. Every streaming connection is backed by a queue of messages to be sent to the client. If this queue grows too large over time, the connection will be closed.
* A streaming server is restarted. This is usually related to a code deploy and is not very frequent.
* Twitter’s network configuration changes. These events are rare, and would represent load balancer restarts or network reconfigurations, for example.

Stalls
------

Set a timer, either a 90 second TCP level socket timeout, or a 90 second application level timer on the receipt of new data. If 90 seconds pass with no data received, including newlines, disconnect and reconnect immediately according to the backoff strategies in the next section. The Streaming API will send a keep-alive newline every 30 seconds to prevent your application from timing out the connection. You should wait at least 3 cycles to prevent spurious reconnects in the event of network congestion, local CPU starvation, local GC pauses, etc.

Reconnecting
------------

Once an **established** connection drops, attempt to reconnect immediately. If the reconnect fails, slow down your reconnect attempts according to the type of error experienced:

* Back off linearly for **TCP/IP level network errors**. These problems are generally temporary and tend to clear quickly. Increase the delay in reconnects by 250ms each attempt, up to 16 seconds.
* Back off exponentially for **HTTP errors** for which reconnecting would be appropriate. Start with a 5 second wait, doubling each attempt, up to 320 seconds.
* Back off exponentially for **HTTP 420 errors**. Start with a 1 minute wait and double each attempt. Note that every HTTP 420 received increases the time you must wait until rate limiting will no longer will be in effect for your account.

Connection churn
----------------

Repeatedly opening and closing a connection (churn) wastes server resources. Keep your connections as stable and long-lived as possible.

Avoid mobile (cellular network) connections from mobile devices. WiFi is generally OK.

Delay opening a streaming connection in cases where the user may quit the application quickly.

If your client works in an environment where the connection quality changes over time, attempt to detect flaky connections. When detected, fall back to REST polling until the connection quality improves.

Rate limiting
-------------

Clients which do not implement backoff and attempt to reconnect as often as possible will have their connections rate limited for a small number of minutes. Rate limited clients will receive HTTP 420 responses for all connection requests.

Clients which break a connection and then reconnect frequently (to change query parameters, for example) run the risk of being rate limited.

Twitter does not make public the number of connection attempts which will cause a rate limiting to occur, but there is some tolerance for testing and development. A few dozen connection attempts from time to time will not trigger a limit. However, it is essential to stop further connection attempts for a few minutes if a HTTP 420 response is received. If your client is rate limited frequently, it is possible that your IP will be blocked from accessing Twitter for an indeterminate period of time.

Best practices
--------------

### Test backoff strategies

A good way to test a backoff implementation is to use invalid authorization credentials and examine the reconnect attempts. A good implementation will not get any 420 responses.

### Issue alerts for multiple reconnects

If a client reaches its upper threshold of its time between reconnects, it should send you notifications so you can triage the issues affecting your connection.

### Handle DNS changes

Test that your client process honors the DNS Time To live (TTL). Some stacks will cache a resolved address for the duration of the process and will not pick up DNS changes within the proscribed TTL. Such aggressive caching will lead to service disruptions on your client as Twitter shifts load between IP addresses.

### User Agent

Ensure your user-agent HTTP header includes the client’s version. This will be critical in diagnosing issues on Twitter’s end. If your environment precludes setting the user-agent field, then set an x-user-agent header.

HTTP Error Codes
----------------

Most error codes are returned with a string with additional details. For all codes greater than 200, clients should wait before attempting another connection. See the Connecting section, above.

|  |  |  |
| --- | --- | --- |
| Status | Text | Description |
| **200** | **Success** | Self evident. |
| **401** | **Unauthorized** | HTTP authentication failed due to either:* Invalid basic auth credentials, or an invalid OAuth request.
* Out-of-sync timestamp in your OAuth request (the response body will indicate this).
* Too many incorrect passwords entered or other login rate limiting.
 |
| **403** | **Forbidden** | The connecting account is not permitted to access this endpoint. |
| **404** | **Unknown** | There is nothing at this URL, which means the resource does not exist. |
| **406** | **Not Acceptable** | At least one request parameter is invalid. For example, the filter endpoint returns this status if:* The track keyword is too long or too short.
* An invalid bounding box is specified.
* Neither the track nor follow parameter are specified.
* The follow user ID is not valid.
 |
| **413** | **Too Long** | A parameter list is too long. For example, the filter endpoint returns this status if:* More track values are sent than the user is allowed to use.
* More bounding boxes are sent than the user is allowed to use.
* More follow user IDs are sent than the user is allowed to follow.
 |
| **416** | **Range Unacceptable** | For example, an endpoint returns this status if:* A count parameter is specified but the user does not have access to use the count parameter.
* A count parameter is specified which is outside of the maximum/minimum allowable values.
 |
| **420** | **Rate Limited** | The client has connected too frequently. For example, an endpoint returns this status if:* A client makes too many login attempts in a short period of time.
* Too many copies of an application attempt to authenticate with the same credentials.
 |
| **503** | **Service Unavailable** | A streaming server is temporarily overloaded. Attempt to make another connection, keeping in mind the connection attempt rate limiting and possible DNS caching in your client. |

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