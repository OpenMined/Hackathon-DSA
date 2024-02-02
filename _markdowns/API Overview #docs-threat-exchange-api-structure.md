::: {._4-u3 ._588p}
ThreatExchange is a subset of API endpoints within the larger ecosystem
of Facebook Graph APIs. It is recommended to review the [Graph API
documentation](/docs/graph-api) , as it covers key concepts: usage of
access tokens for authentication, result pagination, and batching.

The ThreatExchange APIs are made up of various
[objects](/docs/threat-exchange/reference/apis) and each object can have
connections to other objects. For instance, a threat indicator is an
object that can be connected to other threat indicators.

ThreatExchange also allows for multiple members to share the same threat
indicator. Because there is the potential for a collision, we separate
each member\'s submission into distinct
[ThreatDescriptor](/docs/threat-exchange/reference/apis/threat-descriptor)
objects, which are connected to their respective
[ThreatIndicator](/docs/threat-exchange/reference/apis/threat-indicator)

## Viewing Individual Objects {#individual_objects}

You can access a Graph object's properties with its unique ID, e.g. for
a
[ThreatIndicator](/docs/threat-exchange/reference/apis/threat-indicator)
object:

You can do the same for all other objects type within ThreatExchange:

## Queries For Multiple Objects {#multiple_objects}

Queries into ThreatExchange are HTTP GET requests to one of the
following URLs:

**All Graph API objects work in a similar way. After you have
[authenticated](/docs/threat-exchange/getting-started) , try some calls
with the
[` threat_indicator `](/docs/threat-exchange/reference/apis/threat-indicator)
object.**

To ensure consistency, the ThreatExchange APIs and its consumers use
JSON objects as their default currency. Using these APIs gives you a lot
of things for free:

-   Field validation

-   Type checking

-   Persistence to Facebook\'s Graph

-   Everyone else can use what you share and be better protected!

All objects are formatted as maps using a predefined set of field names,
with expected value types. They can be of arbitrary size and field order
in the map is, generally, not important.
:::
