**Ticket ID:** TICKET-103  
**Type:** Enhancement  
**Module:** Clinical Quality → Reports → EpicCare  

**Requestor:** Clinical Supervisor (Ambulatory Ops)  
**Summary:** “Can I export a CSV just for my patients?”

---

### ✅ Request:

Add download button for filtered table output by provider.

---

### 🔄 Resolution:

Added an `st.download_button()` below the data table, scoped to current filter selection. CSV filename includes provider name and timestamp. Tested for multiple users.

