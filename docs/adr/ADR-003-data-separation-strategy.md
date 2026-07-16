# ADR-003 Separation of Shared Card Data and User Collection Data

## Status

Accepted

## Date

2026-07-16

## Context

Pokémon TCG Analyzer stores both public Pokémon card information and user-specific collection information.

Card metadata such as name, rarity, set, type, and images is shared among all users.

However, ownership information such as quantity, purchase price, acquisition method, and collection notes belongs to individual users.

A database design decision is required to determine whether these two types of information should be stored together or separately.

## Considered Options

### Option 1: Store Card and Collection Data Together

Example:

```
UserCollection

user_id
card_name
rarity
set
quantity
purchase_price
```

Advantages:

- Simple structure.
- Easier initial implementation.

Disadvantages:

- Duplicates card metadata.
- Increased storage usage.
- Difficult to update shared card information.
- Poor support for multiple users.

---

### Option 2: Separate Card Data and Collection Data

Example:

```
Card

id
name
rarity
set


CollectionItem

user_id
card_id
quantity
purchase_price
```

Advantages:

- Avoids duplicated metadata.
- Supports multiple users owning the same card.
- Improves data consistency.
- Enables future analytics.

Disadvantages:

- Requires relational joins.
- Slightly more complex schema.

## Decision

The system separates shared card information from user-owned collection information.

The Card entity stores public Pokémon TCG metadata, while CollectionItem stores user-specific ownership data.

## Rationale

This separation follows database normalization principles and improves scalability.

Multiple users can reference the same Card record without duplicating card information.

It also allows future expansion of collection features, including individual card tracking, trading history, and advanced analytics.

## Consequences

### Advantages

- Reduced data duplication.
- Improved data consistency.
- Supports multi-user architecture.
- Easier future expansion.

### Disadvantages

- Requires additional relationships between entities.
- More complex database queries.

## Future Considerations

Future versions may introduce additional entities such as CardInstance or TransactionHistory while preserving the separation between shared card data and user-specific data.