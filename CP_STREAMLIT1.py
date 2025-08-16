import numpy as np
import pickle
import streamlit as st

#loading the model

model = pickle.load(open("customer_churn31.pkl", "rb"))

def customer_prediction(user_input):
    # convert data to an array
    customer_prediction = np.array(user_input)

     #reshape data into two dimensional array
    reshaped_array = input_array.reshape(1, -1)


    #getting prediction
    prediction = model.predict(reshaped_array)

    
    if prediction == 0:
        return "This customer will stay"
    
    
    else:
        return "This customer will go !!!"
    
    
def main():
    st.title("customer churn prediction")

    tenure = st.text_input("duration in the network")
    montant = st.text_input("top-up amount of the customer") 
    frequence_rech =st.text_input("number of times the customer refilled")
    revenue = st.text_input("monthly income of each client")
    on_net = st.text_input("total amount spent on a call using expresso")
    orange = st.text_input("Call to orange network")
    regularity = st.text_input("the times the client is active for 90 days")
    top_pack = st.text_input("the most active expresso package")
    freq_top_pack =  st.text_input("number of times the client has activated top_pack")
    

    performance = ""

    if st.button("Eligibility Result"):
        performance = customer_prediction([float(tenure), float(montant), float( frequence_rech), float(revenue), float(on_net), float(orange), float(regularity), float(top_pack), float(freq_top_pack )])
        st.success(performance) 

if __name__ == "__main__":
        main()           
