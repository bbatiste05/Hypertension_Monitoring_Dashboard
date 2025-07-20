**Ticket ID:** TICKET-102  
**Type:** Enhancement  
**Module:** Ambulatory Analytics – Risk Reporting  

**Requested by:** Nursing Manager (Outreach Team)  
**Summary:** “Can we highlight patients with systolic BP ≥180 in red?”

---

### ✅ Request:

Update the bar chart and patient table to apply a red tag or highlight to patients with **hypertensive crisis** levels.

---

### 🔄 Action Taken:

Modified dashboard logic to apply custom color formatting using Streamlit’s `st.markdown` and Plotly conditional styling for:
- `systolic ≥ 180` → red highlight
- `systolic 160–179` → orange

Change reviewed by Clinical Quality Committee.



