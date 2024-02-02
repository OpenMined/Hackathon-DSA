::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

::: WARNING
Warning

**Deprecation Notice**\
The use of Response Decoration is deprecated in some versions of LMS
APIs. Please refer the [Recent
Changes](../../../marketing/integrations/recent-changes) page for
information on the specific API versions that are affected by this
deprecation.
:::

When you call an API, the response may contain
[URNs](urns?context=linkedin/context) referencing the different types of
objects provided by LinkedIn\'s services. These URNs are valuable on
their own; however, there may be instances when you want to expand a URN
and access the values associated with the entity.

Decoration is a mechanism in LinkedIn\'s APIs to fetch data belonging to
a URN object without having to make an extra call to that object\'s API.
Decoration uses a syntax very similar to LinkedIn\'s [Field
Projections](projections?context=linkedin/context) .

See the following example of a service that returns URN references to
another type of entity:

#### Sample Request

``` lang-https
GET https://api.linkedin.com/v2/{service}/1234
```

#### Sample Response

``` lang-json
{
    "id": 1234,
    "relatedEntity": "urn:li:relatedEntity:6789"
}
```

Rather than taking the ` relatedEntity ` URN value and making a second
GET call to its parent service, you can use decoration to define how
you\'d like the ` relatedEntity ` object to be expanded within the
original API request. To do this, append the ` ~ ` character to
the entity you wish to expand, and then provide the field projection in
parentheses afterwards. For example:

#### Sample Request

``` lang-https
GET https://api.linkedin.com/v2/{service}/1234&projection=(id,relatedEntity~($URN,foo,bar))
```

#### Sample Response

``` lang-json
{
    "id": 1234,
    "relatedEntity": {
        "$URN": "urn:li:relatedEntity:6789",
        "bar": "bloop",
        "foo": "bleep"
    }
}
```

## Decorating within Arrays/Lists

In some circumstances, a service might return a collection of URNs that
are not all of the same type. In this case, provide multiple decoration
instructions to tell the service how to deal with any potential URN type
that is returned. See the following sample request and the list of
different URN types that it returns within entities:

#### Sample Request

``` lang-https
GET https://api.linkedin.com/v2/{service}/1234
```

#### Sample Data

``` lang-json
{
    "entities": [
        "urn:li:foo:123",
        "urn:li:bar:234",
        "urn:li:baz:345"
    ],
    "id": 1234
}
```

To decorate each of the ` foo ` , ` bar ` , and ` baz ` URN types in
this response, use the following projection syntax in your request:

#### Sample Request

``` lang-https
GET https://api.linkedin.com/v2/{service}/1234?projection=entities*~foo(a,b)~bar(c,d)~baz(e,f))
```

#### Sample Response

``` lang-json
{
    "entities": [
        {
            "a": 1,
            "b": 2
        },
        {
            "c": 10,
            "d": 20
        },
        {
            "e": 100,
            "f": 200
        }
    ],
    "id": 1234
}
```

## Sample Projections

Consider the following data model of a sample resource and review the
below samples showing how to access various parts of this data in order
to decorate.

``` lang-json
{
    "person": {
        "current_position": {
            "company": "urn:li:company:1",
            "from": "2009",
            "job_title": "SWE"
        },
        "firstname": "First Name",
        "following_companies": [
            "urn:li:company:1",
            "urn:li:company:2"
        ],
        "lastname": "Last Name",
        "messages": {
            "urn:li:message:1": {
                "bcc": [
                    "urn:li:person:1",
                    "urn:li:person:39"
                ],
                "content": "xyz",
                "from": "urn:li:person:99"
            },
            "urn:li:message:2": {
                "bcc": [
                    "urn:li:person:1",
                    "urn:li:person:80"
                ],
                "content": "abc",
                "count": 1929
            }
        },
        "phone": "200-100-200",
        "position_history": [
            {
                "company": "urn:li:company:4888383",
                "from": "2006",
                "job_title": "SSE",
                "to": "2009"
            },
            {
                "company": "urn:li:company:39939",
                "from": "1999",
                "job_title": "SE",
                "to": "2006"
            }
        ]
    }
}
```

