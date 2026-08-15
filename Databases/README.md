# Databases

## Artifact

For this section, I used the database from my Android event-tracking app from CS-360: Mobile Architecture and Programming.

## Original Artifact

The original database stored user accounts and event information. It allowed users to create accounts, log in, save events, edit events, delete events, and view events in the app.

However, the original database had some problems. Passwords were stored as plain text, events were connected to usernames instead of user IDs, and dates and times were stored separately.

[View Original Artifact](original/)

## Enhanced Artifact

The enhanced database improves security, organization, and performance. I added password hashes and salts, single-use recovery codes, user ID foreign keys, improved date and time storage, database indexes, and a migration process for old data.

These changes make the database safer, more reliable, and easier to maintain.

[View Enhanced Artifact](enhanced/)

## Narrative

The narrative explains what I changed, why I changed it, what skills I used, and how this enhancement connects to the Computer Science program outcomes.

[View Narrative](narrative.md)

## Schema Diagram

The schema diagram shows the relationship between the users table and the events table.

[View Schema Diagram](schema-diagram.md)
