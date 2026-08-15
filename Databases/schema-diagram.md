# Schema Diagram

This schema diagram shows the relationship between the `users` table and the `events` table in the enhanced database.

```text
users
-----
id                          PRIMARY KEY
username                    TEXT
email                       TEXT
password_hash               TEXT
password_salt               TEXT
recovery_code_hash          TEXT
recovery_code_expires       TEXT

        1
        |
        | user_id
        |
        many

events
------
id                          PRIMARY KEY
user_id                     FOREIGN KEY
title                       TEXT
category                    TEXT
event_datetime              TEXT
is_completed                INTEGER
