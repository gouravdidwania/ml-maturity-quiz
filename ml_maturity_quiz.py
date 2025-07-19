import streamlit as st

st.title("🚀 ML Project Maturity Quiz")

score = 0

st.subheader("1. Do your projects live entirely in notebooks?")
q1 = st.radio("", ["🟢 Yes", "🔵 No, they have modular scripts and folders", "🔴 They're deployed as APIs or microservices"])
score += [1, 2, 3][["🟢 Yes", "🔵 No, they have modular scripts and folders", "🔴 They're deployed as APIs or microservices"].index(q1)]

st.subheader("2. Have you ever used Docker to package a model?")
q2 = st.radio("", ["🟢 No", "🔵 Once or twice", "🔴 Regularly"])
score += [1, 2, 3][["🟢 No", "🔵 Once or twice", "🔴 Regularly"].index(q2)]

st.subheader("3. Do you track experiments or monitor data drift?")
q3 = st.radio("", ["🟢 What's data drift?", "🔵 I've used MLflow or DVC", "🔴 I've automated this with alerting systems"])
score += [1, 2, 3][["🟢 What's data drift?", "🔵 I've used MLflow or DVC", "🔴 I've automated this with alerting systems"].index(q3)]

st.subheader("4. Are your models retrained automatically based on new data?")
q4 = st.radio("", ["🟢 No", "🔵 Manually retrained when needed", "🔴 Yes, via orchestration tools"])
score += [1, 2, 3][["🟢 No", "🔵 Manually retrained when needed", "🔴 Yes, via orchestration tools"].index(q4)]

st.subheader("5. Have you ever implemented a custom architecture or novel algorithm?")
q5 = st.radio("", ["🟢 No", "🔵 Tweaked existing ones", "🔴 Yes, and/or published research"])
score += [1, 2, 3][["🟢 No", "🔵 Tweaked existing ones", "🔴 Yes, and/or published research"].index(q5)]

st.markdown("---")
st.write("### 🎯 Your Total Score:", score)

if score <= 7:
    st.success("Level 1–2: You're just getting started—great time to build foundational skills!")
elif score <= 10:
    st.info("Level 3: You’re building solid workflows. Time to explore tools like Docker, MLflow.")
elif score <= 13:
    st.warning("Level 4: You’re deploying models and automating parts. Push toward retraining and orchestration.")
else:
    st.balloons()
    st.success("Level 5: You’re running ML like a pro! Production-grade workflows and MLOps maturity.")

