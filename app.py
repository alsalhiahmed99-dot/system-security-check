import streamlit as st
import time
import random

# إعدادات الصفحة
st.set_page_config(page_title="نظام الرصد الأمني", page_icon="🚫")

# ستايل هكر احترافي
st.markdown("<style>.stApp { background-color: #000000; color: #00FF41; direction: rtl; }</style>", unsafe_allow_html=True)

if 'run' not in st.session_state:
    st.session_state.run = False

if not st.session_state.run:
    st.title("🚫 نظام الفحص الأمني الموحد")
    st.write("تحذير: هذا الجهاز مراقب ومطلوب للفحص.")
    if st.button("بدء فحص الهوية الرقمية"):
        st.session_state.run = True
        st.rerun()
else:
    t = st.empty()
    logs = ""
    
    # رسائل التهديد الشخصية
    m1 = "جاري فحص بروتوكول الإنترنت (IP)..."
    m2 = "تم تحديد هوية المستخدم بنجاح..."
    m3 = "الاسم: محمد البلوشي"
    m4 = "جاري الدخول إلى ملفات الصور الخاصة..."
    m5 = "تم سحب 1,240 صورة من الاستوديو..."
    m6 = "جاري الوصول إلى موقع الجهاز الحالي..."
    m7 = "إرسال البيانات إلى السيرفر الرئيسي..."
    
    for m in [m1, m2, m3, m4, m5, m6, m7]:
        logs += "> " + m + "\n"
        t.code(logs)
        time.sleep(2.5)

    st.write("---")
    st.error("🚨 تم اختراق جهاز محمد البلوشي بنجاح 🚨")
    
    # هنا تطلع صورته
    try:
        st.image("victim.png", caption="المستهدف: محمد البلوشي | الحالة: مراقب")
    except:
        st.warning("تم سحب صورة محمد البلوشي")

    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")
    
    # قسم التهديدات القوية
    st.markdown("<h1 style='color:red; text-align:center;'>يا محمد البلوشي، تم اختراقك!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:white; text-align:center; font-size:20px;'>كل صورك ورسايلك صارت عندنا الحين.</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:yellow; text-align:center;'>سيتم نشر ملفاتك خلال 10 دقائق إذا حاولت إغلاق الصفحة.</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:red; text-align:center; font-weight:bold;'>جاري مسح بيانات الهاتف بالكامل... لا تلمس الشاشة!</p>", unsafe_allow_html=True)
