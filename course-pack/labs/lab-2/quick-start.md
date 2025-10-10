# Week 2 Quick Start Guide

Missed Lab? Start Here. This condensed guide gives you the essentials for Week 2 of Building AI‑Powered Applications.

## TL;DR – What You Need to Do This Week

**Due:** End of Week 2  
**Deliverable:** GitHub repository with capstone proposal  
**Points:** 10

### 5 Critical Steps:

1. Connect with your team
2. Create GitHub repository
3. Write team contract
4. Draft capstone proposal
5. Submit repo URL

**Time Estimate:** 8–12 hours total (spread across the week)

## Step 1: Find Your Team (15 min)

### What to Do

- Check course announcement for team assignments
- Contact teammates via email/Discord/Slack
- Exchange contact information
- Schedule first team meeting

### Team Meeting #1 Agenda

```
1. Introductions (5 min)
   - Name, year, what you want to learn
2. Logistics (10 min)
   - Exchange contact info
   - Agree on communication channel (Discord/Slack/WhatsApp)
   - Set regular meeting times (suggest: 2× per week)
3. Initial Ideas (20 min)
   - Each person shares 1–2 project ideas
   - Don't judge yet, just brainstorm
4. Action Items (5 min)
   - Who creates the GitHub repo?
   - When's the next meeting?
   - Who drafts which proposal sections?
```

**Can't reach a teammate?** Email instructor immediately: Zeshan.ahmad@kiu.edu.ge

## Step 2: Set Up GitHub Repository (30 min)

### Quick Setup

**One person does this:**

1. **Create repo on GitHub**
   - Go to github.com
   - Click "+" → "New repository"
   - Name: `your-project-name`
   - Public or Private (your choice)
   - Initialize with README
   - Add .gitignore: Python (or Node)
   - Click "Create repository"

2. **Add team members**
   - Settings → Collaborators
   - Add each teammate (they need GitHub accounts)
   - Add instructor: [instructor‑github‑username]
   - Set access: Write for team, Read for instructor

3. **Create folder structure**
   ```bash
   mkdir docs src tests data
   touch docs/.gitkeep src/.gitkeep tests/.gitkeep
   touch .env.example requirements.txt
   ```

4. **Update README**
   ```markdown
   # Project Title
   Team: [Names]
   Course: Building AI‑Powered Applications
   About: [Brief description]
   Status:
   - [x] Team formed
   - [ ] Proposal complete
   - [ ] MVP shipped
   ```

**Everyone else:**
   - Accept the GitHub invitation
   - Clone the repo: `git clone [repo-url]`
   - Test: Make a small change, commit, push

Need more help? See [GitHub Setup Guide](./guides/github-setup-guide.md)

## Step 3: Draft Team Contract (1 hour)

### Must‑Have Sections

Use the template at `./templates/team-contract-template.md`.

Don't just fill in blanks – actually discuss:

1. **Roles** (Who does what?)
   - Frontend lead
   - Backend lead
   - AI integration lead
   - Project manager (rotating?)

2. **Meetings** (When and where?)
   - Days and times (be specific!)
   - Duration (e.g., 1 hour)
   - Location (in‑person or Zoom link)

3. **Communication** (How do we stay in touch?)
   - Primary channel (Discord/Slack/WhatsApp)
   - Response time expectations (e.g., within 24 hours)
   - Emergency contact method

4. **Decisions** (How do we decide?)
   - Small stuff: Assigned person decides
   - Big stuff: Vote or consensus
   - Tie‑breaker: Instructor

5. **Conflicts** (What if things go wrong?)
   - Step 1: Talk directly
   - Step 2: Team meeting
   - Step 3: Instructor mediation

Save as `docs/team-contract.md`. All members sign (commit approval). Don't skip this!

## Step 4: Write Capstone Proposal (6–8 hours)

### The 8 Required Sections

Use the template at `./templates/capstone-proposal-template.md`.

1. **Problem Statement (30 min)** – 2–3 paragraphs answering:
   - Who has this problem? (Specific user group)
   - What's the problem? (Specific task/pain point)
   - How do they solve it now? (And why that fails)
   - Why AI? (What AI specifically helps)

   Good: "CS students debugging recursion spend 30 min per error because they can't visualize call stacks"

2. **Target Users (20 min)** – Describe your users:
   - Age, role, context
   - Technical level
   - Main needs and pain points
   - How many people have this problem?

3. **Success Criteria (30 min)** – Define 5+ measurable metrics:
   - Product: Time saved, accuracy, user satisfaction
   - Technical: Latency, cost, uptime
   - Learning: Skills each person wants to gain

4. **Technical Architecture (2 hours)**
   - System overview: 1–2 paragraphs describing how it works
   - Architecture diagram
   - Tech stack (frontend, backend, AI services, database, hosting)
   - AI details: Which model and why, prompt structure, retrieval strategy

5. **Risk Assessment (1 hour)** – List 5+ risks with likelihood, impact, and two or more mitigation strategies each. Cover technical, product, team, and safety/ethical risks.

6. **Research Plan (45 min)** – What you need to learn, experiments you'll run, timeline, resources to review.

7. **User Study Plan (1 hour)** – If you're testing with users: how many participants, how you'll recruit them, what you'll ask them to do, how you'll protect their privacy, consent form.

8. **Timeline (30 min)** – Weekly breakdown (Weeks 3–15), major milestones, dependencies, backup plan.

