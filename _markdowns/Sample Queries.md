<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Once you import our query module, you can use it to query the dataset
using your own custom SQL queries. The code sample below shows importing
the query module; specifying the database, table, and API table;
defining a SQL query; and assigning the query to a variable ( ` sql ` ).

::: _4gnb
::: {#u_0_3_Ry ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
library(fbrir)
athena = AthenaFacade$new()

database <- "fbri_prod_atp"
table <- "ad_targeting_dataset_siep_aug_2020"
api_table <- "ad_archive_api"

# Define your own SQL query and assign to variable 'sql' 
sql <- sprintf("SELECT * FROM %s.%s LIMIT 5", database, table)
athena$QueryAthena(sql)
```
:::
:::

The dataframe result from the R example would look similar to this
(blurred intentionally):

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/340536346_1033375467638366_2464203531615002480_n.png?_nc_cat=102&ccb=1-7&_nc_sid=f537c7&_nc_ohc=4tQ44TP1AZ4AX8hf0oB&_nc_ht=scontent-cdg4-1.xx&oh=00_AfCcLfILFYTWzANZHjbx_xWCHrXxNohyq-XHz4x1TAgS2Q&oe=65B4A495){.img
srcset="https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/340536346_1033375467638366_2464203531615002480_n.png?_nc_cat=102&ccb=1-7&_nc_sid=f537c7&_nc_ohc=4tQ44TP1AZ4AX8hf0oB&_nc_ht=scontent-cdg4-1.xx&oh=00_AfCcLfILFYTWzANZHjbx_xWCHrXxNohyq-XHz4x1TAgS2Q&oe=65B4A495"}

The dataframe result from the Python example would look similar to this
(blurred intentionally):

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/340939213_1106319464104036_8410147747585713878_n.png?_nc_cat=109&ccb=1-7&_nc_sid=f537c7&_nc_ohc=UyVVXj09J_kAX9eCMbM&_nc_ht=scontent-cdg4-2.xx&oh=00_AfCwSaO1xo4c2PZriBz-g71jTySyeaTziQybXFlEGG5d0Q&oe=65B57C80){.img
srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/340939213_1106319464104036_8410147747585713878_n.png?_nc_cat=109&ccb=1-7&_nc_sid=f537c7&_nc_ohc=UyVVXj09J_kAX9eCMbM&_nc_ht=scontent-cdg4-2.xx&oh=00_AfCwSaO1xo4c2PZriBz-g71jTySyeaTziQybXFlEGG5d0Q&oe=65B57C80"}

The sample queries in the rest of this section demonstrate the types of
queries you can perform against the dataset. For each example, we show
the SQL first followed by a tabbed codeblock with Python and R so you
can see how the SQL is used to define the ` sql ` variable. To try out a
sample query, copy the R or Python from the codeblock and paste it into
your Jupyter notebook cell. Then run the code.

Dataframe results screenshots have been blurred intentionally. They are
intended only to show the output format you can expect.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
``` {._5s-8 .prettyprint .lang-sql}
SELECT
    archive_id,
    include
FROM {database}.{table}
WHERE
    CARDINALITY(
        FILTER(
            CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))),
            (x) -> ELEMENT_AT(x, 'Joe Biden') = 'Interests'))  > 0
