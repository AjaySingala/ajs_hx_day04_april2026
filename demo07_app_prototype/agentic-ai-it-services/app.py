import streamlit as st
from graph.workflow import build_graph

# Build LangGraph workflow
graph = build_graph()

st.title("🚀 Agentic AI for IT Services")

# Initialize session state (persists data across reruns)
if "result" not in st.session_state:
    st.session_state.result = None

if "requirement" not in st.session_state:
    st.session_state.requirement = ""

# Input requirement
requirement = st.text_area("Enter Business Requirement", value=st.session_state.requirement)

# Run initial workflow
if st.button("Run AI Workflow"):

    st.session_state.requirement = requirement

    state = {
        "requirement": requirement,
        "feedback": ""  # No feedback in first run
    }

    result = graph.invoke(state)

    # Save result in session state
    st.session_state.result = result


# Show results if available
if st.session_state.result:

    result = st.session_state.result

    st.subheader("📘 Knowledge Assistant")
    st.write(result.get("knowledge_answer"))

    st.subheader("📊 Effort Estimation")
    st.write(result.get("estimate"))

    st.subheader("🏗️ Solution Architecture")
    st.write(result.get("solution"))

    # Feedback input
    feedback = st.text_input("Enter Feedback to Refine Solution")

    # Run refinement ONLY when feedback is entered
    if st.button("Refine Solution"):

        state = {
            "requirement": st.session_state.requirement,
            "solution": result.get("solution"),
            "feedback": feedback
        }

        refined_result = graph.invoke(state)

        st.subheader("🔁 Refined Solution")
        st.write(refined_result.get("refined_solution"))