Check the quality checklist: All sections complete (not just headings), problem is specific and scoped, architecture includes diagram, success criteria are measurable, risks have mitigation strategies, timeline is realistic, no spelling/grammar errors, professional formatting.

Save as `docs/capstone-proposal.md`.

## Step 5: Final Deliverables (1 hour)

### Create These Files

#### `docs/setup.md`

Instructions for setting up development environment:

```markdown
# Setup Instructions

## Prerequisites
- Python 3.11+ (or Node.js 18+)
- Git

## Installation
1. Clone the repository: `git clone [repo-url]`
2. Navigate to repo: `cd project-name`
3. Create virtual environment: `python -m venv venv` (or `npm install` for Node)
4. Activate environment and install dependencies
5. Copy `.env.example` to `.env` and add keys
6. Run the app (instructions coming in Week 3)

## Troubleshooting
Document common issues and solutions here.
```

#### `.env.example`

Example environment variables (no real keys!).

#### `.gitignore`

Already created if you chose Python/Node template. Make sure it includes `.env`, `node_modules/`, `__pycache__/`, etc.

### Create GitHub Issues (30 min)

Create 10–15 issues for your backlog. Each issue should have a clear title, description, acceptance criteria, label, milestone, and (optional) assignee.

## Step 6: Submit (5 min)

### Pre‑Submission Checklist

Repository must have:

- README.md (project info, team names)
- docs/team-contract.md (complete, signed)
- docs/capstone-proposal.md (all 8 sections, 6–8 pages)
- docs/setup.md (dev environment instructions)
- docs/irb-checklist.md (if doing user research)
- .gitignore (configured)
- .env.example (no real secrets!)
- 10–15 GitHub Issues
- All team members added as collaborators
- Instructor added with read access

### Submit

**Where:** Course submission system  
**What:** GitHub repository URL

Format:
```
Repository: https://github.com/username/project-name
Team: [Name 1], [Name 2], [Name 3]
Project: [Project Title]
```

## Time Management

### Suggested Schedule

**Day 1 (Lab Day):**
- Find team (15 min)
- Create GitHub repo (30 min)
- Start team contract (30 min)
- Brainstorm project ideas (30 min)

**Day 2:**
- Team meeting: finalize contract (1 hour)
- Team meeting: pick project idea (1 hour)
- Individual: draft assigned proposal sections (2 hours)

**Day 3:**
- Team meeting: review all sections together (1 hour)
- Individual: polish your sections (1 hour)

**Day 4:**
- Create GitHub issues (30 min)
- Write setup.md (30 min)
- Final proofreading (30 min)

**Day 5 (Due Date):**
- Last check (everything in repo?) (15 min)
- Submit! (5 min)

Total: ~10 hours over 5 days

## Common Mistakes to Avoid

### "We'll figure it out later"
Vague proposal, unclear scope → Fix: Be specific now. Details matter.

### "Let's build everything"
Scope too large for 13 weeks → Fix: Pick the smallest useful version. You can always expand.

### "AI is cool, let's use it"
Solution looking for problem → Fix: Start with the problem, then decide if AI helps.

### "We don't need a contract"
Conflict later when roles unclear → Fix: Spend the hour now. Save yourself pain later.

### "I'll do it all the night before"
Poor quality, stressed team → Fix: Start early, work steadily, review together.

## Emergency Contacts

### Can't Reach Teammates?
Email instructor immediately: Zeshan.ahmad@kiu.edu.ge

### Technical Issues?
- GitHub problems: See [GitHub Setup Guide](./guides/github-setup-guide.md)
- Git stuck: Delete local folder, re‑clone, start fresh
- Can't push: Check you're added as collaborator

### Conceptual Questions?
- Post in course forum (fastest response)
- Office hours: See Week 1 announcement
- Email: Zeshan.ahmad@kiu.edu.ge (24hr response weekdays)

## Resources

**Templates:**
- [Team Contract](./templates/team-contract-template.md)
- [Capstone Proposal](./templates/capstone-proposal-template.md)
- [Repo Structure](./templates/repo-structure.md)

**Guides:**
- [GitHub Setup](./guides/github-setup-guide.md)
- [Problem Statement](./guides/problem-statement-guide.md)
- [Role Assignment](./guides/role-assignment-guide.md)
- [IRB/Ethics](./guides/irb-light-guide.md)

**Full Details:**
- [Main Lab README](./README.md)
- [Homework Assignment](./homework-assignment.md)

## Quick Wins

Start with these to build momentum:

**10 minutes:** Email your team, accept GitHub invitation, clone the repo

**30 minutes:** Read one example proposal, fill out role section of team contract, list 3 project ideas

**1 hour:** Complete team contract, draft problem statement, create GitHub issues

**2 hours:** Write architecture section, create diagram, draft risk assessment

Small steps → Big progress!

## Final Tips

1. **Start Now** – Don't wait. Even 30 minutes today helps.
2. **Communicate** – Over‑communicate with your team. Use your chosen channel actively.
3. **Be Specific** – Every time you write something vague, ask yourself: "Can I be more specific?"
4. **Ask for Help** – Stuck? Confused? Ask! That's what office hours and forums are for.
5. **Have Fun** – You're building something meaningful. Enjoy the process!

## What's Next?

**Week 3:**
- You'll receive proposal feedback
- Start implementing your first features
- Labs focus on multimodal AI integration

**Week 4:**
- Design Review milestone
- Refine architecture
- Update backlog based on learnings

**Looking Ahead:** Week 5: Quiz on retrieval patterns; Week 11: Safety & evaluation audit; Week 15: Final demo day.

You've got this!