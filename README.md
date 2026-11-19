<div align="center">
  <img alt="Tavro Logo" src="assets/Tavro_Horizontal_Logo.png" width="450">

  <h3>Personal AI, On Personal Devices</h3>

  <p>
    <a href="https://github.com/dineshreddy0204/TAVRO-MAIN"><img src="https://img.shields.io/badge/GitHub-TAVRO--MAIN-181717?logo=github" alt="Repo"></a>
    <img src="https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-3776AB?logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/frontend-React%2019%20%2B%20Vite-61DAFB?logo=react&logoColor=black" alt="React">
    <img src="https://img.shields.io/badge/engine-Ollama%20%7C%20MultiEngine-black" alt="Engine">
    <img src="https://img.shields.io/badge/platform-Windows%20ARM64%20%7C%20macOS%20%7C%20Linux-0078D4?logo=windows&logoColor=white" alt="Platform">
    <img src="https://img.shields.io/badge/license-Apache%202.0-22c55e" alt="License">
  </p>
</div>

---

<div align="center">
  <img alt="Tavro Demo Reel" src="assets/tavro_demo_reel.webp" width="80%">
</div>

---

## 🌟 Overview

**Tavro** is an autonomous, local-first personal AI framework built to run powerful language models directly on personal devices. Unlike conventional cloud-dependent assistants that route private context, files, and queries through third-party APIs, Tavro operates on-device by default.

It couples a high-performance **FastAPI** backend with a responsive **React 19 + Vite** desktop and web interface, delivering state-of-the-art agent workflows, deep research capabilities, tool execution, and local model orchestration.

---

## 🏗️ Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Tavro Client Frontend                           │
│              React 19 · TypeScript · Vite · TailwindCSS                │
│                 http://127.0.0.1:5173 (or Tauri App)                   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Reverse Proxy (/v1, /health, WS)
┌───────────────────────────────────▼────────────────────────────────────┐
│                       Tavro API Core Server                            │
│                 FastAPI · Uvicorn · Starlette Engine                   │
│                        http://127.0.0.1:8000                           │
├───────────────────────────────────┬────────────────────────────────────┤
│   Agent Execution & Tool Layer    │      Inference Routing Layer       │
│   · ReAct & CodeAct (OpenHands)   │      · MultiEngine Wrapper         │
│   · Deep Research & Memory        │      · In-Process Engine Resolvers │
│   · Shell, Filesystem, Python     │      · Dynamic Model Pull API      │
│   · MCP Tools & Webhooks          │      · Guardrails & Telemetry      │
└───────────────────────────────────┼────────────────────────────────────┘
                                    │ Local Loopback (HTTP 11434)
┌───────────────────────────────────▼────────────────────────────────────┐
│                    Native Local Ollama Runtime                         │
│       llamacpp · CPU / Snapdragon X NPU Acceleration · Port 11434      │
│              Models: qwen3.5:4b · qwen3.5:0.8b · llama3                │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Key Features

- **Local-First Inference & MultiEngine Routing:**
  - Zero-latency local execution powered by Ollama.
  - Transparent `MultiEngine` routing that resolves local vs. cloud engines dynamically.
  - Dynamic in-app model pulling (`POST /v1/models/pull`) with streaming progress reporting and automatic model map refreshing.
- **Autonomous Agent Workflows:**
  - **Orchestrator:** Multi-turn intent planning with proactive tool calling.
  - **Native ReAct:** Thought-Action-Observation loops for multi-step reasoning.
  - **Native OpenHands (CodeAct):** Generates, refines, and executes real Python code to complete complex tasks.
  - **Deep Research:** Multi-source citation collection, document summarization, and query decomposition.
- **OpenAI-Compatible REST & WebSocket API:**
  - Drop-in compatibility for `/v1/chat/completions`, `/v1/models`, `/v1/info`, `/v1/agents/events`, and server-sent streaming (SSE).
