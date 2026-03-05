# SQL - Introduction

This project covers the basics of SQL and MySQL:

- What is a database and a relational database
- What SQL stands for (Structured Query Language)
- How to create, alter, and delete databases and tables
- How to SELECT, INSERT, UPDATE, and DELETE data
- How to use subqueries and MySQL functions

## Environment

- Ubuntu 22.04 LTS
- MySQL 8.0

## Usage

```bash
cat <filename>.sql | mysql -hlocalhost -uroot -p
```

## Files

| File | Description |
|------|-------------|
| `0-list_databases.sql` | Lists all databases |
| `1-create_database_if_missing.sql` | Creates database `hbtn_0c_0` |
| `2-remove_database.sql` | Deletes database `hbtn_0c_0` |
| `3-list_tables.sql` | Lists all tables in a database |
| `4-first_table.sql` | Creates table `first_table` |
| `5-full_table.sql` | Prints full description of `first_table` |
| `6-list_values.sql` | Lists all rows of `first_table` |
| `7-insert_value.sql` | Inserts a new row in `first_table` |
| `8-count_89.sql` | Counts records with `id = 89` |
| `9-full_creation.sql` | Creates and fills `second_table` |
| `10-top_score.sql` | Lists all records ordered by score |
| `11-best_score.sql` | Lists records with score >= 10 |
| `12-no_cheating.sql` | Updates Bob's score |
| `13-change_class.sql` | Removes records with score <= 5 |
| `14-average.sql` | Computes average score |
| `15-groups.sql` | Lists number of records per score |
| `16-no_link.sql` | Lists records with a name value |

## Author

Victor
