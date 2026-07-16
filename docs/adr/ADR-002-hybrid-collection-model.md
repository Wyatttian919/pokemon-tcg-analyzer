# ADR-002: Adopt Hybrid Collection Model for Card Ownership Tracking

## Status

Accepted

## Date

2026-07-16

## Context

Pokémon TCG collectors may own multiple copies of the same card, but individual cards can also have different physical conditions, grading status, and acquisition histories.

A collection management system needs to balance two conflicting requirements:

1. Simple collection management for general users.
2. Detailed tracking capability for advanced collectors.

Several approaches were considered for representing user-owned cards.

## Considered Options

### Option 1: Quantity-based Collection Model

In this approach, each collection record represents a card type with a quantity value.

Example:

```
Card:
Charizard ex

CollectionItem:
quantity = 3
condition = NM
```

#### Advantages

- Simple database structure.
- Easy collection management.
- Efficient for dashboard calculations.
- Suitable for MVP development.

#### Disadvantages

- Cannot represent individual card differences.
- Difficult to track grading information.
- Cannot record unique acquisition history.

---

### Option 2: Individual Card Tracking Model

In this approach, every physical card receives an independent record.

Example:

```
CardInstance:

Charizard ex
PSA 10
Certificate #12345

Charizard ex
Raw NM

Charizard ex
Raw LP
```

#### Advantages

- Supports detailed collector workflows.
- Enables grading tracking.
- Supports trading history and ownership transfer.

#### Disadvantages

- Higher database complexity.
- More complicated user experience.
- Requires additional data management for MVP.

---

### Option 3: Hybrid Collection Model

The system stores collection information using CollectionItem records while keeping future support for individual card tracking.

Current MVP:

```
Card
 |
 |
CollectionItem

Charizard ex
quantity = 3
condition = NM
```

Future expansion:

```
Card
 |
 |
CardInstance
```

where each CardInstance represents an individual physical card.

## Decision

The project adopts the Hybrid Collection Model.

The MVP implementation uses CollectionItem as the primary ownership entity.

CollectionItem stores:

- user ownership
- quantity
- condition
- acquisition information
- purchase information

The design leaves an extension path for introducing CardInstance in future versions.

## Rationale

The Hybrid Collection Model provides the best balance between usability, implementation complexity, and future scalability.

For MVP users, most collection management scenarios only require knowing:

- Which cards they own.
- How many copies they have.
- Approximate collection value.

Tracking every physical card would introduce unnecessary complexity before advanced features are required.

At the same time, the design avoids blocking future functionality because individual card tracking can be introduced through an additional CardInstance entity.

## Consequences

### Positive Consequences

- Faster MVP development.
- Simpler database schema.
- Easier collection management experience.
- Supports future grading and trading features.

### Negative Consequences

- Cannot distinguish individual cards with different conditions in MVP.
- Some advanced collector workflows require future migration to CardInstance.

## Future Considerations

Future versions may introduce CardInstance to support:

- PSA/BGS/CGC grading information.
- Certification numbers.
- Individual acquisition history.
- Trading records.
- Ownership transfer tracking.

The introduction of CardInstance should extend the existing schema without requiring major changes to Card, User, or CollectionItem entities.