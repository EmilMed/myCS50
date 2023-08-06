-- Keep a log of any SQL queries you execute as you solve the mystery.

--SEARCH FOR CRIME SCENE EVIDENCE
SELECT description FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28;
--SEARCH FOR WITNESS REPORTS
SELECT transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";
--CHECK BAKERY CAMERAS FOR LICENSE PLATES
SELECT bakery_security_logs.activity, bakery_security_logs.license_plate, people.name FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE bakery_security_logs.year = 2021 AND bakery_security_logs.month = 7 AND bakery_security_logs.day = 28 AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute > 15 AND bakery_security_logs.minute < 25;
--