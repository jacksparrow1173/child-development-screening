import streamlit as st
import pandas as pd
from database import init_db, add_student, get_students
from scoring import DOMAINS, compute_scores, validate_question
from chart import generate_chart
from report import create_report


MIN_AGE = 24
MAX_AGE = 60


RESPONSE_OPTIONS = {
    "0 - Age appropriate / Consistently": 0,
    "1 - Sometimes / Mild concern": 1,
    "2 - Rarely / Never / Significant concern": 2,
    "NA - Not observed / No opportunity": None
}


st.set_page_config(page_title="Child Development Screening", layout="wide")

init_db()


st.title("Developmental Red Flag Screening System")


st.sidebar.title("Dashboard")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Register Student",
        "Fill Questionnaire",
        "Reports"
    ]
)



# -----------------------
# Register Student
# -----------------------

if menu == "Register Student":

    st.header("Student Registration")

    name = st.text_input("Child Name")

    age = st.number_input(
        "Age (months)",
        min_value=MIN_AGE,
        max_value=MAX_AGE,
        step=1
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    school = st.text_input("School")

    if st.button("Register Student"):

        if name == "" or school == "":
            st.error("Please fill all fields")

        else:

            student = {
                "id": name,
                "name": name,
                "age_months": age,
                "gender": gender,
                "school": school
            }

            add_student(student)

            st.success("Student Registered Successfully")


# -----------------------
# Fill Questionnaire
# -----------------------

elif menu == "Fill Questionnaire":

    st.header("Developmental Questionnaire")

    students = get_students()

    if len(students) == 0:

        st.warning("No students registered")

    else:

        student_name = st.selectbox(
            "Select Student",
            students["name"]
        )

        role = st.selectbox(
            "Filled by",
            ["Parent", "Teacher"]
        )

        student = students[students["name"] == student_name].iloc[0]

        age = int(student["age_months"])

        st.info(f"Child Age: {age} months")

        scores = {}

        for domain, questions in DOMAINS.items():

            st.subheader(domain)

            vals = []

            for q in questions:

                valid = validate_question(age, q)

                if valid:

                    option = st.selectbox(
                        q,
                        list(RESPONSE_OPTIONS.keys()),
                        key=domain + q
                    )

                else:

                    option = st.selectbox(
                        f"{q} (Milestone expected later)",
                        list(RESPONSE_OPTIONS.keys()),
                        index=3,
                        key=domain + q
                    )

                vals.append(RESPONSE_OPTIONS[option])

            scores[domain] = vals


        if st.button("Generate Result"):

            domain_scores, total, percent, risk = compute_scores(scores)

            result = {
                "domain_scores": domain_scores,
                "total": total,
                "percent": percent,
                "risk": risk
            }

            chart = generate_chart(domain_scores)

            pdf = create_report(student, result, chart)

            st.subheader("Screening Result")

            st.metric("Risk Level", risk)
            st.metric("Risk Percentage", round(percent, 2))
            st.metric("Total Score", total)

            st.image(chart)

            with open(pdf, "rb") as f:

                st.download_button(
                    label="Download PDF Report",
                    data=f,
                    file_name="development_report.pdf",
                    mime="application/pdf"
                )


# -----------------------
# Reports
# -----------------------

elif menu == "Reports":

    st.header("Registered Students")

    students = get_students()

    if len(students) == 0:

        st.warning("No students available")

    else:

        st.dataframe(students)