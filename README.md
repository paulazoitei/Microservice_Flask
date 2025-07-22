# Flask Microservice – Powered API with Monitoring

This is a Python microservice built with **Flask**, designed to:

- Expose REST API endpoints for mathematical operations (`/pow`, `/fibo_function`, `/factorial_function`)
- Persist each request into a **SQLite** database
- Automatically monitor endpoint performance via **Flask-MonitoringDashboard**
- Run in production using **Gunicorn**
- Fully containerized with **Docker**

---

## Features

- Modular, MVC-like structure (`controllers/`, `services/`, `models/`)
- Request logging and persistence with SQLAlchemy
- Monitoring of response times, outliers, and profiling via dashboard
- Configurable via external `config.cfg` (ignored in repo)
- Docker-ready with clean `Dockerfile`

---

## Available API Endpoints

| Method | Endpoint                     | Description                                        |
| ------ | ---------------------------- | -------------------------------------------------- |
| POST   | `/pow_function`              | Input: `{ "number": 2, "power": 3 }` → Output: `8` |
| POST   | `/fibo_function`             | Input: `{ "number": 10 }` → Output: `55`           |
| POST   | `/factorial_function`        | Input: `{ "number": 5 }` → Output: `120`           |
| GET    | `/get_all_requests_function` | Returns all request logs stored in DB              |

---

## Monitoring Dashboard

Visit: `http://localhost:8081/dashboard`

- Login required (credentials stored in `config.cfg`)
- View request stats, execution time distribution, outliers
- Each endpoint can have its own monitoring level (0–3)

---

## Running the App with Docker

### Build the image:

```bash
docker build -t paulazoitei/microservices_flask:2.0 . 
```

### Run the container:

```bash
 docker run -p 8081:8081 paulazoitei/microservices_flask:2.0  
```

> You can also bind to another local port if 8081 is busy: `-p 8082:8081`

---

## Technologies Used

- **Python 3.11**
- **Flask**
- **Flask-MonitoringDashboard** (performance tracking)
- **Gunicorn** (production WSGI server)
- **SQLite** (via SQLAlchemy)
- **Docker**

---

## Notes

- `config.cfg` is **ignored by Git** (see `.gitignore`)
- You can create a `config.cfg.template` to share structure without secrets
- Database file is saved as `instance/request.db` (also ignored from Git)

---

## Future Improvements

- Add Kafka integration for async event logging
- Switch to PostgreSQL or MySQL for persistent storage
- Add authentication & authorization
- Integrate Prometheus & Grafana for advanced observability

---