- **Rich User Interface:**
  - Modern, responsive chat UI built with React 19, Motion animations, Lucide icons, and KaTeX mathematical formula rendering.
  - Contextual Server Status distinguishing configured preferences from active runtime engines.
  - Progressive Web App (PWA) offline capabilities and cross-platform desktop integration via Tauri v2.
- **Memory & Context Retrieval:**
  - Vector and keyword memory interfaces (SQLite, BM25, ColBERT, FAISS).
  - Graceful degradation with actionable status indicators and non-blocking retry mechanisms.

---

## 💻 Tech Stack

| Domain | Technologies |
|---|---|
| **Backend** | Python 3.10–3.12 (CPython), FastAPI, Starlette, Uvicorn, Pydantic v2, HTTPX, Maturin |
| **Frontend** | TypeScript, React 19, Vite, TailwindCSS v4, Zustand, Motion, KaTeX, Lucide React |
| **Local LLM Engine** | Ollama (`0.40.16`+), `llamacpp`, GGUF quantization (Q4_K_M, Q8_0) |
| **Desktop Integration**| Tauri v2, Rust 1.89+ (x86_64-pc-windows-msvc) |
| **Native Extensions** | PyO3, Rust `tavro-python` crate (Memory vector indexing & rate limiting) |

---

## 📂 Project Structure

```
TAVRO-MAIN/
├── assets/                     # Logos, branding icons, and demo reels
├── configs/                    # Default and preset agent configurations (TOML / YAML)
│   └── tavro/                  # Preset configurations (chat-simple, code-assistant, etc.)
├── deploy/                     # Dockerfiles, launchd, and systemd service descriptors
├── desktop/                    # Desktop webview wrappers and Tauri descriptors
├── docs/                       # Architectural documentation, user guides, and diagnosis logs
├── frontend/                   # Modern React 19 web application
│   ├── src/                    # Components, state stores, API clients, and UI pages
│   ├── vite.config.ts          # Vite configuration with PWA and reverse proxying
│   └── package.json            # Node.js dependencies and script entries
├── rust/                       # Native Rust crates (tavro-python PyO3 bindings)
├── src/tavro/                  # Main Python package source code
│   ├── agents/                 # Autonomous agent architectures (ReAct, CodeAct, OpenHands)
│   ├── cli/                    # CLI tool commands (serve, doctor, pull, config)
│   ├── core/                   # Configuration loader, event bus, and credentials
│   ├── engine/                 # Inference engines (Ollama, MultiEngine, Cloud, AFM)
│   ├── memory/                 # Memory stores, indexing engines, and retrieval
│   ├── security/               # Capability policy enforcement and guardrails
│   ├── server/                 # FastAPI routes, middleware, and SSE bridges
│   └── tools/                  # Built-in tool integrations (shell, python, web search, MCP)
├── tests/                      # Pytest unit and integration test suites
├── pyproject.toml              # Python project metadata and dependencies
└── uv.lock                     # Deterministic dependency lockfile
```

---

## 💻 Windows 11 ARM64 & Snapdragon X Notes

Tavro is fully optimized for Windows 11 running on ARM64 processors (such as Qualcomm Snapdragon X):

1. **Serving Python Interpreter:**
   - Run backend services with **x64 CPython 3.12** under Windows x64 emulation (e.g. at `venv\runtime\Scripts\python.exe`). This provides access to prebuilt wheels (`numpy`, `pyarrow`, `scipy`, `ctranslate2`) without requiring custom ARM64 compilation.
2. **Native ARM64 Ollama Runtime:**
   - Ollama provides a native Windows ARM64 binary located at `%LOCALAPPDATA%\Programs\Ollama\ollama.exe`. It executes GGUF inference directly on Snapdragon X CPU/NPU cores at high throughput (~1040+ prompt tokens/sec).
3. **Application Control (WDAC / AppLocker) Policies:**
   - On managed Windows machines where Code Integrity or AppLocker blocks unsigned build executables (`build_script_build.exe`, OS error 4551), Tavro's fallback layer protects uptime and reports actionable status via `/v1/memory/stats`.
