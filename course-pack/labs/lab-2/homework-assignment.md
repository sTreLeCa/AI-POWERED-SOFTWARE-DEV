# Week 2 Homework Assignment

**Building AI‑Powered Applications | Due: End of Week 2**

This week you're transitioning from individual work to team‑based capstone development. Your homework focuses on establishing team infrastructure, defining your project, and submitting your first major milestone.

**Points:** 10 (Capstone Proposal component)  
**Due Date:** [Check course calendar]  
**Submission:** GitHub repository URL via course submission system

## What You Need to Do

### Core Deliverables (Required)

You must submit **ALL** of the following in your team GitHub repository:

#### 1. Team GitHub Repository Setup

- [ ] Repository created and properly structured
- [ ] All team members added as collaborators
- [ ] Instructor added with read access
- [ ] README.md updated with project info
- [ ] .gitignore configured properly
- [ ] .env.example created (no real secrets!)

**Where to put it:** Root of your repository

#### 2. Team Contract

- [ ] All sections completed (not just template)
- [ ] Roles clearly assigned
- [ ] Communication plan defined
- [ ] Conflict resolution process established
- [ ] All team members have "signed" (committed approval)

**Where to put it:** `docs/team-contract.md`

**Template:** [Use the team contract template](./templates/team-contract-template.md)

#### 3. Capstone Proposal

- [ ] Problem statement (clear, specific, AI‑appropriate)
- [ ] Target users identified
- [ ] Success criteria defined (measurable!)
- [ ] Technical architecture outlined
- [ ] Architecture diagram included
- [ ] Risk assessment completed
- [ ] Research plan detailed
- [ ] User study plan (with IRB checklist if needed)
- [ ] All 8 sections complete and thorough

**Where to put it:** `docs/capstone-proposal.md`

**Template:** [Use the capstone proposal template](./templates/capstone-proposal-template.md)

#### 4. Development Environment Setup

- [ ] Setup instructions documented
- [ ] Each team member can clone and run locally
- [ ] Dependencies listed (requirements.txt or package.json)
- [ ] Environment variables documented in .env.example

**Where to put it:** `docs/setup.md`

#### 5. IRB Light Checklist (if applicable)

- [ ] Completed if you're doing user testing
- [ ] Consent form adapted from template
- [ ] Privacy and data protection plan

**Where to put it:** `docs/irb-checklist.md`

**When required:** If you're testing with users, interviewing people, or collecting any human data

**Template:** [Use the IRB light guide](./guides/irb-light-guide.md)

#### 6. Initial Project Backlog

- [ ] 10–15 GitHub Issues created
- [ ] Issues labeled appropriately (setup, research, design, implementation)
- [ ] Issues assigned to weeks/milestones
- [ ] Clear acceptance criteria on each issue

**Where to put it:** Your GitHub Issues tab

### Optional (But Recommended)

#### 7. Architecture Diagram

Create a visual representation of your system architecture. Use draw.io, Excalidraw, Mermaid in markdown, Lucidchart, or even hand‑drawn and scanned.

**Where to put it:** `docs/architecture.png` (or include in your proposal)

## Detailed Requirements

### Repository Structure

Your repository must look like this:

```
your-project-name/
├── README.md                 # Project overview, team info
├── .gitignore                # Configured for your stack
├── .env.example              # Example environment variables
├── requirements.txt          # Python dependencies (or package.json)
├── docs/
│   ├── team-contract.md      # REQUIRED
│   ├── capstone-proposal.md  # REQUIRED
│   ├── setup.md              # REQUIRED
│   ├── irb-checklist.md      # If doing user research
│   └── architecture.png      # Optional but recommended
├── src/                      # Your source code (can be empty for now)
│   ├── backend/
│   ├── frontend/
│   └── scripts/
├── tests/                    # Test files
├── data/                     # Sample data only (no user data!)
└── .github/
    └── workflows/            # CI/CD (later)
```

### Team Contract Requirements

Your team contract must include:

**Team Information**

- All member names, emails, GitHub usernames
- Team name and project title

**Roles & Responsibilities**

- Specific roles for each person
- Clear accountability
- Shared responsibilities identified

**Communication Plan**

- Primary communication channel
- Expected response times
- Meeting schedule (days, times, duration)
- What to do if someone can't attend

**Decision‑Making Process**

- How routine decisions are made
- How major decisions are made
- What to do if you can't agree

**Conflict Resolution**

- Step‑by‑step process
- Agreed solutions for common issues

**Quality Standards**

- Code quality expectations
- Documentation standards
- Testing requirements

**Signatures**

- All team members have approved (either signed or committed approval)

### Capstone Proposal Requirements

Your proposal must include **all 8 sections**:

1. **Problem Statement** (2–3 paragraphs) – Specific problem you're solving, who has this problem, current solutions and their gaps, why AI is appropriate.
2. **Target Users** (1–2 paragraphs) – Who are they? What's their context? What are their specific needs and pain points? How many people have this problem?
3. **Success Criteria** (5 metrics minimum) – Product success metrics, technical success criteria, learning goals for each team member; must be specific and testable.
4. **Technical Architecture** (diagrams + description) – System overview, architecture diagram, technology stack, data flow explanation, AI integration details, third‑party services and APIs.
5. **Risk Assessment** (at least 5 risks) – Technical risks with mitigation strategies, product risks with mitigation strategies, team risks with mitigation strategies, safety & ethical risks with mitigation strategies; each risk must have likelihood, impact, and two or more mitigation strategies.
6. **Research Plan** – What you need to learn, experiments you'll run, timeline for learning, literature/resources you'll review.
7. **User Study Plan** – Number of participants and how you'll recruit them, testing protocol and timeline, data collection methods, privacy and consent process, IRB checklist (if applicable).
8. **Project Timeline** – Weekly breakdown (Weeks 3–15), major milestones highlighted, dependencies identified, backup plan for scope cuts.

**Quality Bar:** Well‑organized and professional; no spelling/grammar errors; specific, not vague; realistic and achievable; shows you've thought deeply about the project.

### Development Environment Requirements

Document in `docs/setup.md`:

**Prerequisites**

- Languages and versions (e.g., Python 3.11+)
- Tools needed (e.g., Git, npm, etc.)

**Installation Steps**

- How to clone the repo
- How to set up virtual environment
- How to install dependencies
- How to configure environment variables

**Running the Application**

