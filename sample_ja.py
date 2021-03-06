# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import spacy
from spacy.lang.ja.examples import sentences

from summarizer import Summarizer, SentenceHandler, TransformerSummarizer
from spacy.lang.ja import Japanese
body = """
テレビやTwitterと連携できるパソコンや、プロセッサや切り替わるパソコンなど、面白いパソコンが次から次へと登場した。旧式Macの禁断ともいえるパワーアップ方法から、NECの最新PC、話題のThinkPad X1 Hybrid、新セキュリティソフトまで一挙に紹介しよう。

■インテル SSD 520をMacに装着！旧式Macはどれほど高速化するのか (上)
インテルが最新SSD「520シリーズ」を発売した。現行SSDの中でもトップクラスの性能を誇る同製品を、旧型Macの高速化を図るというポイントでレビューしてみた。少し風変わ>りなレビューとなるが、どの程度の効果があるか、期待大である。


■http://itlifehack.jp/archives/6716997.html
ThinkPad X1 Hybridは使用するCPUがx86(インテルCore iなど)からARMに切り替わるハイ>ブリッドなPCだが、これと同時にOSも切り替わる。


■初期費用、更新費用ともに無料！ジャストシステム、ヤモリが目印のセキュリティソフト
現在では、多くのユーザーがパソコンにセキュリティソフトを導入しているが、その過半数は毎年5,000円程度かかる更新費用やその手続きについて不満を持っている。有料ソフトを利用するユーザーの約8割は無料のセキュリティソフトを知っているにもかかわらず、性能面で劣るのではという不安から導入を控えているという状況にある。


■テレビの新しい楽しみ方を提案！NECの春PCはTVとTwitterの連携
NECは2012年2月14日、個人向けデスクトップパソコン「VALUESTAR」シリーズ3タイプ16モデルを2月16日より販売すると発表した。新商品では、よりパワフルになった録画機能に加え、TV視聴・録画機能に業界で初めて人気のTwitterを連携させた「SmartVisionつぶやきプラス」を追加するなど、TVパソコンならではの機能を搭載。スマートフォン、ホームネットワーク対応も強化し、「安心・簡単・快適」なデジタルエンターテイメントの提案として、主要モデルに対し以下の強化を行った。


■まるでお祭りの出荷式！レッツノートSX1の出荷が始まる
2月24日に発売されるLet’snote SX1/NX1の出荷式が2月8日に国内製造拠点の神戸工場で行われた。同社のパソコンとして初めてとなる出荷式で、この製品への力の入れようがわかる。
"""

#import spacy
#from spacy.lang.ja.examples import sentences

#nlp = spacy.load("ja_core_news_sm")
#doc = nlp(body)
#print(doc.text)
#for token in doc:
#    print(token.text, token.pos_, token.dep_)


"""
model = Summarizer(
    model="cl-tohoku/bert-base-japanese",
    sentence_handler= SentenceHandler(language=Japanese)
)
result = model(body, min_length=60)
full = ''.join(result)
print(full)
"""
#print("----")
#result = model(body,min_length=10,max_length=30)
#full = ''.join(result)
#print(full)

print("----")
#result = model(body,min_length=5,max_length=15)
#full = ''.join(result)
#print(full)


model = TransformerSummarizer(
    transformer_type="Bert-ja",
    transformer_model_key="cl-tohoku/bert-base-japanese",
    sentence_handler= SentenceHandler(language=Japanese)
)
result = model(body, min_length=60)
full = ''.join(result)
print(full)


