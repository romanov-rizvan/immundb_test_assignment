# ImmuneDB Test Assignment

## How to download project

```
git clone https://github.com/romanov-rizvan/immundb.git
```

## How to run tests via docker-compose
```
cd immunedb
docker-compose up --build
```

## Stop the docker-compose after the tests
```
docker-compose down
```

# Structure of project
## /src/
The "src" directory contains base methods, configuration file, json schemas for collection and payloads and enum with
error message
## /tests/
The "tests" directory contains 2 positive and 1 negative tests.\
These tests have precondition that create collection from json schema: src/schemas/collection_schema.json.\
Check that response code is equal to 200, otherwise drop assertion with error message. \
This collection named "Transaction" and have specified fields: 
```
account_number(unique), account_name, iban, address, amount, type (sending, receiving).
```
After the tests are completed, the Transaction collection is deleted.\
Check that response code is equal to 200, otherwise drop assertion with error message
### test_0_positive::test_put_transaction
This test send the document with one transaction into empty collection with random values (used faker lib):
```
    "account_number": fake.pyint(10000, 99999),
    "account_name": fake.name(),
    "iban": fake.iban(),
    "address": fake.address().replace("\n", ", "),
    "amount": fake.pyint(0, 9999),
    "type": get_random_type(fake.pybool())
```
Check that response code is equal to 200, otherwise drop assertion with error message
### test_0_positive::test_put_several_transactions
This test send the document with 110 transactions in one execution into collection from with random values 
(used faker lib):
```
    "account_number": fake.pyint(10000, 99999),
    "account_name": fake.name(),
    "iban": fake.iban(),
    "address": fake.address().replace("\n", ", "),
    "amount": fake.pyint(0, 9999),
    "type": get_random_type(fake.pybool())
```
Check that response code is equal to 200, otherwise drop assertion with error message
### test_1_negative::test_put_already_exist_transaction
This test send the document with one transaction into collection that already have transaction with same account_number:
```
    "account_number": 123456,
    "account_name": "John Doe",
    "iban": "GB22MWLH34465153677305",
    "address": "2872 Anita Causeway, Port Jeremyfurt, IL 19585",
    "amount": 999999,
    "type": "sending"
```
Check that response code is equal to 409, otherwise drop assertion with error message

## root directory
The root directory contains requirements for the project, this readme file and docker files to build docker image and run 
container