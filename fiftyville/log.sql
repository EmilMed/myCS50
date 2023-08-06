-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28;

SELECT transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";

SELECT id, name, license_plate FROM poeple JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate