from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# قائمة اللغات المدعومة
languages = {
    'ar': 'العربية',
    'en': 'الإنجليزية',
    'fr': 'الفرنسية',
    'de': 'الألمانية',
    'es': 'الإسبانية',
    'it': 'الإيطالية',
    'ru': 'الروسية',
    'ja': 'اليابانية',
    'zh-CN': 'الصينية',
    'tr': 'التركية',
    'hi': 'الهندية',
    'pt': 'البرتغالية',
    'ur': 'الأردية',
    'ko': 'الكورية'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    if request.method == 'POST':
        text = request.form.get('text')
        src = request.form.get('src_lang')
        dest = request.form.get('dest_lang')

        if text:
            try:
                url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={src}&tl={dest}&dt=t&q={text}"
                response = requests.get(url)
                translation = response.json()[0][0][0]
            except:
                translation = "حصل خطأ في الترجمة"

    return render_template('index.html', translation=translation, languages=languages)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
