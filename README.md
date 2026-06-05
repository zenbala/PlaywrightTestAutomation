# Enterprise Web Automation Framework (Python + Playwright)

An enterprise-grade, high-performance web automation ecosystem engineered with **Python**, **Playwright**, and **Pytest**. This framework showcases cutting-edge automated testing methodologies, utilizing Behavior-Driven Development (BDD), isolated parallel execution mechanics, unified page object orchestration, and automatic reporting pipelines.

---

## 🚀 Key Architectural Capabilities

### 🔒 1. Global Authentication Session Caching
Instead of spamming security servers or slowing down runs by logging in before every test case, the framework abstracts authentication to a dedicated service layer (`services/globalauth.py`). 
* The framework executes a login sequence exactly **once** at session initialization.
* It serializes and caches browser cookies and `localStorage` keys locally inside `data/session_state.json`.
* Every subsequent test context spins up pre-seeded with this session state, instantly bypassing auth walls.

### 👥 2. Behavior-Driven Development (BDD Integration)
Features native **`pytest-bdd`** integration to implement human-readable Gherkin syntax step mappings. This bridges the communication gap between technical QA engineers, Product Owners, and manual validation teams.

### 🧬 3. Unified Page Object Manager Pattern
The custom `basepage` container class acts as a single-entry orchestrator for all application components (`LoginPage`, `dashboardPage`). This eliminates top-level import bloat in test scripts and enforces unified, clean variable dot-notation access across steps (e.g., `basePage.loginpage.navigate()`).

### ⚡ 4. Thread-Safe Concurrent Multi-Processing
Integrates **`pytest-xdist`** for heavy parallelism. To prevent multiple background workers from encountering race conditions or corrupting the global token stash at startup, a **FileLock inter-process lock** is wrapped around the session initializer. Only the master worker generates the authentication payload while subsequent workers wait safely.

### 📊 5. Diagnostic Reporting & Allure Dashboards
Configured via `pytest.ini` to auto-capture `--screenshot only-on-failure` and preserve a complete step-by-step interactive visual timeline using Playwright’s execution tracing (`--tracing retain-on-failure`). These assets are embedded dynamically into interactive **Allure Reports**.

---

## 📁 Repository Structure

```text
my_playwright_project/
│
├── .github/workflows/
│   └── playwright.yml       # Continuous Integration Pipeline (GitHub Actions CI)
├── data/
│   ├── test_data.json       # Centralized test registry for static payloads
│   └── session_state.json   # Cached browser state cookies (Explicitly Git Ignored)
├── pages/
│   ├── login_Page.py        # POM: Authentication fields and form actions
│   └── dashboard_Page.py    # POM: Post-login elements and cart workflows
├── services/
│   └── globalauth.py        # Standalone service generating the 1-time global login state
├── tests/
│   ├── features/
│   │   ├── login.feature    # Gherkin scenario definitions for login actions
│   │   └── dashboard.feature# Gherkin scenario definitions for dashboard behaviors
│   ├── test_login_bdd.py    # Pytest-BDD Step bindings for login scenarios
│   └── test_dashboard_bdd.py# Pytest-BDD Step bindings for dashboard scenarios
├── conftest.py              # Central hook configuration, locking engines, and fixtures
└── pytest.ini               # Core engine settings, xdist configurations, and logging layouts

```

---

## 🛠️ Installation & Setup

### 1. Prerequisites

Ensure you have Python 3.9+ installed locally on your system.

### 2. Environment Configuration

Create a `.env` file at your root project directory to store environment configs safely:

```env
BASE_URL=[https://www.saucedemo.com/](https://www.saucedemo.com/)
USERNAME=standard_user
PASSWORD=secret_sauce
ENV_USER=standard_user
ENV_PASSWORD=secret_sauce

```

### 3. Execution Setup

Clone this repository and install all operational dependencies:

```bash
# Clone the repository
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

# Provision a clean local virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install third-party testing components and native browser binaries
pip install -r requirements.txt
playwright install --with-deps

```

---

## 🎯 Running Tests

The framework parameters are automated entirely via settings declared inside `pytest.ini`.

**Run the complete test suite in parallel (Automatic core detection):**

```bash
pytest

```

**Run specific test categories using markers:**

```bash
pytest -m smoke

```

**Run sequentially in a specific browser environment (Headed visualization mode):**

```bash
pytest -n 0 --headed --browser chromium

```

**Serve the local interactive Allure HTML execution dashboard:**

```bash
allure serve allure-results

```
