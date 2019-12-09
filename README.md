# Flyway Database Migrations

This is a really simply demo of how keeping migration files alongside your app 
can be a manageable way of working with databases using flywheel.

To demo, `docker-compose up` the project, visit the website at `http://localhost:5000`
and look at the main page. 

Navigate back to your Jetbrains IDE and click VCS > Apply Patch and view the differences.
Then affect the change, bring the project up again, and see everything working harmoniously.

## Things this does not demo at the moment

* Flyways ability to undo transactions
* The repair functionality if you alter migrations
* The ability to have replaceable migration stages (Ran on every change, good for updating views, stored procedures,
bulk data inserts)

## Upsides

* Available in Docker for CI integration
* Supports many versions of databases
* Moving to it is easy, first migration is a snapshot of prod. Most tools support exporting the create statement,
read more [here](https://flywaydb.org/documentation/existing)

## Downsides

* Cant be triggered in a code-first / dynamic manner except in Java (This does not affect .sql file based migrations)
* Somewhat limited without licenses, no 5.1 -> 5.6 MySql support, no dry-rus, no undo (A real shame)