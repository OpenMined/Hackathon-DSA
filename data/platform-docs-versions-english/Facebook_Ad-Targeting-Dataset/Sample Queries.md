Sample queries
==============

Once you import our query module, you can use it to query the dataset using your own custom SQL queries. The code sample below shows importing the query module; specifying the database, table, and API table; defining a SQL query; and assigning the query to a variable (`sql`).

RPython

    library(fbrir)
    athena = AthenaFacade$new()
    
    database <- "fbri_prod_atp"
    table <- "ad_targeting_dataset_siep_aug_2020"
    api_table <- "ad_archive_api"
    
    # Define your own SQL query and assign to variable 'sql' 
    sql <- sprintf("SELECT * FROM %s.%s LIMIT 5", database, table)
    athena$QueryAthena(sql)

    from fbri.private.sql.query import execute
    
    database = "fbri_prod_atp"
    table = "ad_targeting_dataset_siep_aug_2020"
    api_table = "ad_archive_api"
    
    # Define your own SQL query and assign to variable 'sql' 
    sql = f"SELECT * FROM {database}.{table} LIMIT 5"
    
    execute(sql)

The dataframe result from the R example would look similar to this (blurred intentionally):

  
  

The dataframe result from the Python example would look similar to this (blurred intentionally):

  
  

The sample queries in the rest of this section demonstrate the types of queries you can perform against the dataset. For each example, we show the SQL first followed by a tabbed codeblock with Python and R so you can see how the SQL is used to define the `sql` variable. To try out a sample query, copy the R or Python from the codeblock and paste it into your Jupyter notebook cell. Then run the code.

Dataframe results screenshots have been blurred intentionally. They are intended only to show the output format you can expect.

Get data on ad targeting by user interest
-----------------------------------------

### SQL query

SELECT
    archive\_id,
    include
FROM {database}.{table}
WHERE
    CARDINALITY(
        FILTER(
            CAST(JSON\_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))),
            (x) -> ELEMENT\_AT(x, 'Joe Biden') = 'Interests'))  > 0

### Python and R

RPython

    sql <- sprintf("SELECT archive_id, include FROM %s.%s WHERE CARDINALITY( FILTER( CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))), (x) -> ELEMENT_AT(x, 'Joe Biden') = 'Interests')) > 0", database, table)
    athena$QueryAthena(sql)

    sql = f"SELECT archive_id, include FROM {database}.{table} WHERE CARDINALITY( FILTER( CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))), (x) -> ELEMENT_AT(x, 'Joe Biden') = 'Interests')) > 0"
    execute(sql)

### Dataframe result

Get data and number of ads targeting by education levels
--------------------------------------------------------

### SQL query

WITH education\_table AS (
    SELECT
        REDUCE(
            CAST(JSON\_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))),
            MAP(),
            (s, x) -> (
                    MAP\_CONCAT(s, MAP\_FILTER(x, (k, v) -> v = 'Education level'))
                ),
            s -> s
        ) AS education\_levels
    FROM {database}.{table}
)
SELECT
    education\_levels,
    COUNT(\*) AS count
FROM education\_table
GROUP BY
    education\_levels;
ORDER BY
    -count; 

### Python and R

RPython

    sql <- sprintf("WITH education_table AS ( SELECT REDUCE( CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))), MAP(), (s, x) -> (MAP_CONCAT(s, MAP_FILTER(x, (k, v) -> v = 'Education level'))), s -> s) AS education_levels FROM %s.%s) SELECT education_levels, COUNT(*) AS count FROM education_table GROUP BY education_levels ORDER BY -count;", database, table)        
    athena$QueryAthena(sql)

    sql = f"WITH education_table AS ( SELECT REDUCE( CAST(JSON_EXTRACT(include, '$') AS ARRAY(MAP(VARCHAR, VARCHAR))), MAP(), (s, x) -> (MAP_CONCAT(s, MAP_FILTER(x, (k, v) -> v = 'Education level'))), s -> s) AS education_levels FROM {database}.{table}) SELECT education_levels, COUNT(*) AS count FROM education_table GROUP BY education_levels ORDER BY -count;"
    execute(sql)

### Dataframe result

Get data and count of ads targeting by non-interest
---------------------------------------------------

### SQL query

SELECT
    exclusion,
    exclusion\_type,
    COUNT(\*)
FROM {database}.{table}
CROSS JOIN UNNEST(CAST(JSON\_EXTRACT(exclude, '$') AS MAP(VARCHAR, VARCHAR))) AS t (
        exclusion,
        exclusion\_type
    )
GROUP BY
    exclusion,
    exclusion\_type;

### Python and R

RPython

    sql <- sprintf("SELECT exclusion, exclusion_type, COUNT(*) FROM %s.%s CROSS JOIN  UNNEST(CAST(JSON_EXTRACT(exclude, '$') AS MAP(VARCHAR, VARCHAR))) AS t (exclusion, exclusion_type) GROUP BY exclusion, exclusion_type;", database, table)
    athena$QueryAthena(sql)

    sql =f"SELECT exclusion, exclusion_type, COUNT(*) FROM {database}.{table} CROSS JOIN UNNEST(CAST(JSON_EXTRACT(exclude, '$') AS MAP(VARCHAR, VARCHAR))) AS t (exclusion, exclusion_type) GROUP BY exclusion, exclusion_type;"
    execute(sql)

### Dataframe result

Get data on ad targeting by specific country
--------------------------------------------

### SQL query

In this query, we use the Ad Library data table (`ad_archive_api`) to combine targeting data with delivery data.

SELECT
    a.\*
FROM {database}.{table} AS a,
    {database}.{api\_table} AS b
WHERE
    a.ds = b.ds
    AND a.archive\_id = b.fbid
    AND b.reached\_countries LIKE '%US%';
      

### Python and SQL

RPython

    sql <- sprintf("SELECT a.* FROM %s.%s AS a, %s.%s AS b WHERE a.ds = b.ds AND a.archive_id = b.fbid AND b.reached_countries LIKE '%%US%%';", database, table, database, api_table)
    athena$QueryAthena(sql)

    sql = f"SELECT a.* FROM {database}.{table} AS a, {database}.{api_table} AS b WHERE a.ds = b.ds AND a.archive_id = b.fbid AND b.reached_countries LIKE '%US%';"
    execute(sql)

### Dataframe result