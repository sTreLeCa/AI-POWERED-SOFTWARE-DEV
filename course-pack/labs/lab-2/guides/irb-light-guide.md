# IRB Light Guide & Checklist

**For Week 2 Lab | Building AI-Powered Applications**

---

## What is This?

**IRB** = Institutional Review Board

For full research studies, you'd need formal IRB approval. But since this is a **course project** with limited user testing, we use a simplified "IRB Light" checklist to ensure you're treating users ethically and following data protection rules.

**Required if:** Your project involves any interaction with human participants (user testing, interviews, surveys, data collection).

---

## Do You Need This?

Answer these questions:

- [ ] Will you ask people to test your application?
- [ ] Will you interview users about their needs or experiences?
- [ ] Will you collect any data from users (even anonymized)?
- [ ] Will you observe people using your system?
- [ ] Will you send surveys or questionnaires?

**If you checked ANY box above → Complete this checklist and submit with your proposal**

**If your project is purely technical with no human subjects → You can skip this**

---

## Core Principles

Your user research must follow these principles:

### 1. Informed Consent
- Users must know what they're participating in
- Users must know how their data will be used
- Users can withdraw at any time without penalty

### 2. Privacy & Confidentiality
- Don't collect more data than you need
- Anonymize user data
- Store data securely
- Delete data when done

### 3. Do No Harm
- Don't deceive participants
- Don't expose them to risks
- Don't pressure them to participate

### 4. Respect Autonomy
- Participation is voluntary
- Users can skip questions or tasks
- Users can withdraw at any time

---

## IRB Light Checklist

Complete this and submit as `docs/irb-checklist.md` with your proposal.

---

### Participant Information

**1. Who are your participants?**
- [ ] Adults (18+)
- [ ] Minors (under 18) ⚠️ Requires special care - consult instructor
- [ ] Vulnerable populations (e.g., patients, prisoners) ⚠️ Requires full IRB - not suitable for this course

**2. How many participants?**
- Estimated total: [e.g., 5-10 participants]

**3. How will you recruit them?**
- [ ] Friends and classmates (disclosed in consent)
- [ ] Social media or flyers
- [ ] Instructor-provided participant pool
- [ ] Other: [describe]

**4. Is participation voluntary?**
- [ ] Yes, and participants can withdraw at any time

**5. Will participants be compensated?**
- [ ] No compensation
- [ ] Small gift (e.g., coffee gift card, worth ~$10)
- [ ] Course credit (if instructor-approved)
- [ ] Other: [describe]

⚠️ **Note:** Compensation should be reasonable, not coercive.

---

### Data Collection

**6. What data will you collect?**

Check all that apply:
- [ ] Survey responses
- [ ] Interview responses
- [ ] Screen recordings
- [ ] Audio recordings
- [ ] Video recordings
- [ ] Usage analytics (clicks, time on task)
- [ ] System logs (errors, performance)
- [ ] User-generated content (text, images)
- [ ] Other: [describe]

**7. Will you collect any of the following sensitive information?**

⚠️ If you check ANY of these, you likely need full IRB approval. Consult instructor immediately.

- [ ] Full names
- [ ] Email addresses or contact info (beyond anonymous IDs)
- [ ] Demographic info beyond basic age/role (e.g., race, religion, political affiliation)
- [ ] Health information
- [ ] Financial information
- [ ] Anything that could identify specific individuals
- [ ] Information about illegal activities

**8. How will you protect participant privacy?**
- [ ] Assign anonymous participant IDs (P1, P2, etc.)
- [ ] Don't collect names or contact info (or delete after scheduling)
- [ ] Store data in password-protected location
- [ ] Don't include personally identifiable information in public repo or reports
- [ ] Aggregate data in reports (no individual quotes unless anonymized)

**9. Where will you store the data?**
- [ ] Password-protected Google Drive folder (shared only with team)
- [ ] Encrypted local storage
- [ ] KIU-approved storage system
- [ ] Other: [describe]

⚠️ **Never store raw user data in your public GitHub repo.**

**10. How long will you keep the data?**
- [ ] Until end of semester, then delete
- [ ] Permanently, but fully anonymized
- [ ] Other: [describe]

---

### Informed Consent

**11. How will you obtain consent?**
- [ ] Written consent form (signed before participation)
- [ ] Digital consent form (checkbox + timestamp)
- [ ] Verbal consent (recorded)

**12. Will you use the consent template provided?**
- [ ] Yes, adapted to my study
- [ ] No, using my own (attach to proposal)

**13. What will you tell participants?**

