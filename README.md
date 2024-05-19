# Joint Accounts Spending Tracker

This Django application provides a web interface for tracking and displaying per-day spending data across multiple clients. It includes features for displaying spending by date and client, along with remaining budget limits for each day.
The limits set apply to all clients total spending.

## Features

- Display per-day spending for each client within a specified date range.
- Show cumulative limit remainders to track spending against set budgets.
- Manage data and conCertainly! Enclosing the table of environment variables within a markdown code block will make it visually distinct and preserve the formatting when viewed in markdown renderers such as GitHub or Bitbucket. Here's how you can present the table in a markdown code block in your `README.md`:

| Variable            | Description                                                                                     | Example Value                                                        |
|---------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| `DOMAIN_NAME`       | The domain name where the application is hosted.                                                | `myapp.com`                                                          |
| `DJANGO_SECRET_KEY` | A secret key for a particular Django installation. This is used to provide cryptographic signing. | Generate using `python3 -c 'from django.utils.crypto import get_random_string; print(get_random_string(50))'` |
| `DATABASE_URL`      | The URL to configure the connection to the database.                                            | `sqlite:///Users/ryzhakar/projects/monobank-sync-rust/monobase.sqlite` |
| `DJANGO_ENV`        | The environment in which Django is running. This helps in toggling between development and production settings. | `development` or `production`                                                      |

## Note to self
This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [66d7902](https://github.com/wemake-services/wemake-django-template/tree/66d7902094b8a104f83773171c44635314b5244a). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/66d7902094b8a104f83773171c44635314b5244a...master) since then.
Full documentation is available here: [`docs/`](docs).
