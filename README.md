# org_log – Organizational Logging Package

A reusable, production-ready Python logging package designed for organizational use, educational purposes, and portfolio showcase.

---

## Features

- Modular and reusable logging architecture
- Named loggers for large-scale applications
- Rotating file handler to prevent unlimited log growth
- Clean separation of configuration and usage
- Safe reconfiguration without duplicate handlers
- Fully documented and extensible design

---

## Package Structure

org_log/
│
├── init.py
├── log_setup.py
├── log_writer.py
└── main.py

---

## Installation

Clone the repository and use it directly in your project:

```bash
git clone https://github.com/your-username/org_log.git
No external dependencies are required.
```
Usage Example
Configure Logger
from org_log.log_setup import configure_logger

configure_logger(
    logger_name="org.application",
    log_file="logs/app.log"
)
Write Logs
from org_log.log_writer import log_info, log_warning, log_error

log_info("org.application", "Application started")
log_warning("org.application", "Low disk space detected")
log_error("org.application", "Unhandled exception occurred")

---

## Design Principles
•	Separation of concerns: configuration and usage are isolated
•	Scalability: supports multiple loggers across services
•	Safety: prevents duplicate handlers and log flooding
•	Maintainability: clear structure and documentation

---

## Educational Value
This repository demonstrates:
•	Professional Python package structuring
•	Real-world logging best practices
•	Use of logging and RotatingFileHandler
•	Clean API design for organizational reuse
•	Software craftsmanship

---

## Disclaimer
This project is intended strictly for educational, demonstration, and portfolio showcase purposes.
It is not a drop-in replacement for enterprise observability solutions and should be adapted and reviewed before use in production systems.
