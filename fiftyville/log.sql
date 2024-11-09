-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Seek description about CS50 duck and then take id to investigate more
-- Interview mention the bakery, at 10:15am and id scene: 295
SELECT id, description
    FROM crime_scene_reports
    WHERE month = 7
    AND day = 28 AND street = "Humphrey Street";
-- Based on the word "bakery", we find from the interview who mentioned bakery và vào ngày 28
-- There are 3 witnesses: Ruth, Eugene and Raymond
-- Ruth nói tên khoảng thời gian 10 phút khi vụ trộm xảy ra tên trộm đi trốn ra khỏi bằng xe thế nên tìm license_plate của xe rời đi trong 10 phút

-- Eugene nói rằng tên trôm đã đã rút ATM ở Leggett Street

-- Raymond nói rằng tên trộm đã gọi điện cho đồng phạm trong dưới 1 phút sẽ khởi hàng ngày mai vào chuyến sớm nhất và tên đồng phạm đặt vé
SELECT name, transcript
FROM interviews
    WHERE transcript
    LIKE "%bakery%" AND day = 28;

-- Tìm các license_plate của các xe trong khoảng 10 phút lúc xảy ra việc
-- Có 8 xe ra vào trong khoảng 10h15 là: 13FNH73, 5P2BI95, 94KL13X, 6P58WS2, 4328GD8, G412CB7, L93JTIZ, 322W7JE, 0NTHK55
SELECT *
    FROM bakery_security_logs
    WHERE day = 28;
-- Dựa vào Eugene tìm được rằng kẻ trộm rút tiền vào sáng nên tìm số xe của người rút tiền dựa vào tài khoản ngân hàng
-- Thu hẹp còn 4 người: Bruce (94KL13X), Diana (322W7JE), Luca (4328GD8)
SELECT license_plate, name
    FROM people
    WHERE id in
    (SELECT person_id
        FROM bank_accounts
        WHERE account_number IN
            (SELECT account_number
                FROM atm_transactions
                WHERE day = 28 AND year = 2023
                    AND atm_location = "Leggett Street"
                    AND transaction_type = "withdraw"));
-- Số của từng người là Luca ((389) 555-5198), Diana ((770) 555-1861) và Bruce ((367) 555-5533);
-- Dựa vào cuộc gọi thì thấy có 2 người thực hiện trong ngày 28 là Bruce và Diana
-- Đồng phạm có thể là ((375) 555-8161) hoặc ((770) 555-1861)
SELECT * FROM phone_calls
    WHERE day = 28
    AND caller IN
    (SELECT phone_number
        FROM people
        WHERE name = "Bruce" OR name = "Diana")
    AND duration < 60;
-- Đồng phạm có thể là Robin ((375) 555-8161) và Philip ((725) 555-3243)
SELECT name, phone_number
   FROM people
   WHERE phone_number = "(375) 555-8161" OR phone_number = "(725) 555-3243";

-- Tìm sân bay của Fiftyville là Fiftyville Regional Airport, viết tắt là "CSF", có id là 8
SELECT * FROM airports;
-- Có 5 chiếc rời đi ngày đó trong đó id là 18, 23, 36, 43, 53 và destination_airport_id là 6, 11, 4, 1, 9
-- THời gian khởi hành sớm nhất là 8:20 của chuyến có id 36 tới LaGuardia Airport (id là 4)
SELECT * FROM flights WHERE day = 29;

SELECT * FROM passengers
    WHERE flight_id =
    (SELECT id FROM flights WHERE day = 29 AND id = 36);

-- Dò passport của từng thủ phạm
SELECT passport_number
    FROM people
        WHERE name = "Bruce" OR name = "Diana";

-- Dò tên của thủ phạm dựa trên passport của thủ phạm
SELECT name FROM people
WHERE passport_number =
(
    SELECT passport_number FROM passengers
    WHERE passport_number IN
        (SELECT passport_number
        FROM people
            WHERE name = "Bruce" OR name = "Diana")
    AND flight_id =
        (SELECT id FROM flights WHERE day = 29 AND id = 36)
);

-- Hung thủ chỉ có một, đó là: Bruce
-- Vậy đồng phạm là người gọi cho Bruce là: Robin
SELECT name
   FROM people
   WHERE phone_number =
   (
        SELECT receiver FROM phone_calls
            WHERE day = 28
            AND caller IN
            (SELECT phone_number
                FROM people
                WHERE name = "Bruce")
            AND duration < 60
   );
