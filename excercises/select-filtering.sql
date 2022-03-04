USE db1;
--select users_name, users_email from users;
--select * from guides;
--select * from users;
select * 
from addresses
where addresses_id = 3
and addresses_state = 'NY' 
and addresses_city = 'Manhattan';

select addresses_state 
from addresses
where addresses_id = 3
and addresses_state = 'NY' 
and addresses_city = 'Manhattan';

