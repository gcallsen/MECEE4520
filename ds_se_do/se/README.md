# Software Engineer (SE)

From our lecture slides, The "Software Engineer" cares about:

* Consistent Execution
* Maintainable Code
* _Functional Code_

This is a short demonstration showing one exercise a software engineer
might go through when attempting to take the "data scientist" code and
make it more repeatable and functional in a production environment.

## Usage

This exercise requires that you build your own `docker image` locally.

### Initial Setup

In your shell, type the following:

    cd /path/to/MECEE4520/ds_se_do/se
    ./build-image.sh

### Run Examples

You will now have a functional `docker image` that includes this course
example code along with the `predict.sh` script. This example will
demonstrate how to modify the execution behavior of some code in
production using _environment variables_.

    cd /path/to/MECEE4520/ds_se_do/se
    docker-compose up

When done, `ctrl+c` and `docker-compose rm`
