def set_hant(self, level):
    self.ui.text.setText(f"您上次已達到Lv. {level}\n" f"是否繼續？")
    self.ui.play1.setText("繼續")
    self.ui.play2.setText("重新開始")


def set_hans(self, level):
    self.ui.text.setText(f"您上次已达到Lv. {level}\n" f"是否继续？")
    self.ui.play1.setText("继续")
    self.ui.play2.setText("重新开始")


def set_ja(self, level):
    self.ui.text.setText(f"あなたはLv. {level}に達しました。\n" f"続けますか？")
    self.ui.play1.setText("続ける")
    self.ui.play2.setText("リセット")


def lang_module(self, lang, level):
    if lang == "zh-hant":
        set_hant(self, level)
    elif lang == "zh-hans":
        set_hans(self, level)
    elif lang == "ja":
        set_ja(self, level)
