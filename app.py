import streamlit as st
import requests

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="LawMind | AI Legal Intelligence", page_icon="⚖️", layout="wide")

# 2. تصميم الـ Frontend النظيف والمطور
st.markdown("""
    <style>
    [data-testid="stSidebar"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    #MainMenu, footer, header, [data-testid="stDecoration"] { visibility: hidden !important; display: none !important; }
    div[class^="viewerBadge"], [data-testid="stViewerBadge"] { display: none !important; visibility: hidden !important; }
    
    .block-container { padding-top: 2rem !important; padding-bottom: 3rem !important; max-width: 1000px !important; margin: 0 auto !important; }
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #f8fafc; }
    
    /* شعار الميزان الأصلي مع التوهج الأزرق النيوني والحركة التفاعلية المستقرة */
    .legal-logo {
        text-align: center !important;
        display: block !important;
        width: 100% !important;
        font-size: 5rem !important;
        margin: 0 auto 15px auto !important;
        filter: drop-shadow(0 0 25px rgba(56, 189, 248, 0.85));
        animation: pulse 2.5s infinite alternate;
    }
    
    .main-title { text-align: center !important; display: block; font-size: 3.5rem !important; font-weight: 800; background: linear-gradient(to right, #ffffff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0px 0px 5px 0px; }
    .sub-title { text-align: center !important; display: block; color: #38bdf8; font-size: 1.2rem; font-weight: 400; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 15px; }
    
    .vision-container { text-align: center !important; width: 100%; display: flex; justify-content: center; margin-bottom: 20px; }
    .vision-text { text-align: center !important; color: #94a3b8; font-size: 1.2rem; max-width: 800px; line-height: 1.8; border-bottom: 1px solid rgba(148, 163, 184, 0.1); padding-bottom: 25px; }
    
    .badge-container { display: flex; justify-content: center; align-items: center; width: 100%; margin-bottom: 35px; }
    .moroccan-badge { text-align: center !important; color: #065F46 !important; font-size: 0.95rem; font-weight: bold; background-color: #D1FAE5; padding: 8px 24px; border-radius: 50px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); display: inline-block; white-space: nowrap; unicode-bidi: plaintext !important; }
    
    .credits-container { display: flex; justify-content: center; width: 100%; margin-top: 50px; }
    .team-credits { text-align: center !important; padding: 15px 30px; background: rgba(30, 41, 59, 0.4); border-radius: 15px; border: 1px solid rgba(148, 163, 184, 0.05); font-size: 1rem; color: #e2e8f0; }
    .team-names { color: #38bdf8; font-weight: bold; }
    
    .selection-box { background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(148, 163, 184, 0.1); border-radius: 20px; padding: 30px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2); transition: all 0.3s ease; }
    .selection-box:hover { transform: translateY(-5px); border-color: #38bdf8; box-shadow: 0 15px 35px rgba(56, 189, 248, 0.2); }
    
    @keyframes pulse {
        0% { transform: scale(0.97); filter: drop-shadow(0 0 12px rgba(56, 189, 248, 0.5)); }
        100% { transform: scale(1.03); filter: drop-shadow(0 0 28px rgba(56, 189, 248, 0.9)); }
    }
    
    /* أزرار الاستشارة الملونة التنافسية الفخمة */
    .stButton, div[data-testid="stFormSubmitButton"] { display: flex !important; justify-content: center !important; width: 100% !important; margin: 20px 0; }
    .stButton>button, div[data-testid="stFormSubmitButton"]>button { background: linear-gradient(90deg, #0284c7 0%, #4f46e5 100%) !important; color: #ffffff !important; border: none !important; border-radius: 50px !important; padding: 14px 55px !important; font-weight: bold !important; font-size: 1.15rem !important; transition: all 0.3s ease !important; white-space: nowrap !important; min-width: 260px; box-shadow: 0 4px 15px rgba(2, 132, 199, 0.3) !important; }
    .stButton>button:hover, div[data-testid="stFormSubmitButton"]>button:hover { transform: scale(1.05) !important; color: #ffffff !important; box-shadow: 0 0 25px rgba(56, 189, 248, 0.6) !important; background: linear-gradient(90deg, #0284c7 0%, #4f46e5 100%) !important; }
    
    .chat-bubble-user { background-color: #1e293b; padding: 15px 20px; border-radius: 20px 20px 0px 20px; margin-bottom: 20px; border: 1px solid rgba(56, 189, 248, 0.2); max-width: 85%; margin-left: auto; font-size: 1.1rem; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    .chat-bubble-ai { background-color: #0f172a; padding: 22px; border-radius: 20px 20px 20px 0px; margin-bottom: 20px; border: 1px solid rgba(129, 140, 248, 0.3); max-width: 85%; font-size: 1.1rem; line-height: 1.8; color: #f1f5f9; box-shadow: 0 4px 15px rgba(0,0,0,0.15); }
    .ai-header { color: #818cf8; font-weight: bold; margin-bottom: 8px; }
    .footer-custom { text-align: center; margin-top: 50px; color: #64748b; font-size: 0.85rem; }
    </style>
""", unsafe_allow_html=True)

