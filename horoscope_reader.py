import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import random

# Full Horoscope data in English
weekly_horoscopes_en = {
    "Aries": [
        "This week, new opportunities are on your side. Embrace change with confidence!",
        "A challenge might surprise you, but your energy will help you overcome it.",
        "Take time for yourself; self-care will recharge your spirit.",
        "Collaboration with friends will open doors to exciting ventures."
    ],
    "Taurus": [
        "Focus on your finances this week. Smart decisions will pay off.",
        "Family matters come into focus; show patience and understanding.",
        "Keep steady and persistent; rewards are coming your way.",
        "A creative idea may inspire you to start a new project."
    ],
    "Gemini": [
        "Communication is your strength this week. Express yourself clearly.",
        "Be ready for unexpected meetings that can lead to growth.",
        "Your curiosity will take you on a fun and educational journey.",
        "Stay grounded and avoid overcommitting to multiple tasks."
    ],
    "Cancer": [
        "Home and comfort dominate your thoughts; spend time with loved ones.",
        "Trust your intuition; it will guide you through tricky situations.",
        "Opportunity for personal growth arises from self-reflection.",
        "An old friend may reconnect with you bringing joy and support."
    ],
    "Leo": [
        "Your enthusiasm attracts positive attention—shine brightly!",
        "Leadership roles will come your way; be prepared to take charge.",
        "Balance your work and play for a fulfilling week.",
        "A burst of creativity will help you solve a lingering problem."
    ],
    "Virgo": [
        "Details matter more than ever; double-check your work for success.",
        "Seek clarity in communication to avoid misunderstandings.",
        "Organization at home or office will ease your stress.",
        "Healthy habits introduced this week can transform your routine."
    ],
    "Libra": [
        "Harmony in relationships is your goal; listen with empathy.",
        "A social event could lead to meaningful connections.",
        "Financial balance is important; avoid impulsive spending.",
        "Your artistic side wants expression—find ways to create."
    ],
    "Scorpio": [
        "Harness your passion to push through difficult tasks.",
        "Secrets or hidden information may come to light—stay alert.",
        "Emotional balance will help you make wise decisions.",
        "New opportunities in career can boost your personal growth."
    ],
    "Sagittarius": [
        "Adventure calls! Take a chance on something new and exciting.",
        "Learning something new will broaden your horizons.",
        "Keep a positive attitude to navigate sudden changes.",
        "Friendships deepen through honest and open conversations."
    ],
    "Capricorn": [
        "Focus on your goals; hard work this week leads to success.",
        "Practical decisions at work will earn respect and recognition.",
        "Don’t neglect self-care in the pursuit of ambition.",
        "Financial planning now can prevent stress later."
    ],
    "Aquarius": [
        "Innovative ideas inspire you; don’t be afraid to share them.",
        "Community and teamwork bring rewarding results.",
        "Be open to new perspectives even if they challenge your views.",
        "Technology could provide useful tools to make life easier."
    ],
    "Pisces": [
        "Your imagination and empathy are your strengths this week.",
        "Creative projects bring joy and fulfillment.",
        "Take time to meditate or connect with nature for peace.",
        "Listen carefully to advice from trusted friends."
    ]
}

