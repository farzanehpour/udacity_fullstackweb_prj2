-- Table definitions for the tournament project.
--
-- This schema file created by Shiva Farzanehpour(farzanehpour@gmail.com)
-- for Udacity full stack web development, 2nd project.
--

drop database if exists tournament;
create database tournament;
\c tournament;

--------
--tables
--------

-- table tournament; we can have multiple tournaments runnung at same time.
-- columns:
--		id: primary key, tournament id.
--		name: tournament's name.
create table tournaments (
		id 		serial primary key not null, 
		name 	text
);

--table player; keeps Players' data
-- columns : 
--		id : player_id, Primary key.
--		fk_tournament: tournament id, foriegn key. See tournament table.
-- 		name : Player's name.
create sequence players_id_seq;
create table players (
		id integer primary key not null, 
		fk_tournament serial references tournaments(id),
		name text
);
alter sequence players_id_seq owned by players.id;

-- table matches: keeps match records between players.
-- columns:
--		id : primary key, the match id.
--		fk_player1: first player in the match. 
--					Foriegn key to table players->id.
--		fk_player2: Second player in the match. 
--					Foriegn key to table players->id.
--constraint(s): the pair of player1 and player2 is not allowed to be duplicated.
create table matches (
		id 			serial	primary key not null, 
		fk_player1 	integer	references players(id),
		fk_player2 	integer	references players(id),
		fk_winner 	integer references players(id)
);
alter table matches add constraint unique_match unique (fk_player1, fk_player2);


-- by default, we register one tournament when db is created to cover basic tests
insert into tournaments (id, name) values (1, 'default tournament');

-------
--views
-------

--totalwins view
-- keeps total win of each players.
-- columns:
-- 		players.id
--		players.name
--		totalwin
create or replace view totalwins as
select players.id as id, players.name, count(matches.fk_winner) as totalwin from players
left join matches on matches.fk_winner = players.id group by players.id order by totalwin desc;

-- matchrecords view
--keeps list of total number of matches for all players in descending order 
create or replace view matchrecords as 
select distinct players.id as id, players.name, count(matches.fk_player1+ matches.fk_player2) as records from players
left join matches on (matches.fk_player1 = players.id or matches.fk_player2 = players.id) group by players.id order by records desc;

--reportmatches view
--gives id, name, number of wins and number of matches for all players in descending --ordered list
create or replace view reportmatches as
select totalwins.id, totalwins.name, totalwins.totalwin, matchrecords.records from totalwins
inner join matchrecords
on totalwins.id = matchrecords.id order by totalwins.totalwin desc;

