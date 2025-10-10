# Role Assignment Guide

Clear roles prevent duplicated effort, dropped tasks, unequal workload, and last‑minute scrambles. Good roles enable parallel work streams, clear accountability, efficient skill utilization, and better coordination.

## Important Principles

1. **Roles ≠ Silos** – Everyone should understand the whole system. Roles define accountability, not exclusive ownership.
2. **Roles Can Evolve** – Start with Week 2 assignments, but adapt as you learn more about the project and each other's strengths.
3. **Balance Specialization and Cross‑Training** – Specialists are efficient, but single points of failure are risky. Aim for T‑shaped team members: deep in one area, broad awareness across all.
4. **Consider Learning Goals** – Pick roles that help you learn what you want to learn, not just what you're already good at.

## Common Role Configurations

### For a Team of 2

**Option A: Frontend/Backend Split**

- **Person 1:** Frontend + UX + some backend integration
- **Person 2:** Backend + AI integration + some frontend work

**Option B: Feature‑Based Split**

- **Person 1:** Core AI pipeline (prompts, RAG, evaluation)
- **Person 2:** Application layer (API, UI, deployment)

**Option C: Skill‑Based Split**

- **Person 1:** AI/ML specialist (model selection, prompts, eval)
- **Person 2:** Full‑stack engineer (end‑to‑end implementation)

**Shared Always:** Testing and QA; documentation; user research; project management; demo preparation.

### For a Team of 3

**Option A: Frontend / Backend / AI Split**

- **Person 1:** Frontend lead – UI components, UX design, client‑side integration.
- **Person 2:** Backend lead – API design, database, deployment, infrastructure.
- **Person 3:** AI lead – Model integration, prompt engineering, RAG/embedding pipeline, evaluation.

**Option B: Application / AI / DevOps Split**

- **Person 1:** Application lead – Full‑stack development, UI/UX, user flows.
- **Person 2:** AI lead – Model selection, prompt engineering, evaluation.
- **Person 3:** Platform lead – CI/CD, monitoring, performance optimization, security.

**Option C: Feature‑Based Split** (for complex projects)

- **Person 1:** Feature Area 1 (e.g., Query & Retrieval)
- **Person 2:** Feature Area 2 (e.g., Generation & Response)
- **Person 3:** Feature Area 3 (e.g., Evaluation & Analytics)

**Shared Always:** Architecture decisions; code reviews; documentation; user testing; demo preparation.

## Role Responsibilities Breakdown

### Frontend Lead

**Primary:** UI component development; user experience design; client‑side state management; responsive design; accessibility.

**Secondary:** API integration (with backend lead); user testing facilitation; frontend testing (unit + integration).

**Skills Needed:** React/Next.js or similar framework; CSS/Tailwind; HTTP/REST basics; basic state management.

**Learning Opportunities:** Advanced UX patterns; real‑time streaming UIs; error handling and loading states; component architecture.

### Backend Lead

**Primary:** API design and implementation; database schema design; authentication/authorization; server‑side logic; deployment.

**Secondary:** AI service integration (with AI lead); performance optimization; monitoring and logging; security (secrets, rate limiting).

**Skills Needed:** FastAPI/Flask or Express; database management (SQL/NoSQL); API design principles; basic DevOps.

**Learning Opportunities:** Streaming APIs; async programming; load testing; production best practices.

### AI/ML Lead

**Primary:** Model selection and evaluation; prompt engineering and optimization; RAG/embedding pipeline; AI cost and latency optimization; evaluation framework.

**Secondary:** Backend integration (with backend lead); data preparation and cleaning; safety and bias testing; documentation of AI decisions.

**Skills Needed:** API usage (OpenAI, Anthropic, etc.); prompt engineering; understanding of LLM limitations; basic eval metrics.

**Learning Opportunities:** Advanced RAG techniques; multi‑model orchestration; structured outputs; red teaming.

### DevOps/Platform Lead (for teams of 3)

**Primary:** CI/CD setup; deployment automation; monitoring and alerting; performance optimization; security hardening.

**Secondary:** Backend support; cost optimization; documentation; troubleshooting production issues.

**Skills Needed:** Git/GitHub Actions; cloud platforms (Vercel, Render, etc.); basic Docker/containerization; monitoring tools.

**Learning Opportunities:** Production‑grade deployment; observability; incident response; infrastructure as code.

### Project Manager / Coordinator (Rotating Role)

This can rotate weekly or be shared. It's not a full‑time role for a 2–3 person team.

