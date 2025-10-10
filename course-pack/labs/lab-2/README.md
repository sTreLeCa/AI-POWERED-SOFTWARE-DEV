# Lab 2: Team Formation & Capstone Kickoff

**Week 2 | Building AI-Powered Applications**

This lab transitions you from individual exploration to team‑based capstone development. You'll establish your team infrastructure, define your project scope, and submit your first major deliverable: the **Capstone Proposal**.

**Lab Duration:** 2 hours in‑class + asynchronous team work  
**Due Date:** End of Week 2 (see course calendar for exact date/time)

## Learning Objectives

By the end of this lab, you will:

- Set up a collaborative GitHub repository with proper structure
- Define team roles, workflows, and conflict resolution processes
- Articulate a clear AI‑powered application problem statement
- Identify target users and success criteria
- Outline initial technical architecture and risks
- Submit a complete capstone proposal (10 points)

## What's Due This Week

### Deliverable: Capstone Proposal (10 points)

Your proposal document must include:

1. **Problem Statement** – What problem are you solving? Why does it matter?
2. **Target Users** – Who will use this? What are their pain points?
3. **Success Criteria** – How will you measure if your solution works?
4. **Technical Architecture** – Initial system design (components, APIs, data flow)
5. **Risk Assessment** – What could go wrong? How will you mitigate?
6. **Research Plan** – What do you need to learn? What experiments will you run?
7. **User Study Plan** – How will you gather user feedback?
8. **Team Contract** – Roles, decision‑making, conflict resolution, contribution tracking

**Plus:** IRB Light Checklist (if your project involves user research)

## In‑Class Activities (2 hours)

### Part 1: Team GitHub Setup (30 min)

**Objective:** Create your team's central repository with proper structure.

**Tasks:**
1. One team member creates a new GitHub repository
2. Add all team members as collaborators
3. Set up the initial folder structure (see template)
4. Create a basic README with project title and team members
5. Initialize branch protection rules (optional but recommended)

**Resources:**
- [GitHub Setup Guide](./guides/github-setup-guide.md)
- [Repository Structure Template](./templates/repo-structure.md)

### Part 2: Team Contract Workshop (45 min)

**Objective:** Establish clear team norms and expectations.

**Tasks:**
1. Review the Team Contract Template together
2. Discuss and agree on:
   - Individual roles (who does what)
   - Meeting schedule and communication channels
   - Decision‑making process
   - Conflict resolution steps
   - Contribution tracking method
3. Draft your contract (finalize outside of class)

**Resources:**
- [Team Contract Template](./templates/team-contract-template.md)
- [Role Assignment Guide](./guides/role-assignment-guide.md)

### Part 3: Problem Statement Development (45 min)

**Objective:** Define what you're building and why it matters.

**Tasks:**
1. Brainstorm 3–5 potential AI application ideas
2. Evaluate each against feasibility and impact
3. Select one problem to focus on
4. Write a draft problem statement (2–3 paragraphs)
5. Identify your target users and their pain points
6. Outline 3–5 success criteria

**Resources:**
- [Problem Statement Guide](./guides/problem-statement-guide.md)
- [Capstone Proposal Template](./templates/capstone-proposal-template.md)

## Homework & Asynchronous Work

### Required Actions (Complete by End of Week 2)

1. **Finalize Team Contract**
   - Complete all sections of the template
   - All team members sign/approve
   - Commit to your repo: `docs/team-contract.md`

2. **Complete Capstone Proposal**
   - Fill out all 8 sections of the proposal template
   - Include architecture diagram (use draw.io, Excalidraw, or similar)
   - Proofread as a team
   - Submit as: `docs/capstone-proposal.md`

3. **Set Up Development Environment**
   - Each team member clones the repo
   - Install required dependencies (Python/Node.js, package manager)
   - Create a `setup.md` file documenting environment setup steps
   - Test that everyone can run a "Hello World" example

