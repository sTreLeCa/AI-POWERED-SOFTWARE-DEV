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
### LAB SESSION SCRIPT (60 Minutes)

#### Part 1: Setup Verification & Introduction (0:00-0:10)

**Instructor Script:**

"Good morning/afternoon! Welcome to Week 1 Lab. Today we're going to build and deploy your first AI-powered application. By the end of this hour, you'll have a working app running on your local machine.

Let's start with a quick environment check. Open your terminal and verify:

1. Type `git --version` - you should see a version number
2. Type `python3 --version` OR `node --version` - version number should appear
3. Who has their API key ready? Keep it handy but DON'T share it out loud.

If anyone is missing these, raise your hand now and we'll get you sorted quickly."

**Troubleshooting Time: 5 minutes**
- Pair students with issues with those who are ready
- Have backup Gemini API keys ready for students who couldn't get one https://aistudio.google.com/app/api-keys

---

#### Part 2: The Builder Sprint Workflow (0:10-0:25)

**Instructor Script:**

"We're going to use a three-step workflow today: **Scaffold → Export → Run Locally**. This is how professional developers prototype quickly while maintaining full control of their code.

Step 1 uses a 'builder tool' to generate our starting code. Step 2 exports that code to GitHub. Step 3 proves the code works independently on your machine. Let's do this together."

**Live Demo - Follow Along:**

**STEP 1: Scaffold with Bolt.new**

1. Open browser to https://bolt.new/
2. Sign in with GitHub (one-click OAuth)
3. In the prompt box, paste this exact prompt:

```
Create a minimal web application with:
- A clean, simple UI with one text input field labeled "Enter your prompt"
- A submit button labeled "Generate"  
- An output area that displays the AI response
- Use the Gemini API for text generation
- The app should make a POST request to the Gemini API endpoint
- Include a .env.example file showing the required API_KEY variable
- Use vanilla HTML/CSS/JavaScript, no frameworks
- Make it look professional with basic styling
```

4. Wait 30-60 seconds for generation
5. **CRITICAL:** Review the generated files together:
   - `index.html` - the UI
   - `style.css` - basic styling  
   - `script.js` - API call logic
   - `.env.example` - API key template

**Instructor explains:**
"Notice what the AI generated: a complete folder structure with HTML, CSS, and JavaScript. This is scaffolding - the AI did the boilerplate work. Now we need to own this code."

---

**STEP 2: Export to GitHub**

**Instructor Demo (students follow along):**

1. In Bolt.new, click "Deploy" → "Download Code"
2. Save the ZIP file to your `week1-builder-sprint` folder
3. Extract the ZIP file
4. Open terminal in the extracted folder

```bash
cd ~/ai-apps-course/week1-builder-sprint/[extracted-folder-name]
```

5. Initialize Git repository:

```bash
# Initialize repo
git init

# Create .gitignore file
echo "node_modules/\n.env\n*.log" > .gitignore

# Create .env file (DO NOT COMMIT THIS)
echo "API_KEY=your_actual_api_key_here" > .env

# Add all files
git add .

# First commit
git commit -m "Initial commit: Builder sprint scaffold"
```

6. Create GitHub repository:
   - Go to https://github.com/new
   - Repository name: `week1-builder-sprint`
   - Keep it Private
   - **Do NOT initialize with README**
   - Click "Create repository"

7. Link local repo to GitHub:

```bash
# Copy the commands GitHub shows you, they'll look like:
git remote add origin https://github.com/YOUR-USERNAME/week1-builder-sprint.git
git branch -M main
git push -u origin main
```

**Instructor pauses:**
"Everyone should now have their code on GitHub. Let's verify - go to your GitHub repo in the browser. You should see all your files except .env. If .env is there, we have a security problem!"

---

**STEP 3: Run Locally**

**Instructor Script:**
"Now the critical test - can this run without Bolt.new? Let's prove it."

**For the HTML/JavaScript version:**

1. Open `.env` file and add your REAL API key:
```
API_KEY=your_gemini_api_key_here
```

2. Modify `script.js` to read from .env (Instructor demonstrates):