**Responsibilities:**
- Schedule meetings
- Manage the backlog
- Track progress toward milestones
- Facilitate team decisions
- Update project documentation
- Communicate with instructor

**Time Commitment:** 2–3 hours/week

**Who Should Do This:** Rotate weekly; or person with lightest technical load that week; or whoever is best at organization.

## Picking Your Roles (Team Exercise)

### Step 1: Self‑Assessment (10 min, individual)

Each team member answers:

1. What are you strongest at? (Frontend development, backend development, AI/ML integration, DevOps/infrastructure, UX design, testing and QA, documentation, project management)
2. What do you want to learn?
3. What do you NOT want to do? (Be honest!)
4. Time availability this semester (~8/10/12+ hours per week)

### Step 2: Team Discussion (20 min)

Share your answers and discuss:

- Who has overlapping strengths? (Good for pairing)
- Who has complementary skills? (Good for division)
- Are there gaps in the team? (Need to learn together)
- Does anyone have a strong preference?
- Who wants to stretch vs. play to strengths?

Constraints:
- Must cover all critical areas (frontend, backend, AI)
- Workload should feel roughly equal
- Everyone should learn something new
- No single points of failure

### Step 3: Draft Assignments (10 min)

Propose initial roles:

- **[Name]** – [Primary role] – [Top 3 responsibilities]
- **[Name]** – [Primary role] – [Top 3 responsibilities]
- **[Name]** – [Primary role] – [Top 3 responsibilities] (if 3‑person team)

Test against scenarios:
- "If we need to fix a bug in the prompt system, who does it?" → [Name]
- "If the frontend is broken, who fixes it?" → [Name]
- "If we need to deploy, who does it?" → [Name]
- "If someone is sick for a week, can the others cover?" → [Check]

## Sample Role Assignments

### Example 1: Two‑Person Team (Balanced Skills)

**Team:** Alex (full‑stack) + Jordan (ML background)

**Alex – Application Lead**
- Primary: Frontend + Backend API
- Secondary: Deployment, user testing
- Learning: RAG integration, streaming UIs

**Jordan – AI Lead**
- Primary: Model integration, prompt engineering, evaluation
- Secondary: Backend logic, data pipeline
- Learning: Web APIs, FastAPI, production ML

Shared: Architecture decisions (both in all meetings); code reviews; documentation; user testing; demo preparation.

### Example 2: Two‑Person Team (Both New to AI)

**Team:** Sam (frontend focus) + Taylor (backend focus)

**Sam – Frontend Lead**
- Primary: UI/UX, React components
- Secondary: User research, frontend testing
- Learning: AI integration, prompt design

**Taylor – Backend + AI Lead**
- Primary: API, database, AI service integration
- Secondary: Deployment, monitoring
- Learning: Prompt engineering, RAG, LLM evaluation

Shared: Both learn AI concepts together; pair programming sessions for AI integration; weekly knowledge sharing (Sam teaches React, Taylor teaches FastAPI).

### Example 3: Three‑Person Team (Diverse Skills)

**Team:** Riley (frontend), Casey (backend), Morgan (AI researcher)

**Riley – Frontend Lead**
- Primary: Full UI/UX, all React components
- Secondary: User testing, client‑side caching
- Learning: Streaming response handling, real‑time updates

**Casey – Backend + Platform Lead**
- Primary: API, database, deployment, CI/CD
- Secondary: Performance, monitoring, security
- Learning: Async streaming APIs, production observability

**Morgan – AI + Evaluation Lead**
- Primary: Model selection, prompts, RAG, evaluation framework
- Secondary: Data pipeline, safety testing
- Learning: Production ML, cost optimization, API design

Shared: Weekly sync on architecture; cross‑team pairing (Riley pairs with Casey on API integration, etc.); demo preparation.

## Workload Distribution Guidelines

### How to Keep Things Fair

**Track Contributions:**
- GitHub commits (but also review PRs, docs, meetings)
- Task completion in project board
- Weekly standup reports
- Peer evaluations (mid‑term and final)

**Rebalance When Needed:**
- If someone is overloaded, redistribute tasks
- If someone finishes early, they pick up new work
- Adjust roles at Week 6 if needed

**Expected Time Commitment:**

Total project time: ~12 hours/week/person. This includes coding, meetings, documentation, testing, learning.

**Red Flags:**

- One person has 3× more commits than others
- Someone consistently "doesn't have time" for tasks
- Tasks are late because one person is overwhelmed
- Someone feels their role is "done" by Week 8

