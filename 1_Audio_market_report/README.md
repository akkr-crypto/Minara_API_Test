# Audio Market Report Generator

Minara APIを活用して市況レポートを生成し、VOICEVOXを用いて音声で読み上げるWebアプリケーションです。
最新のマーケット情報をテキストと音声の両方で確認することができます。

## 前提条件

*   **Python 3.8+**
*   **VOICEVOX**: 音声合成エンジンとして使用します。事前にインストールし、起動しておく必要があります。
    *   公式サイト: [https://voicevox.hiroshiba.jp/](https://voicevox.hiroshiba.jp/)
*   **ライブラリ**: リポジトリルートで `pip install -r requirements.txt` を実行済みであること。

## 使い方

1.  **VOICEVOXの起動**
    VOICEVOXアプリを起動してください（デフォルト設定のまま、ポート `50021` でAPIサーバーが立ち上がっている必要があります）。

2.  **サーバーの起動**
    このディレクトリ (`1_Audio_market_report`) に移動し、以下のコマンドでアプリケーションサーバーを起動します。

    ```bash
    python server.py
    ```
    
    起動すると `http://localhost:5000` でアクセス可能になります。

3.  **ブラウザでアクセス**
    ブラウザ（Chrome推奨）で http://localhost:5000 を開きます。

4.  **レポート生成**
    *   **API Key**: Minara APIキーを入力します。
    *   **キャラクター**: 読み上げに使用するVOICEVOXのキャラクターを選択します（VOICEVOX起動中に自動取得されます）。
    *   **レポート対象 / プロンプト**: 「今日の市況を教えて」などのプロンプトを入力し、「レポート生成・読み上げ」ボタンを押します。

## 構成

*   `server.py`: Flaskを使用したバックエンドサーバー。Minara APIへのプロキシとして機能します。
*   `templates/index.html`: フロントエンドUI。音声再生の制御やストリーミングテキストの表示を行います。