# Database Class Examples

Some basic examples for interacting with Elasticsearch, Postgres, and Redis.

Example code assumes you have those three databases running and have a
functional python environment.

If you'd like some help along those lines, you can use
[Rho AI's Public Python-Dev Repo](https://github.com/rhoai/python-dev)
(image available at [rhoai/python-dev]())

## Usage

Assuming you're taking the python-dev approach:

1. `cd /path/to/python-dev`
1. `docker-compose up -d`  # Starts up databases in the background
1. `docker run -it --rm --net python-dev_default -v /path/to/MECEE4520/databases:/code rhoai/python-dev:v0.1.0`

Once inside that container, you can run your code like normal. e.g.:

    python ./code/ex_postgres.py

The image also has the basic db utilities you'd likely want to play with, for
example:

    psql -h postgres -U postgres -d postgres_db

will get you into the psql shell (with password `postgres`...)

And

    redis-cli -h redis

well let you play with redis!

All of the databases are accessible from their names as specified in the
`docker-compose.yml` file (e.g. `curl elasticsearch:9200`)

### Wrapping up

When you're done, you can

* `ctrl+c` to exit the python-dev container
* `docker-compose stop` to stop databases
* `docker-compose rm` to remove stopped database containers
