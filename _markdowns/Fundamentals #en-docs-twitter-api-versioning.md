::: is-table-default
Along with Twitter API v2, we launched a new versioning strategy that
enables developers to better understand when to expect changes to
Twitter's public APIs, and when they will need to migrate to new
versions.

Developers will be notified of deprecations, retirements, changes, and
additions to the Twitter API via our [communication
channels](/en/updates/stay-informed) so they can appropriately plan to
accommodate these changes in their development roadmap. All changes to
the API will be noted in the changelog.

The Twitter API currently has three different versions. We strongly
encourage users to utilize Twitter API v2 when planning their
integration unless we have not released functionality to v2 that is
required by your use case.

To learn more about each version, please visit the following pages:

## Versioning Strategy

Versioning for the Twitter API will be represented by version numbers
declared in the route path for our endpoints:

[ https://api.twitter.com/2/tweets ]{.code-inline}

We aim to release major versions of the Twitter API as necessary but no
more frequently than every 12 months. A major version will be released
when breaking changes are introduced in the API. We will publish
migration guides when launching a new major version to help developers
migrate over to the new version.

A breaking change requires developers to change their code to maintain
existing functionality in their app. Non-breaking changes will be
additive and rolled out to the most recent version when ready, requiring
no work on a developer's end unless you would like to take advantage of
the new functionality.

If a breaking change must be rolled out mid-cycle (for security or
privacy reasons), this change will be made to the most recent version.\

### Breaking changes

These changes require developers to change their code to maintain
existing functionality of their application.

-   Addition of a new required parameter
-   Removal of an existing endpoint
-   Removal of any field in the response (either required or optional)
-   Removal of a query parameter
-   Restructuring of the input or output format (for example, making a
    top-level field a sub-field, or changing the location of errors to
    be inline)
-   Changing the name or data type of an existing input parameter or
    output value
-   Changing the name of a field
-   Changing the resource name
-   Changing a response code
-   Changing error types
-   Changes to existing authorization scopes\

### Non-breaking changes

-   Addition of a new endpoint
-   Addition of a new optional parameter
-   Addition of a new response field
-   Changing text in error messages
-   Availability of new scopes
-   "Nulling" of fields (changing the value of a to null for
    privacy/security reasons as an alternative to removing it
    altogether)

### Deprecation and retirement

First of all, here is our definition of what deprecation and retirement
mean to the Twitter API:

-   **Deprecation:** The feature is no longer supported by the team. No
    new functionality will be released around that feature, and if there
    are any bugs or issues with the product, the chances that we will
    explore a fix are extremely low.
-   **Retired:** The feature will no longer be accessible.

\
In most cases, as soon as a new version is released, the previous
version will be marked as deprecated. Versions will remain in a
deprecated state for a period of time, after which they will be retired.

Please [stay informed](/en/updates/stay-informed) to learn more about
future deprecations and retirements.
:::
