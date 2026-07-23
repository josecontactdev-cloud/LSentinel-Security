# 🛡️ LSentinel

> A modern Discord bot focused on cybersecurity, networking, OSINT, and developer utilities.

![Python](https://img.shields.io/badge/Python-3.14+-blue?logo=python)
![Discord.py](https://img.shields.io/badge/discord.py-2.x-5865F2?logo=discord)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📖 About

LSentinel is an open-source Discord bot built with **Python** and **discord.py**.

The project is designed as both:

- A cybersecurity utility bot
- A networking toolkit
- An OSINT assistant
- A portfolio project demonstrating clean architecture and software engineering practices

Unlike many Discord bots, LSentinel emphasizes:

- Clean Architecture
- Service Layer Pattern
- Unit Testing
- Modular Design
- Logging
- Maintainability
- Scalability

---

# ✨ Features

## 🔐 Crypto

- Hash Generator
- Multiple Algorithms
- Hash Validation *(planned)*

---

## 🌐 Network

- IP Lookup
- DNS Lookup
- Reverse DNS *(planned)*
- HTTP Headers *(planned)*
- HTTP Status *(planned)*

---

## 🛡 Security

- SSL Certificate Check
- Security Headers *(planned)*
- robots.txt Scanner *(planned)*
- security.txt Scanner *(planned)*

---

## 🔍 OSINT

- WHOIS Lookup
- Subdomain Discovery *(planned)*
- Certificate Transparency *(planned)*
- Email Security *(planned)*

---

# 🏗 Project Structure

```
LSentinel-Security/
│
├── src/
│   ├── cogs/
│   ├── core/
│   ├── database/
│   ├── services/
│   ├── utils/
│   └── views/
│
├── tests/
│
├── logs/
│
├── README.md
├── requirements.txt
├── pyproject.toml
└── LICENSE
```

---

# 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/josecontactdev-cloud/LSentinel-Security.git
```

Enter the project.

```bash
cd LSentinel-Security
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### Windows

```powershell
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# ⚙️ Environment Variables

Create a `.env` file.

```env
DISCORD_TOKEN=YOUR_DISCORD_TOKEN
```

---

# ▶ Running

```bash
python src/bot.py
```

---

# 🧪 Testing

Run all unit tests.

```bash
pytest
```

---

# 🎨 Code Quality

Format code.

```bash
black src tests
```

Run Ruff.

```bash
ruff check src tests --fix
```

---

# 🛣 Roadmap

## Phase 1

- [x] Modular Architecture
- [x] Crypto Service
- [x] Network Service
- [x] Logger
- [x] Configuration Manager
- [x] Unit Testing

## Phase 2

- [ ] Security Service
- [ ] OSINT Service
- [ ] Validators
- [ ] Embed Builder Improvements

## Phase 3

- [ ] HTTP Headers
- [ ] robots.txt
- [ ] security.txt
- [ ] Reverse DNS
- [ ] JWT Tools

## Phase 4

- [ ] Database Support
- [ ] Caching
- [ ] Metrics
- [ ] Background Tasks

## Phase 5

- [ ] Docker
- [ ] CI/CD
- [ ] GitHub Actions
- [ ] Documentation Website

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

# 👨‍💻 Author

Developed by **Jose Dev**.

GitHub:
https://github.com/josecontactdev-cloud