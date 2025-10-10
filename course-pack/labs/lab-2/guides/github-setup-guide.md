# GitHub Setup Guide

This guide walks you through setting up your team's GitHub repository for the capstone project. Follow these steps during your first team meeting.

**Time needed:** 30 minutes  
**Who does this:** One team member creates the repo, then everyone else joins

## Step 1: Create the Repository (Team Lead Only)

1. Go to [GitHub](https://github.com) and sign in.
2. Click the "+" icon in the top right → "New repository".
3. Configure your repository:
   - **Repository name:** `[your-project-name]`
   - **Description:** AI‑powered [brief description] – built for Building AI‑Powered Applications course
   - **Visibility:** Public (or Private if you prefer)
   - **Initialize with README:** Yes
   - **Add .gitignore:** Python (or Node depending on your stack)
   - **License:** MIT (recommended) or None
4. Click "Create repository".
5. Copy the repository URL – click the green "Code" button and copy the HTTPS URL (e.g., `https://github.com/username/project-name.git`).

## Step 2: Add Team Members as Collaborators

1. In your repository, click **Settings** (top right).
2. Click **Collaborators** in the left sidebar (you may need to confirm your password).
3. Click **Add people**.
4. Search for each teammate by GitHub username or email.
5. Select **Write** access (allows them to push code).
6. Repeat for all team members.
7. Also add the instructor (GitHub username will be provided) with **Read** access.

Team members will receive an email invitation. Accept it to gain access.

## Step 3: Set Up Repository Structure

**Who does this:** Team lead creates the structure, then everyone pulls it.

### Create the Folder Structure

In your repository, create these folders:

```
your-repo/
├── .github/
│   └── workflows/          # CI/CD configs (later)
├── docs/
│   ├── team-contract.md    # Your team contract
│   ├── capstone-proposal.md # Your proposal
│   ├── setup.md            # Setup instructions
│   └── irb-checklist.md    # If doing user research
├── src/                    # Your source code
│   ├── backend/            # API code
│   ├── frontend/           # UI code
│   └── scripts/            # Utility scripts
├── tests/                  # Test files
├── data/                   # Sample data (not user data!)
├── .env.example            # Example environment variables
├── .gitignore              # Already created
├── README.md               # Already created
└── requirements.txt        # Python deps (or package.json for Node)
```

### How to Create Folders in GitHub Web Interface

**Option A: Use GitHub Web Interface**

1. Click **Add file** → **Create new file**.
2. Type `docs/.gitkeep` as the filename (the `/` creates a folder).
3. Commit the file.
4. Repeat for other folders.

**Option B: Create Locally (Recommended)**

```bash
# Clone the repo
git clone https://github.com/username/project-name.git
cd project-name

# Create folder structure
mkdir -p docs src/backend src/frontend src/scripts tests data .github/workflows

# Create placeholder files
touch docs/.gitkeep src/.gitkeep tests/.gitkeep data/.gitkeep
touch .env.example
touch requirements.txt  # or package.json

# Commit and push
git add .
git commit -m "chore: initialize project structure"
git push origin main
```

## Step 4: Update the README

Replace the default README with your project information:

```markdown
# [Your Project Title]

[One‑line description of what your project does]

**Team:** [Member 1], [Member 2], [Member 3]  
**Course:** Building AI‑Powered Applications  
**Institution:** KIU  
**Semester:** Fall 2025

## About

[2–3 sentence description of your project]

## Status

🚧 **Project Status:** Planning (Week 2)

- [x] Team formed
- [x] Repository created
- [ ] Proposal submitted
- [ ] Core features implemented
- [ ] User testing completed

## Quick Links

- [Capstone Proposal](./docs/capstone-proposal.md)
- [Team Contract](./docs/team-contract.md)
- [Setup Instructions](./docs/setup.md)

## Tech Stack

- **Frontend:** [Framework]
- **Backend:** [Framework]
- **AI/ML:** [Model(s)]
- **Database:** [Database]
- **Hosting:** [Platform]

## Getting Started

You'll fill this in later with setup instructions.

```bash
# Clone the repo
git clone https://github.com/username/project-name.git

# Install dependencies
# (instructions coming in Week 3)

# Run the app
# (instructions coming in Week 3)
```

## Documentation

See the [docs](./docs/) folder for:
- Project proposal
- Team contract
- Setup guide
- Architecture diagrams

## License

[MIT License / None / etc.]

## Contact

For questions, reach out to any team member:
- [Member 1]: [email]
- [Member 2]: [email]
- [Member 3]: [email]
```

How to update:

1. Click on `README.md` in your repo.
2. Click the pencil icon (Edit).
3. Paste the template above and fill in your details.
4. Commit changes.

## Step 5: Set Up .gitignore

Make sure your `.gitignore` file includes:

```
# Environment variables
.env
.env.local
.env.*.local

# API keys and secrets
**/secrets/
**/*.key
**/*.pem

# Dependencies
node_modules/
venv/
env/
__pycache__/
*.pyc

# Build outputs
dist/
build/
*.egg-info/

# IDE files
.vscode/
.idea/
*.swp
*.swo
.DS_Store

# Logs
*.log
logs/

# Database
*.db
*.sqlite

# User data (never commit real user data!)
data/users/
data/recordings/
```

If you initialized with Python `.gitignore`, most of this is already there. Just add the "secrets" and "user data" sections.

## Step 6: Create .env.example

This file shows what environment variables are needed, without exposing actual secrets:

```bash
# .env.example

# AI Model API Keys
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Database
DATABASE_URL=postgresql://user:pass@localhost/db

# Vector DB
PINECONE_API_KEY=your-key-here
PINECONE_ENVIRONMENT=us-east-1-aws

# App Config
APP_ENV=development
DEBUG=True
LOG_LEVEL=INFO

# (Add more as you discover what you need)
```

Everyone on the team should:

1. Copy `.env.example` to `.env` on your local machine.
2. Fill in your actual API keys.
3. **Never commit `.env` to git**.

## Step 7: Set Up Branch Protection (Optional but Recommended)

Protect your `main` branch from accidental force pushes:

1. Go to **Settings** → **Branches**.
2. Click **Add rule**.
3. Branch name pattern: `main`.
4. Enable:
   - Require pull request before merging
   - Require approvals: 1 (at least one teammate reviews)
5. Click **Create**.

What this does:

- You can't push directly to `main`.
- Must create a branch, push changes, open a PR, get approval.
- Prevents accidental overwrites.

**Workflow with branch protection:**

```bash
# Create a feature branch
git checkout -b feature/add-user-auth

# Make changes, commit
git add .
git commit -m "feat: add user authentication"

# Push your branch
git push origin feature/add-user-auth

# Go to GitHub and open a Pull Request
# Ask a teammate to review
# Once approved, merge to main
```

## Step 8: Each Team Member Clones the Repo

Every team member should now:

1. Accept the GitHub invitation (check your email).
2. Clone the repository:
   ```bash
   git clone https://github.com/username/project-name.git
   cd project-name
   ```
3. Verify you have write access:
   ```bash
   # Make a small test change
   echo "# Test by [Your Name]" >> README.md
   git add README.md
   git commit -m "test: verify git access – [Your Name]"
   git push origin main
   ```
4. Pull everyone's changes:
   ```bash
   git pull origin main
   ```

If you get a permission error, ask the team lead to double‑check you were added as a collaborator.

## Step 9: Set Up Git Workflow

### Recommended Branch Strategy

For a small team (2–3 people), keep it simple:

- `main` branch: Always deployable, working code.
- Feature branches: `feature/description` (e.g., `feature/add-rag`, `feature/frontend-ui`).
- Bug fixes: `fix/description`.

**Workflow:**
1. Always pull before starting work: `git pull origin main`.
2. Create a branch: `git checkout -b feature/my-feature`.
3. Make changes, commit often: `git commit -m "feat: add thing"`.
4. Push your branch: `git push origin feature/my-feature`.
5. Open a PR on GitHub.
6. Get a teammate to review.
7. Merge to main.
8. Delete the feature branch.

### Commit Message Format

Use conventional commits:

```
feat: add new feature
fix: fix bug
docs: update documentation
chore: update dependencies
test: add tests
refactor: refactor code
```

Examples:

```
feat: implement RAG with Pinecone
fix: resolve API timeout issue
docs: add setup instructions to README
chore: add OpenAI to requirements.txt
```

## Step 10: Add Project Documentation

Create `docs/setup.md` with development setup instructions:

```markdown
# Development Setup

## Prerequisites

- Python 3.11+ (or Node.js 18+)
- Git
- [Any other requirements]

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/username/project-name.git
   cd project-name
   ```
2. Create virtual environment (Python)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```
5. Run the application
   ```bash
   # (You'll add this in Week 3)
   ```

## Troubleshooting

[Common issues and solutions – fill in as you encounter them]
```

## Checklist: Is Your Repo Ready?

Before moving on, verify:

- Repository is created (public or private)
- All team members have been added as collaborators
- Instructor has read access
- Folder structure is set up (docs/, src/, tests/, etc.)
- README has project info and team names
- `.gitignore` includes secrets and environment files
- `.env.example` exists (no real keys in it!)
- Everyone can clone and push to the repo
- Branch protection is set up (optional)

## Common Issues & Solutions

### "Permission denied" when pushing

**Problem:** You don't have write access.

**Solution:**

- Make sure you accepted the GitHub invitation.
- Ask team lead to verify you're listed as a collaborator.
- Check you're pushing to the correct repo.

### "Failed to push some refs"

**Problem:** Your local branch is behind the remote.

**Solution:**

```bash
git pull origin main --rebase
git push origin main
```

### "Merge conflict"

**Problem:** Two people edited the same file.

**Solution:**

1. Open the conflicted file.
2. Look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. Decide which changes to keep.
4. Remove the conflict markers.
5. `git add [file]`, `git commit`, `git push`.

### Accidentally committed `.env` file

**Problem:** Your secrets are in the repo!

**Solution:**

```bash
# Remove from git but keep local file
git rm --cached .env

# Add to .gitignore if not already there
echo ".env" >> .gitignore

# Commit the removal
git commit -m "chore: remove .env from repo"
git push

# IMPORTANT: Rotate all exposed API keys immediately!
```

### Can't see other people's changes

**Problem:** Forgot to pull.

**Solution:**

```bash
git pull origin main
```

## Next Steps

Once your GitHub is set up:

1. Complete the team contract.
2. Start working on the capstone proposal.
3. Each member sets up their local development environment.
4. Submit your repo URL and proposal by end of Week 2.

## Resources

- [GitHub Docs: Creating a Repository](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [GitHub Docs: Inviting Collaborators](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Conventional Commits](https://www.conventionalcommits.org/)

Questions? Ask in the course forum or during office hours.