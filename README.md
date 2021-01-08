# App Description

This is an app that helps promote positivity via blog, videos, and articles.

## Related Links

### Live Site

https://melsimpson1023.github.io/front-project-sunshine

### Restful API

https://django-deploy-sunshine.herokuapp.com/

## Installation
1. Fork and clone this repo.
2. Switch to the new directory in terminala
3. Create and checkout to a new branch.
4. Run `pipenv shell` to step into the python virtual environment.
5. Run `pipenv install` to install dependencies.
6. Create a psql database on your local machine for your testing
    1. Edit `settings.sql` then run `psql -U postgres -f settings.sql`
    OR:
    1. Type `psql` to get into interactive shell.
    2. Run `CREATE DATABASE "project_db_name";` where `project_db_name` is the name you want for your database.
7. Add the database name to the `.env` file using the key `DB_NAME_DEV`.
8. Generate a secret key using [this tool](https://djecrety.ir) and add it to the `.env` file using the key `SECRET`.

## Commands

Commands are run with the syntax `python3 manage.py <command>`:

| command | action |
|---------|--------|
| `runserver`  |  Run the server |
| `makemigrations`  | Generate migration files based on changes to models  |
| `migrate`  | Run migration files to migrate changes to db  |
| `startapp`  | Create a new app  |

## About

Lux is a site created to spread positivity. There is a blog we can all use. I hope you find the inspriation you have been looked for.

## User Stories

1. I want my user to be able to sign-up.
2. I want my user to sign-in.
3. I want my signed-in user to be able to change password.
4. I want my signed-in user to be able to sign-out.
5. I want my signed-in user to be able to see all blog posts.
6. I want my signed-in user to be able to create, update, delete, and show only their blog post.
7. I want my signed-in user to be able to view the videos.
8. I want my signed-in user to be able to view the articles.
9. I want my signed-in user to be able to logout.