# 3. إدارة جلسة المستخدم والدول واللغات المتاحة
if "page" not in st.session_state: st.session_state.page = "landing"
if "lang" not in st.session_state: st.session_state.lang = "ar"
if "country" not in st.session_state: st.session_state.country = "Morocco"
if "chat_history" not in st.session_state: st.session_state.chat_history = []

OPENAI_API_KEY = st.secrets["openai"]["api_key"].strip() if "openai" in st.secrets else ""

fixed_credits = "💡 Developed by: <span class='team-names'>Mr. Elmahjoub Boumagout</span> & <span class='team-names'>Ms. ASMA AHLBIHI</span>"

locales = {
    "en": {
        "vision_html": "<b>LawMind</b> is the first Moroccan platform that harnesses artificial intelligence to serve humanity in the field of legal consultations.",
        "badge": "100% Moroccan Product 🇲🇦", "select_lang": "Select Language", "select_country": "Select Country Office", "btn_enter": "Launch Intelligence", "placeholder": "Ask your strict legal question here...", "search_btn": "Consult System", "user_label": "Me"
    },
    "ar": {
        "vision_html": "هي اول منصة مغربية تسخر الذكاء الاصطناعي لخدمة البشرية في مجال الاستشارات القانونية.",
        "badge": "منتج مغربي 100% 🇲🇦", "select_lang": "حدد اللغة", "select_country": "حدد مكتب الدولة", "btn_enter": "إطلاق الذكاء القانوني", "placeholder": "اطرح سؤالك القانوني الصارم هنا...", "search_btn": "استشارة النظام", "user_label": "أنا"
    },
    "fr": {
        "vision_html": "<b>LawMind</b> est la première plateforme marocaine qui met l'intelligence artificielle au service de l'humanité dans le domaine des consultations juridiques.",
        "badge": "Produit 100% Marocain 🇲🇦", "select_lang": "Choisir la Langue", "select_country": "Choisir le Bureau de Pays", "btn_enter": "Lancer l'Intelligence", "placeholder": "Posez votre question juridique stricte ici...", "search_btn": "Consulter le Système", "user_label": "Moi"
    },
    "es": {
        "vision_html": "<b>LawMind</b> es la primera plataforma marroquí que pone la inteligencia artificial al servicio de la humanidad en el campo de las consultas jurídicas.",
        "badge": "Producto 100% Marroquí 🇲🇦", "select_lang": "Seleccionar Idioma", "select_country": "Seleccionar Oficina de País", "btn_enter": "Iniciar Inteligencia", "placeholder": "Haga su pregunta legal estricta aquí...", "search_btn": "Consultar Sistema", "user_label": "Yo"
    },
    "de": {
        "vision_html": "<b>LawMind</b> ist die erste marokkanische Plattform, die künstliche Intelligenz im Dienste der Menschheit im Bereich der Rechtsberatung einsetzt.",
        "badge": "100% Marokkanisches Produkt 🇲🇦", "select_lang": "Sprache auswählen", "select_country": "Länderbüro auswählen", "btn_enter": "Intelligenz starten", "placeholder": "Stellen Sie hier Ihre strenge Rechtsfrage...", "search_btn": "System konsultieren", "user_label": "Ich"
    }
}
current_text = locales[st.session_state.lang]
supported_countries = ["Morocco 🇲🇦", "France 🇫🇷", "USA 🇺🇸", "Saudi Arabia 🇸🇦", "Egypt 🇪🇬", "Spain 🇪🇸", "UAE 🇦🇪"]

