# Joint Accounts Spending Tracker

A reporting tool for joined budgeting for monobank.ua clients.
Doesn't make any web requests, only operates on data available.
Meant as a companion app for [monobank-sync](https://github.com/ryzhakar/monobank-sync) tool, which handles data download for it.
That said, you're free to use any data source you want.

## Features

- Display per-day spending for each client within a specified date range.
- Show cumulative limit remainders to track spending against set budgets.
- Manage data and budget configs in admin view.

## Requirements
Set these in config/.env:
| Variable            | Description                                                                                     | Example Value                                                        |
|---------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| `DOMAIN_NAME`       | The domain name where the application is hosted.                                                | `myapp.com`                                                          |
| `DJANGO_SECRET_KEY` | A secret key for a particular Django installation. This is used to provide cryptographic signing. | Generate using `python3 -c 'from django.utils.crypto import get_random_string; print(get_random_string(50))'` |
| `DATABASE_URL`      | The URL to configure the connection to the database.                                            | `sqlite:///Users/ryzhakar/projects/monobank-sync-rust/monobase.sqlite` |
| `DJANGO_ENV`        | The environment in which Django is running. This helps in toggling between development and production settings. | `development` or `production`                                                      |

Create an admin user to access the admin view:
```sh
python3 manage.py createsuperuser
```

Obviously, have an SQLite db file ready at the path you specified.

## How to run
Google it. It's a simple django app.

## Note to self
This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [66d7902](https://github.com/wemake-services/wemake-django-template/tree/66d7902094b8a104f83773171c44635314b5244a). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/66d7902094b8a104f83773171c44635314b5244a...master) since then.
Full documentation is available here: [`docs/`](docs).
