/*
This file is used to bootstrap development database locally.

Note: ONLY development database;
*/

CREATE USER "monoreport-django" SUPERUSER;
CREATE DATABASE "monoreport-django" OWNER "monoreport-django" ENCODING 'utf-8';