Your consent form must include:
- [ ] Purpose of the study
- [ ] What participants will be asked to do
- [ ] How long it will take
- [ ] What data will be collected
- [ ] How data will be used
- [ ] How privacy will be protected
- [ ] That participation is voluntary
- [ ] That they can withdraw anytime
- [ ] Contact info for questions
- [ ] Contact info for complaints

---

### Risks & Benefits

**14. Are there any risks to participants?**

Common risks:
- [ ] Time/inconvenience (typically 30-60 min)
- [ ] Frustration if system doesn't work well
- [ ] Minor discomfort discussing the topic
- [ ] Potential privacy concerns if data leaked

⚠️ High-risk scenarios (require full IRB):
- [ ] Physical harm
- [ ] Psychological distress
- [ ] Legal risk
- [ ] Reputational harm
- [ ] Financial loss

**If you checked any high-risk scenarios, STOP. This requires full IRB review. Redesign your study.**

**15. How will you minimize risks?**
- [ ] Clear explanation of what to expect
- [ ] Participants can stop at any time
- [ ] Data is anonymized and secured
- [ ] System is tested before user studies
- [ ] No collection of sensitive personal information

**16. What are the benefits to participants?**
- [ ] Contributing to a useful tool
- [ ] Learning about AI applications
- [ ] Opportunity to influence design
- [ ] Compensation (if applicable)
- [ ] None (acknowledge this in consent form)

---

### Deception & Disclosure

**17. Will you deceive participants in any way?**
- [ ] No
- [ ] Yes → ⚠️ Explain why necessary and how you'll debrief

**Example of acceptable minimal deception:** "We told them the system was fully automated, but a human reviewed results for quality control. We disclosed this in the debrief."

**Example of unacceptable deception:** "We didn't tell them we were recording their screen." ❌

**18. Will participants know they're being recorded?**
- [ ] Yes, disclosed in consent
- [ ] No recording will happen
- [ ] N/A

---

### Special Populations