# Full Horoscope data in Hindi
weekly_horoscopes_hi = {
    "Aries": [
        "इस सप्ताह, नए अवसर आपके साथ हैं। बदलाव को विश्वास के साथ स्वीकार करें!",
        "एक चुनौती आपको आश्चर्यचकित कर सकती है, लेकिन आपकी ऊर्जा इसे पार कर लेगी।",
        "अपने लिए समय निकालें; स्वयं की देखभाल आपकी आत्मा को पुनः चार्ज करेगी।",
        "मित्रों के साथ सहयोग रोमांचक योजनाओं के द्वार खोलेगा।"
    ],
    "Taurus": [
        "इस सप्ताह अपने वित्त पर ध्यान दें। समझदारी से फैसले करें।",
        "परिवार के मामले महत्वपूर्ण होंगे; धैर्य और समझदारी दिखाएँ।",
        "स्थिर और दृढ़ रहें; पुरस्कार आपकी राह में हैं।",
        "कोई रचनात्मक विचार आपको नया प्रोजेक्ट शुरू करने के लिए प्रेरित कर सकता है।"
    ],
    "Gemini": [
        "इस सप्ताह संचार आपकी ताकत है। स्पष्टता से अपने विचार व्यक्त करें।",
        "अप्रत्याशित मुलाकातों के लिए तैयार रहें जो विकास की ओर ले जाएंगी।",
        "आपकी जिज्ञासा आपको एक मज़ेदार और शैक्षिक यात्रा पर ले जाएगी।",
        "जमीन पर टिके रहें और बहुत सारे कार्यों में खुद को ओवरकमिट न करें।"
    ],
    "Cancer": [
        "घर और आराम आपके विचारों में प्रमुख हैं; प्रियजनों के साथ समय बिताएँ।",
        "अपने अंतर्ज्ञान पर भरोसा करें; यह जटिल परिस्थितियों में मार्गदर्शन करेगा।",
        "आत्म-चिंतन से व्यक्तिगत विकास के अवसर उत्पन्न होंगे।",
        "एक पुराना मित्र आपसे पुनः संपर्क कर सकता है जो आनंद और समर्थन लाएगा।"
    ],
    "Leo": [
        "आपका उत्साह सकारात्मक ध्यान आकर्षित करता है—उज्ज्वल चमकें!",
        "नेतृत्व भूमिकाएं आपके पास आएंगी; नेतृत्व करने के लिए तैयार रहें।",
        "अपने काम और खेल में संतुलन बनाए रखें ताकि सप्ताह संतोषजनक हो।",
        "रचनात्मकता की एक चमक एक लंबित समस्या को हल करने में मदद करेगी।"
    ],
    "Virgo": [
        "इस सप्ताह विवरणों पर विशेष ध्यान दें; सफलता के लिए अपने काम की जाँच करें।",
        "गलतफहमियों से बचने के लिए संचार में स्पष्टता मांगें।",
        "घर या कार्यालय का आयोजन आपके तनाव को कम करेगा।",
        "स्वास्थ्यवर्धक आदतें अपनाने से आपकी दिनचर्या बदल सकती है।"
    ],
    "Libra": [
        "संपर्क में सद्भाव आपका लक्ष्य है; सहानुभूति से सुनें।",
        "एक सामाजिक कार्यक्रम अर्थपूर्ण संबंधों की ओर ले जा सकता है।",
        "वित्तीय संतुलन महत्वपूर्ण है; आवेगी खर्च से बचें।",
        "आपकी कलात्मक पक्ष को अभिव्यक्ति चाहिए—रचनात्मक तरीके खोजें।"
    ],
    "Scorpio": [
        "कठिन कार्यों को पूरा करने के लिए अपने जुनून का उपयोग करें।",
        "गुप्त जानकारियां सामने आ सकती हैं—सचेत रहें।",
        "भावनात्मक संतुलन आपको बुद्धिमान निर्णय लेने में मदद करेगा।",
        "कैरियर में नए अवसर आपकी व्यक्तिगत प्रगति को बढ़ावा देंगे।"
    ],
    "Sagittarius": [
        "साहसिक कार्य आपका आह्वान है! कुछ नया और रोमांचक आजमाएँ।",
        "कुछ नया सीखना आपके दृष्टिकोण को व्यापक बनाएगा।",
        "सकारात्मक दृष्टिकोण रखें ताकि अचानक बदलावों को नेविगेट किया जा सके।",
        "खुले और ईमानदार संवाद से मित्रता गहरी होगी।"
    ],
    "Capricorn": [
        "अपनी मंजिल पर ध्यान केंद्रित करें; इस सप्ताह कड़ी मेहनत सफलता दिलाएगी।",
        "कार्यस्थल पर व्यावहारिक निर्णय आपको सम्मान और मान्यता दिलाएंगे।",
        "महत्वाकांक्षा के पीछा करते हुए स्वयं की देखभाल को नज़रअंदाज न करें।",
        "वित्तीय योजना अब तनाव को भविष्य में रोक सकती है।"
    ],
    "Aquarius": [
        "नवोन्मेषी विचार आपको प्रेरित करते हैं; उन्हें साझा करने से न डरें।",
        "समुदाय और टीम वर्क से फायदेमंद परिणाम मिलेंगे।",
        "नई दृष्टिकोणों के लिए खुले रहें, भले ही वे आपके विचारों को चुनौती दें।",
        "जीवन को आसान बनाने के लिए तकनीक उपयोगी उपकरण प्रदान कर सकती है।"
    ],
    "Pisces": [
        "इस सप्ताह आपकी कल्पना और सहानुभूति आपकी ताकत हैं।",
        "रचनात्मक प्रोजेक्ट आनंद और संतुष्टि लाते हैं।",
        "ध्यान या प्रकृति से जुड़ने के लिए समय निकालें।",
        "विश्वसनीय मित्रों की सलाह ध्यान से सुनें।"
    ]
}

current_language = "English"
weekly_horoscopes = {}

def switch_language_data(lang):
    global weekly_horoscopes, current_language
    if lang.lower() == "hindi":
        weekly_horoscopes = weekly_horoscopes_hi
        current_language = "Hindi"
    else:
        weekly_horoscopes = weekly_horoscopes_en
        current_language = "English"
    update_ui_texts()

