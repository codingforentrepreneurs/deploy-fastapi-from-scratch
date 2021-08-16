```
APP_DB="fast"

APP_DB_USER="fastuser"

APP_DB_PASSWORD="uLEZ-9bFAT0xDMIx2LnMj8ZelT6johrh7iX4E-zazQo"
```

```
psql --command="CREATE DATABASE ${APP_DB};"
psql --command="CREATE USER ${APP_DB_USER} WITH PASSWORD '${APP_DB_PASSWORD}';"
psql --command="ALTER ROLE ${APP_DB_USER} SET client_encoding TO 'utf8';"
psql --command="ALTER ROLE ${APP_DB_USER} SET default_transaction_isolation TO 'read committed';"
psql --command="ALTER ROLE ${APP_DB_USER} SET timezone TO 'UTC';"
psql --command="GRANT ALL PRIVILEGES ON DATABASE ${APP_DB} to ${APP_DB_USER};"
```


```
psql -Atx postgresql://fastuser:uLEZ-9bFAT0xDMIx2LnMj8ZelT6johrh7iX4E-zazQo@50.116.0.232/fast
```
> `psql -Atx postgresql://<dbuser>:<dbpw>@<ipadd>/<db>`