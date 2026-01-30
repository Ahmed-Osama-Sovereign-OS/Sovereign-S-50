from kivymd.app import MDApp
from kivy.core.window import Window
import psutil # لمراقبة المعالج فيزيائياً
import platform

class SovereignS50(MDApp):
    def build(self):
        self.title = "Sovereign S-50 Monster"
        Window.clearcolor = (0, 0, 0, 1) # الأسود المطلق
        # هنا سنضع أول 5 مميزات في الواجهة
        return 

    def get_hardware_entropy(self):
        # ميزة 1: سحب الطاقة العشوائية من المعالج للتشفير
        return psutil.cpu_percent() * 0.12345

SovereignS50().run()
