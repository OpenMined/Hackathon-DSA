[](https://www.booking.com/)

API Documentation

1. [Booking.com](https://booking.com/)
2. Booking Ads Repository
3. API documentation
    

* * *

Booking Ads Repository
======================

API Documentation

See our example below

curl --location 'https://accommodations.booking.com/dml/graphql' \\ --header 'Content-Type: application/json' \\ --data ' { "query":"query SearchAdvertisementRepo($input: SearchAdvertisementRequestInput!) { searchAdvertisement(input: $input) { results\_count pages\_count items { id ad\_name legal\_entity date\_started date\_last\_shown total\_views\_bucket viewers\_per\_country { country bucket } } } }", "variables":{ "input":{ "date\_from":"2023-09-01", "date\_to":"2023-09-15", "ad\_name": "ad name", "legal\_entity": "legal entity name" } } }'