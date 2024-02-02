::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

[URNs](http://www.ietf.org/rfc/rfc2141.txt) are used to represent
foreign associations to an entity (persons, organizations, and so on) in
an API. A URN is a string-based identifier with the format:

` urn:{namespace}:{entityType}:{id} `

For example:

-   ` urn:li:person:123 `
-   ` urn:li:organization:456 `
-   ` urn:li:sponsoredAccount:789 `

URNs encode more information, including the entity type. Using the
entity type, it\'s possible to dereference a URN and access the
underlying data of the entity using a process called
[decoration](decoration?context=linkedin/context) .

URN values returned from LinkedIn\'s APIs are a maximum of 255
characters in length.

## IDs

Simple integer IDs are returned to represent an object\'s primary key.
Your application should support transforming URNs into IDs and vice
versa.

## IDs versus URNs

IDs are self-referencing identifiers similar to a primary key. URNs are
Globally Unique Identifiers (GUID) used to represent an entity\'s
foreign associations.

In the example below, we fetch details about a share and use a
[projection](projections?context=linkedin/context) to limit the results
to the ` id ` and ` owner ` fields. The ` shares ` API returns an ` id `
that is the primary key and an ` owner ` that is a foreign reference to
the person who created the share in the form of a ` URN ` .

  Resource Type   URN                            ID
  --------------- ------------------------------ ------------
  Share           ` urn:li:share:1234 `          1234
  Person          ` urn:li:person:-f_Ut43FoQ `   -f_Ut43FoQ

#### Sample Request

``` lang-https
GET https://api.linkedin.com/v2/shares/1234?projection=(id,owner)
```

``` lang-json
{
    "id": "1234",
    "owner": "urn:li:person:-f_Ut43FoQ"
}
```

## URN Deconstruction

To get more information about the owner of the share, we can deconstruct
the URN by removing the ` urn:li:person ` prefix and making an
additional call to the ` people ` API. We need to deconstruct the URN
and parse the ID because the ` people ` API expects an ID.

#### Sample Request

``` lang-https
GET https://api.linkedin.com/v2/people/id=-f_Ut43FoQ?projection=(id,localizedFirstName,localizedLastName)
```

``` lang-json
{
    "id": "-f_Ut43FoQ",
    "localizedFirstName": "Dwight",
    "localizedLastName": "Schrute"
}
```

## URN Decoration

To make this query more efficient, we can use
[decoration](decoration?context=linkedin/context) to expand the share
owner URN and return the owner\'s first and last name in a single call.
This saves an API call by not having to make a separate call to the
` people ` API.

#### Sample Request

``` lang-https
GET https://api.linkedin.com/v2/shares/1234?projection=(id,owner~(localizedFirstName,localizedLastName))
```

``` lang-json
{
    "id": "1234",
    "owner": "urn:li:person:-f_Ut43FoQ",
    "owner~": {
        "localizedFirstName": "Schrute",
        "localizedLastName": "Dwight"
    }
}
```

## URNs and Namespaces

For common URNs and their namespace conversions, see [URN
Namespaces](../../references/v2/urn-namespace?context=linkedin/context)
.
:::
