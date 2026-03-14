import pandas as pd
import os

STUDENT_FILE = "data/students.csv"


def init_db():

    if not os.path.exists("data"):
        os.mkdir("data")

    if not os.path.exists(STUDENT_FILE):

        df = pd.DataFrame(columns=[
            "id",
            "name",
            "age_months",
            "gender",
            "school"
        ])

        df.to_csv(STUDENT_FILE,index=False)


def add_student(student):

    df = pd.read_csv(STUDENT_FILE)

    df = pd.concat([df,pd.DataFrame([student])],ignore_index=True)

    df.to_csv(STUDENT_FILE,index=False)


def get_students():

    return pd.read_csv(STUDENT_FILE)