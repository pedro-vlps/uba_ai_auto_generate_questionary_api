# UBA Questionary API

UBA Questionary API is a production-oriented backend for an educational platform that generates multiple-choice questions with AI, manages institution-based access, tracks learner answers, and handles paid access through Stripe.

This project was designed to support real product workflows instead of isolated demos. It combines AI-assisted content generation, authentication, subscription-aware permissions, encrypted user data, and administrative operations in a single FastAPI service.

## Recruiter Snapshot

- Product focus: educational SaaS / edtech backend
- Core value: generate domain-specific questions while controlling access by institution, user profile, and payment status
- Main business flows: authentication, AI question generation, answer tracking, Stripe checkout, webhook processing, and admin campaigns
- Engineering highlights: async API design, multi-tenant access rules, encrypted sensitive data, webhook-driven billing sync, and automated test coverage

## What This Project Demonstrates

- Building a backend API around a real business domain instead of a generic CRUD sample
- Integrating OpenAI to generate structured learning content
- Designing permission checks that combine JWT authentication, institution membership, and subscription state
- Handling payment events safely with Stripe webhooks and access synchronization
- Protecting user-sensitive data with encryption and hashed lookup fields
- Organizing code with routers, controllers, services, schemas, middleware, and tests

## Core Features

- AI-generated anatomy and biology questions
- Topic-aware prompt assembly with anti-repetition context from recent questions
- JWT-based authentication for protected routes
- Password reset and nickname recovery flows
- Institution-aware permission checks using the `x-institution-id` header
- User answer submission and latest-answer retrieval
- Stripe checkout session generation with coupon support
- Webhook-based payment processing and subscription synchronization
- Subscription quota tracking for question generation packages
- Admin dashboard summaries for payment cohorts
- Manual inactive-plan follow-up email campaign workflow
- Generic CRUD route generation for selected resources through a reusable internal library

## Tech Stack

| Area | Technologies |
| --- | --- |
| Language | Python 3.13 |
| API framework | FastAPI |
| ASGI server | Uvicorn |
| Validation / settings | Pydantic, `pydantic-settings` |
| Database access | SQLAlchemy Async ORM |
| Database | PostgreSQL 16 |
| AI integration | OpenAI Responses API |
| Payments | Stripe |
| Security | JWT, Fernet encryption, hashed identifiers |
| Containerization | Docker, Docker Compose |
| Testing | Pytest, Coverage |
| Packaging | Poetry |

## Architecture Overview

The application follows a layered structure:

- Routers expose HTTP endpoints and dependency wiring.
- Controllers coordinate request/response behavior.
- Services implement domain and integration logic.
- Schemas validate API contracts.
- Middleware centralizes JWT validation and permission checks.
- Models define the relational data structure with SQLAlchemy.

This separation keeps the business rules testable and makes it easier to evolve integrations such as OpenAI, Stripe, and SMTP independently from the transport layer.

## Business and Technical Highlights

- AI generation is domain-specific rather than generic: the backend builds prompts for anatomy and biology topics and injects recent questions to reduce repetition.
- Access control is business-aware: a valid JWT alone is not enough; the user may also need institution membership and an active package, depending on the route.
- Billing is connected to authorization: Stripe events update subscription records and automatically grant or revoke access to the UBA institution profile.
- Sensitive user fields are protected: email, nickname, DNI, and password are encrypted, while hashed copies support uniqueness checks and lookups.
- The codebase includes dedicated tests for routes, services, infrastructure behavior, permissions, and Stripe webhook normalization.

## Main API Surface

| Area | Endpoints |
| --- | --- |
| Health | `GET /healthy` |
| Authentication | `POST /login`, `POST /login/admin` |
| Account recovery | `POST /forgot-password`, `POST /reset-password`, `POST /forgot-nickname`, `POST /recover-nickname` |
| Users | `POST /users`, `GET /users/me`, `PUT /users/me` |
| AI question generation | `POST /ai/anatomy`, `POST /ai/biology` |
| Answers | `POST /question-answers`, `GET /question-answers/latest-answers` |
| Billing | `POST /stripe/generate`, `POST /stripe/webhook/payment` |
| Admin | `GET /admin/dashboard/user-payment-summary`, `POST /admin/email-campaigns/inactive-plan-follow-up` |
| Resource access | `GET /institutions`, generated CRUD-style endpoints for selected resources |

