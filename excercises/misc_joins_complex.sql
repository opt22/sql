use db1; 
SELECT 
  u.users_email AS 'Email',
  COALESCE(g.guide_count, 0) AS guide_count,
  COALESCE(a.address_count, 0) AS address_count
FROM users u
  LEFT JOIN (
  select count(*) AS guide_count, guides_users_id
  FROM guides
  GROUP BY guides_users_id
  ) AS g
  ON g.guides_users_id = u.users_id
  LEFT JOIN (
    select count(*) AS address_count, addresses_users_id
  from addresses
  GROUP BY addresses_users_id
  ) AS a
  on  a.addresses_users_id = u.users_id
  ORDER BY address_count DESC
  limit 10;
