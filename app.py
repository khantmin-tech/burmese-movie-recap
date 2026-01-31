import streamlit as st
import google.generativeai as genai

# Page ခေါင်းစဉ်
st.set_page_config(page_title="Burmese Movie Recap", page_icon="🎬")

# 1. API Key ချိတ်ဆက်ခြင်း (Streamlit Secrets မှ ယူမည်)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except FileNotFoundError:
    # Local (ကွန်ပျူတာ) မှာ run ရင် ဒီ Error ပြပါလိမ့်မယ်။ Cloud ရောက်မှ အဆင်ပြေပါမယ်။
    st.error("API Key မတွေ့ပါ။ Streamlit Cloud ၏ Secrets ထဲတွင် ထည့်ပေးရန် လိုအပ်ပါသည်။")
    st.stop()

# 2. App ဒီဇိုင်း
st.title("🎬 Burmese Movie Recap Generator")
st.write("ရုပ်ရှင် Script (သို့) ဇာတ်လမ်းအကျဉ်းကို ထည့်ပြီး မြန်မာလို ပြန်ရေးခိုင်းနိုင်ပါသည်။")

# User စာရိုက်ထည့်မည့် နေရာ
user_input = st.text_area("စာသားများကို ဒီမှာ Paste လုပ်ပါ (English/Myanmar)", height=200)

# 3. Gemini ကို အလုပ်ခိုင်းခြင်း
if st.button("Recap လုပ်မယ် (Generate)"):
    if user_input:
        with st.spinner("AI က စဉ်းစားနေပါတယ်... ခဏစောင့်ပါ..."):
            try:
                # Model အသစ် (gemini-1.5-flash) ကို သုံးထားသည်
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # AI ကို ခိုင်းစေမည့် စာသား
                prompt = f"""
                You are a professional movie recap narrator. 
                Please summarize the following text into a highly engaging Burmese movie recap script.
                The tone should be exciting and suitable for a YouTube video.
                
                Input Text:
                {user_input}
                """
                
                # အဖြေထုတ်ခြင်း
                response = model.generate_content(prompt)
                st.subheader("ရရှိလာသော အဖြေ (Result):")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Error ဖြစ်သွားပါတယ်: {e}")
    else:
        st.warning("ကျေးဇူးပြု၍ စာသားအရင်ထည့်ပါ။")
