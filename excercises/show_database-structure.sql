use information_schema; 
show tables;
select concat(col.table_schema, '.', col.table_name) as 'table',
       col.ordinal_position as col_id,
       col.column_name as column_name,
       case when kcu.referenced_table_schema is null
            then null
            else '>-' end as rel,
       concat(kcu.referenced_table_schema, '.', kcu.referenced_table_name)
              as primary_table,
       kcu.referenced_column_name as pk_column_name,
       kcu.constraint_name as fk_constraint_name
from information_schema.columns col
join information_schema.tables tab
     on col.table_schema = tab.table_schema
     and col.table_name = tab.table_name
left join information_schema.key_column_usage kcu
     on col.table_schema = kcu.table_schema
     and col.table_name = kcu.table_name
     and col.column_name = kcu.column_name
     and kcu.referenced_table_schema is not null
where col.table_schema not in('information_schema','sys',
                              'mysql', 'performance_schema')
      and tab.table_type = 'BASE TABLE'
--    and fks.constraint_schema = 'database name'
order by col.table_schema,
         col.table_name,
         col.ordinal_position;
      ;