# --- الواجهة الأولى (Landing Page) ---
if st.session_state.page == "landing":
    st.markdown('<p class="legal-logo">⚖️</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-title">LawMind</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">AI Legal Intelligence</p>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="vision-container"><p class="vision-text">{current_text["vision_html"]}</p></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="badge-container"><span class="moroccan-badge">{current_text["badge"]}</span></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="selection-box"><h3>🌐 {current_text["select_lang"]}</h3>', unsafe_allow_html=True)
        selected_lang_ui = st.selectbox("Language", ["العربية", "English", "Français", "Español", "Deutsch"], index=["ar", "en", "fr", "es", "de"].index(st.session_state.lang), label_visibility="collapsed")
        st.session_state.lang = {"العربية":"ar", "English":"en", "Français":"fr", "Español":"es", "Deutsch":"de"}[selected_lang_ui]
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown(f'<div class="selection-box"><h3>📍 {current_text["select_country"]}</h3>', unsafe_allow_html=True)
        clean_country_names = [c.split()[0] for c in supported_countries]
        default_country_idx = clean_country_names.index(st.session_state.country) if st.session_state.country in clean_country_names else 0
        selected_country_ui = st.selectbox("Country", supported_countries, index=default_country_idx, label_visibility="collapsed")
        st.session_state.country = selected_country_ui.split()[0]
        st.markdown('</div>', unsafe_allow_html=True)
        
    if st.button(current_text["btn_enter"]):
        st.session_state.page = "chat"
        st.rerun()
            
    st.markdown(f'<div class="credits-container"><div class="team-credits">{fixed_credits}</div></div>', unsafe_allow_html=True)

# --- واجهة نظام الشات والاستشارة (Chat Page) ---
elif st.session_state.page == "chat":
    st.markdown('<p class="legal-logo">⚖️</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="main-title" style="font-size: 2.2rem;">LawMind | {st.session_state.country} Bureau</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-title" style="font-size: 0.9rem; margin-bottom: 20px;">AI Legal Intelligence</p>', unsafe_allow_html=True)

    # عرض تاريخ استشارات الجلسة المباشرة بالتنظيم اللغوي الديناميكي
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-bubble-user"><b>👤 {current_text["user_label"]}:</b><br>{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble-ai"><div class="ai-header">⚖️ LawMind AI Intelligence:</div>{message["content"]}</div>', unsafe_allow_html=True)

    with st.form(key="legal_form", clear_on_submit=True):
        user_query = st.text_input(label="Legal Consultation Input", placeholder=current_text["placeholder"], label_visibility="collapsed")
        search_button = st.form_submit_button(current_text["search_btn"])

    if search_button and user_query:
        if not OPENAI_API_KEY:
            st.error("⚠️ Configuration Error: OpenAI API Key is missing.")
        else:
            st.session_state.chat_history.append({"role": "user", "content": user_query})
            with st.spinner("Analyzing Legal Database..."):
                try:
                    system_prompt = (
                        f"You are a strict, hyper-focused Legal Expert AI core specialized in international jurisprudence. "
                        f"Your default focus for this session is set to {st.session_state.country} laws. "
                        f"CRITICAL RULE 1 (DYNAMIC JURISDICTION): Analyze the user's question. If the user explicitly asks about the laws of another specific country, override the default country and answer accurately according to that requested legal system. "
                        f"CRITICAL RULE 2 (THEME GATEKEEPER): You must ONLY answer legal and law-related questions. If the inquiry is outside the boundaries of law, politely decline. "
                        f"CRITICAL RULE 3 (LANGUAGE MATCHING): You must write your professional response in the EXACT SAME LANGUAGE the user used to ask the question."
                    )
                    
                    response = requests.post(
                        "https://api.openai.com/v1/chat/completions",
                        headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
                        json={
                            "model": "gpt-4o-mini",
                            "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_query}],
                            "temperature": 0.2
                        }
                    ).json()
                    
                    if 'choices' in response and response['choices']:
                        output_text = response['choices'][0]['message']['content']
                        st.session_state.chat_history.append({"role": "assistant", "content": output_text})
                        st.rerun()
                    else:
                        st.error("🛑 OpenAI API Error: Please verify key configuration or balance.")
                except Exception as e:
                    st.error(f"System Error: {str(e)}")

st.markdown('<p class="footer-custom">LawMind | AI Legal Intelligence • Powered by Moroccan Innovation 🇲🇦 • © 2026</p>', unsafe_allow_html=True)
