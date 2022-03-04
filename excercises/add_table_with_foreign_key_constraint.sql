use db1; create table db1.addresses
(
addresses_id int NOT NULL AUTO_INCREMENT,
addresses_street_one VARCHAR(45) NOT NULL,
addresses_street_two varchar(45) NULL,
addresses_city varchar(45) NOT NULL,
addresses_state varchar(2) NOT NULL,
addresses_postal_code varchar(20) NULL,
addresses_users_id iNT(11) NOT NULL,
PRIMARY KEY (`addresses_id`),
UNIQUE INDEX `addresses_id_UNIQUE` (`addresses_id` ASC),
INDEX `addresses_users_id_idx` (`addresses_users_id` ASC),

CONSTRAINT `addresses_users_id`
FOREIGN KEY (`addresses_users_id`) REFERENCES `db1`.`users` (`users_id`)
ON DELETE CASCADE
ON UPDATE NO ACTION
);

