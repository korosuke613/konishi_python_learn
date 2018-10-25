# Python勉強会

## 第一回課題

1. 体重と身長からBMIを計算し、出力せよ
2. 入力した西暦がうるう年かどうか判別し、出力せよ
3. 整数型の要素を持つリストを引数に取り、要素をすべて文字列型に変換したリストを返す関数を作成せよ

例) `convert_num_to_str([10, 30, 50, 44])`-> `["10", "30", "50", "44"]`

## 第二回課題

### 2-1
２つの整数A、Bをキーボード入力して、値の大きさを判別して、大きい順に数を表示するプログラムを作成せよ。

`-５と１０が入力された場合、以下のような出力を行なう。`

大きいほうは 10 小さいほうは -5 です。

また、上記のプログラムで同じ数が入力された場合にも対応できるようにする。
大小関係がある場合は上記の表示を、同じ数の場合には「２つの数は等しいです」と表示するプログラムを作成する。
ヒント： if 文を２つ組み合わせる。ブロックの中に if 文をおくことができる。

### 2-2
等比数列を出力するプログラム(ex32.c)を作成する。

初項（浮動小数点数a）、公比（浮動小数点数r）、項数（整数m）を入力する。
等比数列を計算（ an=a×r^(n-1), n={1, 2,..., m}）し、以下のように出力する。

初項2、 公比2、項数4の場合の出力例

```
n=1  2.0000
n=2  4.0000
n=3  8.0000
n=4  16.0000
```

### 2-3

入力文字の総文字数（空白、タブ、改行も１文字と数える）を出力するプログラムを作成せよ。

ヒント：文字数をカウントする変数を用意する。

### 2-4
以下のような表(九九)を出力するようにプログラムを作成せよ。

```
  |  1  2  3  4  5  6  7  8  9
------------------------------
 1|  1  2  3  4  5  6  7  8  9
 2|  2  4  6  8 10 12 14 16 18
 3|  3  6  9 12 15 18 21 24 27
 4|  4  8 12 16 20 24 28 32 36
以下、9まで続く
```
ヒント：プログラムの出力は左から右へ進む。改行すると、そこから再び左から右へ進む。
