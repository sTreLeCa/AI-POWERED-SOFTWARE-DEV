# Problem Statement Guide

This guide helps you craft a strong problem statement for your capstone project.

## What Makes a Good Problem Statement?

A strong problem statement should be:

- **Specific** – Clear, concrete problem, not vague
- **Scoped** – Achievable in 13 weeks by 2–3 people
- **User‑centered** – Focused on real user pain points
- **AI‑appropriate** – Actually benefits from AI/LLMs
- **Measurable** – You can tell if your solution works

## The Problem Statement Formula

Use this structure to craft your problem statement:

```
[Specific user group] struggles with [specific problem] when [context/situation].

Currently, they [current workaround], which leads to [negative consequences].

This problem affects [scale/impact] and costs them [time/money/frustration].

An AI‑powered solution could [how AI helps] by [concrete mechanism], resulting in [desired outcome].
```

## Step‑by‑Step: Crafting Your Statement

### 1. Identify the User

Questions to answer:

- Who exactly experiences this problem?
- What's their context? (Student? Professional? Hobbyist?)
- What's their technical level?
- What's their main goal?

### 2. Define the Problem

Questions to answer:

- What specific task are they trying to accomplish?
- What goes wrong or takes too long?
- When does this problem occur?
- How often does it happen?

### 3. Describe Current Solutions

Questions to answer:

- How do they solve this problem today?
- What tools/methods do they use?
- Why are current solutions inadequate?
- What's missing?

### 4. Quantify the Impact

Questions to answer:

- How much time/money does this cost?
- How many people are affected?
- What happens if the problem isn't solved?
- What's the worst‑case consequence?

### 5. Explain Why AI Helps

Questions to answer:

- What can AI do that existing solutions can't?
- Why is this better than a database query or rule‑based system?
- What specific AI capability are you leveraging? (Understanding, generation, reasoning?)
- Would this work without AI? If yes, rethink your approach.

## Examples: Bad vs. Good

### Too Vague

**Bad:** "Students need help with homework. They spend a lot of time on it and AI could help make it faster."

**Why it's bad:** Which students? Which subjects? What specific homework task? How would AI help? Too broad.

**Improved:**

"High school chemistry students struggle to balance complex redox equations. They currently use trial‑and‑error, which takes 10–15 minutes per problem and has 40% error rate. An AI tutor could guide them step‑by‑step through the balancing process, explain the underlying electron transfer, and verify their work in real time."

### Not AI‑Appropriate

**Bad:** "Restaurant owners need to track inventory. They use spreadsheets, which is tedious. An AI app could make this automatic."

**Why it's bad:** This is a CRUD app problem, not an AI problem. A traditional database would work better. No clear use for LLM capabilities.

**Improved:**

"Small restaurant owners struggle to predict ingredient needs, often over‑ordering (15% waste) or running out mid‑service. They currently guess based on last week's sales. An AI system could analyze historical sales patterns, weather, local events, and seasonal trends to predict next week's ingredient needs with 90% accuracy, reducing waste and stockouts."

### Too Ambitious

**Bad:** "Doctors need to diagnose diseases better. We'll build an AI that can diagnose any disease from symptoms, medical images, and lab results."

**Why it's bad:** Way too broad for a semester project. Requires medical expertise and regulatory approval. Needs massive training data and validation. Safety‑critical with huge liability concerns.

**Improved:**

"Pre‑med students learning dermatology struggle to remember the visual differences between similar skin conditions. They use static flashcards, which don't explain why things look different. An AI tutor could show them randomized dermatology images, accept natural language descriptions, provide instant feedback with explanations, and focus on conditions they find confusing."

### Well‑Scoped

**Good:** "Beginner programmers debugging Python code spend 30–40% of their time misinterpreting error messages. They copy‑paste errors into Google, sift through Stack Overflow posts, and often implement fixes without understanding the root cause. An AI coding assistant could explain Python errors in plain English, show what went wrong in the user's specific code, suggest fixes with reasoning, and quiz the user to ensure understanding before they continue."

