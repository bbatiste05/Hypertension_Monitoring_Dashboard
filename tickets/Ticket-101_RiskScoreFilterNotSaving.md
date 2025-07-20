**Ticket ID:** TICKET-101  
**Type:** Incident – Functionality  
**Module:** Ambulatory Reports → Clarity/Radar  

**Submitted by:** Dr. Smith (Primary Care)  
**Summary:** “Risk Score” filter selection resets after viewing report  

---

### 📝 Description:

Provider reports that when filtering by Risk Score on the Hypertension Monitoring Dashboard, the selection is not retained after navigating away from the page.

---

### 🔄 Reproduction Steps:

1. Open Hypertension Dashboard
2. Use sidebar to filter: Risk Score = 4–5
3. Navigate to another module (e.g., Reports > Recent Visits)
4. Return to dashboard

→ Filter resets to default

---

### ✅ Resolution:

Confirmed dashboard session state was not preserved across tabs. Updated Streamlit to cache the most recent filter state using `st.session_state`. Validated with Dr. Smith and marked resolved.

