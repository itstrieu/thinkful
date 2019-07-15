1. What's the most expensive listing? What else can you tell me about the listing?

```SQL
WITH top_id
as (
SELECT
	id
FROM
	sfo_listings
ORDER BY price DESC
LIMIT 3
)

SELECT
    	sfo_listings.name,
	sfo_listings.price,
	sfo_listings.room_type,
	sfo_listings.neighbourhood,
	sfo_listings.host_name,
	sfo_reviews.review_date,
	sfo_reviews.comments
FROM
	sfo_reviews
JOIN
	top_id
ON
	sfo_reviews.listing_id = top_id.id
```

Of the top three most expensive listings, one listing is for a private room. Marcel's 8000/night private room in Parkside. Depending on the number of guests each listing can accommodate, Marcel's might well be the most expensive. Marcel also received the most number of reviews--most of which were good. 
   
2. What neighborhoods seem to be the most popular?

```SQL
WITH before_avg
AS(
WITH nbh_count
AS (
SELECT
	neighbourhood,
	COUNT(*) as neighbourhood_count
FROM
	sfo_listings
GROUP BY 1
)

SELECT
	sfo_listings.neighbourhood,
	sfo_listings.reviews_per_month,
	nbh_count.neighbourhood_count
FROM
	nbh_count
JOIN
	sfo_listings
ON
	nbh_count.neighbourhood = sfo_listings.neighbourhood
)

SELECT
	neighbourhood,
	AVG(reviews_per_month),
	neighbourhood_count
FROM
	before_avg
GROUP BY neighbourhood, neighbourhood_count
ORDER BY neighbourhood_count DESC
	
```

Mission had the highest number of listings, but not a high number of average reviews per month. Outer Sunset only had 242 listings compared to Mission's 694, but averaged more than twice Mission's reviews per month count. This might indicate that Outer Sunset booked more guests, while residents in Mission were more likely to host. 
    
3. What time of year is the cheapest time to go to San Francisco? What about the busiest?

```SQL
WITH final_table
AS
(
WITH clean_table
AS 
(
SELECT
EXTRACT
	(MONTH from calender_date)
AS
	listing_month,
REPLACE(REPLACE(REPLACE(price,'$',''),'.00', ''),',','')
AS 
	clean_price
FROM 
	sfo_calendar
)
SELECT
	listing_month,
CAST (clean_price AS int)
FROM
	clean_table
)
SELECT
	listing_month,
	AVG(clean_price)
FROM
	final_table
GROUP BY listing_month
ORDER BY avg ASC
```

January is the cheapest month to go to San Francisco, followed by February and December.

```SQL

WITH listings_table
AS
(
WITH base_table
AS
(
SELECT
	available,
EXTRACT
	(MONTH from calender_date)
AS
	listing_month
FROM
	sfo_calendar
)
SELECT
	COUNT(*) AS total_listings,
	listing_month
FROM
	base_table
WHERE available = 'f' OR available = 't'
GROUP BY listing_month
), 

t_table
AS
(
WITH base_table
AS
(
SELECT
	available,
EXTRACT
	(MONTH from calender_date)
AS
	listing_month
FROM
	sfo_calendar
)
SELECT
	COUNT(*) AS available,
	listing_month
FROM
	base_table
WHERE available = 't'
GROUP BY listing_month
)

SELECT
	listings_table.listing_month,
	listings_table.total_listings,
	t_table.available
FROM
	listings_table
JOIN
	t_table
ON
	listings_table.listing_month = t_table.listing_month
ORDER BY available ASC
```

The busiest month of the year to go to San Francisco is September, followed by October and June.
September and October are also the most expensive months to book Airbnbs in San Francisco.

