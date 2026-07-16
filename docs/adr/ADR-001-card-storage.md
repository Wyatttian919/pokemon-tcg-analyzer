# ADR-001 Hybrid Card Storage Strategy

## Status

Accepted

## Context

The Pokémon TCG API provides card metadata and market prices.

We need to determine whether card data should be stored locally or fetched from the API on demand.

## Decision

Use a hybrid strategy.

Static card metadata will be stored locally.

Dynamic pricing data will be synchronized periodically.

## Consequences

Advantages

- Faster queries
- Stable system
- Supports analytics

Disadvantages

- Requires synchronization jobs