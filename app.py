import streamlit as st
import requests

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="LawMind | AI Legal Intelligence", page_icon="⚖️", layout="wide")

# 2. تصميم الـ Frontend الاحترافي المطور والمقاوم لتداخل النصوص
st.markdown("""
    <style>
    [data-testid="stSidebar"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    #MainMenu, footer, header, [data-testid="stDecoration"] { visibility: hidden !important; display: none !important; }
    div[class^="viewerBadge"], [data-testid="stViewerBadge"] { display: none !important; visibility: hidden !important; }
    
    .block-container { padding-top: 2rem !important; padding-bottom: 1rem !important; max-width: 1000px !important; margin: 0 auto !important; }
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #f8fafc; }
    
    /* شعار الميزان الأصلي مع التوهج الأزرق النيوني والحركة التفاعلية */
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
    
    .badge-container { display: flex; justify-content: center; align-items: center; width: 100%; margin-bottom: 25px; }
    .moroccan-badge { text-align: center !important; color: #065F46 !important; font-size: 0.95rem; font-weight: bold; background-color: #D1FAE5; padding: 8px 24px; border-radius: 50px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); display: inline-block; white-space: nowrap; unicode-bidi: plaintext !important; }
    
    /* 🌟 تصميم الحاوية التفاعلية المركزية لـ ساكنة طانطان ونظام التحقق المتكامل */
    .interactive-tantan-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 2px solid rgba(234, 179, 8, 0.4);
        border-radius: 24px;
        padding: 30px;
        text-align: center;
        max-width: 750px;
        margin: 35px auto;
        box-shadow: 0 15px 35px rgba(0,0,0,0.4), 0 0 20px rgba(234, 179, 8, 0.1);
    }
    .tantan-title { color: #eab308 !important; font-size: 1.5rem !important; font-weight: 800 !important; margin-bottom: 12px; letter-spacing: 1px; }
    .tantan-desc { color: #e2e8f0 !important; font-size: 1.1rem; line-height: 1.7; margin-bottom: 20px; }
    .tantan-input-label { font-weight: bold; color: #38bdf8; margin-top: 15px; margin-bottom: 8px; font-size: 1rem; display: block; }
    
    .credits-container { display: flex; justify-content: center; width: 100%; margin-top: 30px; margin-bottom: 20px; }
    .team-credits { text-align: center !important; padding: 15px 30px; background: rgba(30, 41, 59, 0.4); border-radius: 15px; border: 1px solid rgba(148, 163, 184, 0.05); font-size: 1rem; color: #e2e8f0; }
    .team-names { color: #38bdf8; font-weight: bold; }
    
    .selection-box { background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(148, 163, 184, 0.1); border-radius: 20px; padding: 30px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2); transition: all 0.3s ease; }
    .selection-box:hover { transform: translateY(-5px); border-color: #38bdf8; box-shadow: 0 15px 35px rgba(56, 189, 248, 0.2); }
    
    @keyframes pulse {
        0% { transform: scale(0.97); filter: drop-shadow(0 0 12px rgba(56, 189, 248, 0.5)); }
        100% { transform: scale(1.03); filter: drop-shadow(0 0 28px rgba(56, 189, 248, 0.9)); }
    }
    
    /* أزرار الاستشارة الملونة التنافسية الفخمة */
    .stButton, div[data-testid="stFormSubmitButton"] { display: flex !important; justify-content: center !important; width: 100% !important; margin: 25px 0; }
    .stButton>button, div[data-testid="stFormSubmitButton"]>button { background: linear-gradient(90deg, #0284c7 0%, #4f46e5 100%) !important; color: #ffffff !important; border: none !important; border-radius: 50px !important; padding: 14px 55px !important; font-weight: bold !important; font-size: 1.15rem !important; transition: all 0.3s ease !important; white-space: nowrap !important; min-width: 260px; box-shadow: 0 4px 15px rgba(2, 132, 199, 0.3) !important; }
    .stButton>button:hover, div[data-testid="stFormSubmitButton"]>button:hover { transform: scale(1.05) !important; color: #ffffff !important; box-shadow: 0 0 25px rgba(56, 189, 248, 0.6) !important; background: linear-gradient(90deg, #0284c7 0%, #4f46e5 100%) !important; }
    
    .back-btn-container { display: flex !important; justify-content: flex-start !important; width: 100% !important; margin-bottom: -20px; }
    .back-btn-container button { background: rgba(148, 163, 184, 0.1) !important; color: #94a3b8 !important; border: 1px solid rgba(148, 163, 184, 0.2) !important; border-radius: 12px !important; padding: 6px 18px !important; font-size: 0.9rem !important; min-width: auto !important; box-shadow: none !important; }
    .back-btn-container button:hover { background: rgba(239, 68, 68, 0.2) !important; color: #f87171 !important; border-color: #f87171 !important; transform: translateX(-3px) !important; }

    .chat-bubble-user { background-color: #1e293b; padding: 15px 20px; border-radius: 20px 20px 0px 20px; margin-bottom: 20px; border: 1px solid rgba(56, 189, 248, 0.2); max-width: 85%; margin-left: auto; font-size: 1.1rem; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    .chat-bubble-ai { background-color: #0f172a; padding: 22px; border-radius: 20px 20px 20px 0px; margin-bottom: 20px; border: 1px solid rgba(129, 140, 248, 0.3); max-width: 85%; font-size: 1.1rem; line-height: 1.8; color: #f1f5f9; box-shadow: 0 4px 15px rgba(0,0,0,0.15); }
    .ai-header { color: #818cf8; font-weight: bold; margin-bottom: 8px; }
    
    .footer-panel { background: rgba(15, 23, 42, 0.6); border-top: 1px solid rgba(56, 189, 248, 0.15); padding: 30px 20px 15px 20px; margin-top: 60px; border-radius: 24px 24px 0 0; }
    .footer-grid { display: flex; flex-wrap: wrap; justify-content: space-between; max-width: 1000px; margin: 0 auto; gap: 20px; }
    .footer-col { flex: 1; min-width: 250px; }
    .footer-col h4 { color: #38bdf8; font-size: 1.1rem; margin-bottom: 12px; font-weight: 600; border-bottom: 2px solid rgba(56, 189, 248, 0.2); padding-bottom: 5px; width: fit-content; }
    .footer-col p { color: #94a3b8; font-size: 0.95rem; line-height: 1.6; }
    .footer-bottom { text-align: center; margin-top: 25px; padding-top: 15px; border-top: 1px solid rgba(148, 163, 184, 0.08); color: #64748b; font-size: 0.85rem; }
    </style>
""", unsafe_allow_html=True)

