CREATE DATABASE indotel;

USE indotel;

CREATE TABLE indotel (
    id smallint unsigned not null auto_increment,
    prestadora varchar(50) not null,
    tipo varchar(50) not null,
    npa smallint unsigned not null,
    nxx smallint unsigned not null,
    primary key (id)
);