## Accessing URN within a child object

**` (person(current_position(company))) `**

``` lang-json
{
    "person": {
        "current_position": {
            "company": "urn:li:company:1"
        }
    }
}
```

## Accessing URNs within an array of child objects

**` (person(position_history(*(company)))) `**

``` lang-json
{
    "person": {
        "position_history": [
            {
                "company": "urn:li:company:4888383"
            },
            {
                "company": "urn:li:company:39939"
            }
        ]
    }
}
```

## Accessing URNs within an array of URNs

**` (person(following_companies(*))) `**

``` lang-json
{
    "person": {
        "following_companies": [
            "urn:li:company:1",
            "urn:li:company:2"
        ]
    }
}
```

## Selecting a single child field with a URN and expanding the URN

**` (person(current_position(company~))) `**

``` lang-json
{
    "person": {
        "current_position": {
            "company": "urn:li:company:1",
            "company~": {
                "active": true,
                "administrators": [
                    "urn:li:person:6611647"
                ],
                "allEmployeesAsAdmins": false,
                "attributes": {
                    "disableThirdPartyNews": false,
                    "enableStatusUpdate": false,
                    "owns300x250RightAdSlot": false,
                    "paidCareers": false,
                    "paidGoldPlusCareers": false,
                    "paidPlatinumCareers": false,
                    "paidProducts": false,
                    "paidSilverCareers": false,
                    "paidSilverPlusCareers": false,
                    "showAnalytics": false,
                    "showBrandTree": false,
                    "showNews": true,
                    "showPastEmployees": false,
                    "silverProducts": false,
                    "useParentCareers": false
                },
                "companyId": 1,
                "companyType": "PUBLIC_COMPANY",
                "creationTime": 1375816467585,
                "creator": "urn:li:person:6611647",
                "dataVersion": 4,
                "descriptions": [
                    {
                        "description": "test test test testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest test",
                        "locale": "en_US"
                    }
                ],
                "employeeCountRange": "MYSELF_ONLY",
                "heroImage": {
                    "cropHeight": 220,
                    "cropWidth": 646,
                    "cropXPosition": 0,
                    "cropYPosition": 0,
                    "croppedImage": "urn:li:media:/p/2/005/045/187/3d49ef0.png",
                    "height": 220,
                    "uncroppedImage": "urn:li:media:/p/2/005/045/187/3b333d8.png",
                    "width": 646
                },
                "images": [
                    {
                        "originalMedia": "urn:li:media:/p/2/005/045/188/1d5f329.png",
                        "type": "SQUARE_LOGO_LEGACY",
                        "urn": "urn:li:media:/p/2/005/045/188/1d5f329.png"
                    },
                    {
                        "originalMedia": "urn:li:media:/p/2/005/045/188/24809b3.png",
                        "type": "LOGO_LEGACY",
                        "urn": "urn:li:media:/p/2/005/045/188/24809b3.png"
                    }
                ],
                "industries": [
                    "ACCOUNTING"
                ],
                "lastEditor": "urn:li:person:6611647",
                "lastModifiedTime": 1375816467585,
                "logo": "urn:li:media:/p/2/005/045/188/24809b3.png",
                "names": [
                    {
                        "active": true,
                        "locale": "en_US",
                        "name": "r-NQkR5TwJ",
                        "type": "CANONICAL"
                    }
                ],
                "organizationalEntity": "urn:li:organization:1",
                "squareLogo": "urn:li:media:/p/2/005/045/188/1d5f329.png",
                "status": "OPERATING",
                "stockSymbol": "",
                "twitterId": "",
                "universalName": "r-nqkr5twj",
                "websiteUrl": "https://www.whatismyreferer.com/"
            }
        }
    }
}
```

