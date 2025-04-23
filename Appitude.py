import streamlit as st
import time  # For creating delay

# Title of the test app
st.title("GreenLoom Skill Certification Test / ग्रीनलूम कौशल प्रमाणन परीक्षा")

# Instructions
st.write("""
Welcome to the GreenLoom Skill Certification Test!  
Answer the following 10 questions to complete the test. Choose the best answer for each question.  
गुड मोर्निंग! ग्रीनलूम कौशल प्रमाणन परीक्षा में आपका स्वागत है।  
निम्नलिखित 10 सवालों के उत्तर दें और परीक्षा पूरी करें। प्रत्येक सवाल का सबसे अच्छा उत्तर चुनें।
""")

# Show a loading spinner with message
with st.spinner("IBM Granite: Preparing Questions... / आईबीएम ग्रेनाइट: प्रश्न तैयार कर रहे हैं..."):
    time.sleep(3)  # Simulate loading for 3 seconds

# Define the questions and options
questions = [
    {
        "question_en": "What is the primary purpose of a drainage system?",
        "question_hi": "ड्रेनेज सिस्टम का मुख्य उद्देश्य क्या है?",
        "options": [
            "To collect water / पानी जमा करना", 
            "To direct water to the correct path / पानी को सही दिशा में बहाना", 
            "To store water / पानी स्टोर करना"
        ],
        "answer": "To direct water to the correct path / पानी को सही दिशा में बहाना"
    },
    {
        "question_en": "Which of these pipes is lightest?",
        "question_hi": "इनमें से कौन सा पाइप हल्का होता है?",
        "options": [
            "RCC", 
            "PVC", 
            "Iron pipe / लोहे का पाइप"
        ],
        "answer": "PVC"
    },
    {
        "question_en": "What should you always wear during excavation?",
        "question_hi": "खुदाई के दौरान आपको हमेशा क्या पहनना चाहिए?",
        "options": [
            "Mobile phone / मोबाइल फोन", 
            "Gloves and helmet / दस्ताने और हेलमेट", 
            "Loud music / तेज़ संगीत"
        ],
        "answer": "Gloves and helmet / दस्ताने और हेलमेट"
    },
    {
        "question_en": "Which pipe is commonly used in drainage systems?",
        "question_hi": "ड्रेनेज सिस्टम में कौन सा पाइप सामान्यतः उपयोग होता है?",
        "options": [
            "Copper pipe / तांबे का पाइप", 
            "PVC pipe / पीवीसी पाइप", 
            "Rubber pipe / रबर पाइप"
        ],
        "answer": "PVC pipe / पीवीसी पाइप"
    },
    {
        "question_en": "What is the purpose of micro-training?",
        "question_hi": "माइक्रो-ट्रेनिंग का उद्देश्य क्या है?",
        "options": [
            "To enhance knowledge / ज्ञान बढ़ाना", 
            "To pass time / समय बर्बाद करना", 
            "To skip the training process / ट्रेनिंग प्रक्रिया को छोड़ना"
        ],
        "answer": "To enhance knowledge / ज्ञान बढ़ाना"
    },
    {
        "question_en": "What is drainage primarily related to?",
        "question_hi": "ड्रेनेज मुख्यतः किससे संबंधित है?",
        "options": [
            "Flood management / बाढ़ प्रबंधन", 
            "Construction of walls / दीवारों का निर्माण", 
            "Decoration / सजावट"
        ],
        "answer": "Flood management / बाढ़ प्रबंधन"
    },
    {
        "question_en": "Which safety equipment is most critical during work in a drainage system?",
        "question_hi": "ड्रेनेज सिस्टम में काम करते समय सबसे महत्वपूर्ण सुरक्षा उपकरण कौन सा है?",
        "options": [
            "Helmet / हेलमेट", 
            "Watch / घड़ी", 
            "Laptop / लैपटॉप"
        ],
        "answer": "Helmet / हेलमेट"
    },
    {
        "question_en": "What is the main material used in drainage systems?",
        "question_hi": "ड्रेनेज सिस्टम में मुख्य सामग्री क्या है?",
        "options": [
            "Wood / लकड़ी", 
            "Plastic / प्लास्टिक", 
            "Metal / धातु"
        ],
        "answer": "Plastic / प्लास्टिक"
    },
    {
        "question_en": "How is a Skill Passport beneficial for workers?",
        "question_hi": "कौशल पासपोर्ट श्रमिकों के लिए कैसे फायदेमंद है?",
        "options": [
            "Gives a certificate for leisure / आराम के लिए प्रमाण पत्र देता है", 
            "Converts informal skills to formal recognition / अनौपचारिक कौशल को औपचारिक पहचान में बदलता है", 
            "Provides free lunch / मुफ्त भोजन प्रदान करता है"
        ],
        "answer": "Converts informal skills to formal recognition / अनौपचारिक कौशल को औपचारिक पहचान में बदलता है"
    },
    {
        "question_en": "What should be done before installing a drainage system?",
        "question_hi": "ड्रेनेज सिस्टम स्थापित करने से पहले क्या किया जाना चाहिए?",
        "options": [
            "Dig the ground / ज़मीन खोदें", 
            "Plan and survey the site / स्थल की योजना बनाएं और सर्वे करें", 
            "Wait for instructions / निर्देशों का इंतजार करें"
        ],
        "answer": "Plan and survey the site / स्थल की योजना बनाएं और सर्वे करें"
    }
]

# Function to display questions and collect answers
answers = []
for i, q in enumerate(questions):
    st.write(f"**Question {i + 1}:**")
    st.write(f"**English:** {q['question_en']}")
    st.write(f"**Hindi:** {q['question_hi']}")
    answer = st.radio(f"Select the best answer for question {i + 1}", q['options'], key=i)
    answers.append(answer)

# Submit button to evaluate the test
if st.button("Submit Test / परीक्षा सबमिट करें"):
    score = 0
    for i in range(len(questions)):
        if answers[i] == questions[i]['answer']:
            score += 1
    
    # Display the score
    st.write(f"**Your score: {score} out of 10**")
    
    if score >= 8:
        st.success("Congratulations! You passed the test. You are ready for the next steps. / बधाई हो! आपने परीक्षा पास की। आप अगले कदम के लिए तैयार हैं।")
        st.balloons()
    elif score >= 5:
        st.warning("You have some gaps in knowledge. Please review and try again. / आपके ज्ञान में कुछ अंतराल हैं। कृपया पुनः प्रयास करें।")
    else:
        st.error("Unfortunately, you did not pass the test. Please review the training and try again. / दुर्भाग्यवश, आपने परीक्षा पास नहीं की। कृपया ट्रेनिंग की समीक्षा करें और पुनः प्रयास करें।")
