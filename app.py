import streamlit as st
from reviewer import review_code

st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.title("GenAI - AI Python Code Reviewer")

with st.form('review_form'):
    code = st.text_area(
        "Paste your Python code here:",
        height=300,
        placeholder='def foo():\n    pass'
    )
    submit = st.form_submit_button("Review Code")

if submit:
    if not code.strip():
        st.warning("Please paste some Python code to review.")
    else:
        with st.spinner("Reviewing code..."):
            result = review_code(code)

        issues = result.get("issues", [])
        fixed_code = result.get("fixed_code", "")
        explanation = result.get("explanation", "")

        st.subheader("Issues Found")
        if issues:
            for i, issue in enumerate(issues, 1):
                st.markdown(
                    f"**{i}. {issue.get('title', 'Unknown')}** — "
                    f"severity: {issue.get('severity', '')}"
                )
                st.write(issue.get('description', ''))
        else:
            st.success("No issues detected by the reviewer.")

        if fixed_code:
            st.subheader("Suggested Fixed Code")
            st.code(fixed_code, language="python")

        if explanation:
            st.subheader("Explanation")
            st.write(explanation)
