# code-review-agent

An AI-powered reviewer for GitHub pull requests. Install it as a GitHub App, open a PR, and it posts a review with inline comments covering static analysis, security, style and architecture.

> **Status:** in active development. See the roadmap below.

## How it works

```
GitHub ──webhook──▶ gateway ──▶ webhook ──queue──▶ orchestrator ──▶ reviewer ──▶ PR comments
                   (verify     (store PR,          (fetch diff,     (post
                    signature)  enqueue job)        run AI agents)   review)

                         on merge ──queue──▶ learner (store recurring patterns)
```

The orchestrator runs four review agents in parallel and merges their findings:

| Agent | Looks for |
|---|---|
| Static analysis | complexity, unused variables, poor naming |
| Security | OWASP Top 10, hardcoded secrets, injection risks |
| Style | formatting, readability, team-specific patterns |
| Architecture | separation of concerns, error handling, dependency use |

## Tech stack

- **Services:** Python 3.11, FastAPI, Celery, Redis
- **AI:** LangGraph, OpenAI, LangFuse tracing
- **Data:** PostgreSQL, Alembic
- **Infra:** Docker, Kubernetes (EKS), Terraform, GitHub Actions
- **Observability:** Prometheus, Grafana
- **Testing:** Playwright end-to-end tests

## Repository layout

```
services/        one folder per microservice
db/              database migrations
infra/           terraform and kubernetes manifests
monitoring/      prometheus and grafana config
scripts/         maintenance and evaluation jobs
docs/            setup guide and architecture
```

## Roadmap

- [x] Repository setup and CI checks
- [ ] Database schema
- [ ] Gateway, webhook, orchestrator, reviewer and learner services
- [ ] Local development stack (Docker Compose)
- [ ] End-to-end tests
- [ ] AWS infrastructure and deployment pipeline
- [ ] Monitoring and setup guide

## Author

**Dharmil Shah**
[GitHub](https://github.com/shahdharmil11) · [LinkedIn](https://www.linkedin.com/in/dharmilshah1416) · sdharmil1416@gmail.com

## License

[MIT](LICENSE)