4. **WASM-Powered Production Bundling:**
   - The Vite build configuration includes `@rollup/wasm-node` fallback, allowing full client bundling and Service Worker generation without requiring unwhitelisted native `.node` DLLs.

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- **Git:** Version 2.40 or later
- **Python:** Version 3.10, 3.11, or 3.12 (CPython x64 recommended on Windows ARM64)
- **Node.js:** Version 22.0 or later with npm 11+
- **Ollama:** Download and install from [ollama.com](https://ollama.com/download)

### 2. Clone the Repository
```bash
git clone https://github.com/dineshreddy0204/TAVRO-MAIN.git
cd TAVRO-MAIN
```

### 3. Backend Setup
Create and populate a virtual environment with the required dependencies:
```bash
# Windows (PowerShell)
python -m venv venv\runtime
.\venv\runtime\Scripts\Activate.ps1
pip install -e .

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

### 4. Frontend Setup
```bash
cd frontend
npm install
npm run build
cd ..
```

---

## ⚡ Running Tavro

### Step 1: Start Ollama Runtime
Launch Ollama in the background:
```powershell
# Windows
ollama serve

# Linux / macOS
systemctl start ollama # or 'ollama serve'
```
Verify the daemon is responsive:
```bash
curl http://127.0.0.1:11434/api/tags
```

### Step 2: Start the Backend API Server
```powershell
# Using the serving virtual environment:
.\venv\runtime\Scripts\python.exe -m tavro.cli serve --host 127.0.0.1 --port 8000 --engine ollama --model qwen3.5:4b
```
The server binds to `http://127.0.0.1:8000`. Test server health:
```bash
curl http://127.0.0.1:8000/v1/info
```

### Step 3: Start the Web UI
In a separate terminal:
```powershell
cd frontend
npm run dev -- --host 127.0.0.1 --port 5173
```
Open **[http://127.0.0.1:5173](http://127.0.0.1:5173)** in your web browser.

---

## 🧪 Testing

Run both backend and frontend test suites to verify system integrity:

```powershell
# Run backend model management tests:
python -m pytest tests/server/test_model_management.py -v

# Run frontend unit & component tests:
npm --prefix frontend test
```

---

## ⚙️ Configuration Reference

Tavro supports command-line parameters and file-based configuration (`configs/tavro/config.toml`):

| Flag | Short | Default | Description |
|---|---|---|---|
| `--host` | | `127.0.0.1` | Network interface address to bind |
| `--port` | | `8000` | Port for the REST API server |
| `--engine` | `-e` | `ollama` | Active inference provider (`ollama`, `multi`, `nim`, `vllm`) |
| `--model` | `-m` | `qwen3.5:4b` | Default served model tag |
| `--agent` | `-a` | `orchestrator` | Default chat agent architecture (`orchestrator`, `react`, `simple`) |

---

## 🔒 Known Limitations & Enterprise Notes

- **Native Rust Memory Extension (`tavro_rust`):**
  - High-performance vector indexing requires compiling `rust/crates/tavro-python` with `rustc >= 1.89` (`x86_64-pc-windows-msvc`).
  - On enterprise systems with strict Application Control (WDAC / AppLocker), user-space build scripts may be prevented from executing. An administrator must whitelist build scripts or provide a prebuilt `.whl` for `cp312-win_amd64`.
- **Model Downloads:**
  - Pulling models directly from the web interface requires a reachable local Ollama instance on port 11434.

---

## 👤 Author & Maintainer

**PALLEM DINESH KUMAR REDDY**
- **GitHub:** [@dineshreddy0204](https://github.com/dineshreddy0204)
- **Repository:** [https://github.com/dineshreddy0204/TAVRO-MAIN](https://github.com/dineshreddy0204/TAVRO-MAIN)

---

## 📄 License

This project is licensed under the **Apache License 2.0** — Copyright © 2026 **PALLEM DINESH KUMAR REDDY**. See the [LICENSE](LICENSE) file for complete terms.
