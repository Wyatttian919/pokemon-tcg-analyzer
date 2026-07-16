# Pokémon TCG Analyzer - API Design

## 1. API Overview

The REST API is designed around the following core resources:

- Card
- Set
- Collection Item
- Dashboard
- User

## 2. API Design Principles

The API follows RESTful design principles.

- Resource-oriented endpoints
- Stateless communication
- JSON request and response bodies
- Versioned APIs (/api/v1)
- Secure authentication for protected resources

## 3. Authentication

### Purpose

Provide secure user authentication and authorization.

### Operations

- Register
- Login
- Refresh Access Token (Future)
- Logout

## 4. Card API

### Purpose

Provide card search and card information.

### Operations

- Search Cards
- View Card Details
- View Trending Cards
- View Recommendation Cards
- Browse Latest Sets

## 5. Set API

### Purpose

Provide information about Pokémon card sets.

### Operations

- View Latest Sets
- Browse Sets
- View Set Details

## 6. Collection API

### Purpose

Manage the user's personal card collection.

### Operations

- View Collection
- Add Card
- Update Card
- Remove Card 
<!-- 可以标记为全有，再取消。更准确点，批量操作。 -->

## 7. Dashboard API

### Purpose

Provide analytical information for a user's collection

### Operations

- View Dashboard Summary
- View Collection Statistics
- View Value Trend
- View Collection Distribution

## 8. Future APIs

- AI Assistant
- Pack Analytics
- Card Recogntion