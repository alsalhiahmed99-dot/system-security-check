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

if 'hacked' not in st.session_state:
    if st.button("RUN SECURITY CHECK"):
        st.session_state.hacked = True
        st.rerun()

if st.get('hacked'):
    status_area = st.empty()
    log_area = st.empty()
    
    # قائمة الأوامر "الواقعية"
    hacker_commands = [
        "Connecting to proxy 192.168.1.44...",
        "Bypassing Oman-School Firewall...",
        "Gaining Root Privileges... [SUCCESS]",
        "Injecting Payload into WhatsApp.apk...",
        "Accessing Media Storage /DCIM/Camera...",
        "Syncing 1,422 private photos to server...",
        "Triggering Front Camera API...",
        "Extracting GPS Coordinates: 23.5859° N, 58.4059° E",
        "Matching User Profile with FaceID..."
    ]

    for cmd in hacker_commands:
        status_area.warning(f"EXECUTING: {cmd}")
        time.sleep(random.uniform(2.0, 3.5)) # وقت عشوائي عشان يبين إنه حقيقي
    
    st.write("---")
    st.error("🚨 USER IDENTIFIED 🚨")
    time.sleep(2)

    # عد تنازلي مرعب
    for i in range(5, 0, -1):
        st.subheader(f"System Lockdown in {i}...")
        time.sleep(1)
    
    # الصدمة الكبرى - تظهر الصورة
    st.image("victim.png", caption="هذي صورتك يا بطل؟ تم سحب كل ملفاتك بنجاح.")
    
    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    st.snow() # حركة كأن النظام تجمد (Freeze)
    
    st.markdown("### **لا تحاول تغلق المتصفح، جاري الآن مسح الذاكرة الداخلية للهاتف...**")
