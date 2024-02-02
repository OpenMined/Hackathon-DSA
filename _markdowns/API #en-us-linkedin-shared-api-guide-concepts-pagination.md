::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

API calls that return a large number of entities are broken up into
multiple pages of results. You might need to make multiple API calls
with slightly varied paging parameters to iteratively collect all the
data you are trying to gather.

Use the following query parameters to paginate through results:

## Parameters

  Name    Description                                                                                                                       Default
  ------- --------------------------------------------------------------------------------------------------------------------------------- ---------
  start   The index of the first item you want results for.                                                                                 0
  count   The number of items you want included on each page of results. There could be fewer items remaining than the value you specify.   10

To paginate through results, begin with a ` start ` value of 0 and a
` count ` value of N. To get the next page, set ` start ` value to N,
while the ` count ` value stays the same. Subsequent pages start at 2N,
3N, 4N, and so on.

## Samples

#### Sample Request

``` lang-https
GET https://api.linkedin.com/v2/{service}
```

#### Sample Response

``` lang-json
"elements": [
    {"Result #0"},
    {"Result #1"},
    {"Result #2"},
    {"Result #3"},
    {"Result #4"},
    {"Result #5"},
    {"Result #6"},
    {"Result #7"},
    {"Result #8"},
    {"Result #9"}
],
"paging": {
    "count": 10,
    "start": 0
}
```

#### Sample Request

``` lang-https
GET https://api.linkedin.com/v2/{service}?start=10&count=10
```

#### Sample Response

``` lang-json
"elements": [
    {"Result #10"},
    {"Result #11"},
    {"Result #12"},
    {"Result #13"},
    {"Result #14"},
    {"Result #15"},
    {"Result #16"},
    {"Result #17"},
    {"Result #18"},
    {"Result #19"}
],
"paging": {
    "count": 10,
    "start": 10
}
```

### End of the Dataset

You have reached the end of the dataset when your response contains
fewer elements in the ` entities ` block of the response than your
` count ` parameter request.
:::
