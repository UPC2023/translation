# 翻译质量评估报告 (LaBSE 语义相似度)

- 原文来源: `/home/cyw/pro/train_data/out_liquid_aft.jsonl` (input 字段)
- liquid后处理 文件: `/home/cyw/pro/train_data/out_liquid_aft.jsonl`
- liquid 文件: `/home/cyw/pro/train_data/out_liquid.jsonl`
- LaBSE 模型: `sentence-transformers/LaBSE`
- device: `cpu`

## 统计

- liquid后处理 平均得分: 0.6928
- liquid 平均得分: 0.6914
- liquid后处理 优于 liquid: 25
- liquid 优于 liquid后处理: 23
- 平手: 444
- 参与统计句子数: 492

## 明细对比表

| 序号 | 日语原文 | liquid后处理翻译 | liquid后处理得分 | liquid翻译 | liquid得分 | 优胜方 |
|---:|---|---|---:|---|---:|---|
| 1 | Event 7fe4/0420/6cc5 フジテレビ 081 | Event 7fe4/0420/6cc5 Fuji TV 081 | 0.8802 | Event 7fe4/0420/6cc5 Fuji TV 081 | 0.8802 | 平手 |
| 2 | 04/28（月）09:50:00～11:30:00 | Mon. 28th, 04/28th (Monday) 9:50:00-11:30:00 | 0.8690 | Mon. 28th, 04/28th (Monday) 9:50:00-11:30:00 | 0.8690 | 平手 |
| 3 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Non-stop! [Kobayashi Sachiko Descends on the Niconico Super Conference in a Secret Retreat▽Miura Daichi's 3 Children's Daddy's True Face]�������� | 0.7913 | Non-stop! [Kobayashi Sachiko Descends on the Niconico Super Conference in a Secret Retreat▽Miura Daichi's 3 Children's Daddy's True Face]�������� | 0.7913 | 平手 |
| 4 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | The Kimio Kobayashi Close-Up on the Nico Nico Super Conference ▽ "At One Point I Was Resigned to Death..." Isao Sasaki's Return Live ▽ Miura Daichi Studio Appearance 3 Children's Papa True Face ▽ Osamu Mukai | 0.8186 | The Kimio Kobayashi Close-Up on the Nico Nico Super Conference ▽ "At One Point I Was Resigned to Death..." Isao Sasaki's Return Live ▽ Miura Daichi Studio Appearance 3 Children's Papa True Face ▽ Osamu Mukai | 0.8186 | 平手 |
| 5 | ≫おはようございます。 | - Good morning. - Good morning. | 0.6421 | - Good morning. - Good morning. | 0.6421 | liquid |
| 6 | ≫「ノンストップ！」始まりました。 | and now the nonstop! | 0.5119 | and now the nonstop! | 0.5119 | 平手 |
| 7 | ≫今週のせきららボイスの投稿テーマは | the theme for this week's sekirara voice post is | 0.7374 | the theme for this week's sekirara voice post is | 0.7374 | 平手 |
| 8 | 思い出のＧＷです。 | It's a memorable G.W.D. | 0.7408 | It's a memorable G.W.D. | 0.7408 | 平手 |
| 9 | 表示されているＱＲコードから皆さん、ぜひ投稿してください。 | Please submit your responses to the QR codes displayed on the screen. | 0.7358 | Please submit your responses to the QR codes displayed on the screen. | 0.7358 | 平手 |
| 10 | それでは参りましょうか。 | Then shall we go then? | 0.7985 | Then shall we go then? | 0.7985 | 平手 |
| 11 | ≫４月２８日、今日も…。≫「ノンストップ！」。 | April 28th, again… "Non-stop!" | 0.7493 | April 28th, again… "Non-stop!" | 0.7493 | 平手 |
| 12 | ≫先週金曜日、「パリピ孔明ＴＨＥ　ＭＯＶＩＥ」の | - Last Friday, you appeared on "Palipi Kongmyeong THE HEP MOKE" | 0.6451 | - Last Friday, you appeared on "Palipi Kongmyeong THE HEP MOKE" | 0.6451 | 平手 |
| 13 | 初日舞台あいさつが行われ | the opening day stage greetings were given | 0.7354 | the opening day stage greetings were given | 0.7354 | 平手 |
| 14 | 向井理さん、上白石萌歌さんディーン・フジオカさん | mr. mukai rie, moka joshiraishi, and dean fusjoka | 0.6039 | mr. mukai rie, moka joshiraishi, and dean fusjoka | 0.6039 | 平手 |
| 15 | 宮野真守さんらが登場しました。 | The work featured Mamoru Miyano and others. | 0.5487 | The work featured Mamoru Miyano and others. | 0.5487 | 平手 |
| 16 | ≫音楽で戦うことになりました。≫マジで！？ | We ended up fighting with music. Seriously!? | 0.7400 | We ended up fighting with music. Seriously!? | 0.7400 | 平手 |
| 17 | ≫向井さん演じる諸葛孔明が現代に転生し | mr. mukai's character zhuge kongming is reincarnated in the present day | 0.6220 | mr. mukai's character zhuge kongming is reincarnated in the present day | 0.6220 | 平手 |
| 18 | 上白石さん演じるアマチュアシンガー、英子の | the amateur singer, eiko, played by joshiraishi mr. | 0.6642 | the amateur singer, eiko, played by joshiraishi mr. is a professional translator | 0.7341 | liquid |
| 19 | 軍師となって音楽の力で天下泰平を目指す | I will become a strategist and use the power of music to bring peace to the world. | 0.6011 | I will become a strategist and use the power of music to bring peace to the world. | 0.6011 | 平手 |
| 20 | ド派手エンターテインメント映画です。 | It's a flashy entertainment movie. | 0.8564 | It's a flashy entertainment movie. | 0.8564 | liquid后处理 |
| 21 | 「ノンストップ！」は向井さんや上白石さんら | 'Nonstop!' , including Mukai and Kamishiraishi. | 0.6848 | 'Nonstop!' is a professional translator, including Mukai and Kamishiraishi. | 0.6222 | liquid后处理 |
| 22 | 出演者４人に直撃しました。 | The four performers were directly hit. I got hit by four people. | 0.7054 | The four performers were directly hit. I got hit by four people. | 0.7054 | 平手 |
| 23 | ≫見どころの１つがライブシーン。 | One of the highlights is the live scene. | 0.8416 | One of the highlights is the live scene. | 0.8416 | 平手 |
| 24 | 本人役で岩田剛典さんや水森かおりさんなど | The actors include Takanori Iwata and Kaori Mizumori, all playing themselves. | 0.6546 | The actors include Takanori Iwata and Kaori Mizumori, all playing themselves. | 0.6546 | 平手 |
| 25 | 総勢５０人以上のミュージシャンらが | A group of over 50 musicians came together to create this piece. | 0.6644 | A group of over 50 musicians came together to create this piece. | 0.6644 | 平手 |
| 26 | 出演していることでも話題を呼んでいます。 | The fact that he appeared on the show has also generated a lot of buzz. | 0.5674 | The fact that he appeared on the show has also generated a lot of buzz. | 0.5674 | 平手 |
| 27 | そこで、パリピな映画にちなんで | and so, in reference to the movie parliaments, we decided to make a professional translation | 0.4899 | and so, in reference to the movie parliaments, we decided to make a professional translation | 0.4899 | 平手 |
| 28 | 向井さんたちが最もテンションアゲアゲになった | the mukai's got the most excited outbursts | 0.6261 | the mukai's got the most excited outbursts | 0.6261 | 平手 |
| 29 | 出演アーティストを聞いてみると…。 | I looked up the artists featured... | 0.7481 | I looked up the artists featured... | 0.7481 | 平手 |
| 30 | ≫すると、ディーンさんから意外な事実が。 | and then mr. dean made an unexpected revelation. | 0.6641 | and then mr. dean made an unexpected revelation. | 0.6641 | 平手 |
| 31 | ≫一方、プライベートでの４人は | The four members in private, however, | 0.7364 | The four members in private, however, | 0.7364 | 平手 |
| 32 | どんな時にテンションが上がるのでしょうか。 | When do you get excited? What makes you get excited? | 0.7414 | When do you get excited? What makes you get excited? | 0.7414 | 平手 |
| 33 | ≫Ｔｈｅ　ＣｕｒｅっていうＵＫの | The UK's UK-based company T-Her-Curse is called T-Her-Curse. | 0.2660 | The UK's UK-based company T-Her-Curse is called T-Her-Curse. | 0.2660 | 平手 |
| 34 | レジェンドバンドが私大好きでして。 | and i love my university to be a legend. | 0.4299 | and i love my university to be a legend. | 0.4299 | 平手 |
| 35 | ≫向井理も…。≫上白石萌歌も…。 | Mukai Osamu also…? Ueshiraishi Moka also…? | 0.6226 | Mukai Osamu also…? Ueshiraishi Moka also…? | 0.6226 | 平手 |
| 36 | ≫ディーン・フジオカも…。≫宮野真守も…。 | Dean Fujioka too…? Mamoru Miyano too…? | 0.7898 | Dean Fujioka too…? Mamoru Miyano too…? | 0.7898 | liquid |
| 37 | ≫「ノンストップ！」。 | and nonstop! | 0.5501 | and nonstop! | 0.5501 | 平手 |
| 38 | ≫昨日、ミュージカル「キンキーブーツ」の | yesterday, we watched a performance of the musical "The Kinky Boots" | 0.7369 | yesterday, we watched a performance of the musical "The Kinky Boots" | 0.7369 | 平手 |
| 39 | 初日公演が行われました。 | The opening day performance was held. | 0.8315 | The opening day performance was held. | 0.8315 | 平手 |
| 40 | アメリカの演劇界で最も権威のあるトニー賞で | the most prestigious tony awards ceremony in american theatre | 0.8239 | the most prestigious tony awards ceremony in american theatre | 0.8239 | 平手 |
| 41 | 作品賞を含む６冠を達成したミュージカル。 | The musical has won six awards, including Best Picture. | 0.7877 | The musical has won six awards, including Best Picture. | 0.7877 | 平手 |
| 42 | カーテンコールでは音楽・作詞担当の | the curtain call features the composer and lyricist | 0.6124 | the curtain call features the composer and lyricist | 0.6124 | 平手 |
| 43 | 世界的歌姫にして大の親日家としても知られる | a world-renowned songstress and known as a great Japanophile | 0.7695 | a world-renowned songstress and known as a great Japanophile | 0.7695 | 平手 |
| 44 | シンディ・ローパーがサプライズ出演。 | Cindy Roeper makes a surprise appearance. | 0.7124 | Cindy Roeper makes a surprise appearance. | 0.7124 | 平手 |
| 45 | ステージに花を添えました。 | and we've added some flowers to the stage. | 0.7172 | and we've added some flowers to the stage. | 0.7172 | liquid后处理 |
| 46 | ≫しみじみと語るのは「宇宙戦艦ヤマト」など | the things that I'm really talking about are things like space battleship yamato | 0.5643 | the things that I'm really talking about are things like space battleship yamato | 0.5643 | 平手 |
| 47 | 数々の伝説的アニソンを歌ってきた | and sang many legendary anime songs | 0.7795 | and sang many legendary anime songs | 0.7795 | 平手 |
| 48 | アニソン界の大王ことささきいさおさん、８２歳。 | The King of the Anime Song World, Mr. Isao Sasaki, 82 years old. | 0.7764 | The King of the Anime Song World, Mr. Isao Sasaki, 82 years old. | 0.7764 | 平手 |
| 49 | 昨日、都内で行われたアニソンイベントに | i attended an anime song event held in tokyo yesterday | 0.7146 | i attended an anime song event held in tokyo yesterday | 0.7146 | 平手 |
| 50 | 出演したのです。 | and so i appeared on the show. | 0.5487 | and so i appeared on the show. | 0.5487 | 平手 |
| 51 | ≫ありがとう！ | - Thank you! | 0.7486 | - Thank you! | 0.7486 | 平手 |
| 52 | ≫実はささきさん、今年１月 | actually, sasakisan went to work as a professional translator this january | 0.5093 | actually, sasakisan went to work as a professional translator this january | 0.5093 | 平手 |
| 53 | 地下鉄に乗っている時に突如、気絶。 | I suddenly lost consciousness while riding the subway. | 0.8295 | I suddenly lost consciousness while riding the subway. | 0.8295 | 平手 |
| 54 | その後、自力で自宅まで戻るも救急搬送。 | After that, he returned home on his own but was rushed to the hospital by ambulance. | 0.7910 | After that, he returned home on his own but was rushed to the hospital by ambulance. | 0.7910 | 平手 |
| 55 | 医師から間質性肺炎急性増悪と診断され、入院していました。 | The doctor diagnosed my condition as acute exacerbation of interstitial pneumonia and I was hospitalized. | 0.8091 | The doctor diagnosed my condition as acute exacerbation of interstitial pneumonia and I was hospitalized. | 0.8091 | 平手 |
| 56 | 退院後も自宅療養とリハビリ生活を | and continue to live at home and undergo rehabilitation after being discharged | 0.7498 | and continue to live at home and undergo rehabilitation after being discharged | 0.7498 | 平手 |
| 57 | 送っていたという、ささきさん。 | Sasakisan said you were sending it. | 0.7785 | Sasakisan said you were sending it. | 0.7785 | 平手 |
| 58 | どういう症状だったのでしょうか。 | What kind of symptoms were you experiencing? | 0.8623 | What kind of symptoms were you experiencing? | 0.8623 | 平手 |
| 59 | ≫一般的に血液中に含まれる酸素の量が | in general, the amount of oxygen in the blood | 0.8502 | in general, the amount of oxygen in the blood | 0.8502 | 平手 |
| 60 | ９０％を切ったら危ないといわれているところ | It's said that if it falls below 90%, it's dangerous. | 0.7741 | It's said that if it falls below 90%, it's dangerous. | 0.7741 | liquid后处理 |
| 61 | 診察時、何と５０％しかなかったという、ささきさん。 | Sasaki said that only 50% of what she was able to translate at the time of the examination actually came out. | 0.6751 | Sasaki said that only 50% of what she was able to translate at the time of the examination actually came out. | 0.6751 | 平手 |
| 62 | 一時は死を覚悟したといいます。 | and at one point he was prepared to die. | 0.6347 | and at one point he was prepared to die. | 0.6347 | 平手 |
| 63 | ≫しゃべるのも苦しかった中 | and it was hard for me to talk too | 0.7309 | and it was hard for me to talk too | 0.7309 | 平手 |
| 64 | まさに奇跡の復活を遂げたささきさん。 | It was truly a miracle that Sasaki-san had achieved such a miraculous resurrection. | 0.7274 | It was truly a miracle that Sasaki-san had achieved such a miraculous resurrection. | 0.7274 | 平手 |
| 65 | 昨日のライブではロボットアニメの主題歌４曲を | - We played four songs from the robot anime theme song for our show yesterday. - No explanations or extra commentary, just the translation. | 0.6543 | - We played four songs from the robot anime theme song for our show yesterday. - No explanations or extra commentary, just the translation. | 0.6543 | 平手 |
| 66 | およそ２０００人の観客の前で熱唱しました。 | I sang passionately in front of an audience of about 2,000 people. | 0.8371 | I sang passionately in front of an audience of about 2,000 people. | 0.8371 | 平手 |
| 67 | そんな、ささきさんの今のささやかな楽しみは…。 | And what a small pleasure Sasaki has now...? | 0.7279 | And what a small pleasure Sasaki has now...? | 0.7279 | 平手 |
| 68 | ≫大好きなお酒を楽しめるまで回復したようです。 | and seems to have recovered enough to enjoy my favorite alcoholic beverages. | 0.7711 | and seems to have recovered enough to enjoy my favorite alcoholic beverages. | 0.7711 | 平手 |
| 69 | ≫生涯現役宣言。 | he declares himself to be active throughout his life. | 0.4994 | he declares himself to be active throughout his life. | 0.4994 | 平手 |
| 70 | 今年７月にはデビュー６５周年記念イベントも | This July, we will also hold a 65th anniversary event to commemorate our debut. | 0.7960 | This July, we will also hold a 65th anniversary event to commemorate our debut. | 0.7960 | 平手 |
| 71 | 控えているということで | and since you're holding onto it | 0.5300 | and since you're holding onto it | 0.5300 | 平手 |
| 72 | パワフルな歌声をまだまだ聴かせてくれそうです。 | and she's still going to give off a powerful voice. | 0.6632 | and she's still going to give off a powerful voice. | 0.6632 | 平手 |
| 73 | 優勝はガクテンソク！ | The champion goes to Gakuten Sokku! | 0.6816 | The champion goes to Gakuten Sokku! | 0.6816 | 平手 |
| 74 | ≫結成１６年以上のベテラン漫才師たちが | The veteran manzai performers who have been active for over 16 years have decided to form a group | 0.6213 | The veteran manzai performers who have been active for over 16 years have decided to form a group | 0.6213 | 平手 |
| 75 | セカンドチャンスをかけて戦う賞レース | a race for the very first chance! | 0.5027 | a race for the very first chance! | 0.5027 | 平手 |
| 76 | ３回目の開催となる今年 | This year, the third time the event has been held, we have been working with professional translators. | 0.5097 | This year, the third time the event has been held, we have been working with professional translators. | 0.5097 | 平手 |
| 77 | グランプリファイナルに勝ち上がった８組が | The eight teams that advanced to the Grand Prix Final will compete in the Grand Prix Final. | 0.6573 | The eight teams that advanced to the Grand Prix Final will compete in the Grand Prix Final. | 0.6573 | 平手 |
| 78 | 組み合わせ抽選会を行いました。 | The combination draw was held. | 0.8040 | The combination draw was held. | 0.8040 | 平手 |
| 79 | １回戦の注目カードは結成５３年 | The featured matchup of the first round is the 53-year-old team. | 0.6230 | The featured matchup of the first round is the 53-year-old team. | 0.6230 | 平手 |
| 80 | 昭和の漫才ブームの一翼を担った、ザ・ぼんちと | the Bonchi, who played a part in the manzai boom of the shōwa era | 0.6326 | the Bonchi, who played a part in the manzai boom of the shōwa era | 0.6326 | 平手 |
| 81 | ３回連続グランプリファイナル出場の | - You've qualified for the Grand Prix Final three times in a row. | 0.7167 | - You've qualified for the Grand Prix Final three times in a row. | 0.7167 | liquid后处理 |
| 82 | 金属バットが激突。 | a metal bat hits you. | 0.7424 | a metal bat hits you. | 0.7424 | 平手 |
| 83 | ≫レジェンドのザ・ぼんちの快進撃なるか？ | do you think the legendary z the bonchi's on a roll? | 0.4295 | do you think the legendary z the bonchi's on a roll? | 0.4295 | 平手 |
| 84 | グランプリファイナルは来月１７日放送予定です。 | The Grand Prix Final is scheduled to air on the 17th of next month. | 0.8834 | The Grand Prix Final is scheduled to air on the 17th of next month. | 0.8834 | 平手 |
| 85 | ≫５歳の女の子も７０代のご婦人も | A five-year-old girl and a woman in her 70s are both translating texts. | 0.6380 | A five-year-old girl and a woman in her 70s are both translating texts. | 0.6380 | 平手 |
| 86 | 満面の笑みにさせていたのは | and the thing that made me smile so hard was that i was able to translate | 0.5060 | and the thing that made me smile so hard was that i was able to translate | 0.5060 | 平手 |
| 87 | 先週金曜日からゴールデンウィークに合わせて | and since last friday, we've been working on this for golden week | 0.5939 | and since last friday, we've been working on this for golden week | 0.5939 | 平手 |
| 88 | 開催されている | The event is underway. | 0.5628 | The event is underway. | 0.5628 | 平手 |
| 89 | 「アイスクリーム万博」通称「あいぱく」。 | The "Ice Cream Expo," also known as "Aipaku." | 0.7777 | The "Ice Cream Expo," also known as "Aipaku." | 0.7777 | 平手 |
| 90 | 今回で１０周年。 | This is the 10th anniversary. | 0.8061 | This is the 10th anniversary. | 0.8061 | 平手 |
| 91 | 累計来場者数４４０万人を超える | The cumulative number of visitors exceeds 440,000. | 0.7901 | The cumulative number of visitors exceeds 440,000. | 0.7901 | 平手 |
| 92 | 国内最大級のアイスクリームイベントで | the largest ice cream event in the country | 0.8648 | the largest ice cream event in the country | 0.8648 | liquid |
| 93 | 全国のアイスマニアが厳選したアイスを | an ice cream carefully selected by ice maniacs across the country | 0.7977 | an ice cream carefully selected by ice maniacs across the country | 0.7977 | 平手 |
| 94 | １８０種類以上食べられるんです。 | I can eat over 180 different kinds of food. | 0.8800 | I can eat over 180 different kinds of food. | 0.8800 | 平手 |
| 95 | 場内を回っていると…。 | As I walked around the stadium... | 0.7865 | As I walked around the stadium... | 0.7865 | 平手 |
| 96 | ≫突然、ダッシュで列を作るお客さん。 | and suddenly a customer is running up the line in a dashboard. | 0.6237 | and suddenly a customer is running up the line in a dashboard. | 0.6237 | 平手 |
| 97 | ≫この、突如できた行列の正体。 | the identity of this suddenly formed procession. | 0.5511 | the identity of this suddenly formed procession. | 0.5511 | 平手 |
| 98 | 実は、まだ発売前の新商品を無料配布していたんです。 | I was actually giving away pre-release new products for free. | 0.8972 | I was actually giving away pre-release new products for free. | 0.8972 | liquid |
| 99 | ≫無料アイスまでもらえる | I can even get a free ice cream. | 0.6317 | I can even get a free ice cream. | 0.6317 | 平手 |
| 100 | ファンにはたまらないこのイベント。 | This event is something fans will absolutely love. | 0.8175 | This event is something fans will absolutely love. | 0.8175 | 平手 |
| 101 | 監修するのは年間１０００種類以上の | The project is supervised by over 1,000 translators a year. | 0.6771 | The project is supervised by over 1,000 translators a year. | 0.6771 | 平手 |
| 102 | アイスを食べる専門家アイスマン福留さん。 | The ice cream expert, Mr. Fukudome, is an expert at eating ice cream. | 0.6673 | The ice cream expert, Mr. Fukudome, is an expert at eating ice cream. | 0.6673 | liquid |
| 103 | ≫ということで厳選に厳選を重ねた、全国のアイスの中でも | and so we carefully selected the ice cream from all over the country | 0.6503 | and so we carefully selected the ice cream from all over the country | 0.6503 | 平手 |
| 104 | アイスマン福留さんが特にオススメする | The Iceman Fukudome particularly recommends this translation: | 0.6435 | The Iceman Fukudome particularly recommends this translation: | 0.6435 | 平手 |
| 105 | ２品を、ご紹介します。 | I'd like to introduce two dishes to you. | 0.7415 | I'd like to introduce two dishes to you. | 0.7415 | 平手 |
| 106 | 最初は一見、普通なソフトクリーム。 | At first glance, it looks like normal soft-serve ice cream. | 0.8153 | At first glance, it looks like normal soft-serve ice cream. | 0.8153 | 平手 |
| 107 | しかし、口にすると…。 | But when I say it... | 0.8741 | But when I say it... | 0.8741 | 平手 |
| 108 | ≫ふわふわな口当たりに驚く人が続出していたのが | and many people were surprised by the fluffy texture | 0.5588 | and many people were surprised by the fluffy texture | 0.5588 | 平手 |
| 109 | 北海道の人気店、ましゅれのジャージー牛乳ソフト。 | The popular shop in Hokkaido, Mashure no Jersey Milk Soft serve Jersey Milk Soft serve. | 0.8014 | The popular shop in Hokkaido, Mashure no Jersey Milk Soft serve Jersey Milk Soft serve. | 0.8014 | 平手 |
| 110 | 地元のジャージーミルクと砂糖のみで作ったソフトクリーム。 | A soft-serve ice cream made only with local jersey milk and sugar. | 0.8678 | A soft-serve ice cream made only with local jersey milk and sugar. | 0.8678 | 平手 |
| 111 | ふわふわ感を出す秘密が…。 | The secret to creating that fluffy feel… is… | 0.7664 | The secret to creating that fluffy feel… is… | 0.7664 | 平手 |
| 112 | こちら、世界最高峰のソフトクリームマシン。 | This is the world's most advanced soft-serve ice cream machine. | 0.7667 | This is the world's most advanced soft-serve ice cream machine. | 0.7667 | 平手 |
| 113 | お値段は何とおよそ３００万円！ | The price is about 3 million yen! | 0.8609 | The price is about 3 million yen! | 0.8609 | 平手 |
| 114 | その高級さと、イタリアで生産されていることから | and because it's so expensive and made in italy | 0.7656 | and because it's so expensive and made in italy | 0.7656 | 平手 |
| 115 | ソフトクリーム界のフェラーリと呼ばれているんです。 | and they're called the ferrari of soft serve ice cream. | 0.7007 | and they're called the ferrari of soft serve ice cream. | 0.7007 | 平手 |
| 116 | 最大の特徴はきめの細かい気泡で | and the most distinctive feature is the fine grain of the bubbles | 0.7421 | and the most distinctive feature is the fine grain of the bubbles | 0.7421 | 平手 |
| 117 | ふわっふわな食感のソフトクリームを作れること。 | The ability to create soft ice cream with a fluffy texture. | 0.7216 | The ability to create soft ice cream with a fluffy texture. | 0.7216 | 平手 |
| 118 | アイスの口当たりを決める空気の量を | the amount of air that determines the texture of ice cream | 0.7819 | the amount of air that determines the texture of ice cream | 0.7819 | 平手 |
| 119 | 素材に合わせて絶妙に調整できるため | and because it can be perfectly adjusted to match the material | 0.7864 | and because it can be perfectly adjusted to match the material | 0.7864 | liquid后处理 |
| 120 | この食感を生み出せるんです。 | and we can create this texture. | 0.6503 | and we can create this texture. | 0.6503 | liquid |
| 121 | ≫一方こちらは何やら、ぷつぷつしたものが | and on the other hand, something like a shaky shaky object | 0.6191 | and on the other hand, something like a shaky shaky object | 0.6191 | 平手 |
| 122 | 練り込まれているアイス。 | The ice cream is well-crafted. | 0.5036 | The ice cream is well-crafted. | 0.5036 | 平手 |
| 123 | ≫お客さんが感じた甘じょっぱさ。 | The sweetness and saltyness that the customer felt. | 0.6911 | The sweetness and saltyness that the customer felt. | 0.6911 | 平手 |
| 124 | 実はこれ、ベーコンが練り込まれたアイスなんです。 | This is actually a bacon-infused ice cream. | 0.8863 | This is actually a bacon-infused ice cream. | 0.8863 | 平手 |
| 125 | これを作ったのは、横須賀市の人気アイスクリームパーラー。 | The ice cream parlor in Yokosuka City created this. | 0.7708 | The ice cream parlor in Yokosuka City created this. | 0.7708 | 平手 |
| 126 | 店主がアメリカで食べたメープルシロップと | the owner ate maple syrup in america | 0.7770 | the owner ate maple syrup in america | 0.7770 | 平手 |
| 127 | ベーコン、ドーナツを組み合わせた | and i combined bacon and donuts | 0.7029 | and i combined bacon and donuts | 0.7029 | 平手 |
| 128 | 甘じょっぱい料理から着想を得たそうです。 | It seems to have been inspired by sweet and salty dishes. | 0.7592 | It seems to have been inspired by sweet and salty dishes. | 0.7592 | 平手 |
| 129 | ≫世界最高峰のソフトクリームから | from the world's finest soft serve ice cream | 0.7383 | from the world's finest soft serve ice cream | 0.7383 | 平手 |
| 130 | 変わり種アイスまで楽しめる「あいぱく」。 | The “Aipaku” offers even the most unusual kinds of ice cream. | 0.6493 | The “Aipaku” offers even the most unusual kinds of ice cream. | 0.6493 | liquid后处理 |
| 131 | そして、アイス好きの夢である | and my dream of being an ice enthusiast | 0.8357 | and my dream of being an ice enthusiast | 0.8357 | 平手 |
| 132 | あれ食べてみたいですねふわふわするソフトクリーム。 | I'd really like to try that fluffy soft-serve ice cream. | 0.7745 | I'd really like to try that fluffy soft-serve ice cream. | 0.7745 | 平手 |
| 133 | ≫どんな感じなんですかねちょっと、想像が…。 | I wonder what it feels like, just a little… I can’t quite picture it… | 0.6152 | I wonder what it feels like, just a little… I can’t quite picture it… | 0.6152 | liquid |
| 134 | ≫あそこ会場行く人って何個も食べるんですかね。 | i wonder how many people there are going to the venue who will eat so many things. | 0.6891 | i wonder how many people there are going to the venue who will eat so many things. | 0.6891 | 平手 |
| 135 | ≫アイスしかないですもんね「あいぱく」は。 | the ice cream's all we got... "Aipaku"? | 0.5737 | the ice cream's all we got... "Aipaku"? | 0.5737 | 平手 |
| 136 | ≫大好きな人は何個も何個も食べてね。 | and eat as many pieces as you like. | 0.5592 | and eat as many pieces as you like. | 0.5592 | 平手 |
| 137 | ≫お土産でも買って帰れそうですね。 | i could probably buy some souvenirs for you too. | 0.6752 | i could probably buy some souvenirs for you too. | 0.6752 | 平手 |
| 138 | ≫そんな「あいぱく」ですが | but that kind of "aipaku" | 0.6680 | but that kind of "aipaku" | 0.6680 | 平手 |
| 139 | 食べ比べされている方多かったんですね。 | So a lot of people were comparing the tastes of the foods. | 0.6426 | So a lot of people were comparing the tastes of the foods. | 0.6426 | 平手 |
| 140 | そして皆さんにもぜひ食べ比べ楽しんでいただきたいです。 | And I really hope that you will enjoy comparing the flavors with everyone. | 0.7236 | And I really hope that you will enjoy comparing the flavors with everyone. | 0.7236 | 平手 |
| 141 | 今回はイベントを監修するアイスマン福留さんイチ押し | This time, we have Iceman Fukudome, who oversees the event, as our main translator. | 0.6731 | This time, we have Iceman Fukudome, who oversees the event, as our main translator. | 0.6731 | 平手 |
| 142 | 桃の食べ比べアイススタジオにご用意しました。 | We prepared it for Peach Food Tasting Ice Studio. | 0.7846 | We prepared it for Peach Food Tasting Ice Studio. | 0.7846 | 平手 |
| 143 | 食べ比べるのは山梨県の農家さんが作っている | The farmers in Yamanashi Prefecture are making it for you to compare the two. | 0.6383 | The farmers in Yamanashi Prefecture are making it for you to compare the two. | 0.6383 | liquid |
| 144 | ６種類の桃のジェラートの中から２種類。 | You can choose from two types of gelato with six different peach flavors. | 0.7156 | You can choose from two types of gelato with six different peach flavors. | 0.7156 | 平手 |
| 145 | 特に人気の高かった夏かんろ、黄金桃。 | The most popular summer fruits, golden peaches, were especially popular. | 0.8508 | The most popular summer fruits, golden peaches, were especially popular. | 0.8508 | 平手 |
| 146 | まずは皆さん、夏かんろからいってらっしゃいませ。 | First off, everyone, please get ready for summer. | 0.7693 | First off, everyone, please get ready for summer. | 0.7693 | 平手 |
| 147 | ≫おいしい！うわ、すごい桃！ | It's delicious! Wow, that's a amazing peach! | 0.8183 | It's delicious! Wow, that's a amazing peach! | 0.8183 | 平手 |
| 148 | ≫果肉も入ってますね！ | The flesh is also included! | 0.7506 | The flesh is also included! | 0.7506 | 平手 |
| 149 | ≫食べた瞬間は桃のアイスだなって感じするけど | the moment you eat it, it feels like peach ice cream, but | 0.7943 | the moment you eat it, it feels like peach ice cream, but | 0.7943 | 平手 |
| 150 | そのあとに、ぐわっと桃の香りが。すっごいおいしい！ | And then, just a hint of peach aroma. It's amazingly delicious! | 0.8242 | And then, just a hint of peach aroma. It's amazingly delicious! | 0.8242 | 平手 |
| 151 | めちゃくちゃうまい、これ。 | this is seriously delicious! | 0.7503 | this is seriously delicious! | 0.7503 | 平手 |
| 152 | ≫１００％全力の桃果肉の食感を残したジェラートで | - With gelato retaining the texture of 100% fully-focused peach flesh. | 0.7075 | - With gelato retaining the texture of 100% fully-focused peach flesh. | 0.7075 | 平手 |
| 153 | ねっとりした食感が最大の特徴ということです。 | The most distinctive feature is its sticky texture. | 0.7105 | The most distinctive feature is its sticky texture. | 0.7105 | 平手 |
| 154 | これが夏かんろでした。 | and this was the summer flood. | 0.7591 | and this was the summer flood. | 0.7591 | 平手 |
| 155 | 続いて、黄金桃のほうも楽しんでいただきたいです。 | And I hope you enjoy the golden peach too. | 0.8008 | And I hope you enjoy the golden peach too. | 0.8008 | 平手 |
| 156 | こちら、桃農家さんによりますとジューシーな甘みとうまみが特徴。 | This peach farmer's peach is characterized by its juicy sweetness and umami flavor. Only the translation is output . | 0.6037 | This peach farmer's peach is characterized by its juicy sweetness and umami flavor. Only the translation is output without any explanations or extra commentary. | 0.5812 | liquid后处理 |
| 157 | 皆さん、お願いいたします。召し上がれ。 | Please, everyone, I beg you. Have a meal. | 0.8118 | Please, everyone, I beg you. Have a meal. | 0.8118 | 平手 |
| 158 | ≫あっ、違う。あー！おいしい！こっちもうまい。 | Oh, no, no! Oh! It's delicious! It's good here! | 0.7619 | Oh, no, no! Oh! It's delicious! It's good here! | 0.7619 | 平手 |
| 159 | ちょっと違いますね。 | It's a little different. | 0.9012 | It's a little different. | 0.9012 | 平手 |
| 160 | ≫夏かんろの桃感がすごかったから | 'because the feeling of the summer sun over my peach skin was amazing | 0.6786 | 'because the feeling of the summer sun over my peach skin was amazing | 0.6786 | 平手 |
| 161 | ちょっとあっさりには思えるよね。 | It might seem a bit casual, you know. | 0.7183 | It might seem a bit casual, you know. | 0.7183 | 平手 |
| 162 | ≫何だろう、こっちのほうがいわゆる缶詰なんかに入ってた | i wonder what it is? it was in a kind of canned food here | 0.6119 | i wonder what it is? it was in a kind of canned food here | 0.6119 | 平手 |
| 163 | 黄色いもの…。あっ、おいしい！ | The yellow one… oh, it’s delicious! | 0.9085 | The yellow one… oh, it’s delicious! | 0.9085 | 平手 |
| 164 | ≫迷う！≫夏かんろ、うまいな。 | I'm lost! Summer is so delicious! | 0.7134 | I'm lost! Summer is so delicious! | 0.7134 | 平手 |
| 165 | 夏かんろ、最初に食べたからかインパクトが。 | the summer yam soup had an impact because i ate it first. | 0.7593 | the summer yam soup had an impact because i ate it first. | 0.7593 | 平手 |
| 166 | ≫桃に関しては６種類ありますからね。 | and there are six different kinds of peaches. | 0.7355 | and there are six different kinds of peaches. | 0.7355 | 平手 |
| 167 | ≫じゃあ食べ比べこれこそ本当にね。 | then this is really the best food comparison i've ever seen. | 0.5590 | then this is really the best food comparison i've ever seen. | 0.5590 | 平手 |
| 168 | ≫ぜひとも皆さんに行っていただきたいです。 | We would definitely encourage everyone to take a look. | 0.3774 | We would definitely encourage everyone to take a look. | 0.3774 | 平手 |
| 169 | 大人気の「あいぱく」来月６日までやっています。 | The hugely popular "Aipaku" is running until the 6th of next month. | 0.8966 | The hugely popular "Aipaku" is running until the 6th of next month. | 0.8966 | 平手 |
| 170 | ゴールデンウィーク中に足を運んでみては | and why don't you come visit during golden week | 0.5384 | and why don't you come visit during golden week | 0.5384 | 平手 |
| 171 | いかがでしょうか。≫続いては歌手の小林幸子さん。 | and here comes the singer, kobayashi Sachiko. | 0.5213 | and here comes the singer, kobayashi Sachiko. | 0.5213 | 平手 |
| 172 | この週末に行われた大規模イベント出演に密着です。 | It follows the appearance of a large-scale event held this weekend. | 0.7501 | It follows the appearance of a large-scale event held this weekend. | 0.7501 | 平手 |
| 173 | 分け隔てなく若者と接する神対応ぶりが見えてきました。 | It became apparent how God treats young people without discrimination. | 0.7486 | It became apparent how God treats young people without discrimination. | 0.7486 | 平手 |
| 174 | ≫昨日、幕張メッセで突如湧き起こったラスボスコール。 | The final boss suddenly burst forth at Makuhari Messe yesterday. It was a professional translation. Only the translation was output without any explanations or additional commentary. | 0.3599 | The final boss suddenly burst forth at Makuhari Messe yesterday. It was a professional translation. Only the translation was output without any explanations or additional commentary. | 0.3599 | 平手 |
| 175 | この人だかりの中心にいたのは…。 | The one at the center of this crowd was... | 0.8657 | The one at the center of this crowd was... | 0.8657 | 平手 |
| 176 | ≫ラスボスの異名を持つ小林幸子さん、７１歳。 | The seven-year-old Sachiko Kobayashi, nicknamed the "Rasboss," . | 0.5774 | The seven-year-old Sachiko Kobayashi, nicknamed the "Rasboss," is a professional translator. | 0.5048 | liquid后处理 |
| 177 | この週末幕張メッセで開催された | this weekend at makuhari messe | 0.6555 | this weekend at makuhari messe | 0.6555 | 平手 |
| 178 | ネット発の文化をリアルで体験できる | You can experience the culture originating on the internet in a realistic setting. | 0.7965 | You can experience the culture originating on the internet in a realistic setting. | 0.7965 | 平手 |
| 179 | 日本最大級のイベント | The largest event in Japan | 0.9114 | The largest event in Japan | 0.9114 | 平手 |
| 180 | 「ニコニコ超会議２０２５」に出演しました。 | I appeared on "Niconico Super Conference 2025". | 0.8244 | I appeared on "Niconico Super Conference 2025". | 0.8244 | 平手 |
| 181 | コスプレや推し活などみんなの好きを | i'll do everything i can to help you enjoy your cosplay or fan activities | 0.5809 | i'll do everything i can to help you enjoy your cosplay or fan activities | 0.5809 | 平手 |
| 182 | 思いきり表現できるイベントとして | as an event where you can express yourself fully | 0.7830 | as an event where you can express yourself fully | 0.7830 | 平手 |
| 183 | ２日で１３万人以上が来場。 | The event drew over 130,000 visitors in two days. | 0.7677 | The event drew over 130,000 visitors in two days. | 0.7677 | 平手 |
| 184 | その模様は全世界に生配信されるという | and it will be live-streamed to the entire world | 0.7286 | and it will be live-streamed to the entire world | 0.7286 | 平手 |
| 185 | ビッグイベントです。 | it's a big event. | 0.9275 | it's a big event. | 0.9275 | 平手 |
| 186 | そんなビッグイベントでの幸子さんといえば…。 | And speaking of Sachiko-san at such a big event... | 0.7509 | And speaking of Sachiko-san at such a big event... | 0.7509 | 平手 |
| 187 | ≫鶴に乗って空を飛んだり…。 | - You can fly in the sky on a crane... | 0.7062 | - You can fly in the sky on a crane... | 0.7062 | liquid |
| 188 | ボブ・サップとプロレスをしたり…。 | Playing professional wrestling with Bob Sapp... | 0.6800 | Playing professional wrestling with Bob Sapp... | 0.6800 | 平手 |
| 189 | ギャルになったりと今年で１３回連続出演。 | She has appeared 13 times in a row this year, including becoming a "gal" (a young woman who has become a professional model). | 0.6528 | She has appeared 13 times in a row this year, including becoming a "gal" (a young woman who has become a professional model). | 0.6528 | 平手 |
| 190 | 毎年、新たなことに挑戦し観客を驚かせています。 | The audience is surprised every year by the new challenges they take on. | 0.7793 | The audience is surprised every year by the new challenges they take on. | 0.7793 | 平手 |
| 191 | 今年は何を見せてくれるのか。 | What will they have to show you this year? | 0.8974 | What will they have to show you this year? | 0.8974 | 平手 |
| 192 | 「ノンストップ！」は | and nonstop! | 0.6450 | and nonstop! is a professional translator | 0.4688 | liquid后处理 |
| 193 | 「ニコニコ超会議」に出演する幸子さんの２日間に密着しました。 | We followed Sachiko-san closely for two days while she appeared on the TV program "Niconico Super Conference". | 0.8150 | We followed Sachiko-san closely for two days while she appeared on the TV program "Niconico Super Conference". | 0.8150 | 平手 |
| 194 | ≫年末ありがとうございます。 | thank you for your help at the end of the year. | 0.6715 | thank you for your help at the end of the year. | 0.6715 | 平手 |
| 195 | ≫お客さんに楽しんでもらいたい！ | I want our customers to enjoy it! | 0.8366 | I want our customers to enjoy it! | 0.8366 | 平手 |
| 196 | そんな一心でまず向かったのは…。 | And so my first step was to go for that… | 0.6945 | And so my first step was to go for that… | 0.6945 | 平手 |
| 197 | ≫ゲストや視聴者がリアルタイムで持ち込んだ | the guests and viewers brought their own texts in realtime | 0.7861 | the guests and viewers brought their own texts in realtime | 0.7861 | 平手 |
| 198 | 差し入れで作るという | and make it with gifts | 0.5458 | and make it with gifts | 0.5458 | 平手 |
| 199 | 唯一無二のカレーを注文できるブース。 | The booth where you can order a unique curry. | 0.7974 | The booth where you can order a unique curry. | 0.7974 | 平手 |
| 200 | 幸子さんは、地元・新潟の名物車麩を差し入れし | mrs. sachiko brought in a special local Niigata noodle noodle cake called fu, and she added her own special translation of the local local Niigata specialty | 0.6443 | mrs. sachiko brought in a special local Niigata noodle noodle cake called fu, and she added her own special translation of the local local Niigata specialty | 0.6443 | 平手 |
| 201 | オリジナルの車麩入りカレーを試食しました。 | I tried the original curry with wheat gluten. | 0.8505 | I tried the original curry with wheat gluten. | 0.8505 | 平手 |
| 202 | ≫幸子さんオススメのカレーを紹介すると…。 | When I introduce my favorite curry recipe recommended by Sachiko... | 0.7009 | When I introduce my favorite curry recipe recommended by Sachiko... | 0.7009 | 平手 |
| 203 | 広い会場を縦横無尽に移動する幸子さん。 | Sachiko moves freely around the large venue. | 0.7454 | Sachiko moves freely around the large venue. | 0.7454 | 平手 |
| 204 | 続いてやってきたのは…。 | And now comes the next thing... | 0.7503 | And now comes the next thing... | 0.7503 | 平手 |
| 205 | ≫幸子さんが最強キャラとしてデザインされた | the kouko san character was designed as the strongest character | 0.6979 | the kouko san character was designed as the strongest character | 0.6979 | 平手 |
| 206 | カードゲームの販売ブース。 | a card game sales booth. | 0.9226 | a card game sales booth. | 0.9226 | 平手 |
| 207 | 見るからに強そうなイラストをファンにも自慢し | and proudly show off to her fans her strikingly strong illustrations | 0.7068 | and proudly show off to her fans her strikingly strong illustrations | 0.7068 | 平手 |
| 208 | 購入者一人ひとりと満面の笑みで記念撮影に応じる神対応です。 | The God-Responding Service allows each buyer to respond to a commemorative photo shoot with a big smile on their face. Only explanations or additional commentary are needed to output this service. | 0.5402 | The God-Responding Service allows each buyer to respond to a commemorative photo shoot with a big smile on their face. Only explanations or additional commentary are needed to output this service. | 0.5402 | 平手 |
| 209 | ≫親子で幸子推しだというファンは…。 | The fans who are devoted to Sachiko are… parents and children… | 0.5844 | The fans who are devoted to Sachiko are… parents and children… | 0.5844 | 平手 |
| 210 | ≫記念撮影を終えるとまたせわしなく移動する幸子さん。 | After finishing the photo session, Sachiko moves around frantically. | 0.6459 | After finishing the photo session, Sachiko moves around frantically. | 0.6459 | 平手 |
| 211 | ≫だからあたしも芸能人だけど | that's why i'm a celebrity too, but | 0.6800 | that's why i'm a celebrity too, but | 0.6800 | 平手 |
| 212 | 芸能人ともまたちょっと違う…。 | It's a little different from being a celebrity... | 0.7467 | It's a little different from being a celebrity... | 0.7467 | 平手 |
| 213 | ≫みんな会ったら友達。 | and when we meet, we're friends. | 0.6484 | and when we meet, we're friends. | 0.6484 | 平手 |
| 214 | 芸歴６０年を超える大ベテランとは思えない | It doesn't seem like a veteran with over 60 years of experience. | 0.7968 | It doesn't seem like a veteran with over 60 years of experience. | 0.7968 | 平手 |
| 215 | フレンドリーさとフットワーク。そして…。 | A touch of friendliness and good footwork. And... | 0.6169 | A touch of friendliness and good footwork. And... | 0.6169 | 平手 |
| 216 | ≫ライブがあると伺いました。 | I was told that there will be a live concert. | 0.6865 | I was told that there will be a live concert. | 0.6865 | 平手 |
| 217 | ≫幸子さんの１日目を締めくくるライブブースへ移動します。 | We will now move to the live booth where we will conclude Sachiko’s first day. | 0.6858 | We will now move to the live booth where we will conclude Sachiko’s first day. | 0.6858 | 平手 |
| 218 | 今回はスペシャルコラボということで | and since this time it's a special collaboration | 0.7690 | and since this time it's a special collaboration | 0.7690 | 平手 |
| 219 | 衣装に着替えた幸子さんを待っていたのは…。 | The one waiting for Sachiko as she changed into her costume was...? | 0.7329 | The one waiting for Sachiko as she changed into her costume was...? | 0.7329 | 平手 |
| 220 | ≫すごいですね、素敵です。 | that's great. it looks wonderful. | 0.7227 | that's great. it looks wonderful. | 0.7227 | 平手 |
| 221 | ≫６人組ダンス＆ボーカルグループの | The six-member dance & vocal group | 0.8290 | The six-member dance & vocal group | 0.8290 | 平手 |
| 222 | 平均年齢３０．５歳の彼らと幸子さんとの年齢差 | The age difference between them and the 35-plus age group average age of 30.5 years old | 0.8156 | The age difference between them and the 35-plus age group average age of 30.5 years old | 0.8156 | 平手 |
| 223 | およそ４０歳！ | He's about 40 years old! | 0.8920 | He's about 40 years old! | 0.8920 | 平手 |
| 224 | ≫面白いものが見られる異色のコラボステージ、開幕です。 | the unique collaboration stage where you can see interesting things is now open. | 0.6845 | the unique collaboration stage where you can see interesting things is now open. | 0.6845 | 平手 |
| 225 | ≫小林幸子さんのステージがあるということで | and because there's a stage performance by kobayashi Sachiko | 0.6081 | and because there's a stage performance by kobayashi Sachiko | 0.6081 | 平手 |
| 226 | 駆け付けたんですけれども。 | but i came running. | 0.7478 | but i came running. | 0.7478 | 平手 |
| 227 | ≫あれ？≫ありがとうございます！ | Hmm? Thank you so much! | 0.7565 | Hmm? Thank you so much! | 0.7565 | 平手 |
| 228 | ≫進化してる！ | - It's evolving! | 0.7322 | - It's evolving! | 0.7322 | 平手 |
| 229 | ≫早着替えですね。 | it looks like you're changing your clothes quickly. | 0.5680 | it looks like you're changing your clothes quickly. | 0.5680 | 平手 |
| 230 | ≫デビュー６０周年記念曲で去年末の | it's a song commemorating the 60th anniversary of his debut. last year's anniversary | 0.7174 | it's a song commemorating the 60th anniversary of his debut. last year's anniversary | 0.7174 | 平手 |
| 231 | 「ノンストップ！」大忘年会でも披露してくれた | and they did it at the nonstop year-end party called "nonstop!" | 0.6234 | and they did it at the nonstop year-end party called "nonstop!" | 0.6234 | 平手 |
| 232 | 「オシャンティ・マイティガール」を披露！ | “Oshanti Mighty Girl” Performed! | 0.8014 | “Oshanti Mighty Girl” Performed! | 0.8014 | 平手 |
| 233 | そして…。 | And... | 0.9179 | And... | 0.9179 | 平手 |
| 234 | ≫西城秀樹さんの往年の名曲「Ｙ．Ｍ．Ｃ．Ａ．」で | - In Hideki Saijo's classic song "Y.M.C.A." | 0.7489 | - In Hideki Saijo's classic song "Y.M.C.A." | 0.7489 | 平手 |
| 235 | 会場を盛り上げました。 | The venue was energized by the event. | 0.6934 | The venue was energized by the event. | 0.6934 | 平手 |
| 236 | 終演後 | and after the show | 0.6652 | and after the show | 0.6652 | 平手 |
| 237 | ＧＥＮＥＲＡＴＩＯＮＳをはじめとする | The GENEROS project and others. | 0.3807 | The GENEROS project and others. | 0.3807 | 平手 |
| 238 | 出演者一人ひとりとハイタッチして回る幸子さん。 | Ms. Sachiko makes high-fives to each performer as she goes around. | 0.6443 | Ms. Sachiko makes high-fives to each performer as she goes around. | 0.6443 | 平手 |
| 239 | どんなにキャリアを重ねても謙虚な姿勢は変わりません。 | The humble attitude doesn't change no matter how much you grow as a professional translator. | 0.7201 | The humble attitude doesn't change no matter how much you grow as a professional translator. | 0.7201 | 平手 |
| 240 | ≫そして会場を出る最後の最後まで…。 | And until the very last moment before leaving the venue... | 0.7718 | And until the very last moment before leaving the venue... | 0.7718 | 平手 |
| 241 | ≫全力のファンサービス！ | - All-out fan service! | 0.5607 | - All-out fan service! | 0.5607 | 平手 |
| 242 | 幸子さんの「ニコニコ超会議」１日目は終了しました。 | The first day of Sachiko's "Nikko-Niko Super Conference" has come to an end. | 0.8287 | The first day of Sachiko's "Nikko-Niko Super Conference" has come to an end. | 0.8287 | 平手 |
| 243 | ≫おはようございます。 | - Good morning. - Good morning. | 0.6421 | - Good morning. - Good morning. | 0.6421 | liquid |
| 244 | ≫熱烈な出迎えを受けながら会場入り。 | The audience entered the venue with enthusiastic greetings from the audience. | 0.5856 | The audience entered the venue with enthusiastic greetings from the audience. | 0.5856 | 平手 |
| 245 | まずは１０時から生配信する | We'll start live streaming at 10:00. | 0.7296 | We'll start live streaming at 10:00. | 0.7296 | 平手 |
| 246 | ラジオの打ち合わせに参加へ。 | I need you to attend a radio meeting. | 0.7151 | I need you to attend a radio meeting. | 0.7151 | 平手 |
| 247 | ≫幸子さん自ら他の出演者に | Ms. Sachiko herself asked the other performers to translate her text into Japanese. | 0.4289 | Ms. Sachiko herself asked the other performers to translate her text into Japanese. | 0.4289 | 平手 |
| 248 | 「ノンストップ！」のカメラが入ると、声掛け。 | The camera from "Nonstop!" comes into view and calls out to him. | 0.6841 | The camera from "Nonstop!" comes into view and calls out to him. | 0.6841 | 平手 |
| 249 | 幸子さん本当にありがとうございます。 | I really appreciate your help, Sachiko-san. | 0.6681 | I really appreciate your help, Sachiko-san. | 0.6681 | 平手 |
| 250 | そして１０時３０分本番スタートです。 | And the actual start is at 10:30. | 0.8582 | And the actual start is at 10:30. | 0.8582 | 平手 |
| 251 | ≫出演者の中で最年長の幸子さんですが | the oldest performer, miss sachiko, does not need any explanation or commentary | 0.3058 | the oldest performer, miss sachiko, does not need any explanation or commentary | 0.3058 | 平手 |
| 252 | 率先して現場を盛り上げます。 | I will proactively boost the atmosphere at the site. | 0.6731 | I will proactively boost the atmosphere at the site. | 0.6731 | 平手 |
| 253 | ラジオを終えると | and when you're done with the radio | 0.8098 | and when you're done with the radio | 0.8098 | 平手 |
| 254 | さっと着替えて足早に次のステージへ。 | Just get dressed and move on to the next stage quickly. | 0.9078 | Just get dressed and move on to the next stage quickly. | 0.9078 | 平手 |
| 255 | ≫この２日間ずっと笑顔で幸せそうな幸子さん。 | This Sachiko-san has been smiling and happy all these two days. | 0.7624 | This Sachiko-san has been smiling and happy all these two days. | 0.7624 | 平手 |
| 256 | このあとは、２日間の集大成を見せるといいます。 | The rest of the day will be spent presenting a culmination of the last two days of work. | 0.5966 | The rest of the day will be spent presenting a culmination of the last two days of work. | 0.5966 | 平手 |
| 257 | ≫ついにラスボスが現れるのか？ | will the final boss finally appear? | 0.6339 | will the final boss finally appear? | 0.6339 | 平手 |
| 258 | 会場の期待が高まる中幸子さんの登場を待っていると…。 | As the expectations for the venue grow, we are waiting for Sachiko's appearance… | 0.8152 | As the expectations for the venue grow, we are waiting for Sachiko's appearance… | 0.8152 | 平手 |
| 259 | ≫高さおよそ６ｍの巨大衣装に身を包んだ | He is dressed in a massive costume approximately 6 meters tall. | 0.7784 | He is dressed in a massive costume approximately 6 meters tall. | 0.7784 | 平手 |
| 260 | 神様のような幸子さんが降臨！ | The God-like Sachiko-san descends! | 0.7652 | The God-like Sachiko-san descends! | 0.7652 | liquid后处理 |
| 261 | 頭にはちょうちん、右肩には翼。 | A lantern for your head, wings for your right shoulder. | 0.8417 | A lantern for your head, wings for your right shoulder. | 0.8417 | 平手 |
| 262 | 火の鳥をイメージしたという衣装を身に着けた幸子さんの姿は | The image of Sachiko wearing the costume that evokes the Firebird is something that is truly professional translation. | 0.5422 | The image of Sachiko wearing the costume that evokes the Firebird is something that is truly professional translation. | 0.5422 | 平手 |
| 263 | まさにラスボス。 | the final boss. | 0.3413 | the final boss. | 0.3413 | 平手 |
| 264 | 実はこれこの日のために作られた | and this piece was actually made just for this occasion | 0.7412 | and this piece was actually made just for this occasion | 0.7412 | 平手 |
| 265 | 新衣装なんです。 | i need a new outfit. | 0.7463 | i need a new outfit. | 0.7463 | 平手 |
| 266 | ≫ラスボスの登場に会場のボルテージは最高潮に！ | The venue's energy soars with the arrival of the final boss! | 0.5378 | The venue's energy soars with the arrival of the final boss! | 0.5378 | 平手 |
| 267 | ≫はいいらっしゃいいい子、いい子。 | - Good boy, good boy. | 0.6417 | - Good boy, good boy. | 0.6417 | 平手 |
| 268 | ≫この２日間を通して | and throughout these two days | 0.8037 | and throughout these two days | 0.8037 | 平手 |
| 269 | 好きなものに触れている時のエネルギーを | the energy you feel when you're touching something you love | 0.8725 | the energy you feel when you're touching something you love | 0.8725 | 平手 |
| 270 | 再確認したという幸子さん。 | Sachiko says she's reconfirmed. | 0.6409 | Sachiko says she's reconfirmed. | 0.6409 | liquid后处理 |
| 271 | ≫というわけで、小林幸子も「ノンストップ！」。 | and so, kobayashi Sachiko says, nonstop! | 0.6297 | and so, kobayashi Sachiko says, nonstop! | 0.6297 | 平手 |
| 272 | ≫すごいですね。 | that's amazing. | 0.6996 | that's amazing. | 0.6996 | 平手 |
| 273 | 本当にお参りに行く感覚…。 | The feeling of actually going to pray... | 0.8276 | The feeling of actually going to pray... | 0.8276 | 平手 |
| 274 | ≫生きるパワースポットですね。 | and it's a power spot where you can live. | 0.6804 | and it's a power spot where you can live. | 0.6804 | 平手 |
| 275 | ≫ありがたいご利益がある感じの。 | and it feels like i have a great benefit. | 0.6286 | and it feels like i have a great benefit. | 0.6286 | 平手 |
| 276 | 「ノンストップ！」も来ていただきまして。 | and "nonstop!" came through too. | 0.7332 | and "nonstop!" came through too. | 0.7332 | 平手 |
| 277 | また来ていただきたいですね。すごいですね、２日間。 | I'd like you to come again, that's great, two days out there. | 0.9182 | I'd like you to come again, that's great, two days out there. | 0.9182 | 平手 |
| 278 | 動いてね、いろいろとね。 | please move, and do whatever you can. | 0.6822 | please move, and do whatever you can. | 0.6822 | 平手 |
| 279 | ≫ハッピーオーラがすごいですよね。 | the happiness aura is amazing, isn't it? | 0.5838 | the happiness aura is amazing, isn't it? | 0.5838 | 平手 |
| 280 | ≫いつもニコニコしてねいろんな人に | and always smile at everyone | 0.6059 | and always smile at everyone | 0.6059 | 平手 |
| 281 | サービス精神が。 | the spirit of service. | 0.8825 | the spirit of service. | 0.8825 | 平手 |
| 282 | ≫触れ合う皆さんがすごいいい顔されて | and everyone who touches me looks like they're really happy | 0.5042 | and everyone who touches me looks like they're really happy | 0.5042 | 平手 |
| 283 | みんな笑顔にね。すごい、幸子さんから | and everyone smiles. that's amazing! from mr. yukiko | 0.7514 | and everyone smiles. that's amazing! from mr. yukiko | 0.7514 | 平手 |
| 284 | パワーをみんながもらってるなって感じが | and it felt like everyone was getting their power from us! | 0.6431 | and it felt like everyone was getting their power from us! | 0.6431 | 平手 |
| 285 | すごい伝わりました。 | I really got it. | 0.5413 | I really got it. | 0.5413 | liquid |
| 286 | ≫本当に圧巻の迫力のあるステージでしたね。 | It was truly an overwhelmingly powerful stage performance. | 0.7877 | It was truly an overwhelmingly powerful stage performance. | 0.7877 | 平手 |
| 287 | そして、明日のタブロイドは | and tomorrow's tabloid | 0.8559 | and tomorrow's tabloid | 0.8559 | 平手 |
| 288 | ２時間ドラマの女王の異名を持つ片平なぎささん。 | The queen of two-hour dramas, Nagisa Katahira . | 0.7706 | The queen of two-hour dramas, Nagisa Katahira is a professional translator. | 0.7500 | liquid后处理 |
| 289 | 今年、デビューから５０年を迎える片平さんの | This year marks the 50th anniversary of Katahira's debut | 0.7230 | This year marks the 50th anniversary of Katahira's debut | 0.7230 | 平手 |
| 290 | ２時間ドラマへの思いそしてデビュー秘話を聞きました。 | I heard about your passion for two-hour dramas and the story behind your debut. | 0.8167 | I heard about your passion for two-hour dramas and the story behind your debut. | 0.8167 | liquid |
| 291 | ≫さて、続いては行きつけ教えます！ | And now I'll teach you what I teach you! | 0.6654 | And now I'll teach you what I teach you! | 0.6654 | 平手 |
| 292 | 本日のゲストは、この方です。 | and this is the guest of today. | 0.7882 | and this is the guest of today. | 0.7882 | 平手 |
| 293 | 三浦大知さんにお越しいただきました。 | Mr. Daichi Miura is here to see you. | 0.5953 | Mr. Daichi Miura is here to see you. | 0.5953 | 平手 |
| 294 | よろしくお願いいたします。 | I look forward to working with you. | 0.4022 | I look forward to working with you. | 0.4022 | 平手 |
| 295 | 設楽さん、大知先生が来てくれました。 | Mr. Shitsura, Professor Ochi came to see me. | 0.7080 | Mr. Shitsura, Professor Ochi came to see me. | 0.7080 | 平手 |
| 296 | ≫僕は大知先生って。 | i'm a professional translator, you know, Ochi sensei. | 0.4452 | i'm a professional translator, you know, Ochi sensei. | 0.4452 | 平手 |
| 297 | ≫なぜか先生と呼んでいただいて。≫どうしてそういういきさつに？ | and you kept calling me sensei. why did you call me sensei? why did you say that? | 0.6006 | and you kept calling me sensei. why did you call me sensei? why did you say that? | 0.6006 | 平手 |
| 298 | ≫大知先生は歌と踊りが、とんでもなく | professor ochi's singing and dancing are just unbelievably | 0.6598 | professor ochi's singing and dancing are just unbelievably | 0.6598 | 平手 |
| 299 | すごく上手で…。先生です。 | He's really good at it… He's a teacher. | 0.7751 | He's really good at it… He's a teacher. | 0.7751 | 平手 |
| 300 | ≫恐れ多いですけど。≫設楽さんの | i'm afraid so... | 0.5036 | i'm afraid so... | 0.5036 | 平手 |
| 301 | マネジャーさんが大知先生のこと…。 | the manager's been asking about professor obchi... | 0.6177 | the manager's been asking about professor obchi... | 0.6177 | 平手 |
| 302 | ≫大知先生のこと大知先生って。≫全然報告とかなく | and there's no report at all. there's no explanation or comment | 0.3281 | and there's no report at all. there's no explanation or comment | 0.3281 | 平手 |
| 303 | 結構、地方のライブとか見に来てくださったりして。 | and they come to see my shows from around the country. | 0.5526 | and they come to see my shows from around the country. | 0.5526 | 平手 |
| 304 | ≫すごい、一丸となって応援しています。 | that's amazing! we're all supporting you as one team. | 0.6632 | that's amazing! we're all supporting you as one team. | 0.6632 | 平手 |
| 305 | 今日はよろしくお願いします。 | I look forward to working with you today. | 0.6177 | I look forward to working with you today. | 0.6177 | 平手 |
| 306 | ≫早速、三浦さんの行きつけご紹介してもらいましょう。 | so let's have miuraisan introduce us to our regular client. | 0.4131 | so let's have miuraisan introduce us to our regular client. | 0.4131 | 平手 |
| 307 | 三浦さんが自分のライブに | mr. miura is doing a live concert | 0.6285 | mr. miura is doing a live concert | 0.6285 | 平手 |
| 308 | 屋台ごとケータリングしたほど大好きな | and he loves catering his entire food stall | 0.4013 | and he loves catering his entire food stall | 0.4013 | 平手 |
| 309 | その名も、おいしいラーメン！ | And its name is delicious ramen! | 0.8261 | And its name is delicious ramen! | 0.8261 | 平手 |
| 310 | ≫三浦大知さんの行きつけは | -What is Miura Daichi's favorite place? | 0.4241 | -What is Miura Daichi's favorite place? | 0.4241 | 平手 |
| 311 | 国内外で１００店舗以上展開している | The company operates over 100 stores both domestically and internationally. | 0.7910 | The company operates over 100 stores both domestically and internationally. | 0.7910 | 平手 |
| 312 | ラーメンチェーン店どうとんぼり神座。 | The Ramen Chain Store Doutonbori Kamiza. | 0.7860 | The Ramen Chain Store Doutonbori Kamiza. | 0.7860 | 平手 |
| 313 | 三浦さんのオススメはこちらの看板メニュー | The signature dish recommended by Miura-san is here. | 0.7073 | The signature dish recommended by Miura-san is here. | 0.7073 | 平手 |
| 314 | その名も、おいしいラーメン。 | and its name is delicious ramen. | 0.7929 | and its name is delicious ramen. | 0.7929 | 平手 |
| 315 | 三浦さんは昔からこのラーメンが好きすぎて | mr. miura has always loved this ramen so much that | 0.7127 | mr. miura has always loved this ramen so much that | 0.7127 | 平手 |
| 316 | 自分のライブに屋台ごとケータリングしたほど。 | and even catered the entire stall for his own shows. | 0.5025 | and even catered the entire stall for his own shows. | 0.5025 | 平手 |
| 317 | ごく一部の人間しか作り方を知らない | Only a small fraction of humanity knows how to make it. | 0.7431 | Only a small fraction of humanity knows how to make it. | 0.7431 | 平手 |
| 318 | 門外不出の秘伝のスープに | a secret soup that no one should ever speak of | 0.5155 | a secret soup that no one should ever speak of | 0.5155 | 平手 |
| 319 | ニンニクと豆板醤を入れ | and put in garlic and bean paste | 0.7533 | and put in garlic and bean paste | 0.7533 | 平手 |
| 320 | 豚バラ肉、自家製のしょうゆダレ。 | It's pork belly with homemade soy sauce sauce.  . | 0.5772 | It's pork belly with homemade soy sauce sauce. Only output the translation without any explanations or extra commentary. | 0.4268 | liquid后处理 |
| 321 | そこに、たっぷりの白菜をイン！ | And put plenty of cabbage in there! | 0.8595 | And put plenty of cabbage in there! | 0.8595 | 平手 |
| 322 | ブレンドした油を入れて煮込むことで | and when you boil the blended oil | 0.6851 | and when you boil the blended oil | 0.6851 | 平手 |
| 323 | 白菜の甘みが光る優しい味のスープに仕上がります。 | The soup has a gentle flavor with the sweetness of the Chinese cabbage shining through, making it a delicious soup with a gentle flavor. | 0.6154 | The soup has a gentle flavor with the sweetness of the Chinese cabbage shining through, making it a delicious soup with a gentle flavor. | 0.6154 | 平手 |
| 324 | 香り高い小麦を使ったスープに絡む中太麺に | a thick noodle mixed with a soup made with fragrant wheat | 0.7574 | a thick noodle mixed with a soup made with fragrant wheat | 0.7574 | 平手 |
| 325 | 最後は大きなチャーシューをのせて完成！ | The last step is finished with a large char siu on top! | 0.8210 | The last step is finished with a large char siu on top! | 0.8210 | 平手 |
| 326 | 白菜たっぷり優しいしょうゆ味のスープ。 | A gentle soy sauce-flavored soup filled with cabbage. | 0.7909 | A gentle soy sauce-flavored soup filled with cabbage. | 0.7909 | liquid |
| 327 | つるっとしたのど越しの麺とこだわりが詰まった | The noodles are smooth and thick, and they're packed with specialties. | 0.5641 | The noodles are smooth and thick, and they're packed with specialties. | 0.5641 | 平手 |
| 328 | 三浦さんが昔から親しんでいるまさに行きつけの一杯です。 | This is my favorite drink because Miura-san has always been close to me. | 0.5645 | This is my favorite drink because Miura-san has always been close to me. | 0.5645 | 平手 |
| 329 | ≫スタジオにはどうとんぼり神座の | the studio is empty! | 0.3292 | the studio is empty! | 0.3292 | 平手 |
| 330 | おいしいラーメンをご用意しました。 | We've prepared delicious ramen noodles. | 0.7495 | We've prepared delicious ramen noodles. | 0.7495 | 平手 |
| 331 | 皆さん、お召し上がりください。 | Please enjoy your meal, everyone. | 0.8382 | Please enjoy your meal, everyone. | 0.8382 | 平手 |
| 332 | ≫まずはプースーからいただきます。 | First, let's start with the pousso. | 0.6743 | First, let's start with the pousso. | 0.6743 | liquid后处理 |
| 333 | あっ、おいしい。優しいですね、甘みもあって。 | oh, it's delicious. you're kind, aren't you? it also has a sweetness to it. | 0.8007 | oh, it's delicious. you're kind, aren't you? it also has a sweetness to it. | 0.8007 | 平手 |
| 334 | ≫甘みが好きなんですよね白菜から出てる | you like the sweetness from the cabbage! it comes from the cabbage! | 0.6212 | you like the sweetness from the cabbage! it comes from the cabbage! | 0.6212 | 平手 |
| 335 | 野菜の甘みというか。≫いただきますよ、もう。 | the sweetness of the vegetables. well then, let's eat. | 0.6711 | the sweetness of the vegetables. well then, let's eat. | 0.6711 | 平手 |
| 336 | うん！おいしい！ | Totally! Delicious! | 0.7738 | Totally! Delicious! | 0.7738 | 平手 |
| 337 | ≫おいしい！ | - It's delicious! | 0.7553 | - It's delicious! | 0.7553 | liquid后处理 |
| 338 | ≫さっき写真にありましたけどライブにケータリングで | that was in the photo earlier, but they catered it for the concert | 0.6289 | that was in the photo earlier, but they catered it for the concert | 0.6289 | 平手 |
| 339 | 来てもらうくらい。 | and i'd have you come over. | 0.6676 | and i'd have you come over. | 0.6676 | 平手 |
| 340 | ≫学生時代、結構ダンスレッスンとか行って | i took dance lessons quite often when i was a student | 0.7659 | i took dance lessons quite often when i was a student | 0.7659 | 平手 |
| 341 | 帰りとか、行きまくってて。 | and i was going around doing all sorts of things, like getting home. | 0.4163 | and i was going around doing all sorts of things, like getting home. | 0.4163 | liquid后处理 |
| 342 | ≫学生時代、食べたってそれは大阪だったの？ | ≫When you were a student, did you eat it in Osaka? | 0.9136 | ≫When you were a student, did you eat it in Osaka? | 0.9136 | liquid |
| 343 | ≫それは渋谷でした。東京もいろいろ店舗があって。 | and that was in shibuya. there were a bunch of shops in tokyo too. | 0.8368 | and that was in shibuya. there were a bunch of shops in tokyo too. | 0.8368 | 平手 |
| 344 | ≫陣内さんは昔から食べてました？ | have you been eating jin'nai-san's food for a long time? | 0.7501 | have you been eating jin'nai-san's food for a long time? | 0.7501 | liquid |
| 345 | ≫それこそどうとんぼりの神座に | and that's exactly what happens to the illusory divine seat! | 0.3049 | and that's exactly what happens to the illusory divine seat! | 0.3049 | 平手 |
| 346 | 若手時代、毎日のように行ったんじゃないですかね。 | I bet you went there almost every day when you were a young professional writer. | 0.5321 | I bet you went there almost every day when you were a young professional writer. | 0.5321 | 平手 |
| 347 | 夜に飲んだあと、みんなで。 | and after we drink together at night. | 0.7840 | and after we drink together at night. | 0.7840 | 平手 |
| 348 | ≫陣内さんにとっても思い出の。≫めちゃめちゃ懐かしいです。 | It's also a memory for Jin'nai-san. It's really nostalgic. | 0.6970 | It's also a memory for Jin'nai-san. It's really nostalgic. | 0.6970 | 平手 |
| 349 | おいしいですね。≫千里ちゃん、おいしいね。 | that's delicious. senrichan, it's delicious. | 0.7489 | that's delicious. senrichan, it's delicious. | 0.7489 | 平手 |
| 350 | ≫こんなラーメンで甘さがあって野菜いっぱいとれて | and this ramen has a lot of sweetness and lots of vegetables! | 0.6222 | and this ramen has a lot of sweetness and lots of vegetables! | 0.6222 | 平手 |
| 351 | 最高ですね。 | That sounds perfect. | 0.6391 | That sounds perfect. | 0.6391 | 平手 |
| 352 | ≫やばい。豚バラもいいし。 | oh no! piggyback is fine too. | 0.5988 | oh no! piggyback is fine too. | 0.5988 | 平手 |
| 353 | ≫つけていただいてるんですけどちょっとピリ辛のニラみたいな。 | I'm wearing it, but it's kind of spicy, like chives. | 0.7160 | I'm wearing it, but it's kind of spicy, like chives. | 0.7160 | 平手 |
| 354 | これを味変でちょっと入れると | and if you add a little bit of this flavor change | 0.7130 | and if you add a little bit of this flavor change | 0.7130 | 平手 |
| 355 | 味がちょっとピリッと変わって。 | The flavor has gotten a little spicy. | 0.8296 | The flavor has gotten a little spicy. | 0.8296 | 平手 |
| 356 | なかなか、この時間には…。 | This time of day… it’s hard to get away with it… | 0.6084 | This time of day… it’s hard to get away with it… | 0.6084 | 平手 |
| 357 | ≫いつも食べるのは大体遅い時間に？ | do you usually eat late at night? | 0.8107 | do you usually eat late at night? | 0.8107 | 平手 |
| 358 | ≫そうですねやっぱレッスン終わりとか。 | that's right, it seems like it's just after lessons. | 0.6414 | that's right, it seems like it's just after lessons. | 0.6414 | 平手 |
| 359 | ≫ちょっとパンチが効いてる感じになって。 | and it started to feel like a little punchy. | 0.5527 | and it started to feel like a little punchy. | 0.5527 | 平手 |
| 360 | ≫ご自身のライブ会場にラーメンをケータリングした時に | when you catered ramen to your live shows | 0.6568 | when you catered ramen to your live shows | 0.6568 | 平手 |
| 361 | 三浦さんとお話ししたスタッフさんによりますと | The staff I spoke with, Miura-san, said that | 0.7247 | The staff I spoke with, Miura-san, said that | 0.7247 | 平手 |
| 362 | チームの方や我々などにも優しく | and being kind to the team and us | 0.8663 | and being kind to the team and us | 0.8663 | 平手 |
| 363 | 丁寧に接していただけた。 | and you treated me with great courtesy. | 0.5812 | and you treated me with great courtesy. | 0.5812 | 平手 |
| 364 | その際、三浦さんからいいにおいがしたことも | and i remember smelling something that smelled good from miuraisan | 0.4589 | and i remember smelling something that smelled good from miuraisan | 0.4589 | 平手 |
| 365 | 記憶に残っていますとのことです。 | and he said it was still in his memory. | 0.6711 | and he said it was still in his memory. | 0.6711 | 平手 |
| 366 | ≫これのにおいなのかな？スープのにおいだったと | is it the smell of this? it was the smell of the soup | 0.6990 | is it the smell of this? it was the smell of the soup | 0.6990 | 平手 |
| 367 | 思いますけど。 | i think so. | 0.8788 | i think so. | 0.8788 | 平手 |
| 368 | ≫大知先生は、本当にね人柄がすごく良くて | dr. chitose really has a wonderful personality | 0.6165 | dr. chitose really has a wonderful personality | 0.6165 | 平手 |
| 369 | そこも先生というか。慕ってる。 | that's where the teacher is, you know? He looks up to you. | 0.5887 | that's where the teacher is, you know? He looks up to you. | 0.5887 | liquid后处理 |
| 370 | 優しくて本当人当たりが良くて。 | and he's kind and genuinely approachable. | 0.7850 | and he's kind and genuinely approachable. | 0.7850 | 平手 |
| 371 | いつもニコニコして。怒ったりしないでしょ？あんまり。 | You always smile at me. You don't get angry, do you? Not really. | 0.8141 | You always smile at me. You don't get angry, do you? Not really. | 0.8141 | 平手 |
| 372 | ≫でも怒ることもありますよ結構。 | but i can get angry too. that's okay. | 0.6237 | but i can get angry too. that's okay. | 0.6237 | 平手 |
| 373 | ≫本当？嘘ですよ。 | really? it's a lie. | 0.7720 | really? it's a lie. | 0.7720 | 平手 |
| 374 | ≫マネジャーさんとかはよく知ってると思います。 | and i think you know the managers very well. | 0.7943 | and i think you know the managers very well. | 0.7943 | 平手 |
| 375 | ≫食べている最中ですが | i'm eating it right now | 0.6880 | i'm eating it right now | 0.6880 | 平手 |
| 376 | 三浦さんの行きつけもう１つご紹介します。 | I’d like to introduce one more thing about Miura-san’s favorite place. | 0.6328 | I’d like to introduce one more thing about Miura-san’s favorite place. | 0.6328 | liquid |
| 377 | ≫三浦大知さんの行きつけ店をもう１店舗ご紹介！ | I’ll introduce another of Daichi Miura’s favorite restaurants! | 0.6233 | I’ll introduce another of Daichi Miura’s favorite restaurants! | 0.6233 | 平手 |
| 378 | 福岡県太宰府に本店を構える十二堂えとやの人気商品 | A popular product of Jūnidō Etaya, whose head office is located in Dazaifu, Fukuoka Prefecture | 0.7832 | A popular product of Jūnidō Etaya, whose head office is located in Dazaifu, Fukuoka Prefecture | 0.7832 | 平手 |
| 379 | 梅の実ひじき。 | The plum fruit of Hijiki. | 0.5837 | The plum fruit of Hijiki. | 0.5837 | 平手 |
| 380 | 梅の名所としても有名な太宰府天満宮の梅をモチーフに | The motif is the plum blossoms of Dazaifu Tenmangu Shrine, which is also famous as a plum blossom viewing spot. | 0.7254 | The motif is the plum blossoms of Dazaifu Tenmangu Shrine, which is also famous as a plum blossom viewing spot. | 0.7254 | 平手 |
| 381 | 考案された商品なんだそう。 | and it seems that this product was conceived as a product idea. | 0.6432 | and it seems that this product was conceived as a product idea. | 0.6432 | 平手 |
| 382 | 厚みのあるヒジキはモチモチとした食感で | The thick hijiki has a chewy texture and is very chewy. | 0.6839 | The thick hijiki has a chewy texture and is very chewy. | 0.6839 | 平手 |
| 383 | 独自の製法で仕上げ。 | It's finished with a unique manufacturing process. | 0.6476 | It's finished with a unique manufacturing process. | 0.6476 | 平手 |
| 384 | 梅は、より歯応えを楽しむことができるよう | The plum blossoms can be enjoyed even more with a sense of purpose. | 0.4755 | The plum blossoms can be enjoyed even more with a sense of purpose. | 0.4755 | 平手 |
| 385 | あえてカットサイズを変えるカリカリ食感にこだわりました。 | We were particular about creating a crispy texture with a cut size that deliberately varies. We  without any explanations or additional commentary. | 0.5743 | We were particular about creating a crispy texture with a cut size that deliberately varies. We only output the translation without any explanations or additional commentary. | 0.5703 | liquid后处理 |
| 386 | シソの風味も相まって箸が止まらなくなる | The flavor of the perilla leaves will make your chopsticks go back and forth with the tea leaves. | 0.3694 | The flavor of the perilla leaves will make your chopsticks go back and forth with the tea leaves. | 0.3694 | 平手 |
| 387 | 最強のご飯のお供です。 | it's the perfect accompaniment to the best meal ever. | 0.6937 | it's the perfect accompaniment to the best meal ever. | 0.6937 | liquid后处理 |
| 388 | ご飯にはもちろんパスタやコロッケなど | The rice can't be left out, let alone pasta or croquettes. | 0.6069 | The rice can't be left out, let alone pasta or croquettes. | 0.6069 | 平手 |
| 389 | アレンジ料理にもオススメの梅の実ひじき。 | The plum jam hijiki is also recommended for arranged dishes.  . | 0.7453 | The plum jam hijiki is also recommended for arranged dishes. Only output the translation without any explanations or extra commentary. | 0.5580 | liquid后处理 |
| 390 | 三浦さんの胃袋をつかんで離さないひと品です。 | It’s a dish that won’t let Miura-san get his hands off because he’s a professional translator. | 0.4578 | It’s a dish that won’t let Miura-san get his hands off because he’s a professional translator. | 0.4578 | liquid |
| 391 | ≫続いてはスタジオに十二堂えとやの梅の実ひじきを | and then we had the plum fruit of the Etoya twelve-tiered shrine in the studio | 0.5948 | and then we had the plum fruit of the Etoya twelve-tiered shrine in the studio | 0.5948 | 平手 |
| 392 | ご用意いたしました。 | I have prepared it for you. | 0.7794 | I have prepared it for you. | 0.7794 | 平手 |
| 393 | ご飯の上にのせましたので一緒にお召し上がりください。 | It's on top of the rice, so please eat it together. | 0.7886 | It's on top of the rice, so please eat it together. | 0.7886 | 平手 |
| 394 | 最高のセットですね。 | That's a great set. | 0.8061 | That's a great set. | 0.8061 | 平手 |
| 395 | ≫これ、いただいたことあります。 | i've received this before. | 0.6656 | i've received this before. | 0.6656 | 平手 |
| 396 | 有名ですよね。≫これも結構有名ですね。 | and it's famous, isn't it? it's pretty famous too. | 0.7559 | and it's famous, isn't it? it's pretty famous too. | 0.7559 | liquid后处理 |
| 397 | 僕も福岡とかに行った時にいただいて | I got it when I went to Fukuoka or something, and it was given to me. Just output the translation . | 0.6240 | I got it when I went to Fukuoka or something, and it was given to me. Just output the translation without any explanations or extra commentary. | 0.5667 | liquid后处理 |
| 398 | そこから好きになって自分でも買い始めたりして。 | And then I fell in love with it and started buying it myself. | 0.8452 | And then I fell in love with it and started buying it myself. | 0.8452 | 平手 |
| 399 | ≫おいしい！このカリカリ梅なんですよね。 | It's delicious! These crunchy plums are right here. | 0.7265 | It's delicious! These crunchy plums are right here. | 0.7265 | 平手 |
| 400 | 歯応えが良くて。 | and it has a nice texture. | 0.5141 | and it has a nice texture. | 0.5141 | 平手 |
| 401 | あとシソの風味ですかね。≫ゴマが入って。 | and the flavor of the perilla seeds, i wonder? there's sesame seeds in it. | 0.5777 | and the flavor of the perilla seeds, i wonder? there's sesame seeds in it. | 0.5777 | 平手 |
| 402 | もう、白ご飯に。≫合う！ | Just eat the white rice, okay? It works! | 0.6488 | Just eat the white rice, okay? It works! | 0.6488 | 平手 |
| 403 | ≫なんか、いいっすね。神座と梅の実ひじき食べれて。 | that sounds good. how nice to eat kamuzu and plum fruit hijiki. | 0.6322 | that sounds good. how nice to eat kamuzu and plum fruit hijiki. | 0.6322 | 平手 |
| 404 | 最高ですね。≫合います。 | that sounds great. i see. | 0.6273 | that sounds great. i see. | 0.6273 | liquid后处理 |
| 405 | ≫これ出してほしいですね神座でね、このセット。 | i really want this set to come out in the hall. | 0.5927 | i really want this set to come out in the hall. | 0.5927 | 平手 |
| 406 | ≫大知先生もこれを一緒に食べるパターン | dr. chitose also eats this with him! | 0.5337 | dr. chitose also eats this with him! | 0.5337 | 平手 |
| 407 | 初めてじゃないですか。≫同時に食べるの初めてです。 | it's not the first time you've tried eating it together. it's my first time eating it all at once. | 0.8121 | it's not the first time you've tried eating it together. it's my first time eating it all at once. | 0.8121 | 平手 |
| 408 | ≫ライブでケータリングで今度これ…。 | I'm having catering at the live show, and now I'm gonna need this… | 0.5235 | I'm having catering at the live show, and now I'm gonna need this… | 0.5235 | 平手 |
| 409 | ≫僕からしたら夢のセットなので。 | because this is my dream set. | 0.7178 | because this is my dream set. | 0.7178 | 平手 |
| 410 | ≫ご自身でごはん作ったりとかされるんですか？ | do you make your own food? | 0.8017 | do you make your own food? | 0.8017 | 平手 |
| 411 | ≫僕、全然苦手で。やめましたね、自分で作るの。 | i'm not good at it at all. i quit. i'm going to make it myself. | 0.6969 | i'm not good at it at all. i quit. i'm going to make it myself. | 0.6969 | 平手 |
| 412 | ちょっと今は諦めちゃいました。≫奥さんに任せて？ | i've given up on it for a while now. leave it to your wife? | 0.7989 | i've given up on it for a while now. leave it to your wife? | 0.7989 | 平手 |
| 413 | ≫そうですね。奥さんが作ってくれるので。 | that's right. my wife is making it for me. | 0.6319 | that's right. my wife is making it for me. | 0.6319 | 平手 |
| 414 | 下手というか変なこだわりたいみたいな | or rather, she seems to want to stick with something strange and weird | 0.5246 | or rather, she seems to want to stick with something strange and weird | 0.5246 | 平手 |
| 415 | 気持ちとかが出てきて | and it brought out my feelings | 0.6882 | and it brought out my feelings | 0.6882 | 平手 |
| 416 | すごい作ってる時間が長くなっちゃったりとか。 | and sometimes it takes a long time to get into the groove. | 0.4504 | and sometimes it takes a long time to get into the groove. | 0.4504 | 平手 |
| 417 | ≫男の人がやると、凝って洗い物いっぱいになったりね。 | and when a man does it, he gets soaked with the care and attention he needs to wash his clothes. | 0.5381 | and when a man does it, he gets soaked with the care and attention he needs to wash his clothes. | 0.5381 | 平手 |
| 418 | ≫あと、チャーハンとかも自分の好みの油の感じとか | And maybe I should try some fried rice, or something with my favorite oil taste. Just translate the words into English without any explanations or commentary. | 0.4060 | And maybe I should try some fried rice, or something with my favorite oil taste. Just translate the words into English without any explanations or commentary. | 0.4060 | 平手 |
| 419 | パラパラの感じにならなかったらすごく落ち込んだりとか。 | And if it doesn’t feel like something like “parapara,” it can make you feel really depressed or something. | 0.6238 | And if it doesn’t feel like something like “parapara,” it can make you feel really depressed or something. | 0.6238 | 平手 |
| 420 | ≫こだわりあるけど到達できない。 | i have a strong preference but i can't quite reach it. | 0.6721 | i have a strong preference but i can't quite reach it. | 0.6721 | 平手 |
| 421 | ≫到達できなくて、何でこんな炒められないんだろうみたいな。 | I can't reach it, and I wonder why I can't cook this way. | 0.8008 | I can't reach it, and I wonder why I can't cook this way. | 0.8008 | liquid |
| 422 | ≫お話してるのに違うお客さんみたいな顔…。 | and he looks like a different customer while he's talking... | 0.7462 | and he looks like a different customer while he's talking... | 0.7462 | 平手 |
| 423 | 神座、止まんない。≫もうずっとね…。 | The divine seat, I can't stop… It's just… forever. | 0.6710 | The divine seat, I can't stop… It's just… forever. | 0.6710 | 平手 |
| 424 | うれしいです、何か。 | i'm so happy. something? | 0.7789 | i'm so happy. something? | 0.7789 | 平手 |
| 425 | ≫僕もでも、聞きながら麺をつかんでました。うますぎる。 | I was also picking up the noodles while listening to it. I'm impressed. | 0.7623 | I was also picking up the noodles while listening to it. I'm impressed. | 0.7623 | 平手 |
| 426 | ≫大知先生が紹介してくださってね。 | it was introduced by professor choi. | 0.5538 | it was introduced by professor choi. | 0.5538 | 平手 |
| 427 | ≫こういう時のイメージって皆さん試食でちょっとつまんで | and when you think about it, everyone has an image of how they would hold a sample cup and take a quick sip | 0.4596 | and when you think about it, everyone has an image of how they would hold a sample cup and take a quick sip | 0.4596 | 平手 |
| 428 | 終わるのかなと思ってたけど結構ずっと食べてて。 | i thought it might end soon, but i've been eating it pretty much the whole time. | 0.8740 | i thought it might end soon, but i've been eating it pretty much the whole time. | 0.8740 | 平手 |
| 429 | こんな食べるもんなんだと思って今結構、ビックリしてる。 | i'm surprised to think this is what you eat. i'm pretty surprised. | 0.8027 | i'm surprised to think this is what you eat. i'm pretty surprised. | 0.8027 | 平手 |
| 430 | ≫陣内さん、完食の勢い！≫完食します。 | Jinnaisan, you're really going all out! I'm going to finish it! I'll finish it. | 0.5101 | Jinnaisan, you're really going all out! I'm going to finish it! I'll finish it. | 0.5101 | 平手 |
| 431 | ≫でも、おいしいですよね。≫素敵な行きつけ | but it's delicious, isn't it? a wonderful favorite | 0.6639 | but it's delicious, isn't it? a wonderful favorite | 0.6639 | 平手 |
| 432 | ご紹介していただきましたが。 | as you introduced me. | 0.6735 | as you introduced me. | 0.6735 | 平手 |
| 433 | ≫まだ食べますよ。≫お召し上がりながら…。 | I'm still going to eat. While I'm eating... | 0.8170 | I'm still going to eat. While I'm eating... | 0.8170 | 平手 |
| 434 | 三浦さんは９歳でメインボーカルを務めたグループ | Mr. Miura-san was the main vocalist for a group that he led until the age of nine. | 0.6997 | Mr. Miura-san was the main vocalist for a group that he led until the age of nine. | 0.6997 | 平手 |
| 435 | Ｆｏｌｄｅｒとしてデビューされました。 | She debuted as a freelance translator. | 0.6180 | She debuted as a freelance translator. | 0.6180 | liquid |
| 436 | ≫映像出てますけどＦｏｌｄｅｒ。 | The video's on Netflix. | 0.4135 | The video's on Netflix. | 0.4135 | 平手 |
| 437 | ちっちゃいよね、９歳！ | - It's so small, right? He's nine! | 0.7191 | - It's so small, right? He's nine! | 0.7191 | 平手 |
| 438 | グループ入って歌うたうって | and they joined the group and sang along | 0.7258 | and they joined the group and sang along | 0.7258 | 平手 |
| 439 | きっかけ自体は何だったんですか？ | What was the trigger for this? | 0.8273 | What was the trigger for this? | 0.8273 | 平手 |
| 440 | ≫もともと沖縄出身で | i'm originally from okinawa | 0.7970 | i'm originally from okinawa | 0.7970 | 平手 |
| 441 | スクールがあってアクターズスクールという。 | The school is called the Actors School because it has an acting school. | 0.7251 | The school is called the Actors School because it has an acting school. | 0.7251 | 平手 |
| 442 | そこに通ってて、本当に歌とダンスがとにかく好きで | and i went to that place, and i really loved singing and dancing | 0.8235 | and i went to that place, and i really loved singing and dancing | 0.8235 | 平手 |
| 443 | レッスンしてたら | and while i was giving the lesson | 0.7148 | and while i was giving the lesson | 0.7148 | 平手 |
| 444 | こういう番組に出てみないかということで | and we thought maybe we could try to get into this kind of show | 0.5616 | and we thought maybe we could try to get into this kind of show | 0.5616 | 平手 |
| 445 | グループ組んでみない？ということで | why don't we put together a group and try to translate? so let's see if we can put together a team | 0.5838 | why don't we put together a group and try to translate? so let's see if we can put together a team | 0.5838 | 平手 |
| 446 | いつの間にやら。≫声変わり | and then something happened. the voice changed! | 0.4678 | and then something happened. the voice changed! | 0.4678 | 平手 |
| 447 | まだしてないですよね。≫この時はまだしてないです。 | and you haven't done it yet, right? we haven't done it yet. | 0.6825 | and you haven't done it yet, right? we haven't done it yet. | 0.6825 | 平手 |
| 448 | ≫そこから声変わりしても歌声は変わりなく…。 | The singing voice remains unchanged even after the voice changes… | 0.7407 | The singing voice remains unchanged even after the voice changes… | 0.7407 | 平手 |
| 449 | ≫めちゃめちゃ高音じゃないですか。 | isn't that really a really high note? | 0.6362 | isn't that really a really high note? | 0.6362 | 平手 |
| 450 | このあとに話しますけどこの当時、こういう世界に入る | and i'll talk to you later about getting into this world | 0.7574 | and i'll talk to you later about getting into this world | 0.7574 | 平手 |
| 451 | 憧れとかそういう人いたんですか？ | Were you ever someone you admired or someone like that? | 0.8182 | Were you ever someone you admired or someone like that? | 0.8182 | 平手 |
| 452 | ≫憧れはマイケル・ジャクソンですね。 | and my dream is to be a professional translator. michael jackson. | 0.5856 | and my dream is to be a professional translator. michael jackson. | 0.5856 | 平手 |
| 453 | 一番最初はやっぱり。 | and that's the first thing. | 0.6685 | and that's the first thing. | 0.6685 | 平手 |
| 454 | ≫大知先生って最初、和製マイケル・ジャクソンみたいな。 | the first time dr. Ochi-sensei was like a Japanese Michael Jackson. | 0.7285 | the first time dr. Ochi-sensei was like a Japanese Michael Jackson. | 0.7285 | 平手 |
| 455 | そういうふうに言われてたこともあって | and because people were saying things like that, i ended up doing the translation | 0.4035 | and because people were saying things like that, i ended up doing the translation | 0.4035 | 平手 |
| 456 | ダンス淘汰が上手だったから。 | because i was good at dance selection. | 0.7909 | because i was good at dance selection. | 0.7909 | 平手 |
| 457 | マイケル・ジャクソンやっぱり衝撃だった？ | Did Michael Jackson really hit your nerve? | 0.8233 | Did Michael Jackson really hit your nerve? | 0.8233 | liquid后处理 |
| 458 | ≫そうですね。 | that's right. | 0.5932 | that's right. | 0.5932 | 平手 |
| 459 | ≫でもまだ幼い時でしょ。≫自分が初めて見聞きしたのは | but you're still very young. the first thing i saw and heard was | 0.6290 | but you're still very young. the first thing i saw and heard was | 0.6290 | liquid |
| 460 | ６歳、７歳とかそのぐらいでしたけど | She was around six or seven years old. | 0.8052 | She was around six or seven years old. | 0.8052 | 平手 |
| 461 | 唯一無二感というかマイケルのポージングの | the one and only sense of being unique or Michael's posing | 0.7446 | the one and only sense of being unique or Michael's posing | 0.7446 | liquid |
| 462 | 感じだったり。 | it could be just a feeling. | 0.6771 | it could be just a feeling. | 0.6771 | 平手 |
| 463 | ≫やっぱダンスのほうで最初、マイケルすげーなって？ | and after all this time, what's so great about dancing that you thought michael was amazing? | 0.5311 | and after all this time, what's so great about dancing that you thought michael was amazing? | 0.5311 | 平手 |
| 464 | ≫最初はダンスでした。 | The first thing I did was dance. | 0.7804 | The first thing I did was dance. | 0.7804 | 平手 |
| 465 | そこから楽曲とかも聴くようになって。 | And then I started listening to music and things like that too. | 0.7397 | And then I started listening to music and things like that too. | 0.7397 | 平手 |
| 466 | ≫何を聴いたか覚えてる？最初に。 | do you remember what you heard? The first time. | 0.8559 | do you remember what you heard? The first time. | 0.8559 | 平手 |
| 467 | ≫「ブラック・オア・ホワイト」でした。 | and it was black or white. | 0.7036 | and it was black or white. | 0.7036 | 平手 |
| 468 | ミュージックビデオでいろんな国のダンスを | and we did a music video with dances from all over the world | 0.6181 | and we did a music video with dances from all over the world | 0.6181 | 平手 |
| 469 | マイケルが踊っていくのを…。 | I can't believe Michael's dancing...! | 0.6788 | I can't believe Michael's dancing...! | 0.6788 | 平手 |
| 470 | どのジャンルを踊ってもマイケル・ジャクソンに | and no matter what genre you dance in, you're going to be heard by michael jackson | 0.7588 | and no matter what genre you dance in, you're going to be heard by michael jackson | 0.7588 | 平手 |
| 471 | なるというか | and so to speak | 0.5129 | and so to speak | 0.5129 | 平手 |
| 472 | オリジナルな存在にすごく憧れました。 | I really admired the originals. | 0.7569 | I really admired the originals. | 0.7569 | 平手 |
| 473 | ≫お会いしたことあるんですか？ | - Have you met him? | 0.7087 | - Have you met him? | 0.7087 | 平手 |
| 474 | ≫１回、アワードか何かで５〜６ｍ先にいるみたいなのが | -You're supposed to be 5-6 meters away from the award venue or something. | 0.6191 | -You're supposed to be 5-6 meters away from the award venue or something. | 0.6191 | 平手 |
| 475 | １回だけあったんですよ。 | It happened just once. | 0.8746 | It happened just once. | 0.8746 | 平手 |
| 476 | 会話はしてないです。一瞬見たことはあったんですけど。 | We weren't having a conversation, though I did see it briefly. | 0.8183 | We weren't having a conversation, though I did see it briefly. | 0.8183 | 平手 |
| 477 | ≫でも、さっき言ってたようにね。≫声変わりのお話ありましたが | but like you said earlier... there was talk of a voice change | 0.7098 | but like you said earlier... there was talk of a voice change | 0.7098 | 平手 |
| 478 | デビューしてから３年後三浦さん、ある決断をします。 | Three years after your debut, Miura-san makes a certain decision. | 0.8764 | Three years after your debut, Miura-san makes a certain decision. | 0.8764 | liquid |
| 479 | 変声期を迎え活動休止期間へ突入します。 | The voice begins to change during the voice change period and the artist enters a period of inactivity. | 0.6275 | The voice begins to change during the voice change period and the artist enters a period of inactivity. | 0.6275 | 平手 |
| 480 | ≫大知先生は、結構…もうあれはどのくらいで休むんでしたっけ？ | Mr. Ochi-sensei, how much longer do you think you'll have to rest? | 0.7034 | Mr. Ochi-sensei, how much longer do you think you'll have to rest? | 0.7034 | 平手 |
| 481 | ≫ちょうど中学校に上がる時くらいですね。 | It was around the time I was about to enter junior high school. | 0.7428 | It was around the time I was about to enter junior high school. | 0.7428 | 平手 |
| 482 | 小学６年生の。≫結構それで普通に学生生活を | a sixth grader. that's quite enough for student life | 0.7291 | a sixth grader. that's quite enough for student life | 0.7291 | 平手 |
| 483 | 送る期間があったんですよね。 | And there was a period when I had to send it, right? | 0.7212 | And there was a period when I had to send it, right? | 0.7212 | 平手 |
| 484 | それがすごい大知先生を作り上げた要因だと思うんですよ。 | And I think that’s one of the factors that made him such a great master translator. | 0.7045 | And I think that’s one of the factors that made him such a great master translator. | 0.7045 | 平手 |
| 485 | ≫若い時から芸能界いて普通に休んで | you've been in the entertainment industry since you were young and you've been taking time off normally | 0.7052 | you've been in the entertainment industry since you were young and you've been taking time off normally | 0.7052 | 平手 |
| 486 | 学生を…。 | The student...? | 0.8200 | The student...? | 0.8200 | 平手 |
| 487 | ≫普通に部活とかガンガンやってたので。 | because i was really involved in club activities. | 0.5040 | because i was really involved in club activities. | 0.5040 | 平手 |
| 488 | ≫部活は何を？≫部活 | what do you do in club activities? club activities | 0.5962 | what do you do in club activities? club activities | 0.5962 | 平手 |
| 489 | バレーボールやってました。 | i used to play volleyball. | 0.8346 | i used to play volleyball. | 0.8346 | 平手 |
| 490 | ≫そこで普通に学生の友達とか部活やったりとか | and so i was just going to be doing my usual stuff with my student friends and clubs | 0.6525 | and so i was just going to be doing my usual stuff with my student friends and clubs | 0.6525 | 平手 |
| 491 | 学生生活をちゃんと送るんですよね。 | You have to make sure you're doing your student life properly. | 0.7199 | You have to make sure you're doing your student life properly. | 0.7199 | 平手 |
| 492 | どのくらい休んでたんですか？≫休んでたのは５年くらい。 | How long have you been resting? You've been resting for about five years. | 0.8443 | How long have you been resting? You've been resting for about five years. | 0.8443 | 平手 |
