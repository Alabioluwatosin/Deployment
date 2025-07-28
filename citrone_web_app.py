import numpy as np
import pickle
import streamlit as st

#Loading the model

model = pickle.load(open(r"C:\Users\the6t\OneDrive\Desktop\Gomycode\logistic_model_1.pkl", "rb"))

def performance_prediction(user_input):
    # convert data to an array
    input_array = np.array(user_input)

    #reshape data into two dimensional array
    reshaped_array = input_array.reshape(1, -1)

    #getting prediction
    prediction = model.predict(reshaped_array)

    if prediction == 0:
        return "This student did not pass"

    else:
        return "This student passed !!!"


def main():
    st.title("Citrone performance Web App")

    Quiz_summary = st.text_input("Quiz summary score")
    Assignment_summary = st.text_input("Assignment summary score") 
    Grade_point_Average =st.text_input("Learner's Grade point Average score")
    Age = st.text_input("Learner's age")
    Children = st.text_input("Does a learner have children? 1 for yes/0 for No")
    Completed_Nysc = st.text_input("Completed Nysc ? 1 for yes/0 for No")
    Gender = st.text_input("What is learner's gender? 1 for Male/0 for Female")

    performance = ""

    if st.button("Eligibility Result"):
        performance = performance_prediction([float(Quiz_summary), float(Assignment_summary), float(Grade_point_Average), int(Age), int(Children), int(Completed_Nysc), int(Gender)])
        st.success(performance) 


if __name__ == "__main__":
    main()           