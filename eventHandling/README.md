<div align="center">
  <h1>🚀 EventHandling Backend API</h1>
  <p><strong>A robust, secure, and modular Django-based event management system.</strong></p>
  <br>
</div>

## 1. Overview
The **EventHandling API** is a custom backend solution engineered to manage event registrations, user profiles, and administrative capacity control. The architecture prioritizes data integrity and secure authorization through a modular, decorator-based approach, built strictly on **Django's native framework capabilities**.

---

## 2. 🏗️ Architectural Highlights
*   **Decoupled Security Layer**: Implemented a custom `@admin_required` decorator to enforce role-based access control, isolating security logic from core business functionality.
*   **Defensive Validation**: Applied rigorous boolean guardrails (`is_math_valid`, `is_within_limits`, `is_non_negatives`) to ensure all capacity updates maintain atomic data integrity.
*   **Fault-Tolerant Request Processing**: Every API endpoint utilizes standardized `try-except` blocks to catch and gracefully report `JSONDecodeError` and database integrity exceptions.

---

## 3. 🛠️ Technology Stack
| Component | Technology |
| :--- | :--- |
| **Core Engine** | Python 3.x, Django 4.x |
| **Data Persistence** | SQLite ORM |
| **Authorization** | Django Session-based Authentication |

---

## 4. 🔗 API Contract
| Method | Endpoint | Authorization | Description |
| :--- | :--- | :--- | :--- |
| `POST` | `/user_register` | `@login_required` | Registers user profile. |
| `POST` | `/event_registeration` | `@login_required` | Initializes event schema. |
| `GET` | `/event_list` | `@login_required` | Fetches all events. |
| `POST` | `/event_handle` | `@login_required` | Processes reservations. |
| `POST` | `/cancelEvent` | `@login_required`, `@admin_required` | Reverts registration. |
| `POST` | `/event_update` | `@login_required`, `@admin_required` | Admin capacity management. |
| `POST` | `/event_delete` | `@login_required`, `@admin_required` | Admin event removal. |

---

## 5. 🚀 Deployment & Setup

<details>
<summary><strong>Click to expand setup instructions</strong></summary>

### Local Infrastructure
1.  **Environment Initialization**: 
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
2.  **Dependency Configuration**:
    ```bash
    pip install django
    ```
3.  **Migration & Execution**:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```
</details>

<br>

<div align="center">
  <sub>Built with precision for the CodeAlpha Internship</sub>
</div>