4. **Complete IRB Light Checklist (if applicable)**
   - If your project involves user research, complete the checklist
   - Submit as: `docs/irb-checklist.md`
   - See [IRB Guide](./guides/irb-light-guide.md) for when this is required

5. **Create Initial Backlog**
   - Break down your proposal into 10‑15 tasks
   - Create GitHub Issues for each task
   - Label them (e.g., `setup`, `research`, `design`, `implementation`)
   - Assign issues to Week 3–4 milestones

## Submission Instructions

### Where to Submit:
1. Push all files to your team GitHub repository
2. Submit your repo URL via the course submission system
3. Ensure your repo is either public or the instructor has been added as a collaborator

### Required Files in Your Repo:

```
your-repo/
├── README.md (with team info and project title)
├── docs/
│   ├── team-contract.md
│   ├── capstone-proposal.md
│   ├── irb-checklist.md (if applicable)
│   └── setup.md
├── .gitignore
└── (optional) architecture-diagram.png
```

## Grading Rubric (10 points total)

| Component              | Points | Criteria                                                     |
|-----------------------|--------|--------------------------------------------------------------|
| **Problem Clarity**   | 2      | Clear, specific problem with justification. Target users identified. |
| **Technical Feasibility** | 2  | Realistic architecture. Appropriate use of AI. Scope is achievable. |
| **Success Criteria**   | 1      | Measurable, specific success metrics defined.                |
| **Risk Assessment**    | 1      | Identifies key risks with mitigation strategies.             |
| **Research & User Plan** | 1.5 | Clear plan for learning and user feedback.                  |
| **Team Contract**      | 1.5    | Complete, specific, signed by all members.                 |
| **Presentation Quality** | 1   | Well‑organized, proofread, professional formatting.         |

## Tips for Success

**Start Early**

- Don't wait until the last day. Schedule 2–3 team meetings this week.

**Be Specific**

- Vague problem statements lead to scope creep. Be concrete about what you're building.

**Think Small**

- You have 13 weeks. Pick something you can ship, not a research paper.

**Communicate**

- Over‑communicate with your team. Use Slack/Discord/whatever works for you.

**Ask Questions**

- Use office hours. Post in the course forum. We're here to help.

**Document Everything**

- Write things down. Your future self (and teammates) will thank you.

## Common Pitfalls to Avoid

❌ **"We'll build a general‑purpose AI assistant"** – Too broad. Pick a specific use case.

❌ **Skipping the team contract** – This will bite you later. Do it now.

❌ **Ignoring data governance** – If you're using user data, plan for privacy from day one.

❌ **Overpromising** – Be realistic about what's achievable in a semester.

❌ **Not assigning clear roles** – Everyone should know what they're responsible for.

## Resources & Templates

**In This Folder:**

- [GitHub Setup Guide](./guides/github-setup-guide.md)
- [Team Contract Template](./templates/team-contract-template.md)
- [Capstone Proposal Template](./templates/capstone-proposal-template.md)
- [Problem Statement Guide](./guides/problem-statement-guide.md)
- [IRB Light Guide](./guides/irb-light-guide.md)
- [Role Assignment Guide](./guides/role-assignment-guide.md)

**External Resources:**

- [Anthropic API Docs](https://docs.anthropic.com/en/home)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
- [LangChain Documentation](https://python.langchain.com/docs/introduction/)

## Questions?

**During Lab:**

- Raise your hand or ping the instructor in the lab Slack channel

**Outside Lab:**

- Post in the course forum (preferred – others can benefit)
- Email: Zeshan.ahmad@kiu.edu.ge (expect 24‑hour response on weekdays)
- Office hours: See Week 1 announcement

## Looking Ahead: Week 3

Next week, we'll dive into implementation:

- Building your first AI‑powered feature
- Integrating vision and multimodal I/O
- Setting up evaluation hooks
- Cost and latency tracking

Make sure your environment is set up and your proposal is solid before Week 3!

**Remember:** The capstone is 25% of your grade. Invest time now to set yourself up for success later.

Good luck!