```

::: _4gnb
::: {#u_0_7_YZ ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
sql <- sprintf("SELECT archive_id, include FROM %s.%s WHERE CARDINALITY( FILTER( CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))), (x) -> ELEMENT_AT(x, 'Joe Biden') = 'Interests')) > 0", database, table)
athena$QueryAthena(sql)
```
:::
:::

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/373529801_1708042076348362_3062030183088213612_n.png?_nc_cat=103&ccb=1-7&_nc_sid=f537c7&_nc_ohc=_RM0tjX2x4kAX9d0n30&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDoS05NdQ3JHsTjNY8n3HOZcWMIFlskd9L0n-lxqyBz7Q&oe=65B43573){.img
srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/373529801_1708042076348362_3062030183088213612_n.png?_nc_cat=103&ccb=1-7&_nc_sid=f537c7&_nc_ohc=_RM0tjX2x4kAX9d0n30&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDoS05NdQ3JHsTjNY8n3HOZcWMIFlskd9L0n-lxqyBz7Q&oe=65B43573"}
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
``` {._5s-8 .prettyprint .lang-sql}
WITH education_table AS (
    SELECT
        REDUCE(
            CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))),
            MAP(),
            (s, x) -> (
                    MAP_CONCAT(s, MAP_FILTER(x, (k, v) -> v = 'Education level'))
                ),
            s -> s
        ) AS education_levels
    FROM {database}.{table}
)
SELECT
    education_levels,
    COUNT(*) AS count
FROM education_table
GROUP BY
    education_levels;
ORDER BY
    -count; 
```

::: _4gnb
::: {#u_0_b_S+ ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
sql <- sprintf("WITH education_table AS ( SELECT REDUCE( CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))), MAP(), (s, x) -> (MAP_CONCAT(s, MAP_FILTER(x, (k, v) -> v = 'Education level'))), s -> s) AS education_levels FROM %s.%s) SELECT education_levels, COUNT(*) AS count FROM education_table GROUP BY education_levels ORDER BY -count;", database, table)        
athena$QueryAthena(sql)
```
:::
:::

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/373011465_817368689942835_6198596206217206031_n.png?_nc_cat=100&ccb=1-7&_nc_sid=f537c7&_nc_ohc=jn0dcpvfZ_EAX9AzZ9Z&_nc_oc=AQlWk-UBRuoLyQWNt5D4XDw8C29TTUoZVx147WNHQFiwie0u66M24iqQpj1Cjg1aFGM&_nc_ht=scontent-cdg4-2.xx&oh=00_AfCbBTUtOlHFbLrQbFpNqOzAvX2pXBZxitD9-zkbFEtn9A&oe=65B43EBC){.img
srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/373011465_817368689942835_6198596206217206031_n.png?_nc_cat=100&ccb=1-7&_nc_sid=f537c7&_nc_ohc=jn0dcpvfZ_EAX9AzZ9Z&_nc_oc=AQlWk-UBRuoLyQWNt5D4XDw8C29TTUoZVx147WNHQFiwie0u66M24iqQpj1Cjg1aFGM&_nc_ht=scontent-cdg4-2.xx&oh=00_AfCbBTUtOlHFbLrQbFpNqOzAvX2pXBZxitD9-zkbFEtn9A&oe=65B43EBC"}
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
``` {._5s-8 .prettyprint .lang-sql}
SELECT
    exclusion,
    exclusion_type,
    COUNT(*)
FROM {database}.{table}
CROSS JOIN UNNEST(CAST(JSON_EXTRACT(exclude, '$') AS MAP(VARCHAR, VARCHAR))) AS t (
        exclusion,
        exclusion_type
    )
GROUP BY
    exclusion,
    exclusion_type;
```

::: _4gnb
::: {#u_0_f_Cp ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
sql <- sprintf("SELECT exclusion, exclusion_type, COUNT(*) FROM %s.%s CROSS JOIN  UNNEST(CAST(JSON_EXTRACT(exclude, '$') AS MAP(VARCHAR, VARCHAR))) AS t (exclusion, exclusion_type) GROUP BY exclusion, exclusion_type;", database, table)
athena$QueryAthena(sql)
```
:::
:::

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/371115383_2314557848747524_798596474071297563_n.png?_nc_cat=101&ccb=1-7&_nc_sid=f537c7&_nc_ohc=9txNk01ueKMAX-VLT1T&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDliDQQshQYuBXrLe3XJqvaVfd-PuLpja7-UR-FNozwGg&oe=65B4449F){.img
srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/371115383_2314557848747524_798596474071297563_n.png?_nc_cat=101&ccb=1-7&_nc_sid=f537c7&_nc_ohc=9txNk01ueKMAX-VLT1T&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDliDQQshQYuBXrLe3XJqvaVfd-PuLpja7-UR-FNozwGg&oe=65B4449F"}
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
In this query, we use the Ad Library data table ( ` ad_archive_api ` )
to combine targeting data with delivery data.

``` {._5s-8 .prettyprint .lang-sql}
SELECT
    a.*
FROM {database}.{table} AS a,
    {database}.{api_table} AS b
WHERE
    a.ds = b.ds
    AND a.archive_id = b.fbid
    AND b.reached_countries LIKE '%US%';
      
```

### Python and SQL

::: _4gnb
::: {#u_0_j_96 ._4gnf ._4fa6}
``` {.prettyprint .lang-r}
sql <- sprintf("SELECT a.* FROM %s.%s AS a, %s.%s AS b WHERE a.ds = b.ds AND a.archive_id = b.fbid AND b.reached_countries LIKE '%%US%%';", database, table, database, api_table)
athena$QueryAthena(sql)
```
:::
:::

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/373003906_846213867105017_101059097494938799_n.png?_nc_cat=104&ccb=1-7&_nc_sid=f537c7&_nc_ohc=NZN1Q0AbWZIAX9eeOhR&_nc_ht=scontent-cdg4-3.xx&oh=00_AfAprBnW1YCW-dETiIoarNzCJbGUhKDjFSxl_A3ty6OMxw&oe=65B52917){.img
srcset="https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/373003906_846213867105017_101059097494938799_n.png?_nc_cat=104&ccb=1-7&_nc_sid=f537c7&_nc_ohc=NZN1Q0AbWZIAX9eeOhR&_nc_ht=scontent-cdg4-3.xx&oh=00_AfAprBnW1YCW-dETiIoarNzCJbGUhKDjFSxl_A3ty6OMxw&oe=65B52917"}
:::
:::

</div>

</div>
