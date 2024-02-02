::: {._4-u3 ._588p}
**` GET /{ig-media-id}/product_tags `**

Get a collection of product tags on an [IG
Media](/docs/instagram-api/reference/ig-media) . See the [Product
Tagging](/docs/instagram-api/guides/product-tagging) guide for complete
product tagging steps.

### Limitations

-   Instagram Creator accounts are not supported.
-   Stories, Instagram TV, Reels, Live, and Mentions are not supported.

### Requirements

### Request Syntax

``` {._5s-8 .prettyprint .lang-code}
GET https://graph.facebook.com/{api-version}/{ig-media-id}/product_tags
  ?access_token={access-token}
```

### Path Parameters

::: _57-c
Placeholder
:::
:::

Value

` {api-version} `

API [version](/docs/instagram-basic-display-api/overview#versions) .

` {ig-media-id} `

**Required.** IG Media ID.

### Query String Parameters

::: _57-c
Key
:::

Placeholder

Value

` access_token `

` {access-token} `

**Required.** App user\'s
[User](/docs/facebook-login/access-tokens/#usertokens) access token.

### Response

A JSON-formatted object containing an array of product tags on an IG
Media. Responses can include the following product tag fields:

``` {._5s-8 .prettyprint .lang-json}
{
  "data": [
    {
      "product_id": {product-id},
      "merchant_id": {merchant-id},
      "name": "{name}",
      "price_string": "{price-string}",
      "image_url": "{image-url}",
      "review_status": "{review-status}",
      "is_checkout": {is-checkout},
      "stripped_price_string": "{stripped-price-string}",
      "string_sale_price_string": "{string-sale-price-string}",
      "x": {x},
      "y": {y}
    }
  ]
}
```

#### Response Contents

::: _57-c
Property
:::

Value

` product_id `

Product ID.

` merchant_id `

Merchant ID.

` name `

Product name.

` price_string `

Price string.

` image_url `

Product image URL.

` review_status `

Product review status. Values can be:

\

-   ` approved ` --- Product is approved.
-   ` rejected ` --- Product was rejected
-   ` pending ` --- Still undergoing review.
-   ` outdated ` --- Product was approved but has been edited and
    requires reapproval.
-   ` "" ` --- No review status.

` is_checkout `

If ` true ` , product can be purchased directly through the Instagram
app. If ` false ` , product can only be purchased on the merchant\'s
website.

` stripped_price_string `

Product short price string (price displayed in constrained spaces, such
as ` $100 ` instead of ` 100 USD ` ).

` string_sale_price_string `

Product sale price.

` x `

A float that indicates percentage distance from left edge of media
image. Value within ` 0.0 ` -- ` 1.0 ` range.

` y `

A float that indicates percentage distance from top edge of media image.
Value within ` 0.0 ` -- ` 1.0 ` range.

### cURL Example

#### Request

``` {._5s-8 .prettyprint .lang-curl}
curl -i -X GET \ "https://graph.facebook.com/v18.0/90010778325754/product_tags?access_token=EAAOc..."
```

#### Response

``` {._5s-8 .prettyprint .lang-json}
{
  "data": [
    {
      "product_id": 3231775643511089,
      "merchant_id": 90010177253934,
      "name": "Gummy Bears",
      "price_string": "$3.50",
      "image_url": "https://scont...",
      "review_status": "approved",
      "is_checkout": true,
      "stripped_price_string": "$3.50",
      "stripped_sale_price_string": "$3",
      "x": 0.5,
      "y": 0.80000001192093
    }
  ]
}
```
