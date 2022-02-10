def set_hant(self):
    self.ui.label_Music.setText("音樂：")
    self.ui.Windowed_Settings.setText("視窗化")
    self.ui.label_Resolution.setText("解析度：")
    self.ui.Button_Play.setText("選擇職業")
    self.ui.Graphics_Settings.setTitle("顯示設定")
    self.ui.Music_On.setText("開啟")
    self.ui.Music_Off.setText("關閉")
    self.ui.Button_Reset.setText("重設")
    self.ui.Button_Save.setText("儲存")
    # update_text = "偵測到新版本，是否更新？"


def set_hans(self):
    self.ui.label_Music.setText("音乐：")
    self.ui.Windowed_Settings.setText("窗口化")
    self.ui.label_Resolution.setText("分辨率：")
    self.ui.Button_Play.setText("选择职业")
    self.ui.Graphics_Settings.setTitle("显示设置")
    self.ui.Music_On.setText("开启")
    self.ui.Music_Off.setText("关闭")
    self.ui.Button_Reset.setText("重置")
    self.ui.Button_Save.setText("保存")
    # update_text = "检测到新版本，是否更新？"


def set_ja(self):
    self.ui.label_Music.setText("音楽：")
    self.ui.Windowed_Settings.setText("ウィンドウ")
    self.ui.label_Resolution.setText("解像度：")
    self.ui.Button_Play.setText("プレイヤーを\n選択")
    self.ui.Graphics_Settings.setTitle("グラフィック設定")
    self.ui.Music_On.setText("オン")
    self.ui.Music_Off.setText("オフ")
    self.ui.Button_Reset.setText("リセット")
    self.ui.Button_Save.setText("セーブ")
    # update_text = "新しいバージョンを検出しました。\nアップデートしますか？"


def lang_module(self, lang):
    if lang == "zh-hant":
        set_hant(self)
    elif lang == "zh-hans":
        set_hans(self)
    elif lang == "ja":
        set_ja(self)


def update_word(lang) -> str:
    if lang == "zh-hant":
        update_text = "偵測到新版本，是否更新？"
    elif lang == "zh-hans":
        update_text = "检测到新版本，是否更新？"
    elif lang == "ja":
        update_text = "新しいバージョンを検出しました。\nアップデートしますか？"
    else:
        update_text = "New version detected.\nUpdate?"
    return str(update_text)
