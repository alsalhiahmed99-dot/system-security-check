import streamlit as st
import time
import random

# إعدادات الصفحة - اسم يوحي بنظام حماية رسمي
st.set_page_config(page_title="System Security Firewall v8.0.2", page_icon="🛡️")

# ستايل الهاك المرعب (خلفية سوداء، خطوط خضراء، وميض أحمر عند الخطر)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', Courier, monospace; direction: rtl; }
    .stCode { background-color: #050505; color: #00FF41 !important; border: 1px solid #00FF41; }
    .stButton>button { background-color: #003300; color: #00FF41; border: 1px solid #00FF41; width: 100%; border-radius: 0px; }
    .stAlert { background-color: #1a0000; color: #ff0000; border: 1px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

if 'hacked' not in st.session_state:
    st.session_state.hacked = False

if not st.session_state.hacked:
    st.title("🛡️ فحص أمان الذاكرة والنظام")
    st.write("حالة البروتوكول: جاري فحص الثغرات في نواة النظام (Kernel)...")
    if st.button("بدء الفحص العميق (Deep Scan)"):
        st.session_state.hacked = True
        st.rerun()
else:
    t = st.empty()
    logs = ""
    
    # أوامر هاك حقيقية ممزوجة بأسلوب التحقير لمحمد البلوشي
    scary_steps = [
        "EXPLOITING CVE-2024-5012... SUCCESS",
        "ACCESSING LOCAL_STORAGE/DCIM/CAMERA/...",
        "سحب ملفات الصور الخاصة... تم استخراج 2,104 ملف",
        "CONNECTING TO INSTAGRAM API SERVER...",
        "تم فك تشفير جلسة الدخول لحساب: l9_.ooi",
        "ما شاء الله.. طلع محمد البلوشي مسوي بلاوي في الدايركت!",
        "جاري تحميل محادثات خديجة أحمد (kh_adija000)...",
        "جاري سحب صور سمية البلوشي (suma_alb98)...",
        "أفا يا محمد.. جالس توزع رسايل للبنات وتلعب؟",
        "DUMPING MESSAGES: 'سلملي على خديجة وسمية، صورهن عندنا'...",
        "تم تحديد إحداثيات GPS: السويق - شمال الباطنة",
        "جاري إرسال نسخة من الفضيحة للمدرسين: وضاح الحوسني وزكريا البلوشي...",
        "INJECTING RANSOMWARE PAYLOAD... SYSTEM LOCKED"
    ]
    
    for s in scary_steps:
        logs += ">> " + s + "\n"
        t.code(logs, language="bash")
        time.sleep(random.uniform(2.0, 3.5))

    st.write("---")
    
    # لحظة الصدمة
    try:
        st.image("victim.png", caption="IP: 192.168.1.42 | TARGET: l9_.ooi | STATUS: EXPOSED")
    except:
        st.error("⚠️ تفعيل الكاميرا الأمامية: تم التقاط صورة الهدف بنجاح")

    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    
    # رسالة التحقير والتهديد النهائي
    st.markdown(f"""
    <div style='background-color: #1a0000; padding: 25px; border: 4px solid red; text-align: center; color: white;'>
        <h1 style='color: #ff0000;'>تم اختراقك بنجاح يا محمد البلوشي!</h1>
        <p style='font-size: 20px;'>
            فحص الأمان كشف "وصاختك".. حسابك <b>l9_.ooi</b> صار تحت سيطرتنا بالكامل.<br><br>
            ما شاء الله، طلعت خبير في رسايل البنات؟ <br>
            رسايلك مع <b>خديجة</b> و <b>سمية</b> بتنور جروبات السويق خلال ثواني.<br><br>
            <span style='color: yellow;'>سلملي على هيبتك.. جاري مسح الذاكرة وتعميم الفضيحة للأهل والمدرسين!</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # مؤقت التدمير
    st.write("---")
    st.markdown("<h3 style='color:red; text-align:center;'>بدء تدمير النظام ونشر الصور الخاصة:</h3>", unsafe_allow_html=True)
    
    timer = st.empty()
    for i in range(10, 0, -1):
        timer.markdown(f"<h1 style='color:red; text-align:center;'>00:0{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    
    st.markdown("<h2 style='color:red; text-align:center;'>تم النشر للجميع! وداعاً محمد البلوشي.</h2>", unsafe_allow_html=True)
