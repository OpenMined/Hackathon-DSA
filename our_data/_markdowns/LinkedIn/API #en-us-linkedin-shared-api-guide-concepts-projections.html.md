
Field Projections - LinkedIn | Microsoft Learn

Skip to main content

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

Download Microsoft Edge
More info about Internet Explorer and Microsoft Edge

Table of contents 

Exit focus mode

Read in English

Save

Table of contents
Read in English

Save
Edit

Print

Twitter
LinkedIn
Facebook
Email

Table of contents

Field Projections
=================

* Article
* 05/08/2023
* 3 contributors

Feedback

In this article
---------------

Field projection controls how much of an entity's data is displayed in response to an API request.

All APIs have a default set of field projections that control which fields are returned. If you don't need certain fields, you can decrease response time and payload size by using a projection to ask only for the fields your application is interested in.

By default, services may not always return all of the information that your application requests. In these cases, you'll need to use a projection to retrieve any non-default fields.

Field projections are defined using the `&fields=` query parameter and narrowed by providing a comma-separated list of field names that you want returned as the value of the parameter.

In the following example, a service returns these types of objects:

#### Sample Objects

```
{
    "id" : int,      <- Default projection field
    "foo": string,   <- Default projection field
    "bar": boolean,
    "baz": Object
}
```
A GET call to retrieve one of these objects provides the following response:

```
GET https://api.linkedin.com/v2/sampleService/42
```
#### Sample Response

```
{
    "foo": "Zing!",
    "id": 42
}
```
Notice how the `bar` and `baz` fields were not returned in the response. This is because they are not part of the service's default field projection.

If you want to get `id`, `bar`, and `baz` back in the response (but not `foo`, because it's irrelevant to your application), use a field projection:

```
GET https://api.linkedin.com/v2/sampleService/42?fields=id,bar,baz
```
#### Sample Response

```
{
    "bar": true,
    "baz": {
        "beep": "Yay!",
        "bloop": "Meh",
        "blorp": "Boo!"
    },
    "id": 42
}
```
Child Objects
-------------

In the above example, `baz` is returned in the response due to the field projection specified because `baz` is an object that has its own fields. Use field projections to select the data you need.

Use the `parentField:(child**Field_1,…,childField_n**)` syntax to select fields for a child object:

```
GET https://api.linkedin.com/v2/sampleService/42?fields=id,baz:(beep)
```
#### Sample Response

```
{
    "baz": {
        "beep": "Yay!"
    },
    "id": 42
}
```
Parent Field as Map
-------------------

Objects can have nested objects with child fields of their own such as the example below:

#### Sample Data

```
{
    "baz": {
        "1": {
            "beep": "Yay!",
            "foo": "foo1"
        },
        "2": {
            "beep": "Nay!",
            "foo": "foo2"
        }
    },
    "id": 42
}
```
Use the `$*:(childField_1,…,childField_n)` syntax to control the fields requested from nested objects:

```
GET https://api.linkedin.com/v2/sampleService/42?fields=id,baz:($*:(beep))
```
#### Sample Response

```
{
    "baz": {
        "1": {
            "beep": "Yay!"
        },
        "2": {
            "beep": "Nay!"
        }
    },
    "id": 42
}
```

---

Feedback
--------

Was this page helpful?

Yes

No

Provide product feedback

Feedback
--------

Submit and view feedback for

This product
This page

View all page feedback

---

Additional resources
--------------------

California Consumer Privacy Act (CCPA) Opt-Out Icon

Your Privacy Choices

Theme

* Light
* Dark
* High contrast

* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2024

Additional resources
--------------------

### In this article

California Consumer Privacy Act (CCPA) Opt-Out Icon

Your Privacy Choices

Theme

* Light
* Dark
* High contrast

* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2024