# Python勉強会

学んだこと
- `if __name__ == "__main__`
- print関数
- input関数
- for文
- if~elif~else文
- 関数定義
- return文
- 型変換
- 型チェック
- 例外処理
- 例外送出
- list, tuple, dict


## 第一回課題

1. 体重と身長からBMIを計算し、出力せよ
2. 入力した西暦がうるう年かどうか判別し、出力せよ
3. 整数型の要素を持つリストを引数に取り、要素をすべて文字列型に変換したリストを返す関数を作成せよ

例) `convert_num_to_str([10, 30, 50, 44])`-> `["10", "30", "50", "44"]`

## 第二回課題

### 2-1 ✓
２つの整数A、Bをキーボード入力して、値の大きさを判別して、大きい順に数を表示するプログラムを作成せよ。

`-５と１０が入力された場合、以下のような出力を行なう。`

大きいほうは 10 小さいほうは -5 です。

また、上記のプログラムで同じ数が入力された場合にも対応できるようにする。
大小関係がある場合は上記の表示を、同じ数の場合には「２つの数は等しいです」と表示するプログラムを作成する。
ヒント： if 文を２つ組み合わせる。ブロックの中に if 文をおくことができる。

### 2-2 ✓
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

## 第3回


### 3-1 ✓
1. 変数 string に文字列 “Apple”を代入すること.
2. string 中に文字 a が含まれているかを出力すること.
3. 変数 my_list にリスト `[4,3,5,2,1,["p","e","n"]]`を代入すること.
4. my_list に 3 の 2 乗を追加すること (3 の 2 乗を指定する).
5. my_list 中のリスト `["p","e","n"]` を my_list から削除して結果を出力すること. 
6. my_list 中の要素 1~3 をそれぞれ 8,7,6 に一括で変更すること.
7. my_list の最小数と最大数を出力すること.
8. my_list の奇数番めの要素のみ出力すること.
9. my_list を数字の大きい順に並べて, 出力すること.


### 3-2
入力した２つの自然数から、ユークリッドの互除法を使って最大公約数を求めて表示するプログラムを作成する。

#### 最大公約数を求めるアルゴリズム
2つの自然数aとbを入力する。ただし a ≧ b
1. aをbで割った余りcを計算する
2. cが0ならば(割り切れたら)、最大公約数はbである
3. cが0でなければ、bを新しいa、cを新しいbとする
4. 1に戻る
