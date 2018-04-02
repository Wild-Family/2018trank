# API Server on Raspberry Pi 3 Model B
2018 trank hackathon in Osaka.

# How to use

1. 以下を用意する
    - Raspberry Pi (3 Model Bのみ動作確認済)
    - Raspberry Pi用カメラモジュール
    - Raspberry Pi上のサーバを公開する環境(ngrokで動作確認済)
    - LINE Botアカウント
    - Bot用HTTPSサーバ(herokuがおすすめ)
    - [GCP](https://cloud.google.com/?hl=ja)への登録
	

1. 下記リンクよりLINE Botリポジトリをcloneする

1. 同リポジトリ内のindex.phpをコメントに従い修正後，サーバにデプロイ

1. LINE DevelopersページでBotの設定を済ませる

1. 下記の手順よりGoogle Cloud Vision APIの登録を済ませる

1. 本リポジトリをRaspberry Pi上のサーバにcloneし，「python api.py」でプログラムを実行する

1. オバチャンに「とって」と頼んでみよう！

※LINE Botを動作させるにはPHP拡張モジュールのGDが必要です．
Botサーバをherokuで実行する場合，composer.jsonのrequireに以下が記述されている事を確認した後，`composer update`してください
```
"require": {
	"ext-gd": "*"
}
```

# Google Cloud Vision API
顔認識機能のためにGCPの[Google Cloud Vidion API](https://cloud.google.com/vision/?hl=ja) を使用します。

## 手順
- [プロジェクトを選択または作成](https://console.cloud.google.com/project?hl=ja&_ga=2.186290091.-386517192.1516293238)
- [プロジェクトの課金を有効にする](https://support.google.com/cloud/answer/6293499?hl=ja#enable-billing)(月1000リクエストまで無料です)
- [Google Cloud Vision API を有効にする](https://console.cloud.google.com/flows/enableapi?apiid=vision.googleapis.com&hl=ja&_ga=2.210888471.-386517192.1516293238)
- [アプリケーションのデフォルト認証情報を使用するための環境を設定](https://cloud.google.com/vision/docs/common/auth?hl=ja#authenticating_with_application_default_credentials)
- Pythonの設定
    - [Pythonのインストール](https://www.python.org/)
    	- Python 3を選択してください
    - [google client ライブラリのインストール](https://cloud.google.com/vision/docs/reference/libraries?hl=ja#installing_the_client_library)([ライブラリのドキュメント](https://googlecloudplatform.github.io/google-cloud-python/#/docs))
    - [pillow ライブラリのインストール](https://pillow.readthedocs.io/en/latest/)
  
# LINK
- [LINE Bot](https://github.com/Wild-Family/line-bot)
- [Presentation](https://github.com/Wild-Family/presentation)