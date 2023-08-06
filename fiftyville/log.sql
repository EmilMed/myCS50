-- Keep a log of any SQL queries you execute as you solve the mystery.

--SEARCH FOR CRIME SCENE EVIDENCE
SELECT description FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28;
--SEARCH FOR WITNESS REPORTS
SELECT transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";
--CHECK BAKERY CAMERAS FOR LICENSE PLATES
SELECT bakery_security_logs.activity, bakery_security_logs.license_plate, people.name FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE bakery_security_logs.year = 2021 AND bakery_security_logs.month = 7 AND bakery_security_logs.day = 28 AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute > 15 AND bakery_security_logs.minute < 25;
--CHECK FOR ATM WITHDRAWALS
SELECT people.name, atm_transactions.transaction_type FROM people JOIN bank_accounts ON bank_accounts.person_id = people.id JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number WHERE atm_transactions.year = 2021 AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND atm_location = "Leggett Street" AND atm_transactions.transaction_type = "withdraw";
--CHECK PHONE CALLS FOR NAMES
SELECT phone_calls.caller, phone_calls.receiver, caller_people.name AS caller_name, receiver_people.name AS receiver_name FROM phone_calls JOIN people AS caller_people ON phone_calls.caller = caller_people.phone_number JOIN people AS receiver_people ON phone_calls.receiver = receiver_people.phone_number WHERE phone_calls.year = 2021 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration < 60;
--CHECK FOR FLIGHTS FROM FIFTYVILLE
SELECT name FROM people



