API Structure - ThreatExchange - Documentation - Meta for Developers

ThreatExchange* Get Started
* Get Access
* Best Practices
* UI Overview
* UI Reference
* API Overview
* API Examples
* API Structure
* API Reference
* Privacy Controls
* Submitting Data
* Editing Existing Data
* Delete Data
* Re-sharing
* React to Data
* Submit Connections
* Integrations
* Webhooks
* FAQ
* Webinar
* Changelog
API Structure for ThreatExchange
================================
ThreatExchange is a subset of API endpoints within the larger ecosystem of Facebook Graph APIs. It is recommended to review the Graph API documentation, as it covers key concepts: usage of access tokens for authentication, result pagination, and batching.
The ThreatExchange APIs are made up of various objects and each object can have connections to other objects. For instance, a threat indicator is an object that can be connected to other threat indicators.
ThreatExchange also allows for multiple members to share the same threat indicator. Because there is the potential for a collision, we separate each member's submission into distinct ThreatDescriptor objects, which are connected to their respective ThreatIndicator
Viewing Individual Objects
--------------------------
You can access a Graph object’s properties with its unique ID, e.g. for a ThreatIndicator object:
* /{threat\_indicator\_id}
You can do the same for all other objects type within ThreatExchange:
* /{threat\_descriptor\_id}
Queries For Multiple Objects
----------------------------
Queries into ThreatExchange are HTTP GET requests to one of the following URLs:
* /threat\_descriptors
* /threat\_indicators
* /threat\_exchange\_members
* /threat\_privacy\_groups
* /{privacy\_group\_id}/threat\_updates
**All Graph API objects work in a similar way. After you have authenticated, try some calls with the `threat_indicator` object.**
To ensure consistency, the ThreatExchange APIs and its consumers use JSON objects as their default currency. Using these APIs gives you a lot of things for free:
* Field validation
* Type checking
* Persistence to Facebook's Graph
* Everyone else can use what you share and be better protected!
All objects are formatted as maps using a predefined set of field names, with expected value types. They can be of arbitrary size and field order in the map is, generally, not important.