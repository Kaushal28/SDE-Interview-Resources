# ACID Properties

`Transactions` are a single unit of work that accesses and/or modifies the database content. In order to keep data consistent, `ACID` properties are followed before and after the transactions.

**ACID** stands for:

- A - Atomicity
- C - Consistency
- I - Isolation
- D - Durability

## Atomicity

- Either the entire transaction takes place or it doesn't. There is NO partial transaction state. Consider an example of money transfer from account of one person (A) to another person (B). The following operations are supposed to take place for a single transaction
  - Read balance from Account A
  - Update A's balance
  - Update B's balance
- If transactions were not atomic, they can fail at any of the steps, which leads database into inconsistent state. Atomicity ensures that either all 3 steps execute successfully or none of them. This prevents inconsistent state in database (for example amount debited from A but not creditede in B's account). Transaction failers are easier to handle (e.g. by retrying) than inconsistencies.

## Consistency

- This referes to correctness of the database.
- Database should be consistent before and after the execution of the transaction.
- In the above example, the total amount of money in the system must be maintained before and after the transaction.


## Isolation

- This property ensures that multiple transactions can be occurred concurrently without leading to database inconsistencies.
- Transactions occur independently without interference. Changes occurring in a particular transaction will not be visible to any other transaction until that particular change in that transaction is written to memory or has been committed.
- This property ensures that the execution of transactions concurrently will result in a state that is equivalent to a state achieved if these were executed serially in some order.

## Durability
- This property ensures that once the transaction has completed execution, the updates and modifications to the database are stored in and written to disk and they persist even if a system failure occurs. These updates now become permanent and are stored in non-volatile memory. The effects of the transaction, thus, are never lost.
