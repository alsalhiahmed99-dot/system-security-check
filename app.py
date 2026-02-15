import streamlit as st
import time
import random

# إعدادات الصفحة
st.set_page_config(page_title="Terminal - System Root Access", page_icon="📟")

# ستايل الهكر المرعب
st.markdown("""
    <style>
    .stApp { background-color: #020202; color: #39FF14; font-family: 'Courier New', Courier, monospace; }
    .stProgress > div > div > div > div { background-color: #39FF14; }
    </style>
    """, unsafe_allow_html=True)

st.title("📟 System Kernel v4.0.2")
st.write("---")

# تعريف حالة الهكر إذا ما كانت موجودة
if 'hacked' not in st.session_state:
    st.session_state.hacked = False

# الشاشة الأولى: زر البدء
if not st.session_state.hacked:
    st.write("⚠️ تحذير: هذا النظام مخصص للفحص الأمني فقط.")
    if st.button("RUN SECURITY CHECK"):
        st.session_state.hacked = True
        st.rerun()

# الشاشة الثانية: مرحلة الاختراق الوهمي
else:
    status_area = st.empty()
    
    # قائمة الأوامر "الواقعية"
    hacker_commands = [
        "Connecting to proxy 192.168.1.44...",
        "Bypassing Oman-School Firewall...",
        "Gaining Root Privileges... [SUCCESS]",
        "Injecting Payload into WhatsApp.apk...",
        "Accessing Media Storage /DCIM/Camera...",
        "Syncing private photos to server...",
        "Triggering Front Camera API...",
        "Extracting GPS Coordinates: 23.5859° N, 58.4059° E",
        "Matching User Profile with FaceID..."
    ]

    # عرض الأوامر ببطء
    for cmd in hacker_commands:
        status_area.warning(f"EXECUTING: {cmd}")
        time.sleep(random.uniform(1.5, 3.0)) 
    
    st.write("---")
    st.error("🚨 USER IDENTIFIED 🚨")
    time.sleep(2)

    # عد تنازلي مرعب
    for i in range(5, 0, -1):
        st.subheader(f"System Lockdown in {i}...")
        time.sleep(1)
    
    # الصدمة الكبرى - تظهر الصورة
    # تأكد أن الملف اسمه victim.png وموجود في GitHub
    try:
        st.image("victim.png", caption="هذي صورتك يا بطل؟ تم سحب كل ملفاتك بنجاح.")
    except:
        st.error("فشل في تحميل الصورة - تأكد من وجود ملف victim.png")
    
    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    st.markdown("### **لا تحاول أغلاق الصفحة، جاري الآن مسح الذاكرة الداخلية للهاتف...**")
