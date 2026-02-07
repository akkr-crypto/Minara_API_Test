# Minara API Test Repository

Minara APIを活用した各種テストアプリケーションを含むリポジトリです。

## 全体セットアップ

このリポジトリ内のアプリケーションを実行する前に、以下の手順で環境を構築してください。

1.  **Python環境の準備**
    Python 3.8以上が必要です。

2.  **依存ライブラリのインストール**
    リポジトリのルートディレクトリで以下のコマンドを実行し、必要なライブラリを一括インストールしてください。

    ```bash
    pip install -r requirements.txt
    ```

## コンテンツ

*   **[1_Audio_market_report](1_Audio_market_report/)**: 市況レポートを生成し、VOICEVOXを用いて音声で読み上げるWebアプリケーション。