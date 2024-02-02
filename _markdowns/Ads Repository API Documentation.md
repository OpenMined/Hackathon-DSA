::: {.c82435a4b8 .a178069f51 .d01af75260 .a18aeea94d .eda30a72cc .da798eb4ba}
curl \--location \'https://accommodations.booking.com/dml/graphql\' \\
\--header \'Content-Type: application/json\' \\ \--data \' {
\"query\":\"query SearchAdvertisementRepo(\$input:
SearchAdvertisementRequestInput!) { searchAdvertisement(input: \$input)
{ results_count pages_count items { id ad_name legal_entity date_started
date_last_shown total_views_bucket viewers_per_country { country bucket
} } } }\", \"variables\":{ \"input\":{ \"date_from\":\"2023-09-01\",
\"date_to\":\"2023-09-15\", \"ad_name\": \"ad name\", \"legal_entity\":
\"legal entity name\" } } }\'
:::
