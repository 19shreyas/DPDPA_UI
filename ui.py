import streamlit as st

def set_custom_css():
    st.markdown("""
    <style>
    /* Sidebar: white text */
    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #2E2E38;
    }

    /* Main content: dark text (force override) */
    section.main div.block-container {
        color: #2E2E38 !important;
    }

    /* Fix titles and subheaders too */
    h1, h2, h3, h4, h5, h6, p, span, div {
        color: #2E2E38 !important;
    }
    </style>
    """, unsafe_allow_html=True)



# --- Sidebar Navigation ---
st.set_page_config(page_title="DPDPA Compliance Tool", layout="wide")
set_custom_css()
st.sidebar.image(".images/EY-Parthenon_idpWq1a8hl_0.png", width=150)
st.sidebar.title("📘 Navigation")

menu = st.sidebar.radio("Go to", [
    "🏠 Homepage",
    "📄 Create Policy",
    "🧩 Match to DPDPA",
    "📊 Dashboard & Reports",
    "📚 Knowledge Assistant",
    "⚙️ Admin Settings"
])

# --- Homepage ---
if menu == "🏠 Homepage":
    st.title("DPDPA Compliance Tool")
    st.markdown("""
    Welcome to the Digital Personal Data Protection Act (DPDPA) Compliance Platform.
    Use the navigation panel to begin generating or matching your policy to India's latest data protection laws.
    """)

# --- Create Policy ---
elif menu == "📄 Create Policy":
    st.title("Create Policy")
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Full Policy Generator", "Section-wise Generator", "Lifecycle-wise Template", 
        "GPT Draft Assistant", "Saved Drafts"])

    with tab1:
        st.subheader("Full Policy Generator")
        st.text_area("Enter your complete policy draft:", height=300)
        st.button("Generate Suggestions with GPT")

    with tab2:
        st.subheader("Section-wise Generator")
        section = st.selectbox("Choose Section", ["Notice", "Consent", "Data Principal Rights", "Security"])
        st.text_area(f"Draft for {section}:", height=200)
        st.button("Suggest Completion")

    with tab3:
        st.subheader("Lifecycle-wise Template")
        st.markdown("Fill stage-specific privacy info:")
        stages = ["Collection", "Processing", "Storage", "Sharing", "Erasure"]
        for stage in stages:
            st.text_area(f"{stage} Stage", key=stage)

    with tab4:
        st.subheader("GPT-Assisted Draft Builder")
        prompt = st.text_input("Describe your need (e.g. privacy for HR data):")
        st.button("Generate Draft")

    with tab5:
        st.subheader("Saved Drafts")
        st.dataframe({"Draft": ["HR Policy", "Marketing Policy"], "Last Modified": ["2025-05-10", "2025-05-01"]})

# --- Match to DPDPA ---
elif menu == "🧩 Match to DPDPA":
    st.title("Match Policy to DPDPA")

    st.header("1. Upload Your Policy Document")
    upload_option = st.radio("Choose input method:", ["Upload File", "Paste Policy Text"], index=0)
    if upload_option == "Upload File":
        policy_file = st.file_uploader("Upload .docx or .txt file", type=["docx", "txt"])
        policy_text = None
    else:
        policy_text = st.text_area("Paste your policy text here:", height=250)
        policy_file = None

    st.header("2. Choose Matching Level")
    match_level = st.radio("How do you want to match?", [
        "Full Policy Match (default)", "Section-wise Match"], index=0)

    st.header("3. Select Scope of Evaluation")
    scope = st.selectbox("Scope", [
        "Entire DPDPA (default)", "Only Act", "Only Rules", "Custom Sections"], index=0)
    if scope == "Custom Sections":
        custom_sections = st.multiselect("Select specific sections to match against", [
            "Section 4: Lawful Processing", "Section 5: Notice", "Section 6: Rights", 
            "Section 7: Children’s Data", "Section 8: Data Processors", "Section 9: Breach", "Section 10: Grievance"])
    else:
        custom_sections = []

    st.header("4. Industry Context (Optional)")
    industry = st.selectbox("Industry Filter", ["General", "Automotive", "Healthcare", "Fintech", "Other"])
    if industry == "Other":
        custom_industry = st.text_input("Specify your industry")
    else:
        custom_industry = None

    st.header("5. Run Compliance Check")
    if st.button("🔍 Run Compliance Check"):
        if policy_file or policy_text:
            with st.spinner("Running GPT-based compliance evaluation..."):
                st.success("Compliance check complete.")
                st.metric("Overall Compliance", "78%")
                st.markdown("""
                ### Clause-wise Evaluation:
                - **Section 5 (Notice):** ✅ Matched
                - **Section 7 (Children’s Data):** ❌ Missing Guardian Consent Clause
                - **Section 9 (Breach):** ⚠️ Breach timeline undefined
                """)
        else:
            st.warning("Please upload a file or paste policy text.")

    st.header("6. Generate / Export Output")
    export_format = st.selectbox("Choose export format", ["PDF", "CSV", "JSON"])
    include_details = st.checkbox("Include suggested rewrites and clause-level insights")
    if st.button("📥 Download Output"):
        st.success("Export ready (simulated). File will include compliance results and recommendations.")

# --- Dashboard & Reports ---
elif menu == "📊 Dashboard & Reports":
    st.title("Dashboard & Reports")
    st.metric("Overall Compliance", "82%", "+7%")
    st.progress(0.82)
    st.subheader("Risk & GPT Insights")
    st.write("\n- Consent missing in 2 sections\n- Breach response undefined\n")
    st.subheader("Activity Tracker")
    st.dataframe({"Task": ["Upload Policy", "Review Results"], "Status": ["Done", "Pending"]})
    st.download_button("Download Full Report", "Sample Report Data...", file_name="dpdpa_report.txt")

# --- Knowledge Assistant ---
elif menu == "📚 Knowledge Assistant":
    st.title("Knowledge Assistant")
    with st.expander("📘 DPDPA + DPDP Rules Summary"):
        st.markdown("Digital Personal Data Protection Act focuses on consent, purpose limitation, etc.")
    with st.expander("📖 Policy Glossary"):
        st.write({"Data Principal": "The individual to whom personal data relates."})
    with st.expander("🔍 Clause-by-Clause Reference"):
        st.markdown("Section 5: Notice - Clear, itemised, accessible...")
    with st.expander("🆘 Help Centre"):
        st.write("Email: support@dpdpatool.com | Call: +91-XXX-XXX")

# --- Admin Settings ---
elif menu == "⚙️ Admin Settings":
    st.title("Admin Settings")
    st.subheader("User & Role Management")
    st.write("Admin | Reviewer | Editor")
    st.subheader("Organization Profile")
    st.text_input("Organization Name")
    st.text_input("Sector")
    st.subheader("Audit Log Controls")
    st.checkbox("Enable audit logs")
    st.subheader("Data Backup & Export")
    st.button("Download Backup")