```javascript
// At the top of script.js, add:
// NOTE: In production, API keys should NEVER be in frontend code
// This is for educational purposes only
const API_KEY = 'YOUR_GEMINI_KEY_HERE'; // Replace with actual key

// Find the API call section and update it:
async function generateText() {
    const prompt = document.getElementById('promptInput').value;
    const outputDiv = document.getElementById('output');
    
    outputDiv.textContent = 'Generating...';
    
    try {
        const response = await fetch(
            `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${API_KEY}`,
            {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    contents: [{ parts: [{ text: prompt }] }]
                })
            }
        );
        
        const data = await response.json();
        const generatedText = data.candidates[0].content.parts[0].text;
        outputDiv.textContent = generatedText;
    } catch (error) {
        outputDiv.textContent = 'Error: ' + error.message;
        console.error(error);
    }
}
```

3. Run a simple local server:

```bash
# Python option:
python3 -m http.server 8000

# OR Node option (if you have Node):
npx http-server -p 8000
```

4. Open browser to `http://localhost:8000`

5. **TEST IT:**
   - Enter prompt: "Write a haiku about coding"
   - Click Generate
   - Wait 2-3 seconds
   - See the AI response appear

**Instructor Script:**
"If you see AI-generated text, congratulations! You've built and deployed your first AI application. It's running entirely on your machine, no cloud platform required."

---

#### Part 3: Understanding What We Built (0:25-0:35)

**Instructor Walkthrough (Code Review):**

"Let's understand what we actually created. Open your `script.js` file."

**Key Concepts to Explain:**

1. **API Endpoint:**
```javascript
https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent
```
"This is the URL where Google's AI model lives. We're making an HTTP request to this address."

2. **Authentication:**
```javascript
?key=${API_KEY}
```
"This is how Google knows who's making the request and whether to allow it."

3. **Request Payload:**
```javascript
{
    contents: [{ parts: [{ text: prompt }] }]
}
```
"This is the structure Gemini expects. We're sending our user's prompt wrapped in this specific JSON format."

4. **Response Parsing:**
```javascript
data.candidates[0].content.parts[0].text
```
"Gemini sends back multiple possible responses. We're taking the first one."

5. **Error Handling:**
```javascript
try { ... } catch (error) { ... }
```
"Always handle errors. Networks fail. APIs go down. Users enter weird input."

