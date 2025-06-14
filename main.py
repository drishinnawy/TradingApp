print('Hello from modified TradingApp')
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
import webbrowser
import csv
import os
import random
import datetime
import requests

Window.size = (360, 700)  # يمكنك جعلها ديناميكية لاحقًا

KV = '''
MDScreen:
    MDTopAppBar:
        title: "أفضل حاسبة تداول"
        elevation: 4
        pos_hint: {"top": 1}

    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(10)
            spacing: dp(10)
            adaptive_height: True

            MDLabel:
                text: "معلومات السهم"
                halign: "right"
                bold: True

            MDTextField:
                id: stock_name
                hint_text: "اسم السهم"
                mode: "rectangle"

            MDTextField:
                id: stock_code
                hint_text: "رقم السهم"
                mode: "rectangle"

            MDTextField:
                id: platform_fee
                hint_text: "نسبة المنصة (مثال: 0.0015)"
                text: "0.0015"
                mode: "rectangle"

            MDLabel:
                text: "العملة"
                halign: "right"
                bold: True

            MDTextField:
                id: currency
                hint_text: "العملة (مثال: SAR, USD, EUR)"
                text: "SAR"
                mode: "rectangle"

            MDLabel:
                text: "عمليات الشراء"
                halign: "right"
                bold: True

            GridLayout:
                cols: 2
                row_force_default: True
                row_default_height: dp(50)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "السعر"
                MDLabel:
                    text: "العدد"

                MDTextField:
                    id: price1
                    hint_text: "سعر 1"
                MDTextField:
                    id: qty1
                    hint_text: "عدد 1"

                MDTextField:
                    id: price2
                    hint_text: "سعر 2"
                MDTextField:
                    id: qty2
                    hint_text: "عدد 2"

                MDTextField:
                    id: price3
                    hint_text: "سعر 3"
                MDTextField:
                    id: qty3
                    hint_text: "عدد 3"

                MDTextField:
                    id: price4
                    hint_text: "سعر 4"
                MDTextField:
                    id: qty4
                    hint_text: "عدد 4"

                MDTextField:
                    id: price5
                    hint_text: "سعر 5"
                MDTextField:
                    id: qty5
                    hint_text: "عدد 5"

            MDTextField:
                id: sell_price
                hint_text: "سعر البيع"
                mode: "rectangle"

            MDRaisedButton:
                text: "حساب المتوسط والتكلفة والربح"
                on_release: app.calculate()

            MDLabel:
                id: result_label
                text: ""
                halign: "center"

            MDRaisedButton:
                text: "فتح صفحة السهم في تكرشارت"
                on_release: app.open_tickerchart()

            MDRaisedButton:
                text: "عرض شرعية السهم من أرقام"
                on_release: app.open_sharia()

            MDRaisedButton:
                text: "عرض توصيات"
                on_release: app.show_recommendations()

            MDRaisedButton:
                text: "حفظ CSV"
                on_release: app.save_csv()

            MDRaisedButton:
                text: "تحميل كـ PDF"
                on_release: app.export_pdf()
'''

class TradingApp(MDApp):
    def build(self):
    self.title = "أفضل حاسبة تداول"
    self.theme_cls.primary_palette = "BlueGray"
    self.theme_cls.theme_style = "Light"
    return Builder.load_file("tradingapp.kv")

    def get_currency_rate(self, currency):
        try:
            if currency.upper() == "SAR":
                return 1
            response = requests.get("https://api.exchangerate.host/latest?base=SAR")
            response.raise_for_status()
            data = response.json()
            return data.get('rates', {}).get(currency.upper(), 1)
        except requests.exceptions.RequestException:
            return 1

    def calculate(self):
        try:
            total_cost, total_qty, prices = 0, 0, []
            for i in range(1, 6):
                price, qty = self.root.ids[f'price{i}'].text, self.root.ids[f'qty{i}'].text
                if price and qty:
                    p, q = float(price), int(qty)
                    total_cost += p * q
                    total_qty += q
                    prices.append(p)

            avg_price = total_cost / total_qty if total_qty > 0 else 0
            sell_price = float(self.root.ids['sell_price'].text or 0)
            platform_fee = float(self.root.ids['platform_fee'].text)
            total_cost_with_fee = total_cost * (1 + platform_fee)
            total_sell = sell_price * total_qty * (1 - platform_fee)
            profit = total_sell - total_cost_with_fee

            currency = self.root.ids['currency'].text.upper()
            rate = self.get_currency_rate(currency)

            self.root.ids['result_label'].text = f"متوسط السعر: {avg_price * rate:.2f} {currency}\nالتكلفة الإجمالية: {total_cost_with_fee * rate:.2f} {currency}\nالربح/الخسارة: {profit * rate:.2f} {currency}"
        except Exception as e:
            Snackbar(text=f"خطأ في الحساب: {str(e)}").open()

    def open_tickerchart(self):
        code = self.root.ids['stock_code'].text.strip()
        if code:
            webbrowser.open(f"https://www.tickerchart.net/app/ar?symbol={code}")

    def open_sharia(self):
        webbrowser.open("https://www.argaam.com/ar/company/shariahcompanies")

if __name__ == '__main__':
    TradingApp().run()
