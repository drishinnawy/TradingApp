
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
import arabic_reshaper
from bidi.algorithm import get_display

# تسجيل خط عربي (مرفق بصيغة TTF في مجلد المشروع)
LabelBase.register(name='Cairo', fn_regular='Cairo-Regular.ttf')

class ArabicLabel(Label):
    def __init__(self, **kwargs):
        text = kwargs.pop('text', '')
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        kwargs['text'] = bidi_text
        kwargs['font_name'] = 'Cairo'
        super().__init__(**kwargs)

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(ArabicLabel(text='مرحبًا بك في تطبيق التداول', font_size='24sp'))
        layout.add_widget(ArabicLabel(text='هذا مجرد مثال أولي', font_size='18sp'))
        return layout

if __name__ == '__main__':
    MainApp().run()
