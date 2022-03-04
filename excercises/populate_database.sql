USE db1;

INSERT INTO users(users_name, users_email)
VALUES ("Kristine", 'kristine@test.com');

INSERT INTO users(users_name, users_email)
VALUES ("Tiffany", 'tiffany@test.com');

INSERT INTO users(users_name, users_email)
VALUES ("Jordan", 'jordan@test.com');

INSERT INTO addresses(addresses_street_one, addresses_street_two, addresses_city, addresses_state, addresses_postal_code, addresses_users_id)
VALUES ("123 Any Street", "", 'Manhattan', 'NY', '53853', 1);

INSERT INTO addresses(addresses_street_one, addresses_street_two, addresses_city, addresses_state, addresses_postal_code, addresses_users_id)
VALUES ("456 Any Street", "Suite 333", 'Phoenix', 'AZ', '84632', 1);

INSERT INTO addresses(addresses_street_one, addresses_street_two, addresses_city, addresses_state, addresses_postal_code, addresses_users_id)
VALUES ("123 Any Street", "", 'Manhattan', 'NY', '53853', 2);

INSERT INTO addresses(addresses_street_one, addresses_street_two, addresses_city, addresses_state, addresses_postal_code, addresses_users_id)
VALUES ("123 Any Street", "", 'Queens', 'NY', '53853', 3);

INSERT INTO guides(guides_title, guides_users_id, guides_revenue)
VALUES ("My Blog", 1, 500);

INSERT INTO guides(guides_title, guides_users_id, guides_revenue)
VALUES ("Another Post", 2, 1500);

INSERT INTO guides(guides_title, guides_users_id, guides_revenue)
VALUES ("My Great Post", 2, 750);
