/* Note: You also need to enable user login via pg_hba.conf or pgAdmin */

create database metrics;
create role metrics_user;
alter role metrics_user with password 'noprod';
grant all on database metrics to metrics_user;

\c metrics
create table class_metrics (
	id serial primary key not null,
	label text not null,
	label_count integer not null
);

grant all on class_metrics to metrics_user;
grant all on class_metrics_id_seq to metrics_user;