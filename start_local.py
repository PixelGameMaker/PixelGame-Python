def set_hant(self, level):
    """
    self.ui.label_Music.setText("音樂：")
    self.ui.Windowed_Settings.setText("視窗化")
    self.ui.label_Resolution.setText("解析度：")
    self.ui.Button_Play.setText("選擇職業")
    self.ui.Graphics_Settings.setTitle("顯示設定")
    self.ui.Music_On.setText("開啟")
    self.ui.Music_Off.setText("關閉")
    self.ui.Button_Reset.setText("重設")
    self.ui.Button_Save.setText("儲存")
    """
    self.ui.text.setText(f"您上次已達到Lv. {level}\n"
                         f"是否繼續？")
    self.ui.play1.setText("繼續")
    self.ui.play2.setText("重新開始")


def set_hans(self, level):
    """
    self.ui.label_Music.setText("音乐：")
    self.ui.Windowed_Settings.setText("窗口化")
    self.ui.label_Resolution.setText("分辨率：")
    self.ui.Button_Play.setText("选择职业")
    self.ui.Graphics_Settings.setTitle("显示设置")
    self.ui.Music_On.setText("开启")
    self.ui.Music_Off.setText("关闭")
    self.ui.Button_Reset.setText("重置")
    self.ui.Button_Save.setText("保存")
    """
    self.ui.text.setText(f"您上次已达到Lv. {level}\n"
                         f"是否继续？")
    self.ui.play1.setText("继续")
    self.ui.play2.setText("重新开始")


def set_ja(self, level):
    """
    self.ui.label_Music.setText("音楽：")
    self.ui.Windowed_Settings.setText("ウィンドウ")
    self.ui.label_Resolution.setText("解像度：")
    self.ui.Button_Play.setText("プレイヤーを\n選択")
    self.ui.Graphics_Settings.setTitle("グラフィック設定")
    self.ui.Music_On.setText("オン")
    self.ui.Music_Off.setText("オフ")
    self.ui.Button_Reset.setText("リセット")
    self.ui.Button_Save.setText("セーブ")
    """
    self.ui.text.setText(f"あなたはLv. {level}に達しました。\n"
                         f"続けますか？")
    self.ui.play1.setText("続ける")
    self.ui.play2.setText("リセット")


def lang_module(self, lang, level):
    if lang == "zh-hant":
        set_hant(self, level)
    elif lang == "zh-hans":
        set_hans(self, level)
    elif lang == "ja":
        set_ja(self, level)
