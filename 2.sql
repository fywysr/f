create table if not exists Users(
	user_id int primary key,
	suername varchar(10),
	password varchar(10)
);
	
create table if not exists Page(
	page_id int primary key,
	page_name
);
	
create table if not exist Permission(
	user_id int,
	page_id int,
	can_create int,
	can_read int,
	can_update int,
	can_delete int,
	constraint User_fk foreign key(user_id) references Users(user_id),
	constraint Page_fk foreign key(page_id) references Users(page_id)
);