**Why it's good:** Specific user (beginner Python programmers), specific problem (misinterpreting error messages), quantified impact (30–40% of debug time), clear current solution (Google + Stack Overflow), AI adds value (personalized explanation + context‑aware help), achievable scope (focus on common Python errors), measurable (time saved, comprehension quiz scores).

## Common Pitfalls to Avoid

### The "Swiss Army Knife" Trap

Problem: "We'll build an AI assistant that helps with homework, scheduling, meal planning, and fitness tracking."

Fix: Pick ONE problem. Do it well. You have 13 weeks.

### The "X but with AI" Trap

Problem: "It's like Notion but with AI" or "It's Grammarly but for code."

Fix: Don't start with a product. Start with a problem. If your solution is "existing tool + AI," you probably haven't defined a real problem.

### The "Research Project" Trap

Problem: "We'll develop a new attention mechanism to improve LLM reasoning."

Fix: This is a course about building applications, not AI research. Use existing models as building blocks.

### The "Data Science Project" Trap

Problem: "We'll train a model to predict customer churn."

Fix: Wrong course. This course is about using pre‑trained LLMs to build applications, not training models from scratch.

### The "Solution Looking for a Problem" Trap

Problem: "RAG is cool, let's use it. What should we use it for?"

Fix: Start with the problem, not the technology. Pick a problem, then decide if RAG is the right solution.

## Validation Questions

Before committing to your problem, answer these:

### User Validation

- Can you name 3 real people who have this problem?
- Have you experienced this problem yourself?
- Can you interview potential users in Week 3?

### Feasibility Validation

- Can you build a minimum version in 4 weeks?
- Do you have (or can you get) the necessary API access?
- Is the scope narrow enough to finish in 13 weeks?

### AI Validation

- Does this actually need AI, or would a traditional app work?
- Can you explain specifically what AI capability you're using?
- Would this work with current LLM APIs (GPT‑4, Claude, etc.)?

### Impact Validation

- Can you measure whether your solution works?
- Will users actually use this, or is it a novelty?
- Is the problem painful enough that users will try something new?

If you answered "no" or "I'm not sure" to several of these, revisit your problem statement.

## Brainstorming Exercise (30 minutes)

### Part 1: List 5 Problems (10 min)

Think about your own life. What frustrates you? What takes too long?

