import streamlit as st
import time
import random

# إعدادات الصفحة
st.set_page_config(page_title="System Security Firewall v8.0", page_icon="🛡️")

# ستايل هكر مرعب ومستفز
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', monospace; direction: rtl; }
    .stCode { background-color: #050505; color: #ff0000 !important; border: 1px solid #330000; }
    </style>
    """, unsafe_allow_html=True)

if 'hacked' not in st.session_state:
    st.session_state.hacked = False

if not st.session_state.hacked:
    st.title("🛡️ فحص أمان أجهزة أندرويد")
    st.warning("تنبيه: تم رصد ملفات ضارة في حساب l9_.ooi")
    if st.button("تطهير النظام وسد الثغرات"):
        st.session_state.hacked = True
        st.rerun()
else:
    t = st.empty()
    logs = ""
    
    # قائمة التحقير - مرتبة عشان ما يصير خطأ في النسخ
    steps = [
        "إيقاف جدار الحماية... تم بنجاح.",
        "جاري فحص ملفات 'الخزي' في حساب l9_.ooi...",
        "ما شاء الله.. طلع محمد البلوشي مخلص في 'الترقيم'؟",
        "تم كشف المجلد السري لـ خديجة أحمد (kh_adija000)...",
        "أفا يا البلوشي.. هذا وأنت من السويق وعامل فيها مطوع؟",
        "جاري سحب المحادثات مع سمية البلوشي (suma_alb98)...",
        "يا عيني على الكلام.. سلملي على خديجة وسمية وايد!",
        "تم تصوير الشاشة لكل فضايحك في الدايركت..",
        "جاري رفع الصور لجروبات 'أهالي السويق' و 'جروب العائلة'...",
        "تنبيه: المدرس وضاح الحوسني وزكريا البلوشي بيوصلهم التقرير الحين..",
        "مسكين يا محمد.. حسابك l9_.ooi صار 'سبيل' للكل!",
        "باقي شوية وتصير أشهر واحد في السويق بالخيبة!"
    ]
    
    for s in steps:
        logs += ">>> " + s + "\n"
        t.code(logs)
        time.sleep(2.5)

    st.write("---")
    
    try:
        st.image("victim.png", caption="Target: l9_.ooi | Status: EXPOSED")
    except:
        st.error("⚠️ تم فتح الكاميرا.. شكلك وأنت منصدم يضحك يا محمد!")

    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    
    # رسالة التحقير الكبرى
    st.markdown(f"""
    <div style='background-color: #1a0000; padding: 25px; border: 5px double red; text-align: center; color: white;'>
        <h1 style='color: #ff0000;'>يا محمد البلوشي.. ضاعت الهيبة!</h1>
        <p style='font-size: 18px;'>
            تحسب إنك ذكي يا صاحب الحساب <b>l9_.ooi</b>؟ <br><br>
            <b>ما شاء الله</b>.. مسوي فيها بطل وتضحك على <b>خديجة</b> و <b>سمية</b>؟ <br>
            رسايلك "الرومانسية" بتنور جروبات السويق والحين الكل بيعرف حقيقتك.<br><br>
            سلملي على خديجة وسمية، وقولهم
