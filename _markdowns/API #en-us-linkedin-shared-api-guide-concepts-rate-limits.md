::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

To prevent abuse and ensure service stability, all API requests are rate
limited. Rate limits specify the maximum number of API calls that can be
made in a 24 hour period. These limits reset at midnight
[UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) every
day.

There are two kinds of limits that affect your application:

-   **Application** --- The total number of calls that your application
    can make in a day.
-   **Member** --- The total number of calls that a single member per
    application can make in a day.

::: NOTE
Note

The term ` Member ` refers to a LinkedIn user whose token is used to
initiate API calls from the developer application. For example, a
partner is responsible for managing multiple members. This member-level
designation indicates the permissible number of API calls the partner
can initiate from their application on behalf of a member token.
:::

Rate limited requests will receive a 429 response. In rare cases,
LinkedIn may also return a 429 response as part of infrastructure
protection. API service will return to normal automatically.

Your application\'s daily rate limit varies based on which API endpoint
you are using. Standard rate limits are not published in documentation.
You can look up the rate limit of any endpoint your app has access to
through the [Developer Portal](https://www.linkedin.com/developers/apps)
. Select your app from the list and navigate to its Analytics tab. This
page will only show usage and rate limits for endpoints you have made at
least 1 request to today(UTC). If you want to look up a rate limit for
an endpoint not listed in your app\'s Analytics page, make 1 test call
to that endpoint and refresh the Analytics page.

![Rate Limits in the Developer
Portal](../../../api-guide/media/dev-portal-rate-limit.png)
:::