- How to start the app (even if it's just "Hello World" for now)
- Expected output

**Troubleshooting**

- Common issues and solutions

Each team member should be able to follow these instructions and get the app running.

### Initial Backlog Requirements

Create **10–15 GitHub Issues** covering:

**Week 3–4 Tasks:**

- [ ] Set up backend API skeleton
- [ ] Set up frontend scaffold
- [ ] Integrate first AI API call
- [ ] Implement basic prompt template
- [ ] Create database schema (if needed)
- [ ] Set up vector store (if using RAG)

**Week 5–6 Tasks:**

- [ ] Implement core user flow
- [ ] Add retrieval/RAG (if applicable)
- [ ] Create evaluation golden set
- [ ] Conduct first user interview

**Week 7+ Tasks:**

- [ ] Add remaining features
- [ ] Conduct user testing
- [ ] Optimize performance
- [ ] Etc.

**Each Issue Should Have:** Descriptive title, clear description of what needs to be done, acceptance criteria (how you'll know it's done), estimated effort (S/M/L or hours), label (e.g., `setup`, `frontend`, `backend`, `ai`, `research`), assignee (can assign later if not sure yet), milestone (Week 3, Week 4, etc.)

## Submission Instructions

### Step 1: Finalize Your Repository

Make sure everything is committed and pushed:

```bash
git add .
git commit -m "docs: complete week 2 deliverables"
git push origin main
```

### Step 2: Verify Completeness

Go through this checklist:

- [ ] README.md has project title and team names
- [ ] `docs/team-contract.md` exists and is complete
- [ ] `docs/capstone-proposal.md` exists and is complete
- [ ] `docs/setup.md` exists with clear instructions
- [ ] `docs/irb-checklist.md` exists if doing user research
- [ ] .gitignore is configured
- [ ] .env.example exists (no real secrets!)
- [ ] 10–15 GitHub Issues created
- [ ] All team members have been added as collaborators
- [ ] Instructor has been added with read access
- [ ] Repository is either public or instructor has access

### Step 3: Test From Fresh Clone

One team member should:

```bash
# Clone in a new location
git clone [your-repo-url] test-clone
cd test-clone

# Follow your setup.md instructions
# Verify everything works
```

If your teammate can't get it running, fix your setup instructions!

### Step 4: Submit

**Where:** Course submission system (LMS/Canvas/etc.)

**What to submit:**
- Your GitHub repository URL
- Team member names
- Project title

**Format:**

```
Repository: https://github.com/username/project-name
Team: [Name 1], [Name 2], [Name 3]
Project: [Your Project Title]
```

## Grading Rubric (10 points total)

| Component                  | Points | What We're Looking For                                    |
|---------------------------|--------|-----------------------------------------------------------|
| **Problem Clarity**        | 2.0    | Clear, specific problem. Real users identified. Justifies why AI helps. |
| **Technical Feasibility**   | 2.0    | Realistic architecture. Appropriate tech stack. Achievable scope. Diagram included. |
| **Success Criteria**        | 1.0    | Specific, measurable metrics. Both product and technical criteria. |
| **Risk Assessment**         | 1.0    | Identifies key risks across technical, product, team, safety. Concrete mitigation strategies. |
| **Research & User Plan**    | 1.5    | Clear research plan. User study protocol. IRB completed if applicable. Timeline realistic. |
| **Team Contract**           | 1.5    | Complete, specific, thoughtful. Roles clear. Conflict resolution defined. All members signed. |
| **Presentation Quality**     | 1.0    | Professional formatting. Well‑organized. No typos. Complete repo structure. |

### Detailed Grading Criteria

#### Problem Clarity (2.0 points)

- **1.8–2.0:** Crystal clear problem, well‑defined users, strong justification for AI, scoped appropriately
- **1.5–1.7:** Clear problem, users identified, AI justified, but could be more specific
- **1.0–1.4:** Vague problem or unclear why AI is needed
- **0.5–0.9:** Problem is too broad or not well‑defined
- **0.0–0.4:** No clear problem statement

#### Technical Feasibility (2.0 points)

- **1.8–2.0:** Complete architecture with diagram, realistic tech choices, achievable in 13 weeks
- **1.5–1.7:** Good architecture, minor concerns about feasibility
- **1.0–1.4:** Incomplete architecture or overly ambitious scope
- **0.5–0.9:** Significant feasibility concerns
- **0.0–0.4:** Architecture is unrealistic or missing

#### Success Criteria (1.0 point)

- **0.9–1.0:** 5+ specific, measurable metrics covering product, technical, and learning goals
- **0.7–0.8:** Good metrics but some are vague or not measurable
- **0.5–0.6:** Some metrics present but mostly vague
- **0.3–0.4:** Minimal metrics, mostly qualitative
- **0.0–0.2:** No clear success criteria

#### Risk Assessment (1.0 point)

- **0.9–1.0:** 5+ risks identified with likelihood, impact, and 2+ mitigation strategies each
- **0.7–0.8:** Good risk coverage but missing some areas or mitigation strategies
- **0.5–0.6:** Some risks identified but incomplete analysis
- **0.3–0.4:** Minimal risk analysis
- **0.0–0.2:** No meaningful risk assessment

#### Research & User Plan (1.5 points)

- **1.3–1.5:** Detailed research plan, complete user study protocol, realistic timeline, IRB if needed
- **1.0–1.2:** Good plan but some gaps in detail or timeline
- **0.7–0.9:** Basic plan but missing key elements
- **0.4–0.6:** Minimal planning
- **0.0–0.3:** No clear research or user plan

#### Team Contract (1.5 points)

- **1.3–1.5:** Complete, specific, thoughtful contract. Roles clear. All sections addressed. Signed by all.
- **1.0–1.2:** Good contract but some sections are generic or incomplete
- **0.7–0.9:** Basic contract but missing important details
- **0.4–0.6:** Minimal effort, mostly just template
- **0.0–0.3:** Incomplete or not submitted

#### Presentation Quality (1.0 point)

- **0.9–1.0:** Professional, well‑organized, no errors, complete repo structure
- **0.7–0.8:** Good presentation with minor issues
- **0.5–0.6:** Some organizational issues or typos
- **0.3–0.4:** Multiple presentation issues
- **0.0–0.2:** Poor presentation or incomplete submission

### Common Mistakes to Avoid

#### Mistake 1: Vague Problem Statements
**Bad:** "Students need help with homework"  
**Good:** "CS students spend 30 minutes debugging recursion errors due to poor call stack visualization"

#### Mistake 2: Solutions Looking for Problems
**Bad:** "RAG is cool, let's use it for something"  
**Good:** "Students can't find relevant code examples, so we'll use RAG over documentation"

#### Mistake 3: Generic Team Contracts
**Bad:** Leaving template text like "[Add other shared responsibilities]"  
**Good:** Specific agreements like "Alex reviews all PRs within 24 hours"

#### Mistake 4: Overly Ambitious Scope
**Bad:** "We'll build a general‑purpose AI assistant for all subjects"  
**Good:** "We'll build a Python debugging tutor focused on recursion and loops"

#### Mistake 5: Missing Architecture Details
**Bad:** "We'll use OpenAI and a database"  
**Good:** "FastAPI backend with GPT‑4o, PostgreSQL with pgvector for embeddings, Next.js frontend"

#### Mistake 6: Unrealistic Success Criteria
**Bad:** "95% accuracy, <100ms latency, $0 cost"  
**Good:** "80% helpful ratings, <3s response time, <$0.10 per query"

#### Mistake 7: No Risk Mitigation
**Bad:** "Risk: API might go down"  
**Good:** "Risk: API downtime (Medium/High) → Mitigation: Add fallback model, implement retry logic, cache common responses"

#### Mistake 8: Committing Secrets
**Bad:** Pushing `.env` with real API keys  
**Good:** Only commit `.env.example` with fake keys, add `.env` to `.gitignore`

## Tips for Success

### 1. Start Early

- Don't wait until the night before
- Have 2–3 team meetings this week
- Get instructor feedback early (office hours!)

### 2. Be Specific

- "We'll use AI to help students" → Too vague
- "We'll use GPT‑4 to explain Python errors in plain English" → Specific!

### 3. Think Small

- You have 13 weeks, not 13 months
- "Do one thing well" beats "do five things poorly"
- You can always add features later

### 4. Validate Your Ideas

- Talk to 2–3 potential users before finalizing
- Ask: "Would you actually use this?"
- Adjust based on feedback

### 5. Test Your Setup Instructions

- Each team member should clone fresh and follow setup.md
- If it doesn't work for your teammate, it won't work for the grader

### 6. Use the Templates

- Don't start from scratch
- Templates ensure you don't miss required sections
- Adapt them to your project

### 7. Proofread Together

- Do a final team review before submitting
- Check for typos, broken links, missing sections
- Make sure it looks professional

## Getting Help

### During Class (Lab)
- Raise your hand
- Ask the instructor or TAs
- Discuss with other teams

### Outside Class
**Course Forum** (preferred) – Post questions publicly; others can benefit from answers; faster response from peers and instructor

**Office Hours** – See Week 1 announcement for schedule; book a slot if needed; bring specific questions

**Email** (for sensitive issues only) – Zeshan.ahmad@kiu.edu.ge; response within 24 hours (weekdays); include all team members in thread

## After Submission

### What Happens Next?

**Week 3:** Instructor reviews proposals; you receive feedback (within 5 business days); you may need to revise and resubmit if major issues; meanwhile, start building! (Week 3 labs begin)

**Week 4:** Design Review milestone; refine architecture based on what you've learned; update your backlog

**Looking Ahead:** Week 5: Quiz on retrieval and production patterns; Week 11: Safety and Evaluation Audit; Week 15: Final Demo Day

## Frequently Asked Questions

### "Can we change our project idea later?"
Yes, but the earlier the better. Major pivots after Week 6 are risky. Discuss with instructor first.

### "What if we can't agree on an idea?"
Use the decision‑making process in your team contract. If still stuck, each person proposes one idea and you vote. Instructor can be tiebreaker if needed.

### "How much detail is enough for the proposal?"
If someone unfamiliar with your project reads it, they should understand: what you're building, why it matters, how you'll build it, whether it's feasible. Aim for 6–8 pages for the proposal.

### "Do we need to code anything this week?"
Not required for submission, but recommended to set up a "Hello World" to verify your environment works. Week 3 labs will hit the ground running.

### "What if we don't know our tech stack yet?"
Make your best guess based on course materials and your team's skills. You can adjust in Week 3–4. Document your reasoning.

### "Can we use a project we started before this course?"
Only if:
1. It's been approved by the instructor
2. You're adding significant new AI features
3. All team members contributed equally
4. It meets all course requirements
Discuss with instructor during office hours.

### "What if our GitHub repo is private?"
That's fine! Just make sure:
1. All team members have access
2. Instructor has been added as collaborator with read access
3. You submit the URL (instructor can access)

### "One teammate isn't responding. What do we do?"
1. Try multiple channels (email, phone, social media)
2. Document your attempts
3. If no response by Day 3, contact instructor
4. Continue working as a smaller team if needed
5. This will be considered in peer evaluations

## Checklist: Ready to Submit?

Go through this before submitting:

**Repository Setup**
- [ ] Repo created and structured properly
- [ ] All team members added as collaborators
- [ ] Instructor added with read access
- [ ] README is updated with project info

**Required Files**
- [ ] `docs/team-contract.md` complete and signed
- [ ] `docs/capstone-proposal.md` complete (all 8 sections)
- [ ] `docs/setup.md` with clear instructions
- [ ] `docs/irb-checklist.md` if doing user research
- [ ] `.gitignore` configured
- [ ] `.env.example` exists (no real secrets!)

**Quality Checks**
- [ ] No spelling/grammar errors
- [ ] No placeholder text from templates
- [ ] All links work
- [ ] Architecture diagram included
- [ ] Proofread by all team members

**GitHub Issues**
- [ ] 10–15 issues created
- [ ] Issues have labels and milestones
- [ ] Issues have clear acceptance criteria

**Testing**
- [ ] One teammate cloned fresh and followed setup.md successfully
- [ ] All required files are present

**Final Step**
- [ ] Repository URL submitted via course system
- [ ] All team members confirmed submission

## Grading Timeline

- **Submission deadline:** End of Week 2 [exact date/time in course calendar]
- **Grading completed:** Within 5 business days
- **Feedback provided:** Via GitHub Issues or course system
- **Revisions (if needed):** 48 hours to address major issues

Good luck!