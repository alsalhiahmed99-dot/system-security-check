import streamlit as st
import time
import random

# إعدادات الصفحة
st.set_page_config(page_title="🚨 ALERT: PRIVATE DATA LEAK", page_icon="🚫")

# ستايل هكر مرعب
st.markdown("""
    <style>
    .stApp { background-color: #050000; color: #FF0000; font-family: 'Courier New', monospace; direction: rtl; }
    .stCode { background-color: #000000; color: #10FF10 !important; border: 1px solid #FF0000; }
    </style>
    """, unsafe_allow_html=True)

if 'hacked' not in st.session_state:
    st.session_state.hacked = False

if not st.session_state.hacked:
    st.title("🚫 وحدة المراقبة الأخلاقية - السويق")
    st.write("تم رصد محتوى مخزي في حساب l9_.ooi")
    if st.button("كشف المستور"):
        st.session_state.hacked = True
        st.rerun()
else:
    t = st.empty()
    logs = ""
    
    # خطوات الفضيحة مع أسلوب التحقير
    steps = [
        "جاري الدخول لخصوصيات l9_.ooi...",
        "ما شاء الله.. طلع محمد البلوشي مخلص في المتابعة!",
        "تم الوصول لمحادثات خديجة أحمد (kh_adija000)...",
        "جاري سحب صور 'سمية البلوشي' (suma_alb98) من الدايركت...",
        "أفا يا محمد.. جالس تسولف مع بنات ومن ورانا؟",
        "جاري تصوير الشاشة لكل المحادثات 'الرومانسية'...",
        "سلملي على خديجة وسمية، الصور بيوصلن لأهلك الحين!",
        "جاري إعداد 'تقرير الفضيحة' لنشره في جروبات السويق...",
        "تنبيه: سيتم إرسال نسخة خاصة للمدرسين: وضاح الحوسني وزكريا البلوشي."
    ]
    
    for s in steps:
        logs += ">> " + s + "\n"
        t.code(logs)
        time.sleep(3.5)

    st.write("---")
    
    try:
        st.image("victim.png", caption="Target: l9_.ooi | Status: Exposed")
    except:
        st.error("تم التقاط صورة وجهك وأنت خايف بنجاح")

    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    
    # رسالة التحقير النهائية
    st.markdown(f"""
    <div style='background-color: white; padding: 20px; border-radius: 10px; border: 5px solid red; color: black; text-align: center;'>
        <h2 style='color: red;'>ما شاء الله عليك يا محمد البلوشي!</h2>
        <p style='font-weight: bold; font-size: 18px;'>
            طلعت فنان وتتابع بنات وتوزع نظرات؟ <br><br>
            رسايلك مع <b>خديجة</b> و <b>سمية</b> صارت عندنا، والظاهر إنك نسيت إن الله حق.<br><br>
            جاري الآن إرسال "إبداعاتك" لـ <b>أهلك</b> و <b>متابعينك</b> عشان يشوفوا بطولاتك.<br><br>
            <span style='color: red; font-size: 20px;'>سلملي على الحساب l9_.ooi، لأنه بيختفي للأبد بعد ثواني!</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # مؤقت الفضيحة
    timer_area = st.empty()
    for i in range(15, 0, -1):
        timer_area.markdown(f"<h1 style='color:red; text-align:center;'>نشر صور البنات لجروبات السويق خلال: {i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    
    st.markdown("<h1 style='color:red; text-align:center;'>تم النشر! مبروك الفضيحة يا محمد.</h1>", unsafe_allow_html=True)
