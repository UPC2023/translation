# 翻译质量评估报告 (LaBSE 语义相似度)

- 原文来源: `/home/cyw/pro/train_data/out_liquid.jsonl` (input 字段)
- liquidAi 文件: `/home/cyw/pro/train_data/out_liquid.jsonl`
- opus 文件: `/home/cyw/pro/train_data/opus_out.jsonl`
- LaBSE 模型: `sentence-transformers/LaBSE`
- device: `cpu`

## 统计

- liquidAi 平均得分: 0.6914
- opus 平均得分: 0.5999
- liquidAi 优于 opus: 286
- opus 优于 liquidAi: 202
- 平手: 4
- 参与统计句子数: 492

## 明细对比表

| 序号 | 日语原文 | liquidAi翻译 | liquidAi得分 | opus翻译 | opus得分 | 优胜方 |
|---:|---|---|---:|---|---:|---|
| 1 | Event 7fe4/0420/6cc5 フジテレビ 081 | Event 7fe4/0420/6cc5 Fuji TV 081 | 0.8802 | Event 7fe4/0420/6cc5 Huzi TV 081 | 0.9410 | opus |
| 2 | 04/28（月）09:50:00～11:30:00 | Mon. 28th, 04/28th (Monday) 9:50:00-11:30:00 | 0.8690 | 04/ 28 MONTH)09:50:00:01:30:00 | 0.7561 | liquidAi |
| 3 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Non-stop! [Kobayashi Sachiko Descends on the Niconico Super Conference in a Secret Retreat▽Miura Daichi's 3 Children's Daddy's True Face]�������� | 0.7913 | I'm going to go to a meeting of Jehovah's Witnesses. | 0.1165 | liquidAi |
| 4 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | The Kimio Kobayashi Close-Up on the Nico Nico Super Conference ▽ "At One Point I Was Resigned to Death..." Isao Sasaki's Return Live ▽ Miura Daichi Studio Appearance 3 Children's Papa True Face ▽ Osamu Mukai | 0.8186 | I'm ready to die. | 0.1600 | liquidAi |
| 5 | ≫おはようございます。 | - Good morning. - Good morning. | 0.6421 | Good morning. | 0.6892 | opus |
| 6 | ≫「ノンストップ！」始まりました。 | and now the nonstop! | 0.5119 | It's starting to "No Stop!" | 0.7519 | opus |
| 7 | ≫今週のせきららボイスの投稿テーマは | the theme for this week's sekirara voice post is | 0.7374 | (Laughter) | 0.1157 | liquidAi |
| 8 | 思い出のＧＷです。 | It's a memorable G.W.D. | 0.7408 | This is the GW of my memory. | 0.7601 | opus |
| 9 | 表示されているＱＲコードから皆さん、ぜひ投稿してください。 | Please submit your responses to the QR codes displayed on the screen. | 0.7358 | From the displayed QR code, please post everyone. | 0.8219 | opus |
| 10 | それでは参りましょうか。 | Then shall we go then? | 0.7985 | Shall we go? | 0.7220 | liquidAi |
| 11 | ≫４月２８日、今日も…。≫「ノンストップ！」。 | April 28th, again… "Non-stop!" | 0.7493 | It's April 28th, and today too. | 0.6434 | liquidAi |
| 12 | ≫先週金曜日、「パリピ孔明ＴＨＥ　ＭＯＶＩＥ」の | - Last Friday, you appeared on "Palipi Kongmyeong THE HEP MOKE" | 0.6451 | (Laughter) | 0.1018 | liquidAi |
| 13 | 初日舞台あいさつが行われ | the opening day stage greetings were given | 0.7354 | It was the first day of the show. | 0.5926 | liquidAi |
| 14 | 向井理さん、上白石萌歌さんディーン・フジオカさん | mr. mukai rie, moka joshiraishi, and dean fusjoka | 0.6039 | Mr. Rousseau, Mr. Osama Hikashi, Dean Hugika. | 0.4734 | liquidAi |
| 15 | 宮野真守さんらが登場しました。 | The work featured Mamoru Miyano and others. | 0.5487 | Shinno Shizuno has appeared. | 0.7127 | opus |
| 16 | ≫音楽で戦うことになりました。≫マジで！？ | We ended up fighting with music. Seriously!? | 0.7400 | I'm going to fight with the music. Really? | 0.7735 | opus |
| 17 | ≫向井さん演じる諸葛孔明が現代に転生し | mr. mukai's character zhuge kongming is reincarnated in the present day | 0.6220 | Mr. Ryushui, the perforations that play this place have been transformed into modern times. | 0.4845 | liquidAi |
| 18 | 上白石さん演じるアマチュアシンガー、英子の | the amateur singer, eiko, played by joshiraishi mr. is a professional translator | 0.7341 | I'm going to show you an example of this. | 0.0607 | liquidAi |
| 19 | 軍師となって音楽の力で天下泰平を目指す | I will become a strategist and use the power of music to bring peace to the world. | 0.6011 | I'm going to be a soldier, and I'm going to be the power of music to make peace. | 0.5918 | liquidAi |
| 20 | ド派手エンターテインメント映画です。 | It's a flashy entertainment movie. | 0.8564 | It's a flashy entertainment movie. | 0.8564 | 平手 |
| 21 | 「ノンストップ！」は向井さんや上白石さんら | 'Nonstop!' is a professional translator, including Mukai and Kamishiraishi. | 0.6222 | "No, no, no!" | 0.5530 | liquidAi |
| 22 | 出演者４人に直撃しました。 | The four performers were directly hit. I got hit by four people. | 0.7054 | I hit four actors. | 0.8577 | opus |
| 23 | ≫見どころの１つがライブシーン。 | One of the highlights is the live scene. | 0.8416 | One of them is a live scene. | 0.7527 | liquidAi |
| 24 | 本人役で岩田剛典さんや水森かおりさんなど | The actors include Takanori Iwata and Kaori Mizumori, all playing themselves. | 0.6546 | I'm not sure if you're the person who played it. | 0.1662 | liquidAi |
| 25 | 総勢５０人以上のミュージシャンらが | A group of over 50 musicians came together to create this piece. | 0.6644 | I'm going to give you a few examples. | 0.1551 | liquidAi |
| 26 | 出演していることでも話題を呼んでいます。 | The fact that he appeared on the show has also generated a lot of buzz. | 0.5674 | Even the fact that I'm acting, I'm calling on you. | 0.5779 | opus |
| 27 | そこで、パリピな映画にちなんで | and so, in reference to the movie parliaments, we decided to make a professional translation | 0.4899 | (Laughter) | 0.1424 | liquidAi |
| 28 | 向井さんたちが最もテンションアゲアゲになった | the mukai's got the most excited outbursts | 0.6261 | Mr. Eyoi and the others have become the most tense. | 0.4558 | liquidAi |
| 29 | 出演アーティストを聞いてみると…。 | I looked up the artists featured... | 0.7481 | When I listen to an artist... | 0.7761 | opus |
| 30 | ≫すると、ディーンさんから意外な事実が。 | and then mr. dean made an unexpected revelation. | 0.6641 | If you don't, Dean will tell you something you didn't expect. | 0.5633 | liquidAi |
| 31 | ≫一方、プライベートでの４人は | The four members in private, however, | 0.7364 | I'm going to talk about four people in private. | 0.5666 | liquidAi |
| 32 | どんな時にテンションが上がるのでしょうか。 | When do you get excited? What makes you get excited? | 0.7414 | When will the tone go up? | 0.7523 | opus |
| 33 | ≫Ｔｈｅ　ＣｕｒｅっていうＵＫの | The UK's UK-based company T-Her-Curse is called T-Her-Curse. | 0.2660 | It's called the UK. | 0.2559 | liquidAi |
| 34 | レジェンドバンドが私大好きでして。 | and i love my university to be a legend. | 0.4299 | I love the Regend Band. | 0.8106 | opus |
| 35 | ≫向井理も…。≫上白石萌歌も…。 | Mukai Osamu also…? Ueshiraishi Moka also…? | 0.6226 | I'm sure I'll be able to help you. | 0.0837 | liquidAi |
| 36 | ≫ディーン・フジオカも…。≫宮野真守も…。 | Dean Fujioka too…? Mamoru Miyano too…? | 0.7898 | It's not just me, it's me. | 0.1342 | liquidAi |
| 37 | ≫「ノンストップ！」。 | and nonstop! | 0.5501 | "No stop!" | 0.6832 | opus |
| 38 | ≫昨日、ミュージカル「キンキーブーツ」の | yesterday, we watched a performance of the musical "The Kinky Boots" | 0.7369 | (Laughter) | 0.1827 | liquidAi |
| 39 | 初日公演が行われました。 | The opening day performance was held. | 0.8315 | The first day performance was performed. | 0.8906 | opus |
| 40 | アメリカの演劇界で最も権威のあるトニー賞で | the most prestigious tony awards ceremony in american theatre | 0.8239 | It's the best Tony award in the American theater. | 0.8070 | liquidAi |
| 41 | 作品賞を含む６冠を達成したミュージカル。 | The musical has won six awards, including Best Picture. | 0.7877 | The musical that achieved the sixth crown, including the work award. | 0.7970 | opus |
| 42 | カーテンコールでは音楽・作詞担当の | the curtain call features the composer and lyricist | 0.6124 | (Laughter) | 0.0978 | liquidAi |
| 43 | 世界的歌姫にして大の親日家としても知られる | a world-renowned songstress and known as a great Japanophile | 0.7695 | He's also known as a world singer and a great matron. | 0.8005 | opus |
| 44 | シンディ・ローパーがサプライズ出演。 | Cindy Roeper makes a surprise appearance. | 0.7124 | Cindy Roper was a surprise show. | 0.6763 | liquidAi |
| 45 | ステージに花を添えました。 | and we've added some flowers to the stage. | 0.7172 | I added flowers to the stage. | 0.8683 | opus |
| 46 | ≫しみじみと語るのは「宇宙戦艦ヤマト」など | the things that I'm really talking about are things like space battleship yamato | 0.5643 | And I'm going to tell you a little bit about that. | 0.0514 | liquidAi |
| 47 | 数々の伝説的アニソンを歌ってきた | and sang many legendary anime songs | 0.7795 | I've been singing a number of legendary Anisons. | 0.8089 | opus |
| 48 | アニソン界の大王ことささきいさおさん、８２歳。 | The King of the Anime Song World, Mr. Isao Sasaki, 82 years old. | 0.7764 | The great King of the Anison world, Mr. Oldman, is 82 years old. | 0.6991 | liquidAi |
| 49 | 昨日、都内で行われたアニソンイベントに | i attended an anime song event held in tokyo yesterday | 0.7146 | I'm going to show you an example of this. | 0.2185 | liquidAi |
| 50 | 出演したのです。 | and so i appeared on the show. | 0.5487 | I was in the theater. | 0.6612 | opus |
| 51 | ≫ありがとう！ | - Thank you! | 0.7486 | Thank you! | 0.8587 | opus |
| 52 | ≫実はささきさん、今年１月 | actually, sasakisan went to work as a professional translator this january | 0.5093 | Akira-san, this year | 0.6321 | opus |
| 53 | 地下鉄に乗っている時に突如、気絶。 | I suddenly lost consciousness while riding the subway. | 0.8295 | When I was on the subway, I suddenly fainted. | 0.8266 | liquidAi |
| 54 | その後、自力で自宅まで戻るも救急搬送。 | After that, he returned home on his own but was rushed to the hospital by ambulance. | 0.7910 | After that, I could come back home on my own. | 0.6774 | liquidAi |
| 55 | 医師から間質性肺炎急性増悪と診断され、入院していました。 | The doctor diagnosed my condition as acute exacerbation of interstitial pneumonia and I was hospitalized. | 0.8091 | I was diagnosed by the doctor as a trans-polytic pneumonia, and I was in the hospital. | 0.6208 | liquidAi |
| 56 | 退院後も自宅療養とリハビリ生活を | and continue to live at home and undergo rehabilitation after being discharged | 0.7498 | After he was discharged from the hospital, he was in a nursing home and rehab. | 0.6302 | liquidAi |
| 57 | 送っていたという、ささきさん。 | Sasakisan said you were sending it. | 0.7785 | Akira-san said he was sending it. | 0.6930 | liquidAi |
| 58 | どういう症状だったのでしょうか。 | What kind of symptoms were you experiencing? | 0.8623 | What kind of symptoms did she have? | 0.8650 | opus |
| 59 | ≫一般的に血液中に含まれる酸素の量が | in general, the amount of oxygen in the blood | 0.8502 | It's called the blood cell. | 0.1680 | liquidAi |
| 60 | ９０％を切ったら危ないといわれているところ | It's said that if it falls below 90%, it's dangerous. | 0.7741 | They say it's dangerous if you cut 90 percent of it. | 0.8132 | opus |
| 61 | 診察時、何と５０％しかなかったという、ささきさん。 | Sasaki said that only 50% of what she was able to translate at the time of the examination actually came out. | 0.6751 | At the time of the examination, there was only 50 percent of it. | 0.7532 | opus |
| 62 | 一時は死を覚悟したといいます。 | and at one point he was prepared to die. | 0.6347 | I say I'm prepared for death for a time. | 0.6326 | liquidAi |
| 63 | ≫しゃべるのも苦しかった中 | and it was hard for me to talk too | 0.7309 | I've had a lot of trouble talking. | 0.5983 | liquidAi |
| 64 | まさに奇跡の復活を遂げたささきさん。 | It was truly a miracle that Sasaki-san had achieved such a miraculous resurrection. | 0.7274 | Mr. Takeshi, who has brought back the miracle. | 0.6122 | liquidAi |
| 65 | 昨日のライブではロボットアニメの主題歌４曲を | - We played four songs from the robot anime theme song for our show yesterday. - No explanations or extra commentary, just the translation. | 0.6543 | I'm going to show you a live video. | 0.2379 | liquidAi |
| 66 | およそ２０００人の観客の前で熱唱しました。 | I sang passionately in front of an audience of about 2,000 people. | 0.8371 | I sang in front of about 2,000 spectators. | 0.8907 | opus |
| 67 | そんな、ささきさんの今のささやかな楽しみは…。 | And what a small pleasure Sasaki has now...? | 0.7279 | That's not the kind of little fun you're having right now. | 0.5085 | liquidAi |
| 68 | ≫大好きなお酒を楽しめるまで回復したようです。 | and seems to have recovered enough to enjoy my favorite alcoholic beverages. | 0.7711 | I think I've recovered until I can enjoy my favorite drink. | 0.7579 | liquidAi |
| 69 | ≫生涯現役宣言。 | he declares himself to be active throughout his life. | 0.4994 | I've been active all my life. | 0.3785 | liquidAi |
| 70 | 今年７月にはデビュー６５周年記念イベントも | This July, we will also hold a 65th anniversary event to commemorate our debut. | 0.7960 | We're going to have our 65th anniversary in July of this year. | 0.7455 | liquidAi |
| 71 | 控えているということで | and since you're holding onto it | 0.5300 | That's why we're here. | 0.1906 | liquidAi |
| 72 | パワフルな歌声をまだまだ聴かせてくれそうです。 | and she's still going to give off a powerful voice. | 0.6632 | I'm afraid he's still going to let me hear his powerful voice. | 0.6724 | opus |
| 73 | 優勝はガクテンソク！ | The champion goes to Gakuten Sokku! | 0.6816 | The winner's gotta be a giant! | 0.7371 | opus |
| 74 | ≫結成１６年以上のベテラン漫才師たちが | The veteran manzai performers who have been active for over 16 years have decided to form a group | 0.6213 | It's been a long time since I was born. | 0.1221 | liquidAi |
| 75 | セカンドチャンスをかけて戦う賞レース | a race for the very first chance! | 0.5027 | A race to fight with a second chance. | 0.7515 | opus |
| 76 | ３回目の開催となる今年 | This year, the third time the event has been held, we have been working with professional translators. | 0.5097 | This is the third time we've held this year. | 0.7487 | opus |
| 77 | グランプリファイナルに勝ち上がった８組が | The eight teams that advanced to the Grand Prix Final will compete in the Grand Prix Final. | 0.6573 | The eight teams that won the Grand Prix... | 0.6753 | opus |
| 78 | 組み合わせ抽選会を行いました。 | The combination draw was held. | 0.8040 | I've held a combination summary meeting. | 0.7130 | liquidAi |
| 79 | １回戦の注目カードは結成５３年 | The featured matchup of the first round is the 53-year-old team. | 0.6230 | The attention card for the first round was made 53 years ago. | 0.6748 | opus |
| 80 | 昭和の漫才ブームの一翼を担った、ザ・ぼんちと | the Bonchi, who played a part in the manzai boom of the shōwa era | 0.6326 | I'm going to tell you a little bit about this. | -0.0249 | liquidAi |
| 81 | ３回連続グランプリファイナル出場の | - You've qualified for the Grand Prix Final three times in a row. | 0.7167 | I'm going to show you a couple of examples. | 0.1207 | liquidAi |
| 82 | 金属バットが激突。 | a metal bat hits you. | 0.7424 | The metal bat bursts. | 0.8350 | opus |
| 83 | ≫レジェンドのザ・ぼんちの快進撃なるか？ | do you think the legendary z the bonchi's on a roll? | 0.4295 | Are you sure it's the dark march of Zorregend? | 0.4215 | liquidAi |
| 84 | グランプリファイナルは来月１７日放送予定です。 | The Grand Prix Final is scheduled to air on the 17th of next month. | 0.8834 | The Grand Prix is scheduled to be broadcast on the 17th of next month. | 0.8320 | liquidAi |
| 85 | ≫５歳の女の子も７０代のご婦人も | A five-year-old girl and a woman in her 70s are both translating texts. | 0.6380 | A five-year-old girl and a 70-year-old woman. | 0.7597 | opus |
| 86 | 満面の笑みにさせていたのは | and the thing that made me smile so hard was that i was able to translate | 0.5060 | (Laughter) | 0.3787 | liquidAi |
| 87 | 先週金曜日からゴールデンウィークに合わせて | and since last friday, we've been working on this for golden week | 0.5939 | Last Friday, I was with Golden Week. | 0.5871 | liquidAi |
| 88 | 開催されている | The event is underway. | 0.5628 | It's open. | 0.3750 | liquidAi |
| 89 | 「アイスクリーム万博」通称「あいぱく」。 | The "Ice Cream Expo," also known as "Aipaku." | 0.7777 | Ice cream Fowler's name is "Create." | 0.5247 | liquidAi |
| 90 | 今回で１０周年。 | This is the 10th anniversary. | 0.8061 | This is the 10th anniversary. | 0.8061 | 平手 |
| 91 | 累計来場者数４４０万人を超える | The cumulative number of visitors exceeds 440,000. | 0.7901 | Over 4.4 million people. | 0.7008 | liquidAi |
| 92 | 国内最大級のアイスクリームイベントで | the largest ice cream event in the country | 0.8648 | At one of the largest ice cream events in the country | 0.8313 | liquidAi |
| 93 | 全国のアイスマニアが厳選したアイスを | an ice cream carefully selected by ice maniacs across the country | 0.7977 | I'm going to tell you a little bit about ice cream. | 0.2115 | liquidAi |
| 94 | １８０種類以上食べられるんです。 | I can eat over 180 different kinds of food. | 0.8800 | You can eat more than 180 different kinds of food. | 0.8619 | liquidAi |
| 95 | 場内を回っていると…。 | As I walked around the stadium... | 0.7865 | When I'm going around the room... | 0.8213 | opus |
| 96 | ≫突然、ダッシュで列を作るお客さん。 | and suddenly a customer is running up the line in a dashboard. | 0.6237 | All of a sudden, you make a row of dashes with dashes. | 0.5900 | liquidAi |
| 97 | ≫この、突如できた行列の正体。 | the identity of this suddenly formed procession. | 0.5511 | The identity of the matrix that came out of nowhere. | 0.3333 | liquidAi |
| 98 | 実は、まだ発売前の新商品を無料配布していたんです。 | I was actually giving away pre-release new products for free. | 0.8972 | Actually, I was still distributing free new products before they were released. | 0.9049 | opus |
| 99 | ≫無料アイスまでもらえる | I can even get a free ice cream. | 0.6317 | I'll even get free ice cream. | 0.6460 | opus |
| 100 | ファンにはたまらないこのイベント。 | This event is something fans will absolutely love. | 0.8175 | It's this event that's so special to fans. | 0.8110 | liquidAi |
| 101 | 監修するのは年間１０００種類以上の | The project is supervised by over 1,000 translators a year. | 0.6771 | I'm going to tell you a little bit about this. | 0.0431 | liquidAi |
| 102 | アイスを食べる専門家アイスマン福留さん。 | The ice cream expert, Mr. Fukudome, is an expert at eating ice cream. | 0.6673 | Ice Man's Reservation. | 0.3341 | liquidAi |
| 103 | ≫ということで厳選に厳選を重ねた、全国のアイスの中でも | and so we carefully selected the ice cream from all over the country | 0.6503 | It's not a big deal. It's a big deal. | 0.0171 | liquidAi |
| 104 | アイスマン福留さんが特にオススメする | The Iceman Fukudome particularly recommends this translation: | 0.6435 | I'm sorry, I'm sorry. I'm sorry. | 0.0335 | liquidAi |
| 105 | ２品を、ご紹介します。 | I'd like to introduce two dishes to you. | 0.7415 | I'd like to introduce you to two items. | 0.7960 | opus |
| 106 | 最初は一見、普通なソフトクリーム。 | At first glance, it looks like normal soft-serve ice cream. | 0.8153 | At first glance, normal soft cream. | 0.8629 | opus |
| 107 | しかし、口にすると…。 | But when I say it... | 0.8741 | But when I say it... | 0.8741 | 平手 |
| 108 | ≫ふわふわな口当たりに驚く人が続出していたのが | and many people were surprised by the fluffy texture | 0.5588 | It's a very simple thing to do. | 0.0120 | liquidAi |
| 109 | 北海道の人気店、ましゅれのジャージー牛乳ソフト。 | The popular shop in Hokkaido, Mashure no Jersey Milk Soft serve Jersey Milk Soft serve. | 0.8014 | The popular restaurant in Hokkaido, and the Jersey milk software in Hokkaido. | 0.7504 | liquidAi |
| 110 | 地元のジャージーミルクと砂糖のみで作ったソフトクリーム。 | A soft-serve ice cream made only with local jersey milk and sugar. | 0.8678 | Local Jersey milk and sugar only make soft cream. | 0.7968 | liquidAi |
| 111 | ふわふわ感を出す秘密が…。 | The secret to creating that fluffy feel… is… | 0.7664 | The secret that makes me feel so good... | 0.7336 | liquidAi |
| 112 | こちら、世界最高峰のソフトクリームマシン。 | This is the world's most advanced soft-serve ice cream machine. | 0.7667 | This is the world's highest soft cream machine. | 0.8395 | opus |
| 113 | お値段は何とおよそ３００万円！ | The price is about 3 million yen! | 0.8609 | The price is about three million yen! | 0.8566 | liquidAi |
| 114 | その高級さと、イタリアで生産されていることから | and because it's so expensive and made in italy | 0.7656 | And that's what I'm talking about. | 0.1780 | liquidAi |
| 115 | ソフトクリーム界のフェラーリと呼ばれているんです。 | and they're called the ferrari of soft serve ice cream. | 0.7007 | It's called a Ferrari in soft cream. | 0.7338 | opus |
| 116 | 最大の特徴はきめの細かい気泡で | and the most distinctive feature is the fine grain of the bubbles | 0.7421 | The biggest feature is the fine air bubbles. | 0.7753 | opus |
| 117 | ふわっふわな食感のソフトクリームを作れること。 | The ability to create soft ice cream with a fluffy texture. | 0.7216 | Making soft cream with a soft sense of food. | 0.8013 | opus |
| 118 | アイスの口当たりを決める空気の量を | the amount of air that determines the texture of ice cream | 0.7819 | I'm going to give you the amount of air that determines how much ice cream you're wearing. | 0.5686 | liquidAi |
| 119 | 素材に合わせて絶妙に調整できるため | and because it can be perfectly adjusted to match the material | 0.7864 | It's a little bit more complicated than that. | 0.0270 | liquidAi |
| 120 | この食感を生み出せるんです。 | and we can create this texture. | 0.6503 | I can create this sense of food. | 0.8697 | opus |
| 121 | ≫一方こちらは何やら、ぷつぷつしたものが | and on the other hand, something like a shaky shaky object | 0.6191 | (Laughter) | 0.1001 | liquidAi |
| 122 | 練り込まれているアイス。 | The ice cream is well-crafted. | 0.5036 | The ice cream that's been woven into it. | 0.6384 | opus |
| 123 | ≫お客さんが感じた甘じょっぱさ。 | The sweetness and saltyness that the customer felt. | 0.6911 | It's the sweetest thing the customer felt. | 0.6521 | liquidAi |
| 124 | 実はこれ、ベーコンが練り込まれたアイスなんです。 | This is actually a bacon-infused ice cream. | 0.8863 | Actually, it's an ice cream with bacon in it. | 0.8315 | liquidAi |
| 125 | これを作ったのは、横須賀市の人気アイスクリームパーラー。 | The ice cream parlor in Yokosuka City created this. | 0.7708 | It's the popular ice-cream parlor in the city of Sakata. | 0.6716 | liquidAi |
| 126 | 店主がアメリカで食べたメープルシロップと | the owner ate maple syrup in america | 0.7770 | I'm going to give you a couple of examples. | 0.0846 | liquidAi |
| 127 | ベーコン、ドーナツを組み合わせた | and i combined bacon and donuts | 0.7029 | I put bacon and donuts together. | 0.6602 | liquidAi |
| 128 | 甘じょっぱい料理から着想を得たそうです。 | It seems to have been inspired by sweet and salty dishes. | 0.7592 | She said that she was inspired by the sweet food. | 0.7332 | liquidAi |
| 129 | ≫世界最高峰のソフトクリームから | from the world's finest soft serve ice cream | 0.7383 | From the soft cream of the world's highest mountain | 0.7251 | liquidAi |
| 130 | 変わり種アイスまで楽しめる「あいぱく」。 | The “Aipaku” offers even the most unusual kinds of ice cream. | 0.6493 | "Chinese" can be fun to the new ice cream. | 0.5398 | liquidAi |
| 131 | そして、アイス好きの夢である | and my dream of being an ice enthusiast | 0.8357 | It's a dream of ice cream. | 0.5922 | liquidAi |
| 132 | あれ食べてみたいですねふわふわするソフトクリーム。 | I'd really like to try that fluffy soft-serve ice cream. | 0.7745 | I'd like to try that soft cream. | 0.8049 | opus |
| 133 | ≫どんな感じなんですかねちょっと、想像が…。 | I wonder what it feels like, just a little… I can’t quite picture it… | 0.6152 | I don't know what it's like. I can't imagine... | 0.5925 | liquidAi |
| 134 | ≫あそこ会場行く人って何個も食べるんですかね。 | i wonder how many people there are going to the venue who will eat so many things. | 0.6891 | Does someone who goes to the hall over there eat many? | 0.7560 | opus |
| 135 | ≫アイスしかないですもんね「あいぱく」は。 | the ice cream's all we got... "Aipaku"? | 0.5737 | There's no more ice cream, right? "Chinese." | 0.5161 | liquidAi |
| 136 | ≫大好きな人は何個も何個も食べてね。 | and eat as many pieces as you like. | 0.5592 | If you love me, I'll eat a lot of food. | 0.5700 | opus |
| 137 | ≫お土産でも買って帰れそうですね。 | i could probably buy some souvenirs for you too. | 0.6752 | I can buy some souvenirs and go home. | 0.7215 | opus |
| 138 | ≫そんな「あいぱく」ですが | but that kind of "aipaku" | 0.6680 | (Laughter) | 0.2964 | liquidAi |
| 139 | 食べ比べされている方多かったんですね。 | So a lot of people were comparing the tastes of the foods. | 0.6426 | There were so many of them that were compared to them. | 0.7198 | opus |
| 140 | そして皆さんにもぜひ食べ比べ楽しんでいただきたいです。 | And I really hope that you will enjoy comparing the flavors with everyone. | 0.7236 | And I really want you to eat and enjoy it. | 0.7639 | opus |
| 141 | 今回はイベントを監修するアイスマン福留さんイチ押し | This time, we have Iceman Fukudome, who oversees the event, as our main translator. | 0.6731 | This time, I'm going to have to take care of the event. | 0.5239 | liquidAi |
| 142 | 桃の食べ比べアイススタジオにご用意しました。 | We prepared it for Peach Food Tasting Ice Studio. | 0.7846 | I've prepared it for the ice cream studio, compared with the peach diet. | 0.7470 | liquidAi |
| 143 | 食べ比べるのは山梨県の農家さんが作っている | The farmers in Yamanashi Prefecture are making it for you to compare the two. | 0.6383 | It's made by a farmer in Yamanashi prefecture. | 0.6911 | opus |
| 144 | ６種類の桃のジェラートの中から２種類。 | You can choose from two types of gelato with six different peach flavors. | 0.7156 | There are two kinds of peas out of six different gelattos. | 0.7363 | opus |
| 145 | 特に人気の高かった夏かんろ、黄金桃。 | The most popular summer fruits, golden peaches, were especially popular. | 0.8508 | The most popular summer party, the golden peach. | 0.7113 | liquidAi |
| 146 | まずは皆さん、夏かんろからいってらっしゃいませ。 | First off, everyone, please get ready for summer. | 0.7693 | First of all, we can't all go to the summer kitchen. | 0.6008 | liquidAi |
| 147 | ≫おいしい！うわ、すごい桃！ | It's delicious! Wow, that's a amazing peach! | 0.8183 | It's delicious! Wow! Wow! | 0.7409 | liquidAi |
| 148 | ≫果肉も入ってますね！ | The flesh is also included! | 0.7506 | There's also chicken in there! | 0.6952 | liquidAi |
| 149 | ≫食べた瞬間は桃のアイスだなって感じするけど | the moment you eat it, it feels like peach ice cream, but | 0.7943 | You know, the moment I eat it, I feel like a peach ice cream. | 0.7885 | liquidAi |
| 150 | そのあとに、ぐわっと桃の香りが。すっごいおいしい！ | And then, just a hint of peach aroma. It's amazingly delicious! | 0.8242 | After that, there's the smell of sweets and peachs. It's delicious! | 0.8147 | liquidAi |
| 151 | めちゃくちゃうまい、これ。 | this is seriously delicious! | 0.7503 | This is really good. | 0.8018 | opus |
| 152 | ≫１００％全力の桃果肉の食感を残したジェラートで | - With gelato retaining the texture of 100% fully-focused peach flesh. | 0.7075 | It's called "Gerrat." | -0.0032 | liquidAi |
| 153 | ねっとりした食感が最大の特徴ということです。 | The most distinctive feature is its sticky texture. | 0.7105 | The sense of smell is the greatest feature. | 0.7640 | opus |
| 154 | これが夏かんろでした。 | and this was the summer flood. | 0.7591 | This was the summer shower. | 0.9008 | opus |
| 155 | 続いて、黄金桃のほうも楽しんでいただきたいです。 | And I hope you enjoy the golden peach too. | 0.8008 | I'd like you to enjoy the golden peach as well. | 0.8374 | opus |
| 156 | こちら、桃農家さんによりますとジューシーな甘みとうまみが特徴。 | This peach farmer's peach is characterized by its juicy sweetness and umami flavor. Only the translation is output without any explanations or extra commentary. | 0.5812 | This is the sweet sweet spot characteristic of a peach farmer. | 0.6665 | opus |
| 157 | 皆さん、お願いいたします。召し上がれ。 | Please, everyone, I beg you. Have a meal. | 0.8118 | Please, everyone. Enjoy your meal. | 0.7259 | liquidAi |
| 158 | ≫あっ、違う。あー！おいしい！こっちもうまい。 | Oh, no, no! Oh! It's delicious! It's good here! | 0.7619 | No, it's not. It's delicious! It's good too. | 0.6042 | liquidAi |
| 159 | ちょっと違いますね。 | It's a little different. | 0.9012 | It's a little different. | 0.9012 | 平手 |
| 160 | ≫夏かんろの桃感がすごかったから | 'because the feeling of the summer sun over my peach skin was amazing | 0.6786 | I couldn't stop thinking about it. | 0.0915 | liquidAi |
| 161 | ちょっとあっさりには思えるよね。 | It might seem a bit casual, you know. | 0.7183 | It's kind of easy to think of. | 0.6220 | liquidAi |
| 162 | ≫何だろう、こっちのほうがいわゆる缶詰なんかに入ってた | i wonder what it is? it was in a kind of canned food here | 0.6119 | I don't know. This one was in what we call cans. | 0.6178 | opus |
| 163 | 黄色いもの…。あっ、おいしい！ | The yellow one… oh, it’s delicious! | 0.9085 | A yellow one... Oh, it's delicious! | 0.9237 | opus |
| 164 | ≫迷う！≫夏かんろ、うまいな。 | I'm lost! Summer is so delicious! | 0.7134 | I'm lost! I'm good at the Kusaka-kun. | 0.5222 | liquidAi |
| 165 | 夏かんろ、最初に食べたからかインパクトが。 | the summer yam soup had an impact because i ate it first. | 0.7593 | I've eaten it first, or I've had its impact. | 0.6332 | liquidAi |
| 166 | ≫桃に関しては６種類ありますからね。 | and there are six different kinds of peaches. | 0.7355 | There are six kinds of tonsils with respect to tonsils. | 0.6555 | liquidAi |
| 167 | ≫じゃあ食べ比べこれこそ本当にね。 | then this is really the best food comparison i've ever seen. | 0.5590 | That's really what I'm talking about. | 0.4878 | liquidAi |
| 168 | ≫ぜひとも皆さんに行っていただきたいです。 | We would definitely encourage everyone to take a look. | 0.3774 | I'd like you all to go. | 0.6180 | opus |
| 169 | 大人気の「あいぱく」来月６日までやっています。 | The hugely popular "Aipaku" is running until the 6th of next month. | 0.8966 | I'm doing it on the sixth of next month. | 0.5119 | liquidAi |
| 170 | ゴールデンウィーク中に足を運んでみては | and why don't you come visit during golden week | 0.5384 | Why don't you take your feet all the way to the Golden Week? | 0.5210 | liquidAi |
| 171 | いかがでしょうか。≫続いては歌手の小林幸子さん。 | and here comes the singer, kobayashi Sachiko. | 0.5213 | How would you like to go on with it? | 0.3376 | liquidAi |
| 172 | この週末に行われた大規模イベント出演に密着です。 | It follows the appearance of a large-scale event held this weekend. | 0.7501 | I'm very attached to this weekend's large event show. | 0.8220 | opus |
| 173 | 分け隔てなく若者と接する神対応ぶりが見えてきました。 | It became apparent how God treats young people without discrimination. | 0.7486 | I'm beginning to see God's way of dealing with young people without separation. | 0.7353 | liquidAi |
| 174 | ≫昨日、幕張メッセで突如湧き起こったラスボスコール。 | The final boss suddenly burst forth at Makuhari Messe yesterday. It was a professional translation. Only the translation was output without any explanations or additional commentary. | 0.3599 | The Rascore that broke out at the stage yesterday. | 0.4748 | opus |
| 175 | この人だかりの中心にいたのは…。 | The one at the center of this crowd was... | 0.8657 | This man was at the heart of the anchor. | 0.6859 | liquidAi |
| 176 | ≫ラスボスの異名を持つ小林幸子さん、７１歳。 | The seven-year-old Sachiko Kobayashi, nicknamed the "Rasboss," is a professional translator. | 0.5048 | Kooka Kokoko, whose name is Sakurasbo, is 71 years old. | 0.7426 | opus |
| 177 | この週末幕張メッセで開催された | this weekend at makuhari messe | 0.6555 | It's been held this weekend at the stage of the show. | 0.6308 | liquidAi |
| 178 | ネット発の文化をリアルで体験できる | You can experience the culture originating on the internet in a realistic setting. | 0.7965 | It's not just the Internet, it's the Internet. | 0.2868 | liquidAi |
| 179 | 日本最大級のイベント | The largest event in Japan | 0.9114 | Japan's largest event | 0.9407 | opus |
| 180 | 「ニコニコ超会議２０２５」に出演しました。 | I appeared on "Niconico Super Conference 2025". | 0.8244 | I appeared at Nicholas Supervised 2025. | 0.6835 | liquidAi |
| 181 | コスプレや推し活などみんなの好きを | i'll do everything i can to help you enjoy your cosplay or fan activities | 0.5809 | And I'm going to show you some examples of what I'm going to do. | 0.0667 | liquidAi |
| 182 | 思いきり表現できるイベントとして | as an event where you can express yourself fully | 0.7830 | I'm going to show you a couple of examples. | 0.2864 | liquidAi |
| 183 | ２日で１３万人以上が来場。 | The event drew over 130,000 visitors in two days. | 0.7677 | Over 130,000 people will be there in two days. | 0.8476 | opus |
| 184 | その模様は全世界に生配信されるという | and it will be live-streamed to the entire world | 0.7286 | It's not just a picture. It's a picture. | 0.2081 | liquidAi |
| 185 | ビッグイベントです。 | it's a big event. | 0.9275 | It's a big event. | 0.9098 | liquidAi |
| 186 | そんなビッグイベントでの幸子さんといえば…。 | And speaking of Sachiko-san at such a big event... | 0.7509 | Speaking of Sachiko at such a big event... | 0.7907 | opus |
| 187 | ≫鶴に乗って空を飛んだり…。 | - You can fly in the sky on a crane... | 0.7062 | Sometimes I fly in the sky on a crane... | 0.6791 | liquidAi |
| 188 | ボブ・サップとプロレスをしたり…。 | Playing professional wrestling with Bob Sapp... | 0.6800 | Bob Sap and Prolete... | 0.5989 | liquidAi |
| 189 | ギャルになったりと今年で１３回連続出演。 | She has appeared 13 times in a row this year, including becoming a "gal" (a young woman who has become a professional model). | 0.6528 | It's been 13 consecutive performances this year. | 0.7376 | opus |
| 190 | 毎年、新たなことに挑戦し観客を驚かせています。 | The audience is surprised every year by the new challenges they take on. | 0.7793 | Every year, I try new things to surprise the audience. | 0.8752 | opus |
| 191 | 今年は何を見せてくれるのか。 | What will they have to show you this year? | 0.8974 | What will you show me this year? | 0.9253 | opus |
| 192 | 「ノンストップ！」は | and nonstop! is a professional translator | 0.4688 | (Laughter) | 0.3560 | liquidAi |
| 193 | 「ニコニコ超会議」に出演する幸子さんの２日間に密着しました。 | We followed Sachiko-san closely for two days while she appeared on the TV program "Niconico Super Conference". | 0.8150 | I got stuck with Sachiko during the two days she's in the Nicholas Super Meeting. | 0.7759 | liquidAi |
| 194 | ≫年末ありがとうございます。 | thank you for your help at the end of the year. | 0.6715 | Thank you for the end of the year. | 0.8128 | opus |
| 195 | ≫お客さんに楽しんでもらいたい！ | I want our customers to enjoy it! | 0.8366 | I want my guests to enjoy themselves! | 0.7913 | liquidAi |
| 196 | そんな一心でまず向かったのは…。 | And so my first step was to go for that… | 0.6945 | The first thing I went for was... | 0.7418 | opus |
| 197 | ≫ゲストや視聴者がリアルタイムで持ち込んだ | the guests and viewers brought their own texts in realtime | 0.7861 | It's not just about the Internet. | 0.1504 | liquidAi |
| 198 | 差し入れで作るという | and make it with gifts | 0.5458 | It's called "Students." | 0.1085 | liquidAi |
| 199 | 唯一無二のカレーを注文できるブース。 | The booth where you can order a unique curry. | 0.7974 | Booth, you can order the only single curry. | 0.6405 | liquidAi |
| 200 | 幸子さんは、地元・新潟の名物車麩を差し入れし | mrs. sachiko brought in a special local Niigata noodle noodle cake called fu, and she added her own special translation of the local local Niigata specialty | 0.6443 | It's called "Sachiko." | 0.2036 | liquidAi |
| 201 | オリジナルの車麩入りカレーを試食しました。 | I tried the original curry with wheat gluten. | 0.8505 | We tried our original car car car car car car car car car car car car. | 0.5561 | liquidAi |
| 202 | ≫幸子さんオススメのカレーを紹介すると…。 | When I introduce my favorite curry recipe recommended by Sachiko... | 0.7009 | If I introduce Sachiko-san's curry... | 0.6368 | liquidAi |
| 203 | 広い会場を縦横無尽に移動する幸子さん。 | Sachiko moves freely around the large venue. | 0.7454 | Sachiko, who moves around the large hall in an endless way. | 0.7485 | opus |
| 204 | 続いてやってきたのは…。 | And now comes the next thing... | 0.7503 | The next thing I've been doing... | 0.7306 | liquidAi |
| 205 | ≫幸子さんが最強キャラとしてデザインされた | the kouko san character was designed as the strongest character | 0.6979 | Sachiko was designed to be the best character in the world. | 0.5919 | liquidAi |
| 206 | カードゲームの販売ブース。 | a card game sales booth. | 0.9226 | The sales booth for the card game. | 0.8209 | liquidAi |
| 207 | 見るからに強そうなイラストをファンにも自慢し | and proudly show off to her fans her strikingly strong illustrations | 0.7068 | I'm proud of my fans. | 0.4046 | liquidAi |
| 208 | 購入者一人ひとりと満面の笑みで記念撮影に応じる神対応です。 | The God-Responding Service allows each buyer to respond to a commemorative photo shoot with a big smile on their face. Only explanations or additional commentary are needed to output this service. | 0.5402 | One buyer and one full smile are God's response to the memorial shoot. | 0.7019 | opus |
| 209 | ≫親子で幸子推しだというファンは…。 | The fans who are devoted to Sachiko are… parents and children… | 0.5844 | The fans who say it's a parent and a child are... | 0.6701 | opus |
| 210 | ≫記念撮影を終えるとまたせわしなく移動する幸子さん。 | After finishing the photo session, Sachiko moves around frantically. | 0.6459 | Sachiko-san, when she finished her photo shoot, was forced to move again. | 0.5770 | liquidAi |
| 211 | ≫だからあたしも芸能人だけど | that's why i'm a celebrity too, but | 0.6800 | I'm an entertainer, too. | 0.4929 | liquidAi |
| 212 | 芸能人ともまたちょっと違う…。 | It's a little different from being a celebrity... | 0.7467 | The entertainers are also a little different... | 0.7164 | liquidAi |
| 213 | ≫みんな会ったら友達。 | and when we meet, we're friends. | 0.6484 | When we meet, we're friends. | 0.7049 | opus |
| 214 | 芸歴６０年を超える大ベテランとは思えない | It doesn't seem like a veteran with over 60 years of experience. | 0.7968 | I don't think he's been a big fan of 60 years. | 0.7419 | liquidAi |
| 215 | フレンドリーさとフットワーク。そして…。 | A touch of friendliness and good footwork. And... | 0.6169 | Friendlyness and footwork. And... | 0.7181 | opus |
| 216 | ≫ライブがあると伺いました。 | I was told that there will be a live concert. | 0.6865 | I've heard there's a live life. | 0.6779 | liquidAi |
| 217 | ≫幸子さんの１日目を締めくくるライブブースへ移動します。 | We will now move to the live booth where we will conclude Sachiko’s first day. | 0.6858 | I'm going to move to the living room that's starting to close Sachiko's day. | 0.5890 | liquidAi |
| 218 | 今回はスペシャルコラボということで | and since this time it's a special collaboration | 0.7690 | This time, I'm a special corroboror. | 0.6231 | liquidAi |
| 219 | 衣装に着替えた幸子さんを待っていたのは…。 | The one waiting for Sachiko as she changed into her costume was...? | 0.7329 | The one waiting for Sachiko who changed her clothes... | 0.7496 | opus |
| 220 | ≫すごいですね、素敵です。 | that's great. it looks wonderful. | 0.7227 | It's amazing, isn't it? It's nice. | 0.6885 | liquidAi |
| 221 | ≫６人組ダンス＆ボーカルグループの | The six-member dance & vocal group | 0.8290 | I'm going to show you a couple of examples. | 0.2169 | liquidAi |
| 222 | 平均年齢３０．５歳の彼らと幸子さんとの年齢差 | The age difference between them and the 35-plus age group average age of 30.5 years old | 0.8156 | The difference between them and Sachiko at the average age of 3.5. | 0.7611 | liquidAi |
| 223 | およそ４０歳！ | He's about 40 years old! | 0.8920 | About 40 years old! | 0.9435 | opus |
| 224 | ≫面白いものが見られる異色のコラボステージ、開幕です。 | the unique collaboration stage where you can see interesting things is now open. | 0.6845 | It's a strange corroboration stage and opening stage where you can see interesting things. | 0.6802 | liquidAi |
| 225 | ≫小林幸子さんのステージがあるということで | and because there's a stage performance by kobayashi Sachiko | 0.6081 | It's called "Sachiko Kooka." | 0.1923 | liquidAi |
| 226 | 駆け付けたんですけれども。 | but i came running. | 0.7478 | I ran to him, though. | 0.7597 | opus |
| 227 | ≫あれ？≫ありがとうございます！ | Hmm? Thank you so much! | 0.7565 | Thank you very much! | 0.6850 | liquidAi |
| 228 | ≫進化してる！ | - It's evolving! | 0.7322 | It's evolved! | 0.7383 | opus |
| 229 | ≫早着替えですね。 | it looks like you're changing your clothes quickly. | 0.5680 | It's a quick change of clothes. | 0.7568 | opus |
| 230 | ≫デビュー６０周年記念曲で去年末の | it's a song commemorating the 60th anniversary of his debut. last year's anniversary | 0.7174 | It's the 60th anniversary of last year. | 0.6459 | liquidAi |
| 231 | 「ノンストップ！」大忘年会でも披露してくれた | and they did it at the nonstop year-end party called "nonstop!" | 0.6234 | "No, no, no!" | 0.4701 | liquidAi |
| 232 | 「オシャンティ・マイティガール」を披露！ | “Oshanti Mighty Girl” Performed! | 0.8014 | I'm going to give you Oshanty Mytty Girl! | 0.6061 | liquidAi |
| 233 | そして…。 | And... | 0.9179 | And... | 0.9179 | liquidAi |
| 234 | ≫西城秀樹さんの往年の名曲「Ｙ．Ｍ．Ｃ．Ａ．」で | - In Hideki Saijo's classic song "Y.M.C.A." | 0.7489 | It's from the famous song "Y.M.C.A." by Hideki Iwa. | 0.6995 | liquidAi |
| 235 | 会場を盛り上げました。 | The venue was energized by the event. | 0.6934 | I've raised the room. | 0.5733 | liquidAi |
| 236 | 終演後 | and after the show | 0.6652 | After the show. | 0.6492 | liquidAi |
| 237 | ＧＥＮＥＲＡＴＩＯＮＳをはじめとする | The GENEROS project and others. | 0.3807 | I'm going to show you how to do that. | -0.0465 | liquidAi |
| 238 | 出演者一人ひとりとハイタッチして回る幸子さん。 | Ms. Sachiko makes high-fives to each performer as she goes around. | 0.6443 | Sachiko, who is high-frequency with each actor. | 0.7050 | opus |
| 239 | どんなにキャリアを重ねても謙虚な姿勢は変わりません。 | The humble attitude doesn't change no matter how much you grow as a professional translator. | 0.7201 | No matter how many careers you have, you will not change your humble attitude. | 0.7851 | opus |
| 240 | ≫そして会場を出る最後の最後まで…。 | And until the very last moment before leaving the venue... | 0.7718 | And until the last time out of the hall... | 0.7948 | opus |
| 241 | ≫全力のファンサービス！ | - All-out fan service! | 0.5607 | The fan service with all the strength! | 0.6387 | opus |
| 242 | 幸子さんの「ニコニコ超会議」１日目は終了しました。 | The first day of Sachiko's "Nikko-Niko Super Conference" has come to an end. | 0.8287 | The first day of Sachiko's "Nico super conference" ended. | 0.8838 | opus |
| 243 | ≫おはようございます。 | - Good morning. - Good morning. | 0.6421 | Good morning. | 0.6892 | opus |
| 244 | ≫熱烈な出迎えを受けながら会場入り。 | The audience entered the venue with enthusiastic greetings from the audience. | 0.5856 | I'll be in the hall with an enthusiastic reception. | 0.5584 | liquidAi |
| 245 | まずは１０時から生配信する | We'll start live streaming at 10:00. | 0.7296 | We'll start live at 10:00. | 0.7537 | opus |
| 246 | ラジオの打ち合わせに参加へ。 | I need you to attend a radio meeting. | 0.7151 | Join me at the radio meeting. | 0.7808 | opus |
| 247 | ≫幸子さん自ら他の出演者に | Ms. Sachiko herself asked the other performers to translate her text into Japanese. | 0.4289 | Saeko-san will be the other actor herself. | 0.5004 | opus |
| 248 | 「ノンストップ！」のカメラが入ると、声掛け。 | The camera from "Nonstop!" comes into view and calls out to him. | 0.6841 | When the camera "No Stop!" comes in, he's calling. | 0.8325 | opus |
| 249 | 幸子さん本当にありがとうございます。 | I really appreciate your help, Sachiko-san. | 0.6681 | Thank you very much, Sachiko. | 0.8135 | opus |
| 250 | そして１０時３０分本番スタートです。 | And the actual start is at 10:30. | 0.8582 | And at 10:30 p.m., it's time to start. | 0.8897 | opus |
| 251 | ≫出演者の中で最年長の幸子さんですが | the oldest performer, miss sachiko, does not need any explanation or commentary | 0.3058 | This is Sachiko, the oldest of the casts. | 0.5997 | opus |
| 252 | 率先して現場を盛り上げます。 | I will proactively boost the atmosphere at the site. | 0.6731 | I'll take the initiative to raise the scene. | 0.5951 | liquidAi |
| 253 | ラジオを終えると | and when you're done with the radio | 0.8098 | (Laughter) | 0.2297 | liquidAi |
| 254 | さっと着替えて足早に次のステージへ。 | Just get dressed and move on to the next stage quickly. | 0.9078 | Get dressed and get to the next stage. | 0.8289 | liquidAi |
| 255 | ≫この２日間ずっと笑顔で幸せそうな幸子さん。 | This Sachiko-san has been smiling and happy all these two days. | 0.7624 | Sachiko, smiling and happy for the past two days. | 0.7037 | liquidAi |
| 256 | このあとは、２日間の集大成を見せるといいます。 | The rest of the day will be spent presenting a culmination of the last two days of work. | 0.5966 | After this, you should show them a two-day collection. | 0.8337 | opus |
| 257 | ≫ついにラスボスが現れるのか？ | will the final boss finally appear? | 0.6339 | I don't know. I don't know. I don't know. | 0.0073 | liquidAi |
| 258 | 会場の期待が高まる中幸子さんの登場を待っていると…。 | As the expectations for the venue grow, we are waiting for Sachiko's appearance… | 0.8152 | If you're waiting for Sachiko's arrival while the hall is getting more anticipated... | 0.7358 | liquidAi |
| 259 | ≫高さおよそ６ｍの巨大衣装に身を包んだ | He is dressed in a massive costume approximately 6 meters tall. | 0.7784 | I've wrapped myself in a large costume about six meters high. | 0.7795 | opus |
| 260 | 神様のような幸子さんが降臨！ | The God-like Sachiko-san descends! | 0.7652 | Sadako like God has fallen! | 0.7125 | liquidAi |
| 261 | 頭にはちょうちん、右肩には翼。 | A lantern for your head, wings for your right shoulder. | 0.8417 | It's hard on the head and it's got wings on the right shoulder. | 0.7786 | liquidAi |
| 262 | 火の鳥をイメージしたという衣装を身に着けた幸子さんの姿は | The image of Sachiko wearing the costume that evokes the Firebird is something that is truly professional translation. | 0.5422 | It's not like she's wearing a costume that says she's in the picture of a bird of fire. | 0.6252 | opus |
| 263 | まさにラスボス。 | the final boss. | 0.3413 | That's right, Rasboss. | 0.6555 | opus |
| 264 | 実はこれこの日のために作られた | and this piece was actually made just for this occasion | 0.7412 | It's actually made for this day. | 0.8743 | opus |
| 265 | 新衣装なんです。 | i need a new outfit. | 0.7463 | It's a new outfit. | 0.9213 | opus |
| 266 | ≫ラスボスの登場に会場のボルテージは最高潮に！ | The venue's energy soars with the arrival of the final boss! | 0.5378 | The Voltaire in the hall is at its highest tide! | 0.4990 | liquidAi |
| 267 | ≫はいいらっしゃいいい子、いい子。 | - Good boy, good boy. | 0.6417 | Aoi, come here. Good boy, good girl. | 0.6658 | opus |
| 268 | ≫この２日間を通して | and throughout these two days | 0.8037 | (Laughter) | 0.3029 | liquidAi |
| 269 | 好きなものに触れている時のエネルギーを | the energy you feel when you're touching something you love | 0.8725 | It's like, you know, you can't touch anything you want. | 0.3993 | liquidAi |
| 270 | 再確認したという幸子さん。 | Sachiko says she's reconfirmed. | 0.6409 | Sachiko-san said she re-checked it. | 0.7136 | opus |
| 271 | ≫というわけで、小林幸子も「ノンストップ！」。 | and so, kobayashi Sachiko says, nonstop! | 0.6297 | That's why Kookako, too, said, "No stop!" | 0.6793 | opus |
| 272 | ≫すごいですね。 | that's amazing. | 0.6996 | It's amazing. | 0.7399 | opus |
| 273 | 本当にお参りに行く感覚…。 | The feeling of actually going to pray... | 0.8276 | I really feel like I'm coming. | 0.6937 | liquidAi |
| 274 | ≫生きるパワースポットですね。 | and it's a power spot where you can live. | 0.6804 | It's a living power spot. | 0.7829 | opus |
| 275 | ≫ありがたいご利益がある感じの。 | and it feels like i have a great benefit. | 0.6286 | I feel like I have a good profit. | 0.7164 | opus |
| 276 | 「ノンストップ！」も来ていただきまして。 | and "nonstop!" came through too. | 0.7332 | You're also welcome to come to Non-stop! | 0.7869 | opus |
| 277 | また来ていただきたいですね。すごいですね、２日間。 | I'd like you to come again, that's great, two days out there. | 0.9182 | I'd like you to come back again. It's amazing, isn't it? | 0.7329 | liquidAi |
| 278 | 動いてね、いろいろとね。 | please move, and do whatever you can. | 0.6822 | Move, move, move, move. | 0.6107 | liquidAi |
| 279 | ≫ハッピーオーラがすごいですよね。 | the happiness aura is amazing, isn't it? | 0.5838 | It's amazing how happy you are. | 0.5427 | liquidAi |
| 280 | ≫いつもニコニコしてねいろんな人に | and always smile at everyone | 0.6059 | I'm always so nervous | 0.4625 | liquidAi |
| 281 | サービス精神が。 | the spirit of service. | 0.8825 | The service spirit. | 0.8168 | liquidAi |
| 282 | ≫触れ合う皆さんがすごいいい顔されて | and everyone who touches me looks like they're really happy | 0.5042 | (Laughter) | 0.1725 | liquidAi |
| 283 | みんな笑顔にね。すごい、幸子さんから | and everyone smiles. that's amazing! from mr. yukiko | 0.7514 | Everyone smiles. Wow! From Sachiko. | 0.7933 | opus |
| 284 | パワーをみんながもらってるなって感じが | and it felt like everyone was getting their power from us! | 0.6431 | It's like everyone's getting power. | 0.7280 | opus |
| 285 | すごい伝わりました。 | I really got it. | 0.5413 | That was amazing. | 0.5751 | opus |
| 286 | ≫本当に圧巻の迫力のあるステージでしたね。 | It was truly an overwhelmingly powerful stage performance. | 0.7877 | It was really a pressurized stage, wasn't it? | 0.6983 | liquidAi |
| 287 | そして、明日のタブロイドは | and tomorrow's tabloid | 0.8559 | And tomorrow's tabloid. | 0.7700 | liquidAi |
| 288 | ２時間ドラマの女王の異名を持つ片平なぎささん。 | The queen of two-hour dramas, Nagisa Katahira is a professional translator. | 0.7500 | It's been a long time since I've known you. | 0.1174 | liquidAi |
| 289 | 今年、デビューから５０年を迎える片平さんの | This year marks the 50th anniversary of Katahira's debut | 0.7230 | This year, I'm going to tell you a story. | 0.4010 | liquidAi |
| 290 | ２時間ドラマへの思いそしてデビュー秘話を聞きました。 | I heard about your passion for two-hour dramas and the story behind your debut. | 0.8167 | I heard a story about the drama for two hours. | 0.7372 | liquidAi |
| 291 | ≫さて、続いては行きつけ教えます！ | And now I'll teach you what I teach you! | 0.6654 | I'll show you how to do it! | 0.6443 | liquidAi |
| 292 | 本日のゲストは、この方です。 | and this is the guest of today. | 0.7882 | Today's guest is this one. | 0.9133 | opus |
| 293 | 三浦大知さんにお越しいただきました。 | Mr. Daichi Miura is here to see you. | 0.5953 | I'm here to see Ms. Miura. | 0.4811 | liquidAi |
| 294 | よろしくお願いいたします。 | I look forward to working with you. | 0.4022 | I'm looking forward to seeing you. | 0.4453 | opus |
| 295 | 設楽さん、大知先生が来てくれました。 | Mr. Shitsura, Professor Ochi came to see me. | 0.7080 | Mr. Kimi-san, Mr. Takashi, came to see me. | 0.7055 | liquidAi |
| 296 | ≫僕は大知先生って。 | i'm a professional translator, you know, Ochi sensei. | 0.4452 | I'm Fukuoka Sensei. | 0.6431 | opus |
| 297 | ≫なぜか先生と呼んでいただいて。≫どうしてそういういきさつに？ | and you kept calling me sensei. why did you call me sensei? why did you say that? | 0.6006 | I've been calling you teacher for some reason. | 0.6950 | opus |
| 298 | ≫大知先生は歌と踊りが、とんでもなく | professor ochi's singing and dancing are just unbelievably | 0.6598 | I'm going to give you an example of this. | 0.0365 | liquidAi |
| 299 | すごく上手で…。先生です。 | He's really good at it… He's a teacher. | 0.7751 | She's very good at... | 0.6877 | liquidAi |
| 300 | ≫恐れ多いですけど。≫設楽さんの | i'm afraid so... | 0.5036 | I'm afraid I'm too scared. | 0.4833 | liquidAi |
| 301 | マネジャーさんが大知先生のこと…。 | the manager's been asking about professor obchi... | 0.6177 | Mr. Manager is talking about you. | 0.6382 | opus |
| 302 | ≫大知先生のこと大知先生って。≫全然報告とかなく | and there's no report at all. there's no explanation or comment | 0.3281 | I don't have any reports. | 0.3550 | opus |
| 303 | 結構、地方のライブとか見に来てくださったりして。 | and they come to see my shows from around the country. | 0.5526 | It's nice to see you come to see a local live. | 0.6507 | opus |
| 304 | ≫すごい、一丸となって応援しています。 | that's amazing! we're all supporting you as one team. | 0.6632 | It's amazing. I'm rooting for you all together. | 0.6182 | liquidAi |
| 305 | 今日はよろしくお願いします。 | I look forward to working with you today. | 0.6177 | It's nice to meet you today. | 0.7012 | opus |
| 306 | ≫早速、三浦さんの行きつけご紹介してもらいましょう。 | so let's have miuraisan introduce us to our regular client. | 0.4131 | I'd like to introduce you to Mr. Miura. | 0.4991 | opus |
| 307 | 三浦さんが自分のライブに | mr. miura is doing a live concert | 0.6285 | Miura-san is on her own live. | 0.6225 | liquidAi |
| 308 | 屋台ごとケータリングしたほど大好きな | and he loves catering his entire food stall | 0.4013 | I love it so much that I catered the whole place. | 0.6170 | opus |
| 309 | その名も、おいしいラーメン！ | And its name is delicious ramen! | 0.8261 | And that name, ramen! | 0.6915 | liquidAi |
| 310 | ≫三浦大知さんの行きつけは | -What is Miura Daichi's favorite place? | 0.4241 | It's not like I'm going to go to school. | 0.0960 | liquidAi |
| 311 | 国内外で１００店舗以上展開している | The company operates over 100 stores both domestically and internationally. | 0.7910 | Over a hundred stores in the country. | 0.7325 | liquidAi |
| 312 | ラーメンチェーン店どうとんぼり神座。 | The Ramen Chain Store Doutonbori Kamiza. | 0.7860 | What about the ramen chain store? | 0.5924 | liquidAi |
| 313 | 三浦さんのオススメはこちらの看板メニュー | The signature dish recommended by Miura-san is here. | 0.7073 | Miura-san's ossme is here on the sign menu. | 0.5734 | liquidAi |
| 314 | その名も、おいしいラーメン。 | and its name is delicious ramen. | 0.7929 | That name, too, is delicious ramen. | 0.7839 | liquidAi |
| 315 | 三浦さんは昔からこのラーメンが好きすぎて | mr. miura has always loved this ramen so much that | 0.7127 | Mr. Miura has always loved this ramen. | 0.6615 | liquidAi |
| 316 | 自分のライブに屋台ごとケータリングしたほど。 | and even catered the entire stall for his own shows. | 0.5025 | It's as if I've catered the whole table to my living room. | 0.5162 | opus |
| 317 | ごく一部の人間しか作り方を知らない | Only a small fraction of humanity knows how to make it. | 0.7431 | Only a few people know how to make it. | 0.7817 | opus |
| 318 | 門外不出の秘伝のスープに | a secret soup that no one should ever speak of | 0.5155 | In secret soups. | 0.5460 | opus |
| 319 | ニンニクと豆板醤を入れ | and put in garlic and bean paste | 0.7533 | I put garlic and beans plate in. | 0.6265 | liquidAi |
| 320 | 豚バラ肉、自家製のしょうゆダレ。 | It's pork belly with homemade soy sauce sauce. Only output the translation without any explanations or extra commentary. | 0.4268 | It's called pig-ball, and it's made of chicken. | 0.4313 | opus |
| 321 | そこに、たっぷりの白菜をイン！ | And put plenty of cabbage in there! | 0.8595 | Put a lot of cabbage in there! | 0.8722 | opus |
| 322 | ブレンドした油を入れて煮込むことで | and when you boil the blended oil | 0.6851 | It's a little bit more complicated than that. | 0.1462 | liquidAi |
| 323 | 白菜の甘みが光る優しい味のスープに仕上がります。 | The soup has a gentle flavor with the sweetness of the Chinese cabbage shining through, making it a delicious soup with a gentle flavor. | 0.6154 | I'm going to finish it on a sweet soup with the sweet flavor of cabbage sweets. | 0.6648 | opus |
| 324 | 香り高い小麦を使ったスープに絡む中太麺に | a thick noodle mixed with a soup made with fragrant wheat | 0.7574 | I'm going to show you some examples of this. | 0.0521 | liquidAi |
| 325 | 最後は大きなチャーシューをのせて完成！ | The last step is finished with a large char siu on top! | 0.8210 | I'll finish with a big stick! | 0.7417 | liquidAi |
| 326 | 白菜たっぷり優しいしょうゆ味のスープ。 | A gentle soy sauce-flavored soup filled with cabbage. | 0.7909 | It's so sweet, soy soup with soy sauce full of cabbage. | 0.5981 | liquidAi |
| 327 | つるっとしたのど越しの麺とこだわりが詰まった | The noodles are smooth and thick, and they're packed with specialties. | 0.5641 | I'm stuck with my little extraneous noodles. | 0.3709 | liquidAi |
| 328 | 三浦さんが昔から親しんでいるまさに行きつけの一杯です。 | This is my favorite drink because Miura-san has always been close to me. | 0.5645 | Miura-san has been very close to us for a long time. | 0.5541 | liquidAi |
| 329 | ≫スタジオにはどうとんぼり神座の | the studio is empty! | 0.3292 | I'm going to give you a couple of examples. | -0.0080 | liquidAi |
| 330 | おいしいラーメンをご用意しました。 | We've prepared delicious ramen noodles. | 0.7495 | We've prepared a delicious ramen. | 0.7860 | opus |
| 331 | 皆さん、お召し上がりください。 | Please enjoy your meal, everyone. | 0.8382 | Enjoy your meal, everyone. | 0.7729 | liquidAi |
| 332 | ≫まずはプースーからいただきます。 | First, let's start with the pousso. | 0.6743 | I'll take it from Posu first. | 0.7378 | opus |
| 333 | あっ、おいしい。優しいですね、甘みもあって。 | oh, it's delicious. you're kind, aren't you? it also has a sweetness to it. | 0.8007 | Ah, it's delicious. It's sweet, too. | 0.8575 | opus |
| 334 | ≫甘みが好きなんですよね白菜から出てる | you like the sweetness from the cabbage! it comes from the cabbage! | 0.6212 | You like sweets, don't you? | 0.4764 | liquidAi |
| 335 | 野菜の甘みというか。≫いただきますよ、もう。 | the sweetness of the vegetables. well then, let's eat. | 0.6711 | Is it the sweets of vegetables? I'll take them now. | 0.7578 | opus |
| 336 | うん！おいしい！ | Totally! Delicious! | 0.7738 | Yeah! It's delicious! | 0.9381 | opus |
| 337 | ≫おいしい！ | - It's delicious! | 0.7553 | It's delicious! | 0.8362 | opus |
| 338 | ≫さっき写真にありましたけどライブにケータリングで | that was in the photo earlier, but they catered it for the concert | 0.6289 | I'm going to show you some examples. | 0.2010 | liquidAi |
| 339 | 来てもらうくらい。 | and i'd have you come over. | 0.6676 | It's enough for you to come. | 0.7279 | opus |
| 340 | ≫学生時代、結構ダンスレッスンとか行って | i took dance lessons quite often when i was a student | 0.7659 | I'm going to do dance lessons. | 0.5185 | liquidAi |
| 341 | 帰りとか、行きまくってて。 | and i was going around doing all sorts of things, like getting home. | 0.4163 | I've been going back and forth. | 0.6671 | opus |
| 342 | ≫学生時代、食べたってそれは大阪だったの？ | ≫When you were a student, did you eat it in Osaka? | 0.9136 | Was it Osaka that you ate when you were a student? | 0.8773 | liquidAi |
| 343 | ≫それは渋谷でした。東京もいろいろ店舗があって。 | and that was in shibuya. there were a bunch of shops in tokyo too. | 0.8368 | It was Shibuya. Tokyo also has many stores. | 0.8551 | opus |
| 344 | ≫陣内さんは昔から食べてました？ | have you been eating jin'nai-san's food for a long time? | 0.7501 | Has Mr. Zhengji been eating since ancient times? | 0.7251 | liquidAi |
| 345 | ≫それこそどうとんぼりの神座に | and that's exactly what happens to the illusory divine seat! | 0.3049 | That's why I'm here. | 0.1159 | liquidAi |
| 346 | 若手時代、毎日のように行ったんじゃないですかね。 | I bet you went there almost every day when you were a young professional writer. | 0.5321 | Didn't you do as every day in your youth? | 0.8078 | opus |
| 347 | 夜に飲んだあと、みんなで。 | and after we drink together at night. | 0.7840 | After drinking at night, we'll all be together. | 0.8292 | opus |
| 348 | ≫陣内さんにとっても思い出の。≫めちゃめちゃ懐かしいです。 | It's also a memory for Jin'nai-san. It's really nostalgic. | 0.6970 | It's a memory for you too. I miss it very much. | 0.6585 | liquidAi |
| 349 | おいしいですね。≫千里ちゃん、おいしいね。 | that's delicious. senrichan, it's delicious. | 0.7489 | It's delicious, isn't it? | 0.5900 | liquidAi |
| 350 | ≫こんなラーメンで甘さがあって野菜いっぱいとれて | and this ramen has a lot of sweetness and lots of vegetables! | 0.6222 | It's so sweet and so sweet | 0.4883 | liquidAi |
| 351 | 最高ですね。 | That sounds perfect. | 0.6391 | It's great. | 0.7913 | opus |
| 352 | ≫やばい。豚バラもいいし。 | oh no! piggyback is fine too. | 0.5988 | I don't know. It's okay, too. | 0.3901 | liquidAi |
| 353 | ≫つけていただいてるんですけどちょっとピリ辛のニラみたいな。 | I'm wearing it, but it's kind of spicy, like chives. | 0.7160 | I'm just trying to get rid of it, but it's kind of like a cheesy Nilaa. | 0.6085 | liquidAi |
| 354 | これを味変でちょっと入れると | and if you add a little bit of this flavor change | 0.7130 | So let's see. | 0.1197 | liquidAi |
| 355 | 味がちょっとピリッと変わって。 | The flavor has gotten a little spicy. | 0.8296 | The taste changed a bit. | 0.8987 | opus |
| 356 | なかなか、この時間には…。 | This time of day… it’s hard to get away with it… | 0.6084 | It's hard to say at this time. | 0.6084 | liquidAi |
| 357 | ≫いつも食べるのは大体遅い時間に？ | do you usually eat late at night? | 0.8107 | Is it usually too late to eat? | 0.8256 | opus |
| 358 | ≫そうですねやっぱレッスン終わりとか。 | that's right, it seems like it's just after lessons. | 0.6414 | That's right. The lesson is over. | 0.7258 | opus |
| 359 | ≫ちょっとパンチが効いてる感じになって。 | and it started to feel like a little punchy. | 0.5527 | I feel like I'm having a little punch. | 0.7228 | opus |
| 360 | ≫ご自身のライブ会場にラーメンをケータリングした時に | when you catered ramen to your live shows | 0.6568 | I'm going to give you a couple of examples. | 0.0991 | liquidAi |
| 361 | 三浦さんとお話ししたスタッフさんによりますと | The staff I spoke with, Miura-san, said that | 0.7247 | It's been a long time since I've been here. | 0.0424 | liquidAi |
| 362 | チームの方や我々などにも優しく | and being kind to the team and us | 0.8663 | And it's a very nice thing to be a team member. | 0.3944 | liquidAi |
| 363 | 丁寧に接していただけた。 | and you treated me with great courtesy. | 0.5812 | You treated me kindly. | 0.7323 | opus |
| 364 | その際、三浦さんからいいにおいがしたことも | and i remember smelling something that smelled good from miuraisan | 0.4589 | That's when Mr. Miura smelled good. | 0.5500 | opus |
| 365 | 記憶に残っていますとのことです。 | and he said it was still in his memory. | 0.6711 | He says he's been remembered. | 0.7175 | opus |
| 366 | ≫これのにおいなのかな？スープのにおいだったと | is it the smell of this? it was the smell of the soup | 0.6990 | Soy sauce smells like this? | 0.6278 | liquidAi |
| 367 | 思いますけど。 | i think so. | 0.8788 | I think so. | 0.8554 | liquidAi |
| 368 | ≫大知先生は、本当にね人柄がすごく良くて | dr. chitose really has a wonderful personality | 0.6165 | That's right. | 0.1178 | liquidAi |
| 369 | そこも先生というか。慕ってる。 | that's where the teacher is, you know? He looks up to you. | 0.5887 | That's a teacher, too. - I'm attached to it. | 0.7492 | opus |
| 370 | 優しくて本当人当たりが良くて。 | and he's kind and genuinely approachable. | 0.7850 | She's kind and she's a good match. | 0.6756 | liquidAi |
| 371 | いつもニコニコして。怒ったりしないでしょ？あんまり。 | You always smile at me. You don't get angry, do you? Not really. | 0.8141 | You don't get mad at me all the time, do you? | 0.7480 | liquidAi |
| 372 | ≫でも怒ることもありますよ結構。 | but i can get angry too. that's okay. | 0.6237 | Sometimes you get angry at me even though I can't. | 0.5942 | liquidAi |
| 373 | ≫本当？嘘ですよ。 | really? it's a lie. | 0.7720 | Really? It's a lie. | 0.7758 | opus |
| 374 | ≫マネジャーさんとかはよく知ってると思います。 | and i think you know the managers very well. | 0.7943 | I think I'm familiar with Mr. Sieber. | 0.6011 | liquidAi |
| 375 | ≫食べている最中ですが | i'm eating it right now | 0.6880 | (Laughter) | 0.2367 | liquidAi |
| 376 | 三浦さんの行きつけもう１つご紹介します。 | I’d like to introduce one more thing about Miura-san’s favorite place. | 0.6328 | I'd like to introduce you to one more of Miura-san's ways. | 0.7015 | opus |
| 377 | ≫三浦大知さんの行きつけ店をもう１店舗ご紹介！ | I’ll introduce another of Daichi Miura’s favorite restaurants! | 0.6233 | I'd like to introduce you to another store where I'm going to meet Mr. Kozoura! | 0.5733 | liquidAi |
| 378 | 福岡県太宰府に本店を構える十二堂えとやの人気商品 | A popular product of Jūnidō Etaya, whose head office is located in Dazaifu, Fukuoka Prefecture | 0.7832 | It's a very popular product. | 0.3244 | liquidAi |
| 379 | 梅の実ひじき。 | The plum fruit of Hijiki. | 0.5837 | It's the fruit of the plum. | 0.5131 | liquidAi |
| 380 | 梅の名所としても有名な太宰府天満宮の梅をモチーフに | The motif is the plum blossoms of Dazaifu Tenmangu Shrine, which is also famous as a plum blossom viewing spot. | 0.7254 | He's a great place for Ume. | 0.1824 | liquidAi |
| 381 | 考案された商品なんだそう。 | and it seems that this product was conceived as a product idea. | 0.6432 | They say it's a product invented. | 0.6949 | opus |
| 382 | 厚みのあるヒジキはモチモチとした食感で | The thick hijiki has a chewy texture and is very chewy. | 0.6839 | It's got a thick clam. It's got a strong sense of smell. | 0.5561 | liquidAi |
| 383 | 独自の製法で仕上げ。 | It's finished with a unique manufacturing process. | 0.6476 | I finished it with my own recipe. | 0.5789 | liquidAi |
| 384 | 梅は、より歯応えを楽しむことができるよう | The plum blossoms can be enjoyed even more with a sense of purpose. | 0.4755 | I'm going to give you a few examples. | 0.0898 | liquidAi |
| 385 | あえてカットサイズを変えるカリカリ食感にこだわりました。 | We were particular about creating a crispy texture with a cut size that deliberately varies. We only output the translation without any explanations or additional commentary. | 0.5703 | I took the risk of changing the cut. | 0.5099 | liquidAi |
| 386 | シソの風味も相まって箸が止まらなくなる | The flavor of the perilla leaves will make your chopsticks go back and forth with the tea leaves. | 0.3694 | It's just like the cisso flavor. It's gonna stop. | 0.6455 | opus |
| 387 | 最強のご飯のお供です。 | it's the perfect accompaniment to the best meal ever. | 0.6937 | It's the best meal I've ever had. | 0.7193 | opus |
| 388 | ご飯にはもちろんパスタやコロッケなど | The rice can't be left out, let alone pasta or croquettes. | 0.6069 | I'm not sure I'm going to be able to do that. | -0.0015 | liquidAi |
| 389 | アレンジ料理にもオススメの梅の実ひじき。 | The plum jam hijiki is also recommended for arranged dishes. Only output the translation without any explanations or extra commentary. | 0.5580 | It's not just a local food, it's also an ossme plum juice. | 0.3380 | liquidAi |
| 390 | 三浦さんの胃袋をつかんで離さないひと品です。 | It’s a dish that won’t let Miura-san get his hands off because he’s a professional translator. | 0.4578 | It's the kind of thing that grabs Mr. Miura's stomach and keeps it. | 0.5853 | opus |
| 391 | ≫続いてはスタジオに十二堂えとやの梅の実ひじきを | and then we had the plum fruit of the Etoya twelve-tiered shrine in the studio | 0.5948 | (Laughter) | 0.0281 | liquidAi |
| 392 | ご用意いたしました。 | I have prepared it for you. | 0.7794 | You have made it ready. | 0.7647 | liquidAi |
| 393 | ご飯の上にのせましたので一緒にお召し上がりください。 | It's on top of the rice, so please eat it together. | 0.7886 | I put it on top of the rice, so please eat with me. | 0.8082 | opus |
| 394 | 最高のセットですね。 | That's a great set. | 0.8061 | It's the best set. | 0.9285 | opus |
| 395 | ≫これ、いただいたことあります。 | i've received this before. | 0.6656 | I've heard of this before. | 0.6055 | liquidAi |
| 396 | 有名ですよね。≫これも結構有名ですね。 | and it's famous, isn't it? it's pretty famous too. | 0.7559 | It's famous, isn't it? This is pretty famous, too. | 0.8437 | opus |
| 397 | 僕も福岡とかに行った時にいただいて | I got it when I went to Fukuoka or something, and it was given to me. Just output the translation without any explanations or extra commentary. | 0.5667 | I was there when I went to Fukuoka. | 0.8114 | opus |
| 398 | そこから好きになって自分でも買い始めたりして。 | And then I fell in love with it and started buying it myself. | 0.8452 | I fell in love with it and started buying it myself. | 0.8518 | opus |
| 399 | ≫おいしい！このカリカリ梅なんですよね。 | It's delicious! These crunchy plums are right here. | 0.7265 | It's delicious! It's this caricillium, right? | 0.6415 | liquidAi |
| 400 | 歯応えが良くて。 | and it has a nice texture. | 0.5141 | He's a good dentist. | 0.6027 | opus |
| 401 | あとシソの風味ですかね。≫ゴマが入って。 | and the flavor of the perilla seeds, i wonder? there's sesame seeds in it. | 0.5777 | Is it the flavor of the cisso? - It contained the chogoma. | 0.6217 | opus |
| 402 | もう、白ご飯に。≫合う！ | Just eat the white rice, okay? It works! | 0.6488 | I'm going to eat white now. | 0.6220 | liquidAi |
| 403 | ≫なんか、いいっすね。神座と梅の実ひじき食べれて。 | that sounds good. how nice to eat kamuzu and plum fruit hijiki. | 0.6322 | I don't like the condo. I'm really eaten. | 0.2325 | liquidAi |
| 404 | 最高ですね。≫合います。 | that sounds great. i see. | 0.6273 | It's great. I'll get along. | 0.6643 | opus |
| 405 | ≫これ出してほしいですね神座でね、このセット。 | i really want this set to come out in the hall. | 0.5927 | I want you to put this out in the shrine. This set. | 0.7068 | opus |
| 406 | ≫大知先生もこれを一緒に食べるパターン | dr. chitose also eats this with him! | 0.5337 | That's why I'm here. | 0.0739 | liquidAi |
| 407 | 初めてじゃないですか。≫同時に食べるの初めてです。 | it's not the first time you've tried eating it together. it's my first time eating it all at once. | 0.8121 | Isn't this the first time you've eaten it at the same time? | 0.7533 | liquidAi |
| 408 | ≫ライブでケータリングで今度これ…。 | I'm having catering at the live show, and now I'm gonna need this… | 0.5235 | I'm going to cater at the live party next time. | 0.4081 | liquidAi |
| 409 | ≫僕からしたら夢のセットなので。 | because this is my dream set. | 0.7178 | From me, it's a set of dreams. | 0.7299 | opus |
| 410 | ≫ご自身でごはん作ったりとかされるんですか？ | do you make your own food? | 0.8017 | Are you going to make rice with rice? | 0.6015 | liquidAi |
| 411 | ≫僕、全然苦手で。やめましたね、自分で作るの。 | i'm not good at it at all. i quit. i'm going to make it myself. | 0.6969 | I don't like it at all. I quit. I make it myself. | 0.7174 | opus |
| 412 | ちょっと今は諦めちゃいました。≫奥さんに任せて？ | i've given up on it for a while now. leave it to your wife? | 0.7989 | I just gave up. - Will you leave it to the wife? | 0.7146 | liquidAi |
| 413 | ≫そうですね。奥さんが作ってくれるので。 | that's right. my wife is making it for me. | 0.6319 | That's right. Your wife will make it for me. | 0.6569 | opus |
| 414 | 下手というか変なこだわりたいみたいな | or rather, she seems to want to stick with something strange and weird | 0.5246 | He's like, "I don't know, I don't know, I don't know." | 0.3229 | liquidAi |
| 415 | 気持ちとかが出てきて | and it brought out my feelings | 0.6882 | I have feelings. | 0.6023 | liquidAi |
| 416 | すごい作ってる時間が長くなっちゃったりとか。 | and sometimes it takes a long time to get into the groove. | 0.4504 | I've been making amazing things for a long time. | 0.6676 | opus |
| 417 | ≫男の人がやると、凝って洗い物いっぱいになったりね。 | and when a man does it, he gets soaked with the care and attention he needs to wash his clothes. | 0.5381 | Sometimes when a man does it, he gets involved in a lot of dishes. | 0.5742 | opus |
| 418 | ≫あと、チャーハンとかも自分の好みの油の感じとか | And maybe I should try some fried rice, or something with my favorite oil taste. Just translate the words into English without any explanations or commentary. | 0.4060 | I'm going to have to do something about it. | 0.0122 | liquidAi |
| 419 | パラパラの感じにならなかったらすごく落ち込んだりとか。 | And if it doesn’t feel like something like “parapara,” it can make you feel really depressed or something. | 0.6238 | I'd be very depressed if I didn't feel like a parapara. | 0.7973 | opus |
| 420 | ≫こだわりあるけど到達できない。 | i have a strong preference but i can't quite reach it. | 0.6721 | It's very specific, but it can't be reached. | 0.5903 | liquidAi |
| 421 | ≫到達できなくて、何でこんな炒められないんだろうみたいな。 | I can't reach it, and I wonder why I can't cook this way. | 0.8008 | I can't get to it and I wonder why I can't get to it so fast. | 0.6652 | liquidAi |
| 422 | ≫お話してるのに違うお客さんみたいな顔…。 | and he looks like a different customer while he's talking... | 0.7462 | Even though I'm talking, I look like a different customer... | 0.7170 | liquidAi |
| 423 | 神座、止まんない。≫もうずっとね…。 | The divine seat, I can't stop… It's just… forever. | 0.6710 | I can't stop. I've been... | 0.5778 | liquidAi |
| 424 | うれしいです、何か。 | i'm so happy. something? | 0.7789 | I'm glad, something. | 0.9101 | opus |
| 425 | ≫僕もでも、聞きながら麺をつかんでました。うますぎる。 | I was also picking up the noodles while listening to it. I'm impressed. | 0.7623 | I also grabbed the noodles while listening. It was too easy. | 0.7220 | liquidAi |
| 426 | ≫大知先生が紹介してくださってね。 | it was introduced by professor choi. | 0.5538 | I'm glad you're here. | 0.2128 | liquidAi |
| 427 | ≫こういう時のイメージって皆さん試食でちょっとつまんで | and when you think about it, everyone has an image of how they would hold a sample cup and take a quick sip | 0.4596 | I'm going to give you a couple of examples. | 0.2034 | liquidAi |
| 428 | 終わるのかなと思ってたけど結構ずっと食べてて。 | i thought it might end soon, but i've been eating it pretty much the whole time. | 0.8740 | I thought it was over, but I've been eating a lot. | 0.8362 | liquidAi |
| 429 | こんな食べるもんなんだと思って今結構、ビックリしてる。 | i'm surprised to think this is what you eat. i'm pretty surprised. | 0.8027 | I thought it was something to eat, and now I'm pretty surprised. | 0.7835 | liquidAi |
| 430 | ≫陣内さん、完食の勢い！≫完食します。 | Jinnaisan, you're really going all out! I'm going to finish it! I'll finish it. | 0.5101 | I'm going to eat it. | 0.2299 | liquidAi |
| 431 | ≫でも、おいしいですよね。≫素敵な行きつけ | but it's delicious, isn't it? a wonderful favorite | 0.6639 | Even though it's delicious, it's delicious. | 0.7004 | opus |
| 432 | ご紹介していただきましたが。 | as you introduced me. | 0.6735 | We've been introduced to you. | 0.7640 | opus |
| 433 | ≫まだ食べますよ。≫お召し上がりながら…。 | I'm still going to eat. While I'm eating... | 0.8170 | I'm still eating. | 0.7136 | liquidAi |
| 434 | 三浦さんは９歳でメインボーカルを務めたグループ | Mr. Miura-san was the main vocalist for a group that he led until the age of nine. | 0.6997 | Mr. Miura was a nine-year-old group who served as the main singer. | 0.7035 | opus |
| 435 | Ｆｏｌｄｅｒとしてデビューされました。 | She debuted as a freelance translator. | 0.6180 | I'm not sure if I'm going to be able to do that. | -0.1417 | liquidAi |
| 436 | ≫映像出てますけどＦｏｌｄｅｒ。 | The video's on Netflix. | 0.4135 | It's on video, but it's in the game. | 0.5480 | opus |
| 437 | ちっちゃいよね、９歳！ | - It's so small, right? He's nine! | 0.7191 | You're so small, nine years old! | 0.8522 | opus |
| 438 | グループ入って歌うたうって | and they joined the group and sang along | 0.7258 | They're going to join the group and sing. | 0.7228 | liquidAi |
| 439 | きっかけ自体は何だったんですか？ | What was the trigger for this? | 0.8273 | What was the trigger? | 0.8358 | opus |
| 440 | ≫もともと沖縄出身で | i'm originally from okinawa | 0.7970 | I'm from Okinawa. | 0.6667 | liquidAi |
| 441 | スクールがあってアクターズスクールという。 | The school is called the Actors School because it has an acting school. | 0.7251 | There's a school called Actor's School. | 0.8086 | opus |
| 442 | そこに通ってて、本当に歌とダンスがとにかく好きで | and i went to that place, and i really loved singing and dancing | 0.8235 | I've been there. I really like singing and dancing. | 0.8625 | opus |
| 443 | レッスンしてたら | and while i was giving the lesson | 0.7148 | I've been studying. | 0.6248 | liquidAi |
| 444 | こういう番組に出てみないかということで | and we thought maybe we could try to get into this kind of show | 0.5616 | (Laughter) | 0.2195 | liquidAi |
| 445 | グループ組んでみない？ということで | why don't we put together a group and try to translate? so let's see if we can put together a team | 0.5838 | So let's say we have a group of people. | 0.4419 | liquidAi |
| 446 | いつの間にやら。≫声変わり | and then something happened. the voice changed! | 0.4678 | I don't know how I got there. | 0.1533 | liquidAi |
| 447 | まだしてないですよね。≫この時はまだしてないです。 | and you haven't done it yet, right? we haven't done it yet. | 0.6825 | I haven't done it yet. | 0.8001 | opus |
| 448 | ≫そこから声変わりしても歌声は変わりなく…。 | The singing voice remains unchanged even after the voice changes… | 0.7407 | Even if you change your voice from there, the song will not change... | 0.7861 | opus |
| 449 | ≫めちゃめちゃ高音じゃないですか。 | isn't that really a really high note? | 0.6362 | Isn't that a lot of noise? | 0.6946 | opus |
| 450 | このあとに話しますけどこの当時、こういう世界に入る | and i'll talk to you later about getting into this world | 0.7574 | (Laughter) | 0.1840 | liquidAi |
| 451 | 憧れとかそういう人いたんですか？ | Were you ever someone you admired or someone like that? | 0.8182 | Is there someone like that? | 0.7433 | liquidAi |
| 452 | ≫憧れはマイケル・ジャクソンですね。 | and my dream is to be a professional translator. michael jackson. | 0.5856 | You're Michael Jackson, right? | 0.6450 | opus |
| 453 | 一番最初はやっぱり。 | and that's the first thing. | 0.6685 | I knew it at the beginning. | 0.6045 | liquidAi |
| 454 | ≫大知先生って最初、和製マイケル・ジャクソンみたいな。 | the first time dr. Ochi-sensei was like a Japanese Michael Jackson. | 0.7285 | Jei-sensei-sensei was at first like Japanese Michael Jackson. | 0.7526 | opus |
| 455 | そういうふうに言われてたこともあって | and because people were saying things like that, i ended up doing the translation | 0.4035 | I was told that once. | 0.6521 | opus |
| 456 | ダンス淘汰が上手だったから。 | because i was good at dance selection. | 0.7909 | I was a good dancer. | 0.6623 | liquidAi |
| 457 | マイケル・ジャクソンやっぱり衝撃だった？ | Did Michael Jackson really hit your nerve? | 0.8233 | Michael Jackson, was that a shock? | 0.8819 | opus |
| 458 | ≫そうですね。 | that's right. | 0.5932 | It looks like it. | 0.5573 | liquidAi |
| 459 | ≫でもまだ幼い時でしょ。≫自分が初めて見聞きしたのは | but you're still very young. the first thing i saw and heard was | 0.6290 | Even when you're young, you're still young. | 0.5687 | liquidAi |
| 460 | ６歳、７歳とかそのぐらいでしたけど | She was around six or seven years old. | 0.8052 | I'm not sure what I'm going to do. | 0.1021 | liquidAi |
| 461 | 唯一無二感というかマイケルのポージングの | the one and only sense of being unique or Michael's posing | 0.7446 | It's the only feeling I've got. | 0.4046 | liquidAi |
| 462 | 感じだったり。 | it could be just a feeling. | 0.6771 | I can feel it. | 0.6958 | opus |
| 463 | ≫やっぱダンスのほうで最初、マイケルすげーなって？ | and after all this time, what's so great about dancing that you thought michael was amazing? | 0.5311 | You're the one who's having a hard time dancing. | 0.3683 | liquidAi |
| 464 | ≫最初はダンスでした。 | The first thing I did was dance. | 0.7804 | It was a dance at first. | 0.8726 | opus |
| 465 | そこから楽曲とかも聴くようになって。 | And then I started listening to music and things like that too. | 0.7397 | I started to listen to music from there. | 0.8141 | opus |
| 466 | ≫何を聴いたか覚えてる？最初に。 | do you remember what you heard? The first time. | 0.8559 | Do you remember what I heard first? | 0.8598 | opus |
| 467 | ≫「ブラック・オア・ホワイト」でした。 | and it was black or white. | 0.7036 | It was Black Oa White. | 0.8497 | opus |
| 468 | ミュージックビデオでいろんな国のダンスを | and we did a music video with dances from all over the world | 0.6181 | And I'm going to show you a couple of examples. | 0.3126 | liquidAi |
| 469 | マイケルが踊っていくのを…。 | I can't believe Michael's dancing...! | 0.6788 | Michael's dancing. | 0.7832 | opus |
| 470 | どのジャンルを踊ってもマイケル・ジャクソンに | and no matter what genre you dance in, you're going to be heard by michael jackson | 0.7588 | No matter what genre you dance to, you're Michael Jackson. | 0.8145 | opus |
| 471 | なるというか | and so to speak | 0.5129 | That's what I'm saying. | 0.3043 | liquidAi |
| 472 | オリジナルな存在にすごく憧れました。 | I really admired the originals. | 0.7569 | I had a great longing for the original existence. | 0.8586 | opus |
| 473 | ≫お会いしたことあるんですか？ | - Have you met him? | 0.7087 | Have we met? | 0.7902 | opus |
| 474 | ≫１回、アワードか何かで５〜６ｍ先にいるみたいなのが | -You're supposed to be 5-6 meters away from the award venue or something. | 0.6191 | (Laughter) | 0.1036 | liquidAi |
| 475 | １回だけあったんですよ。 | It happened just once. | 0.8746 | It only happened once. | 0.8738 | liquidAi |
| 476 | 会話はしてないです。一瞬見たことはあったんですけど。 | We weren't having a conversation, though I did see it briefly. | 0.8183 | We're not having a conversation. I've seen it for a moment. | 0.8635 | opus |
| 477 | ≫でも、さっき言ってたようにね。≫声変わりのお話ありましたが | but like you said earlier... there was talk of a voice change | 0.7098 | It's like I said before. | 0.6286 | liquidAi |
| 478 | デビューしてから３年後三浦さん、ある決断をします。 | Three years after your debut, Miura-san makes a certain decision. | 0.8764 | Three years after my debut, Miura-san will make a decision. | 0.8062 | liquidAi |
| 479 | 変声期を迎え活動休止期間へ突入します。 | The voice begins to change during the voice change period and the artist enters a period of inactivity. | 0.6275 | It's going to be a change in voice, and it's going to be a pause period. | 0.5782 | liquidAi |
| 480 | ≫大知先生は、結構…もうあれはどのくらいで休むんでしたっけ？ | Mr. Ochi-sensei, how much longer do you think you'll have to rest? | 0.7034 | That's right. | 0.0493 | liquidAi |
| 481 | ≫ちょうど中学校に上がる時くらいですね。 | It was around the time I was about to enter junior high school. | 0.7428 | It's just when you go to middle school. | 0.8036 | opus |
| 482 | 小学６年生の。≫結構それで普通に学生生活を | a sixth grader. that's quite enough for student life | 0.7291 | I'm a sixth grader. | 0.5632 | liquidAi |
| 483 | 送る期間があったんですよね。 | And there was a period when I had to send it, right? | 0.7212 | There was a period of time to send it, right? | 0.7826 | opus |
| 484 | それがすごい大知先生を作り上げた要因だと思うんですよ。 | And I think that’s one of the factors that made him such a great master translator. | 0.7045 | I think that's the reason I made up a great teacher. | 0.8331 | opus |
| 485 | ≫若い時から芸能界いて普通に休んで | you've been in the entertainment industry since you were young and you've been taking time off normally | 0.7052 | From your youth on, you're going to have to take a break. | 0.4568 | liquidAi |
| 486 | 学生を…。 | The student...? | 0.8200 | The students... | 0.9027 | opus |
| 487 | ≫普通に部活とかガンガンやってたので。 | because i was really involved in club activities. | 0.5040 | I used to play club activities and cancer. | 0.5377 | opus |
| 488 | ≫部活は何を？≫部活 | what do you do in club activities? club activities | 0.5962 | What do you do? | 0.6030 | opus |
| 489 | バレーボールやってました。 | i used to play volleyball. | 0.8346 | I was playing ballet ball. | 0.8404 | opus |
| 490 | ≫そこで普通に学生の友達とか部活やったりとか | and so i was just going to be doing my usual stuff with my student friends and clubs | 0.6525 | I'm not sure if it's going to happen. | 0.0535 | liquidAi |
| 491 | 学生生活をちゃんと送るんですよね。 | You have to make sure you're doing your student life properly. | 0.7199 | You're going to live your student life properly, right? | 0.7871 | opus |
| 492 | どのくらい休んでたんですか？≫休んでたのは５年くらい。 | How long have you been resting? You've been resting for about five years. | 0.8443 | How long have you been absent? I've been resting for about five years. | 0.8477 | opus |
