DROP TABLE if exists user;
DROP TABLE if exists post;

Create table user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username text unique not null ,
    password text not null
);

Create Table post(
    id integer primary key AUTOINCREMENT,
    author_id INTEGER not null,
    created timestamp not null default current_timestamp,
    title text not null,
    body text not null
);
