import streamlit as st
import google.generativeai as genai

# Page ခေါင်းစဉ် သတ်မှတ်ခြင်း
st.set_page_config(page_title="Burmese Movie Recap", page_icon="🎬")

# 1. API Key ချိတ်ဆက်ခြင်း (Cloud အတွက် လုံခြုံသောနည်းလမ်း)
# သတိပြုရန်: ဒီအဆင့်ကြောင့် သင့်ကွန်ပျူတာ (Local) မှာ Error တက်နိုင်ပါတယ်။ 
# GitHub နဲ့ Cloud ပေါ်ရောက်မှ အလုပ်လုပ်ပါလိမ့်မယ်။
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except FileNotFoundError:
    st.error("API Key ရှာမတွေ့ပါ။ Streamlit Cloud ၏ Secrets ထဲတွင် ထည့်ပေးရန် လိုအပ်ပါသည်။")
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
                # Model ရွေးချယ်ခြင်း
                model = genai.GenerativeModel('gemini-pro')
                
                # Prompt (AI ကို ခိုင်းစေမည့် ပုံစံ)
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
streamlit
google-generativeai
