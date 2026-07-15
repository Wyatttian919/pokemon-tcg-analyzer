# Pokémon TCG Analyzer

A full-stack web application for Pokémon Trading Card Game collectors.

Pokémon TCG Analyzer helps collectors manage their card collections, track market prices, analyze collection value, and receive AI-powered insights.

## Overview

Pokémon TCG collecting involves managing large collections, tracking price changes, and making decisions about purchases or trades.

This project aims to build an intelligent platform that combines card database management, market analysis, and AI assistance into one application.

The project is inspired by my own experience collecting Pokémon TCG cards and exploring card value trends.

## Features

### Card Database

- Search Pokémon cards by name, set, number, and type
- Display card details including:
  - Card image
  - HP
  - Type
  - Rarity
  - Set information
  - Market price


### Collection Management

- User authentication and personal collections
- Add, remove, and update owned cards
- Track:
  - Card quantity
  - Purchase price
  - Collection value


### Collection Dashboard

- Visualize personal collection statistics
- Display:
  - Total cards owned
  - Estimated collection value
  - Distribution by set
  - Distribution by card type


### Market Analysis

- Track historical card prices
- Visualize price trends
- Analyze collection value changes


### AI-powered Insights (Future)

- AI collection advisor
- Card recommendation based on budget and preferences
- Natural language questions about Pokémon cards
- Card image recognition

## Tech Stack

### Frontend

- React
- TypeScript
- Tailwind CSS


### Backend

- Python
- FastAPI


### Database

- PostgreSQL
- SQLAlchemy


### Authentication

- JWT


### External APIs

- Pokémon TCG API


### Deployment

- Docker
- Vercel
- Render

## System Architecture


## Project Structure

```text
pokemon-tcg-analyzer/

├── frontend/ # React + TypeScript frontend
├── backend/ # FastAPI backend
├── docs/ # Project documentation
├── README.md
└── .gitignore
```

## Roadmap

### Phase 0: Project Setup ✅

- Initialize GitHub repository
- Define project architecture
- Set up development environment


### Phase 1: Core Application

- Design database schema
- Develop FastAPI backend
- Integrate Pokémon TCG API
- Build React frontend
- Implement card search
- Create card detail pages


### Phase 2: User & Collection System

- Implement user authentication
- Build collection management
- Add personal dashboard
- Store user data with PostgreSQL


### Phase 3: Analytics Platform

- Add price history tracking
- Build collection analytics
- Implement market trend visualization
- Add EV calculator for booster products


### Phase 4: AI Integration

- Build AI Pokémon assistant
- Implement recommendation system
- Add RAG-based card knowledge search
- Add image-based card recognition


### Phase 5: Deployment & Optimization

- Containerize application with Docker
- Deploy frontend and backend
- Add automated testing
- Implement CI/CD pipeline
## Future Improvements

Potential future improvements include:

- Mobile application support
- Advanced collection recommendation algorithms
- Community trading features
- Competitive deck analysis
- Real-time market alerts

## Author

Created by Wyatttian919.

This project is built as a personal full-stack development project combining software engineering, data analysis, and AI applications.