## Selecting all child fields and fully expanding a child field containing a URN

**` (person(current_position(*,company~))) `**

``` lang-json
{
    "person": {
        "current_position": {
            "company": "urn:li:company:1",
            "company~": {
                "active": true,
                "administrators": [
                    "urn:li:person:6611647"
                ],
                "allEmployeesAsAdmins": false,
                "attributes": {
                    "disableThirdPartyNews": false,
                    "enableStatusUpdate": false,
                    "owns300x250RightAdSlot": false,
                    "paidCareers": false,
                    "paidGoldPlusCareers": false,
                    "paidPlatinumCareers": false,
                    "paidProducts": false,
                    "paidSilverCareers": false,
                    "paidSilverPlusCareers": false,
                    "showAnalytics": false,
                    "showBrandTree": false,
                    "showNews": true,
                    "showPastEmployees": false,
                    "silverProducts": false,
                    "useParentCareers": false
                },
                "companyId": 1,
                "companyType": "PUBLIC_COMPANY",
                "creationTime": 1375816467585,
                "creator": "urn:li:person:6611647",
                "dataVersion": 4,
                "descriptions": [
                    {
                        "description": "test test test testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest testtest test",
                        "locale": "en_US"
                    }
                ],
                "employeeCountRange": "MYSELF_ONLY",
                "heroImage": {
                    "cropHeight": 220,
                    "cropWidth": 646,
                    "cropXPosition": 0,
                    "cropYPosition": 0,
                    "croppedImage": "urn:li:media:/p/2/005/045/187/3d49ef0.png",
                    "height": 220,
                    "uncroppedImage": "urn:li:media:/p/2/005/045/187/3b333d8.png",
                    "width": 646
                },
                "images": [
                    {
                        "originalMedia": "urn:li:media:/p/2/005/045/188/1d5f329.png",
                        "type": "SQUARE_LOGO_LEGACY",
                        "urn": "urn:li:media:/p/2/005/045/188/1d5f329.png"
                    },
                    {
                        "originalMedia": "urn:li:media:/p/2/005/045/188/24809b3.png",
                        "type": "LOGO_LEGACY",
                        "urn": "urn:li:media:/p/2/005/045/188/24809b3.png"
                    }
                ],
                "industries": [
                    "ACCOUNTING"
                ],
                "lastEditor": "urn:li:person:6611647",
                "lastModifiedTime": 1375816467585,
                "logo": "urn:li:media:/p/2/005/045/188/24809b3.png",
                "names": [
                    {
                        "active": true,
                        "locale": "en_US",
                        "name": "r-NQkR5TwJ",
                        "type": "CANONICAL"
                    }
                ],
                "organizationalEntity": "urn:li:organization:1",
                "squareLogo": "urn:li:media:/p/2/005/045/188/1d5f329.png",
                "status": "OPERATING",
                "stockSymbol": "",
                "twitterId": "",
                "universalName": "r-nqkr5twj",
                "websiteUrl": "https://www.whatismyreferer.com/"
            },
            "from": "2009",
            "job_title": "SWE"
        }
    }
}
```

## Selecting all child fields and expanding child field with a URN for a single value

**` (person(current_position(*,company~(vanityName)))) `**

``` lang-json
{
    "person": {
        "current_position": {
            "company": "urn:li:company:1",
            "company~": {},
            "from": "2009",
            "job_title": "SWE"
        }
    }
}
```

## Accessing complex type object

When a URN is a field's key and the value is an object, it is called a
complex type object. In the following example, the ` messages ` field
maps to an object with 2 fields that are ` MessageUrns ` . These 2
` MessageUrns ` are keys that map to objects containing data such as
` bcc ` , ` count ` , and ` content ` . To access the ` bcc ` values for
each ` MessageUrn ` , use the decoration
` (person(messages()))(person(messages(*(from,bcc(*))))) ` .