**Instructor asks:**
"What happens if:
- The API key is wrong? (Show the error)
- The network is disconnected? (Demonstrate)
- The user enters an empty prompt? (Let's add validation)"

**Quick Enhancement Exercise (5 minutes):**
"Everyone add input validation:"

```javascript
function generateText() {
    const prompt = document.getElementById('promptInput').value;
    
    // ADD THIS:
    if (!prompt.trim()) {
        alert('Please enter a prompt!');
        return;
    }
    
    // ... rest of code
}
```

"Test it. Try clicking Generate with no input. Now it's more user-friendly!"

---

#### Part 4: Cost & Token Tracking (0:35-0:45)

**Instructor Script:**
"Let's talk about the business side of AI applications: cost. Every API call costs money."

**Live Demonstration:**

"Open your browser's Network tab (F12 → Network). Now make another API call. Watch the request."

**Show students:**
1. Request size in bytes
2. Response size in bytes  
3. Response time in milliseconds

**Explain:**
```
Gemini Free Tier:
- 60 requests per minute
- ~32,000 tokens per request (input + output)
- Absolutely free for development

But in production:
- Input: ~$0.00025 per 1K tokens
- Output: ~$0.0005 per 1K tokens

Example cost:
- User sends 100 words (~130 tokens) = $0.0000325
- AI responds with 200 words (~260 tokens) = $0.00013
- Total: ~$0.00016 per interaction
- 10,000 users/day = $1.60/day = $48/month
```

**Exercise: Add Token Counter**

"Let's add basic token tracking:"

```javascript
function estimateTokens(text) {
    // Rough estimate: 1 token ≈ 4 characters
    return Math.ceil(text.length / 4);
}

async function generateText() {
    const prompt = document.getElementById('promptInput').value;
    
    if (!prompt.trim()) {
        alert('Please enter a prompt!');
        return;
    }
    
    const inputTokens = estimateTokens(prompt);
    console.log(`Estimated input tokens: ${inputTokens}`);
    
    outputDiv.textContent = 'Generating...';
    
    const startTime = Date.now();
    
    try {
        const response = await fetch(...);
        const data = await response.json();
        const generatedText = data.candidates[0].content.parts[0].text;
        
        const outputTokens = estimateTokens(generatedText);
        const duration = Date.now() - startTime;
        
        console.log(`Output tokens: ${outputTokens}`);
        console.log(`Total tokens: ${inputTokens + outputTokens}`);
        console.log(`Duration: ${duration}ms`);
        
        outputDiv.textContent = generatedText;
    } catch (error) {
        outputDiv.textContent = 'Error: ' + error.message;
    }
}
```

"Now open your console, make a request, and see the token count!"

---

#### Part 5: Commit Changes & Lab Wrap-up (0:45-0:60)

**Instructor Script:**
"Let's commit your improvements to Git. This builds good habits."

```bash
git add .
git commit -m "Added input validation and token tracking"
git push
```

**Verification:**
"Go to your GitHub repo. You should see your latest commit with today's timestamp."

**Lab Deliverables Checklist:**

Read through with students:
- [ ] Working local application (tested with real prompt)
- [ ] Code committed to GitHub (with at least 2 commits)
- [ ] .env file created locally (but NOT committed)
- [ ] Input validation added
- [ ] Token tracking in console logs
- [ ] Can explain the API request/response flow

**Homework Introduction (5 minutes):**

"Tonight's homework builds directly on this lab. You'll enhance your app with three features:

1. **Streaming responses** - Show text as it generates (better UX)
2. **Cost calculator** - Display estimated cost per request
3. **Error retry logic** - Automatically retry failed requests

Due: Next Tuesday before class.

Full instructions are on the LMS. Start tonight while this is fresh."

**Q&A (5 minutes):**
- "What questions do you have about today's lab?"
- "Any issues we need to troubleshoot?"

**Closing:**
"Great work today. You've gone from zero to a deployed AI application in 60 minutes. Tomorrow we'll add vision capabilities. Come ready to code!"

---

## WEEK 1 HOMEWORK: API Essentials Enhancement

**Due:** Tuesday of Week 2, before class  
**Submission:** GitHub repository link + 300-word reflection  
**Points:** 10 points (graded per syllabus rubric)

### Assignment Overview
Enhance your Week 1 Builder Sprint application with three professional features: streaming responses, cost estimation, and retry logic.

### Requirements

#### Part 1: Streaming Responses (4 points)

**Objective:** Display AI responses as they generate, character by character, instead of waiting for the complete response.

**Implementation:**

1. Modify your API call to use Gemini's streaming endpoint:

```javascript
async function generateTextStreaming() {
    const prompt = document.getElementById('promptInput').value;
    const outputDiv = document.getElementById('output');
    
    if (!prompt.trim()) {
        alert('Please enter a prompt!');
        return;
    }
    
    outputDiv.textContent = ''; // Clear previous output
    
    try {
        const response = await fetch(
            `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:streamGenerateContent?key=${API_KEY}`,
            {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    contents: [{ parts: [{ text: prompt }] }]
                })
            }
        );
        
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            
            const chunk = decoder.decode(value);
            const lines = chunk.split('\n');
            
            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    const jsonStr = line.slice(6);
                    try {
                        const data = JSON.parse(jsonStr);
                        if (data.candidates && data.candidates[0].content) {
                            const text = data.candidates[0].content.parts[0].text;
                            outputDiv.textContent += text;
                        }
                    } catch (e) {
                        // Skip malformed JSON
                    }
                }
            }
        }
    } catch (error) {
        outputDiv.textContent = 'Error: ' + error.message;
        console.error(error);
    }
}
```

**Grading Criteria:**
- Streaming works correctly (2 pts)
- Text appears incrementally (1 pt)
- Error handling present (1 pt)

---

#### Part 2: Cost Calculator (3 points)

**Objective:** Display the estimated cost of each API call to the user.

**Implementation:**

1. Create a cost calculation function:

```javascript
function calculateCost(inputTokens, outputTokens) {
    const INPUT_COST_PER_1K = 0.00025;  // Gemini pricing
    const OUTPUT_COST_PER_1K = 0.0005;
    
    const inputCost = (inputTokens / 1000) * INPUT_COST_PER_1K;
    const outputCost = (outputTokens / 1000) * OUTPUT_COST_PER_1K;
    
    return {
        input: inputCost,
        output: outputCost,
        total: inputCost + outputCost
    };
}
```

2. Add a display element to your HTML:

```html
<span id="costDisplay">Cost: $0.00000</span>
```

3. Update cost after each request:

```javascript
// After generating text:
const cost = calculateCost(inputTokens, outputTokens);
document.getElementById('costDisplay').textContent = 
    `Cost: $${cost.total.toFixed(6)} (In: ${inputTokens} tokens, Out: ${outputTokens} tokens)`;
```

**Grading Criteria:**
- Cost calculation function implemented (1 pt)
- Cost displayed in UI (1 pt)
- Shows input/output token breakdown (1 pt)

---

#### Part 3: Retry Logic with Exponential Backoff (3 points)

**Objective:** Automatically retry failed API requests with increasing delays.

**Implementation:**

```javascript
async function fetchWithRetry(url, options, maxRetries = 3) {
    for (let attempt = 0; attempt < maxRetries; attempt++) {
        try {
            const response = await fetch(url, options);
            
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            return response;
        } catch (error) {
            console.log(`Attempt ${attempt + 1} failed:`, error.message);
            
            if (attempt === maxRetries - 1) {
                // Last attempt failed
                throw error;
            }
            
            // Exponential backoff: 1s, 2s, 4s
            const delay = Math.pow(2, attempt) * 1000;
            console.log(`Retrying in ${delay}ms...`);
            await new Promise(resolve => setTimeout(resolve, delay));
        }
    }
}

// Usage:
async function generateText() {
    try {
        const response = await fetchWithRetry(apiUrl, requestOptions, 3);
        // ... process response
    } catch (error) {
        outputDiv.textContent = 'Failed after 3 attempts: ' + error.message;
    }
}
```

**Grading Criteria:**
- Retry function implemented (1.5 pts)
- Exponential backoff working (1 pt)
- Max retries configurable (0.5 pts)

---

### Part 4: 300-Word Reflection (Extra 0 points - for feedback)

Write a brief reflection answering:

1. **What worked well?** What was easier than expected?
2. **What was challenging?** Where did you get stuck?
3. **Cost insights:** Based on your testing, estimate the monthly cost if your app had:
   - 100 users/day with 5 requests each
   - Average 50 input tokens, 150 output tokens per request
4. **UX Observations:** How does streaming impact user experience compared to waiting for full response?
5. **Next Steps:** What would you add to make this production-ready?

**Grading:** Pass/Fail (must be thoughtful and specific)

---

### Submission Requirements

1. **GitHub Repository Link**
   - Repository must be public or instructor added as collaborator
   - README.md with:
     - Project title and description
     - Setup instructions
     - How to test each feature
     - Screenshots of working features

2. **Code Quality Requirements**
   - Code must run without errors
   - All three features working
   - Clear comments explaining logic
   - No API keys committed to repo
   - .gitignore present

3. **Testing Evidence**
   - Console logs showing token counts
   - Screenshot of streaming in action
   - Screenshot of cost calculator
   - Console logs showing retry attempts

4. **Reflection Document**
   - Submit as PDF or Markdown in repo
   - 300-400 words
   - Answers all 5 reflection questions

---

### Grading Rubric (10 points total)

| Component | Points | Criteria |
|-----------|--------|----------|
| Streaming Responses | 4 | Fully working (4), Partial (2), Not working (0) |
| Cost Calculator | 3 | Complete (3), Partial (1.5), Missing (0) |
| Retry Logic | 3 | Correct implementation (3), Partial (1.5), Missing (0) |
| **TOTAL** | **10** |

**Deductions:**
- Missing README: -1 point
- Code doesn't run: -2 points
- API key committed: -1 point
- Late submission: -1 point per day (max 3 days)

---

### Getting Help

**Office Hours:** See syllabus for times  
**Email:** Zeshan.ahmad@kiu.edu.ge  
**Course Forum:** Check LMS for peer help

**Common Issues:**

1. **Streaming not working:**
   - Check endpoint has `stream` in URL
   - Verify you're using `getReader()`
   - Test with simpler prompts first

2. **Cost showing $0.00000:**
   - Check token estimation function
   - console.log the token values
   - Verify multiplication not division

3. **Retries happening too fast:**
   - Check `await` before setTimeout
   - Verify exponential calculation
   - Add console.logs to debug timing

---

---