## Decision‑Making by Role

| Decision Type | Who Decides? | Who Must Be Consulted? |
|--------------|-------------|------------------------|
| UI component structure | Frontend lead | Full team for major changes |
| API endpoints | Backend lead | Frontend + AI leads |
| Model selection | AI lead | Full team |
| Database schema | Backend lead | AI lead |
| Deployment platform | DevOps lead | Backend lead |
| Prompt templates | AI lead | Full team |

General rule:

- Individual technical decisions → Lead for that area
- Cross‑cutting concerns → Full team discussion
- Project scope/direction → Consensus

## Role Transition Plan

### Week 2–4: Initial Roles

- Follow your assigned roles
- Focus on learning your area
- Over‑communicate and ask for help

### Week 5–6: First Checkpoint

- Discuss what's working and what's not
- Rebalance if needed
- Identify gaps and assign learning

### Week 7–12: Mature Roles

- More autonomy in your area
- Cross‑training on other areas
- Preparing for handoff/demo

### Week 13–15: All Hands

- Everyone works on polish and demo prep
- Roles blur as you focus on shipping
- Final push together

## When Roles Don't Work

### Problem: Skills Mismatch

**Symptom:** "I can't do my assigned role effectively."

**Solutions:**
- Swap roles if another teammate is better suited
- Pair program to learn faster
- Reduce scope in that area
- Ask instructor for resources/help

### Problem: Unequal Workload

**Symptom:** One person doing 60% of work.

**Solutions:**
- Review task breakdown – is it truly equal?
- Check if one person is working too slowly (pair to help)
- Check if one person is taking on too much (redistribute)
- Use GitHub insights to quantify contributions
- Adjust future milestones to rebalance

### Problem: Personality Conflicts

**Symptom:** Two people can't work together.

**Solutions:**
- Separate their work streams (frontend vs. backend)
- Use async communication (PRs + written reviews)
- Bring in third teammate as mediator
- Escalate to instructor if it impacts project

### Problem: Disappearing Teammate

**Symptom:** Someone stops responding or contributing.

**Solutions:**
1. **Week 1 of silence:** Friendly check‑in via multiple channels
2. **Week 2 of silence:** Formal team meeting, document the issue
3. **Week 3 of silence:** Contact instructor, redistribute work
4. Document everything for peer evaluations

## Documenting Your Roles

In your Team Contract, include a Roles & Responsibilities section:

```markdown
### [Team Member 1] – [Role Title]
**Primary Responsibilities:**
- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

**Accountable For:**
- [Deliverable 1]
- [Deliverable 2]

**Learning Goals:**
- [Skill 1]
- [Skill 2]

### [Team Member 2] – [Role Title]
...

### Shared Responsibilities
- Code reviews
- Documentation
- User testing
- Demo preparation
```

## Role‑Based Checklists

### Frontend Lead – Weekly Checklist

- UI components match design
- Responsive on mobile
- Error states handled
- Loading states smooth
- Accessibility basics covered
- Frontend tests passing
- Updated UI documentation

### Backend Lead – Weekly Checklist

- API endpoints documented
- Error handling in place
- Database migrations tested
- Secrets not in code
- Rate limiting implemented
- Backend tests passing
- Deployment working

### AI Lead – Weekly Checklist

- Prompts version controlled
- Cost tracking updated
- Latency logged
- Eval metrics calculated
- Model fallbacks tested
- Safety checks in place
- AI decisions documented

## Final Tips

1. **Over‑communicate early** – Better to over‑share than assume; use async updates (daily standups in Slack); document decisions in GitHub.
2. **Respect each other's expertise** – Trust your frontend lead on UX decisions, AI lead on model selection; but ask questions and learn from each other.
3. **Pairing > Solo work** – Pair for complex tasks; pair for knowledge transfer; pair when stuck.
4. **Rotate unglamorous work** – Documentation; bug fixes; testing; everyone takes a turn.
5. **Celebrate each other's wins** – Shout out good work in team chat; tag people in README for their contributions; acknowledge effort in peer evals.

## Mid‑Semester Check

At Week 6, discuss:

- Are our roles still working?
- Is workload balanced?
- Is anyone blocked by lack of skills?
- Should we swap or share any responsibilities?
- Are we communicating effectively?
- Are decisions getting made efficiently?

Make adjustments as needed. Document changes in your Team Contract.

Remember: Roles are tools to help you succeed, not rigid boxes. Adapt as you learn.

Questions? Discuss in your team, or ask during office hours.