### What to Track in Git
- ✅ All markdown files
- ✅ Templates
- ✅ Guides
- ✅ Example proposals (anonymized)
- ✅ Images and diagrams

### What NOT to Track
- ❌ Student submissions (those go in their repos)
- ❌ Grading sheets with student names
- ❌ Private instructor notes

### Commit Messages
Use clear, descriptive commits:
```
feat: add IRB light guide for user research
fix: correct GitHub setup instructions for SSH
docs: add FAQ section to homework assignment
chore: update external links for 2025
```

---

## Integration with Course Repository

### Recommended Course Repo Structure

```
course-repository/
├── README.md
├── syllabus.pdf
├── schedule.md
│
├── labs/
│   ├── lab-1/
│   ├── lab-2/  ← THIS FOLDER
│   ├── lab-3/
│   └── ...
│
├── lectures/
│   ├── week-1/
│   ├── week-2/
│   └── ...
│
└── resources/
    ├── setup/
    ├── readings/
    └── tools/
```

### Cross-References

Link from course materials:
- Syllabus → Lab 2 README
- Week 2 announcement → Lab 2 README
- Assignment system → Lab 2 homework doc

Link within Lab 2:
- Use relative links: `[Team Contract](./templates/team-contract-template.md)`
- Link to course resources: `../resources/setup/python-setup.md`

---

## Student GitHub Repository Structure

**Students should mirror this in their project repos:**

```
student-project-repo/
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt (or package.json)
│
├── docs/
│   ├── team-contract.md          ← From template
│   ├── capstone-proposal.md      ← From template
│   ├── setup.md
│   ├── architecture.png
│   └── irb-checklist.md (if applicable)
│
├── src/
│   ├── backend/
│   ├── frontend/
│   └── scripts/
│
├── tests/
├── data/ (sample data only)
└── .github/
    └── workflows/
```

**Make sure students understand:**
- `docs/` folder mirrors what they learned in Lab 2
- Templates from lab-2/templates/ go into their docs/
- Their repo structure should follow lab-2/templates/repo-structure.md

---

## Quick Reference Card (for Students)

Create a simple reference that students can bookmark:

```markdown
# Lab 2 Quick Reference

**Main Docs:**
- [Lab Overview](./README.md)
- [Homework Details](./homework-assignment.md)

**Templates (Copy These):**
- [Team Contract](./templates/team-contract-template.md)
- [Proposal](./templates/capstone-proposal-template.md)
- [Repo Structure](./templates/repo-structure.md)

**Step-by-Step Guides:**
- [GitHub Setup](./guides/github-setup-guide.md)
- [Writing Problem Statements](./guides/problem-statement-guide.md)
- [Assigning Roles](./guides/role-assignment-guide.md)
- [User Research Ethics](./guides/irb-light-guide.md)

**Due:** End of Week 2  
**Points:** 10  
**Submit:** GitHub repo URL
```

---

## Checklist: Is Your Lab 2 Folder Complete?

### Content Completeness
- [ ] README.md covers all essentials
- [ ] homework-assignment.md has detailed requirements
- [ ] instructor-guide.md has full lab plan
- [ ] All 4 templates are complete
- [ ] All 4 guides are thorough

### Quality Checks
- [ ] All links work (internal and external)
- [ ] No typos or grammar errors
- [ ] Consistent formatting across files
- [ ] Clear heading hierarchy
- [ ] Code blocks are formatted properly

### Accessibility
- [ ] Headings are semantic (H1, H2, H3)
- [ ] Images have alt text
- [ ] Tables are used appropriately
- [ ] Link text is descriptive

### Student Readiness
- [ ] Entry point (README) is clear
- [ ] Templates are easy to copy
- [ ] Guides are step-by-step
- [ ] FAQ addresses common questions

---


## Summary

This folder structure provides:

**For Students:**
- Clear entry point (README)
- Copy-paste templates
- Step-by-step guides
