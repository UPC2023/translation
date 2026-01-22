# 翻译质量评估报告 (LaBSE 语义相似度)

- 原文来源: `/home/cyw/pro/train_data/train_cleaned_filled.jsonl` (input 字段)
- deepseek 文件: `/home/cyw/pro/train_data/train_cleaned_filled.jsonl`
- deepseek2 文件: `/home/cyw/pro/train_data/train_cleaned_filled.jsonl`
- LaBSE 模型: `sentence-transformers/LaBSE`
- device: `cpu`

## 统计

- deepseek 平均得分: 0.7282
- deepseek2 平均得分: 0.7282
- deepseek 优于 deepseek2: 0
- deepseek2 优于 deepseek: 0
- 平手: 1025
- 参与统计句子数: 1025

## 明细对比表

| 序号 | 日语原文 | deepseek翻译 | deepseek得分 | deepseek2翻译 | deepseek2得分 | 优胜方 |
|---:|---|---|---:|---|---:|---|
| 1 | 結構ガッツリ。 | That's pretty intense. | 0.7817 | That's pretty intense. | 0.7817 | 平手 |
| 2 | その時歌ったり踊ったりしてないんですか？ | Aren't you singing or dancing at that time? | 0.9390 | Aren't you singing or dancing at that time? | 0.9390 | 平手 |
| 3 | 歌は基本してなくてダンスのほうは続けてました。 | I wasn't really singing much, but I kept up with dancing. | 0.7520 | I wasn't really singing much, but I kept up with dancing. | 0.7520 | 平手 |
| 4 | 変声期で | Because my voice was changing. | 0.2896 | Because my voice was changing. | 0.2896 | 平手 |
| 5 | のどはあんまり使えないけどダンスをその間にやろうかと。 | I can't really use my voice much, so maybe I'll dance instead. | 0.6922 | I can't really use my voice much, so maybe I'll dance instead. | 0.6922 | 平手 |
| 6 | それ休んでるって感覚なんですか？ | Do you feel like you're resting? | 0.8714 | Do you feel like you're resting? | 0.8714 | 平手 |
| 7 | それとももう芸能界戻らなくても | Or maybe you don't have to return to show business anymore? | 0.6652 | Or maybe you don't have to return to show business anymore? | 0.6652 | 平手 |
| 8 | このまま違う仕事してもいいのかなくらいの | I'm starting to wonder if it's okay for me to keep doing a different job like this. | 0.6618 | I'm starting to wonder if it's okay for me to keep doing a different job like this. | 0.6618 | 平手 |
| 9 | どっちなんですか？ | Which one is it? | 0.8828 | Which one is it? | 0.8828 | 平手 |
| 10 | 歌うための休みだったので。≫意識的には戻るぞって？ | It was a break for singing. ≫ So you're consciously trying to come back? | 0.8311 | It was a break for singing. ≫ So you're consciously trying to come back? | 0.8311 | 平手 |
| 11 | 何か変な自分の気持ちというか歌とダンスはやるだろうな、多分 | I have this strange feeling... I'll probably end up singing and dancing. | 0.6743 | I have this strange feeling... I'll probably end up singing and dancing. | 0.6743 | 平手 |
| 12 | そういう人生なんだろうなと何となく思ってたので。 | I had this vague feeling that this must be how my life was meant to be. | 0.7534 | I had this vague feeling that this must be how my life was meant to be. | 0.7534 | 平手 |
| 13 | でもちょっと不安じゃない？それだけ休んでるし | But aren't you a little worried? You've been taking so much time off. | 0.7147 | But aren't you a little worried? You've been taking so much time off. | 0.7147 | 平手 |
| 14 | あと、声変わりしちゃったら前みたいに | Also, if my voice changes, I won't be able to sing like before. | 0.7216 | Also, if my voice changes, I won't be able to sing like before. | 0.7216 | 平手 |
| 15 | 歌えないんじゃないかとか | I'm worried I might not be able to sing. | 0.6463 | I'm worried I might not be able to sing. | 0.6463 | 平手 |
| 16 | そういうショービジネスというか。 | That kind of show business, or whatever you call it. | 0.6627 | That kind of show business, or whatever you call it. | 0.6627 | 平手 |
| 17 | こんなに休んでたらまたいけるのかなっていう | I wonder if I'll be able to go again if I rest this much. | 0.8204 | I wonder if I'll be able to go again if I rest this much. | 0.8204 | 平手 |
| 18 | 気持ちはなかった？ | Didn't you feel that way? | 0.8619 | Didn't you feel that way? | 0.8619 | 平手 |
| 19 | やっぱり最初は本当に先週出てたキーが | At first, the notes I could hit one week wouldn’t come out the next. | 0.5803 | At first, the notes I could hit one week wouldn’t come out the next. | 0.5803 | 平手 |
| 20 | 今週出ないとか全然あったんですよ。 | There were definitely times when I didn't show up this week. | 0.7374 | There were definitely times when I didn't show up this week. | 0.7374 | 平手 |
| 21 | 最後に作ってたアルバムとかは全曲違う人が | For the last album I was making, every song had a different producer. | 0.6908 | For the last album I was making, every song had a different producer. | 0.6908 | 平手 |
| 22 | 歌ってるみたいなくらい | It's almost like I'm singing. | 0.6461 | It's almost like I'm singing. | 0.6461 | 平手 |
| 23 | どんどん低くなっていったんですけど | It kept getting lower and lower, but... | 0.7168 | It kept getting lower and lower, but... | 0.7168 | 平手 |
| 24 | でもやっぱり周りのスタッフさん含め | But after all, including the staff around me | 0.8350 | But after all, including the staff around me | 0.8350 | 平手 |
| 25 | 歌うためにしっかり休もうと。今、のどを使うと | I should rest properly to sing. If I use my voice now... | 0.7135 | I should rest properly to sing. If I use my voice now... | 0.7135 | 平手 |
| 26 | 良くないから休もうという結構ポジティブな感じだったので。 | It actually had a pretty positive vibe, like 'Let's rest since this isn't good.' | 0.6874 | It actually had a pretty positive vibe, like 'Let's rest since this isn't good.' | 0.6874 | 平手 |
| 27 | 周りのスタッフさんとか事務所とかも理解あるというかね。 | The staff around me and the office are quite understanding, you know. | 0.8138 | The staff around me and the office are quite understanding, you know. | 0.8138 | 平手 |
| 28 | そこをガッツリ５年ですよだって。 | He said he's been doing it wholeheartedly for five years straight. | 0.6261 | He said he's been doing it wholeheartedly for five years straight. | 0.6261 | 平手 |
| 29 | ５年って芸能界ではもう忘れちゃいますよね。 | Five years is enough time for people in the entertainment industry to forget about you. | 0.7033 | Five years is enough time for people in the entertainment industry to forget about you. | 0.7033 | 平手 |
| 30 | 昔の人みたいなイメージが。 | You give off an old-fashioned vibe. | 0.4593 | You give off an old-fashioned vibe. | 0.4593 | 平手 |
| 31 | そこは結構思い切り決断をしてくれたので | They actually made a pretty decisive decision there. | 0.6524 | They actually made a pretty decisive decision there. | 0.6524 | 平手 |
| 32 | そこは今本当に感謝していますね。 | I'm truly grateful for that right now. | 0.9339 | I'm truly grateful for that right now. | 0.9339 | 平手 |
| 33 | 若いというかさっき見たように | Well, more like young... as you just saw. | 0.6736 | Well, more like young... as you just saw. | 0.6736 | 平手 |
| 34 | 幼いころからやってるから | I've been doing it since I was little. | 0.8107 | I've been doing it since I was little. | 0.8107 | 平手 |
| 35 | 逆にね、そこから…。だって別に、声が変わってから | Actually, from that point on... I mean, it's not like my voice changed or anything. | 0.6559 | Actually, from that point on... I mean, it's not like my voice changed or anything. | 0.6559 | 平手 |
| 36 | デビューする人もいっぱいいるわけだから | After all, there are plenty of people making their debut. | 0.6664 | After all, there are plenty of people making their debut. | 0.6664 | 平手 |
| 37 | そういう意味では良かったのかもしれないですね。 | In that sense, it might have been for the best. | 0.8237 | In that sense, it might have been for the best. | 0.8237 | 平手 |
| 38 | さっき設楽さんがおっしゃった | As Mr. Shitara mentioned earlier | 0.4220 | As Mr. Shitara mentioned earlier | 0.4220 | 平手 |
| 39 | 学校の行事だったりとか小学校の時に活動してたので | I was active in school events and such back in elementary school, so... | 0.7816 | I was active in school events and such back in elementary school, so... | 0.7816 | 平手 |
| 40 | 結構出れなかったことも多かったんです。 | There were actually quite a few times when I couldn't make it. | 0.7142 | There were actually quite a few times when I couldn't make it. | 0.7142 | 平手 |
| 41 | 撮影があるから学校行事出れないとか。 | I can't attend the school event because I have filming. | 0.8909 | I can't attend the school event because I have filming. | 0.8909 | 平手 |
| 42 | それが中学校になって結構ガッツリ学校生活を送って | When I got to middle school, I really threw myself into school life. | 0.6739 | When I got to middle school, I really threw myself into school life. | 0.6739 | 平手 |
| 43 | 運動会みたいなのやったりとか | We do things like sports festivals and such. | 0.6536 | We do things like sports festivals and such. | 0.6536 | 平手 |
| 44 | 部活やったり。それが結構楽しかったというか。 | I joined a club activity. It was actually pretty fun, you know? | 0.7546 | I joined a club activity. It was actually pretty fun, you know? | 0.7546 | 平手 |
| 45 | そこはいい機会だと思う。 | I think that's a good opportunity. | 0.9490 | I think that's a good opportunity. | 0.9490 | 平手 |
| 46 | 僕も振り返ったら思いますよ。 | I think about it too when I look back. | 0.8117 | I think about it too when I look back. | 0.8117 | 平手 |
| 47 | 大知先生の歴史の中で…。 | In Professor Daichi's history... | 0.8734 | In Professor Daichi's history... | 0.8734 | 平手 |
| 48 | 設楽さんが振り返ってくださったんだ。 | Mr. Shitara kindly looked back for me. | 0.4917 | Mr. Shitara kindly looked back for me. | 0.4917 | 平手 |
| 49 | ５年というのは大事だったんじゃないかなと。 | I think those five years must have been really important. | 0.8589 | I think those five years must have been really important. | 0.8589 | 平手 |
| 50 | 三浦大知を作り上げる礎となった期間。 | The period that became the foundation for building Daichi Miura. | 0.8135 | The period that became the foundation for building Daichi Miura. | 0.8135 | 平手 |
| 51 | 誰ですか？≫三浦大知史を語る | Who is it? ≫ Let me tell you about Daichi Miura's history. | 0.7177 | Who is it? ≫ Let me tell you about Daichi Miura's history. | 0.7177 | 平手 |
| 52 | コメンテーターの。 | The commentator's. | 0.6809 | The commentator's. | 0.6809 | 平手 |
| 53 | 専門家の設楽さんが…。 | Our expert Mr. Shitara... | 0.6245 | Our expert Mr. Shitara... | 0.6245 | 平手 |
| 54 | お仕事の一面今はお話しいただいたんですが | You've told me about one aspect of your work now, but... | 0.7435 | You've told me about one aspect of your work now, but... | 0.7435 | 平手 |
| 55 | ここからは、プライベートに迫っていこうと思います。 | From this point on, I'd like to delve into their private lives. | 0.6956 | From this point on, I'd like to delve into their private lives. | 0.6956 | 平手 |
| 56 | 今日は三浦さんと大変親交があります | Today I'm having a very friendly conversation with Mr. Miura. | 0.7329 | Today I'm having a very friendly conversation with Mr. Miura. | 0.7329 | 平手 |
| 57 | 本日ゲスト三浦大知さんなんですけれども | Today's guest is Daichi Miura. | 0.8123 | Today's guest is Daichi Miura. | 0.8123 | 平手 |
| 58 | 親交のあるＡＩさんからパパとしての三浦大知さんの | From our mutual friend AI-san, about Daichi Miura as a father | 0.7348 | From our mutual friend AI-san, about Daichi Miura as a father | 0.7348 | 平手 |
| 59 | タレコミをいただいております。 | We've received a tip. | 0.5630 | We've received a tip. | 0.5630 | 平手 |
| 60 | 大変優しいからお子さんに対しても | She's extremely kind, even towards children. | 0.7159 | She's extremely kind, even towards children. | 0.7159 | 平手 |
| 61 | 甘やかしていそうだと | It seems like you're spoiling them. | 0.3348 | It seems like you're spoiling them. | 0.3348 | 平手 |
| 62 | 思っていましたが意外としっかりしているんだなと | I thought you'd be different, but you're actually quite reliable. | 0.5286 | I thought you'd be different, but you're actually quite reliable. | 0.5286 | 平手 |
| 63 | 思いましたというコメントでした。 | The comment said, 'I thought so.' | 0.7953 | The comment said, 'I thought so.' | 0.7953 | 平手 |
| 64 | どういうことだろう、これ。 | What does this mean? | 0.7945 | What does this mean? | 0.7945 | 平手 |
| 65 | あ〜ってやってんじゃないの？って。 | You're doing it like 'ahhh~', aren't you? | 0.6435 | You're doing it like 'ahhh~', aren't you? | 0.6435 | 平手 |
| 66 | デレデレの。≫結構言っちゃいますね。 | You're being all lovey-dovey. ≫ I end up saying that quite often, don't I? | 0.5056 | You're being all lovey-dovey. ≫ I end up saying that quite often, don't I? | 0.5056 | 平手 |
| 67 | 片付けなさいとか | Stop telling me to clean up. | 0.4297 | Stop telling me to clean up. | 0.4297 | 平手 |
| 68 | お風呂入りなさいとか。≫結構言っちゃうほうだと | Things like 'Go take a bath.' ≫ I end up saying that kind of thing quite often. | 0.6292 | Things like 'Go take a bath.' ≫ I end up saying that kind of thing quite often. | 0.6292 | 平手 |
| 69 | 思います。 | I think. | 0.9143 | I think. | 0.9143 | 平手 |
| 70 | 本当？すごいずっと一緒に踊ってる感じがするけど。 | Really? It's amazing - I feel like we've been dancing together forever. | 0.7824 | Really? It's amazing - I feel like we've been dancing together forever. | 0.7824 | 平手 |
| 71 | もちろん一緒に踊ったりとかもするんですけど | Of course we dance together and all, but... | 0.7220 | Of course we dance together and all, but... | 0.7220 | 平手 |
| 72 | 部屋が片付いてなかったりとか | My room wasn't cleaned up and stuff like that. | 0.6817 | My room wasn't cleaned up and stuff like that. | 0.6817 | 平手 |
| 73 | やらなきゃいけないプリントが | I've got worksheets I have to do. | 0.5803 | I've got worksheets I have to do. | 0.5803 | 平手 |
| 74 | ずっとあったりとかすると何それ？とかっていう感じで | If it keeps happening, I'm like 'What's that all about?' | 0.6615 | If it keeps happening, I'm like 'What's that all about?' | 0.6615 | 平手 |
| 75 | 結構チクチク言っちゃうんですよ。 | I tend to nag quite a bit, you know. | 0.6464 | I tend to nag quite a bit, you know. | 0.6464 | 平手 |
| 76 | そういう面もあるんだ。≫パパの動画も見るんですか？ | I see that side of things too. ≫ Do you watch Dad's videos too? | 0.8794 | I see that side of things too. ≫ Do you watch Dad's videos too? | 0.8794 | 平手 |
| 77 | 子供がですか。結構ミュージックビデオ | Is it for children? Quite a music video. | 0.7591 | Is it for children? Quite a music video. | 0.7591 | 平手 |
| 78 | 見てくれたりとか | You watched it for me and stuff like that. | 0.4400 | You watched it for me and stuff like that. | 0.4400 | 平手 |
| 79 | ライブも来てくれたりします。≫一緒に踊ったりもする？ | You even come to my live shows. ≫Do you dance along too? | 0.7838 | You even come to my live shows. ≫Do you dance along too? | 0.7838 | 平手 |
| 80 | そうですね。≫将来は | Let me see... ≫In the future, | 0.5870 | Let me see... ≫In the future, | 0.5870 | 平手 |
| 81 | パパみたいになりたいみたいな | I think I want to be like Dad. | 0.8175 | I think I want to be like Dad. | 0.8175 | 平手 |
| 82 | 話とかしてるんですか？≫そこはあんまりしてないですね。 | Are you having conversations? ≫ Not really doing that much there. | 0.8434 | Are you having conversations? ≫ Not really doing that much there. | 0.8434 | 平手 |
| 83 | 歌ったり踊ったりするのは好きそうではありますけど | She seems to like singing and dancing, but... | 0.7483 | She seems to like singing and dancing, but... | 0.7483 | 平手 |
| 84 | それをやりたいみたいな感情は今のところまだないですね。 | I don't really feel like doing that right now. | 0.7785 | I don't really feel like doing that right now. | 0.7785 | 平手 |
| 85 | やっぱ俺の子供だなみたいなちょっとダンスすごいなとか | I knew he was my kid - his dancing is pretty amazing, you know? | 0.6354 | I knew he was my kid - his dancing is pretty amazing, you know? | 0.6354 | 平手 |
| 86 | 歌うまいなみたいなところ垣間見えるんですか。 | Can you catch glimpses of her being good at singing? | 0.7876 | Can you catch glimpses of her being good at singing? | 0.7876 | 平手 |
| 87 | この前、学校でみんな集めてライブしたって | The other day, they gathered everyone at school and held a live performance. | 0.6750 | The other day, they gathered everyone at school and held a live performance. | 0.6750 | 平手 |
| 88 | 言ってました。≫ジャイアンじゃん。 | He was saying that. ≫That's Gian, isn't it? | 0.6980 | He was saying that. ≫That's Gian, isn't it? | 0.6980 | 平手 |
| 89 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Nonstop! [Sachiko Kobayashi makes a grand appearance at Niconico Chokaigi ▽ Behind-the-scenes with Daichi Miura, a father of three] | 0.7583 | Nonstop! [Sachiko Kobayashi makes a grand appearance at Niconico Chokaigi ▽ Behind-the-scenes with Daichi Miura, a father of three] | 0.7583 | 平手 |
| 90 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki returns to live performances saying 'I once prepared for death...' ▽ Daichi Miura visits the studio - the true face of a father of three ▽ Masaru Mukai | 0.7978 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki returns to live performances saying 'I once prepared for death...' ▽ Daichi Miura visits the studio - the true face of a father of three ▽ Masaru Mukai | 0.7978 | 平手 |
| 91 | それはＤＮＡがすごいですよ。≫受け継いでるんですね。 | That's amazing DNA. ≫ So you've inherited it, huh? | 0.7782 | That's amazing DNA. ≫ So you've inherited it, huh? | 0.7782 | 平手 |
| 92 | その友達を本当に大切にしなさいって。 | You should really cherish that friend. | 0.8457 | You should really cherish that friend. | 0.8457 | 平手 |
| 93 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Nonstop! [Sachiko Kobayashi makes a grand appearance at Niconico Chokaigi ▽ Behind-the-scenes with Daichi Miura, a father of three] | 0.7583 | Nonstop! [Sachiko Kobayashi makes a grand appearance at Niconico Chokaigi ▽ Behind-the-scenes with Daichi Miura, a father of three] | 0.7583 | 平手 |
| 94 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi▽Isao Sasaki returns to live performances saying 'I once prepared for death...'▽Daichi Miura visits the studio - the real face of a father of three▽Mukai Osamu | 0.8245 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi▽Isao Sasaki returns to live performances saying 'I once prepared for death...'▽Daichi Miura visits the studio - the real face of a father of three▽Mukai Osamu | 0.8245 | 平手 |
| 95 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Nonstop! [Exclusive coverage of Sachiko Kobayashi's appearance at Niconico Chokaigi ▽ Behind-the-scenes look at Daichi Miura as a father of three] | 0.7451 | Nonstop! [Exclusive coverage of Sachiko Kobayashi's appearance at Niconico Chokaigi ▽ Behind-the-scenes look at Daichi Miura as a father of three] | 0.7451 | 平手 |
| 96 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi▽Isao Sasaki's comeback live "I once prepared for death..."▽Daichi Miura visits the studio - the true face of a father of three▽Mukai Osamu | 0.8238 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi▽Isao Sasaki's comeback live "I once prepared for death..."▽Daichi Miura visits the studio - the true face of a father of three▽Mukai Osamu | 0.8238 | 平手 |
| 97 | 子供がゲームしてる時間に一緒にやろうって | Let's play together during the time when the kids are gaming. | 0.8102 | Let's play together during the time when the kids are gaming. | 0.8102 | 平手 |
| 98 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Nonstop! [Exclusive footage of Sachiko Kobayashi appearing at Niconico Chokaigi ▽ Daichi Miura reveals his true self as a father of three] | 0.7193 | Nonstop! [Exclusive footage of Sachiko Kobayashi appearing at Niconico Chokaigi ▽ Daichi Miura reveals his true self as a father of three] | 0.7193 | 平手 |
| 99 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi▽Isao Sasaki returns to live performances saying 'I once prepared for death...'▽Daichi Miura visits the studio - the real face of a father of three▽Mukai Osamu | 0.8245 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi▽Isao Sasaki returns to live performances saying 'I once prepared for death...'▽Daichi Miura visits the studio - the real face of a father of three▽Mukai Osamu | 0.8245 | 平手 |
| 100 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Nonstop! [Exclusive footage of Sachiko Kobayashi appearing at Niconico Chokaigi ▽ Daichi Miura reveals his true self as a father of three] | 0.7193 | Nonstop! [Exclusive footage of Sachiko Kobayashi appearing at Niconico Chokaigi ▽ Daichi Miura reveals his true self as a father of three] | 0.7193 | 平手 |
| 101 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki returns to live performances after 'preparing for death' ▽ Daichi Miura visits the studio - the true face of a father of three ▽ Masaru Mukai | 0.7878 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki returns to live performances after 'preparing for death' ▽ Daichi Miura visits the studio - the true face of a father of three ▽ Masaru Mukai | 0.7878 | 平手 |
| 102 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Nonstop! [Exclusive footage of Sachiko Kobayashi appearing at Niconico Chokaigi ▽ Daichi Miura reveals his true self as a father of three] | 0.7193 | Nonstop! [Exclusive footage of Sachiko Kobayashi appearing at Niconico Chokaigi ▽ Daichi Miura reveals his true self as a father of three] | 0.7193 | 平手 |
| 103 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki returns to live performances saying 'I once prepared for death...' ▽ Daichi Miura visits the studio - the true face of a father of three ▽ Masaru Mukai | 0.7978 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki returns to live performances saying 'I once prepared for death...' ▽ Daichi Miura visits the studio - the true face of a father of three ▽ Masaru Mukai | 0.7978 | 平手 |
| 104 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Nonstop! [Sachiko Kobayashi makes a grand appearance at Niconico Chokaigi ▽ Behind-the-scenes with Daichi Miura, a father of three] | 0.7583 | Nonstop! [Sachiko Kobayashi makes a grand appearance at Niconico Chokaigi ▽ Behind-the-scenes with Daichi Miura, a father of three] | 0.7583 | 平手 |
| 105 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki returns to live performances saying 'I once prepared for death...' ▽ Daichi Miura visits the studio - the true face of a father of three ▽ Masaru Mukai | 0.7978 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki returns to live performances saying 'I once prepared for death...' ▽ Daichi Miura visits the studio - the true face of a father of three ▽ Masaru Mukai | 0.7978 | 平手 |
| 106 | そして来月５月１日に千葉で開催されますが | And it will be held in Chiba on May 1st next month, | 0.8679 | And it will be held in Chiba on May 1st next month, | 0.8679 | 平手 |
| 107 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Nonstop! [Exclusive footage of Sachiko Kobayashi appearing at Niconico Chokaigi ▽ Daichi Miura reveals his true self as a father of three] | 0.7193 | Nonstop! [Exclusive footage of Sachiko Kobayashi appearing at Niconico Chokaigi ▽ Daichi Miura reveals his true self as a father of three] | 0.7193 | 平手 |
| 108 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki returns to live performances after 'preparing for death' ▽ Daichi Miura visits the studio - the real face of a father of three ▽ Masaru Mukai | 0.7894 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki returns to live performances after 'preparing for death' ▽ Daichi Miura visits the studio - the real face of a father of three ▽ Masaru Mukai | 0.7894 | 平手 |
| 109 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Nonstop! [Exclusive footage of Sachiko Kobayashi appearing at Niconico Chokaigi ▽ Daichi Miura reveals his true self as a father of three] | 0.7193 | Nonstop! [Exclusive footage of Sachiko Kobayashi appearing at Niconico Chokaigi ▽ Daichi Miura reveals his true self as a father of three] | 0.7193 | 平手 |
| 110 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki's comeback live performance after 'preparing for death' ▽ Daichi Miura visits the studio - the real face of a father of three ▽ Mukai Osamu | 0.7908 | Sachiko Kobayashi makes a special appearance at Nico Nico Chokaigi ▽ Isao Sasaki's comeback live performance after 'preparing for death' ▽ Daichi Miura visits the studio - the real face of a father of three ▽ Mukai Osamu | 0.7908 | 平手 |
| 111 | スウェットの。カッチカチなるやつね。 | The sweatshirt. The stiff one, you know? | 0.5721 | The sweatshirt. The stiff one, you know? | 0.5721 | 平手 |
| 112 | これ僕小学校の時に経験してるんです。 | I actually experienced this back in elementary school. | 0.8328 | I actually experienced this back in elementary school. | 0.8328 | 平手 |
| 113 | 雪の日に雪合戦、みんなでやりながら | On snowy days, we have snowball fights together while... | 0.7285 | On snowy days, we have snowball fights together while... | 0.7285 | 平手 |
| 114 | 固結びになっちゃって家のトイレに着いたけど | I got so nervous that I had to go to the bathroom at home. | 0.6898 | I got so nervous that I had to go to the bathroom at home. | 0.6898 | 平手 |
| 115 | もう、これが全然…。僕は１０割でしたけど。 | Oh, this is completely... I was 100% sure though. | 0.7487 | Oh, this is completely... I was 100% sure though. | 0.7487 | 平手 |
| 116 | もう２〜３割出た時点で諦めました。 | I gave up when about 20-30% had already come out. | 0.7840 | I gave up when about 20-30% had already come out. | 0.7840 | 平手 |
| 117 | 子供やしね。家やったんでしょ。家やったらまだ…。 | He's just a kid. He was at home, right? If he was at home, then... | 0.6892 | He's just a kid. He was at home, right? If he was at home, then... | 0.6892 | 平手 |
| 118 | 外の６割は…。≫そのあとね、またこのまんまで | About 60% of the outside... ≪And then, it'll stay just like this again. | 0.7095 | About 60% of the outside... ≪And then, it'll stay just like this again. | 0.7095 | 平手 |
| 119 | 乗ってくわけですからね。 | I'll be riding along with you, you see. | 0.6008 | I'll be riding along with you, you see. | 0.6008 | 平手 |
| 120 | あれマジで何とかしてほしいな。 | I really wish someone would do something about that. | 0.6918 | I really wish someone would do something about that. | 0.6918 | 平手 |
| 121 | 携帯のトイレ入れておくべきですね、車の中に。 | We should keep a portable toilet in the car, just in case. | 0.7826 | We should keep a portable toilet in the car, just in case. | 0.7826 | 平手 |
| 122 | 簡単な袋の。 | It's a simple bag. | 0.7883 | It's a simple bag. | 0.7883 | 平手 |
| 123 | 視聴者投票の結果です。 | Here are the results of the viewer vote. | 0.7858 | Here are the results of the viewer vote. | 0.7858 | 平手 |
| 124 | あれー！７７％、何もしない。 | Huh?! 77% and doing nothing. | 0.8795 | Huh?! 77% and doing nothing. | 0.8795 | 平手 |
| 125 | お仕事の人も入ってるかな。≫混むと思ってるから | I wonder if office workers are coming too. ≫ I think it'll be crowded. | 0.7673 | I wonder if office workers are coming too. ≫ I think it'll be crowded. | 0.7673 | 平手 |
| 126 | 行かないって人も多いじゃないですか。 | There are quite a few people who don't go, you know. | 0.7715 | There are quite a few people who don't go, you know. | 0.7715 | 平手 |
| 127 | 意外と混まないかもしれないですよね。 | It might not be as crowded as you'd think. | 0.6355 | It might not be as crowded as you'd think. | 0.6355 | 平手 |
| 128 | いや、混みます。海外に行く人も | No, it'll be crowded. There are also people going overseas. | 0.8248 | No, it'll be crowded. There are also people going overseas. | 0.8248 | 平手 |
| 129 | ちょっといますしね。 | I'll be here for a while. | 0.6529 | I'll be here for a while. | 0.6529 | 平手 |
| 130 | でも、ニュースでディズニーランドとかも | But I saw on the news that places like Disneyland | 0.7260 | But I saw on the news that places like Disneyland | 0.7260 | 平手 |
| 131 | この時間は関東のお天気をお伝えします。 | Now we'll report on the weather in the Kanto region. | 0.7836 | Now we'll report on the weather in the Kanto region. | 0.7836 | 平手 |
| 132 | こちらは現在のお台場の様子です。 | This is the current view of Odaiba. | 0.6761 | This is the current view of Odaiba. | 0.6761 | 平手 |
| 133 | 曇ってますね。≫でも気温は。 | It's cloudy today. ≫ But how about the temperature? | 0.7609 | It's cloudy today. ≫ But how about the temperature? | 0.7609 | 平手 |
| 134 | 気温は２１．７度そして湿度５３％。 | The temperature is 21.7 degrees with 53% humidity. | 0.8725 | The temperature is 21.7 degrees with 53% humidity. | 0.8725 | 平手 |
| 135 | 過ごしやすいですね。 | It's quite pleasant, isn't it? | 0.6092 | It's quite pleasant, isn't it? | 0.6092 | 平手 |
| 136 | やっぱりゴールデンウィークって | As expected, Golden Week is... | 0.3788 | As expected, Golden Week is... | 0.3788 | 平手 |
| 137 | 気温がいいですよね。 | The temperature is nice, isn't it? | 0.8348 | The temperature is nice, isn't it? | 0.8348 | 平手 |
| 138 | テニス日和ですね。≫最高です！ | "Perfect weather for tennis, isn't it?" ≫ "It's absolutely perfect!" | 0.6629 | "Perfect weather for tennis, isn't it?" ≫ "It's absolutely perfect!" | 0.6629 | 平手 |
| 139 | このあとも行きますんでよろしくお願いします。 | I'll be coming later too, so please take care of me. | 0.6021 | I'll be coming later too, so please take care of me. | 0.6021 | 平手 |
| 140 | ではお天気詳しく見ていきましょう。 | Now let's take a detailed look at the weather. | 0.9108 | Now let's take a detailed look at the weather. | 0.9108 | 平手 |
| 141 | まずは北関東です。 | First, we'll head to Northern Kanto. | 0.7886 | First, we'll head to Northern Kanto. | 0.7886 | 平手 |
| 142 | 今は日差しが出ているところも | Right now, there are places where the sun is shining. | 0.6759 | Right now, there are places where the sun is shining. | 0.6759 | 平手 |
| 143 | 厚い雲に覆われます。夜には広く | It will be covered by thick clouds. At night, it will spread widely. | 0.7040 | It will be covered by thick clouds. At night, it will spread widely. | 0.7040 | 平手 |
| 144 | 雨が降り出すでしょう。気温は昨日より少し低く | It will probably start raining. The temperature will be slightly lower than yesterday. | 0.7676 | It will probably start raining. The temperature will be slightly lower than yesterday. | 0.7676 | 平手 |
| 145 | ２３度くらいの予想です。続いて、南関東です。 | The expected temperature is around 23 degrees. Next, we move to southern Kanto. | 0.7477 | The expected temperature is around 23 degrees. Next, we move to southern Kanto. | 0.7477 | 平手 |
| 146 | 今、千葉などで降っている弱い雨はいったんやみますが | The light rain currently falling in Chiba and other areas will stop temporarily, but | 0.6940 | The light rain currently falling in Chiba and other areas will stop temporarily, but | 0.6940 | 平手 |
| 147 | 夕方から再び雨が降り出すでしょう。 | It will start raining again from the evening. | 0.8938 | It will start raining again from the evening. | 0.8938 | 平手 |
| 148 | 夜は本降りになりますよ。 | It's going to rain heavily tonight. | 0.6951 | It's going to rain heavily tonight. | 0.6951 | 平手 |
| 149 | 帰宅時間は横殴りの雨になるかもしれません。 | It might be raining sideways by the time you get home. | 0.7614 | It might be raining sideways by the time you get home. | 0.7614 | 平手 |
| 150 | 気を付けてください。 | Please be careful. | 0.8228 | Please be careful. | 0.8228 | 平手 |
| 151 | 明日の予報です。明日は天気が回復するでしょう。 | Here's tomorrow's forecast. The weather should improve tomorrow. | 0.7852 | Here's tomorrow's forecast. The weather should improve tomorrow. | 0.7852 | 平手 |
| 152 | 日中は各地で晴れて絶好の行楽日和になりそうです。 | During the daytime, it will be sunny across various regions, making perfect weather for outings. | 0.7074 | During the daytime, it will be sunny across various regions, making perfect weather for outings. | 0.7074 | 平手 |
| 153 | 予想最高気温です。 | Here's the forecasted high temperature. | 0.7970 | Here's the forecasted high temperature. | 0.7970 | 平手 |
| 154 | 明日は２２度から２３度ぐらいのところが多いでしょう。 | Tomorrow, temperatures will mostly range between 22 and 23 degrees Celsius. | 0.7754 | Tomorrow, temperatures will mostly range between 22 and 23 degrees Celsius. | 0.7754 | 平手 |
| 155 | 北風が吹いて空気が乾くので | The north wind is blowing and drying out the air, so | 0.8032 | The north wind is blowing and drying out the air, so | 0.8032 | 平手 |
| 156 | 昼間は快適です。こちらのほうが | The daytime is comfortable. This way is better. | 0.7419 | The daytime is comfortable. This way is better. | 0.7419 | 平手 |
| 157 | テニス日和かもしれないですね。≫今日雨なんだ。 | "It might be perfect weather for tennis." ≫ "But it's raining today." | 0.7524 | "It might be perfect weather for tennis." ≫ "But it's raining today." | 0.7524 | 平手 |
| 158 | ねっ、聞いてないです。 | Hey, I didn't hear about that. | 0.8499 | Hey, I didn't hear about that. | 0.8499 | 平手 |
| 159 | 今聞いたじゃん。≫週間予報です。 | You just heard it. ≫It's the weekly forecast. | 0.8306 | You just heard it. ≫It's the weekly forecast. | 0.8306 | 平手 |
| 160 | 水曜日以降も晴れる日が多いでしょう。 | There will likely be many sunny days from Wednesday onward. | 0.8327 | There will likely be many sunny days from Wednesday onward. | 0.8327 | 平手 |
| 161 | ただ、金曜日は雲が広がり雨が降る可能性があります。 | However, on Friday, clouds will spread and there's a chance of rain. | 0.8875 | However, on Friday, clouds will spread and there's a chance of rain. | 0.8875 | 平手 |
| 162 | 気温は晴れる日は２５度ぐらいまで上がって | On sunny days, the temperature rises to about 25 degrees. | 0.8060 | On sunny days, the temperature rises to about 25 degrees. | 0.8060 | 平手 |
| 163 | 夏日になる日もあるでしょう。 | There will probably be some summer-like days. | 0.8151 | There will probably be some summer-like days. | 0.8151 | 平手 |
| 164 | 以上、お天気お伝えしました。 | That's all for the weather report. | 0.5756 | That's all for the weather report. | 0.5756 | 平手 |
| 165 | ここからは今発売中の雑誌「ＥＳＳＥ」から | Next, we'll be featuring content from the currently on-sale magazine "ESSE". | 0.7344 | Next, we'll be featuring content from the currently on-sale magazine "ESSE". | 0.7344 | 平手 |
| 166 | 気になる特集をご紹介します。今回は、こちらです。 | Let me introduce today's featured topic. This time, it's this one. | 0.7595 | Let me introduce today's featured topic. This time, it's this one. | 0.7595 | 平手 |
| 167 | 「プチプラ１００名品」です。 | "100 Petit Prix Premium Picks". | 0.7021 | "100 Petit Prix Premium Picks". | 0.7021 | 平手 |
| 168 | ダイソーのデザインコップは持ち手がなくフックにかけられて | Daiso's design cup doesn't have a handle and can be hung on a hook. | 0.7795 | Daiso's design cup doesn't have a handle and can be hung on a hook. | 0.7795 | 平手 |
| 169 | 省スペースで清潔。 | Space-saving and clean. | 0.9100 | Space-saving and clean. | 0.9100 | 平手 |
| 170 | コップの底に水がたまることもありません。 | Water doesn't even accumulate at the bottom of the cup. | 0.8594 | Water doesn't even accumulate at the bottom of the cup. | 0.8594 | 平手 |
| 171 | セリアのインテリアアイアンウォールバーは | Seria's interior iron wall bar | 0.7748 | Seria's interior iron wall bar | 0.7748 | 平手 |
| 172 | ＤＩＹに最適な万能アイテム。 | The perfect versatile item for DIY projects. | 0.7955 | The perfect versatile item for DIY projects. | 0.7955 | 平手 |
| 173 | インテリアの落下対策やタオル収納などにも使え | You can also use it for preventing interior items from falling and for towel storage. | 0.8425 | You can also use it for preventing interior items from falling and for towel storage. | 0.8425 | 平手 |
| 174 | 値段も１１０円とコスパ最強です。 | It's only 110 yen, so you get the best bang for your buck. | 0.5792 | It's only 110 yen, so you get the best bang for your buck. | 0.5792 | 平手 |
| 175 | 他にも今すぐまねできるアイデアが満載ですよ。 | It's also packed with ideas you can imitate right away. | 0.7327 | It's also packed with ideas you can imitate right away. | 0.7327 | 平手 |
| 176 | ぜひお手に取ってみてください。 | Please feel free to pick it up and try it. | 0.6873 | Please feel free to pick it up and try it. | 0.6873 | 平手 |
| 177 | ただ今、お得な年間定期購読キャンペーン中です。 | We're currently running a special annual subscription campaign. | 0.7773 | We're currently running a special annual subscription campaign. | 0.7773 | 平手 |
| 178 | 新規でお申し込みいただいた方全員に | To all new applicants | 0.8510 | To all new applicants | 0.8510 | 平手 |
| 179 | レジカゴサイズ保冷温ショッピングバッグを | A register/cart-sized insulated shopping bag | 0.6822 | A register/cart-sized insulated shopping bag | 0.6822 | 平手 |
| 180 | プレゼントいたします。２色からお選びいただけます。 | We'll give you a gift. You can choose from two colors. | 0.8936 | We'll give you a gift. You can choose from two colors. | 0.8936 | 平手 |
| 181 | それでは、せきららボイスご紹介します。 | Now then, let me introduce Sekirara Voice. | 0.7665 | Now then, let me introduce Sekirara Voice. | 0.7665 | 平手 |
| 182 | 長野県の方。 | To the person from Nagano Prefecture. | 0.7554 | To the person from Nagano Prefecture. | 0.7554 | 平手 |
| 183 | ゴールデンウィーク初日張り切って | I'm all pumped up for the first day of Golden Week! | 0.5832 | I'm all pumped up for the first day of Golden Week! | 0.5832 | 平手 |
| 184 | 車の掃除をやっていたら | While I was cleaning the car, | 0.7565 | While I was cleaning the car, | 0.7565 | 平手 |
| 185 | 不注意で転んでねんざをしました。 | I wasn't paying attention and fell, spraining my ankle. | 0.5794 | I wasn't paying attention and fell, spraining my ankle. | 0.5794 | 平手 |
| 186 | 医者に行くと骨にひびが入っていて | When I went to the doctor, they told me I had a hairline fracture. | 0.6467 | When I went to the doctor, they told me I had a hairline fracture. | 0.6467 | 平手 |
| 187 | 全治２週間から１か月の診断が。 | The doctor said it'll take two weeks to a month for a full recovery. | 0.6320 | The doctor said it'll take two weeks to a month for a full recovery. | 0.6320 | 平手 |
| 188 | ２７歳、東京都女性の方からです。 | This is from a 27-year-old woman in Tokyo. | 0.8407 | This is from a 27-year-old woman in Tokyo. | 0.8407 | 平手 |
| 189 | 祖母の住む福島の田舎に家族で帰ったことです。 | It's about when our family went back to my grandmother's countryside home in Fukushima. | 0.8045 | It's about when our family went back to my grandmother's countryside home in Fukushima. | 0.8045 | 平手 |
| 190 | 普段はできない川遊びやあまり会えない親戚と | Things we don't usually get to do, like playing in the river, or relatives we rarely see | 0.7437 | Things we don't usually get to do, like playing in the river, or relatives we rarely see | 0.7437 | 平手 |
| 191 | 遊ぶことが楽しみでした。今はみんな大きくなって | I used to look forward to playing together. Now everyone has grown up. | 0.7252 | I used to look forward to playing together. Now everyone has grown up. | 0.7252 | 平手 |
| 192 | 祖母の家に帰る頻度も減ってしまいましたが | I've been visiting my grandmother's house less frequently, but... | 0.7660 | I've been visiting my grandmother's house less frequently, but... | 0.7660 | 平手 |
| 193 | 今年のゴールデンウィークはぜひ会いに行きたいです。 | I really want to meet you during this year's Golden Week. | 0.7566 | I really want to meet you during this year's Golden Week. | 0.7566 | 平手 |
| 194 | いいですね、癒やされますね川遊び。 | That's nice. Playing in the river is so soothing. | 0.7394 | That's nice. Playing in the river is so soothing. | 0.7394 | 平手 |
| 195 | 設楽さんも地元が恋しくなりますか？ | Mr. Shitara, do you ever miss your hometown too? | 0.6206 | Mr. Shitara, do you ever miss your hometown too? | 0.6206 | 平手 |
| 196 | ＦＮＮ　Ｌｉｖｅ　Ｎｅｗｓ　ｄａｙｓ【米ウ首脳が会談…停戦協議どこまで進展？】 | FNN Live News Days: US and Ukraine leaders hold talks... How much progress has been made in ceasefire negotiations? | 0.7272 | FNN Live News Days: US and Ukraine leaders hold talks... How much progress has been made in ceasefire negotiations? | 0.7272 | 平手 |
| 197 | 停戦協議どこまで進展？米ウ首脳会談は「非常に生産的」▽「トランプ関税」対応協議へ…日ベトナム首脳が会談▽待望のパパ１号ホ―ムランは？打撃復調の大谷選手 | How far have the ceasefire talks progressed? US-Ukraine summit described as 'highly productive' ▽ Japan-Vietnam leaders meet to discuss response to 'Trump tariffs' ▽ Will we finally see Ohtani's first home run as a dad? The slugger shows signs of recovery. | 0.7937 | How far have the ceasefire talks progressed? US-Ukraine summit described as 'highly productive' ▽ Japan-Vietnam leaders meet to discuss response to 'Trump tariffs' ▽ Will we finally see Ohtani's first home run as a dad? The slugger shows signs of recovery. | 0.7937 | 平手 |
| 198 | ＞＞こんにちは。 | >>Hello. | 0.8874 | >>Hello. | 0.8874 | 平手 |
| 199 | 女子ゴルフでまたニューヒロインが誕生です。 | A new heroine has emerged in women's golf. | 0.8649 | A new heroine has emerged in women's golf. | 0.8649 | 平手 |
| 200 | ＞＞西郷真央選手が涙の海外メジャー初優勝。 | >> Mao Saigo wins her first overseas major tournament in tears. | 0.7766 | >> Mao Saigo wins her first overseas major tournament in tears. | 0.7766 | 平手 |
| 201 | 日本勢５人目の快挙達成です。 | This marks the fifth Japanese athlete to achieve this remarkable feat. | 0.7377 | This marks the fifth Japanese athlete to achieve this remarkable feat. | 0.7377 | 平手 |
| 202 | 今シーズン最初の海外メジャー大会、 | The first major international competition of this season, | 0.8391 | The first major international competition of this season, | 0.8391 | 平手 |
| 203 | シェブロン選手権に出場した２３歳の西郷真央選手。 | 23-year-old golfer Mao Saigo, who competed in the Chevron Championship. | 0.7461 | 23-year-old golfer Mao Saigo, who competed in the Chevron Championship. | 0.7461 | 平手 |
| 204 | トップと１打差で迎えた最終１８番。 | He entered the final 18th hole just one stroke behind the leader. | 0.6887 | He entered the final 18th hole just one stroke behind the leader. | 0.6887 | 平手 |
| 205 | 西郷選手はバーディーを奪い、 | Player Saigo snatched a birdie, | 0.6549 | Player Saigo snatched a birdie, | 0.6549 | 平手 |
| 206 | 決着は５人によるプレーオフとなります。 | The outcome will be decided by a five-player playoff. | 0.8351 | The outcome will be decided by a five-player playoff. | 0.8351 | 平手 |
| 207 | 西郷選手はプレーオフ最初のホールで、 | Player Saigo, on the first hole of the playoff, | 0.7898 | Player Saigo, on the first hole of the playoff, | 0.7898 | 平手 |
| 208 | ただ一人バーディーを奪い、 | I was the only one who snatched a birdie, | 0.5621 | I was the only one who snatched a birdie, | 0.5621 | 平手 |
| 209 | メジャー大会という大舞台でアメリカツアー初優勝。 | He/She won his/her first victory on the American tour at the major tournament, a grand stage. | 0.8487 | He/She won his/her first victory on the American tour at the major tournament, a grand stage. | 0.8487 | 平手 |
| 210 | 日本勢では史上５人目の快挙となりました。 | This marks the fifth historic achievement for Japanese competitors. | 0.7671 | This marks the fifth historic achievement for Japanese competitors. | 0.7671 | 平手 |
| 211 | 西郷選手は、 | Player Saigo... | 0.6031 | Player Saigo... | 0.6031 | 平手 |
| 212 | 夢にまで見た優勝なので、本当にうれしい。 | I'm so happy because this is the championship I've even dreamed of. | 0.7781 | I'm so happy because this is the championship I've even dreamed of. | 0.7781 | 平手 |
| 213 | 勝ちたい試合で勝てず、 | I couldn't win the match I really wanted to, | 0.7686 | I couldn't win the match I really wanted to, | 0.7686 | 平手 |
| 214 | 悔しい思いをしてきたが、こうやってメジャーで初優勝を挙げるこ | I've had many frustrating experiences, but now I've finally won my first major championship. | 0.6096 | I've had many frustrating experiences, but now I've finally won my first major championship. | 0.6096 | 平手 |
| 215 | とができて、 | I was able to... | 0.5583 | I was able to... | 0.5583 | 平手 |
| 216 | 本当にうれしいとコメントしています。 | They commented that they're truly happy. | 0.7604 | They commented that they're truly happy. | 0.7604 | 平手 |
| 217 | ＞＞ベトナムを訪問中の石破総理大臣は、 | >> Prime Minister Ishiba, who is currently visiting Vietnam, | 0.7803 | >> Prime Minister Ishiba, who is currently visiting Vietnam, | 0.7803 | 平手 |
| 218 | 先ほどからチン首相との首脳会談に臨んでいます。 | I've been attending summit talks with Prime Minister Chin since earlier. | 0.8564 | I've been attending summit talks with Prime Minister Chin since earlier. | 0.8564 | 平手 |
| 219 | では、 | Well then, | 0.8475 | Well then, | 0.8475 | 平手 |
| 220 | 同行している若田部記者の中継です。 | This is reporter Wakata reporting live from the scene. | 0.6387 | This is reporter Wakata reporting live from the scene. | 0.6387 | 平手 |
| 221 | ＞＞アメリカの関税措置を受けて、 | >>In response to the U.S. tariff measures, | 0.8159 | >>In response to the U.S. tariff measures, | 0.8159 | 平手 |
| 222 | 中国がＡＳＥＡＮとの共闘をねらう中、 | As China aims to strengthen cooperation with ASEAN, | 0.6550 | As China aims to strengthen cooperation with ASEAN, | 0.6550 | 平手 |
| 223 | 石破総理はベトナムと経済・安保の両分野で協力を強化し、 | Prime Minister Ishiba strengthened cooperation with Vietnam in both economic and security fields, | 0.8660 | Prime Minister Ishiba strengthened cooperation with Vietnam in both economic and security fields, | 0.8660 | 平手 |
| 224 | 中国との接近にくさびを打ちたい考えです。 | They want to drive a wedge into China's growing closeness. | 0.7453 | They want to drive a wedge into China's growing closeness. | 0.7453 | 平手 |
| 225 | 石破総理はチン首相との会談で、 | Prime Minister Ishiba, during his meeting with Prime Minister Chin, | 0.7982 | Prime Minister Ishiba, during his meeting with Prime Minister Chin, | 0.7982 | 平手 |
| 226 | ベトナムがトランプ政権から４６％の高い税率を突きつけられてい | Vietnam was hit with a high 46% tariff rate by the Trump administration. | 0.7566 | Vietnam was hit with a high 46% tariff rate by the Trump administration. | 0.7566 | 平手 |
| 227 | る関税への対応についても意見交換を行う見通しです。 | They are also expected to exchange opinions regarding measures against tariffs. | 0.7773 | They are also expected to exchange opinions regarding measures against tariffs. | 0.7773 | 平手 |
| 228 | その際に念頭に置くのが習近平国家主席が今月、 | What we need to keep in mind is President Xi Jinping's statement this month, | 0.7017 | What we need to keep in mind is President Xi Jinping's statement this month, | 0.7017 | 平手 |
| 229 | ベトナムを訪問し、 | I visited Vietnam, and | 0.8003 | I visited Vietnam, and | 0.8003 | 平手 |
| 230 | 共同でアメリカの関税に対抗するよう呼びかけた中国の存在です。 | This refers to China's call for joint action against U.S. tariffs. | 0.7553 | This refers to China's call for joint action against U.S. tariffs. | 0.7553 | 平手 |
| 231 | 石破総理は中国の動きに強い懸念を示していて、 | Prime Minister Ishiba has expressed strong concerns about China's actions, | 0.8273 | Prime Minister Ishiba has expressed strong concerns about China's actions, | 0.8273 | 平手 |
| 232 | 会談ではアメリカへの対抗姿勢を抑えつつ、 | During the talks, while toning down their confrontational stance toward the U.S., | 0.8471 | During the talks, while toning down their confrontational stance toward the U.S., | 0.8471 | 平手 |
| 233 | 多角的な自由貿易体制を強化する重要性を確認する見通しです。 | They are expected to reaffirm the importance of strengthening multilateral free trade systems. | 0.8281 | They are expected to reaffirm the importance of strengthening multilateral free trade systems. | 0.8281 | 平手 |
| 234 | またベトナムが中国と海洋問題で対立していることを踏まえ、 | Considering that Vietnam is again in conflict with China over maritime issues, | 0.8425 | Considering that Vietnam is again in conflict with China over maritime issues, | 0.8425 | 平手 |
| 235 | 防衛装備品の供与など安全保障での協力強化も確認する方針で、 | They have also confirmed plans to strengthen security cooperation, including the provision of defense equipment. | 0.8063 | They have also confirmed plans to strengthen security cooperation, including the provision of defense equipment. | 0.8063 | 平手 |
| 236 | このあと記者発表を行います。 | We will hold a press conference shortly. | 0.7157 | We will hold a press conference shortly. | 0.7157 | 平手 |
| 237 | ＞＞アメリカのトランプ大統領は、 | >> U.S. President Trump | 0.8678 | >> U.S. President Trump | 0.8678 | 平手 |
| 238 | ウクライナのゼレンスキー大統領とバチカンでの会談がうまくいっ | Ukrainian President Zelenskyy's meeting at the Vatican went well. | 0.7528 | Ukrainian President Zelenskyy's meeting at the Vatican went well. | 0.7528 | 平手 |
| 239 | たと強調し、 | He/she emphasized that... | 0.6093 | He/she emphasized that... | 0.6093 | 平手 |
| 240 | ロシアのプーチン大統領に攻撃の停止と停戦合意を呼びかけました。 | They called on Russian President Putin to cease attacks and agree to a ceasefire. | 0.8747 | They called on Russian President Putin to cease attacks and agree to a ceasefire. | 0.8747 | 平手 |
| 241 | トランプ氏は２７日、 | On the 27th, Mr. Trump | 0.7303 | On the 27th, Mr. Trump | 0.7303 | 平手 |
| 242 | ゼレンスキー氏との会談を、うまくいった | The meeting with Mr. Zelensky went well. | 0.8501 | The meeting with Mr. Zelensky went well. | 0.8501 | 平手 |
| 243 | よい会談だったと評価しました。 | They evaluated it as a good meeting. | 0.7983 | They evaluated it as a good meeting. | 0.7983 | 平手 |
| 244 | その上で、 | On top of that, | 0.8632 | On top of that, | 0.8632 | 平手 |
| 245 | ロシアに対しては、 | As for Russia, | 0.8987 | As for Russia, | 0.8987 | 平手 |
| 246 | 非常に失望していると不満を示し、 | They expressed their dissatisfaction, saying they were extremely disappointed. | 0.6933 | They expressed their dissatisfaction, saying they were extremely disappointed. | 0.6933 | 平手 |
| 247 | 攻撃の停止と停戦の合意を呼びかけました。 | They called for a cessation of attacks and an agreement to cease fire. | 0.8485 | They called for a cessation of attacks and an agreement to cease fire. | 0.8485 | 平手 |
| 248 | 一方、 | On the other hand, | 0.7544 | On the other hand, | 0.7544 | 平手 |
| 249 | クリミア半島についてトランプ氏は、 | Regarding the Crimean Peninsula, Mr. Trump | 0.8360 | Regarding the Crimean Peninsula, Mr. Trump | 0.8360 | 平手 |
| 250 | ゼレンスキー氏が領有権を放棄するとの認識を示しました。 | President Zelenskyy indicated his recognition that he would relinquish territorial claims. | 0.7560 | President Zelenskyy indicated his recognition that he would relinquish territorial claims. | 0.7560 | 平手 |
| 251 | ＞＞北朝鮮がウクライナへの侵攻を続けるロシアに、 | >>North Korea is providing support to Russia, which continues its invasion of Ukraine, | 0.8256 | >>North Korea is providing support to Russia, which continues its invasion of Ukraine, | 0.8256 | 平手 |
| 252 | 軍を派遣したことを初めて公表しました。 | They publicly announced for the first time that they had deployed troops. | 0.8324 | They publicly announced for the first time that they had deployed troops. | 0.8324 | 平手 |
| 253 | 北朝鮮メディアはきょう、 | North Korean media reported today that | 0.8305 | North Korean media reported today that | 0.8305 | 平手 |
| 254 | ウクライナ軍が越境攻撃を行ってきたロシア西部クルスク州での戦 | The battle in Russia's western Kursk region where Ukrainian forces carried out a cross-border attack | 0.8458 | The battle in Russia's western Kursk region where Ukrainian forces carried out a cross-border attack | 0.8458 | 平手 |
| 255 | 闘に、 | In battle, | 0.8159 | In battle, | 0.8159 | 平手 |
| 256 | 北朝鮮軍が参加したと発表しました。 | They announced that the North Korean military participated. | 0.8867 | They announced that the North Korean military participated. | 0.8867 | 平手 |
| 257 | 北朝鮮がロシアへの派兵を公式に認めたのは初めてです。 | This is the first time North Korea has officially acknowledged sending troops to Russia. | 0.9016 | This is the first time North Korea has officially acknowledged sending troops to Russia. | 0.9016 | 平手 |
| 258 | キム・ジョンウン総書記がロシアと締結した条約に基づき、 | Based on the treaty signed by Chairman Kim Jong-un with Russia, | 0.8566 | Based on the treaty signed by Chairman Kim Jong-un with Russia, | 0.8566 | 平手 |
| 259 | 参戦を決定したとしています。また、 | They have decided to join the battle. Also, | 0.7505 | They have decided to join the battle. Also, | 0.7505 | 平手 |
| 260 | ピョンヤンに近く戦闘慰霊碑が設置されるだろうと伝えていて、 | They reported that a combat memorial monument will likely be erected near Pyongyang, | 0.8573 | They reported that a combat memorial monument will likely be erected near Pyongyang, | 0.8573 | 平手 |
| 261 | 北朝鮮兵士に犠牲者が出たことも明らかにしています。 | They have also revealed that there were casualties among North Korean soldiers. | 0.8420 | They have also revealed that there were casualties among North Korean soldiers. | 0.8420 | 平手 |
| 262 | これに先立ち、 | Prior to this, | 0.6680 | Prior to this, | 0.6680 | 平手 |
| 263 | ロシア軍のゲラシモフ参謀総長は２６日、 | On the 26th, Russian Army Chief of General Staff Gerasimov | 0.8101 | On the 26th, Russian Army Chief of General Staff Gerasimov | 0.8101 | 平手 |
| 264 | 北朝鮮軍が戦闘に参加したことを明らかにしています。 | They have revealed that North Korean forces participated in the battle. | 0.8697 | They have revealed that North Korean forces participated in the battle. | 0.8697 | 平手 |
| 265 | ＞＞栃木県の東北道で乗用車が逆走し３人が死亡した事故で、 | >> In an accident on the Tohoku Expressway in Tochigi Prefecture where a passenger car drove against traffic, three people died. | 0.8845 | >> In an accident on the Tohoku Expressway in Tochigi Prefecture where a passenger car drove against traffic, three people died. | 0.8845 | 平手 |
| 266 | 現場には目立ったブレーキ痕はなく、 | There were no noticeable skid marks at the scene, | 0.8416 | There were no noticeable skid marks at the scene, | 0.8416 | 平手 |
| 267 | 逆走車は速度を落とさず正面衝突した可能性があることが分かりま | It has been found that the wrong-way driver may have collided head-on without reducing speed. | 0.7015 | It has been found that the wrong-way driver may have collided head-on without reducing speed. | 0.7015 | 平手 |
| 268 | した。 | I did it. | 0.7802 | I did it. | 0.7802 | 平手 |
| 269 | おととい夜、 | The night before last, | 0.6450 | The night before last, | 0.6450 | 平手 |
| 270 | 那須塩原市の東北道上りで、 | On the northbound Tohoku Expressway in Nasushiobara City, | 0.8379 | On the northbound Tohoku Expressway in Nasushiobara City, | 0.8379 | 平手 |
| 271 | 乗用車が逆走して当て逃げしたほか、 | A passenger car drove the wrong way and hit-and-ran, and furthermore, | 0.7581 | A passenger car drove the wrong way and hit-and-ran, and furthermore, | 0.7581 | 平手 |
| 272 | さらに車と正面衝突し逆走車を運転していた前原勇太さんと衝突さ | Furthermore, they collided head-on with Yuta Maehara, who was driving the wrong way. | 0.6756 | Furthermore, they collided head-on with Yuta Maehara, who was driving the wrong way. | 0.6756 | 平手 |
| 273 | れた車の平岡勝利さんが死亡しました。 | Mr. Katsutoshi Hiraoka, who was in the car, has died. | 0.7269 | Mr. Katsutoshi Hiraoka, who was in the car, has died. | 0.7269 | 平手 |
| 274 | このほか、 | In addition, | 0.9190 | In addition, | 0.9190 | 平手 |
| 275 | この事故の影響で渋滞中だった車の列にトラックが突っ込み、１人 | Due to this accident, a truck crashed into the line of cars stuck in traffic, killing one person | 0.7893 | Due to this accident, a truck crashed into the line of cars stuck in traffic, killing one person | 0.7893 | 平手 |
| 276 | が死亡しました。 | He/she has passed away. | 0.6548 | He/she has passed away. | 0.6548 | 平手 |
| 277 | 警察のその後の調べで、 | According to the police's subsequent investigation, | 0.9334 | According to the police's subsequent investigation, | 0.9334 | 平手 |
| 278 | 逆走車は追い越し車線で正面衝突したほか、 | The wrong-way driver collided head-on in the passing lane, and | 0.7613 | The wrong-way driver collided head-on in the passing lane, and | 0.7613 | 平手 |
| 279 | 現場に目立ったブレーキ痕がなかったことが分かりました。 | They found no noticeable skid marks at the scene. | 0.7969 | They found no noticeable skid marks at the scene. | 0.7969 | 平手 |
| 280 | 警察は逆走車が速度を落とさず、 | The police reported that the wrong-way driver didn't slow down, | 0.7818 | The police reported that the wrong-way driver didn't slow down, | 0.7818 | 平手 |
| 281 | 乗用車に正面衝突した可能性があると見て、 | They suspect there may have been a head-on collision with a passenger car. | 0.6249 | They suspect there may have been a head-on collision with a passenger car. | 0.6249 | 平手 |
| 282 | 逆走した詳しい経緯を調べています。 | We're investigating the detailed circumstances of how the wrong-way driving occurred. | 0.7137 | We're investigating the detailed circumstances of how the wrong-way driving occurred. | 0.7137 | 平手 |
| 283 | ＞＞宮城県岩沼市の海岸に、 | >> On the coast of Iwanuma City, Miyagi Prefecture, | 0.8805 | >> On the coast of Iwanuma City, Miyagi Prefecture, | 0.8805 | 平手 |
| 284 | 保育士の女性の遺体を遺棄したとして逮捕された男が、 | A man arrested for abandoning the body of a female nursery school teacher | 0.8347 | A man arrested for abandoning the body of a female nursery school teacher | 0.8347 | 平手 |
| 285 | 事件当日、 | On the day of the incident, | 0.8782 | On the day of the incident, | 0.8782 | 平手 |
| 286 | 女性の自宅近くを車で訪れていたことが新たに分かりました。 | It has newly come to light that he had visited near the woman's home by car. | 0.8929 | It has newly come to light that he had visited near the woman's home by car. | 0.8929 | 平手 |
| 287 | ＞＞この事件は今月１３日、 | >> This incident occurred on the 13th of this month, | 0.8984 | >> This incident occurred on the 13th of this month, | 0.8984 | 平手 |
| 288 | 岩沼市の海岸で、 | At the coast of Iwanuma City, | 0.8096 | At the coast of Iwanuma City, | 0.8096 | 平手 |
| 289 | 保育士の行仕由佳さんが胸などを刺されて殺害されているのが見つ | Yuka Gyoshi, a nursery school teacher, was found stabbed to death in the chest. | 0.7339 | Yuka Gyoshi, a nursery school teacher, was found stabbed to death in the chest. | 0.7339 | 平手 |
| 290 | かったもので、警察は、 | Since it was bought, the police... | 0.6079 | Since it was bought, the police... | 0.6079 | 平手 |
| 291 | 知人の佐藤蓮真容疑者２１歳を遺体を遺棄した疑いで逮捕しました。 | The police have arrested 21-year-old suspect Renma Sato, an acquaintance, on suspicion of abandoning a corpse. | 0.7895 | The police have arrested 21-year-old suspect Renma Sato, an acquaintance, on suspicion of abandoning a corpse. | 0.7895 | 平手 |
| 292 | 佐藤容疑者は前日の今月１２日午後７時ごろ、 | Suspect Sato, on the previous day at around 7:00 PM on the 12th of this month, | 0.8629 | Suspect Sato, on the previous day at around 7:00 PM on the 12th of this month, | 0.8629 | 平手 |
| 293 | 行仕さんと複数回電話をしていましたが、 | I had several phone calls with Yukishi-san, but... | 0.8131 | I had several phone calls with Yukishi-san, but... | 0.8131 | 平手 |
| 294 | その後の捜査関係者への取材で、電話をしていた時間帯に、 | According to subsequent interviews with investigation officials, during the time when the phone call was being made, | 0.8412 | According to subsequent interviews with investigation officials, during the time when the phone call was being made, | 0.8412 | 平手 |
| 295 | 佐藤容疑者が行仕さんの自宅近くを車で訪れていたことが新たに分 | It has newly come to light that suspect Sato visited near Yukishi's residence by car. | 0.8567 | It has newly come to light that suspect Sato visited near Yukishi's residence by car. | 0.8567 | 平手 |
| 296 | かりました。 | I borrowed it. | 0.5673 | I borrowed it. | 0.5673 | 平手 |
| 297 | 警察は殺人容疑も視野に事件の詳しい経緯を調べています。 | The police are investigating the details of the incident, keeping murder charges in mind as a possibility. | 0.8427 | The police are investigating the details of the incident, keeping murder charges in mind as a possibility. | 0.8427 | 平手 |
| 298 | ＞＞ミャンマー中部を震源とする大地震から１か月。 | >> It's been one month since the major earthquake struck central Myanmar. | 0.8828 | >> It's been one month since the major earthquake struck central Myanmar. | 0.8828 | 平手 |
| 299 | 被災地では医療体制が追いつかず、 | In the disaster-stricken areas, the medical system couldn't keep up, and | 0.8483 | In the disaster-stricken areas, the medical system couldn't keep up, and | 0.8483 | 平手 |
| 300 | 人々は過酷な生活を強いられています。 | People are forced to live harsh lives. | 0.8915 | People are forced to live harsh lives. | 0.8915 | 平手 |
| 301 | 先月２８日、 | On the 28th of last month, | 0.8019 | On the 28th of last month, | 0.8019 | 平手 |
| 302 | ミャンマーで発生した大地震では、 | In the major earthquake that occurred in Myanmar, | 0.8920 | In the major earthquake that occurred in Myanmar, | 0.8920 | 平手 |
| 303 | 第２の都市マンダレーを中心に大きな被害が出て、 | Major damage occurred centered around Mandalay, the second largest city, and | 0.8803 | Major damage occurred centered around Mandalay, the second largest city, and | 0.8803 | 平手 |
| 304 | 日本人１人を含む３７６９人が死亡、 | 3,769 people died, including one Japanese national. | 0.8892 | 3,769 people died, including one Japanese national. | 0.8892 | 平手 |
| 305 | １０７人が安否不明となっています。 | The safety of 107 people remains unknown. | 0.7883 | The safety of 107 people remains unknown. | 0.7883 | 平手 |
| 306 | 被災地では依然、 | In the disaster-stricken areas, the situation remains... | 0.6474 | In the disaster-stricken areas, the situation remains... | 0.6474 | 平手 |
| 307 | がれきが散乱し、 | Debris was scattered everywhere, | 0.5975 | Debris was scattered everywhere, | 0.5975 | 平手 |
| 308 | 家を失った多くの人たちが路上生活を続けています。 | Many people who lost their homes continue to live on the streets. | 0.8823 | Many people who lost their homes continue to live on the streets. | 0.8823 | 平手 |
| 309 | ＞＞ここが痛いの？ | Does it hurt here? | 0.8333 | Does it hurt here? | 0.8333 | 平手 |
| 310 | ＞＞今月中旬に現地に派遣された日本の医療チームの医師によると、 | According to doctors from the Japanese medical team dispatched to the site earlier this month, | 0.7903 | According to doctors from the Japanese medical team dispatched to the site earlier this month, | 0.7903 | 平手 |
| 311 | 最高気温が４０度を超える過酷な状況の中、 | In the harsh conditions where the maximum temperature exceeds 40 degrees, | 0.8943 | In the harsh conditions where the maximum temperature exceeds 40 degrees, | 0.8943 | 平手 |
| 312 | 医療体制は追いついていないと言います。 | They say the medical system can't keep up. | 0.8659 | They say the medical system can't keep up. | 0.8659 | 平手 |
| 313 | ＞＞けがに伴って、 | >> Due to the injury, | 0.6976 | >> Due to the injury, | 0.6976 | 平手 |
| 314 | 例えば傷をそのままにしていて、 | For example, if you leave a wound untreated, | 0.7638 | For example, if you leave a wound untreated, | 0.7638 | 平手 |
| 315 | そこにばい菌の感染を起こしたりだとか、そういうような方はやは | People who tend to get bacterial infections there, well... | 0.6731 | People who tend to get bacterial infections there, well... | 0.6731 | 平手 |
| 316 | りいらっしゃって。 | Please come in. | 0.4458 | Please come in. | 0.4458 | 平手 |
| 317 | ＞＞実権を握る軍事政権は、 | >> The military regime that holds the real power | 0.7928 | >> The military regime that holds the real power | 0.7928 | 平手 |
| 318 | 対抗する民主派組織などとの戦闘を今月３０日まで一時停止すると | They announced a temporary ceasefire in fighting against opposing democratic organizations until the 30th of this month. | 0.7777 | They announced a temporary ceasefire in fighting against opposing democratic organizations until the 30th of this month. | 0.7777 | 平手 |
| 319 | 発表していますが、 | I'm announcing this, but... | 0.6692 | I'm announcing this, but... | 0.6692 | 平手 |
| 320 | 民主派組織の報道官は停戦は表向きだけだと否定しています。 | The spokesperson for the democratic organization denied that the ceasefire was anything more than superficial. | 0.7273 | The spokesperson for the democratic organization denied that the ceasefire was anything more than superficial. | 0.7273 | 平手 |
| 321 | 戦闘が続く中、 | As the battle continues, | 0.8929 | As the battle continues, | 0.8929 | 平手 |
| 322 | ＞＞メジャーリーグ・ドジャースの大谷翔平選手が、 | >> Shohei Ohtani of the MLB's Los Angeles Dodgers | 0.5784 | >> Shohei Ohtani of the MLB's Los Angeles Dodgers | 0.5784 | 平手 |
| 323 | ２日続けてのマルチヒット。 | He/She got multiple hits for two consecutive days. | 0.7667 | He/She got multiple hits for two consecutive days. | 0.7667 | 平手 |
| 324 | ５月の足音とともにようやく調子が上がってきました。 | I'm finally getting back into my rhythm with the arrival of May. | 0.7472 | I'm finally getting back into my rhythm with the arrival of May. | 0.7472 | 平手 |
| 325 | きのう、 | Yesterday, | 0.8950 | Yesterday, | 0.8950 | 平手 |
| 326 | 父親リスト明け初の３安打と当たりが戻ってきた大谷選手。 | Shohei Ohtani returned to form with his first three-hit game since coming off the paternity list. | 0.7052 | Shohei Ohtani returned to form with his first three-hit game since coming off the paternity list. | 0.7052 | 平手 |
| 327 | 相手バッテリーの警戒も強くなる中、 | While the opposing battery's vigilance intensifies, | 0.8132 | While the opposing battery's vigilance intensifies, | 0.8132 | 平手 |
| 328 | 第１打席では顔すれすれのボールに体をのけぞらせます。 | In his first at-bat, he leans back to avoid a pitch that nearly grazes his face. | 0.6296 | In his first at-bat, he leans back to avoid a pitch that nearly grazes his face. | 0.6296 | 平手 |
| 329 | 大谷選手も思わず声を上げる危険なボールを寸前でかわすと、 | Ohtani barely dodged a dangerous pitch that even made him yell out instinctively, | 0.5854 | Ohtani barely dodged a dangerous pitch that even made him yell out instinctively, | 0.5854 | 平手 |
| 330 | この打席はフォアボールで出塁。 | He reached base on a walk in this at-bat. | 0.5091 | He reached base on a walk in this at-bat. | 0.5091 | 平手 |
| 331 | 続く第２打席は内角のシンカーを捉えると、 | In his second at-bat, he connected with an inside sinker, | 0.6038 | In his second at-bat, he connected with an inside sinker, | 0.6038 | 平手 |
| 332 | 痛烈な打球がライト線へ。 | A scorching line drive heads toward right field. | 0.5574 | A scorching line drive heads toward right field. | 0.5574 | 平手 |
| 333 | ２試合連続ヒットとなるツーベースヒットで出塁します。 | He gets on base with a double, marking his second consecutive game with a hit. | 0.7704 | He gets on base with a double, marking his second consecutive game with a hit. | 0.7704 | 平手 |
| 334 | 第３、 | Third, | 0.8812 | Third, | 0.8812 | 平手 |
| 335 | 第４打席は三振で、 | He struck out in his fourth at-bat. | 0.5473 | He struck out in his fourth at-bat. | 0.5473 | 平手 |
| 336 | 迎えた第５打席。 | He stepped up for his fifth at-bat. | 0.6350 | He stepped up for his fifth at-bat. | 0.6350 | 平手 |
| 337 | 甘く入った変化球を捉え、一、 | He caught the hanging breaking ball and hit a single. | 0.4653 | He caught the hanging breaking ball and hit a single. | 0.4653 | 平手 |
| 338 | 二塁間を破ります。この日は４打数２安打で、 | He breaks through between second base. That day, he went 2 for 4 at bat, | 0.7181 | He breaks through between second base. That day, he went 2 for 4 at bat, | 0.7181 | 平手 |
| 339 | ２日連続のマルチヒット。 | He got multiple hits for two consecutive days. | 0.8012 | He got multiple hits for two consecutive days. | 0.8012 | 平手 |
| 340 | チームも１４安打と、 | The team also had 14 hits, and | 0.9114 | The team also had 14 hits, and | 0.9114 | 平手 |
| 341 | 打線爆発で２連勝です。 | They've won two straight games with explosive batting. | 0.7130 | They've won two straight games with explosive batting. | 0.7130 | 平手 |
| 342 | ＞＞ことしの春の褒章の受章者が発表され、 | >>The recipients of this spring's honors awards have been announced, | 0.8621 | >>The recipients of this spring's honors awards have been announced, | 0.8621 | 平手 |
| 343 | 落語家の柳亭市馬さんらが紫綬褒章に選ばれました。 | Rakugo storyteller Ichiba Ryutei and others were selected to receive the Medal of Honor with Purple Ribbon. | 0.6317 | Rakugo storyteller Ichiba Ryutei and others were selected to receive the Medal of Honor with Purple Ribbon. | 0.6317 | 平手 |
| 344 | ＞＞なんの予兆もなく、 | >>Without any warning, | 0.7972 | >>Without any warning, | 0.7972 | 平手 |
| 345 | 頂いたので、びっくりしてます。 | I'm surprised because I received it. | 0.9352 | I'm surprised because I received it. | 0.9352 | 平手 |
| 346 | 光栄なことだなと。 | I feel truly honored. | 0.6255 | I feel truly honored. | 0.6255 | 平手 |
| 347 | １５歳からもう５５年ぐらいになるのかな。 | It's been about 55 years since I was 15, I guess. | 0.8275 | It's been about 55 years since I was 15, I guess. | 0.8275 | 平手 |
| 348 | この道しかなかったので、 | Since this was the only path available, | 0.7455 | Since this was the only path available, | 0.7455 | 平手 |
| 349 | それはそれで、 | That's fine as it is, | 0.5639 | That's fine as it is, | 0.5639 | 平手 |
| 350 | 今思えば、 | Looking back now, | 0.6577 | Looking back now, | 0.6577 | 平手 |
| 351 | よかったのかなというふうに思います。 | I wonder if it was really okay. | 0.6602 | I wonder if it was really okay. | 0.6602 | 平手 |
| 352 | ＞＞自分はただ好きなことやってきただけで、 | >>I've just been doing what I love, | 0.8721 | >>I've just been doing what I love, | 0.8721 | 平手 |
| 353 | なんにも褒められるようなことはしてないんだけども、 | I haven't done anything particularly praiseworthy, but... | 0.7574 | I haven't done anything particularly praiseworthy, but... | 0.7574 | 平手 |
| 354 | それでこんな栄誉まで頂いていいかしらってね。 | I wonder if I'm really worthy of receiving such an honor. | 0.7093 | I wonder if I'm really worthy of receiving such an honor. | 0.7093 | 平手 |
| 355 | うれしいのと、 | I'm happy and, | 0.8379 | I'm happy and, | 0.8379 | 平手 |
| 356 | 恐縮するのと、本当、 | I'm terribly sorry, and honestly, | 0.8294 | I'm terribly sorry, and honestly, | 0.8294 | 平手 |
| 357 | もうごっちゃごちゃです。 | It's already all mixed up. | 0.5583 | It's already all mixed up. | 0.5583 | 平手 |
| 358 | ＞＞ことしの春の褒章は６０７人と２２の団体が選ばれました。 | >> This spring's honors were awarded to 607 individuals and 22 organizations. | 0.7794 | >> This spring's honors were awarded to 607 individuals and 22 organizations. | 0.7794 | 平手 |
| 359 | ＞＞日経平均株価が一時３００円以上値を上げました。 | >>The Nikkei average temporarily rose by more than 300 yen. | 0.8795 | >>The Nikkei average temporarily rose by more than 300 yen. | 0.8795 | 平手 |
| 360 | 週明けの東京株式市場はいわゆるトランプ関税への警戒感の後退か | At the start of the week, the Tokyo stock market saw a retreat in concerns over the so-called Trump tariffs. | 0.7018 | At the start of the week, the Tokyo stock market saw a retreat in concerns over the so-called Trump tariffs. | 0.7018 | 平手 |
| 361 | ら、 | Well, | 0.5911 | Well, | 0.5911 | 平手 |
| 362 | 先週末のアメリカ市場で主な指数がそろって上昇した流れを受け、 | Following the trend where major indices collectively rose in the U.S. market last weekend, | 0.8668 | Following the trend where major indices collectively rose in the U.S. market last weekend, | 0.8668 | 平手 |
| 363 | 買い注文が広がりました。平均株価は、 | Buy orders have increased. The average stock price... | 0.8272 | Buy orders have increased. The average stock price... | 0.8272 | 平手 |
| 364 | 先週から４営業日連続の上昇で、 | It has been rising for four consecutive business days since last week, | 0.9120 | It has been rising for four consecutive business days since last week, | 0.9120 | 平手 |
| 365 | 一時３万６０００円台を回復しています。 | It temporarily recovered to the 36,000 yen range. | 0.7289 | It temporarily recovered to the 36,000 yen range. | 0.7289 | 平手 |
| 366 | 午前の終値と現在の円相場の値はご覧のとおりです。 | As you can see, here are the morning closing rate and the current yen exchange rate. | 0.8075 | As you can see, here are the morning closing rate and the current yen exchange rate. | 0.8075 | 平手 |
| 367 | ＞＞速報です。 | >> Breaking news. | 0.8277 | >> Breaking news. | 0.8277 | 平手 |
| 368 | 川崎市の解体工事現場できょう午前、 | This morning at a demolition site in Kawasaki City, | 0.8061 | This morning at a demolition site in Kawasaki City, | 0.8061 | 平手 |
| 369 | 作業中に鉄骨が落下し、 | During the work, a steel beam fell and | 0.8296 | During the work, a steel beam fell and | 0.8296 | 平手 |
| 370 | 下にいた作業員５人がけがをしました。 | Five workers below were injured. | 0.8925 | Five workers below were injured. | 0.8925 | 平手 |
| 371 | 午前９時４５分ごろ、 | At around 9:45 AM, | 0.8653 | At around 9:45 AM, | 0.8653 | 平手 |
| 372 | 川崎市川崎区東扇島の建物の解体工事現場で、 | At the demolition site of a building in Higashi-Ogishima, Kawasaki Ward, Kawasaki City, | 0.8605 | At the demolition site of a building in Higashi-Ogishima, Kawasaki Ward, Kawasaki City, | 0.8605 | 平手 |
| 373 | 作業中に物が落ちてきたと１１９番通報がありました。 | There was a 119 emergency call reporting that an object fell during work. | 0.8064 | There was a 119 emergency call reporting that an object fell during work. | 0.8064 | 平手 |
| 374 | 警察と消防によりますと、 | According to the police and fire department, | 0.8906 | According to the police and fire department, | 0.8906 | 平手 |
| 375 | 解体作業中に上から鉄骨が落下して少なくとも５人がけがをしたと | During demolition work, steel beams fell from above, injuring at least five people. | 0.8435 | During demolition work, steel beams fell from above, injuring at least five people. | 0.8435 | 平手 |
| 376 | いうことです。 | That's what I mean. | 0.7388 | That's what I mean. | 0.7388 | 平手 |
| 377 | これまでに救急車や消防車両が１３台出動していて、 | So far, 13 emergency vehicles including ambulances and fire trucks have been dispatched, | 0.8699 | So far, 13 emergency vehicles including ambulances and fire trucks have been dispatched, | 0.8699 | 平手 |
| 378 | 警察などが事故の状況を詳しく調べています。 | The police and others are investigating the details of the accident. | 0.8539 | The police and others are investigating the details of the accident. | 0.8539 | 平手 |
| 379 | ＞＞工事現場から銅線を盗んだとして、 | >> He/She was arrested for stealing copper wires from a construction site, | 0.8339 | >> He/She was arrested for stealing copper wires from a construction site, | 0.8339 | 平手 |
| 380 | チーム忍者と名乗るグループのリーダーらが警視庁に逮捕されまし | The leaders of a group calling themselves 'Team Ninja' were arrested by the Tokyo Metropolitan Police Department. | 0.7358 | The leaders of a group calling themselves 'Team Ninja' were arrested by the Tokyo Metropolitan Police Department. | 0.7358 | 平手 |
| 381 | た。 | It was. | 0.7534 | It was. | 0.7534 | 平手 |
| 382 | 飯島史也容疑者ら２人はことし１月、 | Suspects Fumiya Iijima and one other person allegedly in January this year, | 0.7335 | Suspects Fumiya Iijima and one other person allegedly in January this year, | 0.7335 | 平手 |
| 383 | 足立区の新築マンションの建設現場に忍び込み、２６万円相当の銅 | They sneaked into a construction site of a new condominium in Adachi Ward and stole copper worth 260,000 yen. | 0.7417 | They sneaked into a construction site of a new condominium in Adachi Ward and stole copper worth 260,000 yen. | 0.7417 | 平手 |
| 384 | 線を盗んだ疑いが持たれています。 | He/She is suspected of stealing the wire. | 0.7758 | He/She is suspected of stealing the wire. | 0.7758 | 平手 |
| 385 | 飯島容疑者らは、 | Suspect Iijima and others | 0.5503 | Suspect Iijima and others | 0.5503 | 平手 |
| 386 | 盗んだ銅線をその日のうちに買い取り業者に持ち込み、 | They took the stolen copper wires to a scrap dealer that same day, | 0.8482 | They took the stolen copper wires to a scrap dealer that same day, | 0.8482 | 平手 |
| 387 | 売りさばいていたということです。 | They were selling them off. | 0.6825 | They were selling them off. | 0.6825 | 平手 |
| 388 | 飯島容疑者はチーム忍者と称した地元のグループのリーダーと見ら | Suspect Iijima is believed to be the leader of a local group calling themselves Team Ninja. | 0.8047 | Suspect Iijima is believed to be the leader of a local group calling themselves Team Ninja. | 0.8047 | 平手 |
| 389 | れ、 | Um... | 0.5226 | Um... | 0.5226 | 平手 |
| 390 | 警視庁はこのグループが新築の建設現場を狙い、 | The Metropolitan Police Department believes this group has been targeting new construction sites, | 0.7788 | The Metropolitan Police Department believes this group has been targeting new construction sites, | 0.7788 | 平手 |
| 391 | ほかにも１００件ほど、 | There are about 100 other cases, | 0.8153 | There are about 100 other cases, | 0.8153 | 平手 |
| 392 | 帰宅時間は広く傘の出番となりそうです。 | It looks like umbrellas will be widely needed during the evening commute. | 0.6449 | It looks like umbrellas will be widely needed during the evening commute. | 0.6449 | 平手 |
| 393 | 現在の都心上空はどんよりとした曇り空ですね。 | The sky over the city center is quite overcast right now. | 0.8156 | The sky over the city center is quite overcast right now. | 0.8156 | 平手 |
| 394 | 関東ではすでに雨雲のかかっている所があります。 | In the Kanto region, there are already some areas covered by rain clouds. | 0.7950 | In the Kanto region, there are already some areas covered by rain clouds. | 0.7950 | 平手 |
| 395 | また南風も強まってきました。では予報を見ていきます。 | The southerly winds have also strengthened. Now, let's take a look at the forecast. | 0.8993 | The southerly winds have also strengthened. Now, let's take a look at the forecast. | 0.8993 | 平手 |
| 396 | まずは北関東。 | First, let's head to Northern Kanto. | 0.7686 | First, let's head to Northern Kanto. | 0.7686 | 平手 |
| 397 | 今は日ざしの出ている所も、夜は雨雲が広がります。 | Even places that are sunny now will have rain clouds spreading at night. | 0.8356 | Even places that are sunny now will have rain clouds spreading at night. | 0.8356 | 平手 |
| 398 | 気温は２３度くらいです。 | The temperature is about 23 degrees Celsius. | 0.8675 | The temperature is about 23 degrees Celsius. | 0.8675 | 平手 |
| 399 | 続いて南関東。今、 | Next is southern Kanto. Right now, | 0.8263 | Next is southern Kanto. Right now, | 0.8263 | 平手 |
| 400 | 雨の所も午後はいったんやみますが、夕方以降は広く雨。 | The rain will temporarily stop in the afternoon in rainy areas, but it will rain widely again from evening onward. | 0.8226 | The rain will temporarily stop in the afternoon in rainy areas, but it will rain widely again from evening onward. | 0.8226 | 平手 |
| 401 | 沿岸部は横殴りとなるかもしれません。 | Coastal areas may experience strong sideways winds. | 0.6535 | Coastal areas may experience strong sideways winds. | 0.6535 | 平手 |
| 402 | そしてあすは、天気が回復します。 | And tomorrow, the weather will improve. | 0.7331 | And tomorrow, the weather will improve. | 0.7331 | 平手 |
| 403 | 千葉や茨城の雨も明け方までで、 | The rain in Chiba and Ibaraki will also continue until dawn, | 0.8053 | The rain in Chiba and Ibaraki will also continue until dawn, | 0.8053 | 平手 |
| 404 | 日中は絶好の行楽日和になりそうです。 | It looks like we'll have perfect weather for outings during the day. | 0.6778 | It looks like we'll have perfect weather for outings during the day. | 0.6778 | 平手 |
| 405 | あすの最高気温は２３度前後ですね。 | Tomorrow's high temperature will be around 23 degrees Celsius. | 0.8377 | Tomorrow's high temperature will be around 23 degrees Celsius. | 0.8377 | 平手 |
| 406 | 東京は夏日に迫る陽気ですが、 | Tokyo is experiencing summer-like weather, | 0.8453 | Tokyo is experiencing summer-like weather, | 0.8453 | 平手 |
| 407 | からっとした北風が吹いて快適となりそうです。 | The crisp north wind is blowing, so it should feel quite comfortable. | 0.7939 | The crisp north wind is blowing, so it should feel quite comfortable. | 0.7939 | 平手 |
| 408 | では、最後に週間予報です。 | Now, finally, here's the weekly forecast. | 0.8654 | Now, finally, here's the weekly forecast. | 0.8654 | 平手 |
| 409 | あさって以降も晴れる日が多いでしょう。 | There will likely be many sunny days starting the day after tomorrow. | 0.7150 | There will likely be many sunny days starting the day after tomorrow. | 0.7150 | 平手 |
| 410 | 気温は２５度くらいまで上がる日がほとんどです。 | The temperature will mostly rise to around 25 degrees. | 0.8182 | The temperature will mostly rise to around 25 degrees. | 0.8182 | 平手 |
| 411 | 晴れる日は日ざしが暑いと感じるそうです。 | I heard that on sunny days, the sunlight feels hot. | 0.7851 | I heard that on sunny days, the sunlight feels hot. | 0.7851 | 平手 |
| 412 | 以上、お天気でした。 | That's all for the weather report. | 0.4356 | That's all for the weather report. | 0.4356 | 平手 |
| 413 | ＞＞ではラストニュースです。 | >> And now for our final news story. | 0.7407 | >> And now for our final news story. | 0.7407 | 平手 |
| 414 | あすは昭和１００年の昭和の日ですが、 | Tomorrow is Showa Day marking the 100th year of the Showa era, | 0.7866 | Tomorrow is Showa Day marking the 100th year of the Showa era, | 0.7866 | 平手 |
| 415 | 同じく、 | Likewise, | 0.9171 | Likewise, | 0.9171 | 平手 |
| 416 | ことし１００歳を迎えるレトロな電車があります。 | There's a vintage train that's turning 100 years old this year. | 0.8458 | There's a vintage train that's turning 100 years old this year. | 0.8458 | 平手 |
| 417 | 東京・世田谷区の三軒茶屋と下高井戸を結ぶ東急世田谷線。 | The Tokyu Setagaya Line connects Sangenjaya and Shimo-Takaido in Setagaya Ward, Tokyo. | 0.8765 | The Tokyu Setagaya Line connects Sangenjaya and Shimo-Takaido in Setagaya Ward, Tokyo. | 0.8765 | 平手 |
| 418 | 特徴は２両編成で世田谷の街並みを走るそのレトロな姿。 | Its distinctive feature is its retro appearance as the two-car train runs through the streets of Setagaya. | 0.7902 | Its distinctive feature is its retro appearance as the two-car train runs through the streets of Setagaya. | 0.7902 | 平手 |
| 419 | 道路を横断するこんなシーンも。 | You'll also see scenes like this of people crossing the road. | 0.7561 | You'll also see scenes like this of people crossing the road. | 0.7561 | 平手 |
| 420 | ＞＞おっ、 | >> Oh! | 0.7650 | >> Oh! | 0.7650 | 平手 |
| 421 | すごい。 | Wow. | 0.4874 | Wow. | 0.4874 | 平手 |
| 422 | ＞＞これも世田谷線の名物風景なんです。 | >> This is another famous sight along the Setagaya Line. | 0.8234 | >> This is another famous sight along the Setagaya Line. | 0.8234 | 平手 |
| 423 | ＞＞とにかく、 | >> Anyway, | 0.8348 | >> Anyway, | 0.8348 | 平手 |
| 424 | 孫との思い出のある電車です。 | This is the train that holds memories with my grandchild. | 0.8208 | This is the train that holds memories with my grandchild. | 0.8208 | 平手 |
| 425 | ＞＞街なかとかを走ってて、 | >> When I'm running through town and... | 0.7810 | >> When I'm running through town and... | 0.7810 | 平手 |
| 426 | 親しみやすいかな。 | I wonder if I come across as approachable. | 0.4794 | I wonder if I come across as approachable. | 0.4794 | 平手 |
| 427 | ＞＞世田谷線の歴史は古く、 | >> The Setagaya Line has a long history, | 0.8618 | >> The Setagaya Line has a long history, | 0.8618 | 平手 |
| 428 | １９２５年に玉電の一部として開通。 | It opened in 1925 as part of the Tamaden line. | 0.7535 | It opened in 1925 as part of the Tamaden line. | 0.7535 | 平手 |
| 429 | 来月１日に全線開通１００周年を迎えます。 | The entire line will celebrate its 100th anniversary of full operation on the 1st of next month. | 0.7958 | The entire line will celebrate its 100th anniversary of full operation on the 1st of next month. | 0.7958 | 平手 |
| 430 | それを記念して、 | To commemorate that, | 0.8597 | To commemorate that, | 0.8597 | 平手 |
| 431 | あすからはこちらの特製ヘッドマークをつけた車両が登場。 | Starting tomorrow, trains with these special headmarks will make their appearance. | 0.7500 | Starting tomorrow, trains with these special headmarks will make their appearance. | 0.7500 | 平手 |
| 432 | １００歳をお祝いします。 | We celebrate your 100th birthday. | 0.8209 | We celebrate your 100th birthday. | 0.8209 | 平手 |
| 433 | ＞＞１００歳おめでとうございます。 | >> Congratulations on turning 100 years old! | 0.8667 | >> Congratulations on turning 100 years old! | 0.8667 | 平手 |
| 434 | ＞＞非常に魅力ある商店街が各所に点在してございまして、 | >> There are many highly attractive shopping districts scattered throughout the area, | 0.8622 | >> There are many highly attractive shopping districts scattered throughout the area, | 0.8622 | 平手 |
| 435 | そういった所の皆様と一緒になって、 | Working together with everyone at those places, | 0.7507 | Working together with everyone at those places, | 0.7507 | 平手 |
| 436 | この世田谷線沿線を盛り上げているところでございます。 | We are currently working to liven up the areas along the Setagaya Line. | 0.6177 | We are currently working to liven up the areas along the Setagaya Line. | 0.6177 | 平手 |
| 437 | ＞＞その世田谷線の車両は１０種類のデザインがあるんですが、 | >> Actually, there are 10 different designs for those Setagaya Line trains, | 0.8391 | >> Actually, there are 10 different designs for those Setagaya Line trains, | 0.8391 | 平手 |
| 438 | 特に人気なのが、 | What's especially popular is | 0.9404 | What's especially popular is | 0.9404 | 平手 |
| 439 | こちらの幸福の招き猫電車。 | This is the Lucky Beckoning Cat train. | 0.7207 | This is the Lucky Beckoning Cat train. | 0.7207 | 平手 |
| 440 | ＞＞かわいい。 | >> She's cute. | 0.8635 | >> She's cute. | 0.8635 | 平手 |
| 441 | ＞＞かわいい。 | >> She's cute. | 0.8635 | >> She's cute. | 0.8635 | 平手 |
| 442 | つり革は招き猫。 | The strap handle is shaped like a beckoning cat. | 0.4487 | The strap handle is shaped like a beckoning cat. | 0.4487 | 平手 |
| 443 | 車両と車両をつなぐ連結部分は首輪となっています。 | The coupling part that connects the vehicles acts as a collar. | 0.7592 | The coupling part that connects the vehicles acts as a collar. | 0.7592 | 平手 |
| 444 | ぽかぽか【プロ野球界の全てを知る古田敦也が秘話告白ＳＰ！妻・中井美穂語る素顔】 | Poka Poka [Special Edition: Atsuya Furuta Reveals Untold Stories About Japanese Professional Baseball! His Wife Miho Nakai Shares His True Self] | 0.8356 | Poka Poka [Special Edition: Atsuya Furuta Reveals Untold Stories About Japanese Professional Baseball! His Wife Miho Nakai Shares His True Self] | 0.8356 | 平手 |
| 445 | イチロ―＆松井秀喜＆藤川球児レジェンド選手の凄すぎ秘話▽野村監督の“愛のムチ″＆激動ストライキの真相激白▽妻・中井美穂との特殊な夫婦関係▽ドクタ―岡本の健康診断 | Amazing untold stories of legendary players Ichiro, Hideki Matsui & Kyuji Fujikawa ▽ The truth behind Manager Nomura's 'tough love' & the turbulent strike ▽ The unique marital relationship with wife Miho Nakai ▽ Dr. Okamoto's health checkup | 0.8670 | Amazing untold stories of legendary players Ichiro, Hideki Matsui & Kyuji Fujikawa ▽ The truth behind Manager Nomura's 'tough love' & the turbulent strike ▽ The unique marital relationship with wife Miho Nakai ▽ Dr. Okamoto's health checkup | 0.8670 | 平手 |
| 446 | そう、そう。振りかぶって。 | Yes, yes. Swing it back. | 0.7555 | Yes, yes. Swing it back. | 0.7555 | 平手 |
| 447 | いいね、いいね！ | Nice, nice! | 0.7713 | Nice, nice! | 0.7713 | 平手 |
| 448 | さあ、始まりました「ぽかぽか」月曜日です！ | Here we go! It's a warm and cozy Monday! | 0.6570 | Here we go! It's a warm and cozy Monday! | 0.6570 | 平手 |
| 449 | 皆さん、今週もよろしくお願いします！ | Everyone, let's have another great week together! | 0.6585 | Everyone, let's have another great week together! | 0.6585 | 平手 |
| 450 | ゴールデンウィーク。 | Golden Week. | 0.6380 | Golden Week. | 0.6380 | 平手 |
| 451 | それで来てる人もいるんだ。≫一応最中 | Some people actually come because of that. >> It's still ongoing, by the way. | 0.6657 | Some people actually come because of that. >> It's still ongoing, by the way. | 0.6657 | 平手 |
| 452 | 休みの方もね。今日は働かれている方も | For those who are off today, and also for those who are working. | 0.6855 | For those who are off today, and also for those who are working. | 0.6855 | 平手 |
| 453 | 多いんでしょうけど。 | There must be a lot, right? | 0.6467 | There must be a lot, right? | 0.6467 | 平手 |
| 454 | すごいですね、古田さん…。 | That's amazing, Mr. Furuta... | 0.7726 | That's amazing, Mr. Furuta... | 0.7726 | 平手 |
| 455 | キャッチボールを。羨ましすぎませんか。 | They're playing catch. Aren't you way too jealous? | 0.5751 | They're playing catch. Aren't you way too jealous? | 0.5751 | 平手 |
| 456 | しかも、しゃがんでくれた。 | What's more, they even crouched down for me. | 0.4996 | What's more, they even crouched down for me. | 0.4996 | 平手 |
| 457 | 古田さんが思わず座るくらいいい球投げてたんでしょうね。 | Mr. Furuta must have been throwing such good pitches that you couldn't help but sit down. | 0.7036 | Mr. Furuta must have been throwing such good pitches that you couldn't help but sit down. | 0.7036 | 平手 |
| 458 | 昼太郎できるんだねああいうこと。 | So you can do that kind of thing during the day, huh? | 0.4271 | So you can do that kind of thing during the day, huh? | 0.4271 | 平手 |
| 459 | うまかったよね。 | That was delicious, wasn't it? | 0.7009 | That was delicious, wasn't it? | 0.7009 | 平手 |
| 460 | 昼太郎ってミットはめられるんだね。 | So Hitarou can wear mittens, huh? | 0.3929 | So Hitarou can wear mittens, huh? | 0.3929 | 平手 |
| 461 | サイズが合わないかなと思ったら、大丈夫なのね。 | I thought it might not fit, but it's actually okay. | 0.6057 | I thought it might not fit, but it's actually okay. | 0.6057 | 平手 |
| 462 | 本日はプロ野球界の全てを知る男 | Today, we have the man who knows everything about professional baseball. | 0.8047 | Today, we have the man who knows everything about professional baseball. | 0.8047 | 平手 |
| 463 | 古田敦也がイチロー・松井秀喜との秘話から | From Atsuya Furuta's untold stories with Ichiro and Hideki Matsui | 0.7936 | From Atsuya Furuta's untold stories with Ichiro and Hideki Matsui | 0.7936 | 平手 |
| 464 | ストライキの真相まで全部語るＳＰ。 | A special episode revealing the whole truth behind the strike. | 0.5601 | A special episode revealing the whole truth behind the strike. | 0.5601 | 平手 |
| 465 | 出てくる名前もすごい。 | The names that come up are amazing too. | 0.8463 | The names that come up are amazing too. | 0.8463 | 平手 |
| 466 | 神田さんが大好きで緊張しちゃって。 | I'm so nervous because I really like Kanda-san. | 0.6689 | I'm so nervous because I really like Kanda-san. | 0.6689 | 平手 |
| 467 | 私、古田さん中学高校時代… | I went to middle school and high school with Mr. Furuta... | 0.6647 | I went to middle school and high school with Mr. Furuta... | 0.6647 | 平手 |
| 468 | ヤクルトスワローズの…あ、嘘です。 | The Yakult Swallows... oh wait, just kidding. | 0.6488 | The Yakult Swallows... oh wait, just kidding. | 0.6488 | 平手 |
| 469 | 高校時代は入ってません。 | I wasn't in any clubs during high school. | 0.7325 | I wasn't in any clubs during high school. | 0.7325 | 平手 |
| 470 | ファンクラブに入っておりましたのでね | I was a member of the fan club, you see. | 0.7023 | I was a member of the fan club, you see. | 0.7023 | 平手 |
| 471 | 中学時代にね本当に幸せです。 | I was really happy during my junior high school days. | 0.8434 | I was really happy during my junior high school days. | 0.8434 | 平手 |
| 472 | 良かったです。それでは、まずは | That's good. Well then, first... | 0.7891 | That's good. Well then, first... | 0.7891 | 平手 |
| 473 | 月曜レギュラーの皆さんです。 | Here are our Monday regulars. | 0.6138 | Here are our Monday regulars. | 0.6138 | 平手 |
| 474 | 月曜レギュラー伊集院光さん、横澤夏子さん | Our Monday regulars are Mr. Mitsunori Ijuin and Ms. Natsuko Yokozawa. | 0.6777 | Our Monday regulars are Mr. Mitsunori Ijuin and Ms. Natsuko Yokozawa. | 0.6777 | 平手 |
| 475 | Ｔｒａｖｉｓ　Ｊａｐａｎ松田元太君！ | Travis Japan's Genta Matsuda! | 0.8085 | Travis Japan's Genta Matsuda! | 0.8085 | 平手 |
| 476 | 月曜アナウンサー、松崎さん！ | Monday's announcer, Mr. Matsuzaki! | 0.8552 | Monday's announcer, Mr. Matsuzaki! | 0.8552 | 平手 |
| 477 | 更にまんぷく昼太郎！ | And now, the completely satisfied Hirutaro! | 0.4602 | And now, the completely satisfied Hirutaro! | 0.4602 | 平手 |
| 478 | 伊集院さん、どうですか？昼太郎の。 | Mr. Ijuin, what do you think? About Hirutaro. | 0.6183 | Mr. Ijuin, what do you think? About Hirutaro. | 0.6183 | 平手 |
| 479 | 昼太郎、すげーんだな！ | Hirutaro, you're amazing! | 0.6697 | Hirutaro, you're amazing! | 0.6697 | 平手 |
| 480 | あの距離と、緊張があるからとんでもないことになってるよ | With that distance and tension between us, things are getting completely out of hand. | 0.6124 | With that distance and tension between us, things are getting completely out of hand. | 0.6124 | 平手 |
| 481 | 生放送。 | Live broadcast. | 0.9242 | Live broadcast. | 0.9242 | 平手 |
| 482 | 中途半端な距離だから難しいんですよね。 | It's difficult because the distance is neither here nor there. | 0.7236 | It's difficult because the distance is neither here nor there. | 0.7236 | 平手 |
| 483 | やってたんか？≫それは謎？ | Were you doing that? ≫ That's a mystery? | 0.9373 | Were you doing that? ≫ That's a mystery? | 0.9373 | 平手 |
| 484 | ガチャピン方式だからね。 | That's the Gachapin method for you. | 0.6217 | That's the Gachapin method for you. | 0.6217 | 平手 |
| 485 | 方式とかじゃない。方式もくそもないから！ | It's not about methods or anything. Screw methods! | 0.8082 | It's not about methods or anything. Screw methods! | 0.8082 | 平手 |
| 486 | ピアノとか弾こうと思えば弾けるから。 | I can play piano and stuff if I want to. | 0.7675 | I can play piano and stuff if I want to. | 0.7675 | 平手 |
| 487 | 別に、あれ方式とかないから。ガチャピンが | It's not like there's any particular method or anything. Gachapin is... | 0.7016 | It's not like there's any particular method or anything. Gachapin is... | 0.7016 | 平手 |
| 488 | 全部できるだけだから。 | I'll do everything I can. | 0.5627 | I'll do everything I can. | 0.5627 | 平手 |
| 489 | 本日のゲスト、こちらの方です！ | Here's today's guest! | 0.9148 | Here's today's guest! | 0.9148 | 平手 |
| 490 | 古田敦也さんです！ＴＪ？ | It's Atsuya Furuta! TJ? | 0.7897 | It's Atsuya Furuta! TJ? | 0.7897 | 平手 |
| 491 | ＴＪ！ありがとうございます！ | TJ! Thank you very much! | 0.9209 | TJ! Thank you very much! | 0.9209 | 平手 |
| 492 | 古田さん、ＴＪご存じ？≫今見ました。 | Mr. Furuta, do you know TJ? ≫ I just saw it. | 0.8066 | Mr. Furuta, do you know TJ? ≫ I just saw it. | 0.8066 | 平手 |
| 493 | よろしくお願いいたします。ありがとうございます。 | Thank you very much. I appreciate your help. | 0.7418 | Thank you very much. I appreciate your help. | 0.7418 | 平手 |
| 494 | 古田さん、生放送のバラエティーって | Mr. Furuta, about live variety shows... | 0.6748 | Mr. Furuta, about live variety shows... | 0.6748 | 平手 |
| 495 | あんまりないですよね。≫あんまり出る機会…。 | There aren't many, right? ≫Not many opportunities to appear... | 0.8502 | There aren't many, right? ≫Not many opportunities to appear... | 0.8502 | 平手 |
| 496 | すごいね。すごい人いるね。≫ＴＪ。 | That's amazing. There are some incredible people out there. ≫TJ. | 0.7949 | That's amazing. There are some incredible people out there. ≫TJ. | 0.7949 | 平手 |
| 497 | ありがとうございます。 | Thank you very much. | 0.7402 | Thank you very much. | 0.7402 | 平手 |
| 498 | ちょっとだけやり方間違ってますんで。 | You're doing it slightly wrong. | 0.6973 | You're doing it slightly wrong. | 0.6973 | 平手 |
| 499 | いやいや、何でも。≫Ｊです。 | No no, it's nothing. >> It's J. | 0.6989 | No no, it's nothing. >> It's J. | 0.6989 | 平手 |
| 500 | スポーツバラエティーはあったとしても…。 | Even if there were sports variety shows... | 0.8380 | Even if there were sports variety shows... | 0.8380 | 平手 |
| 501 | なかなか出る機会ないですね。何か岩井さん、昼 | We don't get many chances to go out, do we? Say, Iwai-san, about lunch... | 0.6558 | We don't get many chances to go out, do we? Say, Iwai-san, about lunch... | 0.6558 | 平手 |
| 502 | 似合わないですね。≫よく気づきましたね。 | "It doesn't suit you." ≫ "You noticed that quickly." | 0.6326 | "It doesn't suit you." ≫ "You noticed that quickly." | 0.6326 | 平手 |
| 503 | 澤部さんは似合うけど | It looks good on Sawabe-san, but... | 0.4367 | It looks good on Sawabe-san, but... | 0.4367 | 平手 |
| 504 | 大丈夫ですか？≫僕が一番思います。 | Are you okay? ≫ I'm the one who's most concerned. | 0.8007 | Are you okay? ≫ I'm the one who's most concerned. | 0.8007 | 平手 |
| 505 | この時間で気づくとは。さすがＩＤ野球。 | You noticed at this hour? That's ID Baseball for you. | 0.6935 | You noticed at this hour? That's ID Baseball for you. | 0.6935 | 平手 |
| 506 | 第１回目から思ってたんです。≫ごまかしごまかし | I've been thinking this since the very first episode. >> Stop dodging the issue! | 0.6537 | I've been thinking this since the very first episode. >> Stop dodging the issue! | 0.6537 | 平手 |
| 507 | やってたんですが。 | I was doing it, but... | 0.7840 | I was doing it, but... | 0.7840 | 平手 |
| 508 | 奥様がご出演くださいまして何か聞きました？ | Did you hear anything when Madam appeared? | 0.7693 | Did you hear anything when Madam appeared? | 0.7693 | 平手 |
| 509 | ファンと言ってくださったって。さっき、オープニングで | They said they're a fan. Just now, during the opening... | 0.7266 | They said they're a fan. Just now, during the opening... | 0.7266 | 平手 |
| 510 | 高校は違いますけどって。 | We went to different high schools, though. | 0.6706 | We went to different high schools, though. | 0.6706 | 平手 |
| 511 | 誰だったのか気になりますけど。 | I wonder who it was. | 0.8727 | I wonder who it was. | 0.8727 | 平手 |
| 512 | この番組はどうとかあるんですか？ | Is there something special about this program? | 0.7775 | Is there something special about this program? | 0.7775 | 平手 |
| 513 | トークが長いって言ってました。≫ゲストとトーク１時間以上は…。 | You said the talk was too long. >> Talking with guests for over an hour... | 0.8590 | You said the talk was too long. >> Talking with guests for over an hour... | 0.8590 | 平手 |
| 514 | 思ったより長いから気を付けてねって言われました。 | They told me to be careful because it's longer than expected. | 0.8692 | They told me to be careful because it's longer than expected. | 0.8692 | 平手 |
| 515 | ゲストにそう感じられてたんですね | So that's how the guest felt about it. | 0.7057 | So that's how the guest felt about it. | 0.7057 | 平手 |
| 516 | 「ぽかぽか」って。≫特に神田さんどういうところが | "Poka poka"... What about Kanda-san in particular? | 0.6532 | "Poka poka"... What about Kanda-san in particular? | 0.6532 | 平手 |
| 517 | お好きなんですか。 | Do you like it? | 0.8754 | Do you like it? | 0.8754 | 平手 |
| 518 | 皆さんそうだと思いますけどまずはビジュアルね。 | I think everyone would agree, but first impressions matter. | 0.6648 | I think everyone would agree, but first impressions matter. | 0.6648 | 平手 |
| 519 | 当時の野球選手ってお尻がすごく大きかったり | Baseball players back then had really big butts, you know. | 0.7691 | Baseball players back then had really big butts, you know. | 0.7691 | 平手 |
| 520 | っていう方が多い中でもう、後ろいいですか？ | Even though most people would say that, is it okay if I take the back? | 0.6533 | Even though most people would say that, is it okay if I take the back? | 0.6533 | 平手 |
| 521 | 向いていただいて。すごくシュッとされてるんです。 | Please face this way. You look very sharp. | 0.6290 | Please face this way. You look very sharp. | 0.6290 | 平手 |
| 522 | 本当にスタイリッシュで。あとは知的な方が | You're really stylish. And intelligent too. | 0.6981 | You're really stylish. And intelligent too. | 0.6981 | 平手 |
| 523 | 私、好きでしたので眼鏡と野村さんの横に常にいるという | Because I liked you, I was always by your side wearing glasses, Nomura-san. | 0.7822 | Because I liked you, I was always by your side wearing glasses, Nomura-san. | 0.7822 | 平手 |
| 524 | この知的さですよね。とても格好良かったです。 | It's this intelligence, right? It was really cool. | 0.8050 | It's this intelligence, right? It was really cool. | 0.8050 | 平手 |
| 525 | あんまりビジュアルは | I'm not really into visuals. | 0.4013 | I'm not really into visuals. | 0.4013 | 平手 |
| 526 | 褒めてもらったことないんですけど。 | No one has ever complimented me before. | 0.6796 | No one has ever complimented me before. | 0.6796 | 平手 |
| 527 | 爽やかなイメージはありますが | You have a refreshing image, but... | 0.5937 | You have a refreshing image, but... | 0.5937 | 平手 |
| 528 | そんな古田さんをお迎えしまして | Now we welcome Mr. Furuta. | 0.5009 | Now we welcome Mr. Furuta. | 0.5009 | 平手 |
| 529 | 今日の「ぽかぽか」まずこちらご覧ください。 | For today's "Pokapoka" segment, first take a look at this. | 0.7284 | For today's "Pokapoka" segment, first take a look at this. | 0.7284 | 平手 |
| 530 | 本日のゲストは野球界のレジェンド古田敦也さん。 | Today's guest is baseball legend Atsuya Furuta. | 0.7637 | Today's guest is baseball legend Atsuya Furuta. | 0.7637 | 平手 |
| 531 | １９９０年ヤクルトスワローズに | In 1990, he joined the Yakult Swallows. | 0.6213 | In 1990, he joined the Yakult Swallows. | 0.6213 | 平手 |
| 532 | ドラフト２位で入団。 | He was drafted second overall. | 0.5767 | He was drafted second overall. | 0.5767 | 平手 |
| 533 | 名将・野村克也監督指導のもと | Under the guidance of the legendary manager Katsuya Nomura | 0.8224 | Under the guidance of the legendary manager Katsuya Nomura | 0.8224 | 平手 |
| 534 | １年目から正捕手に抜擢されると…。 | He got promoted to starting catcher right from his rookie year... | 0.7133 | He got promoted to starting catcher right from his rookie year... | 0.7133 | 平手 |
| 535 | ２年目にはセ・リーグの捕手では初となる | In his second year, he became the first catcher in the Central League to achieve this. | 0.7232 | In his second year, he became the first catcher in the Central League to achieve this. | 0.7232 | 平手 |
| 536 | 首位打者を獲得。 | He won the batting title. | 0.5996 | He won the batting title. | 0.5996 | 平手 |
| 537 | 野村ＩＤ野球の申し子と称されリーグ優勝５回、日本一４回と | He was called the prodigy of Nomura ID Baseball, winning the league championship 5 times and becoming Japan Series champion 4 times. | 0.8117 | He was called the prodigy of Nomura ID Baseball, winning the league championship 5 times and becoming Japan Series champion 4 times. | 0.8117 | 平手 |
| 538 | ヤクルト黄金時代をけん引し | He led Yakult's golden era. | 0.6546 | He led Yakult's golden era. | 0.6546 | 平手 |
| 539 | ２００６年にはプロ野球史上２９年ぶりとなる選手兼任監督に。 | In 2006, he became the first player-manager in professional baseball history in 29 years. | 0.8453 | In 2006, he became the first player-manager in professional baseball history in 29 years. | 0.8453 | 平手 |
| 540 | これまで過去に５人しかいない | There have only been five people so far. | 0.7988 | There have only been five people so far. | 0.7988 | 平手 |
| 541 | 選手、監督日本プロ野球選手会会長の | Player and manager, president of the Japanese Professional Baseball Players Association | 0.8515 | Player and manager, president of the Japanese Professional Baseball Players Association | 0.8515 | 平手 |
| 542 | ３つを経験したまさに球界の全てを知る男！ | The man who's experienced all three and truly knows everything about the baseball world! | 0.8361 | The man who's experienced all three and truly knows everything about the baseball world! | 0.8361 | 平手 |
| 543 | 引退後も１８年の現役生活で培った | Even after retirement, I've cultivated [these skills] during my 18 years as an active player. | 0.6673 | Even after retirement, I've cultivated [these skills] during my 18 years as an active player. | 0.6673 | 平手 |
| 544 | 経験と理論を武器に解説者として活躍。 | He/She thrives as a commentator armed with both experience and theory. | 0.8075 | He/She thrives as a commentator armed with both experience and theory. | 0.8075 | 平手 |
| 545 | 一方、私生活では１９９５年に結婚した | On the other hand, in his/her personal life, he/she got married in 1995. | 0.7589 | On the other hand, in his/her personal life, he/she got married in 1995. | 0.7589 | 平手 |
| 546 | 元フジテレビアナウンサーの中井美穂さんと | With Miho Nakai, former Fuji TV announcer, | 0.8872 | With Miho Nakai, former Fuji TV announcer, | 0.8872 | 平手 |
| 547 | 今年３０周年を迎えます。 | This year marks our 30th anniversary. | 0.8720 | This year marks our 30th anniversary. | 0.8720 | 平手 |
| 548 | 今日は、そんな古田さんに | Today, I'll be talking with Mr. Furuta about that. | 0.5636 | Today, I'll be talking with Mr. Furuta about that. | 0.5636 | 平手 |
| 549 | イチロー、松井秀喜など伝説のプレーヤーとの秘話から | From untold stories about legendary players like Ichiro and Hideki Matsui | 0.8247 | From untold stories about legendary players like Ichiro and Hideki Matsui | 0.8247 | 平手 |
| 550 | プロ野球史上初のストライキの裏側まで | Even behind the scenes of professional baseball's first-ever strike | 0.7620 | Even behind the scenes of professional baseball's first-ever strike | 0.7620 | 平手 |
| 551 | 何でも聞いちゃうぽいぽいトーク、スタートです！ | Let's start our fun, no-holds-barred Q&A session! | 0.5390 | Let's start our fun, no-holds-barred Q&A session! | 0.5390 | 平手 |
| 552 | 改めて、神田さんご覧になってどうですか？ | Now that you've had another look, what do you think of Kanda-san? | 0.6189 | Now that you've had another look, what do you think of Kanda-san? | 0.6189 | 平手 |
| 553 | 思い出しますね〜！本当にあのころ強かったですからね。 | Ah, it brings back memories! We were really strong back then, you know. | 0.7184 | Ah, it brings back memories! We were really strong back then, you know. | 0.7184 | 平手 |
| 554 | 今も頑張ってますけどね。≫すみません。 | I'm still doing my best, you know. ≫ I'm sorry. | 0.7544 | I'm still doing my best, you know. ≫ I'm sorry. | 0.7544 | 平手 |
| 555 | とんでもないこと言ってますよ | You're saying something outrageous. | 0.6610 | You're saying something outrageous. | 0.6610 | 平手 |
| 556 | 古田さん前にして。≫すいません…。 | (You're) standing in front of Mr. Furuta. ≫I'm sorry... | 0.7176 | (You're) standing in front of Mr. Furuta. ≫I'm sorry... | 0.7176 | 平手 |
| 557 | 伊集院さん１年目で正捕手になって | Mr. Ijuin became the starting catcher in his first year. | 0.6329 | Mr. Ijuin became the starting catcher in his first year. | 0.6329 | 平手 |
| 558 | ２年目で首位打者とか | Becoming the batting champion in just your second year... | 0.6829 | Becoming the batting champion in just your second year... | 0.6829 | 平手 |
| 559 | あの辺は…。 | That area... | 0.8315 | That area... | 0.8315 | 平手 |
| 560 | あの時スポーツニュースをやらせてもらってたんだけど | I was actually hosting the sports news back then. | 0.8241 | I was actually hosting the sports news back then. | 0.8241 | 平手 |
| 561 | 他の監督からの評価も | I've also received evaluations from other directors. | 0.7641 | I've also received evaluations from other directors. | 0.7641 | 平手 |
| 562 | いっぱい聞いてるから。広島は初めて | I've heard a lot about it. This is my first time in Hiroshima. | 0.6815 | I've heard a lot about it. This is my first time in Hiroshima. | 0.6815 | 平手 |
| 563 | 古田さんがグラウンド立ったの見た時に | When I saw Mr. Furuta standing on the field | 0.7306 | When I saw Mr. Furuta standing on the field | 0.7306 | 平手 |
| 564 | 山本浩二監督がスカウトにお前らどこに | Coach Koji Yamamoto asked the scouts, "Where are you guys?" | 0.5682 | Coach Koji Yamamoto asked the scouts, "Where are you guys?" | 0.5682 | 平手 |
| 565 | 目をつけてんだ！って言って全員説教だったそうです。 | Apparently, he yelled "I've got my eye on you!" and then lectured everyone. | 0.6556 | Apparently, he yelled "I've got my eye on you!" and then lectured everyone. | 0.6556 | 平手 |
| 566 | うちは何でマークしてないんだっていう | Why aren't we marked? That's what I'm saying. | 0.6893 | Why aren't we marked? That's what I'm saying. | 0.6893 | 平手 |
| 567 | その感じとか。 | That kind of feeling. | 0.8616 | That kind of feeling. | 0.8616 | 平手 |
| 568 | その辺の逸話は入ってるんですか？ | Does it include those kinds of anecdotes? | 0.7173 | Does it include those kinds of anecdotes? | 0.7173 | 平手 |
| 569 | 古田さんの耳に。≫僕は | To Mr. Furuta's ears. ≫I am | 0.7619 | To Mr. Furuta's ears. ≫I am | 0.7619 | 平手 |
| 570 | 目が悪いっていうのは眼鏡をかけてたのもあって | The reason I said my eyesight is bad is partly because I was wearing glasses. | 0.6950 | The reason I said my eyesight is bad is partly because I was wearing glasses. | 0.6950 | 平手 |
| 571 | プロ野球でもなかなか入れなかったので | I couldn't even get into professional baseball easily, so... | 0.8149 | I couldn't even get into professional baseball easily, so... | 0.8149 | 平手 |
| 572 | ２４歳から２５歳になる年にプロ野球に入ったので | I joined professional baseball in the year I turned from 24 to 25 years old. | 0.8735 | I joined professional baseball in the year I turned from 24 to 25 years old. | 0.8735 | 平手 |
| 573 | ちょっと遅れたんですけどそういうこともあったと思います。 | I was running a bit late, but I think things like that happen sometimes. | 0.7966 | I was running a bit late, but I think things like that happen sometimes. | 0.7966 | 平手 |
| 574 | 捕手として眼鏡はというのはというのもあったけどと。 | There was also the thing about wearing glasses as a catcher. | 0.7612 | There was also the thing about wearing glasses as a catcher. | 0.7612 | 平手 |
| 575 | 改めて、神田さんから古田さんの魅力を | Once again, Mr. Kanda, could you tell us about Mr. Furuta's appeal? | 0.4641 | Once again, Mr. Kanda, could you tell us about Mr. Furuta's appeal? | 0.4641 | 平手 |
| 576 | 伝えていただけると。 | Could you please tell them? | 0.6292 | Could you please tell them? | 0.6292 | 平手 |
| 577 | よろしいでしょうか？こんな機会をいただきまして | Is this alright? I'm truly grateful for this opportunity. | 0.6849 | Is this alright? I'm truly grateful for this opportunity. | 0.6849 | 平手 |
| 578 | ありがとうございます。 | Thank you very much. | 0.7402 | Thank you very much. | 0.7402 | 平手 |
| 579 | 私、神田が皆さんにお伝えします | I, Kanda, will inform everyone. | 0.6234 | I, Kanda, will inform everyone. | 0.6234 | 平手 |
| 580 | 古田敦也のここがすごいよ！まず１つ目は…。 | Here's what's amazing about Atsuya Furuta! First of all... | 0.7318 | Here's what's amazing about Atsuya Furuta! First of all... | 0.7318 | 平手 |
| 581 | コーナーを背負ってるんですね神田さんが。 | Mr. Kanda is carrying the corner section, isn't he? | 0.5425 | Mr. Kanda is carrying the corner section, isn't he? | 0.5425 | 平手 |
| 582 | めくりまで作って。≫ここがすごいよ！１つ目は | They even made flip book animations. ≫This part is amazing! First of all, | 0.5313 | They even made flip book animations. ≫This part is amazing! First of all, | 0.5313 | 平手 |
| 583 | マスクを外しても絶対に眼鏡が外れない！ | Even if I take off my mask, my glasses absolutely won't fall off! | 0.8797 | Even if I take off my mask, my glasses absolutely won't fall off! | 0.8797 | 平手 |
| 584 | １つ目がそこなの？ | Is the first one over there? | 0.9369 | Is the first one over there? | 0.9369 | 平手 |
| 585 | ２個しかないのに１個、それでいいの？ | There are only two, and you're taking one? Are you sure that's okay? | 0.8358 | There are only two, and you're taking one? Are you sure that's okay? | 0.8358 | 平手 |
| 586 | そうです。本当にすごくて。 | That's right. It's really amazing. | 0.8254 | That's right. It's really amazing. | 0.8254 | 平手 |
| 587 | 当時、私も眼鏡かけてたんですよ。 | Back then, I used to wear glasses too. | 0.8453 | Back then, I used to wear glasses too. | 0.8453 | 平手 |
| 588 | でも、すぐずれるんです。 | But it gets misaligned right away. | 0.6930 | But it gets misaligned right away. | 0.6930 | 平手 |
| 589 | でもキャッチャーミットかぶってて…。 | But (he/she) was wearing a catcher's mitt... | 0.6889 | But (he/she) was wearing a catcher's mitt... | 0.6889 | 平手 |
| 590 | マスクね。ミットじゃない。全然知らないから野球のことは。 | It's a mask. Not a mitt. I don't know anything about baseball. | 0.8501 | It's a mask. Not a mitt. I don't know anything about baseball. | 0.8501 | 平手 |
| 591 | 知ってます！マスクをばって外して | I know! You're taking off your mask with a snap! | 0.7363 | I know! You're taking off your mask with a snap! | 0.7363 | 平手 |
| 592 | ちゃんとここにあるんです。その証拠Ｖ、ご覧ください。 | It's definitely here. Please take a look at this evidence video. | 0.7698 | It's definitely here. Please take a look at this evidence video. | 0.7698 | 平手 |
| 593 | 神田さんが大好きな | I really like Kanda-san. | 0.5517 | I really like Kanda-san. | 0.5517 | 平手 |
| 594 | 古田さんがマスクを外すシーンがこちら。 | Here's the scene where Mr. Furuta takes off his mask. | 0.7829 | Here's the scene where Mr. Furuta takes off his mask. | 0.7829 | 平手 |
| 595 | マスクを外しダイビングキャッチでも | Even if I take off my mask and make a diving catch | 0.8015 | Even if I take off my mask and make a diving catch | 0.8015 | 平手 |
| 596 | 一切、眼鏡がずれない古田さんでした。 | Mr. Furuta never had his glasses slip even once. | 0.5882 | Mr. Furuta never had his glasses slip even once. | 0.5882 | 平手 |
| 597 | すごい！全くずれてないですよ！ | Wow! It's not off at all! | 0.7828 | Wow! It's not off at all! | 0.7828 | 平手 |
| 598 | まず取る時に普通引っかかるはずだし | First of all, it should normally get caught when you try to take it out. | 0.7274 | First of all, it should normally get caught when you try to take it out. | 0.7274 | 平手 |
| 599 | あんだけ、ぐいんってなったらぐりんってなるはずなんです。 | If it bends that much going 'gween', then it should go 'gween'. | 0.5392 | If it bends that much going 'gween', then it should go 'gween'. | 0.5392 | 平手 |
| 600 | なのに全くずれない。 | And yet it doesn't shift at all. | 0.7938 | And yet it doesn't shift at all. | 0.7938 | 平手 |
| 601 | どういうことなんですか？ | What do you mean? | 0.8630 | What do you mean? | 0.8630 | 平手 |
| 602 | もちろんマスク上げる時のサイズと | Of course, the size when raising the mask and... | 0.7968 | Of course, the size when raising the mask and... | 0.7968 | 平手 |
| 603 | 眼鏡のサイズを合わせていて | I'm adjusting the size of my glasses. | 0.6746 | I'm adjusting the size of my glasses. | 0.6746 | 平手 |
| 604 | 当たらない眼鏡にしてます。もちろん大きい眼鏡だと | I'm wearing glasses that don't press on my nose. Of course, with bigger glasses... | 0.7790 | I'm wearing glasses that don't press on my nose. Of course, with bigger glasses... | 0.7790 | 平手 |
| 605 | 当たると思うんですけど少し幅を狭めて。 | I think it'll hit, but narrow the width a bit. | 0.9312 | I think it'll hit, but narrow the width a bit. | 0.9312 | 平手 |
| 606 | でもそれまでいなかったわけじゃないですか | But it's not like I wasn't there until then, you know? | 0.8190 | But it's not like I wasn't there until then, you know? | 0.8190 | 平手 |
| 607 | そういう選手は。当たらないものはないけど | That kind of player... They never miss their mark. | 0.5881 | That kind of player... They never miss their mark. | 0.5881 | 平手 |
| 608 | 自分で作るってことですか？≫自分で作るというか | You mean I should make it myself? ≫ Well, not exactly make it myself, but... | 0.7343 | You mean I should make it myself? ≫ Well, not exactly make it myself, but... | 0.7343 | 平手 |
| 609 | 自分でサイズを合わせる感じです。 | You'll need to adjust the size yourself. | 0.6452 | You'll need to adjust the size yourself. | 0.6452 | 平手 |
| 610 | 本当いなかったんですよねキャッチャーで眼鏡の選手。 | There really wasn't a catcher who wore glasses, was there? | 0.5907 | There really wasn't a catcher who wore glasses, was there? | 0.5907 | 平手 |
| 611 | しかもキャッチャーやったことない | Besides, I've never played catcher before. | 0.6867 | Besides, I've never played catcher before. | 0.6867 | 平手 |
| 612 | スカウトほど | There's nothing like being scouted. | 0.3485 | There's nothing like being scouted. | 0.3485 | 平手 |
| 613 | あれ、無理だって言ってたらしいです。 | Oh, apparently they said it's impossible. | 0.7907 | Oh, apparently they said it's impossible. | 0.7907 | 平手 |
| 614 | でもレジェンドキャッチャーのノムさんだけは | But only Nomu-san, the legendary catcher, | 0.6782 | But only Nomu-san, the legendary catcher, | 0.6782 | 平手 |
| 615 | 今、眼鏡も良くなってきてるからいけるだろって言って | He said, 'My glasses have been getting better lately, so I should be able to manage.' | 0.6409 | He said, 'My glasses have been getting better lately, so I should be able to manage.' | 0.6409 | 平手 |
| 616 | そっから眼鏡も進化しましたよね。 | Glasses evolved from there too, didn't they? | 0.7278 | Glasses evolved from there too, didn't they? | 0.7278 | 平手 |
| 617 | スポーツ用のグラスも古田さんに影響されて | I was also influenced by Mr. Furuta to get sports glasses. | 0.6285 | I was also influenced by Mr. Furuta to get sports glasses. | 0.6285 | 平手 |
| 618 | 僕、進化したとすら。 | I might have even evolved. | 0.6824 | I might have even evolved. | 0.6824 | 平手 |
| 619 | 昔の眼鏡はどうしてもいわゆるガラスだったんですよね。 | Back in the day, glasses inevitably had what you'd call glass lenses. | 0.7167 | Back in the day, glasses inevitably had what you'd call glass lenses. | 0.7167 | 平手 |
| 620 | 当たったら割れるとか。それから | They say it'll break if it gets hit. And then... | 0.6728 | They say it'll break if it gets hit. And then... | 0.6728 | 平手 |
| 621 | プラスチックレンズができて | The plastic lenses are ready. | 0.7207 | The plastic lenses are ready. | 0.7207 | 平手 |
| 622 | あと、重量が軽くなりました。昔、眼鏡かけてる人って | Also, they've become lighter in weight. Back in the day, people who wore glasses... | 0.7809 | Also, they've become lighter in weight. Back in the day, people who wore glasses... | 0.7809 | 平手 |
| 623 | ここにすごい跡がついたじゃないですか。 | Look, there's a huge mark left here! | 0.7185 | Look, there's a huge mark left here! | 0.7185 | 平手 |
| 624 | 今、痕がつかなくなったのは軽くなったのもあるんで | The fact that it doesn't leave marks now is partly because it's become lighter. | 0.6907 | The fact that it doesn't leave marks now is partly because it's become lighter. | 0.6907 | 平手 |
| 625 | それで、そんなに不具合なく…。 | So, there weren't that many problems... | 0.8256 | So, there weren't that many problems... | 0.8256 | 平手 |
| 626 | でもね、ないほうがいいよ。雨の時とか | But you know, it's better not to have it. Especially when it rains. | 0.7835 | But you know, it's better not to have it. Especially when it rains. | 0.7835 | 平手 |
| 627 | 大変なんで。≫おしゃれですよね、あの形。 | It's tough. ≫That shape is stylish, isn't it? | 0.7949 | It's tough. ≫That shape is stylish, isn't it? | 0.7949 | 平手 |
| 628 | どこのブランドなんですか？≫ファッションとして | Which brand is this? ≫ For fashion | 0.7908 | Which brand is this? ≫ For fashion | 0.7908 | 平手 |
| 629 | 買おうとしてるの？ | Are you trying to buy it? | 0.8916 | Are you trying to buy it? | 0.8916 | 平手 |
| 630 | テレビの生放送であんまブランド名とか | They don't mention brand names much during live TV broadcasts. | 0.6506 | They don't mention brand names much during live TV broadcasts. | 0.6506 | 平手 |
| 631 | 言わないほうがいい…。 | You shouldn't say it... | 0.8676 | You shouldn't say it... | 0.8676 | 平手 |
| 632 | 大人でした。あ〜テンション下がっちゃった！ | I was being mature. Ugh~ now I'm feeling down! | 0.7533 | I was being mature. Ugh~ now I'm feeling down! | 0.7533 | 平手 |
| 633 | 松田君テンション下がっちゃった！ | Matsuda-kun's mood just dropped! | 0.7494 | Matsuda-kun's mood just dropped! | 0.7494 | 平手 |
| 634 | ＴＪ！Ｔｒａｖｉｓ　Ｊａｐａｎ！ | TJ! Travis Japan! | 0.8430 | TJ! Travis Japan! | 0.8430 | 平手 |
| 635 | あとでこっそり伺います。≫ちなみに、後ろでバンドが | I'll come by quietly later. ≫By the way, there's a band playing in the back. | 0.8176 | I'll come by quietly later. ≫By the way, there's a band playing in the back. | 0.8176 | 平手 |
| 636 | ついてるわけではないんですか。 | So you're not lucky after all? | 0.5928 | So you're not lucky after all? | 0.5928 | 平手 |
| 637 | これもそうなんですけどこうなってます。 | This one is like that too, but it's turned out this way. | 0.7982 | This one is like that too, but it's turned out this way. | 0.7982 | 平手 |
| 638 | 耳にかかる。 | It hangs over my ear. | 0.6513 | It hangs over my ear. | 0.6513 | 平手 |
| 639 | 俺、素顔見せるのが嫌だな…。 | I really hate showing my bare face... | 0.8688 | I really hate showing my bare face... | 0.8688 | 平手 |
| 640 | 深くかかってるんだ。≫これもそうなんです、動かない。 | I'm deeply involved in this. ≫ This one's the same - it won't move. | 0.8349 | I'm deeply involved in this. ≫ This one's the same - it won't move. | 0.8349 | 平手 |
| 641 | これもあんまりやられないってことですか？ | So you're saying this isn't done very often either? | 0.7627 | So you're saying this isn't done very often either? | 0.7627 | 平手 |
| 642 | ちょっとずれてくることもあるんですけど。 | Sometimes it gets a little out of alignment. | 0.6747 | Sometimes it gets a little out of alignment. | 0.6747 | 平手 |
| 643 | キャッチャーマスクと眼鏡があります。 | There's a catcher's mask and glasses. | 0.9002 | There's a catcher's mask and glasses. | 0.9002 | 平手 |
| 644 | 松田君、いける？かけてみて。普通の人がやったらどうなるのか。 | Matsuda-kun, can you do it? Give it a try. Let's see what would happen if an ordinary person tried it. | 0.7884 | Matsuda-kun, can you do it? Give it a try. Let's see what would happen if an ordinary person tried it. | 0.7884 | 平手 |
| 645 | 急に出場が決まったみたいな。 | Looks like they suddenly decided to participate. | 0.7701 | Looks like they suddenly decided to participate. | 0.7701 | 平手 |
| 646 | この回から松田行くぞって。 | From this episode, Matsuda's going with us. | 0.6662 | From this episode, Matsuda's going with us. | 0.6662 | 平手 |
| 647 | ユニホーム持ってきてないじゃないか。 | You didn't bring your uniform, did you? | 0.7055 | You didn't bring your uniform, did you? | 0.7055 | 平手 |
| 648 | いけるか？それで。 | Can you do it? With that. | 0.8482 | Can you do it? With that. | 0.8482 | 平手 |
| 649 | キャッチャーフライね。 | It's a catcher's fly. | 0.6047 | It's a catcher's fly. | 0.6047 | 平手 |
| 650 | 座ってて構えてる。いくよ。はい、キャッチャー！ | Stay seated and get ready. Here we go. Okay, catcher! | 0.6974 | Stay seated and get ready. Here we go. Okay, catcher! | 0.6974 | 平手 |
| 651 | やばい！取っちゃった！ | Oh no! I took it! | 0.8311 | Oh no! I took it! | 0.8311 | 平手 |
| 652 | 眼鏡が挟まってる！ | My glasses are stuck! | 0.8487 | My glasses are stuck! | 0.8487 | 平手 |
| 653 | 痛っ！≫全部持ってかれてる。 | Ouch! ≫ They took everything. | 0.6880 | Ouch! ≫ They took everything. | 0.6880 | 平手 |
| 654 | ここ、ばさーって。≫ダメよ。 | "I'm gonna touch here." ≫ "No, you can't." | 0.4883 | "I'm gonna touch here." ≫ "No, you can't." | 0.4883 | 平手 |
| 655 | マスクが本体みたいになってるから。 | Because the mask has become like my real face. | 0.7300 | Because the mask has become like my real face. | 0.7300 | 平手 |
| 656 | 絶対取れるんですよ。≫普通こうなるんですよ。 | You'll definitely get it. ≫ This is how it normally goes. | 0.8402 | You'll definitely get it. ≫ This is how it normally goes. | 0.8402 | 平手 |
| 657 | でも、よくとったねちゃんとフライを。 | But you caught it perfectly - a nice clean fly ball. | 0.5875 | But you caught it perfectly - a nice clean fly ball. | 0.5875 | 平手 |
| 658 | むずっ！これ。 | Ugh! This is tough. | 0.6353 | Ugh! This is tough. | 0.6353 | 平手 |
| 659 | この眼鏡だと、でかいから。≫サイズも違うしね。 | These glasses are too big for me. ≫ And the size is different too. | 0.8123 | These glasses are too big for me. ≫ And the size is different too. | 0.8123 | 平手 |
| 660 | 無理ゲーじゃん、これ。 | This game is impossible! | 0.6156 | This game is impossible! | 0.6156 | 平手 |
| 661 | もっとキュッとしてた眼鏡をということですよね、古田さんは。 | You're saying Furuta-san should wear glasses that make her look sharper, right? | 0.6342 | You're saying Furuta-san should wear glasses that make her look sharper, right? | 0.6342 | 平手 |
| 662 | でも生放送でうまいこととれましたね。 | But you managed to pull it off nicely during the live broadcast. | 0.7865 | But you managed to pull it off nicely during the live broadcast. | 0.7865 | 平手 |
| 663 | 眼鏡取れて、マスクもきれいに取れるってなかなかね。 | It's pretty nice how it comes off without messing up your glasses or mask. | 0.5999 | It's pretty nice how it comes off without messing up your glasses or mask. | 0.5999 | 平手 |
| 664 | こんなにガチャガチャして…。 | You're making so much noise... | 0.6707 | You're making so much noise... | 0.6707 | 平手 |
| 665 | すごいね。やっぱ持ってるね。≫うれしい！ | That's amazing! You really have it, don't you? ≫ I'm so happy! | 0.8263 | That's amazing! You really have it, don't you? ≫ I'm so happy! | 0.8263 | 平手 |
| 666 | 松田君すごいってみんな言うじゃないですか。 | Everyone says Matsuda-kun is amazing, don't they? | 0.8155 | Everyone says Matsuda-kun is amazing, don't they? | 0.8155 | 平手 |
| 667 | もう１個、神田さん。 | One more, Kanda-san. | 0.7548 | One more, Kanda-san. | 0.7548 | 平手 |
| 668 | 古田さんのすごいところ２つ目、こちらです。 | Here's the second amazing thing about Mr. Furuta. | 0.7166 | Here's the second amazing thing about Mr. Furuta. | 0.7166 | 平手 |
| 669 | クールそうに見えて実は武闘派。 | He may look cool, but he's actually a fighter at heart. | 0.7381 | He may look cool, but he's actually a fighter at heart. | 0.7381 | 平手 |
| 670 | やっぱりＩＤ野球のイメージが強い。 | As expected, they're strongly associated with small-ball baseball. | 0.4241 | As expected, they're strongly associated with small-ball baseball. | 0.4241 | 平手 |
| 671 | 実際そうなので、すごく知的で何があっても冷静という | That's actually true - (he's/she's) extremely intelligent and stays calm no matter what happens. | 0.6097 | That's actually true - (he's/she's) extremely intelligent and stays calm no matter what happens. | 0.6097 | 平手 |
| 672 | イメージがあるんですけどいざという時に | I have an image in mind, but when it comes down to it... | 0.7530 | I have an image in mind, but when it comes down to it... | 0.7530 | 平手 |
| 673 | 古田敦也、怒ります。見ちゃってください。 | Atsuya Furuta is getting angry. You've got to see this. | 0.6597 | Atsuya Furuta is getting angry. You've got to see this. | 0.6597 | 平手 |
| 674 | こちらです。 | Here it is. | 0.8532 | Here it is. | 0.8532 | 平手 |
| 675 | 神田さんが大好きな | I really like Kanda-san. | 0.5517 | I really like Kanda-san. | 0.5517 | 平手 |
| 676 | 古田さんの勇ましいシーンがこちら。 | Here's Mr. Furuta's heroic scene. | 0.7331 | Here's Mr. Furuta's heroic scene. | 0.7331 | 平手 |
| 677 | 今狙ったろって。 | I just aimed at you, didn't I? | 0.5719 | I just aimed at you, didn't I? | 0.5719 | 平手 |
| 678 | うわ、すげえ。≫いけいけ！ | Whoa, amazing! ≫Go go! | 0.8598 | Whoa, amazing! ≫Go go! | 0.8598 | 平手 |
| 679 | キャッチャーの人もすごかったな。 | The catcher was amazing too. | 0.8486 | The catcher was amazing too. | 0.8486 | 平手 |
| 680 | これですよ！これ！ここに来ちゃった時の | This is it! Right here! This is what happened when I came here! | 0.8756 | This is it! Right here! This is what happened when I came here! | 0.8756 | 平手 |
| 681 | うおーって。 | Whoa! | 0.7436 | Whoa! | 0.7436 | 平手 |
| 682 | 格好いいんですよね。 | You look really cool. | 0.6777 | You look really cool. | 0.6777 | 平手 |
| 683 | 最後めちゃくちゃふてくされてた。 | At the end, (he/she) was being totally sulky. | 0.6615 | At the end, (he/she) was being totally sulky. | 0.6615 | 平手 |
| 684 | 平気ですよみたいな顔してね。 | You're putting on a face like everything's fine. | 0.7366 | You're putting on a face like everything's fine. | 0.7366 | 平手 |
| 685 | あれは、熱くなったなと。 | Looks like things are heating up. | 0.6001 | Looks like things are heating up. | 0.6001 | 平手 |
| 686 | 野球ファンなら分かるんですけど | Baseball fans would understand this, but... | 0.6527 | Baseball fans would understand this, but... | 0.6527 | 平手 |
| 687 | ３球目なんですよ。 | It's the third pitch. | 0.8260 | It's the third pitch. | 0.8260 | 平手 |
| 688 | ３球連続来たんです。あれ、阪神の嶋田っていう | He threw three pitches in a row. Oh, that's Shimada from Hanshin. | 0.6048 | He threw three pitches in a row. Oh, that's Shimada from Hanshin. | 0.6048 | 平手 |
| 689 | ピッチャーで | I'll be the pitcher. | 0.3765 | I'll be the pitcher. | 0.3765 | 平手 |
| 690 | いまだに忘れてないです。≫名前、すっと出る。 | I still haven't forgotten. ≫Your name comes to mind immediately. | 0.8601 | I still haven't forgotten. ≫Your name comes to mind immediately. | 0.8601 | 平手 |
| 691 | 今アンパイアやってるんだけどあいつが投げたんです。 | I'm umpiring right now, but that guy was the one who threw it. | 0.7596 | I'm umpiring right now, but that guy was the one who threw it. | 0.7596 | 平手 |
| 692 | ３球目だったんですよ。１球目も | It was the third pitch. The first one too. | 0.8087 | It was the third pitch. The first one too. | 0.8087 | 平手 |
| 693 | おいって声掛けたんですけど３球目もだったんで | I called out 'Hey!' but he threw the third pitch anyway. | 0.6520 | I called out 'Hey!' but he threw the third pitch anyway. | 0.6520 | 平手 |
| 694 | ゴングが鳴りますよね。 | The gong will sound, right? | 0.7289 | The gong will sound, right? | 0.7289 | 平手 |
| 695 | 相手のキャッチャーの人もね。≫山田っていうんですけどね。 | Their catcher too. ≫His name's Yamada, by the way. | 0.5508 | Their catcher too. ≫His name's Yamada, by the way. | 0.5508 | 平手 |
| 696 | あれは別にパフォーマンスじゃ | That wasn't really a performance. | 0.6920 | That wasn't really a performance. | 0.6920 | 平手 |
| 697 | ないですよね？本気でみんなが | There's no way, right? Everyone can't possibly be serious. | 0.5740 | There's no way, right? Everyone can't possibly be serious. | 0.5740 | 平手 |
| 698 | オラオラ！ってなるわけですよね。 | You just go 'Ora ora!' like that, right? | 0.5655 | You just go 'Ora ora!' like that, right? | 0.5655 | 平手 |
| 699 | お子さんもたくさん見てますからね。 | A lot of children are watching too, you know. | 0.8423 | A lot of children are watching too, you know. | 0.8423 | 平手 |
| 700 | ほんまに殴ったりとかすると | If you actually hit someone or something like that... | 0.6218 | If you actually hit someone or something like that... | 0.6218 | 平手 |
| 701 | まずいじゃないですか。殴る人もいるけど。 | That's not good, is it? Some people might even hit you. | 0.6965 | That's not good, is it? Some people might even hit you. | 0.6965 | 平手 |
| 702 | それはみんな分かってるんで | Everyone already knows that, so... | 0.7553 | Everyone already knows that, so... | 0.7553 | 平手 |
| 703 | それやると、例えば１か月２か月停止とか | If you do that, you might get suspended for like one or two months. | 0.8262 | If you do that, you might get suspended for like one or two months. | 0.8262 | 平手 |
| 704 | １年停止とかなっちゃうんで | I might get suspended for a year or something. | 0.7612 | I might get suspended for a year or something. | 0.7612 | 平手 |
| 705 | 本当の暴力じゃなくて押し合いでワーッと来て | It's not real violence, they're just pushing each other and getting all worked up. | 0.7292 | It's not real violence, they're just pushing each other and getting all worked up. | 0.7292 | 平手 |
| 706 | ガチャガチャする感じ。口は悪い言葉 | She gives off a rough-around-the-edges vibe. Her mouth spews harsh words. | 0.5199 | She gives off a rough-around-the-edges vibe. Her mouth spews harsh words. | 0.5199 | 平手 |
| 707 | 放送禁止用語がいっぱい飛び交ってますけど。 | There's a lot of banned words being thrown around here. | 0.7713 | There's a lot of banned words being thrown around here. | 0.7713 | 平手 |
| 708 | 手は出さないって１個あるんですね、そりゃ。 | There's one rule - don't lay a hand on anyone, got it? | 0.5951 | There's one rule - don't lay a hand on anyone, got it? | 0.5951 | 平手 |
| 709 | だから、乱闘シーンとか今、映ってなかったですけど | So, the fight scene wasn't shown just now. | 0.8455 | So, the fight scene wasn't shown just now. | 0.8455 | 平手 |
| 710 | 最近ちょっと減ってきたんですけど | It's been decreasing a bit lately. | 0.8249 | It's been decreasing a bit lately. | 0.8249 | 平手 |
| 711 | 実際の僕らみたいに当事者が当たって周りに | Just like how we actually are, when the person involved takes the hit and those around them... | 0.7295 | Just like how we actually are, when the person involved takes the hit and those around them... | 0.7295 | 平手 |
| 712 | バーっと集まってきて止めにかかるんですよね。 | They all come rushing in and try to stop me, you know. | 0.5077 | They all come rushing in and try to stop me, you know. | 0.5077 | 平手 |
| 713 | 暴れる人とかもいるので。 | Because there are people who act violently. | 0.7825 | Because there are people who act violently. | 0.7825 | 平手 |
| 714 | 止められる前おとなしいのに止められてから | She was quiet before being stopped, but after being stopped... | 0.5961 | She was quiet before being stopped, but after being stopped... | 0.5961 | 平手 |
| 715 | 暴れるっていうやつがいるんです。止められること分かってるんです。 | There's this guy who keeps acting violent. He knows he can be stopped. | 0.6940 | There's this guy who keeps acting violent. He knows he can be stopped. | 0.6940 | 平手 |
| 716 | 止められて、うわーって暴れる。 | They tried to stop me, and I went "Whoa!" and struggled wildly. | 0.4812 | They tried to stop me, and I went "Whoa!" and struggled wildly. | 0.4812 | 平手 |
| 717 | あれはね、野球選手みんなから馬鹿にされる。 | You know what? All the baseball players make fun of him. | 0.7345 | You know what? All the baseball players make fun of him. | 0.7345 | 平手 |
| 718 | パフォーマンスだと。それ恥ずいな。 | You call that a performance? That's embarrassing. | 0.7101 | You call that a performance? That's embarrassing. | 0.7101 | 平手 |
| 719 | 大阪弁でいうとヘタレっていうんですけど。 | In Osaka dialect, we'd call someone like that a 'hetare' (good-for-nothing). | 0.5768 | In Osaka dialect, we'd call someone like that a 'hetare' (good-for-nothing). | 0.5768 | 平手 |
| 720 | けど、止められてからうわーって暴れるやつがいて。 | But there's this guy who goes wild and starts thrashing around after being stopped. | 0.7676 | But there's this guy who goes wild and starts thrashing around after being stopped. | 0.7676 | 平手 |
| 721 | それはみんな野球選手からの扱いが悪くなる。 | That will make all the baseball players treat you worse. | 0.7683 | That will make all the baseball players treat you worse. | 0.7683 | 平手 |
| 722 | すいません。神田さんが私、いい仕事したみたいな | Excuse me. It seems Mr. Kanda thinks I did a good job. | 0.7489 | Excuse me. It seems Mr. Kanda thinks I did a good job. | 0.7489 | 平手 |
| 723 | 顔してるんですけど | I'm making a face right now. | 0.6704 | I'm making a face right now. | 0.6704 | 平手 |
| 724 | 僕も野球、大ファンなんで野球面の話を | I'm also a huge baseball fan, so let's talk about baseball. | 0.7948 | I'm also a huge baseball fan, so let's talk about baseball. | 0.7948 | 平手 |
| 725 | ちゃんとしなきゃダメなんですよ。マニアックな話を | You've got to take this seriously. Stop with all the niche talk. | 0.4385 | You've got to take this seriously. Stop with all the niche talk. | 0.4385 | 平手 |
| 726 | しようっていうんじゃないんです。 | I'm not saying we should do it. | 0.8347 | I'm not saying we should do it. | 0.8347 | 平手 |
| 727 | 両面で、いい面いっぱいありますから。 | There are many good aspects on both sides. | 0.8163 | There are many good aspects on both sides. | 0.8163 | 平手 |
| 728 | 待たせたぞじゃないんです少なすぎなんです。 | I didn't make you wait - there's just too few of them. | 0.7739 | I didn't make you wait - there's just too few of them. | 0.7739 | 平手 |
| 729 | 僕のほうです。ここがすごいよ！古田敦也。 | It's me. This part is amazing! Atsuya Furuta. | 0.8030 | It's me. This part is amazing! Atsuya Furuta. | 0.8030 | 平手 |
| 730 | まず、僕の１つ目なんですけど一番分かりやすい | First, regarding my first point, it's the easiest to understand. | 0.7656 | First, regarding my first point, it's the easiest to understand. | 0.7656 | 平手 |
| 731 | バッターとしてすごかったですよという | They were amazing as a batter. | 0.6524 | They were amazing as a batter. | 0.6524 | 平手 |
| 732 | 野球詳しくなくても分かるのが | Even if you don't know much about baseball, you can understand it. | 0.6703 | Even if you don't know much about baseball, you can understand it. | 0.6703 | 平手 |
| 733 | キャッチャーなのに１試合で４ホームラン。 | He's a catcher, yet he hit four home runs in a single game. | 0.7902 | He's a catcher, yet he hit four home runs in a single game. | 0.7902 | 平手 |
| 734 | すごい！ | Wow! | 0.6892 | Wow! | 0.6892 | 平手 |
| 735 | 全打席？≫大谷選手が１本打ったって | Every at-bat? ≫ I heard Ohtani got one hit. | 0.6255 | Every at-bat? ≫ I heard Ohtani got one hit. | 0.6255 | 平手 |
| 736 | 爽やかな朝じゃないですか。２本打ったら | It's a refreshing morning, isn't it? Let's hit two balls. | 0.7128 | It's a refreshing morning, isn't it? Let's hit two balls. | 0.7128 | 平手 |
| 737 | 今日２本だよ！って思うじゃないですか。 | You know how you think, 'Two videos today!' | 0.6782 | You know how you think, 'Two videos today!' | 0.6782 | 平手 |
| 738 | キャッチャーなのにっていうのはキャッチャーっていうのは | Even though you're a catcher, being a catcher means... | 0.6355 | Even though you're a catcher, being a catcher means... | 0.6355 | 平手 |
| 739 | 特に古田さんの時代ぐらいから | Especially since around Mr. Furuta's era | 0.7319 | Especially since around Mr. Furuta's era | 0.7319 | 平手 |
| 740 | とにかく守備を頑張ってくれと。あとピッチャーのリードを | Just do your best on defense. And also help guide the pitcher. | 0.6774 | Just do your best on defense. And also help guide the pitcher. | 0.6774 | 平手 |
| 741 | 頑張ってくれと。 | Do your best. | 0.7548 | Do your best. | 0.7548 | 平手 |
| 742 | だから、打撃は二の次でいいって言われてるのに | Even though they told me batting comes second... | 0.5766 | Even though they told me batting comes second... | 0.5766 | 平手 |
| 743 | ２００３年の６月２８日 | June 28, 2003 | 0.7194 | June 28, 2003 | 0.7194 | 平手 |
| 744 | 広島戦、日本大記録になります。１試合で４本塁打です。 | Against Hiroshima, they've set a new Japanese record - 4 home runs in a single game. | 0.7982 | Against Hiroshima, they've set a new Japanese record - 4 home runs in a single game. | 0.7982 | 平手 |
| 745 | ４打数連続ホームランを達成します。 | He/She hits home runs in four consecutive at-bats. | 0.7769 | He/She hits home runs in four consecutive at-bats. | 0.7769 | 平手 |
| 746 | ありがとうございます。≫これ言っとかなきゃ | Thank you very much. ≫ I had to say this. | 0.7772 | Thank you very much. ≫ I had to say this. | 0.7772 | 平手 |
| 747 | ダメですよね。 | That's no good, right? | 0.7432 | That's no good, right? | 0.7432 | 平手 |
| 748 | 最近、皆さん、僕のこと分かってないと思うのでね。 | Lately, I feel like none of you really understand me. | 0.7975 | Lately, I feel like none of you really understand me. | 0.7975 | 平手 |
| 749 | 結構いい選手だったんでね。思い出していただいて | He was actually quite a good player, you know. Please try to remember him. | 0.7978 | He was actually quite a good player, you know. Please try to remember him. | 0.7978 | 平手 |
| 750 | ありがとうございます。 | Thank you very much. | 0.7402 | Thank you very much. | 0.7402 | 平手 |
| 751 | 日本タイ記録で他に王選手とか | Among Japanese-Thai records, there's also Player Oh and others. | 0.6267 | Among Japanese-Thai records, there's also Player Oh and others. | 0.6267 | 平手 |
| 752 | 選ばれた人間しか打ってないんです。 | Only chosen people can hit it. | 0.7429 | Only chosen people can hit it. | 0.7429 | 平手 |
| 753 | 守備がすごいリードがすごいっていわれてるけど | People say my defense and lead are amazing, but... | 0.6096 | People say my defense and lead are amazing, but... | 0.6096 | 平手 |
| 754 | 通算ホームラン２００本以上打ってるんです。 | He's hit over 200 home runs in his career. | 0.7538 | He's hit over 200 home runs in his career. | 0.7538 | 平手 |
| 755 | これ、キャッチャーっていう重責をやりながら | While handling this heavy responsibility of being a catcher, | 0.7615 | While handling this heavy responsibility of being a catcher, | 0.7615 | 平手 |
| 756 | しかも大学出て、社会人出て | What's more, (I/You/He/She) graduated from university and entered the workforce. | 0.4445 | What's more, (I/You/He/She) graduated from university and entered the workforce. | 0.4445 | 平手 |
| 757 | 遅いプロ入りでキャッチャーとしては | He started his professional career relatively late for a catcher. | 0.4404 | He started his professional career relatively late for a catcher. | 0.4404 | 平手 |
| 758 | 歴代７位の記録ですって。≫ありがとうございます。 | "They say it's the 7th best record in history." ≫ "Thank you very much." | 0.7226 | "They say it's the 7th best record in history." ≫ "Thank you very much." | 0.7226 | 平手 |
| 759 | あんまり持ち上げられるといいことないよって | Being praised too much isn't always a good thing, you know. | 0.4160 | Being praised too much isn't always a good thing, you know. | 0.4160 | 平手 |
| 760 | 教えられてきたので…。 | Because that's what I was taught... | 0.8722 | Because that's what I was taught... | 0.8722 | 平手 |
| 761 | 向こうがポンコツな分僕は持ち上げるほう…。 | Since they're hopeless, I'll have to pick up the slack... | 0.5393 | Since they're hopeless, I'll have to pick up the slack... | 0.5393 | 平手 |
| 762 | ポンコツじゃない！これすごいですから。 | I'm not useless! This is actually amazing. | 0.6997 | I'm not useless! This is actually amazing. | 0.6997 | 平手 |
| 763 | 神田さんは顔ファンだから。≫４はすごいですね。 | Because Kanda-san is a fan of your face. ≫Wow, number 4 is amazing. | 0.7173 | Because Kanda-san is a fan of your face. ≫Wow, number 4 is amazing. | 0.7173 | 平手 |
| 764 | ４が出る時って行ける感じが…。何なんですか？ | When a four comes up, it feels like I can go... What is this? | 0.8128 | When a four comes up, it feels like I can go... What is this? | 0.8128 | 平手 |
| 765 | この試合がたまたまなんですけど | This match just happened by chance, but... | 0.7156 | This match just happened by chance, but... | 0.7156 | 平手 |
| 766 | 年に１回ある | It happens once a year. | 0.8303 | It happens once a year. | 0.8303 | 平手 |
| 767 | ＮＨＫでの中継だったんです。だから、ＮＨＫって全国ネットで | It was broadcast on NHK. That's why NHK reaches nationwide. | 0.8217 | It was broadcast on NHK. That's why NHK reaches nationwide. | 0.8217 | 平手 |
| 768 | ヤクルトと広島のなんてやらないのに | I'm not even going to watch the Yakult vs. Hiroshima game. | 0.6422 | I'm not even going to watch the Yakult vs. Hiroshima game. | 0.6422 | 平手 |
| 769 | その時に打てたっていう俺ってすごいなって思ったんです。 | I thought to myself, 'Damn, I'm amazing for being able to hit it at that moment.' | 0.6929 | I thought to myself, 'Damn, I'm amazing for being able to hit it at that moment.' | 0.6929 | 平手 |
| 770 | 持ってるなと思いました。 | I thought you had it. | 0.8765 | I thought you had it. | 0.8765 | 平手 |
| 771 | 中継があるないで気合の入り方、違うんですか？ | Does your level of determination change depending on whether it's being broadcast or not? | 0.5242 | Does your level of determination change depending on whether it's being broadcast or not? | 0.5242 | 平手 |
| 772 | そこまで気づいてないんですけど。 | I haven't really noticed that much, though. | 0.7694 | I haven't really noticed that much, though. | 0.7694 | 平手 |
| 773 | やってることは知ってるんですけど | I know what you're doing, but... | 0.7984 | I know what you're doing, but... | 0.7984 | 平手 |
| 774 | そういう時に活躍できてよかったなと思って。 | I'm glad I could be useful in that situation. | 0.7479 | I'm glad I could be useful in that situation. | 0.7479 | 平手 |
| 775 | 今日、映像が出ないので | The video isn't showing up today, so... | 0.8070 | The video isn't showing up today, so... | 0.8070 | 平手 |
| 776 | 借りれなかったのかなと。 | I wonder if they couldn't borrow it. | 0.7302 | I wonder if they couldn't borrow it. | 0.7302 | 平手 |
| 777 | 眼鏡ずれないやつは映像出てホームランは見れない？ | Can't you guys with glasses that don't slip see the home run in the footage? | 0.7924 | Can't you guys with glasses that don't slip see the home run in the footage? | 0.7924 | 平手 |
| 778 | ＮＨＫだとちょっとね難しいんですよ。 | NHK is a bit difficult, you know. | 0.8312 | NHK is a bit difficult, you know. | 0.8312 | 平手 |
| 779 | １本出て、２本出て | One comes out, then two come out. | 0.7564 | One comes out, then two come out. | 0.7564 | 平手 |
| 780 | 次ぐらいから狙おうかみたいな？ | Maybe we should aim for the next one or something? | 0.6357 | Maybe we should aim for the next one or something? | 0.6357 | 平手 |
| 781 | ３本打ったあとに４本目が日本記録っていうのは | After hitting three, the fourth one being a Japanese record is... | 0.8529 | After hitting three, the fourth one being a Japanese record is... | 0.8529 | 平手 |
| 782 | お客さんも全員知っていて。 | All the customers knew about it too. | 0.8146 | All the customers knew about it too. | 0.8146 | 平手 |
| 783 | 広島球場で、僕にとってはアウェーだったんですけど | It was at Hiroshima Stadium, which felt like an away game for me, but... | 0.7471 | It was at Hiroshima Stadium, which felt like an away game for me, but... | 0.7471 | 平手 |
| 784 | ピッチャーも打たれたくないからストレート投げないんですよ。 | The pitcher doesn't throw fastballs because he doesn't want to get hit either. | 0.7979 | The pitcher doesn't throw fastballs because he doesn't want to get hit either. | 0.7979 | 平手 |
| 785 | スリーボールになったらブーイングが起きたんです。 | When it became three balls, the crowd started booing. | 0.5665 | When it became three balls, the crowd started booing. | 0.5665 | 平手 |
| 786 | 広島のファンが勝負しろって。 | Hiroshima fans are telling them to fight harder. | 0.6523 | Hiroshima fans are telling them to fight harder. | 0.6523 | 平手 |
| 787 | ＴＪ！ | TJ! | 0.9568 | TJ! | 0.9568 | 平手 |
| 788 | 続いて３項目の２つ目なんですが | Next, regarding the second item out of the three points, | 0.6989 | Next, regarding the second item out of the three points, | 0.6989 | 平手 |
| 789 | 例えば家族に野球詳しい人いたら今日聞いたことを通ぶって言うと | For example, if you have a family member who knows a lot about baseball, you could casually mention what you heard today. | 0.8370 | For example, if you have a family member who knows a lot about baseball, you could casually mention what you heard today. | 0.8370 | 平手 |
| 790 | おお、すごいな！と思われるので２つ目はこちらです。 | You'll probably think 'Wow, amazing!' so here's the second one. | 0.7305 | You'll probably think 'Wow, amazing!' so here's the second one. | 0.7305 | 平手 |
| 791 | ちょっとマニアック。通算盗塁阻止率 | This is a bit niche. Career caught stealing percentage. | 0.4702 | This is a bit niche. Career caught stealing percentage. | 0.4702 | 平手 |
| 792 | 驚異の４割６分２厘。 | An astonishing batting average of .462. | 0.4492 | An astonishing batting average of .462. | 0.4492 | 平手 |
| 793 | 家帰ったら、野球詳しい家族に | When I get home, I'll ask my family member who knows baseball well. | 0.7322 | When I get home, I'll ask my family member who knows baseball well. | 0.7322 | 平手 |
| 794 | でも、古田っていったら盗塁阻止率よねって言うと | But when you mention Furuta, people immediately think about his caught stealing percentage, right? | 0.4125 | But when you mention Furuta, people immediately think about his caught stealing percentage, right? | 0.4125 | 平手 |
| 795 | どうしたお前！？って言われますから。 | Because people say to me, 'What's wrong with you!?' | 0.6755 | Because people say to me, 'What's wrong with you!?' | 0.6755 | 平手 |
| 796 | でも、本当に守備がすごくて要するに、何個盗塁を | But honestly, his defense is amazing - basically, how many stolen bases | 0.5947 | But honestly, his defense is amazing - basically, how many stolen bases | 0.5947 | 平手 |
| 797 | みんなが仕掛けてきてそのうちいくつ | Everyone keeps setting them up, and some of them | 0.6585 | Everyone keeps setting them up, and some of them | 0.6585 | 平手 |
| 798 | アウトにしたかっていう確率なんですけど | It's about the probability of getting them out. | 0.6041 | It's about the probability of getting them out. | 0.6041 | 平手 |
| 799 | 普通、３割台でもまあまあ守れてるよねっていう | Usually, maintaining around a 30% success rate is considered decent, right? | 0.6157 | Usually, maintaining around a 30% success rate is considered decent, right? | 0.6157 | 平手 |
| 800 | 数字なんです。 | It's a number. | 0.8967 | It's a number. | 0.8967 | 平手 |
| 801 | １年でも４割超えれば | If we can exceed 40% even in one year | 0.7914 | If we can exceed 40% even in one year | 0.7914 | 平手 |
| 802 | こいつはすごいっていうことなんです。 | This means he's amazing. | 0.8151 | This means he's amazing. | 0.8151 | 平手 |
| 803 | １８年間通算で４割６分っていう | He maintained a .460 batting average over 18 years. | 0.5134 | He maintained a .460 batting average over 18 years. | 0.5134 | 平手 |
| 804 | プロ野球記録は考えられなくて | I can't even imagine professional baseball records. | 0.7784 | I can't even imagine professional baseball records. | 0.7784 | 平手 |
| 805 | １年目から３割いってればまあまあよく頑張ったな | If you've managed to hit 30% right from your first year, you've done pretty well. | 0.6991 | If you've managed to hit 30% right from your first year, you've done pretty well. | 0.6991 | 平手 |
| 806 | ましてや１年目であたふたしてる中で | Especially when you're flustered during your first year | 0.7146 | Especially when you're flustered during your first year | 0.7146 | 平手 |
| 807 | すごいじゃんっていう中で | While everyone was saying 'That's amazing!' | 0.4250 | While everyone was saying 'That's amazing!' | 0.4250 | 平手 |
| 808 | リーグ１位、５割２分７厘。≫１年目で！？ | "First place in the league with a .527 winning percentage." ≫ "In your first year!?" | 0.6145 | "First place in the league with a .527 winning percentage." ≫ "In your first year!?" | 0.6145 | 平手 |
| 809 | いきなりそうなんです。 | It's so sudden. | 0.7261 | It's so sudden. | 0.7261 | 平手 |
| 810 | だから走っても走ってもアウトにするんです。 | That's why no matter how hard I run, I always get out. | 0.7654 | That's why no matter how hard I run, I always get out. | 0.7654 | 平手 |
| 811 | 恐ろしいのは１年目っていうのは | What's scary is that first year. | 0.8462 | What's scary is that first year. | 0.8462 | 平手 |
| 812 | まだ古田ってどんなもん？っていうころだから | This was back when we were still wondering what kind of guy Furuta really was. | 0.4455 | This was back when we were still wondering what kind of guy Furuta really was. | 0.4455 | 平手 |
| 813 | みんな走ってくるんですよ。 | Everyone comes running. | 0.9235 | Everyone comes running. | 0.9235 | 平手 |
| 814 | 新人すごいか知らないけど俺の足のほうがあるからねって | I don't know if the newbie is amazing or not, but my legs are better, you know. | 0.7706 | I don't know if the newbie is amazing or not, but my legs are better, you know. | 0.7706 | 平手 |
| 815 | バンバンくる中、次々と刺して５割超える。 | Despite coming at me relentlessly, I kept stabbing them one after another, exceeding a 50% hit rate. | 0.6031 | Despite coming at me relentlessly, I kept stabbing them one after another, exceeding a 50% hit rate. | 0.6031 | 平手 |
| 816 | そして１９９３年６割４分４厘。 | And in 1993, it was 64.4 percent. | 0.6913 | And in 1993, it was 64.4 percent. | 0.6913 | 平手 |
| 817 | もう目の前の投げることには集中してないってことなんですか。 | So you're saying you're no longer focusing on throwing what's right in front of you? | 0.7686 | So you're saying you're no longer focusing on throwing what's right in front of you? | 0.7686 | 平手 |
| 818 | ランナーは気にしてます。キャッチャー | The runner is paying attention. The catcher. | 0.6747 | The runner is paying attention. The catcher. | 0.6747 | 平手 |
| 819 | みんなそうなんですけど。 | Everyone is like that though. | 0.8726 | Everyone is like that though. | 0.8726 | 平手 |
| 820 | 分かるんですか？走りそうに見せかけて走らない | Can you tell? I pretend like I'm going to run, but I don't. | 0.6282 | Can you tell? I pretend like I'm going to run, but I don't. | 0.6282 | 平手 |
| 821 | 選手もいるじゃないですか。 | There are players too, you know. | 0.7825 | There are players too, you know. | 0.7825 | 平手 |
| 822 | もちろんいますけどスタート切ったり切らなかったり。 | Of course I'm here, but sometimes I start and sometimes I don't. | 0.7865 | Of course I'm here, but sometimes I start and sometimes I don't. | 0.7865 | 平手 |
| 823 | 常に、こっちもいつでもいけるように準備をしてて。 | Make sure you're always ready to go whenever I am. | 0.7420 | Make sure you're always ready to go whenever I am. | 0.7420 | 平手 |
| 824 | すごい、歴代ランキング…。≫上位にこんなに入ってる。 | Wow, the all-time rankings... ≫I can't believe I'm ranked this high. | 0.6822 | Wow, the all-time rankings... ≫I can't believe I'm ranked this high. | 0.6822 | 平手 |
| 825 | １位、３位、４位が古田さんなんですね。 | So Mr. Furuta came in first, third, and fourth place, huh? | 0.6704 | So Mr. Furuta came in first, third, and fourth place, huh? | 0.6704 | 平手 |
| 826 | あり得ないんですよ。≫何がすごかったら | "That's impossible!" ≫ "What would be amazing enough?" | 0.5268 | "That's impossible!" ≫ "What would be amazing enough?" | 0.5268 | 平手 |
| 827 | できることなんですか？ | What can you do? | 0.8453 | What can you do? | 0.8453 | 平手 |
| 828 | トータルのタイムキャッチャーがとってから | Since the total time capture was taken | 0.7392 | Since the total time capture was taken | 0.7392 | 平手 |
| 829 | セカンドベース上に | On second base | 0.8912 | On second base | 0.8912 | 平手 |
| 830 | 大体１．９秒くらいで | It's roughly about 1.9 seconds. | 0.8977 | It's roughly about 1.9 seconds. | 0.8977 | 平手 |
| 831 | プロだったら２秒切りたい１．９秒ぐらい | If you're a pro, you'd want to shave off 2 seconds - aiming for around 1.9 seconds. | 0.7784 | If you're a pro, you'd want to shave off 2 seconds - aiming for around 1.9 seconds. | 0.7784 | 平手 |
| 832 | とって早く投げるか強い球を投げるか。 | Should I throw it quickly or throw a powerful ball? | 0.8587 | Should I throw it quickly or throw a powerful ball? | 0.8587 | 平手 |
| 833 | あとはコントロールよく投げるのが大事なんですけど。 | After that, the important thing is to throw with good control. | 0.7833 | After that, the important thing is to throw with good control. | 0.7833 | 平手 |
| 834 | その３つそろってるんですよ。すごい選手の成功率が | He's got all three of those qualities. That's why top players have such high success rates. | 0.6324 | He's got all three of those qualities. That's why top players have such high success rates. | 0.6324 | 平手 |
| 835 | ９割なんですよ。それを６割にするって | It's 90% now. And you're saying we should reduce it to 60%? | 0.6494 | It's 90% now. And you're saying we should reduce it to 60%? | 0.6494 | 平手 |
| 836 | 考えられない、どう考えても。 | I can't believe it, no matter how I think about it. | 0.7839 | I can't believe it, no matter how I think about it. | 0.7839 | 平手 |
| 837 | ちょっと映像もあるみたいなので見てください。 | It seems there's some footage too, so please take a look. | 0.8603 | It seems there's some footage too, so please take a look. | 0.8603 | 平手 |
| 838 | 古田さんが盗塁を阻止するシーンがこちら。 | Here's the scene where Mr. Furuta prevents the stolen base. | 0.7126 | Here's the scene where Mr. Furuta prevents the stolen base. | 0.7126 | 平手 |
| 839 | 俺の顔いらんな、あの写真。≫監督の高津さんです。 | You don't need my face in that photo. ≫ This is Director Takatsu. | 0.8306 | You don't need my face in that photo. ≫ This is Director Takatsu. | 0.8306 | 平手 |
| 840 | 両方ともものすごいバッターがバッターボックスにいて | Both batters at the plate are incredible hitters. | 0.5777 | Both batters at the plate are incredible hitters. | 0.5777 | 平手 |
| 841 | お前バッターのほう頑張れ盗塁は俺がやるって感じ。 | You focus on batting. I'll handle stealing bases. | 0.5339 | You focus on batting. I'll handle stealing bases. | 0.5339 | 平手 |
| 842 | ランナーはもう俺に任せてバッターに集中するみたいな | The runner seems to be leaving it to me now and focusing on the batter. | 0.7599 | The runner seems to be leaving it to me now and focusing on the batter. | 0.7599 | 平手 |
| 843 | そういう感じ。 | That's the feeling. | 0.8603 | That's the feeling. | 0.8603 | 平手 |
| 844 | ピッチャーは思いっきり投げればいいみたいなね。 | It seems like the pitcher should just throw with all their might. | 0.7306 | It seems like the pitcher should just throw with all their might. | 0.7306 | 平手 |
| 845 | しゃがみ具合は他のキャッチャーと | Your crouching stance is different from other catchers. | 0.5426 | Your crouching stance is different from other catchers. | 0.5426 | 平手 |
| 846 | 同じなんですよね？ | It's the same, right? | 0.8972 | It's the same, right? | 0.8972 | 平手 |
| 847 | 僕、どちらかというとひざがやわらかかったと | I'd say my knees were rather flexible, if anything. | 0.6374 | I'd say my knees were rather flexible, if anything. | 0.6374 | 平手 |
| 848 | 思うんです。 | I think so. | 0.9090 | I think so. | 0.9090 | 平手 |
| 849 | だから低いところに低く構えられたほうだと思うので。 | So I think it's better to keep your stance low when you're in a low position. | 0.6857 | So I think it's better to keep your stance low when you're in a low position. | 0.6857 | 平手 |
| 850 | 低いところはパンといける感じなんですけど | The lower parts have a nice bounce to them. | 0.4200 | The lower parts have a nice bounce to them. | 0.4200 | 平手 |
| 851 | かたい人は | Stubborn people | 0.6315 | Stubborn people | 0.6315 | 平手 |
| 852 | どうしても浮き気味になるので一瞬、時間がかかるって | It tends to float up no matter what, so it'll take a moment. | 0.6401 | It tends to float up no matter what, so it'll take a moment. | 0.6401 | 平手 |
| 853 | いわれてるんです。 | They're saying that. | 0.3518 | They're saying that. | 0.3518 | 平手 |
| 854 | 古田さん的には全部ですか？肩と速さと、コントロールと。 | Mr. Furuta, do you mean everything? The arm strength, speed, and control? | 0.7981 | Mr. Furuta, do you mean everything? The arm strength, speed, and control? | 0.7981 | 平手 |
| 855 | 肩の強さだけで言うと僕より強いキャッチャーは | If we're just talking about arm strength, there are catchers stronger than me. | 0.6998 | If we're just talking about arm strength, there are catchers stronger than me. | 0.6998 | 平手 |
| 856 | いっぱいいたと思います。 | I think there were a lot of them. | 0.7605 | I think there were a lot of them. | 0.7605 | 平手 |
| 857 | あとはコントロール正確に投げるっていうことを | After that, it's all about throwing with precise control. | 0.6716 | After that, it's all about throwing with precise control. | 0.6716 | 平手 |
| 858 | 注意して、やってました。 | I was doing it carefully. | 0.7763 | I was doing it carefully. | 0.7763 | 平手 |
| 859 | 澤部君でいえばゲストが暴走してくるわけよ。 | Speaking of Sawabe-kun, guests tend to go wild around him. | 0.5572 | Speaking of Sawabe-kun, guests tend to go wild around him. | 0.5572 | 平手 |
| 860 | それを刺してＣＭにいくっていう。 | They said they'd stab him and then go film the commercial. | 0.5496 | They said they'd stab him and then go film the commercial. | 0.5496 | 平手 |
| 861 | １回も時間を破綻させない能力だから。 | Because it's the ability to never waste time even once. | 0.8823 | Because it's the ability to never waste time even once. | 0.8823 | 平手 |
| 862 | できてますね〜！≫できてないですよ！ | You're doing great! ≫ No I'm not! | 0.7541 | You're doing great! ≫ No I'm not! | 0.7541 | 平手 |
| 863 | 球界の古田。≫できてないですって。 | "Furuta of the baseball world." ≫ "He says he hasn't been able to do it." | 0.5850 | "Furuta of the baseball world." ≫ "He says he hasn't been able to do it." | 0.5850 | 平手 |
| 864 | 何か、ふーってそのままＣＭにいく時あります。 | You know how sometimes you just sigh and then it cuts straight to a commercial? | 0.3875 | You know how sometimes you just sigh and then it cuts straight to a commercial? | 0.3875 | 平手 |
| 865 | 投げてないのに。 | But I didn't throw it. | 0.7886 | But I didn't throw it. | 0.7886 | 平手 |
| 866 | ボール持ったまま。≫その中で古田さんがすごいのは | He kept holding the ball. ≫ What's amazing about Mr. Furuta in that situation is | 0.6231 | He kept holding the ball. ≫ What's amazing about Mr. Furuta in that situation is | 0.6231 | 平手 |
| 867 | 体も強いっていう。 | They say he's physically strong too. | 0.7936 | They say he's physically strong too. | 0.7936 | 平手 |
| 868 | 当時のプロ野球はまあ激突、荒々しいんですよ。 | Back then, professional baseball was quite intense and rough, you know. | 0.8041 | Back then, professional baseball was quite intense and rough, you know. | 0.8041 | 平手 |
| 869 | そのＶＴＲもあるということで見てください。 | Please watch it since we also have that VTR available. | 0.8078 | Please watch it since we also have that VTR available. | 0.8078 | 平手 |
| 870 | 古田さんが体を張ってブロックするシーンが、こちら。 | Here's the scene where Mr. Furuta puts his body on the line to block. | 0.6841 | Here's the scene where Mr. Furuta puts his body on the line to block. | 0.6841 | 平手 |
| 871 | うわー！ | Whoa! | 0.9316 | Whoa! | 0.9316 | 平手 |
| 872 | 強いな。 | You're strong. | 0.8092 | You're strong. | 0.8092 | 平手 |
| 873 | もうタックルだからね。 | It's already tackle time. | 0.5198 | It's already tackle time. | 0.5198 | 平手 |
| 874 | 交通事故じゃん。 | That's a traffic accident. | 0.8901 | That's a traffic accident. | 0.8901 | 平手 |
| 875 | 別の競技だな。 | That's a different sport. | 0.8565 | That's a different sport. | 0.8565 | 平手 |
| 876 | これ、ちょっと横澤も。 | Hey, Yokozawa, you should try this too. | 0.5622 | Hey, Yokozawa, you should try this too. | 0.5622 | 平手 |
| 877 | 飛んじゃってましたもんね。 | It flew away, didn't it? | 0.6076 | It flew away, didn't it? | 0.6076 | 平手 |
| 878 | 本当交通事故のような。危ない！ | That was almost like a traffic accident. That was dangerous! | 0.8087 | That was almost like a traffic accident. That was dangerous! | 0.8087 | 平手 |
| 879 | これ、今はもうないですか？さすがに。 | This isn't available anymore, is it? I figured as much. | 0.7248 | This isn't available anymore, is it? I figured as much. | 0.7248 | 平手 |
| 880 | 今はルールでなくなりましたね。 | It's no longer a rule now, is it? | 0.8085 | It's no longer a rule now, is it? | 0.8085 | 平手 |
| 881 | 昔は逆にぶっ飛ばせみたいな感じでやってましたね。 | Back in the day, we actually used to go all out with reckless abandon. | 0.5348 | Back in the day, we actually used to go all out with reckless abandon. | 0.5348 | 平手 |
| 882 | 特に外国人選手は | Especially foreign players | 0.9355 | Especially foreign players | 0.9355 | 平手 |
| 883 | メジャーリーガーはそういう感じだったので。 | That's how Major Leaguers were. | 0.7165 | That's how Major Leaguers were. | 0.7165 | 平手 |
| 884 | 皆さんも連想してほしいですけど | I'd like you all to imagine this as well, but... | 0.7158 | I'd like you all to imagine this as well, but... | 0.7158 | 平手 |
| 885 | １００ｋｇくらいのやつが思い切り僕のとこ | A guy weighing about 100kg came charging straight at me. | 0.7086 | A guy weighing about 100kg came charging straight at me. | 0.7086 | 平手 |
| 886 | 走ってくるんですよ。めっちゃ怖いですよ。 | They're running this way. It's super scary! | 0.6479 | They're running this way. It's super scary! | 0.6479 | 平手 |
| 887 | あるんですか？堅い構えとか…。 | Is there one? Like a stiff stance or something... | 0.7913 | Is there one? Like a stiff stance or something... | 0.7913 | 平手 |
| 888 | タッチしなきゃいけないんですけど | I have to touch it, but... | 0.7524 | I have to touch it, but... | 0.7524 | 平手 |
| 889 | 今のもよく見たら分かるんですけど | If you look closely at what just happened, you'll understand. | 0.5715 | If you look closely at what just happened, you'll understand. | 0.5715 | 平手 |
| 890 | タッチされる瞬間にこっちが力を抜くっていうのが | The trick is for me to relax my muscles the moment you touch me. | 0.5346 | The trick is for me to relax my muscles the moment you touch me. | 0.5346 | 平手 |
| 891 | コツなんです。 | It's all about technique. | 0.4567 | It's all about technique. | 0.4567 | 平手 |
| 892 | こっちが力でがっといっちゃうと | If I push too hard with brute force... | 0.4434 | If I push too hard with brute force... | 0.4434 | 平手 |
| 893 | カウンターでこっちのどこかが壊れます。 | Something over here will break at the counter. | 0.7792 | Something over here will break at the counter. | 0.7792 | 平手 |
| 894 | 足首骨折した | I broke my ankle. | 0.7168 | I broke my ankle. | 0.7168 | 平手 |
| 895 | キャッチャーもいます。踏ん張りすぎて。 | There's also a catcher. He's bracing himself too hard. | 0.7831 | There's also a catcher. He's bracing himself too hard. | 0.7831 | 平手 |
| 896 | 当たる瞬間、タッチはいかないといけないんですけど | At the moment of impact, you have to make contact, but... | 0.6976 | At the moment of impact, you have to make contact, but... | 0.6976 | 平手 |
| 897 | ちょっと体を抜くんです。だから２〜３ｍ飛んでるんですけど。 | I'm pulling my body back slightly. That's why I'm flying about 2-3 meters. | 0.8755 | I'm pulling my body back slightly. That's why I'm flying about 2-3 meters. | 0.8755 | 平手 |
| 898 | でも、すぐ立ち上がってるのもそんなに痛くないというか | But the fact that I can stand up right away means it doesn't hurt that much, I guess. | 0.7179 | But the fact that I can stand up right away means it doesn't hurt that much, I guess. | 0.7179 | 平手 |
| 899 | うまく抜いてるという。≫それの練習は | He says he's pulling it out skillfully. ≫ And the practice for that... | 0.6671 | He says he's pulling it out skillfully. ≫ And the practice for that... | 0.6671 | 平手 |
| 900 | されるわけなんですか？ | Are you saying this will happen? | 0.6688 | Are you saying this will happen? | 0.6688 | 平手 |
| 901 | 練習はしてないですけどこれは１シーズンに | I haven't practiced, but this is just one season. | 0.8533 | I haven't practiced, but this is just one season. | 0.8533 | 平手 |
| 902 | 何十回…、１０回以上ありますね。 | Dozens of times... Well, more than ten times, I'd say. | 0.8562 | Dozens of times... Well, more than ten times, I'd say. | 0.8562 | 平手 |
| 903 | ちなみに普通にそのまま救急車というケースも | By the way, there are also cases where we just normally call it an ambulance. | 0.7128 | By the way, there are also cases where we just normally call it an ambulance. | 0.7128 | 平手 |
| 904 | よく当時はあったんですよ。≫勝ち気になってますから | "That used to happen quite often back then." ≫ "Because she's being feisty." | 0.5337 | "That used to happen quite often back then." ≫ "Because she's being feisty." | 0.5337 | 平手 |
| 905 | よく分かってないキャッチャーはいっちゃうんですよね。 | Catchers who don't really get it tend to rush things, you know? | 0.5093 | Catchers who don't really get it tend to rush things, you know? | 0.5093 | 平手 |
| 906 | いっちゃったらドーンとこっちもけがしちゃうので | If I go all out, I might end up hurting myself too, so... | 0.4976 | If I go all out, I might end up hurting myself too, so... | 0.4976 | 平手 |
| 907 | 当たりながら抜いて飛ばされるんですけど | I'll pass you while making contact and get blown away. | 0.6293 | I'll pass you while making contact and get blown away. | 0.6293 | 平手 |
| 908 | すぐ立ち上がって次のランナー見なきゃいけないんで。 | I have to get up right away and check on the next runner. | 0.8629 | I have to get up right away and check on the next runner. | 0.8629 | 平手 |
| 909 | あのＶＴＲ見てすごいところは僕、すぐ立ち上がって | When I watched that VTR, the amazing part was that I immediately stood up | 0.8566 | When I watched that VTR, the amazing part was that I immediately stood up | 0.8566 | 平手 |
| 910 | すぐ次のランナー抑えにいってるあれを見てほしいです。 | I want you to look at that play where they're going to stop the next runner. | 0.7477 | I want you to look at that play where they're going to stop the next runner. | 0.7477 | 平手 |
| 911 | もう１回見たい！≫もう１回いけませんか？ | I want to watch it again! ≫ Can we watch it one more time? | 0.8568 | I want to watch it again! ≫ Can we watch it one more time? | 0.8568 | 平手 |
| 912 | いよいよ自分で言い出しましたね。 | You finally said it yourself, huh? | 0.6817 | You finally said it yourself, huh? | 0.6817 | 平手 |
| 913 | 古田さんが体を張ってブロックするシーンが、こちら。 | Here's the scene where Mr. Furuta puts his body on the line to block. | 0.6841 | Here's the scene where Mr. Furuta puts his body on the line to block. | 0.6841 | 平手 |
| 914 | モスビー、これも。 | Mosby, this one too. | 0.9419 | Mosby, this one too. | 0.9419 | 平手 |
| 915 | センターなんで足の速い選手。体も１００ｋｇぐらいあって。 | He's a center player who's surprisingly fast despite weighing around 100 kg. | 0.7309 | He's a center player who's surprisingly fast despite weighing around 100 kg. | 0.7309 | 平手 |
| 916 | この時には嫌だなと思ってますよ。 | At this point, I'm thinking 'I really don't like this.' | 0.6957 | At this point, I'm thinking 'I really don't like this.' | 0.6957 | 平手 |
| 917 | 飛んですぐ立ち上がってるんですよ。 | He jumps and immediately gets back up. | 0.6574 | He jumps and immediately gets back up. | 0.6574 | 平手 |
| 918 | すげえ！≫思い切り | Wow! ≫ Give it your all! | 0.6492 | Wow! ≫ Give it your all! | 0.6492 | 平手 |
| 919 | ２ｍくらい飛ばされてるのにすぐ | Even though I was sent flying about 2 meters, I got right back up. | 0.6132 | Even though I was sent flying about 2 meters, I got right back up. | 0.6132 | 平手 |
| 920 | アウトってアピールしてすぐ立ち上がって | He appealed 'Out!' and immediately stood back up. | 0.5599 | He appealed 'Out!' and immediately stood back up. | 0.5599 | 平手 |
| 921 | １塁ランナーセカンド行こうとしてるんで、すぐ。 | The runner on first is trying to go to second, so hurry. | 0.5981 | The runner on first is trying to go to second, so hurry. | 0.5981 | 平手 |
| 922 | すげえ！ | Wow! | 0.7580 | Wow! | 0.7580 | 平手 |
| 923 | かっけえー！≫プロ！ | That's so cool! ≫ You're a pro! | 0.7548 | That's so cool! ≫ You're a pro! | 0.7548 | 平手 |
| 924 | 我々はこういうところを見ていますね。 | We're looking at places like this. | 0.8585 | We're looking at places like this. | 0.8585 | 平手 |
| 925 | 神田さんもぜひこういうところを。≫こういうところですね！ | "Mr. Kanda, you should definitely try places like this too." ≫ "Places like this, right!" | 0.5887 | "Mr. Kanda, you should definitely try places like this too." ≫ "Places like this, right!" | 0.5887 | 平手 |
| 926 | 格好良かったー！≫眼鏡取れないだけじゃ | You looked so cool! ≫ It's just that I can't take my glasses off. | 0.7911 | You looked so cool! ≫ It's just that I can't take my glasses off. | 0.7911 | 平手 |
| 927 | ないですからね。 | Because there isn't any. | 0.8544 | Because there isn't any. | 0.8544 | 平手 |
| 928 | ラスト更に強いところがあります。 | There's an even stronger part at the end. | 0.8468 | There's an even stronger part at the end. | 0.8468 | 平手 |
| 929 | 試合中に野村監督からガチ説教されてもへこたれない。 | Even if Manager Nomura gives me a serious scolding during the game, I won't let it get me down. | 0.7323 | Even if Manager Nomura gives me a serious scolding during the game, I won't let it get me down. | 0.7323 | 平手 |
| 930 | メンタル面も。 | And mentally too. | 0.7906 | And mentally too. | 0.7906 | 平手 |
| 931 | 野村監督は育てようと思ってますから | Manager Nomura is thinking about developing (players). | 0.5350 | Manager Nomura is thinking about developing (players). | 0.5350 | 平手 |
| 932 | とにかくマスコミの前とかで悪く言うんですよ。 | Anyway, they speak badly about it in front of the media. | 0.7989 | Anyway, they speak badly about it in front of the media. | 0.7989 | 平手 |
| 933 | 例えば、新人時代野村監督のコメントです。 | For example, here's a comment from Manager Nomura during his rookie days. | 0.7752 | For example, here's a comment from Manager Nomura during his rookie days. | 0.7752 | 平手 |
| 934 | 古田は肩は一流 | Furuta has a first-rate throwing arm. | 0.5093 | Furuta has a first-rate throwing arm. | 0.5093 | 平手 |
| 935 | 打撃は二流リードは三流っつってるんです。 | They say my batting is second-rate and my leadership is third-rate. | 0.5900 | They say my batting is second-rate and my leadership is third-rate. | 0.5900 | 平手 |
| 936 | 厳しいんです。 | It's tough. | 0.8010 | It's tough. | 0.8010 | 平手 |
| 937 | そんな古田選手をキャッチャーとして | With veteran player Furuta as catcher | 0.5951 | With veteran player Furuta as catcher | 0.5951 | 平手 |
| 938 | 一流に育てたかったので | I wanted to raise you to be first-class. | 0.7421 | I wanted to raise you to be first-class. | 0.7421 | 平手 |
| 939 | とにかく１プレー１プレーガチ説教して | Anyway, I'll seriously lecture you play by play. | 0.6144 | Anyway, I'll seriously lecture you play by play. | 0.6144 | 平手 |
| 940 | それがもうテレビに抜かれるんです。 | That's already going to be scooped by TV. | 0.8054 | That's already going to be scooped by TV. | 0.8054 | 平手 |
| 941 | あとでじゃないんです。 | It can't wait until later. | 0.6429 | It can't wait until later. | 0.6429 | 平手 |
| 942 | どんなことで怒られましたか？ | What did you get scolded for? | 0.8255 | What did you get scolded for? | 0.8255 | 平手 |
| 943 | 例えば、僕がキャッチャーでサインだすんで | For example, I'm the catcher giving signs. | 0.7689 | For example, I'm the catcher giving signs. | 0.7689 | 平手 |
| 944 | ストレートのサインを出して打たれるとしたら | If I give the sign for a fastball and it gets hit... | 0.5976 | If I give the sign for a fastball and it gets hit... | 0.5976 | 平手 |
| 945 | ベンチに帰って | Go back to the bench. | 0.8112 | Go back to the bench. | 0.8112 | 平手 |
| 946 | 今のは何でストレートなんだ！つって。 | Why was that one straight?! I mean... | 0.6441 | Why was that one straight?! I mean... | 0.6441 | 平手 |
| 947 | ストレートのサインを出した根拠を示せ！って怒られるんです。 | They yell at me to explain why I called for a straight pitch! | 0.5332 | They yell at me to explain why I called for a straight pitch! | 0.5332 | 平手 |
| 948 | 僕も一応理由があってこの理由でストレートがいいと | I also have my reasons, and for this reason, I think being straightforward is best. | 0.7437 | I also have my reasons, and for this reason, I think being straightforward is best. | 0.7437 | 平手 |
| 949 | 思いましたって。 | I thought so. | 0.9342 | I thought so. | 0.9342 | 平手 |
| 950 | そんなもんダメに決まってんだろみたいな感じで。 | He was like 'Obviously that's no good'. | 0.4679 | He was like 'Obviously that's no good'. | 0.4679 | 平手 |
| 951 | 結果、打たれてるんでこっちもしょうがない | Well, they're hitting us hard, so there's nothing we can do about it. | 0.3531 | Well, they're hitting us hard, so there's nothing we can do about it. | 0.3531 | 平手 |
| 952 | シュンとして立たされてるっていう | They're just standing there looking all dejected. | 0.2215 | They're just standing there looking all dejected. | 0.2215 | 平手 |
| 953 | そんな感じで。≫いつも近くに | That's about it. ≫ I'm always nearby. | 0.7610 | That's about it. ≫ I'm always nearby. | 0.7610 | 平手 |
| 954 | 座られてませんでした？ | Were you sitting here? | 0.7806 | Were you sitting here? | 0.7806 | 平手 |
| 955 | 一番最初は１年生だったのでベンチの | At first, I was just a freshman so I was on the bench. | 0.7054 | At first, I was just a freshman so I was on the bench. | 0.7054 | 平手 |
| 956 | 端っこのほうだったんですけど | I was sitting near the edge though. | 0.5891 | I was sitting near the edge though. | 0.5891 | 平手 |
| 957 | 毎回呼ばれるんですよ、試合中に。おい古田！って言われて | They call out to me every time during the game. They'll be like 'Hey, Furuta!' | 0.7296 | They call out to me every time during the game. They'll be like 'Hey, Furuta!' | 0.7296 | 平手 |
| 958 | 僕もプロテクターつけて立ってるんですけど | I'm standing here wearing a protector too, but... | 0.6775 | I'm standing here wearing a protector too, but... | 0.6775 | 平手 |
| 959 | 怒られるんですよね。怒られると | I always get scolded, you know. When I get scolded... | 0.5170 | I always get scolded, you know. When I get scolded... | 0.5170 | 平手 |
| 960 | 実家の母が何でいつも怒られてんの？って。 | My mom back home was like, 'Why do you always get scolded?' | 0.7635 | My mom back home was like, 'Why do you always get scolded?' | 0.7635 | 平手 |
| 961 | 映像で抜かれちゃうから。 | Because I'll get cut from the footage. | 0.8233 | Because I'll get cut from the footage. | 0.8233 | 平手 |
| 962 | 立たされてるんで。立たされる絵面が…。 | I'm being made to stand. The sight of being forced to stand... | 0.6226 | I'm being made to stand. The sight of being forced to stand... | 0.6226 | 平手 |
| 963 | 怒られるのはしょうがないですけど | I know I'm going to get scolded, but... | 0.5088 | I know I'm going to get scolded, but... | 0.5088 | 平手 |
| 964 | 絵面を何とか避けようと思って | I was trying my best to avoid that visual. | 0.5652 | I was trying my best to avoid that visual. | 0.5652 | 平手 |
| 965 | 自分から１か月くらい経ったら近くに行って | I'll go visit nearby after about a month passes. | 0.8085 | I'll go visit nearby after about a month passes. | 0.8085 | 平手 |
| 966 | 先輩にどいてもらって | I asked my senior to move aside. | 0.4161 | I asked my senior to move aside. | 0.4161 | 平手 |
| 967 | すみません僕ここ座っていいですか？って。 | Excuse me, would it be okay if I sat here? | 0.8804 | Excuse me, would it be okay if I sat here? | 0.8804 | 平手 |
| 968 | 監督の目の前に座ってるんですよね、いつも。 | I always end up sitting right in front of the director. | 0.8610 | I always end up sitting right in front of the director. | 0.8610 | 平手 |
| 969 | そうすると監督もめっちゃ怒ってるんですけど | And then the director gets super angry about it, but... | 0.6990 | And then the director gets super angry about it, but... | 0.6990 | 平手 |
| 970 | 怒られる時は | When I'm about to get scolded | 0.6414 | When I'm about to get scolded | 0.6414 | 平手 |
| 971 | 振り返って、すみませんと。ここで立てとは言わないんです | Looking back, I'm sorry. I didn't tell you to stand here. | 0.8137 | Looking back, I'm sorry. I didn't tell you to stand here. | 0.8137 | 平手 |
| 972 | さすがに。≫皆さん、母の気持ちで | That's impressive. >> Everyone, think like a mother would. | 0.5059 | That's impressive. >> Everyone, think like a mother would. | 0.5059 | 平手 |
| 973 | 見てほしいんですけど | I want you to look at this... | 0.7164 | I want you to look at this... | 0.7164 | 平手 |
| 974 | 実際の怒られている映像ありますので | We actually have footage of him getting scolded. | 0.6087 | We actually have footage of him getting scolded. | 0.6087 | 平手 |
| 975 | 自分が故郷の母だと思って。 | Think of me as your mother back home. | 0.7670 | Think of me as your mother back home. | 0.7670 | 平手 |
| 976 | 野村監督にベンチで怒られているシーンがこちら。 | Here's the scene where Manager Nomura is yelling at him from the dugout. | 0.7237 | Here's the scene where Manager Nomura is yelling at him from the dugout. | 0.7237 | 平手 |
| 977 | 普通に、ちゃんと。≫めっちゃ説教されてる。 | "Act normal and properly." ≫ I got seriously lectured. | 0.5805 | "Act normal and properly." ≫ I got seriously lectured. | 0.5805 | 平手 |
| 978 | ありがとうございます。 | Thank you very much. | 0.7402 | Thank you very much. | 0.7402 | 平手 |
| 979 | 悲しそうな顔してたな。≫今のなんかは | You looked really sad just now. ≫About what happened earlier... | 0.6726 | You looked really sad just now. ≫About what happened earlier... | 0.6726 | 平手 |
| 980 | ミスだからしょうがないですけど | It was a mistake, so there's nothing we can do about it. | 0.3777 | It was a mistake, so there's nothing we can do about it. | 0.3777 | 平手 |
| 981 | 俺は、ここっつったのにここに投げちゃう | I told you to put it here, but you threw it here anyway. | 0.6549 | I told you to put it here, but you threw it here anyway. | 0.6549 | 平手 |
| 982 | ピッチャーもいるわけじゃないですか。 | There's also a pitcher, you know. | 0.6694 | There's also a pitcher, you know. | 0.6694 | 平手 |
| 983 | そういう時も | Even at times like that | 0.8352 | Even at times like that | 0.8352 | 平手 |
| 984 | 怒られるのは古田さんじゃないですか。 | Isn't it Mr. Furuta who's going to get scolded? | 0.5720 | Isn't it Mr. Furuta who's going to get scolded? | 0.5720 | 平手 |
| 985 | だからサインボールが来ないことって | That's why I never get any signed baseballs. | 0.6330 | That's why I never get any signed baseballs. | 0.6330 | 平手 |
| 986 | いっぱいあるんですよ。 | There are plenty of them. | 0.7235 | There are plenty of them. | 0.7235 | 平手 |
| 987 | それを例えばピッチャーが悪いみたいな言い訳をすると | If you make excuses like blaming the pitcher, for example | 0.7469 | If you make excuses like blaming the pitcher, for example | 0.7469 | 平手 |
| 988 | ピッチャーのほうからも嫌われるんですよ。 | Even the pitcher dislikes me, you know. | 0.6085 | Even the pitcher dislikes me, you know. | 0.6085 | 平手 |
| 989 | ピッチャーもプロだから | The pitcher is a pro too, you know. | 0.6708 | The pitcher is a pro too, you know. | 0.6708 | 平手 |
| 990 | 自分がミスったこと分かってますし | I know I made a mistake, and... | 0.7931 | I know I made a mistake, and... | 0.7931 | 平手 |
| 991 | 周りで見てる選手たちもプロなので、どっちが悪いかって | The other players watching are professionals too, so they can tell who's at fault. | 0.6480 | The other players watching are professionals too, so they can tell who's at fault. | 0.6480 | 平手 |
| 992 | 分かるじゃないですか。 | You understand, don't you? | 0.8488 | You understand, don't you? | 0.8488 | 平手 |
| 993 | ピッチャーのミスなのにねって分かる。 | You can tell it was the pitcher's mistake, right? | 0.6971 | You can tell it was the pitcher's mistake, right? | 0.6971 | 平手 |
| 994 | そこでキャッチャーが言い訳をするようなことをすると | If the catcher starts making excuses at that point, | 0.5875 | If the catcher starts making excuses at that point, | 0.5875 | 平手 |
| 995 | 言いたくなるんですけど自分のために言うと | I feel like saying this, but if I'm being honest... | 0.5696 | I feel like saying this, but if I'm being honest... | 0.5696 | 平手 |
| 996 | そこで関係がぎくしゃくしちゃうので | That's why things get awkward between us. | 0.5309 | That's why things get awkward between us. | 0.5309 | 平手 |
| 997 | そこで僕が監督から | That's when the manager told me | 0.6311 | That's when the manager told me | 0.6311 | 平手 |
| 998 | 説教を食らってると今度は逆に信頼を。 | Just when I'm getting lectured, now suddenly they're trusting me. | 0.5282 | Just when I'm getting lectured, now suddenly they're trusting me. | 0.5282 | 平手 |
| 999 | あいつは俺らのために頑張ってくれるって | He said he'd do his best for us. | 0.6859 | He said he'd do his best for us. | 0.6859 | 平手 |
| 1000 | 当時若かったので | I was young at the time, so | 0.8765 | I was young at the time, so | 0.8765 | 平手 |
| 1001 | そういう意味もあったので言い訳は…。 | That's part of what I meant, so I won't make excuses... | 0.6483 | That's part of what I meant, so I won't make excuses... | 0.6483 | 平手 |
| 1002 | 言い訳は絶対ダメだっていうこともあるんでね。 | There are times when making excuses is absolutely unacceptable, you know. | 0.6830 | There are times when making excuses is absolutely unacceptable, you know. | 0.6830 | 平手 |
| 1003 | でもまだ若い時にそこまですでに考えれてたんですか。 | But were you really thinking that far ahead when you were still young? | 0.8505 | But were you really thinking that far ahead when you were still young? | 0.8505 | 平手 |
| 1004 | それは考えてましたね。言い訳は絶対できない。 | I've thought about that. There's absolutely no excuse. | 0.8227 | I've thought about that. There's absolutely no excuse. | 0.8227 | 平手 |
| 1005 | ピッチャーが三振とったりしたら | When the pitcher gets a strikeout | 0.6854 | When the pitcher gets a strikeout | 0.6854 | 平手 |
| 1006 | ピッチャーがすごいみたいになるじゃないですか。 | It makes the pitcher look really impressive, doesn't it? | 0.6070 | It makes the pitcher look really impressive, doesn't it? | 0.6070 | 平手 |
| 1007 | でもダメだったらキャッチャーの責任みたいな感じなんですか。 | But if things go wrong, does it feel like it's the catcher's responsibility? | 0.8723 | But if things go wrong, does it feel like it's the catcher's responsibility? | 0.8723 | 平手 |
| 1008 | 全部じゃないですけど野村監督は特に | Not everyone, but especially Manager Nomura. | 0.7626 | Not everyone, but especially Manager Nomura. | 0.7626 | 平手 |
| 1009 | いいチームには必ずいいキャッチャーが | Every good team always has a good catcher. | 0.7844 | Every good team always has a good catcher. | 0.7844 | 平手 |
| 1010 | 出るっていうんでキャッチャーを育てなきゃ | I heard you're playing, so I've got to train the catcher. | 0.5132 | I heard you're playing, so I've got to train the catcher. | 0.5132 | 平手 |
| 1011 | 強くならない。 | I won't get stronger. | 0.8455 | I won't get stronger. | 0.8455 | 平手 |
| 1012 | 当時弱かったんです、ヤクルト。弱かったので | The Yakult team was weak back then. Because they were weak, | 0.7207 | The Yakult team was weak back then. Because they were weak, | 0.7207 | 平手 |
| 1013 | そういう気持ちがあったと思うので。 | I think I had those kinds of feelings. | 0.9052 | I think I had those kinds of feelings. | 0.9052 | 平手 |
| 1014 | 今回、古田さんから見てすごかった | This time, it was amazing from Mr. Furuta's perspective. | 0.6145 | This time, it was amazing from Mr. Furuta's perspective. | 0.6145 | 平手 |
| 1015 | レジェンド選手事前に伺っております。 | We've already contacted the legendary player in advance. | 0.6255 | We've already contacted the legendary player in advance. | 0.6255 | 平手 |
| 1016 | まずは松井選手。 | First up is player Matsui. | 0.7998 | First up is player Matsui. | 0.7998 | 平手 |
| 1017 | やっぱりゴジラ松井僕らの時は | As expected, Godzilla Matsui was our era. | 0.5025 | As expected, Godzilla Matsui was our era. | 0.5025 | 平手 |
| 1018 | 日本人で一番ホームランを打ってた選手だと思いますけど | I think he's the Japanese player who hit the most home runs. | 0.8705 | I think he's the Japanese player who hit the most home runs. | 0.8705 | 平手 |
| 1019 | 嫌だったですね、やっぱり。 | I really didn't like it, after all. | 0.7080 | I really didn't like it, after all. | 0.7080 | 平手 |
| 1020 | 読み合いに負けて長打というのは？ | What do you mean by hitting a long ball because you lost the mind game? | 0.6075 | What do you mean by hitting a long ball because you lost the mind game? | 0.6075 | 平手 |
| 1021 | 松井って、とにかく初球からバンバン打つという | Matsui, he just swings at the first pitch every time without fail. | 0.7167 | Matsui, he just swings at the first pitch every time without fail. | 0.7167 | 平手 |
| 1022 | タイプじゃなくてできるだけ変化球も見逃して | Don't just swing at fastballs - try to lay off breaking balls too when you can. | 0.4546 | Don't just swing at fastballs - try to lay off breaking balls too when you can. | 0.4546 | 平手 |
| 1023 | ストライクなかなか放ってこない人もいるんで | Some pitchers rarely throw strikes. | 0.4572 | Some pitchers rarely throw strikes. | 0.4572 | 平手 |
| 1024 | 見逃して、僕らの裏をかいていろいろやったりするというのは | They'll take advantage if we let our guard down, doing all sorts of things behind our backs. | 0.6128 | They'll take advantage if we let our guard down, doing all sorts of things behind our backs. | 0.6128 | 平手 |
| 1025 | 彼もそういうの得意だったと思いますね。 | I think he was good at that sort of thing too. | 0.9205 | I think he was good at that sort of thing too. | 0.9205 | 平手 |