**19. Will any participants be:**
- [ ] Under 18? ⚠️ Requires parental consent + assent. Consult instructor.
- [ ] From a vulnerable group (prisoners, patients, etc.)? ⚠️ Requires full IRB.
- [ ] Your students (if you're a TA)? ⚠️ Power dynamic - must be truly voluntary.
- [ ] In a power relationship with you (boss, professor, etc.)? ⚠️ May not be able to freely consent.

**If you checked any of these, redesign your study or get full IRB approval.**

---

### Data Security

**20. Who has access to the raw data?**
- [ ] Only team members
- [ ] Team members + instructor
- [ ] Other: [describe]

**21. How will you ensure data security?**
- [ ] Password-protected files
- [ ] Encrypted storage
- [ ] Access controls (only team members have link/password)
- [ ] Data not stored on personal devices (or encrypted if so)
- [ ] Backups are also secure

**22. What will you do if data is compromised (laptop stolen, accidental share, etc.)?**
- [ ] Notify participants immediately
- [ ] Notify instructor immediately
- [ ] Document what happened
- [ ] Change security practices going forward

---

### Reporting & Publication

**23. How will you report results?**
- [ ] Aggregate data only (no individual responses)
- [ ] Anonymized quotes (no names or identifying info)
- [ ] Case studies with participant permission
- [ ] Other: [describe]

**24. Where will results be shared?**
- [ ] Course presentation / demo day
- [ ] Project documentation (public GitHub repo)
- [ ] Course portfolio
- [ ] Conference or publication (requires full IRB)

**25. Will participants' identities be revealed anywhere?**
- [ ] No, all anonymous
- [ ] Yes, with explicit written permission for each use

---

## Consent Template

Use this template, adapted to your study. Provide to participants before they start.

---

### **Participant Consent Form**

**Study Title:** [Your Project Title]

**Researchers:** [Your Names], [University]

**Purpose:** We are building [brief description of your AI application] as part of a course project. We want to test the system with real users to understand how well it works and where we can improve it.

**What You'll Do:** We will ask you to [describe tasks, e.g., "use our AI coding tutor to debug three Python errors"]. This will take approximately [X] minutes.

**Data Collection:** We will collect:
- [e.g., Screen recordings of your session]
- [e.g., Task completion times]
- [e.g., Your feedback via a short survey]

We will NOT collect:
- Your name or contact information (beyond an anonymous ID)
- [Add other things you won't collect]

**Privacy:** Your data will be:
- Assigned an anonymous ID (e.g., Participant 1)
- Stored in a password-protected folder accessible only to the research team
- Used only for this course project
- Deleted at the end of the semester

**Voluntary Participation:** Your participation is completely voluntary. You may:
- Decline to answer any question
- Stop at any time without penalty
- Withdraw your data after the session

**Risks:** There are minimal risks. You may experience:
- [e.g., Minor frustration if the system doesn't work perfectly]
- [e.g., Time investment of ~30 minutes]

**Benefits:** You will:
- [e.g., Contribute to improving an AI tool]
- [e.g., Receive a $10 coffee gift card as thanks]

**Questions or Concerns:**
- Research team: [your email]
- Course instructor: Zeshan.ahmad@kiu.edu.ge

**Consent:**
- [ ] I have read and understood this consent form
- [ ] I agree to participate in this study
- [ ] I agree to be recorded (if applicable)

**Participant Signature:** ______________________ **Date:** __________

**Or Digital Consent:**
By clicking "I Agree" below, you consent to participate under the terms described above.

[ I Agree - Start Study ]

---

## Tips for Ethical Research

### 1. Treat Participants with Respect
- Be on time
- Thank them for their time
- Listen to their feedback
- Don't dismiss their concerns

### 2. Be Transparent
- Don't hide what you're testing
- Explain how their data will be used
- Answer their questions honestly

### 3. Prioritize Privacy
- Don't ask for data you don't need
- Don't share raw data outside the team
- Anonymize everything in your reports

### 4. Handle Withdrawals Gracefully
- If someone wants to stop, let them
- Delete their data if they ask
- Don't pressure them to continue

### 5. Document Everything
- Keep signed consent forms
- Log who participated and when
- Note any issues or concerns
- Save this documentation (but not in public repo)

---

## Common Mistakes to Avoid

❌ **"We'll just have friends test it, no paperwork needed"**
- Even casual testing needs consent and privacy protection

❌ **"We're not publishing this, so ethics don't matter"**
- Ethics matter regardless of publication. You're still collecting data from humans.

❌ **"We'll ask for permission later"**
- Get consent BEFORE collecting any data

❌ **"We need their email to follow up"**
- Use anonymous IDs. If you need follow-up, get explicit permission separately.

❌ **"We'll test with kids because they love tech"**
- Minors require parental consent and special protections. Avoid unless absolutely necessary.

❌ **"We'll store test videos in our public repo for demonstration"**
- Never put user data in public repos, even if "anonymized." Risk is too high.

---

## Approval Process for This Course

1. **Complete this checklist** as part of your Week 2 proposal
2. **Include your consent form** (adapted from template)
3. **Instructor reviews** and provides feedback
4. **Get approval before recruiting any participants**
5. **Conduct research** following approved plan
6. **Report any issues** to instructor immediately

**Do NOT start user testing until your IRB checklist is approved.**

---

## When You Need Full IRB

Consult instructor and university IRB if:
- Working with minors
- Collecting sensitive personal data (health, financial, etc.)
- Studying vulnerable populations
- Research involves more than minimal risk
- Planning to publish in academic venues

**Full IRB can take weeks to months. Plan accordingly or redesign your study.**

---

## After Your Study

### In Your Final Report, Include:

1. **Number of participants**
2. **Demographics (aggregate only)**
   - E.g., "5 participants, ages 20-24, 3 CS majors, 2 non-CS"
3. **Data collection methods**
4. **Anonymized results**
   - No individual identifying information
   - Use participant IDs if sharing quotes
5. **Limitations**
   - Small sample size, convenience sampling, etc.

### Clean Up Your Data:

- [ ] Delete recordings (or anonymize permanently)
- [ ] Remove any accidentally collected personal info
- [ ] Keep only anonymized summaries for your report
- [ ] Verify nothing sensitive is in your public repo

---

## Checklist Summary

Before submitting with your proposal, confirm:

- [ ] I've determined whether my project needs this checklist (user testing = yes)
- [ ] I've completed all relevant sections above
- [ ] I've adapted the consent template for my study
- [ ] I understand I cannot start user testing until approved
- [ ] I know how to protect participant privacy
- [ ] I have a plan for secure data storage
- [ ] I know what to do if something goes wrong
- [ ] I will not work with minors or vulnerable populations without full IRB

---

## Resources

- [OWASP AI Privacy Guidelines](https://owasp.org/www-project-ai-security-and-privacy-guide/)
- [GDPR Basics for Researchers](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/)
- [ACM Code of Ethics](https://www.acm.org/code-of-ethics)
- [IEEE Ethics Guidelines](https://www.ieee.org/about/corporate/governance/p7-8.html)

---

**Questions?** Email Zeshan.ahmad@kiu.edu.ge or ask during office hours.

**Remember:** Ethical research protects both participants and researchers. Take it seriously.
