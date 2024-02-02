
Disconnections explained | Docs | Twitter Developer Platform 

Disconnections explained

Disconnections explained
------------------------

Disconnects from your PowerTrack stream can happen for a handful of reasons - whether they proactively planned or unplanned. Regardless of whether or not they were planned, any sort of disconnect can be surprising cause for data loss, but they don’t have to be. A basic understanding of the types of disconnects that you might encounter and how to quickly reconnect can mean the difference between a major issue and something that can be incorporated into your application design by reconnecting, or using Backfill or Recovery. Please note that for any disconnect, forced or client-side, your console.gnip.com dashboard will have a message that displays the kind of disconnect that you experienced and a timestamp for the disconnect.  

This article will go over the types of disconnects you might encounter, how to minimize their effects, and how to troubleshoot issues related to disconnects.  

### Forced disconnects

At the highest level, forced disconnects happen when Twitter actively closes your connection to the stream. These can happen for a variety of reasons, and when you are force disconnected from your stream then Twitter will send a zero byte chunk in accordance with HTTP chunked encoding practice. In all cases of forced disconnects, you should be able to reconnect to the stream immediately and you should be sure to have reconnect logic written into your code to prevent further data loss.

There are three types of forced disconnects that your app will need to be prepared for.  

#### **Twitter maintenance**

Twitter deploys for ongoing maintenance several times a week. During these updates, sometimes customer streams will experience one or more disconnects. This will be accompanied by a “Twitter is closing for operational reasons” message. These should be expected disconnections, and your application should be able to reconnect immediately, so make sure that you have reconnect logic written into your application.  

#### **Full buffer disconnect**

A full buffer disconnect generally indicates that your application’s code isn’t keeping up with the amount of data that we’re streaming to you and there is a backup of cached data on the Twitter server side for your connection which needs to be flushed. This can happen after a major rule change, a big event, or simply because your application is having trouble consuming the stream. Full buffer disconnects are triggered when your stream connection buffer hits a certain threshold of Tweets. If you are disconnected for a full buffer, reconnecting with backfill is not available and data will begin streaming from the time you reconnect. It's likely that you will need to run a Recovery to recover Tweets lost in the disconnection. If you find that full buffer disconnects are happening frequently, reach out to the support team to assist you in making sure that your application is properly configured. 

Here are some suggestions to prevent these kinds of disconnects from occurring in the future:

1. Ensure nothing is slowing down the process reading from the stream. Do not do any processing in the process/thread that is reading from the stream. Instead, have this process read the message then pass off any processing (such as parsing, date calculations, etc) of the message to a separate process or thread.
2. Verify there are no network issues between your application and Twitter preventing messages from being sent.
3. Make sure you have sufficient bandwidth for the volume of activities on your stream.  Some streams can have high volumes requiring significant bandwidth (~10 Mbps is not unheard of). Keep in mind these streams require this bandwidth to be sustained 24 hours a day, including spikes that may cause 2-3 times the volume during significant world events. These spikes are often absorbed by Twitter's buffer, and are one of the reasons it is in place.

#### **Too many connections**

Each stream is configured to allow for a specified number of connections. This number is determined between you and your account manager, and is available in your account agreement. If you connect to your stream with more connections than are allowed, you will be force disconnected. Any extra connections are allowed for approximately one minute. If after one minute an extra connection exists, the most recent connection is forced disconnected. Allowing an extra connection for a minute enables the customer to, for example, spin up a new server and connect with it, then teardown a server that is being ‘retired.’  

### Client disconnects

A client disconnect is essentially any disconnection that occurs which isn’t initiated by our servers. There are many causes for this. Sometimes this could be caused by the code or the architecture of your application, but this often occurs when something in the internet or network layer cuts off the connection. This section provides a list of the most common causes for a client disconnects.  

**Issues at the network layer**

Routing issues at the networking level can cause disconnects. For example, a Border Gateway Protocol (BGP) update can go awry, and clients can disconnect as routers fail to keep up with the sudden additional load put on them when a route fails. As network operators cooperate to reroute traffic, you may notice a pattern of disconnects for some time.  

**Firewall configuration**

Clients may have firewalls set up with session limits that cut off the connections after a certain amount of time, which they need to create exceptions for. From our side, our servers just see the connection close, so we don’t have a way to see whether it was closed by the proactive actions of your app, or just something related to the internet connection between your client and the Twitter servers.  

**Data burst and packet loss**

Clients should be designed to handle spikes in the volume of Tweets received. If a client is slow to consume a stream, it will receive a full buffer disconnect. However, there are situations where the client is not able to handle a sudden surge in volume (for example, after significant rule activity) which will cause the client to drop packets. When this happens, you may notice the client resetting a TCP/IP connection. In certain cases, the connection is terminated correctly and cleanly; however, there may be situations where the underlying networking layer doesn't close the socket properly, or does so after a set delay. In your dashboard, this event will be reported as a client disconnect. In such cases, clients must be sized to handle multiple times the average Tweet volume. It can be beneficial to examine the network traffic to detect any pattern that leads the client to drop packets.  

**Failure to reconnect after a disconnection**

Occasionally, some customers have trouble reconnecting to their stream after they’ve terminated a connection. Assuming there are no operational issues posted on our Status Page, one reason might be that something within your code is keeping the connection alive. In these scenarios, we see something in the layer outside of your app persisting, because the connection wasn’t properly terminated. Generally we see similar behavior when the HTTP client portion of the code isn’t getting proactively closed. It might also be that there is simply some network latency or delay set at the configuration level preventing the request from going through.

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