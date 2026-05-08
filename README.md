# 🎰 Gambling App

A Python CLI-based gambling application built with clean architecture principles and the **Strategy design pattern**. Players can interact with various casino-style games through a command-line interface, with persistent data backed by a database layer.

---

## 📁 Project Structure

```
gambling_app/
├── main.py              # Entry point — bootstraps and launches the CLI
├── cli/                 # Command-line interface layer (GameCLI)
├── service/             # Business logic / game orchestration
├── strategy/            # Strategy pattern implementations (game algorithms)
├── entity/              # Domain models (Player, Game, etc.)
├── dto/                 # Data Transfer Objects
├── enums/               # Enumerations (game types, statuses, etc.)
├── exceptions/          # Custom exception classes
├── validation/          # Input validation logic
├── utils/               # Helper utilities
├── DBs/                 # Database files / persistence layer
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- No external dependencies required (pure Python)

### Running the App

```bash
git clone https://github.com/MohitAr2/gambling_app.git
cd gambling_app
git checkout dev
python main.py
```

---

## 🏗️ Architecture

The app follows a layered architecture:

**CLI → Service → Strategy → Entity / DB**

| Layer | Responsibility |
|---|---|
| `cli/` | Handles user input/output, menu navigation |
| `service/` | Orchestrates game flow and business rules |
| `strategy/` | Pluggable game logic via the Strategy pattern |
| `entity/` | Core domain models |
| `dto/` | Data shapes passed between layers |
| `validation/` | Guards inputs before processing |
| `exceptions/` | Domain-specific error handling |
| `DBs/` | Flat-file or SQLite persistence |

### Design Pattern: Strategy

Each game type is implemented as a separate strategy class. The service layer selects and executes the correct strategy at runtime, making it straightforward to add new games without modifying existing code.

---

## 🌿 Branch Structure

| Branch | Description |
|---|---|
| `dev` | Main integration branch — all features merge here |
| `feature/blackjack` | Blackjack game implementation |
| `feature/slots` | Slot machine game implementation |
| `feature/roulette` | Roulette game implementation |
| `feature/wallet` | Player wallet / balance management |

---

## 🧱 Key Concepts

- **Entities** represent core domain objects (e.g., `Player`, `Game`, `Bet`).
- **DTOs** carry data between layers without exposing internals.
- **Enums** standardise game states, result types, and game names.
- **Custom exceptions** provide meaningful error messages for invalid bets, insufficient funds, etc.
- **Validation** ensures all user inputs are sanitised before reaching the service layer.

---

## 📝 Contributing

1. Branch off `dev` using the `feature/<name>` convention.
2. Keep game logic inside `strategy/` and orchestration inside `service/`.
3. Add validation for all new user-facing inputs.
4. Merge back to `dev` via pull request.
