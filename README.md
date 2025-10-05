# AI-POWERED-SOFTWARE-DEV

This repository contains course materials for the AI-Powered Applications course at KIU. The course teaches how to build AI powered applications using large language models and retrieval‑augmented generation.

## Structure

- course‑pack/labs – Lab materials and starter code.
- .devcontainer – Codespaces and local dev container settings.
- .github/workflows – Continuous integration workflow.
- package.json – Node.js dependencies and scripts.
- requirements.txt – Python dependencies.

## Getting Started

To run the Week 1 builder sprint app:

1. Install Node.js (version 18+) and Python (version 3.9+).
2. Clone this repository to your machine.
3. Open a terminal and navigate to `course‑pack/labs/week‑01/builder‑sprint‑app`.
4. Copy `.env.example` to `.env` and paste your API key for Gemini.
5. From the repository root run `npm install`.
6. Run `pip install -r requirements.txt` to install Python packages.
7. Start a local server with `python -m http.server 8000` or `npx http-server -p 8000`.
8. Open a browser to `http://localhost:8000` and test the app.

## Labs

The Week 1 and 2 lab guide is in `course‑pack/labs/week‑01‑02/LAB.md`. It covers team formation, pre‑lab setup, the builder sprint, and assignments like streaming responses, cost calculation, and retry logic.

Check the labs directory for future assignments and examples.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
