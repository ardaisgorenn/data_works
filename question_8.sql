CREATE TEMPORARY TABLE t1 (
	Device_Type varchar,
	Stats_Acces_Link varchar
)

insert into t1 (Device_Type, Stats_Acces_Link)
values('YRT326', '<url>https://ret323_TRu.crown.com</url>')
values('TRU151', '<url>http://tXh67.dia_meter.com</url>')
values('AXO145', '<url>https://xcd32112.smart_meter.com</url>')

select 
	*, 
	regexp_replace(Stats_Acces_Link, 'http(s)?(:)?(\/\/)?|(\/\/)?(www\.)?<*[A-z]*>|</', '', 'g') 
from t1