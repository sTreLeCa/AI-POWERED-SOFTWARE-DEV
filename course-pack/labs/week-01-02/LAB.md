# Building AI-Powered Applications
## Week 1 & 2 Lab Materials + Team Formations

---

## TEAM FORMATIONS FOR CAPSTONE PROJECT

### Team Formation Strategy
Teams are balanced based on:
- **API comfort level** (technical skill distribution)
- **Role preferences** (strategist, builder, researcher, presenter)
- **AI tool experience** (mix of experience levels)
- **Collaboration style** (balancing solo workers with team players)

### TEAM 1: The Technical Pioneers
**Focus: High technical capability, balanced roles**

1. **Tarkashvili.Mariam@kiu.edu.ge**
   - Role: The Builder/Coder
   - API Comfort: Very comfortable
   - Experience: ChatGPT, Gemini, Claude, Perplexity, Cursor, Lovable/Bolt
   - Strength: Deep AI tool experience, portfolio-focused

2. **lomjaria.mamuka@kiu.edu.ge**
   - Role: The Strategist/Planner
   - API Comfort: Neutral
   - Experience: ChatGPT, GitHub Copilot
   - Strength: Organization, planning, troubleshooting

3. **[Student 3 email TBD]**
   - Role: The Researcher/Thinker
   - API Comfort: Somewhat comfortable
   - Experience: Mixed tools
   - Strength: Analysis and documentation

4. **[Student 4 email TBD]**
   - Role: The Communicator/Presenter
   - API Comfort: Neutral
   - Experience: Basic AI tools
   - Strength: UX design, communication

---

## WEEK 1 LAB: Builder Sprint & API Foundations
**Duration:** 1 hour  
**Format:** Guided hands-on coding session  
**Objective:** Get a working AI text-generation app running locally

---

### PRE-LAB REQUIREMENTS (Complete BEFORE Lab)

#### Mandatory Setup (Due: Night before lab)

**1. Development Environment Setup (20 minutes)**

Install the following tools:
**a) Git**
- Mac: Already installed or `brew install git`
- Windows: https://git-scm.com/download/win
- Linux: `sudo apt-get install git`
- **Verify:** Open terminal, type `git --version`

**b) Python 3.9+ OR Node.js 18+**

Python Option:
```bash
# Check version
python3 --version  # Should be 3.9 or higher

# Install if needed
# Mac: brew install python
# Windows: https://www.python.org/downloads/
# Linux: sudo apt-get install python3
```

Node.js Option:
```bash
# Check version
node --version  # Should be 18 or higher

# Install if needed
# Mac: brew install node
# Windows/Linux: https://nodejs.org/
```

**c) Package Manager**
- Python: `pip3` (comes with Python)
- Node: `npm` (comes with Node.js)

**d) Code Editor**
- Recommended: **Cursor IDE** - https://cursor.sh/
- Alternative: VS Code - https://code.visualstudio.com/

**2. Create GitHub Account (5 minutes)**
- Sign up at https://github.com/ if you don't have an account
- Verify email address
- Generate Personal Access Token:
  1. Settings → Developer settings → Personal access tokens → Tokens (classic)
  2. Generate new token (classic)
  3. Select scopes: `repo`, `workflow`
  4. Copy token immediately (won't be shown again)

**3. Get Free AI API Access (15 minutes)**

Choose ONE of the following:

**Option A: Google Gemini (Recommended for Free Tier)**
1. Visit https://ai.google.dev/
2. Click "Get API key in Google AI Studio"
3. Sign in with Google account
4. Create new project or select existing
5. Click "Get API key" → "Create API key"
6. **Copy and save** your API key securely
7. Free tier: 60 requests/minute

**Test your key:**
```bash
curl -H "Content-Type: application/json" \
  -d '{"contents":[{"parts":[{"text":"Hello"}]}]}' \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=YOUR_API_KEY"
```

**Option B: OpenAI (Requires $5 minimum credit)**
1. Visit https://platform.openai.com/
2. Sign up and verify phone
3. Add $5 minimum credit
4. Go to API keys section
5. Create new secret key
6. **Copy and save** immediately

**Option C: Anthropic Claude (Requires credit)**
1. Visit https://console.anthropic.com/
2. Sign up with email
3. Add payment method ($5 minimum)
4. Generate API key
5. Save securely

**4. Pre-Lab Knowledge Check (10 minutes)**
Watch this 8-minute video: "What is an API?" 
- Link: https://www.youtube.com/watch?v=s7wmiS2mSXY

**5. Create Project Directory (5 minutes)**
```bash
# Create workspace for the course
mkdir ~/ai-apps-course
cd ~/ai-apps-course
mkdir week1-builder-sprint
cd week1-builder-sprint
```

#### Pre-Lab Checklist
Submit via LMS by midnight before lab:
- [ ] Git installed and verified
- [ ] Python or Node.js installed and verified
- [ ] GitHub account created
- [ ] API key obtained and tested
- [ ] Code editor installed
- [ ] Watched API basics video
- [ ] Project directory created

---
