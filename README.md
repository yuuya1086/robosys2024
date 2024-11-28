# BMIコマンド
![test](https://github.com/yuuya1086/robosys2024/actions/workflows/test.yml/badge.svg)

## 概要

自分の体型が気になる…'\n'
そんなお悩み抱えていませんか？'\n'
このコマンドを使用すると、自分のBMI値、適正体重が分かります。'\n'
あなたが今、痩せているのか、肥満気味なのか、適正であるのかをすぐ知ることができます。

## インストール方法

以下の手順でコマンドをインストールしてください。

- リポジトリをクローン
```bash
git clone https://github.com/yuuya1086/robosys2024.git
```
- robosys2024に移動
```bash
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