**` (person(messages())) `**

``` lang-json
{
    "person": {
        "messages": {
            "urn:li:message:1": {
                "bcc": [
                    "urn:li:personr:1",
                    "urn:li:person:39"
                ],
                "content": "xyz",
                "from": "urn:li:person:99"
            },
            "urn:li:message:2": {
                "bcc": [
                    "urn:li:person:1",
                    "urn:li:person:80"
                ],
                "content": "abc",
                "count": 1929
            }
        }
    }
}
```

**` (person(messages(*(from,bcc(*))))) `**

``` lang-json
{
    "person": {
        "messages": {
            "urn:li:message:1": {
                "bcc": [
                    "urn:li:person:1",
                    "urn:li:person:39"
                ],
                "from": "urn:li:person:99"
            },
            "urn:li:message:2": {
                "bcc": [
                    "urn:li:person:1",
                    "urn:li:person:80"
                ]
            }
        }
    }
}
```

## Accessing all URNs within any array from a BATCH_GET call

Note that a BATCH_GET call returns a ` results ` field by default.

**` (results(*(person(following_companies(*))))) `**

#### Sample Data

``` lang-json
{
    "results": {
        "123123": {
            "person": {
                "current_position": {
                    "company": "urn:li:company:1",
                    "from": "2009",
                    "job_title": "SWE"
                },
                "firstname": "First Name",
                "following_companies": [
                    "urn:li:company:1",
                    "urn:li:company:2"
                ],
                "lastname": "Last Name",
                "messages": {
                    "urn:li:message:1": {
                        "bcc": [
                            "urn:li:person:1",
                            "urn:li:person:39"
                        ],
                        "content": "xyz",
                        "from": "urn:li:person:99"
                    },
                    "urn:li:message:2": {
                        "bcc": [
                            "urn:li:person:1",
                            "urn:li:person:80"
                        ],
                        "content": "abc",
                        "count": 1929
                    }
                },
                "phone": "200-100-200",
                "position_history": [
                    {
                        "company": "urn:li:company:4888383",
                        "from": "2006",
                        "job_title": "SSE",
                        "to": "2009"
                    },
                    {
                        "company": "urn:li:company:39939",
                        "from": "1999",
                        "job_title": "SE",
                        "to": "2006"
                    }
                ]
            }
        }
    }
}
```

**` (results(*(person(following_companies(*))))) `**

``` lang-json
{
    "results": {
        "123123": {
            "person": {
                "following_companies": [
                    "urn:li:company:1",
                    "urn:li:company:2"
                ]
            }
        }
    }
}
```

::: NOTE
Note

Always use ` entity~ ` in the projection parameter to make the expansion
request. If the ` entity ` is expanded, the response returns ` entity~ `
. If for some reason the ` entity ` cannot be expanded, the response
returns ` entity! ` .
:::

## Rate Limiting

Response decoration makes calls to other services in order to resolve
the requested, decorated entity. These calls are subject to rate
limiting. It is possible for calls to return a 200 while the decoration
call is rate limited.

The following example makes a request to the ` /me ` endpoint and uses
response decoration to resolve the ` digitalMediaAsset ` URN in the
` displayImage ` field. The call to the ` /me ` endpoint is successful,
but the decoration call to resolve ` displayImage ` is rate limited.

``` lang-http
GET https://api.linkedin.com/v2/me?projection=(id,profilePicture(displayImage~(*)))
```

``` lang-json
{
    "profilePicture": {
        "displayImage!": {
            "serviceErrorCode": 101,
            "message": "Resource level throttle limit for calls to this resource is reached.",
            "status": 429
        },
        "displayImage": "urn:li:digitalmediaAsset:C4D03AQGFBHiaY1XXNA"
    },
    "id": "z6_nnTIGu-"
}
```
:::
