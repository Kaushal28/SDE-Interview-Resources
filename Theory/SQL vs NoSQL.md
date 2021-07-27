# When to use SQL vs NoSQL?
- Choice between SQL and NoSQL databases depends on many aspects. For example nature of data to be stored, scaling requirements, future changes in schema, development time, etc.
- NoSQL databases are newer and designed for horizontal scaling, fast queries, allowing for frequent application changes, and making programming simpler for developers. Examples: MongoDB, CouchDB, etc.
- SQL databases are older/mature and are design for reducing data duplication (as storage was costly than developers' time), rigid, complex, tablular schemas and require vertical scaling. Examples: PostgreSQL, MySQL, etc.

## Use SQL when
- You don't expect too many changes going forward. Limited amounts of data volume with limited data types and static data structure.
- You want to ensure ACID properties for all your transactions (ACID properties/transactions are not ensured across multiple documents in NoSQL)
- There are considerable amount of transactions in your application. SQL databases are mature and well suited for executing heavy duty and complex transactions.
- high amount of data consistency is required
- better community support is required to ensure less challenges at the time of development

## Use NoSQL when
- your structure of data is dynamic, there would considerable changes over time (NoSQL provides highly flexible schema design)
- 100% data consistency is not that much important (for example social media applications) as compared to data availability and scaling.
- you have huge amounts of data
- horizontal scaling is required because of high application usage.
- faster and comparatively easier development
- faster queries are required because data in NoSQL databases is typically stored in a way that is optimized for queries. The rule of thumb when you use MongoDB is Data is that is accessed together should be stored together. Queries typically do not require joins, so the queries are very fast as compared to normalized SQL tables.
