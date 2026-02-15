import streamlit as st
import time
import random

# إعدادات الصفحة - اسم يوحي ببرنامج حماية
st.set_page_config(page_title="System Security Shield v5.0", page_icon="🔒")

# ستايل هكر احترافي (خلفية سوداء، خط أخضر فاقع، وبدون حواف)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #000000; color: #00FF41; border: 1px solid #00FF41; width: 100%; }
    .stError { background-color: #1a0000; color: #ff0000; border: 1px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

# حالة الجلسة
if 'access_granted' not in st.session_state:
    st.session_state.access_granted = False

if not st.session_state.access_granted:
    st.title("🔒 Security Analyzer")
    st.write("System status: SECURE")
    st.write("Scanning for vulnerabilities...")
    if st.button("START FULL SYSTEM SCAN"):
        st.session_state.access_granted = True
        st.rerun()

else:
    # شاشة الاختراق
    status_text = st.empty()
    terminal_logs = st.empty()
    logs = ""

    # سلسلة عمليات وهمية تبدو حقيقية جداً
    processes = [
        "Connecting to local gateway 192.168.1.1...",
        "Exploiting CVE-2023-4012 (Kernel level)...",
        "ROOT ACCESS: GRANTED",
        "Accessing /private/var/mobile/Library/SMS/...",
        "Downloading WhatsApp Database...",
        "Opening Front Camera Module (Silent Mode)...",
        "Capturing user metadata...",
        "Uploading to remote server: 45.22.190.11...",
        "ENCRYPTING LOCAL FILES..."
    ]

    for p in processes:
        logs += f"> {p}\n"
        terminal_logs.code(logs, language="bash")
        time.sleep(random.uniform(2.5, 4.0)) # وقت طويل لزيادة التوتر

    st.write("---")
    st.error("⚠️ CRITICAL BREACH DETECTED: DATA LEAK IN PROGRESS")
    time.sleep(2)

    # العد التنازلي للتدمير
    count_area = st.empty()
    for i in range(10, 0, -1):
        count_area.subheader(f"System Wipe in {i} seconds...")
        time.sleep(1)
    
    count_area.empty()
    
    # اللحظة الحاسمة: عرض الصورة بدون كلمات تشجيعية
    try:
        st.image("victim.png", caption="IP Address: 156.190.42.11 | Identity: CONFIRMED")
    except:
        st.error("ERROR: RECOVERY_IMAGE_NOT_FOUND")

    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    
    st.markdown("""
    <h2 style='color: red; text-align: center;'>تم سحب بياناتك بنجاح.</h2>
    <p style='color: white; text-align: center;'>لا تقم بإغلاق المتصفح لضمان عدم تلف نظام التشغيل.</p>
    """, unsafe_allow_html=True)
