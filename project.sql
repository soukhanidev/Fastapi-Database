use gomrok;
////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE select_product(
    pid int 
)
begin
select * from product
where id = pid ;
end //
delimiter ;
////////////////////////////////////////////////////
call s_product();



use gomrok;
//////////////////////////////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE insert_product(
	IN pid int,
    IN pname varchar(20),
    IN ptype varchar(20),
    IN pyear int
)
begin
insert into product( id,p_name,p_type,p_year) values (pid,pname,ptype,pyear);
end //
delimiter ;
/////////////////////////////////////////////////////////////////////////////////
call insert_product(2,"Tablet","Digital",2018);

call s_product(12,asus,laptop,2013);

select * from product;



CREATE TABLE product(
 id int not null,
 p_name varchar(20),
 p_type varchar(20),
 p_year int,
 PRIMARY KEY (id)
 );
drop table product;
drop procedure insert_product;

delimiter //
CREATE PROCEDURE select_product(
	IN pid int,
    IN pname varchar(20),
    IN ptype varchar(20),
    IN pyear int
)
begin
insert into product( id,p_name,p_type,p_year) values (pid,pname,ptype,pyear);
end //
delimiter ;
delimiter //
CREATE PROCEDURE select_product(
		state int,
		pname VARCHAR(50),
        pid int,
        ptype VARCHAR(50)
)

BEGIN

	IF @state=1
	    BEGIN
			SELECT id,p_name,p_type,p_year
					FROM product
					WHERE p_name = pname
		END
	IF state==2
		BEGIN
			SELECT id,p_name,p_type,p_year
				FROM product
				WHERE id = pid;
		END
	IF state==3
		BEGIN
			SELECT id,p_name,p_type,p_year
			FROM product
			WHERE p_type = ptype;
		END
		
END //
delimiter ;




CREATE PROCEDURE select_product(
		state int,
		pname VARCHAR(50),
        pid int,
        ptype VARCHAR(50)
)
begin 
	if @state=1
    begin
			SELECT id,p_name,p_type,p_year
			FROM product
			WHERE p_type = ptype
    end
end

//////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE update_product(
   IN pid int ,
   IN pyear int
)
begin
UPDATE product
SET
p_year = pyear where id = pid ;
end //
delimiter ;
///////////////////////////////////////////////////////////
delimiter//
CREATE PROCEDURE delete_product(
	IN pid int

)
BEGIN
DELETE FROM product
WHERE id=pid;
END //
delimiter ;
/////////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE insert_transport(
	IN tid int,
    IN ttype varchar(20)

)
begin
insert into transport( id,p_type) values (tid,ttype);
end //
delimiter ;
///////////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE select_transport(
    vid int 
)
begin
select * from transport
where veichle_id = vid ;
end //
delimiter ;
/////////////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE delete_transport(
	IN vid int

)
BEGIN
DELETE FROM transport
WHERE veichle_id=vid;
END //
delimiter ;
///////////////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE delete_customer(
	IN cid int

)
BEGIN
DELETE FROM customer
WHERE id=cid;
END //
delimiter ;
///////////////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE delete_store(
	IN sid int

)
BEGIN
DELETE FROM store
WHERE stored_id=sid;
END //
delimiter ;
///////////////////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE insert_customer(
	IN id int,
    IN fname varchar(20),
    IN lname varchar(20),
    IN age int
)
begin
insert into customer( id,first_name,last_name,age) values (id,fname,lname,age);
end //
delimiter ;
////////////////////////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE insert_store(
	IN sid int,
    IN stype varchar(20),
    IN capacity int
)
begin
insert into store( store_id,store_type,store_capacity) values (sid,stype,capacity);
end //
delimiter ;
////////////////////////////////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE select_customer(
    cid int 
)
begin
select * from customer
where id = cid ;
end //
delimiter ;
//////////////////////////////////////////////////////////////////////////////////
delimiter //
CREATE PROCEDURE select_customer(
    cid int 
)
begin
select * from customer
where id = cid ;
end //
delimiter ;
///////////////////////////////////////////////////////////////////////////////////