1. [Problem from your academic life]
2. [Problem from a hobby or interest]
3. [Problem from a part‑time job or internship]
4. [Problem you've heard others complain about]
5. [Problem you've tried to solve with existing tools but failed]

### Part 2: Pick 2 to Explore (10 min)

For each, answer:

- Who has this problem?
- How do they currently solve it?
- Why would AI help?
- Can you build it in 13 weeks?

### Part 3: Choose One (10 min)

As a team, discuss:

- Which problem are you most excited about?
- Which is most feasible?
- Which would look best in your portfolio?

Pick one. You can always pivot later, but commit for now.

## Fleshing Out Your Statement

Once you've picked a problem, write out:

### 1. Problem Statement (3–4 sentences)
[Use the formula above]

### 2. Target Users (1 paragraph)
- Who are they?
- What's their context?
- What's their technical level?
- How big is this user group?

### 3. Current Solution Analysis (1 paragraph)
- What do they do now?
- What tools exist?
- Why aren't those sufficient?
- What gap will you fill?

### 4. Why AI? (1 paragraph)
- What specific AI capability are you using? (Natural language understanding? Text generation? Pattern matching across large context? Conversational interaction?)
- Why is this better than a traditional approach?
- What's the AI enabling that wasn't possible before?

### 5. Success Looks Like… (bullets)
- User can accomplish [task] in [X time]
- Solution has [Y accuracy/quality]
- Users rate it [Z satisfaction score]
- Costs less than [$X per interaction]

## Example: Full Problem Statement

Here's what a complete problem statement looks like in your proposal:

---

**Problem Statement**

Computer science students learning recursion struggle to debug their recursive functions, often spending 30–45 minutes per bug. The main issue is visualizing the call stack and understanding how the function behaves at each recursion level. Currently, students use print statements and debuggers, but these tools require manually stepping through every call, which is tedious and doesn't build intuition. About 60% of intro CS students report recursion as their most difficult topic, and 30% of office hour visits are recursion‑related.

**Target Users**

Our primary users are undergraduate CS students in their first or second year, typically taking CS2 (Data Structures) or similar courses. They have basic programming knowledge (loops, functions, arrays) but are new to recursion. They're comfortable with web applications and expect instant feedback. Based on enrollment data, we estimate 200+ students at KIU alone fit this profile each semester.

**Current Solutions and Gaps**

Students currently use:
1. Online visualizers like Python Tutor – but these don't explain *why* things happen, just show execution.
2. YouTube tutorials – not interactive, can't handle their specific code.
3. Office hours – limited availability, doesn't scale.

What's missing is a tool that:
- Accepts their actual code (not just examples).
- Explains what's happening in natural language.
- Adapts explanations to their confusion points.
- Available 24/7.

**Why AI?**

An LLM‑based tutor can:

1. **Understand their code** – parse their recursive function and trace execution.
2. **Generate personalized explanations** – adapt language to their level.
3. **Answer follow‑up questions** – natural conversation vs static content.
4. **Identify misconceptions** – recognize common errors and address them directly.

This wouldn't be possible with a traditional app because:
- Rule‑based systems can't handle arbitrary code.
- Static visualizers can't answer "but why?" questions.
- Traditional tutoring doesn't scale to 200+ students.

**Success Criteria**

We'll know our solution works if:
- Students can debug a recursive function in <15 minutes (vs 30–45 currently).
- 80%+ of users report understanding improved after one session.
- Solution correctly traces execution for 95%+ of student‑submitted functions.
- Average cost <$0.10 per tutoring session.
- At least 20 students use it for 3+ sessions each.

---

## Tips for Success

1. **Talk to Real Users Early** – Interview 3–5 potential users in Week 2–3; ask about their current workflow; validate your assumptions.
2. **Start Narrow, Expand Later** – It's easier to add features than to cut scope mid‑semester. "Do one thing well" is better than "do five things poorly".
3. **Pick a Problem You Care About** – You'll spend 13 weeks on this; passion helps when you hit roadblocks; it will show in your final demo.
4. **Balance Ambition and Feasibility** – Dream big, but prototype small; Week 3–4 should be a working (if rough) demo; Week 15 should be polished and complete.
5. **Remember: You're Building an Application** – Focus on user experience, not just AI accuracy; "Ship something users want" beats "technically impressive but unusable"; portfolio impact comes from solving real problems.

## Red Flags – When to Reconsider

🚩 "We'll disrupt an entire industry"  
🚩 "No one has ever solved this problem before"  
🚩 "We need more than $500 in API costs"  
🚩 "We'll train our own model from scratch"  
🚩 "We can't demo this without months of training data"  
🚩 "We need partnerships with companies to launch"  
🚩 "This requires hardware we don't have"  
🚩 "We'll need IRB approval for medical/financial data"  

If any of these apply, rescope.

## Getting Feedback

Before finalizing your problem statement:

### Peer Review (Week 2 Lab)

- Share with another team.
- Get their honest reaction.
- Is it clear? Exciting? Feasible?

### User Validation (Week 2–3)

- Show your problem statement to 2–3 potential users.
- Do they agree it's a problem?
- Would they use your solution?

### Instructor Review (Week 2)

- Office hours.
- Course forum.
- Proposal feedback.

Don't wait until the proposal is due. Validate early!

## Final Checklist

Before submitting your proposal, confirm:

- Problem is specific (not "people need better X").
- Users are clearly defined (not "everyone").
- Current solutions and their gaps are identified.
- AI adds clear value (not just buzzword).
- Scope is realistic for 13 weeks.
- You can measure success.
- You're excited about this problem.
- You've talked to potential users.
- Your team agrees this is the right problem.

## Resources

- [YC's Guide to Evaluating Startup Ideas](https://www.ycombinator.com/library/6e-how-to-evaluate-startup-ideas)
- [Paul Graham: How to Get Startup Ideas](http://paulgraham.com/startupideas.html)
- [Jobs to Be Done Framework](https://jtbd.info/2-what-is-jobs-to-be-done-jtbd-796b82081cca)

Remember: A clear problem statement is half the work. Get this right, and the rest of your project will flow from it. Questions? Post in the course forum or ask during office hours.