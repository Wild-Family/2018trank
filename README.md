# API Server on Raspberry Pi 3 Model B
2018 trank hackathon in Osaka.

# How to use

1. 以下を用意する
	- Raspberry Pi (3 Model Bのみ動作確認済)
  	- Raspberry Pi用カメラモジュール
  	- Raspberry Pi上のサーバを公開する環境(ngrokで動作確認済)
  	- LINE Botアカウント
  	- Bot用HTTPSサーバ(herokuがおすすめ)

1. 下記リンクよりLINE Botリポジトリをcloneする

1. 同リポジトリ内のindex.phpをコメントに従い修正後，サーバにデプロイ

1. LINE DevelopersページでBotの設定を済ませる

1. 本リポジトリをRaspberry Pi上のサーバにcloneし，「python api.py」でプログラムを実行する

1. オバチャンに「とって」と頼んでみよう！

※LINE Botを動作させるにはPHP拡張モジュールのGDが必要です．
Botサーバをherokuで実行する場合，composer.jsonのrequireに以下が記述されている事を確認した後，`composer update`してください
```
"require": {
	"ext-gd": "*"
}
```

# LINK

- [LINE Bot](https://github.com/Wild-Family/line-bot)

- [Presentation](https://github.com/Wild-Family/presentation)