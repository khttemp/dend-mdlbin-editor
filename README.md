# dend-mdlbin-editor

## 概要

dend-mdlbin-editor は、電車でD ClimaxStage、RisingStage のモデルバイナリを、GUI画面上で編集するソフトウェアである。

## 動作環境

* 電車でDが動くコンピュータであること
* OS: Windows 10 64bit の最新のアップデートであること
* OSの端末が日本語に対応していること

※ MacOS 、 Linux などの Unix 系 OS での動作は保証できない。

## 免責事項

このプログラムを使用して発生したいかなる損害も製作者は責任を負わない。

このプログラムを実行する前に、自身のコンピュータのフルバックアップを取得して、
安全を担保したうえで実行すること。
このプログラムについて、電車でD 作者である、地主一派へ問い合わせてはいけない。

このソフトウェアの更新やバグ取りは、作者の義務ではなく解消努力目標とする。
Issue に上げられたバグ情報が必ず修正されるものではない。

* ライセンス：MIT

電車でD の正式なライセンスを持っていること。

本プログラムに関連して訴訟の必要が生じた場合、東京地方裁判所を第一審の専属的合意管轄裁判所とする。

このプログラムのバイナリを実行した時点で、この規約に同意したものと見なす。

## 実行方法

![title](https://github.com/khttemp/dend-mdlbin-editor/blob/main/image/title.png)

1. メニュの「ファイルの開く」で指定のBINファイルを開く。

    そのバイナリファイルは、【モデル名_番号.BIN】の形式である。

    例）H2000_00.BIN、H2800_00.BIN、MU2000_0.BIN・・・

    必ず、プログラムが書込みできる場所で行ってください

2. スクリプト内容の行を選ぶ

    このバイナリファイルの構成は全部10個のリストがあり

    このリストの中から、さらに分けられている。

    区切りの形式は【---#9, 9#---】とした。（以下、9-9とする）

3. 区切りの行を選択すると、現在のリストの数を修正できる。

    区切りを基準に、さらに増やしたり、減らすことが出来る。

4. コマンドの行を選択すると、このコマンドを修正、挿入、削除、コピーできる。

    コピーしたコマンドは区切りの中で挿入できる。

5. このプログラムは、コマンドや区切りに修正を加えた瞬間、すぐ保存される。

## ソースコード版の実行方法

このソフトウェアは Python3 系で開発されているため、 Python3 系がインストールされた開発機であれば、
ソースコードからソフトウェアの実行が可能である。


### 依存ライブラリ

* Tkinter

  Windows 版 Python3 系であれば、インストール時のオプション画面で tcl/tk and IDLE のチェックがあったと思う。
  tcl/tk and IDLE にチェックが入っていればインストールされる。
  
  Linux 系 OS では、 パッケージ管理システムを使用してインストールする。

### 動作環境

以下の環境で、ソースコード版の動作確認を行った

* OS: Windows 10 64bit
* Python 3.7.9 64bit
* pip 21.2.4 64bit
* PyInstaller 3.4 64bit
* 横960×縦640ピクセル以上の画面解像度があるコンピュータ

### ソースコードの直接実行

Windows であれば以下のコマンドを入力する。


````
> python mdlDecrypt.py
````

これで、実行方法に記載した画面が現れれば動作している。

### FAQ

* Q. ImportError: No module named tkinter と言われて起動しない

  * A. 下のようなメッセージだろうか？ それであれば、 tkinter がインストールされていないので、インストールすること。
  
  ````
  > python editor.py
  Traceback (most recent call last):
    File "editor.py", line 6, in <module>
      from tkinter import *
  ImportError: No module named tkinter
  ````


* Q. 電車でDのゲームがあるが、指定したBINファイルがない。  

  * A. PackファイルをGARbro のような、アーカイバで展開すると得られる。

  * A. GARbro を使用して空パスワードで解凍すると無効なファイルになるので、適切なパスワードを入力すること。


* Q. BINファイルを指定しても、「電車でDのファイルではない、またはファイルが壊れた可能性があります。」と言われる

  * A. 抽出方法が間違っているか、抽出時のパスワードが間違っているのでは？作業工程をやり直した方がよい。

* Q. BINファイルを改造しても、変化がないけど？

  * A. 既存のPackファイルとフォルダーが同時にあるなら、Packファイルを優先して読み込んでいる可能性がある。

    読み込みしないように、抽出したPackファイルを変更するか消そう。

* Q. ダウンロードがブロックされる、実行がブロックされる、セキュリティソフトに削除される

  * A. ソフトウェア署名などを行っていないので、ブラウザによってはダウンロードがブロックされる

  * A. 同様の理由でセキュリティソフトが実行を拒否することもある。


### Windows 版実行バイナリ（ .exeファイル ）の作成方法

pyinstaller か py2exe ライブラリをインストールする。 pip でも  easy_install  でも構わない。

下は、 pyinstaller を使用して、Windows 版実行バイナリ（ .exeファイル ）を作る例である。

````
> pyinstaller mdlDecrypt.py --onefile
（ コンソール出力は省略 ）
````

dist フォルダーが作られて、 mdlDecrypt.exe が出力される。

### Virustotal

![virustotal](https://github.com/khttemp/dend-mdlbin-editor/blob/main/image/virustotal.png)


## モデルバイナリの改造方法

### モデルを180度回転する

![180-1](https://github.com/khttemp/dend-mdlbin-editor/blob/main/image/180-1.png)

モデルの回転は0-0の枠でやっている。

CHK_OBJ_PARAMで、インデックスが7の場合（8両目）の場合

FROM 100に移動し、コマンドで180度回転している。

インデックスが7ではない場合、FROM 300に移動する。

これを応用し、下記の図が阪急2000系の4両目と8両目を180度回転したバイナリである。

※必ず、Climax Stageの場合は「TRAIN_DATA3RD.BIN」

  　Rising Stageの場合は「TRAIN_DATA4TH.BIN」の

  　モデルインデックスの並びも修正すること。

![180-2](https://github.com/khttemp/dend-mdlbin-editor/blob/main/image/180-2.png)

適用した画像

![180-3](https://github.com/khttemp/dend-mdlbin-editor/blob/main/image/180-3.png)

### 幕の設定方法

![maku1](https://github.com/khttemp/dend-mdlbin-editor/blob/main/image/maku1.png)

幕の設定は0-2の枠でやっている。

CHK_CAUSEのコマンドで、選択したコース名を比較し

一致すれば2番目のFROMの行、違う場合、3番目のFROMの行まで移動する

そして、CHG_ANIMEで、指定している枠で幕を設定する

例）300（名鉄名古屋本線）の場合、8-14で設定した幕に変える

### 幕のファイル入れ方

![maku2](https://github.com/khttemp/dend-mdlbin-editor/blob/main/image/maku2.png)

幕のファイルは、リスト8の中で保存する

さっきの、名鉄名古屋本線の8-14の場合、

SWAP_TXで、幕のファイル（H2000_To_Toyohashi.png、H2000_Side_Toyohashi.png）を指定している。

この画像ファイルは、PackのMDLフォルダー入れる必要がある。

### 回送幕

推測であるが、9-4の枠でやっている可能性が高い

ただ、モデルによって回送幕の変え方が違ったりすることもあるので注意が必要。

以上。