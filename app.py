import streamlit as st
import time
import random

# إعدادات الصفحة - اسم يوحي بالأمان
st.set_page_config(page_title="Android System Security Update v4.1", page_icon="🛡️")

# ستايل هكر
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', monospace; direction: rtl; }
    .stCode { background-color: #000000; color: #00FF41 !important; border: 1px solid #00FF41; }
    </style>
    """, unsafe_allow_html=True)

if 'secure_mode' not in st.session_state:
    st.session_state.secure_mode = True

if st.session_state.secure_mode:
    st.title("🛡️ نظام فحص أمان الجهاز")
    st.write("حالة النظام: جاري التحقق من الثغرات...")
    st.info("هذا الفحص يحمي بياناتك من الاختراق الخارجي.")
    if st.button("بدء الفحص الشامل"):
        st.session_state.secure_mode = False
        st.rerun()
else:
    t = st.empty()
    logs = ""
    
    # تحول الفحص من أمان إلى فضيحة واستهزاء
    steps = [
        "جاري فحص ملفات النظام...",
        "تم اكتشاف ثغرة في تطبيق Instagram...",
        "جاري محاولة سد الثغرة في حساب l9_.ooi...",
        "لحظة.. ما شاء الله! شو هذا اللي حصلناه في الدايركت؟",
        "أفا يا محمد البلوشي.. وبعدك تتابع بنات؟",
        "جاري سحب محادثات خديجة أحمد (kh_adija000)...",
        "جاري استخراج صور سمية البلوشي (suma_alb98)...",
        "سلملي على خديجة وسمية، صورهن صارن عندنا الحين!",
        "جاري إرسال تقرير 'السلوك' لجروبات السويق...",
        "تنبيه: سيتم إرسال نسخة للمدرسين: وضاح الحوسني وزكريا البلوشي."
    ]
    
    for s in steps:
        logs += ">> " + s + "\n"
        t.code(logs)
        time.sleep(3.0)

    st.write("---")
    
    try:
        st.image("victim.png", caption="Identity: l9_.ooi | Status: Exposed")
    except:
        st.error("تم التقاط صورتك وأنت منصدم بنجاح!")

    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    
    # رسالة التحقير النهائية
    st.markdown(f"""
    <div style='background-color: white; padding: 20px; border-radius: 10px; border: 5px solid red; color: black; text-align: center;'>
        <h2 style='color: red;'>فحص الأمان كشف المستور يا محمد البلوشي!</h2>
        <p style='font-weight: bold; font-size: 18px;'>
            مسوي نفسك تفحص الأمان وأنت غارق في رسايل البنات؟ <br><br>
            حسابك <b>l9_.ooi</b> صار كتاب مفتوح، ورسايلك مع <b>خديجة</b> و <b>سمية</b> بتوصل لأهلك الحين.<br><br>
            <span style='color: red; font-size: 20px;'>سلملي على الحساب، وعلى هيبتك في السويق!</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # مؤقت الفضيحة
    timer_area = st.empty()
    for i in range(15, 0, -1):
        timer_area.markdown(f"<h1 style='color:red; text-align:center;'>نشر المحادثات لجروبات السويق خلال: {i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    
    st.markdown("<h1 style='color:red; text-align:center;'>تم النشر! مبروك الفضيحة يا محمد.</h1>", unsafe_allow_html=True)
