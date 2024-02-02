::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

LinkedIn V2 APIs support two protocol versions: 1.0 and 2.0. See the
following syntax differences to help you migrate from 1.0 to 2.0.

LinkedIn plans to deprecate protocol version 1.0 in the near future. We
strongly encourage developers to migrate as soon as possible and take
advantage of the performance improvements in protocol version 2.0.

To use version 2.0, you must pass ` X-Restli-Protocol-Version: 2.0.0 `
as the header in your API requests. If you don\'t pass a header, your
call will default to version 1.0.

## Single Resource Key

When performing a GET, PARTIAL_UPDATE, or DELETE on a resource, you must
supply the resource key. See the following protocol version 1.0 example:

``` lang-https
GET https://api.linkedin.com/urn:li:endorsement:(urn:li:person:2qXA98-mVk,65761962366)
```

In protocol version 2.0, you must URL encode the entire resource key.
The ` ( ` must be encoded to ` %28 ` , ` ) ` to ` %29 ` , ` : ` to
` %3A ` and ` , ` to ` %2C ` . See the following example:

``` lang-https
GET https://api.linkedin.com/v2/endorsement/urn%3Ali%3Aendorsement%3A%28urn%3Ali%3Aperson%3A2qXA98-mVk%2C65761962366%29
```

Note that special characters in a params string not part of a resource
key should not be encoded. See the following example where parentheses
are not encoded:

``` lang-https
GET https://api.linkedin.com/v2/ugcPosts?q=authors&authors=List(urn%3Ali%3Aorganization%3A12345)
```

In cases where only numeric ID are passed in as the primary resource
key, nothing will change from 1.0 to 2.0. Some APIs require a compound
or complex key. The following table lists the syntax differences:

  Key Type                        Version 1.0                                                        Version 2.0
  ------------------------------- ------------------------------------------------------------------ --------------------------------------------------------------
  primitive key, long             3                                                                  3
  primitive key, string           someString                                                         someString
  compound key with association   stringKey=string&longKey=5                                         (stringKey:string,longKey:5)
  complex key                     \$param.a=value&\$param.b=value &keyPart1=value1&keyPart2=value2   (\$param:(a:value,b:value), keyPart1:value1,keyPart2=value2)

## Multiple Resource Keys

To perform a ` BATCH_GET ` in protocol version 1.0:

``` lang-https
GET https://api.linkedin.com/people?ids=1&ids=2&ids=3
```

In protocol version 2.0, you must change this query to a ` List `
syntax:

``` lang-https
GET https://api.linkedin.com/v2/people?ids=List(1,2,3,4)
```

## Complex Keys

In protocol version 1.0, if a resource has complex keys:

``` lang-https
GET https://api.linkedin.com/people?ids[0].$params.a=value0A&ids[0].$params.b=value0B&ids[1].$params.a=value1A&ids[1].$params.b=value1B&ids[2].$params.a=value2A&ids[2].$params.b=value2B
```

In protocol version 2.0, if a resource has complex keys:

``` lang-https
GET https://api.linkedin.com/people?ids=List(($params.a:value0A,$params.b:value0B),($params.a:value1A,$params.b:value1B),($params.a:value2A,$params.b:value2B))
```

::: NOTE
Note

The values and the resource parameters must be URL encoded but not the
` , ` grouping the fields and values. The single resource key had the
` , ` encoded because it was part of the whole value.
:::

## Parameters

When performing a ` FINDER ` in version 1.0, you often have query
parameters such as filters represented as an array:

``` lang-https
GET https://api.linkedin.com/resource?q=FinderParam&param.aList[0]=foo&param.aList[1]=bar&param.aList[2]=baz& param.anObject.aField=1&param.anObject.anotherField=value
```

In protocol version 2.0, you must change this query to a ` List `
syntax, much like the multiple keys:

``` lang-https
GET https://api.linkedin.com/resource?q=myFinder&param=(aList:List(foo,bar,baz),anObject:(aField:1,anotherField:value))
```

::: NOTE
Note

The values and the resource parameters must be URL encoded but not the
` , ` grouping the fields and values. The single resource key had the
` , ` encoded because it was part of the whole value.
:::
:::
