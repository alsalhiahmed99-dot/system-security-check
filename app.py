import streamlit as st
import time
import random

# إعدادات الصفحة - اسم يوحي باختراق أمني حقيقي
st.set_page_config(page_title="FATAL SYSTEM ERROR", page_icon="💀")

# ستايل الهاك الاحترافي
st.markdown("<style>.stApp{background-color:#050000;color:#0f4;font-family:'Courier New';direction:rtl;}</style>", unsafe_allow_html=True)

if 'h' not in st.session_state:
    st.session_state.h = False

if not st.session_state.h:
    st.title("🛡️ نظام فحص الحماية الموحد")
    st.write("تنبيه: تم رصد نشاط غير قانوني. اضغط للفحص.")
    if st.button("بدء فحص النظام"):
        st.session_state.h = True
        st.rerun()
else:
    t = st.empty()
    log = ""
    # خطوات اختراق التلفون كامل بأسلوب مرعب
    steps = [
        "إرسال طلب Root Access... تم القبول",
        "اختراق Kernel النظام... SUCCESS",
        "جاري سحب قائمة الأسماء (Contacts)... تم سحب 450 رقم",
        "جاري الدخول إلى استوديو الصور (DCIM)...",
        "تم العثور على 3,421 صورة.. جاري الرفع للسيرفر",
        "جاري فحص محادثات WhatsApp و SMS...",
        "فتح سجل المكالمات الصادرة والواردة...",
        "🚨 تنبيه: تم اكتشاف حساب Instagram: l9_.ooi",
        "ما شاء الله يا محمد البلوشي.. طلع عندك بلاوي!",
        "كشف محادثات خديجة أحمد (kh_adija000)...",
        "كشف محادثات سمية البلوشي (suma_alb98)...",
        "أفا يا دنجوان السويق.. كل الصور والرسايل عندنا!",
        "جاري إرسال نسخة لـ وضاح الحوسني وزكريا البلوشي...",
        "تفعيل الكاميرا الأمامية.. تم التقاط صورة الهدف"
    ]
    
    for s in steps:
        log += ">>> " + s + "\n"
        t.code(log)
        time.sleep(2.5)

    st.write("---")
    
    try:
        st.image("victim.png")
    except:
        st.error("تم سحب صورة وجهك يا محمد!")

    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    
    # رسالة التحقير والقصف
    st.markdown("<div style='border:4px solid red;padding:20px;text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:red;'>تم اختراق تلفونك بالكامل!</h2>", unsafe_allow_html=True)
    st.markdown("<p>يا محمد البلوشي.. تلفونك صار ملكنا.</p>", unsafe_allow_html=True)
    st.markdown("<p><b>ما شاء الله</b>.. طلعت خبير في البنات ورسايل الدايركت؟</p>", unsafe_allow_html=True)
    st.markdown("<p>سلملي على <b>خديجة</b> و <b>سمية</b>.. فضيحتكم في السويق الحين.</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:yellow;'>باقي ثواني وتوصل صورك ورسايلك لأهلك ولمدرسينك.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    timer = st.empty()
    for i in range(15, 0, -1):
        timer.markdown(f"<h1 style='color:red;text-align:center;'>تدمير الذاكرة ونشر الصور: {i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    
    st.markdown("<h1 style='color:red;text-align:center;'>GAME OVER</h1>", unsafe_allow_html=True)
