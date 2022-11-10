-- This scripts assume postgresql will be used for query engine

with table_1 as (
	select 
		v.country as country,
		case 
			when v.daily_vaccinations = '' then '-1'
			else v.daily_vaccinations
		end::int as daily_vaccinations		
	from dev.vaccination v
),

table_2 as (
	select 
		country as country, 
		PERCENTILE_DISC(0.5) within group(order by daily_vaccinations) as median
	from table_1
	where daily_vaccinations > 0
	group by 1
)

select
	table_2.country,
	coalesce (
		case
			when daily_vaccinations = '' then table_2.median::varchar
			else daily_vaccinations
		end, '0'
	)::int as daily_vaccinations
from dev.vaccination
left join table_2 on dev.vaccination.country = table_2.country

