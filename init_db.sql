CREATE DATABASE geography_db;
CREATE USER geo_admin WITH PASSWORD 'geo_pass';
GRANT ALL PRIVILEGES ON DATABASE geography_db TO geo_admin;
\c geography_db;
CREATE EXTENSION IF NOT EXISTS pg_trgm;