::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The Collections API responds with data structures that often depart from
the objects you traditionally encounter in the Twitter API.

In the Collections API, all identifiers (IDs, cursors, collection
positions) are presented as strings. These strings are safe to consume
and utilize in all programming languages, including those that do not
support 64-bit integers.

While representations of
[Tweets](https://dev.twitter.com/overview/api/tweets) and
[Users](https://dev.twitter.com/overview/api/users) generally match
other Twitter API representations, watch for minor differences in the
object structure, especially around data related to counts.

While the API typically returns objects-embedded-within-objects (such as
the author of a Tweet being embedded within the Tweet itself), these API
methods provide decomposed responses where each object type is grouped
together and each object is represented only once. Instead of containing
associated child objects, the objects contain simple ID references to
the association.

Here are some of the response structures you will encounter in the
Collections API.

## Object collections

API methods that return multiple objects of the same type are segmented
such that one component of the response contains the objects and any
associated objects while another component simply lists references to
those same objects and contextual information (such as cursors) needed
to navigate the boundaries of the collection in subsequent requests.

You will see responses like this in [GET collections /
list](https://dev.twitter.com/rest/reference/get/collections/list) .

### Structure

-   [ response ]{.code-inline} (object)
    -   [ results ]{.code-inline} (array of objects)
        -   each object typically contains one key/value pair housing an
            object's ID
    -   [ cursors ]{.code-inline} (object)
        -   [ next_cursor ]{.code-inline} (string)
        -   [ previous_cursor ]{.code-inline} (string)
-   [ objects ]{.code-inline} (object)
    -   [ users ]{.code-inline} (object, ID as key)
    -   [ tweets ]{.code-inline} (object, ID as key)
    -   [ timelines ]{.code-inline} (object, ID as key)

## Single objects

Even methods that return a single "primary object" respond with a
decomposed structure, similar to a collection.

Methods that can return only one core object:

You will see responses like this in: [GET collections /
show](https://dev.twitter.com/rest/reference/get/collections/show)

### Structure

[ response ]{.code-inline} (object)

-   a key/value pair indicating the object's type and identifier (e.g. [
    \"timeline_id\":\"custom-393773270547177472\" ]{.code-inline} )

[ objects ]{.code-inline} (object)

-   [ users ]{.code-inline} (object, ID as key)
-   [ tweets ]{.code-inline} (object, ID as key)
-   [ timelines ]{.code-inline} (object, ID as key)
:::
:::
:::
:::
:::
:::
:::
:::
