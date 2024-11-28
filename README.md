# BMIコマンド
![test](https://github.com/yuuya1086/robosys2024/actions/workflows/test.yml/badge.svg)

## 概要

このコマンドを使用すると、自分のBMI値、適正体重が分かります。

## インストール方法

以下の手順でコマンドをインストールしてください。

- リポジトリをクローン
```bash
git clone https://github.com/yuuya1086/robosys2024.git
```
```bash
- robosys2024に移動
cd robosys2024
```

## 実行方法

- 身長170cm、体重60㎏の人のBMI値、適正体重を知りたいとき…
```bash
　 ./BMI.py 170 60
```
　 ↑ 上記のように入力してください。

※注意

入力する身長の単位は[cm]、体重の単位は[㎏]となっています。

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7~3.10

## テスト環境
- Ubuntu 24.04 LTS
