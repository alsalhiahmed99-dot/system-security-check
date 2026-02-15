import streamlit as st
import time
import random

# إعدادات الصفحة
st.set_page_config(page_title="Security System", page_icon="🛡️")

# ستايل الهكر
st.markdown("<style>.stApp { background-color: #000000; color: #00FF41; }</style>", unsafe_allow_html=True)

# حالة الجلسة
if 'run' not in st.session_state:
    st.session_state.run = False

if not st.session_state.run:
    st.title("System Security Check")
    if st.button("Start Scan"):
        st.session_state.run = True
        st.rerun()
else:
    t = st.empty()
    logs = ""
    # الأوامر العربية حطيناها في متغيرات بسيطة جداً
    m1 = "جاري الاتصال بالسيرفر..."
    m2 = "اختراق النظام... تم"
    m3 = "سحب الصور والملفات..."
    m4 = "فتح الكاميرا الأمامية..."
    
    for m in [m1, m2, m3, m4]:
        logs += "> " + m + "\n"
        t.code(logs)
        time.sleep(3)

    st.write("---")
    # التهديدات النهائية
    st.error("🚨 تم الاختراق بنجاح 🚨")
    
    try:
        st.image("victim.png", caption="Identity Confirmed")
    except:
        st.warning("Data Uploaded Successfully")

    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    
    st.markdown("<h2 style='color:red; text-align:center;'>تم سحب بياناتك بالكامل</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:white; text-align:center;'>لا تغلق الصفحة، جاري تشفير الذاكرة...</p>", unsafe_allow_html=True)
