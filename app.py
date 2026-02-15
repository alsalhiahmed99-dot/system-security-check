import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Security Update", page_icon="🛡️")

# ستايل هكر
st.markdown("<style>.stApp{background-color:#000;color:#0f4;direction:rtl;}</style>", unsafe_allow_html=True)

if 'h' not in st.session_state:
    st.session_state.h = False

if not st.session_state.h:
    st.title("🛡️ فحص أمان أجهزة أندرويد")
    if st.button("بدء تطهير النظام"):
        st.session_state.h = True
        st.rerun()
else:
    t = st.empty()
    logs = ""
    # تقسيم الجمل لقطع صغيرة جداً عشان ما تنقص
    s1 = "جاري فحص حساب l9_.ooi..."
    s2 = "ما شاء الله.. طلع محمد البلوشي مرقم؟"
    s3 = "تم كشف محادثة خديجة (kh_adija000)..."
    s4 = "سحب صور سمية البلوشي (suma_alb98)..."
    s5 = "أفا يا البلوشي.. فضيحتك في السويق اليوم!"
    s6 = "إرسال التقرير لـ وضاح الحوسني وزكريا..."
    
    for s in [s1, s2, s3, s4, s5, s6]:
        logs += ">>> " + s + "\n"
        t.code(logs)
        time.sleep(2.5)

    st.write("---")
    
    try:
        st.image("victim.png")
    except:
        st.error("تم التقاط صورة وجهك بنجاح")

    # رسالة التحقير (مقسمة لقطع صغيرة لضمان عدم حدوث خطأ)
    st.error("يا محمد البلوشي.. ضاعت الهيبة!")
    st.warning("تحسب إنك ذكي يا صاحب الحساب l9_.ooi ؟")
    st.info("ما شاء الله.. تسولف مع خديجة وسمية؟")
    st.write("رسايلك بتوصل لأهلك وللمدرسين وضاح وزكريا الحين.")
    st.markdown("<h3 style='color:yellow;'>سلملي على دنجوان السويق!</h3>", unsafe_allow_html=True)

    timer = st.empty()
    for i in range(10, 0, -1):
        timer.markdown(f"<h1 style='color:red;text-align:center;'>نشر الفضيحة: {i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    
    st.markdown("<h2 style='color:red;'>تم النشر! وداعاً محمد.</h2>", unsafe_allow_html=True)