# 3. إدارة جلسة المستخدم والدول واللغات المتاحة
if "page" not in st.session_state: st.session_state.page = "landing"
if "lang" not in st.session_state: st.session_state.lang = "ar"
if "country" not in st.session_state: st.session_state.country = "Morocco"
if "chat_history" not in st.session_state: st.session_state.chat_history = []

OPENAI_API_KEY = st.secrets["openai"]["api_key"].strip() if "openai" in st.secrets else ""

fixed_credits = "💡 Developed by: <span class='team-names'>Mr. Elmahjoub Boumagout</span> & <span class='team-names'>Ms. ASMA AHLBIHI</span>"

# حزم النصوص المترجمة بالكامل ديناميكياً لتشمل خانة الفوتر والبطاقة التفاعلية المركزية لطانطان
locales = {
    "en": {
        "vision_html": "<b>LawMind</b> is the first Moroccan platform that harnesses artificial intelligence to serve humanity in the field of legal consultations.",
        "badge": "100% Moroccan Product 🇲🇦", "select_lang": "Select Language", "select_country": "Select Country Office", "btn_enter": "Launch Intelligence", "placeholder": "Ask your strict legal question here...", "search_btn": "Consult System", "user_label": "Me", "back_btn": "⬅ Back",
        "tt_title": "☀️ Tan-Tan Province Exclusive Initiative", 
        "tt_desc": "Residents of Tan-Tan province benefit from full and free 100% access to the legal advisor service in Morocco. Please verify your eligibility inside this panel.", 
        "tt_label": "Verify Free Access Eligibility (Enter CNIE / ID Card Number):", 
        "tt_placeholder": "e.g. JF12345", 
        "tt_success": "🎉 Congratulations! Your card starts with JF. You are fully eligible for free access.", 
        "tt_fail": "❌ Sorry, this card number is not eligible for this exclusive local initiative.",
        "footer_goals_title": "🎯 Our Goals", "footer_goals_desc": "Harnessing advanced artificial intelligence technologies to serve humanity, facilitate access to strict legal information, and support digital legal innovation in line with international standards.", "footer_addr_title": "📍 Registered Headquarters", "footer_addr_desc": "No. 11, Al-Alawiyyin Street, Administrative District, Tan-Tan, Kingdom of Morocco."
    },
    "ar": {
        "vision_html": "هي اول منصة مغربية تسخر الذكاء الاصطناعي لخدمة البشرية في مجال الاستشارات القانونية.",
        "badge": "منتج مغربي 100% 🇲🇦", "select_lang": "حدد اللغة", "select_country": "حدد مكتب الدولة", "btn_enter": "إطلاق الذكاء القانوني", "placeholder": "اطرح سؤالك القانوني الصارم هنا...", "search_btn": "استشارة النظام", "user_label": "أنا", "back_btn": "⬅ رجوع",
        "tt_title": "☀️ مبادرة إقليم طانطان الحصرية", 
        "tt_desc": "يستفيد سكان إقليم طانطان من ولوج كامل ومجاني بنسبة 100% إلى خدمات المستشار القانوني في المغرب. يرجى التحقق من أهليتك داخل هذه الخانة.", 
        "tt_label": "التحقق من الأهلية المجانية (أدخل رقم بطاقة التعريف الوطنية):", 
        "tt_placeholder": "مثال: JF12345", 
        "tt_success": "🎉 تهانينا! بطاقتك تبدأ بـ JF. أنت مؤهل للاستفادة الكاملة والمجانية من النظام.", 
        "tt_fail": "❌ عذراً، رقم هذه البطاقة غير مؤهل للاستفادة من هذه المبادرة المحلية الحصرية.",
        "footer_goals_title": "🎯 أهدافنا", "footer_goals_desc": "تسخير تقنيات الذكاء الاصطناعي المتقدمة لخدمة البشرية وتسهيل الولوج إلى المعلومة القانونية الصارمة، ودعم ريادة الأعمال والابتكار القانوني الرقمي بما يتماشى مع المعايير الدولية المعاصرة.", "footer_addr_title": "📍 العنوان الاجتماعي", "footer_addr_desc": "رقم 11، زنقة العلويين، الحي الإداري، طانطان، المملكة المغربية."
    },
    "fr": {
        "vision_html": "<b>LawMind</b> est la première plateforme marocaine qui met l'intelligence artificielle au service de l'humanité dans le domaine des consultations juridiques.",
        "badge": "Produit 100% Marocain 🇲🇦", "select_lang": "Choisir la Langue", "select_country": "Choisir le Bureau de Pays", "btn_enter": "Lancer l'Intelligence", "placeholder": "Posez votre question juridique stricte ici...", "search_btn": "Consulter le Système", "user_label": "Moi", "back_btn": "⬅ Retour",
        "tt_title": "☀️ Initiative Exclusive de la Province de Tan-Tan", 
        "tt_desc": "Les habitants de la province de Tan-Tan bénéficient d'un accès complet et gratuit au conseiller juridique au Maroc. Veuillez vérifier votre éligibilité.", 
        "tt_label": "Vérifier l'éligibilité gratuite (Entrez le numéro de CNIE / Carte ID) :", 
        "tt_placeholder": "ex: JF12345", 
        "tt_success": "🎉 Félicitations ! Votre carte commence par JF. Vous êtes éligible pour un accès gratuit.", 
        "tt_fail": "❌ Désolé, ce numéro de carte n'est pas éligible pour cette initiative locale.",
        "footer_goals_title": "🎯 Nos Objectifs", "footer_goals_desc": "Exploiter les technologies d'intelligence artificielle pour servir l'humanité, faciliter l'accès à l'information juridique stricte et soutenir l'innovation juridique numérique.", "footer_addr_title": "📍 Siège Social", "footer_addr_desc": "N° 11, Rue Al-Alawiyyin, Quartier Administratif, Tan-Tan, Royaume du Maroc."
    },
    "es": {
        "vision_html": "<b>LawMind</b> es la primera plataforma marroquí que pone la inteligencia artificial al servicio de la humanity en el campo de las consultas jurídicas.",
        "badge": "Producto 100% Marroquí 🇲🇦", "select_lang": "Seleccionar Idioma", "select_country": "Seleccionar Oficina de País", "btn_enter": "Iniciar Inteligencia", "placeholder": "Haga su pregunta legal estricta aquí...", "search_btn": "Consultar Sistema", "user_label": "Yo", "back_btn": "⬅ Volver",
        "tt_title": "☀️ Iniciativa Exclusiva de la Provincia de Tan-Tan", 
        "tt_desc": "Los residentes de la provincia de Tan-Tan se benefician de un acceso total y gratuito al asesor legal en Marruecos. Verifique su elegibilidad.", 
        "tt_label": "Verificar elegibilidad gratuita (Ingrese el número de tarjeta CNIE / ID):", 
        "tt_placeholder": "ej: JF12345", 
        "tt_success": "🎉 ¡Felicitaciones! Su tarjeta comienza con JF. Eres elegible para acceso gratuito.", 
        "tt_fail": "❌ Lo sentimos, este número de tarjeta no es elegible para esta iniciativa.",
        "footer_goals_title": "🎯 Nuestros Objetivos", "footer_goals_desc": "Aprovechar la inteligencia artificial avanzada para servir a la humanidad, facilitar el acceso a información jurídica estricta y apoyar la innovación legal digital.", "footer_addr_title": "📍 Domicilio Social", "footer_addr_desc": "Nº 11, Calle Al-Alawiyyin, Distrito Administrativo, Tan-Tan, Reino de Marruecos."
    },
    "de": {
        "vision_html": "<b>LawMind</b> ist die erste marokkanische Plattform, die künstliche Intelligenz im Dienste der Menschheit im Bereich der Rechtsberatung einsetzt.",
        "badge": "100% Marokkanisches Produkt 🇲🇦", "select_lang": "Sprache auswählen", "select_country": "Länderbüro auswählen", "btn_enter": "Intelligenz starten", "placeholder": "Stellen Sie hier Ihre strenge Rechtsfrage...", "search_btn": "System konsultieren", "user_label": "Ich", "back_btn": "⬅ Zurück",
        "tt_title": "☀️ Exklusive Initiative der Provinz Tan-Tan", 
        "tt_desc": "Einwohner der Provinz Tan-Tan profitieren von einem vollständigen und kostenlosen Zugang zum Rechtsberater in Marokko. Bitte prüfen Sie Ihre Berechtigung.", 
        "tt_label": "Kostenlose Berechtigung prüfen (Geben Sie die CNIE / ID-Kartennummer ein):", 
        "tt_placeholder": "z.B. JF12345", 
        "tt_success": "🎉 Herzlichen Glückwunsch! Ihre Karte beginnt mit JF. Sie sind für den kostenlosen Zugriff berechtigt.", 
        "tt_fail": "❌ Leider ist diese Kartennummer für diese exklusive lokale Initiative nicht berechtigt.",
        "footer_goals_title": "🎯 Unsere Ziele", "footer_goals_desc": "Nutzung fortschrittlicher künstlicher Intelligenz, um der Menschheit zu dienen, den Zugang zu rechtlichen Informationen zu erleichtern und digitale juristische Innovationen zu unterstützen.",
        "footer_addr_title": "📍 Hauptsitz", "footer_addr_desc": "Nr. 11, Al-Alawiyyin-Straße, Verwaltungsbezirk, Tan-Tan, Königreich Marokko."
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
    
    # 🗂️ صناديق خيارات اللغة والدول العليا
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
        
    # 🌟 الإصلاح المطلوب والمثالي: وضع "الخانة والبطاقة التفاعلية الحصرية بالوسط أسفل الخانتين مباشرةً"
    st.markdown(f"""
        <div class="interactive-tantan-card">
            <div class="tantan-title">{current_text["tt_title"]}</div>
            <div class="tantan-desc">{current_text["tt_desc"]}</div>
            <span class="tantan-input-label">💳 {current_text["tt_label"]}</span>
        </div>
    """, unsafe_allow_html=True)
    
    # حقل الإدخال تفاعلي مدمج ومتناسق لغوياً وهندسيّاً بالوسط تماماً
    cnie_input = st.text_input("CNIE Verification Input", placeholder=current_text["tt_placeholder"], label_visibility="collapsed", key="cnie_checker_central").strip()
    
    if cnie_input:
        if cnie_input.upper().startswith("JF"):
            st.success(current_text["tt_success"])
        else:
            st.error(current_text["tt_fail"])
            
    # زر الدخول يظهر مباشرة أسفل لوحة التحكم والتحقق بالمنتصف
    if st.button(current_text["btn_enter"]):
        st.session_state.page = "chat"
        st.rerun()
            
    st.markdown(f'<div class="credits-container"><div class="team-credits">{fixed_credits}</div></div>', unsafe_allow_html=True)

# --- واجهة نظام الشات والاستشارة (Chat Page) ---
elif st.session_state.page == "chat":
    st.markdown('<div class="back-btn-container">', unsafe_allow_html=True)
    if st.button(current_text["back_btn"]):
        st.session_state.page = "landing"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p class="legal-logo">⚖️</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="main-title" style="font-size: 2.2rem;">LawMind | {st.session_state.country} Bureau</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-title" style="font-size: 0.9rem; margin-bottom: 20px;">AI Legal Intelligence</p>', unsafe_allow_html=True)

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
                        f"CRITICAL RULE 2 (THEME GATEKEEPER): You must ONLY answer legal and law-related questions. If the inquiry is outside the boundaries of law, politely decline to answer. "
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

# 🌐 الفوتر الاحترافي الساحر والمترجم ديناميكياً بالكامل حسب اختيار اللغة لقسم "أهدافنا والعنوان"
st.markdown(f"""
    <div class="footer-panel">
        <div class="footer-grid">
            <div class="footer-col">
                <h4>{current_text['footer_goals_title']}</h4>
                <p>{current_text['footer_goals_desc']}</p>
            </div>
            <div class="footer-col">
                <h4>{current_text['footer_addr_title']}</h4>
                <p>📍 {current_text['footer_addr_desc']}<br>
                📧 Contact: support@lawmind.ai</p>
            </div>
        </div>
        <div class="footer-bottom">
            LawMind | AI Legal Intelligence • Powered by Moroccan Innovation 🇲🇦 • © 2026
        </div>
    </div>
""", unsafe_allow_html=True)