def update_ui_texts():
    if current_language == "Hindi":
        instruction_label.config(text="अपना जन्मदिन दर्ज करें (YYYY-MM-DD):")
        calculate_btn.config(text="राशि पता करें")
        horoscope_btn.config(text="साप्ताहिक भविष्य देखें")
        prompt_label.config(text="क्या आप दूसरा भविष्य जानना चाहते हैं?")
        yes_btn.config(text="हाँ")
        no_btn.config(text="नहीं")
        root.title("साप्ताहिक राशिफल ऐप")
    else:
        instruction_label.config(text="Enter your Birthday (YYYY-MM-DD):")
        calculate_btn.config(text="Get Zodiac Sign")
        horoscope_btn.config(text="See Weekly Horoscope")
        prompt_label.config(text="Do you want to get another horoscope?")
        yes_btn.config(text="Yes")
        no_btn.config(text="No")
        root.title("Weekly Horoscope Zodiac Sign App")

def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):

        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"

def show_horoscope():
    sign = zodiac_label.cget("text").split(": ")[1]
    reading = random.choice(weekly_horoscopes.get(sign, ["Horoscope not available."]))
    horoscope_text.config(state='normal')
    horoscope_text.delete("1.0", tk.END)
    if current_language == "Hindi":
        horoscope_text.insert(tk.END, f"{sign} के लिए साप्ताहिक राशिफल:\n\n{reading}")
    else:
        horoscope_text.insert(tk.END, f"Weekly Horoscope for {sign}:\n\n{reading}")
    horoscope_text.config(state='disabled')
    prompt_label.pack(pady=10)
    yes_btn.pack(side="left", padx=10)
    no_btn.pack(side="right", padx=10)

def reset_app():
    birthday_entry.delete(0, tk.END)
    zodiac_label.config(text="")
    horoscope_text.config(state='normal')
    horoscope_text.delete("1.0", tk.END)
    horoscope_text.config(state='disabled')
    prompt_label.pack_forget()
    yes_btn.pack_forget()
    no_btn.pack_forget()
    horoscope_btn.pack_forget()

def exit_app():
    root.destroy()

def calculate_zodiac():
    bday = birthday_entry.get()
    try:
        date_obj = datetime.strptime(bday, "%Y-%m-%d")
        sign = get_zodiac_sign(date_obj.day, date_obj.month)
        if current_language == "Hindi":
            zodiac_label.config(text=f"आपका राशि चिन्ह: {sign}")
        else:
            zodiac_label.config(text=f"Your Zodiac Sign: {sign}")
        horoscope_btn.pack(pady=5)
    except ValueError:
        if current_language == "Hindi":
            messagebox.showerror("त्रुटि", "कृपया अपना जन्मदिन YYYY-MM-DD फॉर्मेट में दर्ज करें।")
        else:
            messagebox.showerror("Invalid date format", "Please enter your birthday in YYYY-MM-DD format.")

def ask_language():
    lang = simpledialog.askstring("Select Language", "Select language for your horoscope reading:\nType 'English' or 'Hindi'")
    if lang is None or lang.lower() not in ['english', 'hindi']:
        messagebox.showinfo("Info", "Defaulting to English.")
        lang = "English"
    switch_language_data(lang)
    show_main_ui()

def show_main_ui():
    instruction_label.pack(pady=10)
    birthday_entry.pack()
    calculate_btn.pack(pady=5)
    zodiac_label.pack()
    horoscope_text.pack(pady=10)

# Tkinter app setup
root = tk.Tk()
root.geometry("400x450")
root.config(bg="#2c3e50")

instruction_label = tk.Label(root, font=("Arial", 14), fg="white", bg="#2c3e50")
birthday_entry = tk.Entry(root, font=("Arial", 14), bg="#34495e", fg="white", insertbackground="white")
zodiac_label = tk.Label(root, font=("Arial", 16, "bold"), pady=10, fg="white", bg="#2c3e50")
calculate_btn = tk.Button(root, command=calculate_zodiac, font=("Arial", 14), bg="#2980b9", fg="white", activebackground="#1abc9c")
horoscope_btn = tk.Button(root, command=show_horoscope, font=("Arial", 14), bg="#32cd32", fg="white", activebackground="#7fff7f")
horoscope_btn.pack_forget()
horoscope_text = tk.Text(root, font=("Arial", 12), height=7, width=45, bg="#34495e", fg="white", wrap="word", state='disabled')
prompt_label = tk.Label(root, font=("Arial", 14), fg="white", bg="#2c3e50")
yes_btn = tk.Button(root, font=("Arial", 12), bg="#2980b9", fg="white", activebackground="#1abc9c", command=reset_app)
no_btn = tk.Button(root, font=("Arial", 12), bg="#ff4500", fg="white", activebackground="#ff7256", command=exit_app)

# Hide all initially
for widget in [instruction_label, birthday_entry, zodiac_label, calculate_btn, horoscope_text, prompt_label, yes_btn, no_btn]:
    widget.pack_forget()
prompt_label.pack_forget()
yes_btn.pack_forget()
no_btn.pack_forget()

# Start app by asking language
root.after(200, ask_language)

root.mainloop()
