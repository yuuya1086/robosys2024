# BMIコマンド
![test](https://github.com/yuuya1086/robosys2024/actions/workflows/test.yml/badge.svg)

## 概要

自分の体型が気になる…<br>
そんなお悩み抱えていませんか？<br>
このコマンドを使用すると、自分のBMI値、適正体重が分かります。<br>
あなたが今、痩せているのか、肥満気味なのか、適正であるのかをすぐに知ることができます。

## 起動する手順

- gitをインストールしてください。
```bash
   sudo apt install git
```

　 → インストールされたら以下の手順でコマンドを起動してください。

- リポジトリをクローン
```bash
   git clone https://github.com/yuuya1086/robosys2024.git
```
- robosys2024に移動
```bash
   cd robosys2024
```
- 実行権限を付ける
```bash
   chmod +x bmi
```

## 実行方法

（例）身長170cm、体重60㎏の人のBMI値、適正体重を知りたいとき…

- 以下のように身長[cm]、体重[kg]の順で入力し実行。
```bash
   echo 170 60 | ./bmi
```

※注意

入力する身長の単位は[cm]、体重の単位は[㎏]となっています。

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7~3.10

## ライセンス

- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布及び使用が許可されます。
- このコマンドのBMI値、適正体重の計算方法は以下のサイトを基にコードを書いています。

　[参考にしたサイト](https://medipalette.lotte.co.jp/diet/4696#h3-1)

- © 2024 Yuuya Tanaka

## テスト環境
- Ubuntu 22.04 LTS