## Project Structure

```text
src/
  configs/        # environment settings and async database session setup
  controllers/    # request orchestration
  databases/      # SQL scripts, migrations, and seed data
  helpers/        # AI prompt templates and permission dictionaries
  middleware/     # JWT validation and authorization rules
  models/         # SQLAlchemy models and generated route declarations
  routers/        # FastAPI route definitions
  schemas/        # request/response contracts
  services/       # business logic and third-party integrations
  utils/          # encryption, JWT, sanitization, and lookup helpers
tests/            # route, service, permission, and infrastructure tests
```

## Local Development

### Prerequisites

- Python 3.13
- Poetry
- Docker and Docker Compose
- PostgreSQL 16 if you prefer running the database outside Docker

### Environment Variables

Create a `.env` file in the project root. The application settings are defined in `src/configs/configs.py`.

```env
APP_ENV=DEV

POSTGRES_DB=your_database
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5434

OPENAI_API_KEY=your_openai_key

FERNET_KEY=your_fernet_key
JWT_SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=60

RESTRICT_STRIPE_AUTH_KEY=your_stripe_restricted_key
PUBLIC_STRIPE_AUTH_KEY=your_stripe_publishable_key
SECRET_STRIPE_AUTH_KEY=your_stripe_secret_key
WEBHOOK_STRIPE_SECRECT_KEY=your_stripe_webhook_secret
DEFAULT_PRICE_ID=price_xxx
PAYMENT_CURRENCY=ars
CHECKOUT_REDIRECT_URL=https://your-frontend.example.com/payment/success

PASSWORD_RESET_TOKEN_EXPIRATION_MINUTES=30
PASSWORD_RESET_INCLUDE_TOKEN_IN_RESPONSE=false
PASSWORD_RESET_URL=https://your-frontend.example.com/reset-password
NICKNAME_RECOVERY_TOKEN_EXPIRATION_MINUTES=30
NICKNAME_RECOVERY_INCLUDE_TOKEN_IN_RESPONSE=false
NICKNAME_RECOVERY_URL=https://your-frontend.example.com/recover-nickname

SMTP_ENABLED=false
SMTP_HOST=localhost
SMTP_PORT=1025
SMTP_USE_TLS=false
SMTP_USE_SSL=false
SMTP_USERNAME=
SMTP_PASSWORD=
SMTP_FROM_EMAIL=noreply@example.com
SMTP_FROM_NAME=UBA Questionary
SUPPORT_EMAIL=support@example.com

FRONTEND_ORIGINS=http://localhost:3000
```

### Run with Docker Compose

```bash
docker compose up --build
```

The API will be available at `http://localhost:8000`.

If the API and database both run inside Docker Compose, use `POSTGRES_HOST=db` and `POSTGRES_PORT=5432`.

### Run with Poetry

```bash
poetry install
poetry run uvicorn src.__main__:app --reload
```

If you run the API with Poetry against the database exposed by Docker Compose, keep `POSTGRES_HOST=localhost` and `POSTGRES_PORT=5434`.

## Testing

```bash
poetry run pytest
```

To run the predefined task shortcuts:

```bash
poetry run task test
poetry run task coverage
```

## API Documentation

Interactive API documentation is available in non-production environments:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

These routes are disabled when `APP_ENV` is set to `P`.

## Why This Backend Stands Out

Unlike tutorial-style APIs, this project ties together several concerns that usually appear in real products:

- AI content generation with domain constraints
- Payment-aware entitlement management
- Institution and profile-based authorization
- Secure handling of personal information
- Operational admin tooling
- Automated verification of core business flows

It is a strong example of backend engineering for SaaS and edtech scenarios, especially where product logic, security, and third-party integrations must work together reliably.
